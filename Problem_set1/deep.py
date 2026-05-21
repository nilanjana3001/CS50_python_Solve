
#deep thoughts
def output(a):
  a=a.lower()
  if a== "42" or a =="forty-two" or a =="forty two":
     print("Yes")
  else:
     print("No")



def main():

  c=input("What is the Answer to the great Question of Life,the Universe, and Everything?")
  result=output(c)

main()