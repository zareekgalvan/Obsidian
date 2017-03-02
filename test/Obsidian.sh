#!/bin/sh
echo "1. Variables Test:"  > test/output.txt 
python ObsidianParser.py test/testVars.txt >> test/output.txt 

#echo "2. Functions Test:" >> test/output.txt 
#python ObsidianParser.py test/testFuncs.txt >> test/output.txt 

#echo "3. Main Test:" >> test/output.txt 
#python ObsidianParser.py test/testFuncs.txt >> test/output.txt 

more test/output.txt