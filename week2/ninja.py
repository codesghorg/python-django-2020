

ninjas = [
    {
        'name': 'Naruto',
        'age': 16,
        'skills': {
            'Taijustu': 70,
            'Genjustu': 0,
            'Ninjustu': 65
        },
        'team': 7
    },

    {
        'name': 'Choji',
        'age': 15,
        'skills': {
            'Taijustu': 70,
            'Genjustu': 0,
            'Ninjustu': 65
        },
        'team': 3
    },

    {
        'name': 'Shino',
        'age': 17,
        'skills': {
            'Taijustu': 70,
            'Genjustu': 0,
            'Ninjustu': 75
        },
        'team': 8
    },

    {
        'name': 'Sasuke',
        'age': 16,
        'skills': {
            'Taijustu': 90,
            'Genjustu': 0,
            'Ninjustu': 95
        },
        'team': 7
    }
]


for ninja in ninjas:

    """
    Name: 
    Age: 
    Team: 
    Skills Total:
    """

    print(f"Name: {ninja['name']}")
    print(f"Age: {ninja['age']}")
    print(f"Team: {ninja['team']}")

    skills_total = sum(ninja['skills'].values())

    print(f"Skills Total: {skills_total}")
    print()
