from deep_translator import GoogleTranslator

print('=-=' * 20)
print('BEM VINDO AO SEU SITE DE TRADUÇÃO')
print('É SIMPLES, BASTA SELECIONAR A OPÇÃO DO IDIOMA QUE VOCÊ QUER TRADUZIR:')
print('=-=' * 20)
print('\033[92mOPÇÃO 1 = INGLÊS\033[0m\n'
      '\033[92mOPÇÃO 2 = ESPANHOL\033[0m\n'
      '\033[92mOPÇÃO 3 = FRANCÊS\033[0m\n'
      '\033[92mOPÇÃO 4 = ALEMÃO\033[0m\n'
      '\033[92mOPÇÃO 5 = INGLÊS, ESPANHOL, FRANCÊS E ALEMÃO\033[0m')

idioma_selecionado = int(input('\033[96mQual o IDIOMA que você quer que traduza? \033[0m'))


def traduzir_para_ingles(frase):
    tradutor = GoogleTranslator(source="pt", target="en")
    traducao = tradutor.translate(frase)
    return traducao

def traduzir_para_espanhol(frase):
    tradutor = GoogleTranslator(source="pt", target="es")
    traducao = tradutor.translate(frase)
    return traducao

def traduzir_para_frances(frase):
    tradutor = GoogleTranslator(source="pt", target= "fr")
    traducao = tradutor.translate(frase)
    return traducao

def traduzir_para_alemao (frase):
    tradutor = GoogleTranslator(source="pt", target="de")
    traducao = tradutor.translate(frase)
    return traducao

if idioma_selecionado == 1:
    frase_ingles = str(input('Escreva o que quer traduzir para o INGLÊS> '))
    traducao = traduzir_para_ingles(frase_ingles)
    print(f'A tradução da sua frase é: \033[91m{traducao}\033[0m')

elif idioma_selecionado == 2:
    frase_espanhol = str(input('Escreva o que quer traduzir para o ESPANHOL> '))
    traducao = traduzir_para_espanhol(frase_espanhol)
    print(f'A tradução da sua frase é: \033[91m{traducao}\033[0m')

elif idioma_selecionado == 3:
    frase_frances = str(input('Escreva o que quer traduzir para o FRANCÊS> '))
    traducao = traduzir_para_frances (frase_frances)
    print(f'A tradução da sua frase é: \033[91m{traducao}\033[0m')

elif idioma_selecionado == 4:
    frase_alemao = str(input('Escreva o que quer traduzir pro ALEMÃO> '))
    traducao = traduzir_para_alemao (frase_alemao)
    print(f'A tradução da sua frase é: \033[91m{traducao}\033[0m')

elif idioma_selecionado == 5:
    frase = str(input('Escreva o que quer traduzir> '))
    traducao_ingles = traduzir_para_ingles(frase)
    traducao_espanhol = traduzir_para_espanhol(frase)
    traducao_frances = traduzir_para_frances(frase)
    traducao_alemao = traduzir_para_alemao(frase)

    print('A tradução da sua frase é:')
    print(f'Para INGLÊS: \033[91m{traducao_ingles}\033[0m')
    print(f'Para ESPANHOL: \033[91m{traducao_espanhol}\033[0m')
    print(f'Para FRANCÊS: \033[91m{traducao_frances}\033[0m')
    print(f'Para ALEMÃO: \033[91m{traducao_alemao}\033[0m')

else:
    print('-' * 20)
    print('\033[91mDesculpe, opção marcada não existe.\033[0m')
    print('-' * 20)
