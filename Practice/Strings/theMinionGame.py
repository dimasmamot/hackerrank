def minion_game(input_string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print("Kevin {}".format(kevsc))
    elif kevsc < stusc:
        print("Stuart {}".format(stusc))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)