x=("boy","men","girl","women")
c=("red","black","brown","white")
def cloths(x,c):
    if x == "boy" :
        print("you selected dress type for boys")
        if c=="red":
            print("color of shirt is red")
        elif  c=="black":
            print("color of shirt is black")
        elif  c=="brown":
            print("color of shirt is brown")
        elif  c=="white":
            print("color of shirt is white")
        else:
            print("enter valid color")
    elif x== "men" :
        print("you selected dress type for men")
        if c=="red":
            print("color of shirt is red")
        elif  c=="black":
            print("color of shirt is black")
        elif  c=="brown":
            print("color of shirt is brown")
        elif  c=="white":
            print("color of shirt is white")
        else:
            print("enter valid color")
    elif x== "girl" :
        print("you selected dress type for girl")
        if c=="red":
            print("color of shirt is red")
        elif  c=="black":
            print("color of shirt is black")
        elif  c=="brown":
            print("color of shirt is brown")
        elif  c=="white":
            print("color of shirt is white")
        else:
            print("enter valid color")
    elif x== "women" :
        print("you selected dress type for women")  
        if c=="red":
            print("color of shirt is red")
        elif  c=="black":
            print("color of shirt is black")
        elif  c=="brown":
            print("color of shirt is brown")
        elif  c=="white":
            print("color of shirt is white")
        else:
            print("enter valid color")
    else:
        print("enter valid detail") 

print("enter one of the following:\n 1.boy\n 2.men\n 3.girl\n 4.women")
x=input("select a dress type for:")
c=input("select a dress type for:")
cloths(x,c)