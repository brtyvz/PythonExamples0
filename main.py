# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# dict = {
#     'Christian':["America",18],
#     'Daisy':["England",12],
#     "Mehmet":["Turkey",19],
#      "Dante":["İtaly",15]
# }
# dict.__delitem__("Christian")
# print("//////////////////////")
# dict ["Ahmet"] = ["Japan",29]
# print("//////////////////////")
# dict["Daisy"][1] = 14
# print(dict)
#
# print("//////////////////////")
# for key in dict.keys():
#  print(key)
#
# print("//////////////////////")
#
# for key in dict.values():
#   print(key)

list = [1, 2, 3, 4, 5, 6]
even = []
odd = []

def func(liste):
    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

even_numbers, odd_numbers = func(list)
print("Çift Sayılar:", even_numbers)
print("Tek Sayılar:", odd_numbers)






func(list)