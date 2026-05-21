#interpreter
def calculator(a,c,b):

    if c=="+":
        print(f"{a+b:.1f}")
    elif c=="-":
        print(f"{a-b:.1f}")
    elif c=="*":
        print(f"{a*b:.1f}")
    elif c=="/":
        print(f"{a/b:.1f}")
    else:
        print("Invalid Choice.")

def main():
    expression=input("Expression:")
    parts=expression.split()
    x=float(parts[0])
    y=parts[1]
    z=float(parts[2])
    result=calculator(x,y,z)

main()

