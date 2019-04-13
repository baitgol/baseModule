#!/usr/bin/python
# -*- coding: utf-8 -*-

# paramiko.py

import paramiko

paramiko.util.log_to_file('paramiko.log')

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('162.168.2.70',22,'rhino','rhino')


sftp=ssh.open_sftp()
sftp.put('d:\\123.txt','/home/test/input')
#sftp.get('/home/atp/123','d:\\123')
stdin,stdout,stderr=ssh.exec_command('ls /home/')
for line in stdout:
    print line,
	
ssh.close()
