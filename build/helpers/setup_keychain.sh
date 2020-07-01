security create-keychain -p $KEYCHAIN_PASSWORD $KEYCHAIN_NAME
security unlock-keychain -p $KEYCHAIN_PASSWORD $KEYCHAIN_NAME

security list-keychains -d user -s $KEYCHAIN_NAME
security default-keychain -s $KEYCHAIN_NAME

echo $SIGNING_IDENTITY_P12_B64 > encoded_identity
base64 --decode encoded_identity > identity.p12
rm encoded_identity

security import identity.p12 -k $KEYCHAIN_NAME -P $SIGNING_IDENTITY_PASSWORD -T /usr/bin/codesign > /dev/null
rm identity.p12
security set-key-partition-list -S apple-tool:,apple: -s -k $KEYCHAIN_PASSWORD $KEYCHAIN_NAME > /dev/null

export identity="$(security find-identity -p codesigning -v | head -n 1 | cut -d'"' -f2)"
echo $identity
