
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
