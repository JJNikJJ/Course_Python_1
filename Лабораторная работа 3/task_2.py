# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, sep=","):
    first_group = participants_first_group.split(sep)
    second_group = participants_second_group.split(sep)
    first_set = set(first_group)
    second_set = set(second_group)
    common_participants = sorted(list(first_set.intersection(second_set)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, sep="|")
print(common_participants)