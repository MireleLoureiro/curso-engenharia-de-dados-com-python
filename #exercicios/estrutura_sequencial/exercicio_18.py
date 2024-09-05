tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de Internet (em Mbps): "))

velocidade_internet_MBps = velocidade_internet / 8
tempo_download_segundos = tamanho_arquivo / velocidade_internet_MBps
tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")
