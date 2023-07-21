import csv

class Change:
    def __init__(self, filepath, filename):
        self.filepath = filepath
        self.filename = filename
        
    def txt_to_csv(self):
        f_in = open(self.filepath + self.filename + ".txt", "r")
        f_out = open(self.filepath + self.filename + ".csv", "w")
            
        for line in f_in:
            line_replace=line.replace("\n",",")
            f_out.write(line_replace)
            
        f_in.close()
        f_out.close()