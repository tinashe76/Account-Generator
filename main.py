#Github tinashe76
#special thanks to Johan Godhino for his help with the password generator

import random

#--------------------------------------------ONLY CHANGE VALUES IN THIS SECTION---------------------------------------
chars = "0123456789"
index = ""
abc = "abcdefghijklmnopqrstuvwxyz"
usernames = ["ruzo", "rimbo", "blaco", "belco", "brembo", "blum", "rapt", "sydyney", "lucus", "red", "maybo", "liz9", "tea",
		"samantha", "ssie", "oldm", "cera", "jonth", "uawei", "reckfest", "welc"]
firstName = ["Noel", "Anold", "Samantha", "Yolanda", "Elwis", "Shaun", "Brendon", "John", "Travis", "Rad", "Austin", "Shadreck",
		 "Nobuhle", "Philip", "Lionel", "Trevor", "Prince", "Jord", "Coplin", "Mark", "Mayer", "Riptide", "Sam", "Enail", "Lawrence"]
lastName = ["Nyoni", "Banda", "Dube", "Sibanda", "Nyathi", "Mlambo", "Mzilikazi", "Ncube", "Puma", "Tito", "Rakha", "Mpofu", "Moyo"]
password1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #This is to ensure that every password has atleast 1 uppercase character
password2 = "abcdefghijklmnopqrstuvwxyz123456789*!@#$%&"
#-----------------------------------------------------------------------------------------------------------------------

while index != "stop":
	number_len = 7  #Change value to increase length of Phone Number
	index = str(input("\nFirst Three Digits: "))  # For example Enter the first three digits of your phone numbers
	if index != "stop":
		number_count = int(input("How many Accounts: "))
		for x in range(0,number_count):
			number = ""
			password = ""
			for x in range(0,number_len): # x in range 0 to 7. Hence every Variable will contain 7 characters at the end of the iteration.
				password_char = random.choice(password1) + random.choice(password2)
				password += password_char
				number_char = random.choice(chars)
				number = number + number_char
				name = random.choice(usernames) + random.choice(abc)
				expansion = random.choice(chars)
				people = f"{random.choice(firstName)} {random.choice(lastName)}"
			print(f"\n{index + number} : {password + expansion} : {name + number_char + expansion} : {people}")

"""NOTE variables contain different number of characters because of concatenation. e.g password has 14 characters because we added
	password1 and password2, for those who dont understand."""






