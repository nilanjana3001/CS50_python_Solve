def convert(a):
 result =""
 for char in a:
  if char=='a'or char=='e'or char=='i'or char=='o'or char=='u' or char=='A'or char=='E'or char=='I'or char=='O'or char=='U':
    pass
  else:
   result = result+char
 
 return result 

def main():
 b=input("Input:")
 result=convert(b)
 print("Output:",result)

main()