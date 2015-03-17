def get_emails(filename):
	"""Returns a dictionary of lists corresponding to emails of officers, alumni,
	members, and candidates."""
	
	dic = {'officers': [], 'alumni': [], 'members': [], 'candidates': []}

	f = open(filename, 'r')
	for line in f:
		if line == "officers@upe.berkeley.edu\n":
			email = f.readline()
			while email != "\n":
				dic['officers'].append(str.strip(email.split(',')[0]))
				email = f.readline()

		if line == "alumni@upe.berkeley.edu\n":
			email = f.readline()
			while email != "\n":
				dic['alumni'].append(str.strip(email.split(',')[0]))
				email = f.readline()

		if line == "members@upe.berkeley.edu\n":
			email = f.readline()
			while email != "\n":
				dic['members'].append(str.strip(email.split(',')[0]))
				email = f.readline()

		if line == "candidates@upe.berkeley.edu\n":
			email = f.readline()
			while email != "\n":
				dic['candidates'].append(str.strip(email.split(',')[0]))
				email = f.readline()
	
	for member_type in dic.keys():
		if dic[member_type] == []:
			return "Error with input, missing " + member_type
			
	return dic

#dic = get_emails("virtual")
#print(dic)
