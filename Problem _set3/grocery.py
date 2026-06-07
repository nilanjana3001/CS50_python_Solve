def main():
    groceries={

 }
    while True:
        try:
            item=input("Items:").capitalize()
            if item in groceries:
             groceries[item]+=1
            else:
             groceries[item]=1
            
        except(EOFError):
             break
        for item in sorted(groceries):
             print(groceries[item],item)

main()            
    
