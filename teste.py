
#1. Reverter as ordens das palavras:

def reverter_ordem_frase(frase):
 palavras = frase.split() 
palavras_revertidas = palavras[::-1] 
frase_revertida = ' '.join(palavras_revertidas)
 return frase_revertida

frase_original = "Hello, World! OpenAI is Amazing" 
frase_revertida = reverter_ordem_frase(frase_original) 
print(frase_revertida)

#2. Remoção dos caracteres duplicados:

def remover_caracteres_duplicados(frase): 
caracteres_unicos = set() nova_frase = ""

for char in frase:
    if char not in caracteres_unicos:
        caracteres_unicos.add(char)
        nova_frase += char

return nova_frase   
frase_original = "Hello, World!" 
frase_sem_duplicados = remover_caracteres_duplicados(frase_original)
 print(frase_sem_duplicados)

#3. Uma substring palidroma mais longa da string a seguir: "babad"

def encontrar_palindromo(s):
if len(s) < 2: return s

inicio = 0
fim = 0

for i in range(len(s)):
    len1 = expandir_ao_redor_do_centro(s, i, i)
    len2 = expandir_ao_redor_do_centro(s, i, i + 1)
    length = max(len1, len2)

    if length > fim - inicio:
        inicio = i - (length - 1) // 2
        fim = i + length // 2

return s[inicio:fim+1]
def expandir_ao_redor_do_centro(s, esquerda, direita): 
	while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]: esquerda -= 1 direita += 1

return direita - esquerda - 1
string_original = "babad" 
substring_palindromo = encontrar_palindromo(string_original)
 print(substring_palindromo)

#4. Coloque em maiuscula a primeira letra de cada palavra dentro da frase: 
def capitalizar_primeira_letra(frase): frases = frase.split('. ') frases_capitalizadas = []

for f in frases:
    frase_capitalizada = f.capitalize()
    frases_capitalizadas.append(frase_capitalizada)

nova_frase = '. '.join(frases_capitalizadas)

return nova_frase
texto_original = "hello. how are you? i'm fine, thank you." 
texto_transformado = capitalizar_primeira_letra(texto_original) 
print(texto_transformado)

#5. verifique se a string é um anagrama de um palindromo na frase a seguir:"racecar"

def verifica_anagrama_palindromo(string): 
ocorrencias = {}

for char in string:
    if char in ocorrencias:
        ocorrencias[char] += 1
    else:
        ocorrencias[char] = 1

impares = 0
for count in ocorrencias.values():
    if count % 2 != 0:
        impares += 1
        if impares > 1:
            return False

return True
string = "racecar" anagrama_palindromo = verifica_anagrama_palindromo(string) 
print(anagrama_palindromo)
