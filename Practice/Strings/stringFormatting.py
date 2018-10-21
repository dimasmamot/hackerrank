def print_formatted(num):
    binaryLen = len(str(bin(num))[2:]) + 1
    for number in range(1, num+1):     
        binary = (str(bin(number))[2:]).rjust(binaryLen, " ")
        decimal = str(number).rjust(binaryLen-1, " ")
        octal = (str(oct(number))[2:]).rjust(binaryLen, " ")
        hexadecimal = (str(hex(number))[2:]).upper().rjust(binaryLen, " ")

        print("{}{}{}{}".format(decimal, octal, hexadecimal, binary))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)