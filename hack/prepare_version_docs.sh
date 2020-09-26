#!/bin/bash

set -e

cp -r docs version-$1 && cd version-$1
sed -i 's/id: /id: version-1.9.0-/g' $(find *.md)
for FILE in *.md; 
do
 sed -i '/^sidebar_label:.*/a original_id: '$(echo "$FILE" | cut -f 1 -d '.') $FILE
done
cd ..
mv version-$1 website/versioned_docs
