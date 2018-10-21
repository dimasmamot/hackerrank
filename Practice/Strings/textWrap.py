def wrap(string, max_width):    
    if len(string) < max_width:
        return string
    else:
        print(string[0:max_width])
        return wrap(string[max_width:], max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)