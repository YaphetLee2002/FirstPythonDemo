tem =input()
if tem[-1]=='m':
    ans=3.2808*eval(tem[0:-1])
    print('%.2fft' %ans)
else:
    ans=eval(tem[0:-2])/3.2808
    print('%.2fm' %ans)