#!/bin/sh
echo "----------------------------------------------" > test/output.txt 
echo "1. Variables Test:"  >> test/output.txt 
python ObsidianParser.py test/testVars.txt >> test/output.txt 

echo "----------------------------------------------" >> test/output.txt 
echo "2. Functions Test:" >> test/output.txt 
python ObsidianParser.py test/testFuncs.txt >> test/output.txt 

echo "----------------------------------------------" >> test/output.txt 
echo "3. Statements Test:" >> test/output.txt 
python ObsidianParser.py test/testStatements.txt >> test/output.txt 

echo "----------------------------------------------" >> test/output.txt 
echo "4. Expressions Test:" >> test/output.txt 
python ObsidianParser.py test/testExpressions.txt >> test/output.txt 

echo "----------------------------------------------" >> test/output.txt 
echo "5. Main Test:" >> test/output.txt 
python ObsidianParser.py test/testMain.txt >> test/output.txt

echo "----------------------------------------------" >> test/output.txt 
echo "6. Complete Test:" >> test/output.txt 
python ObsidianParser.py test/testComplete.txt >> test/output.txt  

git log --pretty=format:'%h : %s' --graph > Other/commits.log

more test/output.txt