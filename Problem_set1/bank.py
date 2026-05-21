#Savings Bank

def output(n):
    n=n.strip()
    n=n.lower()
    if n.startswith("hello"):
      print("$0")
    elif n.startswith("h"):
      print("$20")
    else:
      print("$100")

def main():
   c=input("Greetings:")
   result=output(c)

main()