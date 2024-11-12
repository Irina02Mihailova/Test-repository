class User:
    def __init__(self, id, name, access_level='user'):
        self._id = id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name, access_level='admin')
        print(f'Пользователь {name} добавлен.')

    def add_user(self, user_list, id, name):
        new_user = User(id, name)
        user_list.append(new_user)
        print(f'Пользователь {name} добавлен.')

    def remove_user(self, user_list, id):
        for user in user_list:
            if user.get_user_id() == id:
                user_list.remove(user)
                print(f'Пользователь {user.get_name()} удален.')
                return
        print('Пользователь не найден.')

user_list = []

admin = Admin(id=1, name='Admin User')

admin.add_user(user_list, id=2, name='Виктория')
admin.add_user(user_list, id=3, name='Николай')
admin.add_user(user_list, id=4, name='Евгений')
admin.add_user(user_list, id=5, name='Мария')

for user in user_list:
    print(f'id - {user.get_user_id()}, name - {user.get_name()}, access_level - {user.get_access_level()}')

admin.remove_user(user_list, 2)

for user in user_list:
    print(f'id - {user.get_user_id()}, name - {user.get_name()}, access_level - {user.get_access_level()}')

