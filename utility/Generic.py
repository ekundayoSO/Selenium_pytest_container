import random
import string


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


username = generate_random_string(3)
domain = random.choice(["gmail.com"])
random_email = f"{username}@{domain}"
print(random_email)


def generate_random_password(length=6):
    characters = string.ascii_letters + string.ascii_uppercase + string.hexdigits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Usage example:
random_password = generate_random_password()
print(random_password)


def reused_info():
    my_email = "ncu@gmail.com"
    my_password = "%+G~@*la"
    return my_email, my_password
