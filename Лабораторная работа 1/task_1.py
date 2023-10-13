numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
count = 0
for i in range(0, len(numbers)):
    if numbers[i] is None:
        count = i
        numbers[i] = 0

sum_of_num = sum(numbers)
count_of_num = len(numbers)
average = sum_of_num / count_of_num
numbers[count] = average
print("Измененный список:", numbers)
