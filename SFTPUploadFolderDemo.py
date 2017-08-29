import paramiko, sys, os

host = "10.2.0.51"
port = 22
transport = paramiko.Transport(host, port)

password = "root1234"
username = "root"
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport( transport )
remote_dir = '/tmp/ui/'
parent = 'D:\\tmp\\20170828\\业财对接-团险保全保单计划变更核算规则会计科目缺失3484\\'
print( "===================" + parent )
for dirpath, dirnames, filenames in os.walk( parent ):
    remote_path  = os.path.join( remote_dir, dirpath )
    print( '----------' + remote_path )
    #print( dirpath )
#sftp.put(local_path, path)

sftp.close()
transport.close()
print( 'Upload done!')

