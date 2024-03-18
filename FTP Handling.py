#FTP Handling

from ftplib import FTP

# Informações de conexão FTP
ftp_host = 'ftp.example.com'
ftp_user = 'seu_usuario'
ftp_password = 'sua_senha'

# Função para fazer upload de um arquivo para o servidor FTP
def upload_file():
    file_to_upload = 'local_file.txt'
    remote_path = '/remote/directory/' + file_to_upload
    
    # Conectando ao servidor FTP
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_password)

    # Mudando para o diretório remoto
    ftp.cwd('/remote/directory/')

    # Fazendo upload do arquivo
    with open(file_to_upload, 'rb') as f:
        ftp.storbinary('STOR ' + remote_path, f)

    # Fechando a conexão FTP
    ftp.quit()
    print(f"Arquivo '{file_to_upload}' enviado com sucesso para '{remote_path}'.")

# Função para baixar um arquivo do servidor FTP
def download_file():
    remote_file = '/remote/directory/remote_file.txt'
    local_path = 'local_file.txt'
    
    # Conectando ao servidor FTP
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_password)

    # Mudando para o diretório remoto
    ftp.cwd('/remote/directory/')

    # Baixando o arquivo
    with open(local_path, 'wb') as f:
        ftp.retrbinary('RETR ' + remote_file, f.write)

    # Fechando a conexão FTP
    ftp.quit()
    print(f"Arquivo '{remote_file}' baixado com sucesso para '{local_path}'.")

# Chamando as funções para fazer upload e download
upload_file()
download_file()