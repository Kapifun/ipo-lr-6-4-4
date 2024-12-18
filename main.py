# Запрашиваем у пользователя строку для поиска
search_string = input("Введите строку для поиска: ")
# Открываем файл и читаем его содержимое
with open('text.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
# Находим строки, содержащие искомую подстроку
matching_lines = []
for line in lines:
    if search_string in line:
        matching_lines.append(line.strip())
# Выводим количество найденных строк
print(f"\nКоличество найденных строк: {len(matching_lines)}")
# Выводим строки
for line in matching_lines:
    print(line)
# Сортируем строки
sorted_lines = sorted(matching_lines, key=len)
# Выводим отсортированные строки по длине
print("\nОтсортированные строки по длине:")
for line in sorted_lines:
    print(line)