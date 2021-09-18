# Taqi Syed
# 1863528

from datetime import date

def calc_age(currentDate, birth):

    pres = currentDate
    age = pres.year - birth.year - ((pres.month, pres.day) < (birth.month, birth.day))
    return age


print('Birthday calculator')
print('Current day')
month1 = int(input('Month: '))
day1 = int(input('Day: '))
year1 = int(input('Year: '))

print('Birthday')
birth_m = int(input('Month: '))
birth_d = int(input('Day: '))
birth_y = int(input('Year: '))

print('You are', calc_age(date(month1, day1, year1), date(birth_m, birth_d, birth_y)), 'years old.')
if day1 == birth_d:
    print('Happy Birthday')
    


