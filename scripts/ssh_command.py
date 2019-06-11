#!/usr/bin/python3

import sys
#import spur
import paramiko

if(len(argv) != 5):
	print("Illegal number of arguments!")
	exit(1)

host_name = sys.argv[1]
user_name = sys.argv[2]
passwd = sys.argv[3]
command = sys.argv[4]

ssh = parmiko.SSHClient()
ssh.connect(host_name, username = user_name, password = password)
stdin,stdout,stderr = ssh.exec_command(command)
outlines = stdout.readlines()
resp = ''.join(outlines)
print(resp)


#shell = spur.SshShell(hostname = host_name, username = user_name, password = passwd)
#result = shell.run(command)
#print(result.output)


