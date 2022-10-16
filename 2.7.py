PString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
CString = 'DEFGHIJKLMNOPQRSTUVWXYZABCdefghijklmnopqrstuvwxyzabc'
PCode = input('')
for i in range(len(PCode)):
    if ((PCode[i] in PString)):
        k = 0
        for k in range(0, 52):
            if PCode[i] == PString[k]:
                print(CString[k], end='')
    else:
        print(PCode[i], end='')