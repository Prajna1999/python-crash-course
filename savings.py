def calculatePrincipal():
    principal=float(input("How much money you currently have? "))
    target=float(input("How much you want to have? "))
    interestRate=float(input("What is the interest rate? "))
    year=0
    while principal<=target:
        principal=principal*(1+(interestRate/100))
        print("%.2f"%principal)
        year+=1
    
    print(f"You achieved your taget in {year} years")

def main():
    calculatePrincipal()

if __name__=="__main__":
    main()