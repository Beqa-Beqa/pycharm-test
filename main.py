from models import session, User

user_1 = User(username='Hermana', first_name='Levan', last_name='Bochor', age=25)
user_2 = User(username='Hermana2', first_name='Levan2', last_name='Bochor2', age=26)
user_3 = User(username='Hermana3', first_name='Levan3', last_name='Bochor3', age=27)

session.add_all([user_1, user_2, user_3])
session.commit()

users = session.query(User).all()

for user in users:
    print(user)