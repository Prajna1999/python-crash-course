def isEligibleForSenate(age:int, citizenTenure:int)->bool:
    if age>=30 and citizenTenure>=9:
        return True
    return False

def isEligibleForHouse(age:int, citizenTenure:int)->bool:
    if age>=25 and citizenTenure>=7:
        return True
    return False


def isEligibleForCongress(age:int,citizenTenure:int)->None:
    resultString=f"You are eligible for the House"
    if isEligibleForHouse(age, citizenTenure):
        if isEligibleForSenate(age,citizenTenure):
            print(f"{resultString} and the Congress")
        else:
             print(resultString)
    else:

        print("You are ineligible for Congress")
    
   
def startsWithArticle(title:str):
    # titleList=title.split(" ",maxsplit=1)[0]
    # if titleList in {"A", "An", "The"}:
    #     return True
    # return False

    # extra space after each article
    return title.startswith(("A ", "An ", "The "))


def main():
    print(startsWithArticle("The Wealth of the Nation"))
    print(startsWithArticle("Theb Wealth of the Nation"))
    print(startsWithArticle("There Goes Marnie"))
    print(startsWithArticle("A song"))
    print(startsWithArticle("Ac heil"))

if __name__=="__main__":
    main()


