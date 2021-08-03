import random

while True:
    n=input('rool the dict: ')
    randum=random.randint(1,6)
    print(randum)

    if randum==6:
        print('you won great')
        randum=random.randint(1,6)
    else:
        print('ypu lost')
        break    


