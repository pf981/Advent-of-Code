# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/21

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: RPG Simulator 20XX ---</h2><p>Little <span title="The sky above the battle is the color of television, tuned to a dead channel.">Henry Case</span> got a new video game for Christmas.  It's an <a href="https://en.wikipedia.org/wiki/Role-playing_video_game">RPG</a>, and he's stuck on a boss.  He needs to know what equipment to buy at the shop.  He hands you the <a href="https://en.wikipedia.org/wiki/Game_controller">controller</a>.</p>
# MAGIC <p>In this game, the player (you) and the enemy (the boss) take turns attacking.  The player always goes first.  Each attack reduces the opponent's hit points by at least <code>1</code>.  The first character at or below <code>0</code> hit points loses.</p>
# MAGIC <p>Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.  An attacker always does at least <code>1</code> damage.  So, if the attacker has a damage score of <code>8</code>, and the defender has an armor score of <code>3</code>, the defender loses <code>5</code> hit points.  If the defender had an armor score of <code>300</code>, the defender would still lose <code>1</code> hit point.</p>
# MAGIC <p>Your damage score and armor score both start at zero.  They can be increased by buying items in exchange for gold.  You start with no items and have as much gold as you need.  Your total damage or armor is equal to the sum of those stats from all of your items.  You have <em>100 hit points</em>.</p>
# MAGIC <p>Here is what the item shop is selling:</p>
# MAGIC <pre><code>Weapons:    Cost  Damage  Armor
# MAGIC Dagger        8     4       0
# MAGIC Shortsword   10     5       0
# MAGIC Warhammer    25     6       0
# MAGIC Longsword    40     7       0
# MAGIC Greataxe     74     8       0
# MAGIC 
# MAGIC Armor:      Cost  Damage  Armor
# MAGIC Leather      13     0       1
# MAGIC Chainmail    31     0       2
# MAGIC Splintmail   53     0       3
# MAGIC Bandedmail   75     0       4
# MAGIC Platemail   102     0       5
# MAGIC 
# MAGIC Rings:      Cost  Damage  Armor
# MAGIC Damage +1    25     1       0
# MAGIC Damage +2    50     2       0
# MAGIC Damage +3   100     3       0
# MAGIC Defense +1   20     0       1
# MAGIC Defense +2   40     0       2
# MAGIC Defense +3   80     0       3
# MAGIC </code></pre>
# MAGIC <p>You must buy exactly one weapon; no dual-wielding.  Armor is optional, but you can't use more than one.  You can buy 0-2 rings (at most one for each hand).  You must use any items you buy.  The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.</p>
# MAGIC <p>For example, suppose you have <code>8</code> hit points, <code>5</code> damage, and <code>5</code> armor, and that the boss has <code>12</code> hit points, <code>7</code> damage, and <code>2</code> armor:</p>
# MAGIC <ul>
# MAGIC <li>The player deals <code>5-2 = 3</code> damage; the boss goes down to 9 hit points.</li>
# MAGIC <li>The boss deals <code>7-5 = 2</code> damage; the player goes down to 6 hit points.</li>
# MAGIC <li>The player deals <code>5-2 = 3</code> damage; the boss goes down to 6 hit points.</li>
# MAGIC <li>The boss deals <code>7-5 = 2</code> damage; the player goes down to 4 hit points.</li>
# MAGIC <li>The player deals <code>5-2 = 3</code> damage; the boss goes down to 3 hit points.</li>
# MAGIC <li>The boss deals <code>7-5 = 2</code> damage; the player goes down to 2 hit points.</li>
# MAGIC <li>The player deals <code>5-2 = 3</code> damage; the boss goes down to 0 hit points.</li>
# MAGIC </ul>
# MAGIC <p>In this scenario, the player wins!  (Barely.)</p>
# MAGIC <p>You have <em>100 hit points</em>.  The boss's actual stats are in your puzzle input.  What is <em>the least amount of gold you can spend</em> and still win the fight?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''Hit Points: 104
Damage: 8
Armor: 1'''

# COMMAND ----------

inp2 = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''

# COMMAND ----------

import re

boss = [int(x) for x in re.findall(r'\d+', inp)]
shop = [[[int(x) for x in re.findall(r'(?<= )\d+', line[1:])] for line in table.split('\n')[1:]] for table in inp2.split('\n\n')]

# COMMAND ----------

from itertools import chain, combinations
from heapq import heappush, heappop

def comb(l, take_min, take_max):
  return chain.from_iterable(combinations(l, r) for r in range(take_min, take_max+1))

loadouts = []
loadouts_rev = []

for weapons in comb(shop[0], 1, 1):
  for armors in comb(shop[1], 0, 1):
    for rings in comb(shop[2], 0, 2):
      cost, damage, armor = [sum(x) for x in zip(*(weapons + armors + rings))]
      heappush(loadouts, (cost, damage, armor))
      heappush(loadouts_rev, (-cost, damage, armor))

# COMMAND ----------

def does_win(loadout, boss):
  _, damage, armor = loadout
  boss_hp, boss_damage, boss_armor = boss
  
  damage = max(damage - boss_armor, 1)
  boss_damage = max(boss_damage - armor, 1)
  hp = 100
  
  while True:
    boss_hp -= damage
    hp -= boss_damage
    
    if boss_hp <= 0:
      return True
    if hp <= 0:
      return False

while True:
  loadout = heappop(loadouts)
  if does_win(loadout, boss):
    break

answer = loadout[0]
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.</p>
# MAGIC <p>What is the <em>most</em> amount of gold you can spend and still <em>lose</em> the fight?</p>
# MAGIC </article>

# COMMAND ----------

while True:
  loadout = heappop(loadouts_rev)
  if not does_win(loadout, boss):
    break

answer = -loadout[0]
answer