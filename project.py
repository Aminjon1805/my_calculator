#CALCULATOR - a ? b = c, where ? = +, -, /, *

def find_sign(smth:list):
    for i in "+-/*":
        if i in smth:
            return i


operation = input("Write your operation(a ? b, ex-> 12 + 12): ")
operation_elem = [i for i in operation if i != " "]
find_sign_val = find_sign(operation_elem)


find_position_sign = operation_elem.index(find_sign_val)
num_1 = float("".join(operation_elem[:find_position_sign]))
num_2 = float("".join(operation_elem[find_position_sign + 1:]))

if find_sign_val == "+":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")

elif find_sign_val == "-":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")

elif find_sign_val == "/":
    if num_2 == 0:
        print("ERROR!We can not divide zero 😁 !")
    else:
        print(f"{num_1} / {num_2} = {num_1 / num_2}")

elif find_sign_val == "*":
    print(f"{num_1} * {num_2} = {num_1 * num_2}")

else:
    print("Unknown operation")







