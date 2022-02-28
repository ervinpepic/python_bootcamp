class User:
    def __init__(self, user_id, username):  # constructor or a.k.a initializer
        self.id = user_id  # attribute 1
        self.name = username  # attribute 2
        # attribute 3 default value, so we don't need to include it in the init func
        self.followers = 0
        # attribute 4 default value, so we don't need to include it in the init func
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(1, "Erin")
user_2 = User(2, "Emel")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)