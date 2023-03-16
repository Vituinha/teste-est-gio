#Primeira maneira e mais simples de realizar o procedimento
texto = "Texto que deve ser invertido"
print(texto[::-1])

#Segunda forma de realizar o procedimento solicitado

#Definindo variável auxiliar para realizar a inverção e a lista que receberá a string invertida
str_invertida = []
aux = -1

#Definindo função que converte uma string para uma lista de python
def ConverteParaString(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

#Transformando String em lista
str = ConverteParaString("Texto que deve ser invertido")

#Criando uma nova lista com os caracteres invertidos
while(len(str) > ((aux * - 1) - 1)):
    str_invertida.append(str[aux])
    aux = aux - 1
    str.pop

#Mostrando em tela a nova string gerada
print("".join(str_invertida))