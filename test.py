import re
names = ["Mishu", "Nipu", "Shuvo", "Sumi", "Tumpa", "Roni", "Riya", "Adnan", "Ladoo", "Chumchum", "Kaju", "Pesta", "Modhu", "Babui", "Babu", "Tuktuki", "Piku", "Mumu", "Tutu", "Chotu", "Koko", "Nono", "Potol", "Boba", "Bhuto", "Khoka", "Khuki", "Dusto"]

for name in names:                   #Search with the first letter
    if re.search(r"^S", name):
        print(name)		
print("---------")        
for name in names:                    #Search with the first letter
	if re.match(r"R", name):
		print(name)
print("---------") 		        

for name in names:
	if re.search(r"a$", name):		#search with the last leter
		print(name)
print("---------") 				

for name in names:
	if re.search(r"hu", name):
		print(name)
print("---------") 	
for name in names:
	if re.search(r"hu | ab", name):
		print(name)	