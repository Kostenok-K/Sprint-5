import random


class UserData:
    current_user = {'name': 'Кирилл', 'email': 'kostenokkirill@gmail.com', 'password': '123456'}
    random_user = {'name': 'Кирилл', 'email': f'kostenok{random.randint(100, 999)}@gmail.com',
                   'password': f'{random.randint(100000, 999999)}'}
