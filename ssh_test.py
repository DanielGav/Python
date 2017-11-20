#Instala pip3 install paramiko
import paramiko

def get_connection():
    ssh = paramiko.SSHClient()  # Iniciamos un cliente SSH
    ssh.load_system_host_keys()  # Agregamos el listado de host conocidos
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Si no encuentra el host, lo agrega automáticamente
    ssh.connect('itnovaretest.ddns.net', username='root', password='iso120625')  # Iniciamos la conexión.
    return ssh

def restart_nginx(ssh_obj):
    stdin, stdout, stderr = ssh_obj.exec_command("sudo service nginx restart")


def reload_supervisor(ssh_obj):
    stdin, stdout, stderr = ssh_obj.exec_command("sudo supervisorctl reload")


def restart_services():
    print("Iniciamos la conexión")
    ssh_obj = get_connection()
    print("Reiniciamos nginx")
    restart_nginx(ssh_obj)
    print("Reiniciamos supervisor")
    reload_supervisor(ssh_obj)
    print('Finalizado correctamente')


restart_services()