# signing
export identity="$(security find-identity -p codesigning -v | head -n 1 | cut -d'"' -f2)"
python3 find_and_sign_binaries.py "$identity" "../../cmu_graphics"

# notarizing
cd ../../
zip -r cmu_graphics_installer.zip cmu_graphics sample.py
xcrun altool --notarize-app \
             --primary-bundle-id "cmu-graphics-installer.zip" \
             --username "$APPLE_ID" --password "$APPLE_PASSWORD" \
             --file cmu_graphics_installer.zip
