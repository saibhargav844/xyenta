from datetime import date

try:
    year =int(input('enter year:'))
    Month = int(input('enter month:'))
    day =  int(input('enter day:'))

    DOB = date(year,Month,day)
    # print(DOB)
    today = date.today()
    # print(today)

    def ageCaluculator(DOB):
        age = today.year - DOB.year -((today.month,today.day)<(DOB.month,DOB.day))
        print('age:',age)

    ageCaluculator(DOB)

except Exception as e:
    print('error',e)