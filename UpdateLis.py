'''该脚本读取某个目录下的文件，然后上传到lis服务器上，成功执行后，将该目录下的文件删除
'''
import os,time,sys,subprocess,shlex

def updatelis( local_dir, remote_dir, hostname, port, password ):
    hostname = hostname
    port = port
    local_dir = local_dir
    remote_dir = remote_dir
    password = password
    updatelis_command_string = 'pscp -r -batch -pw ' + password + ' ' + local_dir + ' root@' + hostname + ':' + remote_dir
    print( updatelis_command_string )
    '''Not use in Windows 
    args = shlex.split( updatelis_command_string )
    print( args )
    '''
    try:
        #proc = subprocess.Popen( updatelis_command_string, stderr = subprocess.STDOUT )
        subprocess.check_call( updatelis_command_string )
    except subprocess.CalledProcessError:
        print( "error occured!!!\n")
    #pipe = subprocess.Popen( updatelis_command_string ).stdout
    '''
    if ( pipe != None and pipe %256 ) :
        print( ' There is some errors ')
        return 1
    else :
        print( " Excute OK!")
        return 0
    while pipe.poll() is None:
        time.sleep(1)
    return_code = pipe.return_code
    print( return_code )
    sys.exit( return_code )
    '''

host = '10.2.0.51'
port = 22
password = 'root1234'

remote_dir = "/tmp/user_projects/web/lis/ui/"

local_dir = "d:/tmp/lisupdate/"

if ( not os.path.exists( local_dir )):
    print( 'No need to Update!, Bacause ' + local_dir + ' Not exits!!!\\n')
    sys.exit()
else:
    updatelis( local_dir, remote_dir, host, port, password )

