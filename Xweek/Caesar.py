# Шифр Цезаря
# Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом,
# находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3,
# А была бы заменена на Г, Б станет Д, и так далее.
# Шифр назван в честь римского императора Гая Юлия Цезаря, использовавшего его для секретной переписки со своими генералами.
# Следующая часть работы зашифрована шифром Цезаря.
class Caesar:
    alphabet = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, key):
        self._encode = dict()
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            encoded = self.alphabet[(i + key) % len(self.alphabet)]
            self._encode[letter] = encoded
            self._encode[letter.upper()] = encoded.upper()
        self._decode = {v: k for k, v in self._encode.items()}  # TODO
        #print(self._decode.items())


    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])
        #pass  # TODO


# for i in range(33):
#     #print(Caesar(i).decode('Кыжг вгбдебь ътячан'))
#     #print(Caesar(i).encode('Кыжг вгбдебь ътячан'))
#     if Caesar(i).decode('Кыжг вгбдебь ътячан') == 'Шифр простой замены':
#         print(i)
key = 14
cipher = Caesar(key)
line = input()
while line:
    print(cipher.decode(line))
    line = input()
# key = int(input('Ээъыцмъ фубз:'))
# cipher = Caesar(key)
# line = input()
# while line:
#     print(cipher.encode(line))
#     line = input()
# Допишите метод decode и расшифруйте следующий раздел лабораторной работы. Подумайте, почему вам не сообщили ключ шифрования и что вам с этим делать.
