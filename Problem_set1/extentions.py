# File Extention

def output(k):
   k=k.lower()
   if k.endswith(".gif"):
         print("image/gif")
   elif k.endswith(".jpg"):
        print("image/jpeg")
   elif k.endswith(".jpeg"):
        print("image/jpeg")
   elif k.endswith(".png"):
        print("image/png")
   elif k.endswith(".pdf"):
        print("application/pdf")
   elif k.endswith(".txt"):
        print("text/plain")
   elif k.endswith(".zip"):
        print("application/zip") 
   else:
        print("application/octet-stream")   

def main():
     c=input("Enter a text:")
     result=output(c)

main()        