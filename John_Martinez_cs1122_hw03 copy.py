'''
John Martinez
N17140055
cs1122
John_Martinez_cs1122_hw03.py
'''


# Problem 2
def EightBitBinary(number):
    if number <= 128:
        binaryStr = ''
        while number > 0:
            binaryStr = str(number % 2) + binaryStr
            number = number // 2

        print('0'*(8-len(binaryStr)) + binaryStr)


EightBitBinary(57) 
EightBitBinary(123)
EightBitBinary(85)
EightBitBinary(38)
    
# Problem 3

def convertToASCII(hexList):
    newString = ''
    for item in hexList:
        charInt = item
        newString += chr(charInt)
    print(newString)

convertToASCII([0x41,0x53,0x43,0x49,0x49,0x20,0x77,0x68,0x61,\
                0x74,0x20,0x79,0x6f,0x75,0x20,0x64,\
                0x69,0x64,0x20,0x74,0x68,0x65,0x72,0x65])

convertToASCII([0x39,0x41,0x4d,0x20,0x69,0x73,0x20,0x74,0x6f,\
                0x6f,0x20,0x65,0x61,0x72,0x6c,0x79,0x20,0x66,\
                0x6f,0x72,0x20,0x63,0x6c,0x61,0x73,0x73])

convertToASCII([0x43,0x6f,0x6d,0x70,0x75,0x74,0x65,0x72,0x73,\
                0x20,0x61,0x72,0x65,0x20,0x6d,0x61,0x67,0x69,0x63])

convertToASCII([0x57,0x68,0x61,0x74,0x20,0x74,0x68,0x65,0x20,0x68,0x65,0x78,0x3f])

# Problem 4

def convertToHex(bitString):
    newString = ''
    binList = ['0000','0001','0010','0011','0100','0101','0110','0111','1000',\
               '1001','1010','1011','1100','1101','1110','1111']
    hexStr = '0123456789abcdef'
    while len(bitString) % 4 > 0:
        bitString = '0' + bitString

    start = 0
    end = 4
    for i in range((len(bitString)//4)):
        char = bitString[start:end]
        index = binList.index(char)
        newString += hexStr[index]
        start += 4
        end += 4
    print('0x'+newString)

convertToHex('00001011101011101101111010101101')
convertToHex('11001010111111101111101011001110')
convertToHex('10111110111011111101000000001101')
convertToHex('11111111111111111001000001100010')

# Problem 5

def octalToDecimal(octalInt):
    decNum = 0
    power = 0
    while octalInt >= 10:
        factor = octalInt % 10
        decNum += factor * (8**power)
        octalInt = octalInt // 10
        power+=1
    decNum += octalInt * (8**power)
    print(decNum)

octalToDecimal(10)
octalToDecimal(42)
octalToDecimal(77)
octalToDecimal(113)
    
