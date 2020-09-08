students = [
    {
        'name': 'Student 1',
        'age': 24,
        'course': 'Computer Science',
        'marks': {
            'Python Programming': {'mark':  80, 'hours': 3},
            'Network Admin': {'mark':  79, 'hours': 3},
            'Internet': {'mark':  89, 'hours': 2},
            'Calculus':{'mark':   78, 'hours': 1},
            'Algebra': {'mark':  90,  'hours': 2}
        }
    },

    {
        'name': 'Student 2',
        'age': 25,
        'course': 'Computer Science',
        'marks': {
            'Python Programming':{'mark':  60, 'hours': 3},
            'Network Admin':{'mark':  69, 'hours': 3},
            'Internet': {'mark': 79, 'hours': 2},
            'Calculus': {'mark': 68, 'hours': 1},
            'Algebra': {'mark': 80, 'hours': 2}
        }
    },

    {
        'name': 'Student 3',
        'age': 21,
        'course': 'Computer Science',
        'marks': {
            'Python Programming': {'mark': 90, 'hours': 3},
            'Network Admin':{'mark': 97, 'hours': 3},
            'Internet': {'mark': 98,'hours': 2},
            'Calculus': {'mark': 87,'hours': 1},
            'Algebra': {'mark': 90,'hours': 2},
        }
    }
]


def calculate_cwa(marks):
    s = 0
    h = 0
    for mark in marks.values():
        s += mark['mark'] * mark['hours']
        h += mark['hours']
    
    cwa = s/h
    return cwa

def calculate_mean(marks):
    s = 0
    h = 0
    for mark in marks.values():
        s += mark['mark']
        h += 1
    
    mean = s/h
    return mean


def print_marks(marks):
    print(f"Course          Marks")
    print("======          =====")
    for subject, mark in marks.items():
        print(f"{subject}          {mark}")


def print_grade_report(students):
    print()
    for s in students:

        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
        print()
        print(f"Grade Report for {s['name']}")
        
        print_marks(s['marks'])
        
        mean = calculate_mean(s['marks'])

        cwa = calculate_cwa(s['marks'])

        print()
        print(f"Mean scores is {mean}")
        print(f"Your CWA is {cwa}")
        print()


print_grade_report(students)
