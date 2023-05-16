#Завдання 1 test2
#Перепиши наступний код за допомогою генератору списку

numbers = [3,5,45,97,32,22,10,19,39,43]
result = [number for number in numbers if number % 2 == 0]
print(result)

# Завдання 2
# Підрахуй кількість пробілів у реченні нижче використовуючи генератор списку.

story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thankyou veryю"
count = len([word for word in story.split() if len(word) > 4])
print(count)

# Завдання 3
# Підрахуй кількість слів, що більше 4 символів у реченні story, використовуючи генератор списку.

story = "Mr. and Mrs. Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thankyou very much."
count = sum([1 for i in story if i == " "])
print(count)