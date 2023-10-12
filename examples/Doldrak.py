"""
This file describes the heroic adventurer Doldrak
"""
dungeonsheets_version = "0.18.0"

name = "Doldrak Salmarir"
player_name = "Nic"

classes = ['Paladin']
levels = [3]
subclasses = ["Oathbreaker"]
background = "Soldier"
race = "Dragonborn"
alignment = "Chaotic good"

xp = 0
hp_current = 23
hp_max = 28
inspiration = 1

strength = 17
dexterity = 10
constitution = 13
intelligence = 11
wisdom = 13
charisma = 16

skill_proficiencies = ('athletics', 'intimidation', 'religion', 'survival')

features = ('Harness Divine Power')
feature_choices = ("great-weapon fighting",)


weapon_proficiencies = ()
proficiencies_text = ()

languages = """Common, Draconic"""

cp = 0
sp = 0
ep = 0
gp = 8
pp = 0

weapons = ('Glaive', 'Hand Crossbow', 'Sickle')
magic_items = ('Bird of Paradise')
armor = "Rusted Plate"
shield = "shield"

equipment = """Dagger, Unarmed strike, Playing cards, Emblem, Alms box, Blanket, Candle,Tinderbox, Waterskin, Block of incense, Censer, Vestments"""
attacks_and_spellcasting = ""
spells_prepared = (
    'Ceremony',
    'Compelled Duel',
    'Cure wounds',
    'shield of faith',
    'bless'
)
__spells_unprepared = (
    'Command',
    'Detect evil and good',
    'Detect magic',
    'Detect poison and disease',
    'Divine favor',
    'Heroism',
    'Protection from evil and good',
    'Purify food and drink',
    'Searing smite',
    'Thunderous smite',
    'wrathful smite'
)
spells = spells_prepared+__spells_unprepared
wild_shapes = ()

personality_traits = """I'm haunted by my meories of war. I can't get the images of violence out of my mind."""

ideals = """Mercy. The weak deserve a second chance, and it is my job to provide it."""

bonds = """I fight for those who have fallen in war."""

flaws = """TODO: Describe your characters interesting flaws.
"""

features_and_traits = """Draconic Ancestry: Brass (Fire)"""
