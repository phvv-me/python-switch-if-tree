# if...else tree

name = "Thomas Walker"

names = name.split()
if names[0] == "Arthur":
    if names[1] == "Franklin":
        initials = "A.F."
    elif names[1] == "Goodman":
        initials = "A.G."
    elif names[1] == "Walker":
        initials = "A.W."
    else:
        initials = "A."
elif names[0] == "Matthew":
    if names[1] == "Franklin":
        initials = "M.F."
    elif names[1] == "Goodman":
        initials = "M.G."
    elif names[1] == "Walker":
        initials = "M.W."
    else:
        initials = "M."
elif names[0] == "Peter":
    if names[1] == "Franklin":
        initials = "P.F."
    elif names[1] == "Goodman":
        initials = "P.G."
    elif names[1] == "Walker":
        initials = "P.W."
    else:
        initials = "P."
elif names[0] == "Thomas":
    if names[1] == "Franklin":
        initials = "T.F."
    elif names[1] == "Goodman":
        initials = "T.G."
    elif names[1] == "Walker":
        initials = "T.W."
    else:
        initials = "T."
else:
    initials = None

print(initials)

# switch pattern with dict.get()

switch = {
    "Arthur": {"Franklin": "A.F.", "Goodman": "A.G.", "Walker": "A.W."},
    "Matthew": {"Franklin": "M.F.", "Goodman": "M.G.", "Walker": "M.W."},
    "Peter": {"Franklin": "P.F.", "Goodman": "P.G.", "Walker": "P.W."},
    "Thomas": {"Franklin": "T.F.", "Goodman": "T.G.", "Walker": "T.W."},
}

names = "Thomas Walker".split()

initials = switch.get(names[0]).get(names[1], f"{names[0]}.")

print(initials)
