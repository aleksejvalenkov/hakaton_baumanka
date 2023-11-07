import paramiko 

def main():
    
    host = '192.168.14.103'
    user = 'muxi'
    secret = 'muxi'
    port = 22

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command('ls -l')
    print('1')
    comm = 'scp muxi@192.168.14.103:/home/muxi/src/dog /home/alex/Documents/hackaton_baumanka/test.jpeg'
    stdin, stdout, stderr = client.exec_command(comm)
    print('2')
    data = stdout.read() + stderr.read()
    client.close()

if __name__ == "__main__":
    main()