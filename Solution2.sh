#!/usr/bin/bash
#------------------
dual=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
#input.txt file shuld be kept in the same folder where Solution2.sh is present
input=$(<input.txt)
phrase=$input
rotat=3
newphrase=$(echo $phrase | tr "${dual:0:26}" "${dual:${rotat}:26}")
echo "-------------Original content of file----------"
echo ${phrase}
echo "--------------after shifing 3 digits output is----------- "
echo ${newphrase}