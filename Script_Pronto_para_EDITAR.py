# import tkinter as tk
# import datetime
# import psutil

# def solicitar_senha():
#     senha = input("Digite a senha para prosseguir: ")
#     # Substitua "senha_padrao" pela sua senha real
#     return senha == "123456"

# def verificar_expiracao(data_expiracao):
#     data_atual = datetime.datetime.now()
#     return data_atual > data_expiracao

# def obter_endereco_mac():
#     # Obtendo o endereço MAC
#     endereco_mac = None
#     for interface, informacoes in psutil.net_if_addrs().items():
#         if interface.startswith('Ethernet') or interface.startswith('Wi-Fi'):
#             for info in informacoes:
#                 if info.family == psutil.AF_LINK:
#                     endereco_mac = info.address
#                     break
#             if endereco_mac:
#                 break
#     return endereco_mac

# def iniciar_aplicacao():
#     senha_correta = solicitar_senha()

#     if senha_correta:
#         data_expiracao = datetime.datetime(2024, 12, 31)  # Substitua pela sua data de expiração
#         expirado = verificar_expiracao(data_expiracao)

#         if not expirado:
#             mac_address = obter_endereco_mac()
#             resultado_label.config(text=f"Endereço MAC: {mac_address}")
#         else:
#             resultado_label.config(text="A licença expirou. Entre em contato com o suporte.")
#     else:
#         resultado_label.config(text="Senha incorreta. Acesso negado.")

# # Criar a janela principal
# janela = tk.Tk()
# janela.title("Aplicação Tkinter")

# # Criar widgets (rótulos, entrada de senha, botão e rótulo de resultado)
# senha_label = tk.Label(janela, text="Digite a senha:")
# senha_entry = tk.Entry(janela, show="*")  # Para ocultar a senha
# iniciar_button = tk.Button(janela, text="Iniciar Aplicação", command=iniciar_aplicacao)
# resultado_label = tk.Label(janela, text="")

# # Posicionar os widgets na janela
# senha_label.grid(row=0, column=0, pady=10)
# senha_entry.grid(row=0, column=1, pady=10)
# iniciar_button.grid(row=1, column=0, columnspan=2, pady=10)
# resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

# # Iniciar o loop principal da aplicação
# janela.mainloop()

import tkinter as tk

def iniciar_codigo():
    # Aqui você coloca o código que deseja executar ao clicar no botão
    print("Código iniciado!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Minha Interface")

# Criar um botão na janela
botao = tk.Button(janela, text="Iniciar Código", command=iniciar_codigo)
botao.pack(pady=20)

# Iniciar o loop principal da interface gráfica
janela.mainloop()


