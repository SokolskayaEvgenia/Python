"""1. Создайте программу, заполняющую двухмерный список символами по образцу: А​

А Б​

А Б В​

…..​

А Б В Г …..	Ь Э ​

А Б В Г …..	Ь Э Ю​

А Б В Г …..	Ь Э Ю Я​"""

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
b = []
for i in range(0,len(alphabet)+1):
    for j in range (1,len(alphabet)+1):
        if len(b)> len(alphabet)-1:
            break
        b.append(alphabet[i:j])
print(b)



