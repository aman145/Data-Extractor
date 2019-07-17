import re
import nltk
from nltk.text import Text

lines=list()
with open(r'C:\Users\admin\Desktop\Project_1\extract\text_files\demo5042721661.txt','r') as openfileobject:
    for line in openfileobject:
        lines.append(line.split(" "))

for i in lines:
    if i[0].isalpha():
        if len(i)>=4:
            for j in range(len(i)):
                    if (bool(re.match('[0-9]', i[j]))):
                        
                            print(i,j)
                            break
            