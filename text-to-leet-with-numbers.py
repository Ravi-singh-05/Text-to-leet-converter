import random


def leet_list(x):
    #this 'x' we will use to fetch the correct word and then it will  put a leet word in place of real word
    A = ['4', "/\"", '''@''', 'aye', '(L']
    B = ['I3', '8', '13', '|3', 'ß', '!3', '(3', '/3', ')3', '|-]', 'j3', '6']
    C = ['[', '¢', '{', '<', '(', '©']
    D = [')', '|)', '(|', '[)', 'I>', '|>', '?', 'T)', 'I7', 'cl', '|}', '>', '|]']
    E = ['3', '&', '£', '€', 'ë', '[-', '|=-']
    F = ['|=', 'ƒ', "|#", 'ph', '/=', 'v']
    G = ['&', '6', '(_+', '9', 'C-', 'gee', '(?', '[,', '{,', '<-', '(.']
    H = ["#", '/-/', '[-]', ']-[', ')-(', '(-)', ':-:', '|~|','|-|', ']~[', '}{', '!-!', '1-1', '\-/', 'I+I']
    I = ['1', '[]', '|', '!', 'eye', "3y3"]
    J = [',_|', '_|', '._|', '._]', '_]', '_]', ']', ';']
    K = ['>|', '|<', '/<', '1<', '|c', '|(', '|{']
    L = ['1', '£', '7', '|_', '|']
    M = ['/\/\ ', "/V\ ", "[]V[]", "|\/|", "^^", "|V|", "nn", "IVI", "]\/[", "1^1", "ITI"]
    N = ['^/', '|\|', '/\/', '[\]','{\}', '|V', '/V', 'И', 'ท']
    O = ['0', '()', 'oh', '[]', 'Ø']
    P = ['|*', '|o', '?', '|>', '9', '[]D', '|7']
    Q = ['(_,)', '9', '()_', '2', '0_', '<|', '&']
    R = ['I2', '|?', '/2', 'lz', '|9', '12', '[z', 'Я', '|2']
    S = ['5', '$', '§', 'ehs', 'es', '2']
    T = ['7', '+', '-|-', '][', '†', "|"]
    Y = ['L|', 'µ']
    U = ['(_)', '|_|']
    V = ['\/', '|/', '\|']
    W = ['\/\/', 'VV', ' \^/ ', '\V/', '\X/','\|/', '\_|_/', '\_:_/', 'Ш', 'uu', '2u']
    X = ['><', 'Ж', '}{', 'ecks', ')(', '][']
    Y = ['`/', 'Ч', '7', '\|/', '¥']
    Z = ['2', '7_', '-/_']
    number=['1','2','3','4','5','6','7','8','9','0']
    #creting list of list for further processing..
    leet_li=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
    leet_lit=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for it in range(65,91):
        zs=x.upper()
        #zs convert the 'x' in upper case in case if it was not already in upper case
        if zs in leet_lit:
            z=leet_lit.index(zs)
        elif zs in number:
            return zs
        
        return leet_li[z] 

 
con=input("enter the string you want to conver in to leet form-->")
#con variable mean text you want to convert
leet_word=''
wor= list(con)
for iterable in wor:
    if iterable !=" ":
        num=leet_list(iterable)
        # this variable num will get leet list of the respected variables you will enter
        cal = random.randint(0,len(num)-1) # this is just to create randomness and also to choose element from list.
        leet_word+=num[cal]
    else:
        leet_word+=" " #This  is because if you enter a <space> between two latters so it will also give space in the leet word
print()
print(leet_word)   # This finally prints the leet word  
input()   # this is to hold the output on screen in case you are not usind any ide and you are runnign code by just double clicking it.
# Made by Ravi singh, if you want to suggest anything you can mail on (rvsng028@gmail.com)
 
