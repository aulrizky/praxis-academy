

class User:
    def __init__(self,username,location):
        print('user being created')
        self.username = username
        self.location = location
    
    def insert(self):
        print('inserting user')
        data = {}
        data[self.username] = self.location
        print(data)

user_input = User('buto','rawapening')
data = User.insert(user_input)


