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
//! VC_REDIST_NOTICE.txt for the redistribution terms.

use std::env;
use std::error::Error;
use std::fs;
use std::path::{Path, PathBuf};

/// Anything listed here must be a REDIST file that Microsoft's Visual Studio
/// license terms allow us to redistribute. Do not add DLLs without checking
/// that, and see VC_REDIST_NOTICE.txt.
const DLL_NAMES: [&str; 2] = ["msvcp140.dll", "vcruntime140.dll"];

/// Redistributing Microsoft's DLLs requires shipping a notice alongside them.
const NOTICE_NAME: &str = "VC_REDIST_NOTICE.txt";

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
    println!("cargo:rerun-if-changed={NOTICE_NAME}");
    println!("cargo:rerun-if-env-changed=VCToolsRedistDir");

    let is_windows_msvc = env::var("CARGO_CFG_TARGET_OS").as_deref() == Ok("windows")
        && env::var("CARGO_CFG_TARGET_ENV").as_deref() == Ok("msvc");
    if !is_windows_msvc {
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

    let manifest_dir = PathBuf::from(env::var("CARGO_MANIFEST_DIR")?);
    fs::copy(manifest_dir.join(NOTICE_NAME), out_dir.join(NOTICE_NAME))?;

    Ok(())
}
