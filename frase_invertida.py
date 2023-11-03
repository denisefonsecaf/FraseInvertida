#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Escreva uma função que:
#a) Receba uma frase como parâmetro.
#b) Retorne uma nova frase com cada palavra com as letras invertidas.

def frase_invertida_funcao(frase):
    palavras = frase.split() # Divide a frase em palavras
    
    palavras_invertidas = [] # Inicializa uma lista para armazenar as palavras invertidas
    
    # Inverte as letras de cada palavra e as adiciona à lista de palavras invertidas
    for palavra in palavras:
        palavra_invertida = palavra[::-1]
        palavras_invertidas.append(palavra_invertida)
    
    # Une as palavras invertidas em uma nova frase
    nova_frase = ' '.join(palavras_invertidas)
    
    return nova_frase

# Exemplo de uso da função
frase_original = "Me desculpe pelo o atraso"
frase_invertida = frase_invertida_funcao(frase_original)
print(f"Frase original: {frase_original}")
print(f"Frase com letras invertidas: {frase_invertida}")