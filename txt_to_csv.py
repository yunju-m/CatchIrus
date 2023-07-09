# txt파일을 csv파일로 변환
import csv

f_in = open("./media/test.txt", "r")
f_out = open("./media/test.csv", "w")
    
for line in f_in:
    line_replace=line.replace("\n",",")
    f_out.write(line_replace)
f_in.close()
f_out.close()