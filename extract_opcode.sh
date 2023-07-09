#!/bin/bash

# 파일의 opcode를 추출하는 쉘스크립트
num=0
for file in $"./media"/*
do
    count=0
    num=$(($num + 1))
    name=$(basename "$file")
    fileName="${name%.*}"
    touch ./media/$fileName.txt
    echo ${fileName} >> $"./media"/$fileName.txt
    
    # opcode 추출
    for op in $(objdump -d $file | grep "^ " | cut -f 3 | cut -f 1 -d $' ');
    do
        if [ $count -lt 500 ]
        then
            count=$(($count + 1))
            echo ${op} >> $"./media"/$fileName.txt
        else
            break
        fi
    done
done