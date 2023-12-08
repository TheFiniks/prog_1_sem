# Шифр простой замены
# Итак, вы догадались почему шифр Цезаря не является криптостойким: слишком мала мощность множества ключей и нужный ключ легко найти методом полного перебора.
# Можно ли увеличить криптостойкость, не меняя метод шифрования? Да, можно. Если заменять один символ алфавита на определённый другой символ того же алфавита по какой-то таблице замен, то сама таблица замен и является ключом.
# Множество ключей — это множество возможных таблиц простых замен. Для русского алфавита мощность множества таблиц простых замен равна факториалу от 33. 33! = 8683317618811886495518194401280000000
# Если тратить на проверку одного варианта 0.000001 секунды, получится 2.8e+23 лет. Может показаться, что шифр простой замены вполне криптостойкий, однако это не так.
# Его достаточно просто взломать при помощи частотного анализа. Дело в том, что частота появления заданной буквы алфавита в достаточно длинных текстах одна и та же для разных текстов одного языка. Если в шифротексте будет символ с вероятностью появления, аналогичной стандартной для языка, то можно предположить, что он и является указанной зашифрованной буквой.
# Метод частотного криптоанализа известен с IX-го века, хотя наиболее известным случаем его применения в реальной жизни, возможно, является дешифровка египетских иероглифов в 1822 году.
# Итак, следующая часть работы зашифрована при помощи следующей программы:
class Monoalphabet:
    alphabet = 'оаиетрнвлсмкыпзфдяшуьбгчжхйцюэёщъ'  # TODO
    # alphabet = 'оатинерслвкмпядзфуыгйшчбьхжющцэёъ'  # TODO
    # alphabet = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'
    def __init__(self, keytable):
        lowercase_code = {x: y for x, y in zip(self.alphabet, keytable)}
        uppercase_code = {x.upper(): y.upper() for x, y in zip(self.alphabet, keytable)}
        self._encode = lowercase_code
        self._encode.update(uppercase_code)
        self._decode = {v: k for k, v in self._encode.items()}  # TODO

    def encode(self, text):
        return ''.join([self._encode.get(char, char) for char in text])

    def decode(self, line):
        return ''.join([self._decode.get(char, char) for char in line])
        # pass  # TODO


def find_letter(text):
    alphabet = [elem for elem in Monoalphabet.alphabet]
    letter_frequency = {a: text.count(a) for a in alphabet}
    return letter_frequency


def dic_sort(data):
    sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return sorted_data


f = open('SSC.txt', encoding='utf8')
stat = open('statistics.txt', encoding='utf8')
text = ''.join([line.strip() for line in f])
data = ''.join([line.strip() for line in stat])
freq = find_letter(text)
cipher_letters = dic_sort(freq)
vik_freq = 'оеаинтсрвлкмдпуяыьгзбчйхжшюцщэфъё'
# result_freq = ''.join([letter[0] for letter in cipher_letters])
result_freq = 'цэгщбжюояшсчзайпмиетхьрлнвыёфкдъу'
cipher = Monoalphabet(result_freq)
freq2 = find_letter(data)
cipher_letters2 = dic_sort(freq2)
result_freq2 = ''.join([letter[0] for letter in cipher_letters2])
print(vik_freq)
print(result_freq2)
print(result_freq)
print(cipher.decode(text))
# key = [elem for elem in Monoalphabet.alphabet]
# for i in range(100000):
#     random.shuffle(key)
#     key = ''.join(key)
#     cipher = Monoalphabet(key)
#     print(cipher.decode('Егпж Огнщющжэ (ацягэяпэогбюцы йэсщюз)'))
#     key = [elem for elem in Monoalphabet.alphabet]
# line = input()
# while line:
#     print(cipher.encode(line))
#     line = input()
# Программу для частотного анализа следует написать самостоятельно. Успехов!

