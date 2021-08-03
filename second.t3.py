seconds =int(input('enter secont:'))

h = seconds // 3600
seconds %= 3600

m =  seconds //60
seconds %= 60

s= seconds

print('hour:',h,'minutes:',m,'seconds:',s)