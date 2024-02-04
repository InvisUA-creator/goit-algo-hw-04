def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_data = line.strip().split(  # Розділяємо рядок на ідентифікатор, ім'я та вік кота
                    ","
                )
                if len(cat_data) == 3:  # Перевіряємо, чи вірно розділено дані
                    cat_dict = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2],
                    }
                    cats_info.append(cat_dict)
                else:
                    print(f"Некоректні дані у рядку: {line}")

        return cats_info

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None


cats_info = get_cats_info("hw-4_1\\text.txt")

if cats_info is not None:
    print(cats_info)
