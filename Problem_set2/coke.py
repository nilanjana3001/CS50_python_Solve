def main():
    amount_due=50
    print("Amount Due: 50")
    while amount_due> 0:
        k=int(input("Insert coin:"))
        if k==25 or k==10 or k==5:
            amount_due=amount_due-k
            print("Amount Due:",amount_due)
        else :
            print("Invalid insert.")

    print (f"Charged Owned",amount_due* -1)
main()         