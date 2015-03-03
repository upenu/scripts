from users.models import UserProfile

def get_users():
    users = UserProfile.objects.all()
    result = {t[0]:[] for t in UserProfile.USER_TYPES}
    for user in users:
        result[user.user_type].append(user.user.email)
    return result
