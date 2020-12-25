import os

from operator import add,sub,mul,truediv
from datetime import datetime

abs_path =os.getcwd()
os.mkdir(".\logs")
operators ={'+' : add, '-' : sub, '*' : mul, '/' : truediv}


s = input('type your input : ').split()
k = 0
res = s[1]

if(s[0] in operators):
    k = 1   
    for i in range(2, len(s)):
        if( s[i].isdecimal() or "".join(s[i].split(".")).isdecimal()):
            res = operators[s[0]](float(res), float(s[i]))
        else:
            k = 0
            break
op = s[0]
del s[0]
       
if(k == 0):
    print(f'Expression : {op} {" ".join(s)} \nERROR: Invalid expression \nReport: INFO-1, ERROR-1 ')
    with open(os.path.join(abs_path, 'logs','excep.log'), 'w+') as f:
        f.write('{} :: ERROR :: Invalid expression :: {}'.format(datetime.now()," ".join(s)))
else:
    if(res.is_integer()):
       res = int(res)
    print(f'Expression : {op} {" ".join(s)} \nResult: {res} \nReport: INFO-1, ERROR-0')   
    with open(os.path.join(abs_path, 'logs','info.log'), 'w+') as f:
        f.write('{} :: INFO  :: {} :: {}'.format(datetime.now()," ".join(s),res))
f.close()
        
