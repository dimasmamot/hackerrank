def count_substring(string, sub_string):
    
    def loop(acc, stri, substr):
        if stri.find(substr) != -1:
            return loop(acc + 1, stri[stri.find(substr)+1:], substr)
        else:
            return acc
    
    return loop(0, string, sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)