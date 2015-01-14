#!/bin/bash

#for((i=1;i<10;i++))
#for
for i in `seq 10`
do
wget http://www.fy56.com/Anli_List.asp?page=$i -O 11
print $i
sleep 1s
iconv -f gbk -t utf8 11 > 22
python parsehtml.py >> result.txt
done
