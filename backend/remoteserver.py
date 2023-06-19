import paramiko, io


class RemoteServer():
    def __init__(self, host, port, user, key, script) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.key = key
        self.script = script
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(host, port=port, username=user, pkey=paramiko.RSAKey.from_private_key(io.StringIO(key)))
        
    
    def close(self):
        self.ssh.close()

if __name__ == "__main__":
    pass