import shutil
import os
import paramiko

def backup_to_remote(local_dir, remote_host, remote_port, remote_user, remote_pass, remote_dir):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh_client.connect(remote_host, port=remote_port, username=remote_user, password=remote_pass)

        sftp = ssh_client.open_sftp()

        sftp.mkdir(remote_dir, mode=0o755, ignore_existing=True)

        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_path = os.path.join(root, file)
                remote_path = os.path.join(remote_dir, os.path.relpath(local_path, local_dir))
                sftp.put(local_path, remote_path)

        sftp.close()
        ssh_client.close()

        return True, "Backup successful."
    except Exception as e:
        return False, f"Backup failed: {str(e)}"

local_directory = "/path/to/local/directory"

remote_host = "remote.server.com"
remote_port = 22
remote_user = "username"
remote_pass = "password"
remote_directory = "/path/to/remote/directory"

success, message = backup_to_remote(local_directory, remote_host, remote_port, remote_user, remote_pass, remote_directory)

print(message)
