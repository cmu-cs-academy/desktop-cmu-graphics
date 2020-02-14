echo $SIGNING_IDENTITY_P12_B64 > encoded_identity
base64 --decode encoded_identity > identity.p12
rm encoded_identity

cat identity.p12
cat $SIGNING_IDENTITY_PASSWORD
security import identity.p12 -k ~/Library/Keychains/login.keychain -P $SIGNING_IDENTITY_PASSWORD
security import identity.p12 -k ~/Library/Keychains/login.keychain -P $SIGNING_IDENTITY_PASSWORD > /dev/null
rm identity.p12

export identity="$(security find-identity -p codesigning -v | head -n 1 | cut -d'"' -f2)"
echo $identity
