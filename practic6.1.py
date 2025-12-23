
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
