""" Сначала неправильно прочитала задание
и написала программу из арабских в римские. Обратный перевод: нашла в интеренете использовала
библиотеку roman"""

import roman

"""4. Написать программу преобразующую произвольное целое число до 4000,
написанное римскими цифрами, в арабские. (
Стандартные обозначения цифр: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500,
M = 1000, числа 9 и 90 записываются как IX и XC,
число 3888 как MMMDCCCLXXXVIII, число 989 как IXM и т.д.)
Для уменьшения размеров программы можно использовать рекурсию.​"""

roman_thousand = {1: 'M', 2: 'MM', 3: 'MMM'}
roman_hundred = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
roman_ten = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
roman_one = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}

number = input("Введите произвольное целое число до 4000: ")
if number[0] == '0' or number.isdigit() == 0:
    print("Введите корректное число!")
else:
    if len(number) == 4:
        thousand = int(number[0])
        hundred = int(number[1])
        ten = int(number[2])
        one = int(number[3])
        if hundred == 0:
            if ten == 0:
                if one == 0:
                    roman_number = str(roman_thousand.get(thousand))
                else:
                    roman_number = str(roman_thousand.get(thousand)) + str(roman_one.get(one))
            else:
                if one == 0:
                    roman_number = str(roman_thousand.get(thousand)) + str(roman_ten.get(ten))
                else:
                    roman_number = str(roman_thousand.get(thousand)) + str(roman_ten.get(ten)) + str(roman_one.get(one))
        elif ten == 0:
            if one == 0:
                roman_number = str(roman_thousand.get(thousand)) + str(roman_hundred.get(hundred))
            else:
                roman_number = str(roman_thousand.get(thousand)) + str(roman_hundred.get(hundred)) + str(roman_one.get(one))
        else:
            if one == 0:
                roman_number = str(roman_thousand.get(thousand)) + str(roman_hundred.get(hundred)) + str(roman_ten.get(ten))
            else:
                roman_number = str(roman_thousand.get(thousand)) + str(roman_hundred.get(hundred)) + str(roman_ten.get(ten)) + str(roman_one.get(one))
    elif len(number) == 3:
        hundred = int(number[0])
        ten = int(number[1])
        one = int(number[2])
        if ten == 0:
            if one == 0:
                roman_number = str(roman_hundred.get(hundred))
            else:
                roman_number = str(roman_hundred.get(hundred)) + str(roman_one.get(one))
        else:
            if one == 0:
                roman_number = str(roman_hundred.get(hundred)) + str(roman_ten.get(ten))
            else:
              roman_number = str(roman_hundred.get(hundred)) + str(roman_ten.get(ten)) + str(roman_one.get(one))
    elif len(number) == 2:
        ten = int(number[0])
        one = int(number[1])
        if one != 0:
            roman_number = str(roman_ten.get(ten)) + str(roman_one.get(one))
        else:
            roman_number = str(roman_ten.get(ten))
    else:
        one = int(number)
        roman_number = roman_one.get(one)

    print (number, ' - ', roman_number)
    arabic_number = roman.fromRoman(roman_number)
    print ("и обратно...", roman_number, ' - ', arabic_number )
    

