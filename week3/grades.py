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
    string = ""
    string += f"Course          Marks\n"
    string += "======          =====\n"
    for subject, mark in marks.items():
        string += f"{subject}          {mark}\n"
    return string


def print_grade_report(students):
    report_list = []
    for s in students:

        string = "\n"
        string += f"Name: {s['name']}\n"
        string += f"Age: {s['age']}\n"
        string += f"Course: {s['course']}\n"
        string += "\n"
        string += f"Grade Report for {s['name']}\n"
        
        string += print_marks(s['marks'])
        
        mean = calculate_mean(s['marks'])

        cwa = calculate_cwa(s['marks'])

        string += "\n"
        string += f"Mean scores is {mean}\n"
        string += f"Your CWA is {cwa}\n"
        string += "\n"

        report_list.append({
            'name': s['name'],
            'report': string
        })
    
    return report_list

