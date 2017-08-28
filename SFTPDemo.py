import paramiko
import sys
host = "10.2.0.51"
port = 22
transport = paramiko.Transport(host, port)

password = "root1234"
username = "root"
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport( transport )
path = '/tmp/test.txt' #+ sys.argv[1]
print( path )
#local_path = sys.argv[1]
local_path = 'D:\\IdeaProjects\\Python3\\test.txt'
sftp.put(local_path, path)

sftp.close()
transport.close()
print( 'Upload done!')
