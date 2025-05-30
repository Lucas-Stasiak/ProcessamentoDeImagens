from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from tkinter import messagebox
from PIL import Image, ImageTk
import statistics

label_imagem_result = None  
entry_valor_soma = 0  
entry_valor_subtracao = 0
entry_valor_multiplicacao = 0
entry_valor_divisao = 0
btn_reset_campos = None
entry_valor_blending = 0

def configurar_label(label):
    global label_imagem_result
    label_imagem_result = label

def configurar_labelImgA(label):
    global label_imagemA
    label_imagemA = label

def configurar_entry_limiarizacao(entry):
    global entry_valor_limiarizacao 
    entry_valor_limiarizacao = entry

def configurar_entry(entry):
    global entry_valor_soma
    entry_valor_soma = entry

def configurar_entry_subtracao(entry):
    global entry_valor_subtracao
    entry_valor_subtracao = entry

def configurar_entry_multiplicacao(entry):
    global entry_valor_multiplicacao
    entry_valor_multiplicacao = entry

def configurar_entry_divisao(entry):
    global entry_valor_divisao
    entry_valor_divisao = entry

def configurar_entry_blending(entry):
    global entry_valor_blending
    entry_valor_blending = entry

def configurar_btn_reset_campos(btn):
    global btn_reset_campos
    btn_reset_campos = btn

def configurar_comboBox(combobox):
    global comboBox
    comboBox = combobox

def configurar_comboBox2(combobox):
    global comboBox2
    comboBox2 = combobox

def configurar_entry_ordem(entry):
    global entry_valor_ordem
    entry_valor_ordem = entry

def configurar_entry_gaussiana(entry):
    global entry_valor_gaussiana
    entry_valor_gaussiana = entry

def adicao_imagem():

    if verificaEntrada(entry_valor_soma.get()):

        if  entry_valor_soma.get() == "0" or entry_valor_soma.get() == '':

            # Carregar as imagens (com ou sem canal alfa)
            imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
            imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

            # Se imgA ou imgB for 1 bit, convertemos para RGB
            if len(imgA.shape) == 2:  # Imagem de 1 bit ou escala de cinza
                imgA = (imgA > 127).astype(np.uint8) * 255
                imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)  # Converte 1 bit para 3 canais RGB

            if len(imgB.shape) == 2:  # Imagem de 1 bit ou escala de cinza
                imgB = (imgB > 127).astype(np.uint8) * 255
                imgB = cv2.cvtColor(imgB, cv2.COLOR_GRAY2BGR)  # Converte 1 bit para 3 canais RGB

            # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
            if imgA.shape != imgB.shape:
                print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
                return

            # Obter as dimensões das imagens
            altura, largura, canais = imgA.shape

            # Criar uma matriz para a imagem resultante
            img_result = imgA.copy()

            # Converter para uint16 para evitar overflow na soma
            imgA = imgA.astype(np.uint16)
            imgB = imgB.astype(np.uint16)

            # Realizar a soma pixel por pixel
            for y in range(altura):
                for x in range(largura):
                    for c in range(canais):  # Para todos os canais (RGB)
                        soma = imgA[y, x, c] + imgB[y, x, c]
                        img_result[y, x, c] = 255 if soma > 255 else soma

            # Salvar a imagem resultante
            cv2.imwrite("img_result.png", img_result)

            # Exibir a imagem resultante
            img_result_pil = Image.open("img_result.png")
            img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
            img_result_tk = ImageTk.PhotoImage(img_result_pil)
            label_imagem_result.config(image=img_result_tk)
            label_imagem_result.image = img_result_tk
            label_imagem_result.place(x=1500, y=30)
        
        else:

            if int(entry_valor_soma.get()) < 0 or  int(entry_valor_soma.get()) > 255:
                resetarEntradas()
                print("insira valores de 0 a 255")

            else:

                imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

                # Se imgA ou imgB for 1 bit, convertemos para RGB
                if len(imgA.shape) == 2:  # Imagem de 1 bit ou escala de cinza
                    imgA = (imgA > 127).astype(np.uint8) * 255
                    imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)  # Converte 1 bit para 3 canais RGB

                # Obter as dimensões das imagens
                altura, largura, canais = imgA.shape

                # Criar uma matriz para a imagem resultante
                img_result = imgA.copy()

                # Converter para uint16 para evitar overflow na soma
                imgA = imgA.astype(np.uint16)

                # Realizar a soma pixel por pixel
                for y in range(altura):
                    for x in range(largura):
                        for c in range(canais):  # Para todos os canais (RGB)
                            soma = imgA[y, x, c] + int(entry_valor_soma.get())
                            img_result[y, x, c] = 255 if soma > 255 else soma

                # Salvar a imagem resultante
                cv2.imwrite("img_result.png", img_result)
            
                # Exibir a imagem resultante
                img_result_pil = Image.open("img_result.png")
                img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
                img_result_tk = ImageTk.PhotoImage(img_result_pil)
                label_imagem_result.config(image=img_result_tk)
                label_imagem_result.image = img_result_tk
                label_imagem_result.place(x=1500, y=30)
    else:
        resetarEntradas()       

def subtracao_imagem():
    
    if verificaEntrada(entry_valor_subtracao.get()):

            if entry_valor_subtracao.get() == "0" or entry_valor_subtracao.get() == '':
                
                imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
                imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

                # Se imgA ou imgB for 1 bit, converter para RGB
                if len(imgA.shape) == 2:
                    imgA = (imgA > 127).astype(np.uint8) * 255
                    imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

                if len(imgB.shape) == 2:
                    imgB = (imgB > 127).astype(np.uint8) * 255
                    imgB = cv2.cvtColor(imgB, cv2.COLOR_GRAY2BGR)

                # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
                if imgA.shape != imgB.shape:
                    print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
                    return

                # Obter as dimensões das imagens
                altura, largura, canais = imgA.shape

                # Criar uma matriz para a imagem resultante
                img_result = imgA.copy()

                # Converter para int16 para evitar overflow na subtração
                imgA = imgA.astype(np.int16)
                imgB = imgB.astype(np.int16)

                # Realizar a subtração pixel por pixel garantindo que os valores não sejam menores que 0
                for y in range(altura):
                    for x in range(largura):
                        for c in range(canais):  # Para todos os canais (RGB)
                            subtracao = imgA[y, x, c] - imgB[y, x, c]
                            img_result[y, x, c] = max(0, subtracao)  # Garantir que não seja menor que 0

                # Salvar a imagem resultante
                cv2.imwrite("img_result.png", img_result)

                # Exibir a imagem resultante
                img_result_pil = Image.open("img_result.png")
                img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
                img_result_tk = ImageTk.PhotoImage(img_result_pil)
                label_imagem_result.config(image=img_result_tk)
                label_imagem_result.image = img_result_tk
                label_imagem_result.place(x=1500, y=30)

            else:

                if int(entry_valor_subtracao.get()) < 0 or  int(entry_valor_subtracao.get()) > 255:
                    resetarEntradas()
                    print("insira valores de 0 a 255")

                else:

                    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

                    if len(imgA.shape) == 2:
                        imgA = (imgA > 127).astype(np.uint8) * 255
                        imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

                    altura, largura, canais = imgA.shape
                    img_result = imgA.copy()
                    imgA = imgA.astype(np.int16)

                    # Realizar a subtração pixel por pixel garantindo que os valores não sejam menores que 0
                    for y in range(altura):
                        for x in range(largura):
                            for c in range(canais):  # Para todos os canais (RGB)
                                subtracao = imgA[y, x, c] - int(entry_valor_subtracao.get())
                                img_result[y, x, c] = max(0, subtracao)  # Garantir que não seja menor que 0

                    cv2.imwrite("img_result.png", img_result)

                    # Exibir a imagem resultante
                    img_result_pil = Image.open("img_result.png")
                    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
                    img_result_tk = ImageTk.PhotoImage(img_result_pil)
                    label_imagem_result.config(image=img_result_tk)
                    label_imagem_result.image = img_result_tk
                    label_imagem_result.place(x=1500, y=30)
    else:
            resetarEntradas()

def multiplicacao_imagem():
        
        if verificaEntrada(entry_valor_multiplicacao.get()):
            
     
            imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

            if len(imgA.shape) == 2:
                imgA = (imgA > 127).astype(np.uint8) * 255
                imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

            altura, largura, canais = imgA.shape
            img_result = imgA.copy()
            imgA = imgA.astype(np.int16)

            if int(entry_valor_multiplicacao.get()) >= 0 and int(entry_valor_multiplicacao.get()) <= 255:
            # Realizar a subtração pixel por pixel garantindo que os valores não sejam menores que 0
                for y in range(altura):
                 for x in range(largura):
                    for c in range(canais):  # Para todos os canais (RGB)
                        if entry_valor_multiplicacao.get() == "0" or entry_valor_multiplicacao.get() == '':
                            subtracao = imgA[y, x, c] 
                            img_result[y, x, c] = 255 if subtracao > 255 else subtracao
                        else:
                                if int(entry_valor_multiplicacao.get()) > 255:
                                        subtracao = imgA[y, x, c] = 255
                                        img_result[y, x, c] = 255 if subtracao > 255 else subtracao
                                else:
                                        subtracao = imgA[y, x, c] * int(entry_valor_multiplicacao.get())
                                        img_result[y, x, c] = 255 if subtracao > 255 else subtracao


                cv2.imwrite("img_result.png", img_result)

            # Exibir a imagem resultante
                img_result_pil = Image.open("img_result.png")
                img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
                img_result_tk = ImageTk.PhotoImage(img_result_pil)
                label_imagem_result.config(image=img_result_tk)
                label_imagem_result.image = img_result_tk
                label_imagem_result.place(x=1500, y=30)
            else:
             entry_valor_multiplicacao.delete(0, END)  # Remove todo o conteúdo atual
             entry_valor_multiplicacao.insert(0, '') 
             print("valor nao permitido! insira valores de 0 a 255")
        else:
            resetarEntradas()

def divisao_imagem():
        
        if verificaEntrada(entry_valor_divisao.get()):

     
                imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

                if len(imgA.shape) == 2:
                    imgA = (imgA > 127).astype(np.uint8) * 255
                    imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

                altura, largura, canais = imgA.shape
                img_result = imgA.copy()
                imgA = imgA.astype(np.int16)

                if int(entry_valor_divisao.get()) >= 0 and int(entry_valor_divisao.get()) < 256:

                # Realizar a subtração pixel por pixel garantindo que os valores não sejam menores que 0
                    for y in range(altura):
                     for x in range(largura):
                        for c in range(canais):  # Para todos os canais (RGB)
                            if entry_valor_divisao.get() == "0" or entry_valor_divisao.get() == '':
                                subtracao = imgA[y, x, c] 
                                img_result[y, x, c] = max(0, subtracao)
                            else:
                                if int(entry_valor_divisao.get()) > 255:
                                    subtracao = imgA[y, x, c] = 0
                                    img_result[y, x, c] = max(0, subtracao)

                                else:
                                    subtracao = imgA[y, x, c] / int(entry_valor_divisao.get())
                                    img_result[y, x, c] = max(0, subtracao)

                    cv2.imwrite("img_result.png", img_result)

                    # Exibir a imagem resultante
                    img_result_pil = Image.open("img_result.png")
                    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
                    img_result_tk = ImageTk.PhotoImage(img_result_pil)
                    label_imagem_result.config(image=img_result_tk)
                    label_imagem_result.image = img_result_tk
                    label_imagem_result.place(x=1500, y=30)

                else:
                    entry_valor_divisao.delete(0, END)  # Remove todo o conteúdo atual
                    entry_valor_divisao.insert(0, '')  
                    print("Valor nao permitido! insira valores de 0 a 255")
        else:
            resetarEntradas()

def diferenca_imagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
    imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

    # Se imgA ou imgB for 1 bit, converter para RGB
    if len(imgA.shape) == 2:
        imgA = (imgA > 127).astype(np.uint8) * 255
        imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

    if len(imgB.shape) == 2:
        imgB = (imgB > 127).astype(np.uint8) * 255
        imgB = cv2.cvtColor(imgB, cv2.COLOR_GRAY2BGR)

    # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
    if imgA.shape != imgB.shape:
        print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
        return

    # Obter as dimensões das imagens
    altura, largura, canais = imgA.shape

    # Criar matrizes para as imagens resultantes
    imgC = np.zeros_like(imgA)  # C = A - B
    imgD = np.zeros_like(imgB)  # D = B - A
    img_result = np.zeros_like(imgA)  # img_result = C + D

    # Converter para int16 para evitar overflow na subtração
    imgA = imgA.astype(np.int16)
    imgB = imgB.astype(np.int16)

    # Percorrer pixel por pixel para calcular C, D e img_result
    for y in range(altura):
        for x in range(largura):
            for c in range(canais):  # Para todos os canais (RGB)
                C = max(0, imgA[y, x, c] - imgB[y, x, c])  # C = A - B
                D = max(0, imgB[y, x, c] - imgA[y, x, c])  # D = B - A
                imgC[y, x, c] = C
                imgD[y, x, c] = D
                img_result[y, x, c] = min(255, C + D)  # Garantir que não ultrapasse 255

    # Salvar as imagens
    cv2.imwrite("imgC.png", imgC)
    cv2.imwrite("imgD.png", imgD)
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem final no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def inverterImagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

    if imgA is None:
        print("Erro: Imagem não encontrada!")
        return

    # Verificar se a imagem é binária (1 bit)
    if len(imgA.shape) == 2 and np.unique(imgA).size == 2:  # Imagem binária (0 e 255)
        # A imagem binária é 1-bit (preto e branco), então invertemos os valores
        imgA = cv2.bitwise_not(imgA)
        img_result = imgA
    else:
        altura, largura = imgA.shape[:2]  # Para imagens em escala de cinza ou coloridas
        canais = imgA.shape[2] if len(imgA.shape) == 3 else 1  # Se tiver 3 canais, usamos o valor de canais

        img_result = np.zeros_like(imgA)  # Criando uma nova imagem vazia com as mesmas dimensões

        if comboBox2.get() == "direita para esquerda":
            # Espelhar a imagem horizontalmente
            for y in range(altura):
                for x in range(largura):
                    img_result[y, largura - 1 - x] = imgA[y, x]

        elif comboBox2.get() == "cima para baixo":
            # Espelhar a imagem verticalmente
            for y in range(altura):
                for x in range(largura):
                    img_result[altura - 1 - y, x] = imgA[y, x]

    # Salvando a imagem invertida
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem resultante no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def blending_imagem(C = 0):

    C = float(entry_valor_blending.get())

    if float(entry_valor_blending.get()) > 0 and float(entry_valor_blending.get()) < 1:

        imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
        imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

        # Verifica se as imagens foram carregadas corretamente
        if imgA is None or imgB is None:
            print("Erro ao carregar as imagens. Certifique-se de que os arquivos existem.")
            return

        # Se imgA ou imgB for grayscale (1 canal), converter para RGB (3 canais)
        if len(imgA.shape) == 2:
            imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

        if len(imgB.shape) == 2:
            imgB = cv2.cvtColor(imgB, cv2.COLOR_GRAY2BGR)

        # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
        if imgA.shape != imgB.shape:
            print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
            return

        # Obter as dimensões da imagem
        altura, largura, canais = imgA.shape

        # Criar matriz para a imagem resultante
        img_result = np.zeros_like(imgA, dtype=np.float32)

        # Converter as imagens para float32 para evitar erros de precisão
        imgA = imgA.astype(np.float32)
        imgB = imgB.astype(np.float32)

        # Percorrer pixel por pixel para calcular o blending
        for y in range(altura):
            for x in range(largura):
                for c in range(canais):  # Para todos os canais (RGB)
                    img_result[y, x, c] = (C * imgA[y, x, c]) + ((1 - C) * imgB[y, x, c])

        # Garantir que os valores fiquem no intervalo válido (0-255) e converter para uint8
        img_result = np.clip(img_result, 0, 255).astype(np.uint8)

        # Salvar a imagem resultante
        cv2.imwrite("img_result.png", img_result)

        # Exibir a imagem resultante no Tkinter
        img_result_pil = Image.open("img_result.png")
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)
    else:
        print("insira um valor entre 0.0 ate 1.0")
        resetarEntradas()

def converter_imagem():
    imgA = cv2.imread("imagemA.png")
    imgB = cv2.imread("imagemB.png")
    
    if comboBox.get() == 'RGB to 1bit':
        altura, largura, _ = imgA.shape
        img_result = np.zeros((altura, largura), dtype=np.uint8)

        for y in range(altura):
            for x in range(largura):
                # Obtém os valores RGB do pixel
                B, G, R = imgA[y, x]
                # converter para escala de cinza
                Y = int(0.299 * R + 0.587 * G + 0.114 * B)
                # limiar de binarização
                img_result[y, x] = 255 if Y > 127 else 0

        cv2.imwrite("img_result.png", img_result)
        img_result = Image.open("img_result.png")
        img_result = img_result.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result)
        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)
        
     
    elif comboBox.get() == 'RGB to 8bit':
                altura, largura, _ = imgA.shape
                img_result = np.zeros((altura, largura), dtype=np.uint8)

                for y in range(altura):
                    for x in range(largura):
                        # Obtém os valores RGB do pixel
                        B, G, R = imgA[y, x]
                        # converter para escala de cinza
                        Y = int(0.299 * R + 0.587 * G + 0.114 * B)
                        img_result[y, x] = Y
                     

                cv2.imwrite("img_result.png", img_result)
                img_result = Image.open("img_result.png")
                img_result = img_result.resize((350, 350), Image.Resampling.LANCZOS)
                img_result_tk = ImageTk.PhotoImage(img_result)
                label_imagem_result.config(image=img_result_tk)
                label_imagem_result.image = img_result_tk
                label_imagem_result.place(x=1500, y=30)


    elif comboBox.get() == 'to Double':
        
        img_result = cv2.addWeighted(imgA, 0.5, imgB, 0.5, 0)
        cv2.imwrite("img_result.png", img_result)   
        img_result = Image.open("img_result.png")
        img_result = img_result.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result)
        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)
        

    else:
        print("Selecione uma opção de conversão")

def verificaEntrada(entrada):
    if entrada.isdigit() or entrada == '':
        return True
    else:
        return False

def media_imagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
    imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

    # Verifica se as imagens foram carregadas corretamente
    if imgA is None or imgB is None:
        print("Erro ao carregar as imagens. Certifique-se de que os arquivos existem.")
        return

    # Se imgA ou imgB for grayscale (1 canal), converter para RGB (3 canais)
    if len(imgA.shape) == 2:
        imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)

    if len(imgB.shape) == 2:
        imgB = cv2.cvtColor(imgB, cv2.COLOR_GRAY2BGR)

    # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
    if imgA.shape != imgB.shape:
        print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
        return

    # Obter as dimensões da imagem
    altura, largura, canais = imgA.shape

    # Criar matriz para a imagem resultante
    img_result = np.zeros_like(imgA, dtype=np.float32)

    # Converter as imagens para float32 para evitar erros de precisão
    imgA = imgA.astype(np.float32)
    imgB = imgB.astype(np.float32)

    # Percorrer pixel por pixel para calcular a média
    for y in range(altura):
        for x in range(largura):
            for c in range(canais):  # Para todos os canais (RGB)
                img_result[y, x, c] = (imgA[y, x, c] + imgB[y, x, c]) / 2

    # Garantir que os valores fiquem no intervalo válido (0-255) e converter para uint8
    img_result = np.clip(img_result, 0, 255).astype(np.uint8)

    # Salvar a imagem resultante
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem resultante no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def not_imagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

    # Verifica se a imagem foi carregada corretamente
    if imgA is None:
        print("Erro ao carregar a imagem. Certifique-se de que o arquivo existe.")
        return

    # Obter as dimensões da imagem
    altura, largura = imgA.shape[:2]
    
    # Verificar se a imagem tem 4 canais (RGBA)
    if len(imgA.shape) == 3 and imgA.shape[2] == 4:  # Imagem com canal alfa (transparência)
        print("Imagem com transparência detectada (RGBA).")
        canais = 4
        MAX = 255
    elif len(imgA.shape) == 2:  # Imagem em escala de cinza
        canais = 1
        MAX = 255
    else:  # Imagem colorida (RGB)
        canais = 3
        MAX = 255

    # Criar matriz para a imagem resultante
    img_result = np.zeros_like(imgA, dtype=np.uint8)

    # Percorrer pixel por pixel e aplicar a operação NOT
    for y in range(altura):
        for x in range(largura):
            if canais == 1:  # Imagem em escala de cinza
                img_result[y, x] = MAX - imgA[y, x]
            elif canais == 3:  # Imagem colorida (RGB)
                for c in range(canais):
                    img_result[y, x, c] = MAX - imgA[y, x, c]
            elif canais == 4:  # Imagem com transparência (RGBA)
                # Inverter os canais de cor (R, G, B), mas deixar o canal alfa (transparência) inalterado
                for c in range(3):  # Só os três canais de cor
                    img_result[y, x, c] = MAX - imgA[y, x, c]
                img_result[y, x, 3] = imgA[y, x, 3]  # Manter o canal alfa intacto

    # Salvar a imagem resultante
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem resultante no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def and_imagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
    imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

    # Verifica se as imagens foram carregadas corretamente
    if imgA is None or imgB is None:
        print("Erro ao carregar as imagens. Certifique-se de que os arquivos existem.")
        return

    # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
    if imgA.shape != imgB.shape:
        print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
        return

    # Obter as dimensões das imagens
    altura, largura = imgA.shape[:2]

    # Verificar os canais das imagens
    if len(imgA.shape) == 3:
        canais = imgA.shape[2]
    else:
        canais = 1  # Imagem em escala de cinza

    # Criar uma matriz para a imagem resultante
    img_result = np.zeros_like(imgA, dtype=np.uint8)

    # Percorrer pixel por pixel e aplicar a operação AND
    for y in range(altura):
        for x in range(largura):
            if canais == 1:  # Imagem em escala de cinza
                img_result[y, x] = imgA[y, x] & imgB[y, x]
            else:  # Imagem colorida (RGB)
                for c in range(canais):
                    img_result[y, x, c] = imgA[y, x, c] & imgB[y, x, c]

    # Salvar a imagem resultante
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem resultante no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def or_imagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
    imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

    # Verifica se as imagens foram carregadas corretamente
    if imgA is None or imgB is None:
        print("Erro ao carregar as imagens. Certifique-se de que os arquivos existem.")
        return

    # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
    if imgA.shape != imgB.shape:
        print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
        return

    # Obter as dimensões das imagens
    altura, largura = imgA.shape[:2]

    # Verificar os canais das imagens
    if len(imgA.shape) == 3:
        canais = imgA.shape[2]
    else:
        canais = 1  # Imagem em escala de cinza

    # Criar uma matriz para a imagem resultante
    img_result = np.zeros_like(imgA, dtype=np.uint8)

    # Percorrer pixel por pixel e aplicar a operação OR
    for y in range(altura):
        for x in range(largura):
            if canais == 1:  # Imagem em escala de cinza
                img_result[y, x] = imgA[y, x] | imgB[y, x]
            else:  # Imagem colorida (RGB)
                for c in range(canais):
                    img_result[y, x, c] = imgA[y, x, c] | imgB[y, x, c]

    # Salvar a imagem resultante
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem resultante no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def xor_imagem():
    imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)
    imgB = cv2.imread("imagemB.png", cv2.IMREAD_UNCHANGED)

    # Verifica se as imagens foram carregadas corretamente
    if imgA is None or imgB is None:
        print("Erro ao carregar as imagens. Certifique-se de que os arquivos existem.")
        return

    # Garantir que ambas as imagens tenham o mesmo tamanho e número de canais
    if imgA.shape != imgB.shape:
        print(f"As imagens precisam ter o mesmo tamanho e número de canais. imgA shape: {imgA.shape}, imgB shape: {imgB.shape}")
        return

    # Obter as dimensões das imagens
    altura, largura = imgA.shape[:2]

    # Verificar os canais das imagens
    if len(imgA.shape) == 3:
        canais = imgA.shape[2]
    else:
        canais = 1  # Imagem em escala de cinza

    # Criar uma matriz para a imagem resultante
    img_result = np.zeros_like(imgA, dtype=np.uint8)

    # Percorrer pixel por pixel e aplicar a operação XOR
    for y in range(altura):
        for x in range(largura):
            if canais == 1:  # Imagem em escala de cinza
                img_result[y, x] = imgA[y, x] ^ imgB[y, x]
            else:  # Imagem colorida (RGB)
                for c in range(canais):
                    img_result[y, x, c] = imgA[y, x, c] ^ imgB[y, x, c]

    # Salvar a imagem resultante
    cv2.imwrite("img_result.png", img_result)

    # Exibir a imagem resultante no Tkinter
    img_result_pil = Image.open("img_result.png")
    img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
    img_result_tk = ImageTk.PhotoImage(img_result_pil)

    label_imagem_result.config(image=img_result_tk)
    label_imagem_result.image = img_result_tk
    label_imagem_result.place(x=1500, y=30)

def resetarEntradas():

           entry_valor_divisao.delete(0, END)  # Remove todo o conteúdo atual
           #entry_valor_divisao.insert(0, "0")  # Define o valor como "0"
           entry_valor_multiplicacao.delete(0, END)
           entry_valor_soma.delete(0, END)
           entry_valor_subtracao.delete(0, END)
           #entry_valor_multiplicacao.insert(0, "0")
           #entry_valor_soma.insert(0, "0")
           #entry_valor_subtracao.insert(0, "0")
           entry_valor_blending.delete(0, END)
           entry_valor_blending.insert(0, "0.8")
           entry_valor_limiarizacao.delete(0, END)
           entry_valor_limiarizacao.insert(0, "127")
           entry_valor_ordem.delete(0, END)
           entry_valor_ordem.insert(0, "1")
           entry_valor_gaussiana.delete(0, END)
           entry_valor_gaussiana.insert(0, "0.1")



def aplicar_limiarizacao():
    if verificaEntrada(entry_valor_limiarizacao.get()):
        try:
            # Lê a imagem
            imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

            # Verifica se a imagem é em escala de cinza
            if len(imgA.shape) == 2:  # Imagem em escala de cinza
                imgA = (imgA > 127).astype(np.uint8) * 255
                imgA = cv2.cvtColor(imgA, cv2.COLOR_GRAY2BGR)  # Converte para RGB para o cálculo do limiar

            altura, largura, canais = imgA.shape
            valor_limiar = int(entry_valor_limiarizacao.get())

            if 0 <= valor_limiar <= 255:  # Verifica se o valor de limiarização é válido
                # Cria a imagem binarizada com o mesmo tamanho da original
                img_result = np.zeros((altura, largura), dtype=np.uint8)

                for y in range(altura):
                    for x in range(largura):
                        # Obtém os valores RGB do pixel
                        B, G, R = imgA[y, x]
                        # Calcula o valor de cinza (escala de cinza)
                        Y = int(0.299 * R + 0.587 * G + 0.114 * B)
                        # Aplica o limiar
                        img_result[y, x] = 255 if Y > valor_limiar else 0

                # Salva a imagem binarizada
                cv2.imwrite("img_result.png", img_result)

                # Exibe a imagem no Tkinter
                img_result_pil = Image.open("img_result.png")
                img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
                img_result_tk = ImageTk.PhotoImage(img_result_pil)

                label_imagem_result.config(image=img_result_tk)
                label_imagem_result.image = img_result_tk
                label_imagem_result.place(x=1500, y=30)
            else:
                entry_valor_limiarizacao.delete(0, END)  # Remove o conteúdo atual
                entry_valor_limiarizacao.insert(0, '127')  # Define o valor padrão
                print("Valor não permitido! Insira valores de 0 a 255.")
        except Exception as e:
            print(f"Erro ao processar a imagem: {e}")
            resetarEntradas()
    else:
        resetarEntradas()

# funçao MAX
def aplicar_filtro_max():
    try:
        # Lê a imagem
        imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

        # Verifica se a imagem é em escala de cinza
        if len(imgA.shape) == 2:  # Imagem em escala de cinza
            altura, largura = imgA.shape
            # Cria uma imagem resultante de escala de cinza
            img_result = np.zeros((altura, largura), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Inicializa o valor máximo
                    max_val = 0

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém o valor do pixel vizinho
                                val = imgA[ny, nx]

                                # Atualiza o valor máximo
                                max_val = max(max_val, val)

                    # Atribui o valor máximo calculado ao pixel da imagem resultante
                    img_result[y, x] = max_val

        else:
            # Se for uma imagem RGB, tratamos da mesma forma que antes
            altura, largura, canais = imgA.shape
            img_result = np.zeros((altura, largura, 3), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Inicializa os valores máximos para cada canal
                    max_R = max_G = max_B = 0

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém os valores RGB do pixel vizinho
                                B, G, R = imgA[ny, nx]

                                # Atualiza os valores máximos para cada canal
                                max_B = max(max_B, B)
                                max_G = max(max_G, G)
                                max_R = max(max_R, R)

                    # Atribui os valores máximos calculados aos canais da imagem resultante
                    img_result[y, x] = [max_B, max_G, max_R]

        # Salva a imagem resultante
        cv2.imwrite("img_result_max.png", img_result)

        # Exibe a imagem no Tkinter
        img_result_pil = Image.open("img_result_max.png")
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        resetarEntradas()


def aplicar_filtro_min():
    try:
        # Lê a imagem
        imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

        # Verifica se a imagem é em escala de cinza
        if len(imgA.shape) == 2:  # Imagem em escala de cinza
            altura, largura = imgA.shape
            # Cria uma imagem resultante de escala de cinza
            img_result = np.zeros((altura, largura), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Inicializa o valor mínimo
                    min_val = 255  # Valor máximo possível para um pixel em escala de cinza

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém o valor do pixel vizinho
                                val = imgA[ny, nx]

                                # Atualiza o valor mínimo
                                min_val = min(min_val, val)

                    # Atribui o valor mínimo calculado ao pixel da imagem resultante
                    img_result[y, x] = min_val

        else:
            # Se for uma imagem RGB, tratamos da mesma forma que antes
            altura, largura, canais = imgA.shape
            img_result = np.zeros((altura, largura, 3), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Inicializa os valores mínimos para cada canal
                    min_R = min_G = min_B = 255  # O valor mínimo começa em 255 para cada canal

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém os valores RGB do pixel vizinho
                                B, G, R = imgA[ny, nx]

                                # Atualiza os valores mínimos para cada canal
                                min_B = min(min_B, B)
                                min_G = min(min_G, G)
                                min_R = min(min_R, R)

                    # Atribui os valores mínimos calculados aos canais da imagem resultante
                    img_result[y, x] = [min_B, min_G, min_R]

        # Salva a imagem resultante
        cv2.imwrite("img_result_min.png", img_result)

        # Exibe a imagem no Tkinter
        img_result_pil = Image.open("img_result_min.png")
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        resetarEntradas()







def aplicar_filtro_media():
    try:
        # Lê a imagem
        imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

        # Verifica se a imagem é em escala de cinza
        if len(imgA.shape) == 2:  # Imagem em escala de cinza
            altura, largura = imgA.shape
            # Cria uma imagem resultante de escala de cinza
            img_result = np.zeros((altura, largura), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Lista para armazenar os valores dos pixels vizinhos
                    vizinhos = []

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém o valor do pixel vizinho
                                vizinhos.append(imgA[ny, nx])

                    # Calcula a média dos pixels vizinhos
                    media_val = int(np.mean(vizinhos))
                    # Atribui o valor médio calculado ao pixel da imagem resultante
                    img_result[y, x] = media_val

        else:
            # Se for uma imagem RGB, tratamos da mesma forma que antes
            altura, largura, canais = imgA.shape
            img_result = np.zeros((altura, largura, 3), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Listas para armazenar os valores dos canais vizinhos
                    vizinhos_R, vizinhos_G, vizinhos_B = [], [], []

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém os valores RGB do pixel vizinho
                                B, G, R = imgA[ny, nx]
                                vizinhos_B.append(B)
                                vizinhos_G.append(G)
                                vizinhos_R.append(R)

                    # Calcula a média dos pixels vizinhos para cada canal
                    media_B = int(np.mean(vizinhos_B))
                    media_G = int(np.mean(vizinhos_G))
                    media_R = int(np.mean(vizinhos_R))

                    # Atribui os valores médios calculados aos canais da imagem resultante
                    img_result[y, x] = [media_B, media_G, media_R]

        # Salva a imagem resultante
        cv2.imwrite("img_result_media.png", img_result)

        # Exibe a imagem no Tkinter
        img_result_pil = Image.open("img_result_media.png")
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        resetarEntradas()


def aplicar_filtro_mediana():
    try:
        # Lê a imagem
        imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

        # Verifica se a imagem é em escala de cinza
        if len(imgA.shape) == 2:  # Imagem em escala de cinza
            altura, largura = imgA.shape
            # Cria uma imagem resultante de escala de cinza
            img_result = np.zeros((altura, largura), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Lista para armazenar os valores dos pixels vizinhos
                    vizinhos = []

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém o valor do pixel vizinho
                                vizinhos.append(imgA[ny, nx])

                    # Calcula a mediana dos pixels vizinhos
                    mediana_val = int(np.median(vizinhos))
                    # Atribui o valor da mediana calculado ao pixel da imagem resultante
                    img_result[y, x] = mediana_val

        else:
            # Se for uma imagem RGB, tratamos da mesma forma que antes
            altura, largura, canais = imgA.shape
            img_result = np.zeros((altura, largura, 3), dtype=np.uint8)

            # Tamanho fixo da janela do filtro (3x3)
            tamanho_filtro = 3
            raio = tamanho_filtro // 2  # Raio da janela (meia largura do filtro)

            # Loop para percorrer os pixels da imagem
            for y in range(altura):
                for x in range(largura):
                    # Listas para armazenar os valores dos canais vizinhos
                    vizinhos_R, vizinhos_G, vizinhos_B = [], [], []

                    # Loop para percorrer os pixels vizinhos dentro da janela do filtro
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            # Calcula as coordenadas do pixel vizinho
                            ny, nx = y + dy, x + dx

                            # Verifica se o pixel vizinho está dentro dos limites da imagem
                            if 0 <= ny < altura and 0 <= nx < largura:
                                # Obtém os valores RGB do pixel vizinho
                                B, G, R = imgA[ny, nx]
                                vizinhos_B.append(B)
                                vizinhos_G.append(G)
                                vizinhos_R.append(R)

                    # Calcula a mediana dos pixels vizinhos para cada canal
                    mediana_B = int(np.median(vizinhos_B))
                    mediana_G = int(np.median(vizinhos_G))
                    mediana_R = int(np.median(vizinhos_R))

                    # Atribui os valores da mediana calculados aos canais da imagem resultante
                    img_result[y, x] = [mediana_B, mediana_G, mediana_R]

        # Salva a imagem resultante
        cv2.imwrite("img_result_mediana.png", img_result)

        # Exibe a imagem no Tkinter
        img_result_pil = Image.open("img_result_mediana.png")
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
        resetarEntradas()



def aplicar_filtro_ordem():
    if verificaEntrada(entry_valor_ordem.get()):
        try:
            # Lê a imagem
            imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

            # Obtém o valor de ordem da entrada
            valor_ordem = int(entry_valor_ordem.get())

            # Verifica se o valor de ordem é válido
            if valor_ordem < 0:
                print("O valor de ordem deve ser maior ou igual a 0.")
                resetarEntradas() 
                return
           

            # Verifica se a imagem é em escala de cinza
            if len(imgA.shape) == 2:  # Imagem em escala de cinza
                altura, largura = imgA.shape
                # Cria uma imagem resultante de escala de cinza
                img_result = np.zeros((altura, largura), dtype=np.uint8)

                # Tamanho fixo da janela do filtro (3x3)
                tamanho_filtro = 3
                raio = tamanho_filtro // 2

                # Loop para percorrer os pixels da imagem
                for y in range(altura):
                    for x in range(largura):
                        vizinhos = []

                        # Loop para capturar os vizinhos
                        for dy in range(-raio, raio + 1):
                            for dx in range(-raio, raio + 1):
                                ny, nx = y + dy, x + dx

                                # Verifica os limites
                                if 0 <= ny < altura and 0 <= nx < largura:
                                    vizinhos.append(imgA[ny, nx])

                        # Ordena os valores e seleciona o valor baseado na ordem
                        vizinhos.sort()
                        valor_filtro = vizinhos[min(valor_ordem, len(vizinhos) - 1)]
                        img_result[y, x] = valor_filtro

            else:
                # Tratamento para imagens RGB
                altura, largura, canais = imgA.shape
                img_result = np.zeros((altura, largura, 3), dtype=np.uint8)

                # Tamanho fixo da janela do filtro (3x3)
                tamanho_filtro = 3
                raio = tamanho_filtro // 2

                # Loop para percorrer os pixels da imagem
                for y in range(altura):
                    for x in range(largura):
                        vizinhos_R, vizinhos_G, vizinhos_B = [], [], []

                        # Loop para capturar os vizinhos
                        for dy in range(-raio, raio + 1):
                            for dx in range(-raio, raio + 1):
                                ny, nx = y + dy, x + dx

                                # Verifica os limites
                                if 0 <= ny < altura and 0 <= nx < largura:
                                    B, G, R = imgA[ny, nx]
                                    vizinhos_B.append(B)
                                    vizinhos_G.append(G)
                                    vizinhos_R.append(R)

                        # Ordena os valores e seleciona o valor baseado na ordem
                        vizinhos_R.sort()
                        vizinhos_G.sort()
                        vizinhos_B.sort()

                        valor_R = vizinhos_R[min(valor_ordem, len(vizinhos_R) - 1)]
                        valor_G = vizinhos_G[min(valor_ordem, len(vizinhos_G) - 1)]
                        valor_B = vizinhos_B[min(valor_ordem, len(vizinhos_B) - 1)]

                        img_result[y, x] = [valor_B, valor_G, valor_R]

            # Salva a imagem resultante
            cv2.imwrite("img_result_ordem.png", img_result)

            # Exibe a imagem no Tkinter
            img_result_pil = Image.open("img_result_ordem.png")
            img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
            img_result_tk = ImageTk.PhotoImage(img_result_pil)

            label_imagem_result.config(image=img_result_tk)
            label_imagem_result.image = img_result_tk
            label_imagem_result.place(x=1500, y=30)

        except Exception as e:
            print(f"Erro ao processar a imagem: {e}")
            resetarEntradas()
    else:
        resetarEntradas()



def aplicar_filtro_suavizacao_conservativa(caminho_imagem="imagemA.png", tamanho_filtro=3):
    try:
        # Carrega a imagem
        imgA = cv2.imread(caminho_imagem, cv2.IMREAD_UNCHANGED)
        if imgA is None:
            raise ValueError("Imagem não encontrada ou erro ao carregar a imagem.")

        # Cria a imagem de saída com mesmas dimensões e tipo da imagem carregada
        img_result = np.zeros_like(imgA)
        raio = tamanho_filtro // 2
        
        # Se a imagem estiver em escala de cinza (2D)
        if len(imgA.shape) == 2:
            altura, largura = imgA.shape
            for y in range(altura):
                for x in range(largura):
                    vizinhos = []
                    # Itera pela vizinhança 3x3 ignorando o pixel central
                    for dy in range(-raio, raio + 1):
                        for dx in range(-raio, raio + 1):
                            ny, nx = y + dy, x + dx
                            if (dy, dx) != (0, 0) and 0 <= ny < altura and 0 <= nx < largura:
                                vizinhos.append(imgA[ny, nx])
                    
                    valor_pixel = imgA[y, x]
                    if vizinhos:
                        min_vizinho = min(vizinhos)
                        max_vizinho = max(vizinhos)
                        # Se o pixel estiver abaixo do mínimo ou acima do máximo, corrige
                        if valor_pixel < min_vizinho:
                            img_result[y, x] = min_vizinho
                        elif valor_pixel > max_vizinho:
                            img_result[y, x] = max_vizinho
                        else:
                            img_result[y, x] = valor_pixel
                    else:
                        img_result[y, x] = valor_pixel
        
        # Se a imagem for colorida (3D)
        else:
            altura, largura, canais = imgA.shape
            for y in range(altura):
                for x in range(largura):
                    # Processa os 3 primeiros canais (assumindo RGB) dinamicamente
                    for c in range(min(3, canais)):
                        vizinhos = []
                        for dy in range(-raio, raio + 1):
                            for dx in range(-raio, raio + 1):
                                ny, nx = y + dy, x + dx
                                if (dy, dx) != (0, 0) and 0 <= ny < altura and 0 <= nx < largura:
                                    vizinhos.append(imgA[ny, nx, c])
                        
                        valor_pixel = imgA[y, x, c]
                        if vizinhos:
                            min_vizinho = min(vizinhos)
                            max_vizinho = max(vizinhos)
                            if valor_pixel < min_vizinho:
                                img_result[y, x, c] = min_vizinho
                            elif valor_pixel > max_vizinho:
                                img_result[y, x, c] = max_vizinho
                            else:
                                img_result[y, x, c] = valor_pixel
                        else:
                            img_result[y, x, c] = valor_pixel
                    # Se existir canal alfa (imagem RGBA), copia-o sem alteração
                    if canais == 4:
                        img_result[y, x, 3] = imgA[y, x, 3]

        # Conversão para exibição com PIL sem precisar salvar em disco
        if len(imgA.shape) == 2:
            img_result_pil = Image.fromarray(img_result)
        else:
            # Converter de BGR (formato do OpenCV) para RGB
            img_result_rgb = cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB)
            img_result_pil = Image.fromarray(img_result_rgb)

        # Redimensiona a imagem para exibição (350 x 350 pixels, por exemplo)
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        # Atualiza o label do Tkinter (certifique-se que "label_imagem_result" esteja definido no seu contexto)
        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

def aplicar_filtro_gaussiano():
    try:
        import math

        # Lê a imagem
        imgA = cv2.imread("imagemA.png", cv2.IMREAD_UNCHANGED)

        sigma = float(entry_valor_gaussiana.get())  # valor do desvio padrão (pode ser ajustável)
        tamanho_filtro = 3
        raio = tamanho_filtro // 2

        # Criação do kernel Gaussiano 3x3
        kernel = np.zeros((tamanho_filtro, tamanho_filtro), dtype=np.float32)
        soma = 0.0
        for y in range(-raio, raio + 1):
            for x in range(-raio, raio + 1):
                valor = (1 / (2 * math.pi * sigma**2)) * math.exp(-(x**2 + y**2) / (2 * sigma**2))
                kernel[y + raio, x + raio] = valor
                soma += valor
        kernel /= soma  # Normaliza o kernel

        # Aplica o filtro Gaussiano na imagem
        if len(imgA.shape) == 2:
            altura, largura = imgA.shape
            img_result = np.zeros_like(imgA, dtype=np.uint8)
            for y in range(raio, altura - raio):
                for x in range(raio, largura - raio):
                    valor = 0.0
                    for ky in range(-raio, raio + 1):
                        for kx in range(-raio, raio + 1):
                            valor += imgA[y + ky, x + kx] * kernel[ky + raio, kx + raio]
                    img_result[y, x] = np.clip(valor, 0, 255)
        else:
            altura, largura, canais = imgA.shape
            img_result = np.zeros_like(imgA, dtype=np.uint8)
            for y in range(raio, altura - raio):
                for x in range(raio, largura - raio):
                    for c in range(canais):
                        valor = 0.0
                        for ky in range(-raio, raio + 1):
                            for kx in range(-raio, raio + 1):
                                valor += imgA[y + ky, x + kx, c] * kernel[ky + raio, kx + raio]
                        img_result[y, x, c] = np.clip(valor, 0, 255)

        # Salva e exibe a imagem resultante
        cv2.imwrite("img_result_gaussiano.png", img_result)

        img_result_pil = Image.open("img_result_gaussiano.png")
        img_result_pil = img_result_pil.resize((350, 350), Image.Resampling.LANCZOS)
        img_result_tk = ImageTk.PhotoImage(img_result_pil)

        label_imagem_result.config(image=img_result_tk)
        label_imagem_result.image = img_result_tk
        label_imagem_result.place(x=1500, y=30)

    except Exception as e:
        print(f"Erro ao aplicar filtro Gaussiano: {e}")
        resetarEntradas()
