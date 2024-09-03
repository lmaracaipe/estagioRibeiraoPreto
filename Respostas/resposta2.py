#2 - Verificar a existência da letra 'a' em uma string e contar suas ocorrências


def contar_letra_a(s):
    s_lower = s.lower()
    contador = s_lower.count('a')
    return contador

# String a ser verificada (pode ser modificada ou recebida via entrada)
texto = "Abracadabra"

quantidade = contar_letra_a(texto)

if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
