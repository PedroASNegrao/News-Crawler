
words_lista = []
lowcase_lista = []
lista = open("Lista/list.txt", "r", encoding='utf-8')
for line in lista:
    aux = line.replace('\n', '')
    aux = aux + ' '
    words_lista.append(aux)

for words in words_lista:
    low = words.lower()
    low = ' ' + low + ' '
    lowcase_lista.append(low)

words_lista = words_lista + lowcase_lista




