# 2nd Quarter Project
from pyscript import document, display


def candidate_checker(e):
    club_members = ['kristine pasco', 'renn santos', 'luisito balajadia',
                    'josua ortiz', 'vivian carabot', 'jean evangelista',
                    'jubilee caballero', 'hariette onofre']

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations {candidate}! You are now part of the ICT club.')  # 0 and 1, True or False

    document.getElementById('result').innerHTML = messages[member_checker]


def result_checker(e):
    document.getElementById('output').innerHTML = " "
    grade7 = {'Alice Blue', 'Anita Bath', 'Justin Case'}
    grade8 = {'Eileen Dover', 'Ella Vator', 'Joe Kerr', 'Paige Turner'}
    grade9 = {'Sheldon Cooper', 'Billy Sparks', 'Tam Nguyen'}
    grade10 = {'Juanito Lakarin', 'Restituto Fruto', 'Ligaya Anonuevo', 'Francisco Portero'}

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value
    new_members = first_name + " " + last_name
    new_members_set = {new_members}        
    all_members = grade7 | grade8 | grade9 | grade10 | new_members_set
    total_members = len(grade7 | grade8 | grade9 | grade10 | new_members_set)

    members_list = "<br>".join(sorted(all_members))

    document.getElementById('output').innerHTML = f'All members:<br>  {members_list}'
    display(f'Total members: {total_members}', target='output') 


# Skills test - 2nd Quarter
from pyscript import display, document

non_metals = {
    "H":  ("Hydrogen",    1,  1.008),
    "He": ("Helium",      2,  4.0026),
    "C":  ("Carbon",      6,  12.011),
    "N":  ("Nitrogen",    7,  14.007),
    "O":  ("Oxygen",      8,  15.999),
    "F":  ("Fluorine",    9,  18.998),
    "Ne": ("Neon",       10,  20.180),
    "P":  ("Phosphorus", 15,  30.974),
    "S":  ("Sulfur",     16,  32.06),
    "Cl": ("Chlorine",   17,  35.45),
    "Ar": ("Argon",      18,  39.948),
    "Se": ("Selenium",   34,  78.971),
    "Br": ("Bromine",    35,  79.904),
    "Kr": ("Krypton",    36,  83.798),
    "I":  ("Iodine",     53,  126.90),
    "Xe": ("Xenon",      54,  131.29),
    "Rn": ("Radon",      86,  222)
}

def element_checker(e):
    document.getElementById('result').innerHTML = " "
    element1 = document.getElementById('element_name').value.strip().title()
    
    # Using .get() - no if statement
    result = non_metals.get(
    element1,
    ("Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {element1}<br>
    <b>Element:</b> {result[0]}<br>
    <b>Atomic Number:</b> {result[1]}<br>
    <b>Atomic Mass:</b> {result[2]}
    """
