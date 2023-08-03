import os
import csv
import pickle

with open("op_dic.pickle", "rb") as fr:
    dic = pickle.load(fr)

with open("4gram_dic.pickle", "rb") as ff:
    four_gram = pickle.load(ff)

class Data:
    num = 0
    def __init__(self, input_filepath, output_filepath):
        self.input_filepath = input_filepath
        self.output_filepath = output_filepath
    
    def predict(self):
        data = {}
        with open(self.input_filepath, "r") as inp:
            reader = csv.reader(inp)
            data = {rows[0]:rows[1:504] for rows in reader}
        
        # opcode를 4-gram으로 묶기 ex) add int mov mov mov -> (add, int, mov, mov), (int, mov, mov, mov) ...
        op_to_4gram = {}
        fname = list(data.keys())
        opcode = list(data.values())

        for k in range(len(opcode)):
            tmp1 = []
            for i in range(len(opcode[k])-3):
                tmp2 = []
                for j in range(4):
                    if opcode[k][i+j] in dic:
                        tmp2.append(dic[opcode[k][i+j]])
                    else:
                        dic[opcode[k][i+j]] = num
                        tmp2.append(dic[opcode[k][i+j]])
                        num += 1
                tmp1.append(tmp2)
            op_to_4gram[fname[k]] = tmp1

        # 4-gram으로 묶인 것들 숫자로 치환 ex) (add, int, mov, mov), (int, mov, mov, mov) -> 1, 2, ...
        num = 0
        fgram_to_num = {}
        fname = list(op_to_4gram.keys())
        opcode = list(op_to_4gram.values())

        for i in range(len(opcode)):
            tmp1 = []
            for j in range(len(opcode[i])):
                tmp2 = ""
                for k in range(len(opcode[i][j])):
                    tmp2 += str(opcode[i][j][k]) + " "
                tmp2 = tmp2.rstrip()
                if tmp2 in four_gram:
                    tmp1.append(four_gram[tmp2])
                else:
                    four_gram[tmp2] = num
                    tmp1.append(four_gram[tmp2])
                    num += 1
            fgram_to_num[fname[i]] = tmp1
        
        # csv파일로 만들기
        with open(self.output_filepath, "w") as f:
            write = csv.writer(f)
            print("file name", sep=",", file=f, end=",")
            for i in range(500):
                print(i, sep=",", file=f, end=",")
            print("class", sep=",", file=f)
            for k, v in fgram_to_num.items():
                print(k, sep=",", file=f, end=",")
                for d in v:
                    print(d, sep=",", file=f, end=",")
                print("-1", file=f)