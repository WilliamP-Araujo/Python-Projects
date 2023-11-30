#Teste de formated Strings

nome= "Marcos"
sobrenome= "Silva"
profissao= "Programador"


texto = "O " + nome +""+ sobrenome + " e um excelente " + "["+ profissao + "]"

texto2 = f" {nome} {sobrenome} e um excelente [{profissao}]"

print(texto2)

print(texto)

#Teste sem supervisão

nome2 = "Daphne"
sobrenome2 = "Ribeiro"
objeto = "Celular"


texto3= f" A {nome2} {sobrenome2} quer um {objeto} novo porém ainda lhe falta monetario"

print(texto3)

#Terceiro teste

#Dentro das variavéis existe um caracter não reconhecido dentro da ASCII, porém isso não causara nenhum problema
nome3= "Felipe "
sobrenome3= "Lunkes  Fin"
país="croacia"

texto4= "O " + nome3 + "" + sobrenome3 + " precisou viajar para " + país+" recentemente"

print(texto4)


#Metodos de Strings

mensagem = "                  Eu adoro macarrão"
#Toda vez que necessario inserir um metodo dentro de uma String, basta inserir um "." depois da variavel em print.
print(mensagem.lower())
#Existem varias funções que voce pode agregar dentro de uma String
print(mensagem.upper())
#Varias mesmo.
print(mensagem.strip())