#!/bin/bash

#!/bin/bash

echo "Start"

git init &&
git remote add origin git@github.com:kiri3914/elfido.git &&
git add . &&
git commit -m "all" &&
git push origin master

echo "Finish"