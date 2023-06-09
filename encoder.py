import numpy as np


class ConvolutionalEncoder():

    def __init__(self, communications):
        self.communications = communications

    def multiply(self, poly1, poly2):
        max_adder = len(poly1) + len(poly2) - 1
        start = [x for x in range(max_adder)]
        dct = dict.fromkeys(start, 0)
        result = []
        for ind1, elem1 in enumerate(poly1):
            for ind2, elem2 in enumerate(poly2):
                if elem1 != 0 and elem2 != 0:
                    res = ind1 + ind2
                    dct[res] += 1

        for key in range(len(dct)):
            result.append(dct[key])

        for ind, elem in enumerate(result):
            if elem % 2 == 0:
                result[ind] = 0
            else:
                result[ind] = 1
        return result

    def encode(self, info_word):
        adders = []

        for lst in self.communications:
            adder = self.multiply(info_word, lst)
            adders.append(adder)
        
        encoded_word = []
        for index in range(len(adder)):
            for number in range(len(adders)):
                encoded_word.append(adders[number][index])
        return encoded_word

    def decode(self, code_word):
        ind = 0
        adder = []
        while ind < len(code_word):
            adder.append(int(code_word[ind]))
            ind += len(self.communications)

        registers = self.communications[0]
        decoded_word = []
        res_list = list(np.polydiv(adder, registers)[0])
        for numb in res_list:
            if numb % 2 == 0:
                decoded_word.append(0)
            else:
                decoded_word.append(1)
        return decoded_word


def translate(text: str, binary: bool):
    if binary:
        text_ord = [bin(ord(elem))[2:] for elem in text]
        return text_ord
    else:
        text_int = int(text, 2)
        text_chr = chr(text_int)
        return text_chr





if __name__ == '__main__':
    comm = [[1, 1, 1], [1, 0, 1]]
    # i = [1, 1, 0, 1]
    # C = [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1]

    i = [1, 1, 0, 0, 1, 0, 1]
    C = [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1]
    
    myCode = ConvolutionalEncoder(comm)
    print(myCode.encode(i))
    print(myCode.decode(C))
    # print(myCode.__doc__)


    txt = 'eu'
    b = True
    print(translate(txt, b))
