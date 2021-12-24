p1n=input("Enter Name of Player 1: ")
p2n=input("Enter Name of Player 2: ")

p="pawn"
k="knight"
b="bishop"
r="rook"
ki="king"
q="queen"

p2="pawn"
k2="knight"
b2="bishop"
r2="rook"
ki2="king"
q2="queen"


print (p1n + "'s "  +  "turn")
p1=input("Choose Piece: ")


mp= ("e3","e4")
mk= ("Nf3","Nh3")
mb=("Be2","Bd3","Bc4","Bb5","Ba6")
mki=("Ke2")
mq=("Qe2")
mr=("Ra1","Ra2","Ra3","Ra4","Ra5","Ra6","Ra7","Ra8","Rh1","Rh2","Rh3","Rh4","Rh5","Rh6","Rh6","Rh7","Rh8 ")
def pa(p):
    print (mp) 
    print (input("Choose Move: "))
    print (p2n + "'s "  +  "turn")
    
def kn(k):
     print (mk)
     print (input("Choose move: "))
     print (p2n + "'s "  +  "turn")

def bi(b):
     print (mb)
     print (input("Choose move: "))
     print (p2n + "'s "  +  "turn")

def kin(ki):
     print (mki)
     print (input("Choose move: "))
     print (p2n + "'s "  +  "turn")

def qe(q):
     print (mq)
     print (input("Choose move: "))
     print (p2n + "'s "  +  "turn")
     
def ro(r):
     print (mr)
     print (input("Choose move: "))
     print (p2n + "'s "  +  "turn")


mp2= ("e5","e6")
mk2= ("Nf6","Nh6")
mb2=("Be7","Bd6","Bc5","Bb4","Ba3")
mki2=("Ke7")
mq2=("Qe7")
mr2=("Ra1","Ra2","Ra3","Ra4","Ra5","Ra6","Ra7","Ra8","Rh1","Rh2","Rh3","Rh4","Rh5","Rh6","Rh6","Rh7","Rh8 ")
def pa2(p2):
     print (mp2) 
     print (input("Choose move: "))
     print (p1n + "'s "  +  "turn")
def kn2(k2):
     print (mk2)
     print (input("Choose move: "))
     print (p1n + "'s "  +  "turn")
def bi2(b2):
     print (mb2)
     print (input("Choose move: "))
     print (p1n + "'s "  +  "turn")

def kin2(ki2):
     print (mki2)
     print (input("Choose move:Ke7 "))
     print (p1n + "'s "  +  "turn")

def qe2(q2):
     print (mq2)
     print (input("Choose move: "))
     print (p1n + "'s "  +  "turn")
     
def ro2(r2):
     print (mr2)
     print (input("Choose move: "))
     print (p1n + "'s "  +  "turn")



v=1
while (v==1):
    
     if (p1=="pawn" ):
        print (pa(p))    
     elif (p1=="knight"):
        print (kn(k))     
     elif (p1=="bishop"):
        print (bi(b))
     elif (p1=="king"):
        print (kin(ki))       
     elif (p1=="queen"):
        print (qe(q))
     elif (p1=="rook"):
        print (ro(r))
     else:
        print ("That piece is not moveable")
        print ("Do you want to stop?")
        g=input("Enter Either Yes or No: ")
        if (g=="yes"):
            print ("The game had ended.")
            break
        
  
     p2=input("Choose Piece: ")
     if (p2=="pawn" ):
        print (pa2(p2))    
     elif (p2=="knight"):
        print (kn2(k2))     
     elif (p2=="bishop"):
        print (bi2(b2))
     elif (p2=="king"):
        print (kin2(ki2))       
     elif (p2=="queen"):
        print (qe2(q2))
     elif (p2=="rook"):
        print (ro2(r2))
     else:
        print ("That piece is not moveable")
        print ("Do you want to stop?")
        g=input("Enter Either Yes or No: ")
        if (g=="yes"):
            print ("The game had ended.")
            break
    

     p1=input("Choose Piece: ")    
     if (p1=="pawn" ):
        print (pa(p))    
     elif (p1=="knight"):
        print (kn(k))     
     elif (p1=="bishop"):
        print (bi(b))
     elif (p1=="king"):
        print (kin(ki))       
     elif (p1=="queen"):
        print (qe(q))
     elif (p1=="rook"):
        print (ro(r))
     else:
        print ("That piece is not moveable")
        print ("Do you want to stop?")
        g=input("Enter Either Yes or No: ")
        if (g=="yes"):
            print ("The game had ended.")
            break
    
    
     p2=input("Choose Piece: ")  
     if (p2=="pawn" ):
        print (pa2(p2))    
     elif (p2=="knight"):
        print (kn2(k2))     
     elif (p2=="bishop"):
        print (bi2(b2))
     elif (p2=="king"):
        print (kin2(ki2))       
     elif (p2=="queen"):
        print (qe2(q2))
     elif (p2=="rook"):
        print (ro2(r2))
     else:
        print ("That piece is not moveable")
        print ("Do you want to stop?")
        g=input("Enter Either Yes or No: ")
        if (g=="yes"):
            print ("The game had ended.")
            break