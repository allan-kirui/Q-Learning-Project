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

Target = {
    "Pts": 100,
    "Icon": 'Q',
    "Color": Colors.LIGHT_PURPLE
}
FIELDS.append(Target)
INDEX_TARGET = 2

Mud = {
    "Pts": -10,
    "Icon": '&',
    "Color": Colors.BROWN
}
FIELDS.append(Mud)

Fence = {
    "Pts": -20,
    "Icon": 'H',
    "Color": Colors.PURPLE
}
FIELDS.append(Fence)

FIELD_QuePasa = {
    "Pts": -100,
    "Icon": '?',
    "Color": Colors.LIGHT_GREY
}
