'''
Source(s):
https://www.blog.pythonlibrary.org/2012/10/26/python-101-how-to-move-files-between-servers/
https://stackoverflow.com/questions/12831865/python-script-to-get-files-from-one-server-into-another-and-store-them-in-separa
'''
import os
import paramiko


class SSHConnection(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, host, username, password, port=22):
        """Initialize and setup connection"""
        self.sftp = None
        self.sftp_open = False

        # open SSH Transport stream
        self.transport = paramiko.Transport((host, port))

        self.transport.connect(username=username, password=password)

    # ----------------------------------------------------------------------
    def _openSFTPConnection(self):
        """
        Opens an SFTP connection if not already open
        """
        if not self.sftp_open:
            self.sftp = paramiko.SFTPClient.from_transport(self.transport)
            self.sftp_open = True

    # ----------------------------------------------------------------------
    def get(self, remote_path, local_path=None):
        """
        Copies a file from the remote host to the local host.
        """
        self._openSFTPConnection()
        self.sftp.get(remote_path, local_path)

        # ----------------------------------------------------------------------

    def put(self, local_path, remote_path=None):
        """
        Copies a file from the local host to the remote host
        """
        self._openSFTPConnection()
        self.sftp.put(local_path, remote_path)

    # ----------------------------------------------------------------------
    def close(self):
        """
        Close SFTP connection and ssh connection
        """
        if self.sftp_open:
            self.sftp.close()
            self.sftp_open = False
        self.transport.close()


if __name__ == "__main__":
    host = "myserver"
    username = "mike"
    pw = "dingbat!"

    origin = '/home/mld/projects/ssh/random_file.txt'
    dst = '/home/mdriscoll/random_file.txt'

    ssh = SSHConnection(host, username, pw)
    ssh.put(origin, dst)
    ssh.close()

### Considerations for moving it from SFTP to SSH key based

# localpath = '~/pathNameForToday/'
# os.system('mkdir ' + localpath)
# ssh = paramiko.SSHClient()
# ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
# ssh.connect(server, username=username, password=password)
# sftp = ssh.open_sftp()
# sftp.get(remotepath, localpath)
# sftp.close()
# ssh.close()