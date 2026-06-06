#Camel Case

def convert(s):
    result=""
    for char in s:
      if char.isupper():
        result=result+"_"+char.lower()
      else:
        result=result+char

    return result



def main():
    k=input("Enter in camel case:")
    result=convert(k)
    print(result)
     
main()