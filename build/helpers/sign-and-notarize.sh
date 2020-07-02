export identity="$(security find-identity -p codesigning -v | head -n 1 | cut -d'"' -f2)"
python3 find_and_sign_binaries.py "$identity" "../../cmu_graphics"
