# # class User(object):
# #     _some_class_attr = 1

# #     def __init__(self):
# #         self.some_class_attr = 2
    
# #     # def get_some_class_attr(self):
# #     #     return self.some_class_attr

# #     def __str__(self): # redefine with the magic method
# #         return 'Hi'

# #     def __getattr__(self, item):
# #         return 'No attr {}'.format(item)


# #     @property
# #     def get_some_class_attr(self):
# #         return self._some_class_attr
    
# #     @get_some_class_attr.setter
# #     def get_some_class_attr(self, new_attr):
# #         self._some_class_attr = new_attr

# # user = User()

# # # print(user.some_class_attr) # 1
# # # print(User.some_class_attr) # 2

# # # sca = user.get_some_class_attr()  # sca - not class instanse, just var that has some attr
# # # print(sca)

# # # print(user)
# # # print(user.ddd)

# # user.get_some_class_attr = 10

# # print(user.get_some_class_attr)

# class CreateMixin(object):
#     # maybe static - means not using self - possible to make out func and not ini func on every class call
#     def create(self): 
#         print('create()')

# class UpdateMixin(object):
#     def update(self): 
#         print('update()')

# class User(CreateMixin, UpdateMixin):
#     # def __init__(self, user_name):
#     #     self._name = user_name

#     @staticmethod
#     def get_user_name(self):
#         print('koko')

#     # def get_name(self):
#     #     print("User.get_name = {}".format(self._name))

# # class User2(User):
# #     def get_name(self):
# #         print("User.get_name = {}".format(self._name))
# #         super.get_name() # calls parent method

# #     def __init__(self, a):
# #         super().__init__(a)
# #         self.some_new_attr = 'b' # call original init with modified field


# # user = User('me')

# # user.create()
# # user.update()

# User.get_user_name(User)

class User():
    __slots__ = ['name', 'last_name', 'age']

    pass

user = User()

user.name = 'i'
print(user.name)

# user.i = 10