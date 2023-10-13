users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_visits = set(users)
unique_visits_ = "Уникальные посещения"
general_visits_ = "Общее количество"
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dictionary_of_user = {general_visits_: 0, unique_visits_: 0}
count_of_user = len(users)

count_of_unique = len(unique_visits)
dictionary_of_user[general_visits_] = count_of_user
dictionary_of_user[unique_visits_] = count_of_unique

print(dictionary_of_user)
