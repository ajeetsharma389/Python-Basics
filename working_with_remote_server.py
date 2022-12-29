import paramiko

ssh_var =  paramiko.SSHClient()

ssh_var.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_var.connect(hostname='IP',username='ec2-user',password='xxxxxx',port=22)

stdin, stdout, stderr = ssh_var.exec_command('whoami')

print(stdout.read())