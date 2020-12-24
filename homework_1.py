import os

from operator import add,sub,mul,truediv
from datetime import datetime

abs_path =os.getcwd()
os.mkdir(".\logs")

s = input('type your input : ').split()
print(s)
operators ={'+' : add, '-' : sub, '*' : mul, '/' : truediv}
k = 0
res = s[1]

if(s[0] in operators):
    k = 1   
    param = s[1]
    for i in range(2, len(s)):
        if( s[i].isdecimal() or "".join(s[i].split(".")).isdecimal()):
            param = param + ' ' + s[i]
            res = operators[s[0]](float(res), float(s[i]))
        else:
            k = 0
           # raise Exception('Invalid expression!') 
            break
        
if(k == 0):
    print(f'Expression : {s[0]} {param} \nERROR: Invalid expression \nReport: INFO-1, ERROR-1 ')
    with open(os.path.join(abs_path, 'logs','excep.log'), 'w+') as f:
        f.write('{} :: ERROR :: Invalid message :: {}'.format(datetime.now(),param))
        f.close()
else:
    if(res.is_integer()):
       res = int(res)
    print(f'Expression : {s[0]} {param} \nResult: {res} \nReport: INFO-1, ERROR-0')   
    with open(os.path.join(abs_path, 'logs','info.log'), 'w+') as f:
        f.write('{} :: INFO :: Invalid message :: {} :: {}'.format(datetime.now(),param,res))
        f.close()
        
