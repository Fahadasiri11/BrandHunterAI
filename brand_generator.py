import random

WORDS = {
    "AI": {
        "prefix": [
            "Neo", "Syn", "Cogni", "Agent", "Deep",
            "Smart", "Auto", "Nova", "Core", "Intel"
        ],
        "suffix": [
            "ra", "ify", "ora", "exa", "ium",
            "gen", "ica", "lyt", "verse", "ix"
        ]
    },

    "SaaS": {
        "prefix": [
            "Cloud", "Flow", "Task", "Sync", "Work",
            "Stack", "Scale", "Link", "Launch", "Boost"
        ],
        "suffix": [
            "ly", "hub", "pro", "base", "space",
            "grid", "suite", "desk", "pilot", "logic"
        ]
    },

    "Cybersecurity": {
        "prefix": [
            "Cyber", "Secure", "Shield", "Fort", "Safe",
            "Guard", "Zero", "Vault", "Cipher", "Trust"
        ],
        "suffix": [
            "lock", "net", "core", "point", "gate",
            "matrix", "wall", "node", "zone", "sync"
        ]
    },

    "Finance": {
        "prefix": [
            "Fin", "Pay", "Cash", "Money", "Fund",
            "Prime", "Capital", "Credit", "Vault", "Coin"
        ],
        "suffix": [
            "flow", "wise", "pilot", "grid", "link",
            "hub", "base", "logic", "mint", "stack"
        ]
    },

    "Healthcare": {
        "prefix": [
            "Medi", "Health", "Care", "Bio", "Life",
            "Well", "Vital", "Nova", "Pure", "Cure"
        ],
        "suffix": [
            "core", "lab", "tech", "care", "plus",
            "nova", "wise", "path", "link", "sense"
        ]
    }
}


def generate_names(industry="AI", count=20):

    words = WORDS.get(industry, WORDS["AI"])

    names = set()

    while len(names) < count:

        name = (
            random.choice(words["prefix"]) +
            random.choice(words["suffix"])
        )

        names.add(name)

    return sorted(names)
