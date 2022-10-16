str1='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
str2='DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc'
str=str(input())
for i in range(len(str)):
    if ((str[i] in str1)):
        k=0
        for k in range(0,52):
            if str[i]==str1[k]:
                print(str2[k],end='')
    else:
        print(str[i],end='')