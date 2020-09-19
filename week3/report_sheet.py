import grades

from pprint import pprint

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

reports = grades.print_grade_report(students)

for report in reports:
    
    report_file = open(f"{report['name']} Report.txt", 'w')

    report_file.write(report['report'])

    report_file.close()
