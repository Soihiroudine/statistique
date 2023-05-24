import pandas as pd

data = pd.DataFrame(
    {
        "matieres":[
            "Java",
            "Ocaml",
            "Programmation web1",
            "Cybersecuriter",
            "Validation et test",
            "Méthode algorithmique",
            "Anglais",
            "UEO",
            "Intro Proba Stat",
            "DECOUVERTE DU MONDE DU TRAVAIL",
        ],

        "Notes":[
            13.3, 
            5.5,
            12.2,
            13,
            17,
            13,
            10,
            12.7,
            8,
            10,
        ],
        "ECTS":[
            6,
            3,
            3,
            3,
            3,
            3,
            2,
            2,
            3,
            2,
        ],
    }
)

print(data)

print()
print(data.describe())

print()
print(data["Notes"])

print()
print(data["Notes"].describe())