



# importing pandas as pd
# import pandas as pd
#
# # dictionary of lists
# dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
# 		'degree': ["MBA", "BCA", "M.Tech", "MBA"],
# 		'score':[90, 40, 80, 98]}
#
# df = pd.DataFrame(dict)
#
# print(df)


# importing pandas module
# import pandas as pd
#
# # Define a dictionary containing employee data
# data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#          'Age': [27, 24, 22, 32],
#          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#          'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
#
# # Define a dictionary containing employee data
# data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
#          'Age': [17, 14, 12, 52],
#          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#          'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}
#
# # Convert the dictionary into DataFrame
# df = pd.DataFrame(data1, index=[0, 1, 2, 3])
#
# # Convert the dictionary into DataFrame
# df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
#
# print(df, "\n\n", df1)
#
# # using a .concat() method
# frames = [df, df1]
#
# res1 = pd.concat(frames)
# print(res1)






























# # list_consti = [1,1,1,2,3,3]
# # winning_len_conti = len(list_consti)/2
# # number_of_parties = len(set(list_consti))
# # winning_percent = 50
# # # output_ = [(1,2),(1,3)]
# # vote_count = {}
# #
# # for party in list_consti:
# #     if party not in vote_count.keys():
# #         vote_count.update({party:list_consti.count(party)})
# #
# # max_seat_win = max(vote_count.values())
# # wining_combination = []
# #
# # def func():
# #     for key, values in vote_count.items():
# #         if values > max_seat_win:
# #             return key
# #         else:
# #             wining_combination.append(key)
# from select import select
# from unicodedata import numeric
#
# # print(func())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import numpy as np
# # import pandas as pd
# # arr = np.array([1, 2, 3])
# # df = pd.DataFrame({'Col': arr})
#
# # list_in = ["sdgsd", "ssgsd", "erts","gtdf","iuyu","sa","poiu"]
# #
# # s_order = ["e","g","s"]
# # output_dict = {}
# #
# # for item in list_in:
# #     if item[:1] in s_order:
# #         output_dict.update({item:s_order.index(item[:1])})
# #     else:
# #         output_dict.update({item: len(list_in) +1})
# # print(output_dict)
# # print(list(i[0] for i in sorted(output_dict.items() , key=lambda x:x[1])))
#
# # union = remove duplicates
# # union all = sare aayenge dono
# #
# # select c1, count(c2)
# # where =
# # group by = aggregation k basis pr
# # having = aggregation function
# #
# # select
# # union
# # select
# # union
# # select
#
# table yes/no
# create table yesno(
#     field int
#     value varchar(10)
# )
# Insert into yeasno(
#
#
# )
#
# select
#
#
# #normalisation 1. first normal form 2.
# student table(
#     id,name,subjects
#     1, ashutosh, 'Maths,English,Hindi')
# )

# input= "a1b4h5"
# # output: abbbbhhhhh
#
# def fxn(input):
#     i = 0
#     while i < len(input):
#         char = input[i]
#         num = ''
#         i = i+1
#         while i< len(input) and input[i].isdigit():
#             num = num + input[i]
#             i = i + 1
#         print(char*int(num),end='')
#
# print(fxn(input))
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
#         return result
#     return wrapper
#
# @timer
# def my_function():
#     # Some time-consuming operation here
#     # for i in range(100):
#     time.sleep(1)
#     print("adfsdgsdgf")
#
# my_function()


# import pandas as pd
# import pandas as pd
#
# # list of strings
# # lst = ['Geeks', 'For', 'Geeks', 'is',
# # 			'portal', 'for', 'Geeks']
# #
# # # Calling DataFrame constructor on list
# # df = pd.DataFrame(lst)
# # print(df)
# data = {'Name': ['Tom', 'nick', 'krish', 'jack'], 'Age': [20, 21, 19, 18]}
#
# # Create DataFrame
# df = pd.DataFrame(data)
#
# # Print the output.
# print(df)

# def make_multiplier(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
# double = make_multiplier(2)
# print(double(5))  # Output: 10

# from multiprocessing import Process
#
# def print_numbers():
#     for i in range(5):
#         print(i)
#
# if __name__ == "__main__":
#     p1 = Process(target=print_numbers)
#     p2 = Process(target=print_numbers)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
# Design a plugin architecture for a media player supporting various formats (MP3, MP4, AVI) that allows adding new formats without modifying the core codebase.
#
#    SRP: Each plugin handles one format.
#    OCP: New formats are added as plugins without changing the core code.
#    LSP: Plugins are substitutable without media player modification.
#    ISP: Plugins implement only relevant methods.
#    DIP: Media player depends on an abstraction that plugins follow.
#
# Deliverables: Design the system using SOLID principles, provide code snippets and explain adherence to SOLID principles.

# task_list1 = [3,6,8,5]
# task_list2 = [5,10,13,7]
#
# (3,6),(3,8),(6,5)
#
# output_task_pair = []
#
# def task_schedular():
    