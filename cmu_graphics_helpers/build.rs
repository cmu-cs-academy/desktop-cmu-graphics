//! Write the Visual C++ redistribution notice into OUT_DIR, so that maturin can
//! place it inside the Windows wheel's package directory.

use std::env;
use std::error::Error;
use std::fs;
use std::path::PathBuf;

const NOTICE_NAME: &str = "VC_REDIST_NOTICE.txt";

/// The text of the notice. It lives here, rather than in a checked-in .txt file,
/// so that it ships only in the wheels that actually carry the DLLs: the source
/// distribution would otherwise include a notice describing files it does not
/// contain, and excluding the file from the sdist would break building this
/// crate from source on Windows.
const NOTICE_TEXT: &str = r#"===============================================================================
Microsoft Visual C++ Runtime Libraries
===============================================================================
Copyright (c) Microsoft Corporation. All rights reserved.

This application includes redistributable binary files from the Microsoft Visual
C++ Runtime, distributed under the Microsoft Software License Terms for
Microsoft Visual Studio / Microsoft Visual C++ Redistributable package.

This package includes the following files, redistributed unmodified, in the
cmu_graphics_helpers.libs directory:

    msvcp140.dll
    vcruntime140_1.dll

For official Microsoft Visual Studio license terms, see:
https://visualstudio.microsoft.com/license-terms/"#;

fn main() -> Result<(), Box<dyn Error>> {
    println!("cargo:rerun-if-changed=build.rs");

    // Only the Windows wheel carries the DLLs, so only it needs the notice.
    if env::var("CARGO_CFG_TARGET_OS").as_deref() != Ok("windows") {
        return Ok(());
    }

    let out_dir = PathBuf::from(env::var("OUT_DIR")?);
    fs::write(out_dir.join(NOTICE_NAME), NOTICE_TEXT)?;

    Ok(())
}
