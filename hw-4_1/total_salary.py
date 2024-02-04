def total_salary(path):
    total_salary = 0
    number_of_salaries = 0

    try:
        with open(path, "r") as file: # Відкриття файлу
            for line in file:  # Проходимось по ньому
                salary = int(line.strip().split(",")[1]) # Читання рядків
                total_salary += salary # Загальна сума
                number_of_salaries += 1 # Кількість рядків

        average_salary = int(
            total_salary / number_of_salaries
        )  # Обчислення середньої заробітної плати

        print(
            f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average_salary}"  # Вивід результату
        )

    except FileNotFoundError:
        print("Файл не знайдено.") # Обробка
    except Exception as e:
        print(f"Сталася помилка: {e}") # Обробка


total_salary("hw-4_1\\path.txt")  # Виклик
