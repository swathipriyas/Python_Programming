#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      admin
#
# Created:     17/02/2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n=int(input("enter tne number:"))
i=0
r=1
m=2
while(i<n):
    if(i<=1):
        s=i
    else:
        s=r+m
        r=m
        m=s
        print(s)
        i=i+1
