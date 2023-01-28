from enum import Enum

class Pawns(Enum):
    X = ['move_down', 'attack_down']
    M = ['move_down', 'attack_down', 'move_up', 'attack_up']
    o = ['move_up', 'attack_up']
    O = ['move_down', 'attack_down', 'move_up', 'attack_up']