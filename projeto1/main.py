print("Projeto 1")

variavel_tipo_string = "Conjunto de caracteres alfanuméricos"
variavel_tipo_int = 12  # Número inteiro
variavel_tipo_float = 4.5  # Número com casas decimais
variavel_tipo_bool = True  # Booleano
variavel_tipo_lista = [1, 2, 1.2, "Luanny", "Emanuelly", True]
variavel_tipo_dicionario = {
    "nome": "Ismael",
    "idade": 23,
}
variavel_tipo_tupla = ("Jesus", 33, "XD")
variavel_tipo_comentario = """Um comentário atribuido a uma variável vira uma frase"""

print(variavel_tipo_string)
print(variavel_tipo_float)
print(variavel_tipo_float)
print(variavel_tipo_bool)
print(variavel_tipo_lista)
print(variavel_tipo_dicionario)
print(variavel_tipo_tupla)
print(variavel_tipo_comentario)

nome = input("digite seu nome:")

print("Seu nome é " + nome)
print("De novo, seu nome é %s %s" % (nome, "XD"))
print("Disponha, {} {}".format("Senhor", nome))
print(f'Seu nome é {nome} meu nome é {variavel_tipo_dicionario["nome"]}')
