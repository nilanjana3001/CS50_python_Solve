
    
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    for char in s:
        if char.isalpha() == False and char.isdigit() == False:
            return False
    found_number = False
    for char in s:
        if char.isdigit():
            if char == "0" and found_number == False:
                return False
            found_number = True
        if found_number and char.isalpha():
            return False
    return True
main()