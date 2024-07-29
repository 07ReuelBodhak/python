authenticated = False

def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Function {func.__name__} called with arguments {args}, {kwargs}")
        result = func(*args,*kwargs)
        print(f"Function {func.__name__} returned {result}")
    return wrapper

def requires_authentication(func):
    def wrapper(*args, **kwargs):
        if not authenticated:
            raise Exception("Authentication Failed")
        return func(*args, **kwargs)
    return wrapper

def caching_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def login():
        global authenticated
        print("Welcome to login Page")
        username = input("please Enter username :")
        password = input("please enter password :")
        result = authentication(username,password)
        if result:
            authenticated = True
            home()
        else:
            print("invalid authentication")
            authenticated = False
            home()

@caching_decorator
def authentication(username,password):
    if username == "xyz" and password == "pqr":
        return {"username" : username, "password" : password}
    else:
        return None
    
@requires_authentication
def home():
    return "sensitive data"

try:
    print(login())
    if authenticated:
        print(home())
except Exception as e:
    print(e)