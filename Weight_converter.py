weight = input("Enter your weight: ")
choice = input("(L)bs or (K)gs: ")
pounds = int(weight) / 0.45
kilograms = int(weight) * 0.45
if choice.upper() == 'L':
    print(f'{kilograms} kgs')
elif choice.upper() == 'K' :
    print(f'{pounds} lbs')