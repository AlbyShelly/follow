#!/bin/bash
xclip -i ../token.txt -selection clipboard
git add .
git commit -m $1
git push
