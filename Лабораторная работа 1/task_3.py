list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_list = len(list_players)

first_group = list_players[0:count_of_list//2:]
second_group = list_players[count_of_list//2::]

print(first_group)
print(second_group)
