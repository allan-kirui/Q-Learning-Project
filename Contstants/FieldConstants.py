from Contstants import Colors

FIELDS = []

Wall = {
    "Pts": -100,
    "Icon": '#',
    "Color": Colors.DARK_GREY
}
FIELDS.append(Wall)
INDEX_WALL = 0

Path = {
    "Pts": -1,
    "Icon": '.',
    "Color": Colors.WHITE
}
FIELDS.append(Path)
INDEX_PATH = 1

Mud = {
    "Pts": -10,
    "Icon": '&',
    "Color": Colors.BROWN
}
FIELDS.append(Mud)

Target = {
    "Pts": 100,
    "Icon": 'Q',
    "Color": Colors.CYAN
}
FIELDS.append(Target)



FIELD_QuePasa = {
    "Pts": -100,
    "Icon": '?',
    "Color": Colors.LIGHT_GREY
}
