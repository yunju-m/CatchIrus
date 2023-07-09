import os
import csv
import pickle

dic = {}
four_gram = {}
num = 0

# opcode를 dictionary로 만들기
def make_dic():
    total_data = {}
    with open("./media/test.csv", "r") as inp:
        reader = csv.reader(inp)
        total_data = {rows[0]:rows[1:501] for rows in reader}
    return total_data

# dictionary에 있는 opcode들 숫자로 변환
def change_num(total_data):
    global num
    ngram = {}
    fname = list(total_data.keys())
    opcode = list(total_data.values())

    for k in range(len(opcode)):
        temp1 = []
        for i in range(len(opcode[k]) - 3):
            temp2 = []
            for j in range(4):
                if opcode[k][i + j] in dic:
                    temp2.append(dic[opcode[k][i + j]])
                else:
                    dic[opcode[k][i + j]] = num
                    temp2.append(dic[opcode[k][i + j]])
                    num += 1
            temp1.append(temp2)
        ngram[fname[k]] = temp1
    return ngram

# 숫자로 변환한 opcode를 4-gram 전처리
def make_4gram(ngram):
    global num
    num = 0
    result = {}
    fname = list(ngram.keys())
    opcode = list(ngram.values())

    for i in range(len(opcode)):    # 500번 반복
        temp = []
        for j in range(len(opcode[i])): # 998번 반복
            tmp = ""
            for k in range(len(opcode[i][j])):  # 4번 반복
                tmp += str(opcode[i][j][k]) + " "
            tmp = tmp.rstrip()
            if tmp in four_gram:
                temp.append(four_gram[tmp])
            else:
                four_gram[tmp] = num
                temp.append(four_gram[tmp])
                num += 1
        result[fname[i]] = temp
    return result

# csv로 저장
def make_csv(fgram):
    with open('test.csv', 'w') as f:
        write = csv.writer(f)
        print("file name", sep=',', file=f, end=',')
        for i in range(500):
            print(i, sep=',', file=f, end=',')
        print(' ', file=f)
        for k, v in fgram.items():
            print(k, sep=',', file=f, end=',')
            for d in v:
                print(d, sep=',', file=f, end=',')
            print(' ', file=f)

l = make_dic()
ngram = change_num(l)
fgram = make_4gram(ngram)
make_csv(fgram)