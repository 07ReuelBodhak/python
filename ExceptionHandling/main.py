class InvalidPassword(Exception):
    def __init__(self):
        self.message = "invalid password"
        super().__init__(self.message)

def check(password):
    if password != 123:
        raise InvalidPassword()

try:
    check(124)
except InvalidPassword as e:
    print(e)
