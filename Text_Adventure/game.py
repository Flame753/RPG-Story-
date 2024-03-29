from player import Player
import world
from collections import OrderedDict


def play():
    print("Escape from Cave Terror!")
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        room.modify_mana(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
            dashline()  # makes dash lines on the screen
        elif not player.is_alive():
            print("Your journey has come to an early end!")


def get_available_action(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print Inventory")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, world.EnemyTile) and not room.enemy.is_alive():
        action_adder(actions, 'inv', player.investigate, "Investigate Corpse")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
        action_adder(actions, 'sp', player.spell_attack, "Spell Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world. tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
        if player.currentHP < 100:
            action_adder(actions, 'h', player.heal, "Heal")

        action_adder(actions, 'st', player.status, "Stats")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_action = get_available_action(room, player)
        action_input = input("Action: ")
        action = available_action.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")
            dashline()


def dashline():  # makes dash lines on the screen
    print("-"*20)


play()
