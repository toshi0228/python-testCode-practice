

def get_username(user):
    return user.username


def get_sign(user):
    return user.get_fullname()

# def get_username(user):
#     """ ユーザー user を受け取りユーザー名を返す
#     """
#     return user.username

# def get_sign(user):
#     """ ユーザー user を受け取り 'John Doe <john@example.com>' 形式の署名を返す
#     """
#     return user.get_fullname() + ' <' + user.email + '>'
