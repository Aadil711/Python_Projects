#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sayli
#
# Created:     13-08-2022
# Copyright:   (c) sayli 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

first=input("ENTER 1st digit:")
second=input("ENTER 2nd digit :")
first=int(first)
second=int(second)
operator=input("ENTER OPERATOR:")
if operator=="+":
    print(first + second)
elif operator=="/":
    print(first / second)
elif operator =="%":
    print(first%second)
elif operator=="*":
    print(first * second)
else :
    print("invalid operation and you are a fool")
