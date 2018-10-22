from collections import OrderedDict

def merge_the_tools(string, k):
    subsegment = []
    for i in range(0, len(string), k):
        subsegment.append(string[i:i+k])
    
    for item in subsegment:
        print("".join(list(OrderedDict.fromkeys(item))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)