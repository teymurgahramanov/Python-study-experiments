import random
while True:
    print("""Select mode
            1. Easy (1-2)
            2. Medium (0-10)
            3. Hard (0-100)""")
    mode=int(input("Mode: "))
    number=int(input("Your number: "))
    easy=random.choice([1, 2])
    medium=random.randint(0,10)
    hard=random.randint(0,100)

    def result(number,y):
        if number==y:
            print("You are lucky!")
        else:
            print("You are looser!")
    if mode==1:
        print(easy)
        result(number,easy)
    if mode==2:
        print(medium)
        result(number,medium)
    if mode==3:
        print(hard)
        result(number,hard)
    continue