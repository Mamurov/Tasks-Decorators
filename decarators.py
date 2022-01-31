from datetime import datetime
# task1

# def not_during_the_night(func):
#     def wrapper():
#         if 9 <= datetime.now().hour < 21:
#             func()
#         else:
#             print("Вы сейчас не диапазоне времени 9:00-17:00")
#         return func
#     return wrapper

# @not_during_the_night
# def say_whee():
#     print("Whee!")

# say_whee()

# task2

# def time_decorator(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         print(datetime.now() - start)
#         return func
#     return wrapper

# @time_decorator
# def func_for():
#     ls = []
#     for x in range(1, 100000):
#         ls.append(x)
#     return ls

# func_for()

# # task3

# def repeat(num):
#     def get_func(func):
#         def wrap(*args, **kwargs):
#             for i in range(num):
#                 print(*args, **kwargs)
#         return wrap
#     return get_func

# @repeat(num=4)
# def func_1(text):
#     print(f"{text}")

# func_1("Hello")


# # task4

# all_data = {"name1": 12345, "name2": 4567, "theboy": 777888}

# def check_it(func):
#     def wrapper(username, password):
#         if username in all_data.keys():
#             if password in all_data.values():
#                 func(username, password)
#             else:
#                 raise Exception("Password is invalid")
#         else:
#             raise Exception("Username is Not Defined")
#     return wrapper

# @check_it
# def login(username, password):
#     print(f'Wellcome, {username}')


# def main():
#     username = input("Username: ")
#     password = int(input("Password: "))
#     login(username, password)

# main()
