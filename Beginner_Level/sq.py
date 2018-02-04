#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     04/02/2018
# Copyright:   (c) Administrator 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#squares=[]
for x in range(1,11):
     #squares.append(x**2)
     #print(squares)
     squares=[x**2 for x in range(1,11)]
     print"squares=",squares