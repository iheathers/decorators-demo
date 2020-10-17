import functools


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(*args):
            if user['access_level'] == access_level:
                return func(*args)
        return secure_func
    return my_decorator


@user_has_permission('admin')
def my_func(password):
    return f"Password: {password}"


@user_has_permission('admin')
def another():
    print("Hello")


user = {'name': "Jude", 'access_level': 'admin'}

# my_func = user_has_permission(my_func)

print(my_func(1234))
print(another())
