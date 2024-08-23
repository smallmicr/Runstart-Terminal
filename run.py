import os 
import time
print('welcome')
conf = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'config.txt'
part = open(conf,'r',encoding='utf-8')
pa = part.read()
f = os.listdir(pa)
while True:
    cmd = input('userApp>')
    if cmd == 'ls':
        for i in f:
            print(i)
        continue
    else:
        print('没有该指令')
