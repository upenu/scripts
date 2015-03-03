def get_emails(filename):
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

	return dic

dic = get_emails("virtual")
#print(dic)
