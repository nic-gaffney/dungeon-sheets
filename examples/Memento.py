"""This file describes the heroic adventurer Memento.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.18.0"

name = "Memento"
player_name = "Dylan"

# Be sure to list Primary class first
classes = ['Warlock']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Hexblade Patron"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Haunted One"
race = "Scourge Aasimar"
alignment = "Chaotic good"

xp = 0
hp_max = 27
hp_current = 27
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 13
dexterity = 12
constitution = 16
intelligence = 10
wisdom = 13
charisma = 18

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('arcana', 'intimidation', 'investigation', 'survival')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """[choose one], [choose one], Common, Celestial"""

# Inventory
# TODO: Get yourself some money
cp = 17
sp = 0
ep = 0
gp = 44
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Handaxe", "Dagger", "Longsword"]  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "None"  # Eg "leather armor"
shield = "None"  # Eg "shield"

equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Infusions for Artificer
infusions = () # Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """TODO"""

ideals = """TODO"""

bonds = """TODO"""

flaws = """TODO"""

features_and_traits = """TODO: Describe other features and abilities your
character has."""
