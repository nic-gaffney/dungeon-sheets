"""This file describes the heroic adventurer Alwynn.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.18.0"

name = "Alwynn"
player_name = "Brie"

# Be sure to list Primary class first
classes = ['Rogue']
levels = [3]
subclasses = ["Soulknife"]
background = "Pirate"
race = "Wood Elf"
alignment = "Neutral evil"

xp = 0
hp_max = 23
hp_current = 23
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 10
dexterity = 17
constitution = 13
intelligence = 10
wisdom = 11
charisma = 12

# Select what skills you're proficient with
skill_proficiencies = ('deception', 'sleight of hand', 'stealth', 'acrobatics', 'athletics', 'perception')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ('deception', 'sleight of hand')

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
features = ('Steady aim')

# If selecting among multiple feature options:
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ("Thieve's Tools")

# Proficiencies and languages
languages = """Common, Elvish"""

# Inventory
cp = 0
sp = 0
ep = 0
gp = 49
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Dagger", "Shortsword","Scorching Slasher"]
magic_items = ('Potion of Healing')
armor = "Studded Leather Armor"
shield = "None"

equipment = """A belaying pin, common clothes, Thieves tools"""

attacks_and_spellcasting = """"""

# List of known spells
spells_prepared = ()  

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Infusions for Artificer
infusions = ()

# Backstory
# Describe your backstory here
personality_traits = """TODO"""

ideals = """TODO"""

bonds = """TODO"""

flaws = """TODO"""

features_and_traits = """Panataism is the idea that the gods are not gods, just Rahaezal split into aspects of personality. A Panatanist will live life to the extremes, trying to feel a godly amount of one type of feeling. They try to witness the world with as much emotional emphasis as possible in order to understand the different “emanations” of Rahaezal’s soul. Thus, their zeal for life is a celebration of Rahaezals sacrifice and their evocation of Rahaezal’s spirit through feeling."""
