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
            Width = len(Symbol) + len(SecondNumber) + 1
            print(FirstNumber.rjust(len(SecondNumber)+3), "\n", Symbol,
                  SecondNumber, "\n", "-"*Width, "\n", Result.rjust(Width), "\n")

        elif(len(SecondNumber) < len(FirstNumber)):

            Width = len(Symbol) + len(FirstNumber)
            print(FirstNumber.rjust(len(FirstNumber)+2), "\n", Symbol,
                  SecondNumber.rjust(len(FirstNumber)-1), "\n", "-"*Width, "\n", Result.rjust(Width), "\n")

        elif(len(SecondNumber) == len(FirstNumber)):
            Width = len(Symbol) + len(SecondNumber) + 1
            print(FirstNumber.rjust(len(FirstNumber)+3), "\n", Symbol,
                  SecondNumber, "\n", "-"*Width, "\n", Result.rjust(Width), "\n")


math(["32 + 633", "2223801 - 2222", "45 + 433", "123 + 49", "1111111 + 1"])
