weight = int(input('inert weight: '))
choose = input('select (K)g or (L)bs: ')
if choose.upper() == 'L':
    converted_choose = weight * 0.45
    print(f'Your wight is {converted_choose} Kg')
else:
    converted_choose = weight / 0.45
    print(f'Your weight is {converted_choose} Pouns ')