#>90, "A",>80, "B",>70, "C",>60, "D",<=60, "F"
Mark= int(input("please enter Grade"))
if Mark>90:
    Grade= "A"
elif Mark>80:
    Grade="B"
elif Mark>70:
    Grade="C"
elif Mark>60:
    Grade="D"
else:
    Grade="F"
    print (Grade) 