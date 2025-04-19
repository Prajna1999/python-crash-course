from typing import List
def printShort(lis:List[str], character_count:int)->None:

    if not isinstance(lis, list):
        raise TypeError("Expected a list, but got {}".format(type(lis)))
    try:
        for word in lis:
            count_chars=len(word)
            if (count_chars>0 and count_chars<=character_count):
                print(word)
    except TypeError as e:
        print(f"Ouch! type mismatch: {str(e)}")


def printEven(list:List[int])->None:
    if not isinstance(list,list):
        raise TypeError("Expected a list, but got{}".format(type(List)))
    try:

        for number in list:
            if (number%2==0):
                print(number)
    except TypeError as e:
        print(f"Ouch! type mismatch: {str(e)}")

def uniqueList(vals:List[str])->List[str]:
    newList=[]   
    for val in vals:
        if val not in newList:
            newList.append(val)
        else:
            continue
    return newList
def main():
    # printShort(['a', 'long', 'one'],3)
    # printShort(['d','three', 'sun','ba'], 3)
    # printEven(4)
    result=uniqueList(['cat', 'dog', 'cat', 'bug', 'dog', 'ant', 'dog', 'bug'])
    print(result)


if __name__=="__main__":
    main()



