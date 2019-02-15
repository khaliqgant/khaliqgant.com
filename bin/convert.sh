#!/bin/bash

cd ./posts
for i in *.md; do
    output=${i/md/html}
    ../node_modules/showdown/bin/showdown.js makehtml -i $i -o $output
done
