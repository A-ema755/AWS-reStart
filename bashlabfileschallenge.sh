#!/bin/bash

# This script creates empty files in batches of 25. It names the files
# <yourName><number> where <youName> is a constant initialized in the script and
# <number> is automatically generated sequentially starting from the highest number
# that currently exists in the directory.
#

yourName=Emanuel

# Find all files whose name starts with <yourName> and extract determine the
# highest number.

numbers=($(ls | grep ^$yourName | grep -oE [0-9]\+))

declare -i maxNumber=0
declare -i num=0

for (( i=0; i<${#numbers[@]}; i++ ))
do
   num=${numbers[i]}
#  if [ $num > $maxNumber ]
   if ((num > maxNumber))
   then
      maxNumber=$num
   fi
#   echo ${numbers[i]}
done

echo "max = $maxNumber"

# Initialize next number.

declare -i nextNumber=$maxNumber+1
echo $nextNumber

# Create the next 25 files.

for i in {1..25}
do
   echo "Creating file number $i"
   nextFileName="$yourName$nextNumber"
   echo $nextFileName
   touch $nextFileName
   nextNumber=$nextNumber+1
done

echo "File creation done!"
