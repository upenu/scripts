from users.models import UserProfile

def get_users():
	"""
		Returns a dictionary of users, in the form:
		{<user_type>:[list of email addresses]}

		where user_type is the INTEGER representation of the type of user (see models.py on the server)
	"""
    users = UserProfile.objects.all()
    result = {t[0]:[] for t in UserProfile.USER_TYPES}
    
    for user in users:
        result[user.user_type].append(user.user.email)
    return result
