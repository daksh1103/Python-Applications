
from IPython.display import clear_output
def display(list1):
    clear_output()       
    print(list1[0]+'|'+list1[1]+'|'+list1[2])
    print(' ---')
    print(list1[3]+'|'+list1[4]+'|'+list1[5])
    print(' ---')
    print(list1[6]+'|'+list1[7]+'|'+list1[8])
        
        
def userinput():
    sym1=''
    while sym1!='X' and sym1!='O':  
        sym1=input('Enter the symbol Player1 wants to choose')
    if sym1=='X':
        sym2='O'
    else:
        sym2='X'
    return [sym1,sym2]
def check(list1,mark):
    return  ((list1[0]==mark and list1[1]==mark and list1[2]==mark) or(list1[3]==mark and list1[4]==mark and list1[5]) or 
             (list1[6]==mark and list1[7]==mark and list1[8])or(list1[0]==mark and list1[3]==mark and list1[6])
             or(list1[1]==mark and list1[4]==mark and list1[7])or (list1[2]==mark and list1[5]==mark and list1[8])or
             (list1[0]==mark and list1[4]==mark and list1[8]) or (list1[2]==mark and list1[4]==mark and list1[6]))
    
def main():
    choice=''
    while choice!='YES' and choice!='NO': 
        choice=input('Do u want to play TIC TAC TOE')
    while(choice=='YES'):
        list1=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display(list1)
        a=userinput()
        clear_output()
        print('Player1 chose '+a[0])
        print('Lets Start The Game-------------------!!!!!!!!!!!!!!!!!! Good Luck')
        game=1
        while(game!=0):
            k=[]
            place1=int(input('Player1 Enter the symbol  '))
            if place1 in k:
                place1=int(input('Already used ..please enter a different number'))
            else:
                k.append(place1)
            list1[place1-1]=a[0]
            display(list1)
            bol=check(list1,a[0])
            if (bol):
                print('Player1 won')
                break
            place2=int(input('Player2 Enter the symbol '))
            if place2 in k:
                place2=int(input('Already used ..please enter a different number'))
            else:
                k.append(place1)
            list1[place2-1]=a[1]
            display(list1)
            bol=check(list1,a[1])
            if (bol):
                print('Player2 Won')
                break
        choice=input('Game is over! DO U WISH TO CONTINUE ')
        clear_output()
        
main()