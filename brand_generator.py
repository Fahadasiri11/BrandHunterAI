import random

PREFIXES = [
    "Neo", "Syn", "Nova", "Core", "Meta",
    "Quantum", "Hyper", "Ultra", "Aero", "Cyber"
]

ROOTS = [
    "Vex", "Nex", "Lux", "Gen", "Mind",
    "Flow", "Mesh", "Logic", "Pulse", "Byte"
]

SUFFIXES = [
    "AI", "X", "IQ", "OS", "Hub",
    "Labs", "Tech", "Core", "Net", "Cloud"
]


def generate_names(count=20):
    names = set()

    while len(names) < count:
        name = (
            random.choice(PREFIXES)
            + random.choice(ROOTS)
            + random.choice(SUFFIXES)
        )
        names.add(name)

    return sorted(names)
