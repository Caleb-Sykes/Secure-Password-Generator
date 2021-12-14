# Title: Secure Password Generator / Author: Caleb Sykes / Date: 15.02.2021

import random

# CLI Script / Secure Password Generator
# Generates a secure password 14 characters in length
# Comprises of upper case, lower case, special character, and number

# Generates password
def generate():
    lis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','\"','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','\[','\]','^','_','`','{','}','|','~']
    passwd = []
    for i in range(0,14):
        passwd.append(lis[random.randint(0,(len(lis)-1))])
    return(passwd)

# Checks if password meets requirements
def verify(x):
    special = ['!','\"','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','\[','\]','^','_','`','{','}','|','~']
    reqs = []
    for i in x:
        if i.isupper():
            reqs.append('U')
        elif i.islower():
            reqs.append('L')
        elif i.isnumeric():
            reqs.append('N')
        for a in special:
            if i == a:
                reqs.append('S')
    try:
        reqs.index('U')
        reqs.index('L')
        reqs.index('N')
        reqs.index('S')
    except ValueError:
        return(False)
    return(True)

passwd = generate()

while verify(passwd) == False:
    passwd = generate()

passwd = "".join(passwd)
print(passwd)
