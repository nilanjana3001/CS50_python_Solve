
months={
    
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June":6,
    "July":7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
 }
def convert(date):
    if "/" in date:
        parts=date.split("/")
        month=int(parts[0])
        day=int(parts[1])
        year=int(parts[2])
    else:
        parts=date.split(" ")
        if parts[0] not in month:
         raise ValueError
        month=month[parts[0]]
        day=int(parts[1].replace(",",""))
        year=int(parts[2])
    if month < 1 or month > 12:
      raise ValueError
     
    if day < 1 or day > 31:
      raise ValueError  
    return f"{year}-{month:02d}-{day:02d}"
     
                        


def main():
    while True:
        try:
            date=input("Date:")
            print(convert(date))
            break
        except ValueError:
            pass

main()
                
