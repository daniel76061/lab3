def encode(text):
    dictionary = {
        0 : 'A',
        1 : 'B',
        2 : 'C',
        3 : 'D',
        4 : 'E',
        5 : 'F',
        6 : 'G',
        7 : 'H',
        8 : 'I',
        9 : 'J',
        10 : 'K',
        11 : 'L',
        12 : 'M',
        13 : 'N',
        14 : 'O',
        15 : 'P',
        16 : 'Q',
        17 : 'R',
        18 : 'S',
        19 : 'T',
        20 : 'U',
        21 : 'V',
        22 : 'W',
        23 : 'X',
        24 : 'Y',
        25 : 'Z',
        26 : 'a',
        27 : 'b',
        28 : 'c',
        29 : 'd',
        30 : 'e',
        31 : 'f',
        32 : 'g',
        33 : 'h',
        34 : 'i',
        35 : 'j',
        36 : 'k',
        37 : 'l',
        38 : 'm',
        39 : 'n',
        40 : 'o',
        41 : 'p',
        42 : 'q',
        43 : 'r',
        44 : 's',
        45 : 't',
        46 : 'u',
        47 : 'v',
        48 : 'w',
        49 : 'x',
        50 : 'y',
        51 : 'z',
        52 : '0',
        53 : '1',
        54 : '2',
        55 : '3',
        56 : '4',
        57 : '5',
        58 : '6',
        59 : '7',
        60 : '8',
        61 : '9',
        62 : '+',
        63 : '/',
    }

    counter = 0
    encoded = ''

    # Convert given text to bin
    to_bin = str(''.join(bin(ord(c)) for c in text).replace('b',''))

    # split text to 6 bit chunks
    split = [to_bin[i:i+6] for i in range(0, len(to_bin), 6)]
    
    # while last chunks lenght is smaller than 6 characters, add zeros
    while len(split[-1]) < 6:
        split[-1] += '0'

    # while sum of chunks in list is not divisible by 4, add another one and fill with zeros
    while len(split) % 4 != 0:
            split.append('000000')
            counter += 1

    # mapping 6 bit chunks to elements in dictionary
    for el in split:
        encoded += dictionary[(int(el, 2))]

    # if there was any chunk filled with zeros, replace it with = sign
    if counter == 1:
        encoded = encoded[:-1] + '='
    if counter == 2:
        encoded = encoded[:-2] + '=='

    # return encoded text
    return encoded

if __name__ == '__main__':
    text_to_encode = input("Enter text to encode: ")
    print(encode(text_to_encode))
