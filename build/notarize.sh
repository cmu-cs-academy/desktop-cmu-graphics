set -e

# setup
source env.sh
export zipname=cmu_graphics_installer.zip

# signing
if [[ $CI == "true" ]] ; then
    ./helpers/setup_keychain.sh
fi
export identity="$(security find-identity -p codesigning -v $keychain_name | head -n 1 | cut -d'"' -f2)"
echo "Signing with identity" $identity
find ../cmu_graphics -type f -iname "*.so" -o -iname "*.dylib" -exec codesign -vfs "$identity" {} +

# notarizing
cd ../
zip -r $zipname cmu_graphics sample.py
echo "Uploading zip to the notarization service ..."
notarization_out=$(\
    xcrun altool --notarize-app \
                 --primary-bundle-id "cmu-graphics-installer.zip" \
                 --username "$APPLE_ID" --password "$APPLE_PASSWORD" \
                 --file $zipname\
)

# get the request uuid
delimiter="RequestUUID = "
notarization_out=$notarization_out$delimiter

notarization_out_lines=()
while [[ $notarization_out ]]; do
  notarization_out_lines+=( "${notarization_out%%"$delimiter"*}" )
  notarization_out=${notarization_out#*"$delimiter"}
done

request_uuid="${notarization_out_lines[1]}"
echo "Captured request UUID:" $request_uuid

# wait for notarization to complete
while :
do
    status=$((xcrun altool --notarization-info $request_uuid -u $APPLE_ID -p $APPLE_PASSWORD || true) 2>&1)
    finished=0

    if [[ "$status" == *"Error: Failed to get notarization info."* ]]; then
        echo "Notarization has not yet started. Checking back in 30 seconds ..."
        sleep 30
        continue
    fi

    IFS=$'\n' read -rd '' -a status_lines <<<"$status" || true
    for status_line in "${status_lines[@]}"; do
        if [[ "$status_line" == *"Status:"* ]]; then
            IFS=$":" read -rd '' -a line_pieces <<<"$status_line" || true
            if [[ "${line_pieces[1]}" == *"in progress"* ]]; then
                echo "Notarization Status: in progress. Checking back in 30 seconds ..."
            elif [[ "${line_pieces[1]}" == *"success"* ]]; then
                finished=1
                echo "Notarization Status:" ${line_pieces[1]}
            else
                echo "Notarization failed"
                exit 1
            fi
        fi
    done

    if ((finished)); then
        break
    else
        sleep 30
    fi
done
