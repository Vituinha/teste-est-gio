#Valor a ser validado pela sequencia
valor = 13

#Variáveis validadoras
Numero_1 = 0
Numero_2 = 1
Numero_validador = 0

#Testa a sequência de Fibonacci para o valor desejado
while(valor > Numero_validador):
    Numero_validador = Numero_1 + Numero_2
    Numero_1 = Numero_2
    Numero_2 = Numero_validador

#Valida se o valor está na sequência
if(valor == 0 or valor == Numero_validador):
    print(valor, "está na sequência de Fibonacci")
else:
    print(valor, "não está na sequência de Fibonacci")
