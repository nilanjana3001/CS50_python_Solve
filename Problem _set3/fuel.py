def convert(fraction):
    parts=fraction.split("/")
    x=int(parts[0])
    y=int(parts[1])
    if x>y:
       raise ValueError
    elif y==0:
      raise ZeroDivisionError
    else:
     return round(x/y*100)

def gauge(percentage):
   if percentage<=1:
    return "E"
   if percentage >=99:
    return "F"
   else:
      return str(percentage)+ "%"
   
def main():
   while True:
      try:
         fraction=input("Fraction:")
         percentage=convert(fraction)
         print(gauge(percentage))
         break
      except(ValueError,ZeroDivisionError):
         pass
      
main()      
  




