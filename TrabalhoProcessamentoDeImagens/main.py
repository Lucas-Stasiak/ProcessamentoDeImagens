from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import funcoes
from tkinter import Label, Tk


Janela = Tk()
Janela.title("Implementação das Técnicas de Processamento de Imagens")
largura_janela = 1920  # largura
altura_janela = 1080   # altura
label_imagemA = Label(Janela)
label_imagemA.pack(pady=20)
label_imgA = Label(Janela, text="Imagem A", font=("Arial", 10), fg="black")
label_imgA.place(x=150, y=10)
label_imagemB = Label(Janela)
label_imagemB.pack(pady=20)
label_imgB = Label(Janela, text="Imagem B", font=("Arial", 10), fg="black")
label_imgB.place(x=510, y=10)
label_img_result = Label(Janela, text="Imagem Resultante", font=("Arial", 10), fg="black")
label_img_result.place(x=1620, y=10)
label_imagem_result = Label(Janela)
label_imagem_result.pack(pady=20)
label_Operacoes_aritmeticas = Label(Janela, text="Operações Aritméticas", font=("Arial", 10), fg="black")
label_Operacoes_aritmeticas.place(x=800, y=10)
label_Operacoes_logicas = Label(Janela, text="Operações Lógicas", font=("Arial", 10), fg="black")
label_Operacoes_logicas.place(x=1000, y=10)
label_Realce_Imagens = Label(Janela, text="Realce de Imagem", font=("Arial", 10), fg="black")
label_Realce_Imagens.place(x = 1200, y = 10)
label_Realce_Bordas = Label(Janela, text="Realce de Bordas", font=("Arial", 10), fg="black")
label_Realce_Bordas.place(x = 1330, y = 10)
label_Operacoes_morfologicas = Label(Janela, text="Operações Morfológicas", font=("Arial", 10), fg="black")
label_Operacoes_morfologicas.place(x = 1330, y = 270)

funcoes.configurar_label(label_imagem_result)
funcoes.configurar_labelImgA(label_imagemA)

def atualizar_comboBox():
    opcao = comboBox.get()
    print(opcao)

#comboBox escolher tipo de conversão
comboBox = ttk.Combobox(Janela, width=15)
comboBox['values'] = ('RGB to 1bit', 'RGB to 8bit', 'to Double')
comboBox.place(x=130, y=390)
comboBox.bind("<<ComboboxSelected>>",lambda event: atualizar_comboBox)
funcoes.configurar_comboBox(comboBox)



def centralizar_janela(janela, largura, altura):
    # Obtém a largura e altura da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição x e y para centralizar
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Define a geometria da janela para centralizá-la
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
centralizar_janela(Janela, largura_janela, altura_janela)

def selecionar_imagem_A():
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tif")]
    )
    
    if caminho_imagem:
        imagem = Image.open(caminho_imagem)  # Abre a imagem
        imagem = imagem.resize((350, 350), Image.Resampling.LANCZOS)  # Redimensiona a imagem
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagemA.config(image=imagem_tk)
        label_imagemA.image = imagem_tk  
        label_imagemA.place(x=10, y=30)
        imagem.save("imagemA.png")
        
def selecionar_imagem_B():
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tif")]
    )
    
    if caminho_imagem:
        imagem = Image.open(caminho_imagem)  # Abre a imagem
        imagem = imagem.resize((350, 350), Image.Resampling.LANCZOS)  # Redimensiona a imagem
        imagem_tk = ImageTk.PhotoImage(imagem)

        label_imagemB.config(image=imagem_tk)
        label_imagemB.image = imagem_tk  
        label_imagemB.place(x=370, y=30)
        imagem.save("imagemB.png")

def salvar_imagem():
    caminho_imagem = filedialog.asksaveasfilename(
        title="Salvar imagem",
         defaultextension=".png",
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if caminho_imagem:
        cv2.imwrite(caminho_imagem, cv2.imread("img_result.png"))
        print("Imagem salva com sucesso!")





# botão para selecionar imagem A
btn_selectRGB_IMG = Button(Janela, text="Load img A", command=selecionar_imagem_A, width=15, height=2)
btn_selectRGB_IMG.pack(pady=5)
btn_selectRGB_IMG.place(x=10, y=390)

# botão para selecionar imagem B
btn_selectBin_IMG = Button(Janela, text="Load img B",command=selecionar_imagem_B, width=15, height=2)
btn_selectBin_IMG.pack(pady=5)
btn_selectBin_IMG.place(x=485, y=390)

#botão para converter imagem
btn_convert_img = Button(Janela, text="Converter",command=funcoes.converter_imagem, width=15, height=2)
btn_convert_img.pack(pady=10)
btn_convert_img.place(x=248, y=390)

# botão salvar imagem
btn_save_img = Button(Janela, text="Save img",command= salvar_imagem, width=15, height=2)
btn_save_img.pack(pady=5)
btn_save_img.place(x=1620, y=390)

# botão operação aritmética adição de imagens
btn_adicao_img = Button(Janela, text="Adição",command=funcoes.adicao_imagem,width=15, height=2)
btn_adicao_img.pack(pady=5)
btn_adicao_img.place(x=750, y=50)

# botão operação aritmética subtração de imagens
btn_subtracao_img = Button(Janela,text="Subração",command=funcoes.subtracao_imagem,width=15, height=2)
btn_subtracao_img.pack(pady=5)
btn_subtracao_img.place(x=750, y=100)

# botão operação aritmética multiplicação de imagens
btn_multiplicacao_img = Button(Janela,text="Multiplicação",command=funcoes.multiplicacao_imagem, width=15, height=2)
btn_multiplicacao_img.pack(pady=5)
btn_multiplicacao_img.place(x=750, y=150)

# botão operação aritmética divisão de imagens
btn_divisao_img = Button(Janela,text="Divisão",command=funcoes.divisao_imagem, width=15, height=2)
btn_divisao_img.pack(pady=5)
btn_divisao_img.place(x=750, y=200)

# caixa de entrada dos valores para soma
entry_valor_soma = Entry(Janela,font=("Arial", 22), width=5)
entry_valor_soma.pack(pady=30)
entry_valor_soma.place(x=880, y=50)
#entry_valor_soma.insert(0, "0")
funcoes.configurar_entry(entry_valor_soma)

# caixa de entrada dos valores para subtração
entry_valor_subtracao = Entry(Janela,font=("Arial", 22), width=5)
entry_valor_subtracao.pack(pady=30)
entry_valor_subtracao.place(x=880, y=100)
#entry_valor_subtracao.insert(0, "0")
funcoes.configurar_entry_subtracao(entry_valor_subtracao)

# caixa de entrada dos valores para multiplicação
entry_valor_multiplicacao = Entry(Janela,font=("Arial", 22), width=5)
entry_valor_multiplicacao.pack(pady=30)
entry_valor_multiplicacao.place(x=880, y=150)
#entry_valor_multiplicacao.insert(0, "0")
funcoes.configurar_entry_multiplicacao(entry_valor_multiplicacao)

# caixa de entrada dos valores para divisão
entry_valor_divisao = Entry(Janela,font=("Arial", 22), width=5)
entry_valor_divisao.pack(pady=30)
entry_valor_divisao.place(x=880, y=200)
#entry_valor_divisao.insert(0, "0")
funcoes.configurar_entry_divisao(entry_valor_divisao)

# caixa de entrada dos valores para Blending
entry_valor_blending = Entry(Janela,font=("Arial", 22), width=5)
entry_valor_blending.pack(pady=30)
entry_valor_blending.place(x=880, y=250)
entry_valor_blending.insert(0, "0.8")
funcoes.configurar_entry_blending(entry_valor_blending)

# botão operação lógica de imagens
btn_AND_img = Button(Janela, text="AND",command=funcoes.and_imagem ,width=15, height=2)
btn_AND_img.pack(pady=5)
btn_AND_img.place(x=1000, y=50)

# botão operação lógica de imagens
btn_OR_img = Button(Janela, text="OR", command=funcoes.or_imagem ,width=15, height=2)
btn_OR_img.pack(pady=5)
btn_OR_img.place(x=1000, y=100)

# botão operação lógica de imagens
btn_XOR_img = Button(Janela, text="XOR",command=funcoes.xor_imagem ,width=15, height=2)
btn_XOR_img.pack(pady=5)
btn_XOR_img.place(x=1000, y=150)

# botão operação lógica de imagens
btn_NOT_img = Button(Janela, text="NOT",command=funcoes.not_imagem ,width=15, height=2)
btn_NOT_img.pack(pady=5)
btn_NOT_img.place(x=1000, y=200)

#botão resetar campos
btn_reset_campos = Button(Janela,font=("Arial", 17) ,text="Limpar", command=funcoes.resetarEntradas, width = 6, height = 1)
btn_reset_campos.pack(pady=5)
btn_reset_campos.place(x = 880, y = 300)
funcoes.configurar_btn_reset_campos(btn_reset_campos)

#botão inverter imagem
btn_inverter_img = Button(Janela, text="Inverter",command=funcoes.inverterImagem, width=15, height=2)
btn_inverter_img.pack(pady=5)
btn_inverter_img.place(x = 248, y = 440)

#comboBox escolher tipo de conversão
comboBox2 = ttk.Combobox(Janela, width=15)
comboBox2['values'] = ('direita para esquerda', 'cima para baixo')
comboBox2.place(x=130, y=440)
comboBox2.bind("<<ComboboxSelected>>",lambda event: atualizar_comboBox)
funcoes.configurar_comboBox2(comboBox2)

#botão calcular a diferença entre as duas imagens
btn_calcular_dif = Button(Janela, text="Diferença",command=funcoes.diferenca_imagem ,width = 15, height = 2)
btn_calcular_dif.pack(pady=5)
btn_calcular_dif.place(x = 750, y = 300)

# botão operação aritmética blending de imagens
btn_blending_img = Button(Janela,text="Blending",command=funcoes.blending_imagem ,width=15, height=2)
btn_blending_img.pack(pady=5)
btn_blending_img.place(x=750, y=250)

# botão média das imagens
btn_media_img = Button(Janela, text="Média",command=funcoes.media_imagem, height=2, width=15)
btn_media_img.pack(pady= 5)
btn_media_img.place(x = 750, y = 350)

# botão equalizar histograma
btn_equalizar_imgA = Button(Janela, text="Equalizar Imagem A", command=funcoes.adicao_imagem, width=30, height=3)
btn_equalizar_imgA.pack(pady=10)
btn_equalizar_imgA.place(x=870, y=700)

# botão para aplicar limiarização da imagem
btn_limiarizacao_imgA = Button(Janela, text="Aplicar Limiar", command=funcoes.aplicar_limiarizacao, width=15, height=2)
btn_limiarizacao_imgA.pack(pady=10)
btn_limiarizacao_imgA.place(x=248, y=490)

# entry valor para aplicar limiarização
entry_valor_limiarizacao = Entry(Janela,font=("Arial", 22), width=5)
entry_valor_limiarizacao.pack(pady=30)
entry_valor_limiarizacao.place(x=155, y=492)
entry_valor_limiarizacao.insert(0, "127")
funcoes.configurar_entry_limiarizacao(entry_valor_limiarizacao)

# botão MAX
btn_MAX_imaA = Button(Janela, text="MAX", command=funcoes.aplicar_filtro_max, width=15, height=2)
btn_MAX_imaA.pack(pady=10)
btn_MAX_imaA.place(x = 1200, y = 50)

# botão MIN
btn_MIN_imgA = Button(Janela, text="MIN",command=funcoes.aplicar_filtro_min, width=15, height=2)
btn_MIN_imgA.pack(pady=10)
btn_MIN_imgA.place(x = 1200, y = 100)

# botão MEDIA
btn_MEDIAA_imgA = Button(Janela, text="MEDIA", command=funcoes.aplicar_filtro_media, width=15, height=2)
btn_MEDIAA_imgA.pack(pady=10)
btn_MEDIAA_imgA.place(x=1200, y=150)

# botão MEDIANA
btn_MEDIANA_imgA = Button(Janela, text="MEDIANA", command=funcoes.aplicar_filtro_mediana, width=15, height=2)
btn_MEDIANA_imgA.pack(pady=10)
btn_MEDIANA_imgA.place(x=1200, y=200)

# botão Suavização Conservativa
btn_SUAVIZACAO_CONSERVATIVA = Button(Janela, text="SUAV. CONSER.", command=funcoes.aplicar_filtro_suavizacao_conservativa, width=15, height=2)
btn_SUAVIZACAO_CONSERVATIVA.pack(pady=10)
btn_SUAVIZACAO_CONSERVATIVA.place(x=1200, y=250)

# botão ORDEM
btn_ORDEM = Button(Janela, text="ORDEM", command=funcoes.aplicar_filtro_ordem, width=15, height=2)
btn_ORDEM.pack(pady=10)
btn_ORDEM.place(x=1200, y=300)

# entry valor ordem
entry_valor_ordem = Entry(Janela, font=("Arial", 22), width=7)
entry_valor_ordem.pack(pady=20)
entry_valor_ordem.place(x=1200, y=350)
entry_valor_ordem.insert(0, "1")
funcoes.configurar_entry_ordem(entry_valor_ordem)

# botão Filtragem Gaussiana
btn_Gaussiana = Button(Janela, text="Gaussiana", command=funcoes.aplicar_filtro_gaussiano, width=15, height=2)
btn_Gaussiana.pack(pady=10)
btn_Gaussiana.place(x=1200, y=400)

# entry valor Gaussiana
entry_valor_gaussiana = Entry(Janela, font=("Arial", 22), width=7)
entry_valor_gaussiana.pack(pady=20)
entry_valor_gaussiana.place(x=1200, y=450)
entry_valor_gaussiana.insert(0, "0.1")
funcoes.configurar_entry_gaussiana(entry_valor_gaussiana)

# botão detecçao de borda primeira ordem Prewitt
btn_prewitt = Button(Janela, text="Prewitt", command=funcoes.aplicar_filtro_prewitt, width=15, height=2)
btn_prewitt.pack(pady=10)
btn_prewitt.place(x=1330, y=50)

# botão detecçao de borda primeira ordem Sobel
btn_sobel = Button(Janela, text="Sobel", command=funcoes.aplicar_filtro_sobel, width=15, height=2)
btn_sobel.pack(pady=10)
btn_sobel.place(x=1330, y=100)

# botão detecçao de borda segunda ordem Lapciano
btn_Lapciano = Button(Janela, text="Lapciano", command=funcoes.aplicar_filtro_laplaciano, width=15, height=2)
btn_Lapciano.pack(pady=10)
btn_Lapciano.place(x=1330, y=150)

# botão operação morfológica dilatação
btn_Dilatacao = Button(Janela, text="Dilatação", command=funcoes.aplicar_dilatacao, width=15, height=2)
btn_Dilatacao.pack(pady=10)
btn_Dilatacao.place(x=1330, y=300)

# botão operação morfológica erosão
btn_Erosao = Button(Janela, text="Erosão", command=funcoes.aplicar_erosao, width=15, height=2)
btn_Erosao.pack(pady=10)
btn_Erosao.place(x=1330, y=350)

# botão operação morfológica Abertura
btn_Abertura = Button(Janela, text="Abertura", command=funcoes.aplicar_abertura, width=15, height=2)
btn_Abertura.pack(pady=10)
btn_Abertura.place(x=1330, y=400)

# botão operação morfológica Fechamento
btn_Fechamento = Button(Janela, text="Fechamento", command=funcoes.aplicar_fechamento, width=15, height=2)
btn_Fechamento.pack(pady=10)
btn_Fechamento.place(x=1330, y=450)

# botão operação morfológica erosão
btn_Contorno = Button(Janela, text="Contorno", command=funcoes.aplicar_contorno, width=15, height=2)
btn_Contorno.pack(pady=10)
btn_Contorno.place(x=1330, y=500)

Janela.mainloop()