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



import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions)
ants.bees_win = lambda: None
queen_tunnel, side_tunnel = [[gamestate.places['tunnel_{0}_{1}'.format(i, j)] for j in range(9)] for i in range(2)]
queen = ants.QueenAnt()
back = ants.ThrowerAnt()
front = ants.ThrowerAnt()
guard = ants.BodyguardAnt()
guarded = ants.ThrowerAnt()
side = ants.ThrowerAnt()
bee = ants.Bee(10)
side_bee = ants.Bee(10)
queen_tunnel[0].add_insect(back)
queen_tunnel[1].add_insect(guard)
queen_tunnel[1].add_insect(guarded)
queen_tunnel[2].add_insect(queen)
queen_tunnel[3].add_insect(front)
side_tunnel[0].add_insect(side)
queen_tunnel[4].add_insect(bee)
side_tunnel[4].add_insect(side_bee)
queen.action(gamestate)
bee.armor
back.action(gamestate)
bee.armor
front.action(gamestate)
bee.armor
guard.action(gamestate)








import ants, importlib
importlib.reload(ants)
beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
gamestate = ants.GameState(None, beehive, ants.ant_types(),ants.dry_layout, dimensions)
#
# Extensive damage doubling tests
queen_tunnel, side_tunnel = [[gamestate.places['tunnel_{0}_{1}'.format(i, j)] for j in range(9)] for i in range(2)]
queen = ants.QueenAnt()
queen_tunnel[7].add_insect(queen)
# Turn 0
thrower = ants.ThrowerAnt()
fire = ants.FireAnt()
ninja = ants.NinjaAnt()
side = ants.ThrowerAnt()
front = ants.NinjaAnt()
queen_tunnel[0].add_insect(thrower)
queen_tunnel[1].add_insect(fire)
queen_tunnel[2].add_insect(ninja)
queen_tunnel[8].add_insect(front)
side_tunnel[0].add_insect(side)
# layout right now
# [thrower, fire, ninja, , , , , queen, front]
# [side   ,     ,      , , , , ,      ,      ]
thrower.damage, fire.damage, ninja.damage = 101, 102, 103
front.damage, side.damage = 104, 105
queen.action(gamestate)
(thrower.damage, fire.damage, ninja.damage)
(front.damage, side.damage)
# Turn 1
tank = ants.TankAnt()
guard = ants.BodyguardAnt()
queen_tank = ants.TankAnt()
queen_tunnel[6].add_insect(tank)          # Not protecting an ant
queen_tunnel[1].add_insect(guard)         # Guarding FireAnt
queen_tunnel[7].add_insect(queen_tank)    # Guarding QueenAnt
# layout right now
# [thrower, guard/fire, ninja, , , , tank, queen_tank/queen, front]
# [side   ,           ,      , , , ,     ,                 ,      ]
tank.damage, guard.damage, queen_tank.damage = 1001, 1002, 1003
queen.action(gamestate)
# unchanged
(thrower.damage, fire.damage, ninja.damage)













