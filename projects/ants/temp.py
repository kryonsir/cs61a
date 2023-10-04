from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
gamestate = GameState(None, beehive, ant_types(), layout, (1, 9))
#
# Testing bodyguard performs thrower's action
bodyguard = BodyguardAnt()
thrower = ThrowerAnt()
bee = Bee(2)
# Place bodyguard before thrower
gamestate.places["tunnel_0_0"].add_insect(bodyguard)
gamestate.places["tunnel_0_0"].add_insect(thrower)
gamestate.places["tunnel_0_3"].add_insect(bee)
bodyguard.action(gamestate)
bee.armor
