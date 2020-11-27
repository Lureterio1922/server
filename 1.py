
if __name__ == '__main__':
    k=input().split(' ')
    s=set()
    for i in range(len(k)):
        b=k[i]
        s.add(b[0].upper()+b[1:].lower())
    print(s)











