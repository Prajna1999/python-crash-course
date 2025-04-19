def sumAll():
    total=0
    while True:
        number=input("Input a number to continue (0 to stop) ")
        if number=='0':
            break
        try:
                
            total+=int(number)
            print(total)
        except ValueError:
            print("Invalid input,Please put a valid integer")
    
    print("Final sum is ", total)


def main():
    sumAll()

if __name__=="__main__":
    main()
