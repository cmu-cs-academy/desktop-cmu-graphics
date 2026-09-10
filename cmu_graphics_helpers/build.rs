//! Copy the Visual C++ runtime DLLs we ship on Windows into OUT_DIR, so that
//! maturin can place them inside the wheel's package directory.
//!
//! cmu_graphics_helpers is C++ (Rust plus Skia), so the built .pyd imports
//! MSVCP140.dll, the C++ standard library. Unlike VCRUNTIME140.dll -- which
//! CPython's own Windows installer drops next to python.exe -- MSVCP140.dll only
//! exists on machines where someone installed the Visual C++ Redistributable. On
//! a fresh Windows machine it is absent, and importing cmu_graphics fails with
//! "ImportError: DLL load failed while importing cmu_graphics_helpers".
//!
//! Shipping the DLLs next to the .pyd fixes that: CPython loads extension modules
//! with LOAD_WITH_ALTERED_SEARCH_PATH, so Windows searches the directory holding
//! the .pyd when resolving its dependencies. (The bundled pygame finds its
//! SDL2.dll the same way.) Keeping them inside the package directory also means
//! build/helpers/build_cmuhelp_modules.py picks them up unchanged when it vendors
//! this wheel into the zip distribution.
//!
//! See [tool.maturin] include in pyproject.toml for the other half of this, and
//! NOTICE_TEXT below for the redistribution terms.

use std::env;
use std::error::Error;
use std::fs;
use std::path::{Path, PathBuf};

/// Anything listed here must be a REDIST file that Microsoft's Visual Studio
/// license terms allow us to redistribute. Do not add DLLs without checking
/// that, and see NOTICE_TEXT below.
///
/// The .pyd itself only imports msvcp140.dll and vcruntime140.dll, but
/// msvcp140.dll in turn imports vcruntime140_1.dll (which holds the x64
/// exception-handling runtime), so all three have to travel together or
/// msvcp140.dll cannot load. tests/check_binaries.py walks these dependencies
/// transitively to keep this list honest.
const DLL_NAMES: [&str; 3] = ["msvcp140.dll", "vcruntime140.dll", "vcruntime140_1.dll"];

/// Redistributing Microsoft's DLLs requires shipping a notice alongside them.
const NOTICE_NAME: &str = "VC_REDIST_NOTICE.txt";

/// The text of the notice. It lives here, rather than in a .txt
/// file, so that it ships only in the wheels that actually carry the DLLs.
const NOTICE_TEXT: &str = r#"===============================================================================
Microsoft Visual C++ Runtime Libraries
===============================================================================
Copyright (c) Microsoft Corporation. All rights reserved.

This application includes redistributable binary files from the Microsoft Visual
C++ Runtime, distributed under the Microsoft Software License Terms for
Microsoft Visual Studio / Microsoft Visual C++ Redistributable package.

This package includes the following files, redistributed unmodified:

    msvcp140.dll
    vcruntime140.dll
    vcruntime140_1.dll

For official Microsoft Visual Studio license terms, see:
https://visualstudio.microsoft.com/license-terms/"#;

/// Directories that may hold a Visual Studio installation.
const PROGRAM_FILES: [&str; 2] = ["C:\\Program Files", "C:\\Program Files (x86)"];

fn children(dir: &Path) -> Vec<PathBuf> {
    let Ok(entries) = fs::read_dir(dir) else {
        return Vec::new();
    };
    let mut paths: Vec<PathBuf> = entries.flatten().map(|entry| entry.path()).collect();
    paths.sort();
    paths
}

/// Every path matching `<parent>/<any dir>/<suffix>`, for the version-numbered
/// directories that Visual Studio installs under.
fn expand_wildcard(parents: &[PathBuf], suffix: &str) -> Vec<PathBuf> {
    let mut out = Vec::new();
    for parent in parents {
        for child in children(parent) {
            let candidate = if suffix.is_empty() { child } else { child.join(suffix) };
            if candidate.is_dir() {
                out.push(candidate);
            }
        }
    }
    out
}

/// Locate the x64 VC++ redistributable directory.
///
/// Inside a Visual Studio developer prompt VCToolsRedistDir is set for us.
/// Otherwise walk the standard install locations, which are laid out as
/// <Program Files>/Microsoft Visual Studio/<year>/<edition>/VC/Redist/MSVC/
/// <toolset version>/x64/Microsoft.VC<nnn>.CRT
fn find_redist_dir() -> Option<PathBuf> {
    if let Ok(env_dir) = env::var("VCToolsRedistDir") {
        let crt_dirs = expand_wildcard(&[PathBuf::from(env_dir).join("x64")], "");
        if let Some(found) = crt_dirs.into_iter().max() {
            return Some(found);
        }
    }

    let roots: Vec<PathBuf> = PROGRAM_FILES
        .iter()
        .map(|dir| Path::new(dir).join("Microsoft Visual Studio"))
        .collect();

    let years = expand_wildcard(&roots, "");
    let editions = expand_wildcard(&years, "VC\\Redist\\MSVC");
    // The toolset version directories sort in version order for the versions
    // Visual Studio produces, so the last one is the newest installed.
    let toolsets = expand_wildcard(&editions, "x64");
    expand_wildcard(&toolsets, "")
        .into_iter()
        .filter(|path| {
            path.file_name()
                .and_then(|name| name.to_str())
                .is_some_and(|name| name.starts_with("Microsoft.VC") && name.ends_with(".CRT"))
        })
        .max()
}

fn copy_dll(redist_dir: &Path, name: &str, out_dir: &Path) -> Result<(), Box<dyn Error>> {
    // The redistributable directory names these in capitals; match case-insensitively.
    let source = children(redist_dir)
        .into_iter()
        .find(|path| {
            path.file_name()
                .and_then(|found| found.to_str())
                .is_some_and(|found| found.eq_ignore_ascii_case(name))
        })
        .ok_or_else(|| format!("{name} not found in {}", redist_dir.display()))?;

    fs::copy(&source, out_dir.join(name))?;
    println!("cargo:warning=bundling {} from {}", name, source.display());
    Ok(())
}

fn main() -> Result<(), Box<dyn Error>> {
    println!("cargo:rerun-if-changed=build.rs");
    println!("cargo:rerun-if-env-changed=VCToolsRedistDir");

    // The redistributable directory we read from below is the x64 one, so this
    // only applies to x86_64 Windows builds. On win-arm64 (only reachable by
    // building from the sdist, since we publish no arm64 wheel) bundling x64
    // DLLs would produce a wheel that cannot load at all, so bundle nothing and
    // leave that build depending on an installed redistributable.
    let is_windows_x64_msvc = env::var("CARGO_CFG_TARGET_OS").as_deref() == Ok("windows")
        && env::var("CARGO_CFG_TARGET_ENV").as_deref() == Ok("msvc")
        && env::var("CARGO_CFG_TARGET_ARCH").as_deref() == Ok("x86_64");
    if !is_windows_x64_msvc {
        return Ok(());
    }

    let out_dir = PathBuf::from(env::var("OUT_DIR")?);
    let redist_dir = find_redist_dir().ok_or(
        "could not find the Visual C++ redistributable directory. Set VCToolsRedistDir, \
         or build from a Visual Studio developer command prompt.",
    )?;

    for name in DLL_NAMES {
        copy_dll(&redist_dir, name, &out_dir)?;
    }

    fs::write(out_dir.join(NOTICE_NAME), NOTICE_TEXT)?;

    Ok(())
}
