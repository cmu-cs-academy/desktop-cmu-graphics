security create-keychain -p $keychain_password $keychain_name || true
security unlock-keychain -p $keychain_password $keychain_name || true

echo $SIGNING_IDENTITY_P12_B64 > encoded_identity
base64 --decode encoded_identity > identity.p12
rm encoded_identity

security import identity.p12 -k $keychain_name -P $SIGNING_IDENTITY_PASSWORD -T /usr/bin/codesign > /dev/null
rm identity.p12

# stop password popup from appearing (for Travis)
security set-key-partition-list -S apple-tool:,apple: -s -k $keychain_password $keychain_name > /dev/null
