from functools import wraps
import time 

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time

class User:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"

class Users:
    def __init__(self, users: dict[User]):
        self.users = users

    # @timefn
    def __getitem__(self, user_id: str):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def __repr__(self) -> str:
        return f"Users(users={self.users})"
    

if __name__ == "__main__":
    users = [
        User("1", "John", ""),
        User("2", "Jane", "")
    ]
    users = Users(users)
    print(users["1"])
    print(users["2"])

