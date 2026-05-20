def convert(s):
    s = s.replace(" ", "...")
    return s

def main():
    text = input("Enter a text: ")
    result = convert(text)
    print(result)

main()