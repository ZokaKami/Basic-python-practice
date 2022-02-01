import re


def math(vals):
    for number in vals:
        x = re.search("\d+", number)
        y = re.search("[+,-]", number)
        z = re.search("\d+$", number)
        FirstNumber = x.group()
        Symbol = y.group()
        SecondNumber = z.group()
        Result = int(FirstNumber) + int(SecondNumber)
        Result = str(Result)

        if(len(FirstNumber) < len(SecondNumber)):
            print(FirstNumber.rjust(len(SecondNumber)+2))
            print(Symbol, SecondNumber)
            Width = len(Symbol) + len(SecondNumber) + 1
            print("-" * Width)
            print(Result.rjust(Width), "\n")

        elif(len(SecondNumber) < len(FirstNumber)):
            print(FirstNumber.rjust(len(FirstNumber) + 1))
            print(Symbol, z.group().rjust(len(FirstNumber)-1))
            Width = len(Symbol) + len(FirstNumber)
            print("-" * Width)
            print(Result.rjust(Width), "\n")

        elif(len(SecondNumber) == len(FirstNumber)):
            print(FirstNumber.rjust(len(FirstNumber)+2))
            print(Symbol, z.group())
            Width = len(Symbol) + len(SecondNumber) + 1
            print("-" * Width)
            print(Result.rjust(Width), "\n")


math(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "111111111111 + 1"])
