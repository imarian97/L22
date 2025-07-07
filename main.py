from mate import medie

elevi=[
    {"nume": "Ion", "note": [9, 8, 7]},
    {"nume": "Maria", "note": [10, 9, 8]},
    {"nume": "Andrei", "note": [6, 7,]}
]

x=map(lambda e: medie(e["note"]),elevi)
print(list(x))