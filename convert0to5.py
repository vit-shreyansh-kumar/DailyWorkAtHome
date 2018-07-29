__about__="Convert 0 to 5 in a digit"


def convert0to5(num):
    if num == 0:
        return 5

    digit = num % 10
    print(digit)
    if digit == 0:
        digit = 5
        
    return convert0to5(num/10)*10+digit

if __name__=="__main__":
    num = 10
    finalnum = convert0to5(num)
    print("Num Ip:",num)
    print("Num Op:",finalnum)

