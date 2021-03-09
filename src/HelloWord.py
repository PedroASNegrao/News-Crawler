
words_lista = []
lowcase_lista = []
lista = open("../Lista/list.txt", "r", encoding='utf-8')
for line in lista:
    aux = line.replace('\n', '')
    aux = aux
    words_lista.append(aux)

for words in words_lista:
    low = words.lower()
    lowcase_lista.append(low)

words_lista = words_lista + lowcase_lista

test = "A cerimônia ocorre na Capela 4 do Cemitério de Taguatinga, e o sepultamento"

words_test = ["corre", "Capela", "Taguatinga"]
teste_vazio = ['teste']

if teste_vazio:
    print("OK")


"""
for parameters in words_test:
    if test.find(parameters) != -1:
        init = test.find(parameters)
        end = init + len(parameters)

        if (test[init-1].isalpha() == False) and (test[end].isalpha() == False):
            print("FOUND")
        #test[init-1].isalpha()
        #test[]

"""

