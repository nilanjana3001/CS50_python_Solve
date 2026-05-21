#Meal Time
def convert(n):
    n=n.split(":")
    x=int(n[0])
    y=int(n[1])
    z=x+y/60
    return z
    


def main():
    k=input("Enter time:")
    t=convert(k)
    if (7<= t <=8):
        print("Breakfast Time.")
    elif(12<= t <= 13):
        print("Lunch Time.")
    elif(18<= t <= 19):
        print("Dinner Time.")
    else:
        print("....")

    

main()


