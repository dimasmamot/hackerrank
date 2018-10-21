if __name__ == '__main__':
    s = input()
    
    def isContain(fun, amount, string):
        count = 0
        for c in string:
            if fun(c):
                count += 1
        
        if count >= amount:
            return True
        else:
            return False
        
    print(isContain(str.isalnum, 1, s))
    print(isContain(str.isalpha, 1, s))    
    print(isContain(str.isdigit, 1, s))    
    print(isContain(str.islower, 1, s))    
    print(isContain(str.isupper, 1, s))    