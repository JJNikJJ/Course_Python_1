# TODO Найдите количество книг, которое можно разместить на дискете
information_volume= 1.44 #Mbyte
number_of_pages = 100
number_of_lines = 50
number_of_ch = 25
single_code = 4 #byte
information_volume = information_volume * 1024 * 1024 #byte

symbol_in_book = number_of_pages * number_of_lines * number_of_ch
byte_in_book = symbol_in_book * single_code

count_of_book = information_volume//byte_in_book
print("Количество книг, помещающихся на дискету:", int(count_of_book))
