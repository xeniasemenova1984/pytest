# тестовый пример 1
i_tuple = (25, 1, 3, 100, 200, 13, 2)
max_element = max(i_tuple)
print("Максимальный элемент кортежа: ", max_element)
assert max_element == 200

# тестовый пример 2
count = i_tuple.count(max_element+1)
print("Не найден элемент:", max_element+1)
assert count == 0

# тестовый пример 3
def hi(x="Hi"):
      print(x)
      assert count != "Bye"

i_tuple2 = ("Hello", "Good mornihg")
x = i_tuple2[1]
hi(x)

# тестовый пример 4
def get_fruct(x="Apple"):
      print(x)
      assert count != "tomato"

dict_sample = {1: "mango", 2: "pawpaw"}
get_fruct(dict_sample[2])

# тестовый пример 5
def get_names(names):
      l = []
      for i in names.items():
            if len(i[1]) == 4:
                  l.append(i)
      assert len(l) == 4
      print(l)

names = {1:"Ryan", 2:"Kieran", 3:"Mark", 4:"John", 5:"David", 6:"Paul"}
get_names(names)

# тестовый пример 6
def get_answer(names):
      x = names["Mark"]
      y = names["Kieran"]
      z = names["Ryan"]
      try:
            assert (z + y) / x
      except ZeroDivisionError:
            print("Деление на ноль")

names = {"Ryan":1, "Kieran":2, "Mark":0}
get_answer(names)