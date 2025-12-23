
students = {}

def add_student(group, full_name, course, grades):
    """Додає студента до словника"""
    if group not in students:
        students[group] = []

    students[group].append({
        "ПІБ": full_name,
        "курс": course,
        "оцінки": grades
    })
add_student(
    "КН-44",
    "Обух Володимир Валентинович",
    2,
    {
        "Математика": 90,
        "Програмування": 95,
        "Фізика": 88
    }
)

add_student(
    "КН-44",
    "Грибоєдова Марина Олегівна",
    2,
    {
        "Математика": 55,
        "Програмування": 79,
        "Фізика": 87
    }
)

add_student(
    "КН-44",
    "Могильний Дмитро Валерійович",
    2,
    {
        "Математика": 85,
        "Програмування": 92,
        "Фізика": 80
    }
)
print("Список студентів:")
for group, group_students in students.items():
    print(f"\nГрупа: {group}")
    for s in group_students:
        print(s)

# РОБОТА СТУДЕНТА 2: [Грибоєдова Марина]
# Характеристика структури: Структура "словник груп із вкладеними  списками словників студентів" є логічною та зручною для 
# обробки даних по кожній групі окремо.

def average_grade(student):
    """Обчислює середній бал студента"""
    grades = student["оцінки"].values()
    return sum(grades) / len(grades) if grades else 0

def sort_students_by_average(group):
    """Сортує студентів за середнім балом (від вищого до нижчого)"""
    if group in students:
        return sorted(
            students[group],
            key=average_grade,
            reverse=True
        )
    return []

# Виведення результатів
print("--- Список студентів групи КН-44, відсортований за середнім балом ---")
sorted_students = sort_students_by_average("КН-44")

for s in sorted_students:
    print(f"{s['ПІБ']} — середній бал: {average_grade(s):.2f}")
    
# Робота зі словниками
# Третій студент: пошук та редагування даних
# Автор: Тарасенко С.В.

def find_student(full_name):
    """Пошук студента за ПІБ"""
    for group, group_students in students.items():
        for student in group_students:
            if student["ПІБ"] == full_name:
                return group, student
    return None, None

def update_grade(full_name, subject, new_grade):
    """Оновлення оцінки студента"""
    group, student = find_student(full_name)
    if student:
        student["оцінки"][subject] = new_grade
        print("Оцінку оновлено")
    else:
        print("Студента не знайдено")

# Приклад використання
update_grade("Грибоєдова Марина Олегівна", "Програмування", 79)

# Виведення оновлених даних
print("\nОновлені дані:")
for group, group_students in students.items():
    print(f"\nГрупа: {group}")
    for s in group_students:
        print(s)

# Робота зі словниками
# Четвертий студент: видалення студента + статистика по групі
# Автор: Лифар Я.С.
# Характеристика структури: дана структура є оптимальною та зручною
# для зберігання й обробки інформації про студентів у межах кожної групи.
# Вона дозволяє легко додавати, сортувати та редагувати дані,
# тому є оптимальною для навчальних задач і невеликих наборів даних.

add_student(
    "КН-44",
    "Лифар Ярослав Сергійович",
    2,
    {
        "Математика": 83,
        "Програмування": 90,
        "Фізика": 85
    }
)

add_student(
    "КН-44",
    "Невідомий студент",
    2,
    {
        "Математика": 85,
        "Програмування": 92,
        "Фізика": 80
    }
)

#Видалення студента за ПІБ
def remove_student(full_name):
    for group, group_students in students.items():
        for i, s in enumerate(group_students):
            
            if s["ПІБ"] == full_name:
                del group_students[i]
                return True
    return False

#Розрахунок статистику для групи(кількість, середній бал, середній бал по групі)
def group_statistics(group):
    
    #Перевірка існування групи 
    if group not in students or not students[group]:
        return None

    per_student_avg = {}
    total_sum = 0
    total_count = 0
     
    for s in students[group]:
        #розраховуємо средній бал для кожного студента
        per_student_avg[s["ПІБ"]] = average_grade(s)
        #cумуємо усі оцінки групи 
        grades = list(s["оцінки"].values())
        total_sum += sum(grades)
        #сумуємо кількість усіх оцінок групи
        total_count += len(grades)

    #розраховуємо середній бал по групі
    group_avg = total_sum / total_count
    return {
        "кількість": len(students[group]),
        "середній": per_student_avg,
        "середній_група": group_avg
    }

# Приклад використання 
#Виводимо список студентів до видалення
print("Список студентів групи КН-44 до видалення:")
for s in students["КН-44"]:
    print(s)

#Виводимо статистику до видалення
stats = group_statistics("КН-44")
print("\nСтатистика групи КН-44 до видалення:")
print("Кількість студентів до видалення:", stats["кількість"])
for pib, avg in stats["середній"].items():
    print(f"    {pib} — середній бал: {avg:.2f}")
print(f"    Середній бал по групі: {stats['середній_група']:.2f}")
print()

#Видаляємо студента
name_to_delete = "Невідомий студент"

if remove_student(name_to_delete):
    print(f"Було видалено студента: {name_to_delete}")
else:
    print(f"Студента для видалення з ПІБ({name_to_delete}) не знайдено!")

#Виводимо список студентів після видалення
print("\nПоточний список студентів групи КН-44:")
for s in students["КН-44"]:
    print(s)
    
#Виводимо статистику після видалення
stats = group_statistics("КН-44")
print("\nПоточна статистика групи КН-44:")
print("Кількість студентів після видалення:", stats["кількість"])
for pib, avg in stats["середній"].items():
    print(f"    {pib} — середній бал: {avg:.2f}")
print(f"    Середній бал по групі: {stats['середній_група']:.2f}")
