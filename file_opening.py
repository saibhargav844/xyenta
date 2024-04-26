import os

try:

   
    with open("C:\\Users\\SaiBhargavGorre\\Downloads\\loandata.csv",'r+')as f:
        lines = f.readlines(1000)
        
    with open("C:\\Users\\SaiBhargavGorre\\filehandling.txt",'w') as g:
        g.writelines(lines)

except Exception as e:
    print('error message:',e)
            