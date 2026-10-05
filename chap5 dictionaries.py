birthdays = {'Luban': 'June 25 2013', 'Labib': 'March 4 2007', 'Lisan': 'July 19 2019'}
while True:
	print("Enter A Name: (Or Enter Blank To Exit)")
	name = input()
	if name == '':
		break
	if name in birthdays:
		print(birthdays[name] + ' Is The Birthday Of ' + name)
	else:
		print("I Do Not Have THe Birthday Information Of " + name)
		print("Please Provide Their Bithday")
		b_day = input()
		birthdays[name] = b_day
		print("Birthdays Database Successfully Update")
