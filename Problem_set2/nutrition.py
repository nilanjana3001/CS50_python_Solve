
fruits={
        "apple":130,
        "avocado":50,
        "banana":110,
        "canataloupe":50,
        "grapes":90,
        "grapefruit":60,
        "honeydew":50,
        "kiwi":90,
        "lemon":15,
        "lime":20,
        "nectarine": 60,
        "orange":80,
        "peach":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "watermelon":80,  
                }


def main():
    x=input("Enter Item:").lower()
    if x in fruits:
     print("Calories:",fruits[x])

main()
