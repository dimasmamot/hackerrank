import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    rangoli = []
    
    for i in range(size):
        s = ('-').join(alpha[i:size])
        pattern = (s[::-1]+s[1:]).center(4*n-3, '-')
        rangoli.append(pattern)

    rangoliPad = rangoli[::-1] + rangoli[1:]
    print('\n'.join(rangoliPad))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)