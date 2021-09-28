# Databricks notebook source
# MAGIC %md https://adventofcode.com/2018/day/22

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 22: Mode Maze ---</h2><p>This is it, your final stop: the year <span title="Yes, really: there is no year zero.">-483</span>. It's snowing and dark outside; the only light you can see is coming from a small cottage in the distance. You make your way there and knock on the door.</p>
# MAGIC <p>A portly man with a large, white beard answers the door and invites you inside. For someone living near the North Pole in -483, he must not get many visitors, but he doesn't act surprised to see you. Instead, he offers you some milk and cookies.</p>
# MAGIC <p>After talking for a while, he asks a favor of you. His friend hasn't come back in a few hours, and he's not sure where he is.  Scanning the region briefly, you discover one life signal in a cave system nearby; his friend must have taken shelter there.  The man asks if you can go there to retrieve his friend.</p>
# MAGIC <p>The cave is divided into square <em>regions</em> which are either dominantly <em>rocky</em>, <em>narrow</em>, or <em>wet</em> (called its <em>type</em>). Each region occupies exactly one <em>coordinate</em> in <code>X,Y</code> format where <code>X</code> and <code>Y</code> are integers and zero or greater. (Adjacent regions can be the same type.)</p>
# MAGIC <p>The scan (your puzzle input) is not very detailed: it only reveals the <em>depth</em> of the cave system and the <em>coordinates of the target</em>. However, it does not reveal the type of each region. The mouth of the cave is at <code>0,0</code>.</p>
# MAGIC <p>The man explains that due to the unusual geology in the area, there is a method to determine any region's type based on its <em>erosion level</em>. The erosion level of a region can be determined from its <em>geologic index</em>. The geologic index can be determined using the first rule that applies from the list below:</p>
# MAGIC <ul>
# MAGIC <li>The region at <code>0,0</code> (the mouth of the cave) has a geologic index of <code>0</code>.</li>
# MAGIC <li>The region at the coordinates of the target has a geologic index of <code>0</code>.</li>
# MAGIC <li>If the region's <code>Y</code> coordinate is <code>0</code>, the geologic index is its <code>X</code> coordinate times <code>16807</code>.</li>
# MAGIC <li>If the region's <code>X</code> coordinate is <code>0</code>, the geologic index is its <code>Y</code> coordinate times <code>48271</code>.</li>
# MAGIC <li>Otherwise, the region's geologic index is the result of multiplying the erosion <em>levels</em> of the regions at <code>X-1,Y</code> and <code>X,Y-1</code>.</li>
# MAGIC </ul>
# MAGIC <p>A region's <em>erosion level</em> is its <em>geologic index</em> plus the cave system's <em>depth</em>, all <a href="https://en.wikipedia.org/wiki/Modulo_operation">modulo</a> <code>20183</code>. Then:</p>
# MAGIC <ul>
# MAGIC <li>If the <em>erosion level modulo <code>3</code></em> is <code>0</code>, the region's type is <em>rocky</em>.</li>
# MAGIC <li>If the <em>erosion level modulo <code>3</code></em> is <code>1</code>, the region's type is <em>wet</em>.</li>
# MAGIC <li>If the <em>erosion level modulo <code>3</code></em> is <code>2</code>, the region's type is <em>narrow</em>.</li>
# MAGIC </ul>
# MAGIC <p>For example, suppose the cave system's depth is <code>510</code> and the target's coordinates are <code>10,10</code>. Using <code>%</code> to represent the modulo operator, the cavern would look as follows:</p>
# MAGIC <ul>
# MAGIC <li>At <code>0,0</code>, the geologic index is <code>0</code>. The erosion level is <code>(0 + 510) % 20183 = 510</code>. The type is <code>510 % 3 = 0</code>, <em>rocky</em>.</li>
# MAGIC <li>At <code>1,0</code>, because the <code>Y</code> coordinate is <code>0</code>, the geologic index is <code>1 * 16807 = 16807</code>. The erosion level is <code>(16807 + 510) % 20183 = 17317</code>. The type is <code>17317 % 3 = 1</code>, <em>wet</em>.</li> 
# MAGIC <li>At <code>0,1</code>, because the <code>X</code> coordinate is <code>0</code>, the geologic index is <code> 1 * 48271 = 48271</code>. The erosion level is <code>(48271 + 510) % 20183 = 8415</code>. The type is <code>8415 % 3 = 0</code>, <em>rocky</em>.</li>
# MAGIC <li>At <code>1,1</code>, neither coordinate is <code>0</code> and it is not the coordinate of the target, so the geologic index is the erosion level of <code>0,1</code> (<code>8415</code>) times the erosion level of <code>1,0</code> (<code>17317</code>), <code>8415 * 17317 = 145722555</code>. The erosion level is <code>(145722555 + 510) % 20183 = 1805</code>. The type is <code>1805 % 3 = 2</code>, <em>narrow</em>.</li>
# MAGIC <li>At <code>10,10</code>, because they are the target's coordinates, the geologic index is <code>0</code>. The erosion level is <code>(0 + 510) % 20183 = 510</code>. The type is <code>510 % 3 = 0</code>, <em>rocky</em>.</li>
# MAGIC </ul>
# MAGIC <p>Drawing this same cave system with rocky as <code>.</code>, wet as <code>=</code>, narrow as <code>|</code>, the mouth as <code>M</code>, the target as <code>T</code>, with <code>0,0</code> in the top-left corner, <code>X</code> increasing to the right, and <code>Y</code> increasing downward, the top-left corner of the map looks like this:</p>
# MAGIC <pre><code><em>M</em>=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===<em>T</em>===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC </code></pre>
# MAGIC <p>Before you go in, you should determine the <em>risk level</em> of the area. For the rectangle that has a top-left corner of region <code>0,0</code> and a bottom-right corner of the region containing the target, add up the risk level of each individual region: <code>0</code> for rocky regions, <code>1</code> for wet regions, and <code>2</code> for narrow regions.</p>
# MAGIC <p>In the cave system above, because the mouth is at <code>0,0</code> and the target is at <code>10,10</code>, adding up the risk level of all regions with an <code>X</code> coordinate from <code>0</code> to <code>10</code> and a <code>Y</code> coordinate from <code>0</code> to <code>10</code>, this total is <code><em>114</em></code>.</p>
# MAGIC <p><em>What is the total risk level for the smallest rectangle that includes <code>0,0</code> and the target's coordinates?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''depth: 11817
target: 9,751'''

# COMMAND ----------

import re

def get_regions(depth, target_x, target_y):
  extra = 20
  geologic_index = {}
  erosion_level = {}
  region_type = {}
  for x in range(target_x + extra):
    for y in range(target_y + extra):
      if (x, y) in ((0, 0), (target_x, target_y)):
        geologic_index[(x, y)] = 0
      elif y == 0:
        geologic_index[(x, y)] = x * 16807
      elif x == 0:
        geologic_index[(x, y)] = y * 48271
      else:
        geologic_index[(x, y)] = erosion_level[(x-1, y)] * erosion_level[(x, y-1)]
      erosion_level[(x, y)] = (geologic_index[(x, y)] + depth) % 20183
      region_type[(x, y)] = erosion_level[(x, y)] % 3
  return region_type

depth, target_x, target_y = (int(x) for x in re.findall(r'\d+', inp))
regions = get_regions(depth, target_x, target_y)

answer = sum(risk_level for (x, y), risk_level in regions.items() if 0 <= x <= target_x and 0 <= y <= target_y)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Okay, it's time to go rescue the man's friend.</p>
# MAGIC <p>As you leave, he hands you some tools: a <em>torch</em> and some <em>climbing gear</em>. You can't equip both tools at once, but you can choose to use <em>neither</em>.</p>
# MAGIC <p>Tools can only be used in certain regions:</p>
# MAGIC <ul>
# MAGIC <li>In <em>rocky</em> regions, you can use the <em>climbing gear</em> or the <em>torch</em>. You cannot use <em>neither</em> (you'll likely slip and fall).</li>
# MAGIC <li>In <em>wet</em> regions, you can use the <em>climbing gear</em> or <em>neither</em> tool. You cannot use the <em>torch</em> (if it gets wet, you won't have a light source).</li>
# MAGIC <li>In <em>narrow</em> regions, you can use the <em>torch</em> or <em>neither</em> tool. You cannot use the <em>climbing gear</em> (it's too bulky to fit).</li>
# MAGIC </ul>
# MAGIC <p>You start at <code>0,0</code> (the mouth of the cave) with <em>the torch equipped</em> and must reach the target coordinates as quickly as possible. The regions with negative <code>X</code> or <code>Y</code> are solid rock and cannot be traversed. The fastest route might involve entering regions beyond the <code>X</code> or <code>Y</code> coordinate of the target.</p>
# MAGIC <p>You can <em>move to an adjacent region</em> (up, down, left, or right; never diagonally) if your currently equipped tool allows you to enter that region. Moving to an adjacent region takes <em>one minute</em>. (For example, if you have the <em>torch</em> equipped, you can move between <em>rocky</em> and <em>narrow</em> regions, but cannot enter <em>wet</em> regions.)</p>
# MAGIC <p>You can <em>change your currently equipped tool or put both away</em> if your new equipment would be valid for your current region. Switching to using the <em>climbing gear</em>, <em>torch</em>, or <em>neither</em> always takes <em>seven minutes</em>, regardless of which tools you start with. (For example, if you are in a <em>rocky</em> region, you can switch from the <em>torch</em> to the <em>climbing gear</em>, but you cannot switch to <em>neither</em>.)</p>
# MAGIC <p>Finally, once you reach the target, you need the <em>torch</em> equipped before you can find him in the dark. The target is always in a <em>rocky</em> region, so if you arrive there with <em>climbing gear</em> equipped, you will need to spend seven minutes switching to your torch.</p>
# MAGIC <p>For example, using the same cave system as above, starting in the top left corner (<code>0,0</code>) and moving to the bottom right corner (the target, <code>10,10</code>) as quickly as possible, one possible route is as follows, with your current position marked <code>X</code>:</p>
# MAGIC <pre><code>Initially:
# MAGIC <em>X</em>=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Down:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC <em>X</em>|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Right:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .<em>X</em>=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Switch from using the torch to neither tool:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .<em>X</em>=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Right 3:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|<em>X</em>|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Switch from using neither tool to the climbing gear:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|<em>X</em>|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Down 7:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..<em>X</em>==..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Right:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..=<em>X</em>=..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Down 3:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||.<em>X</em>.|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Right:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||..<em>X</em>|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Down:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.<em>X</em>..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Right 4:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===T===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=<em>X</em>||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Up 2:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===<em>X</em>===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC 
# MAGIC Switch from using the climbing gear to the torch:
# MAGIC M=.|=.|.|=.|=|=.
# MAGIC .|=|=|||..|.=...
# MAGIC .==|....||=..|==
# MAGIC =.|....|.==.|==.
# MAGIC =|..==...=.|==..
# MAGIC =||.=.=||=|=..|=
# MAGIC |.=.===|||..=..|
# MAGIC |..==||=.|==|===
# MAGIC .=..===..=|.|||.
# MAGIC .======|||=|=.|=
# MAGIC .===|=|===<em>X</em>===||
# MAGIC =|||...|==..|=.|
# MAGIC =.=|=.=..=.||==|
# MAGIC ||=|=...|==.=|==
# MAGIC |=.=||===.|||===
# MAGIC ||.|==.|.|.||=||
# MAGIC </code></pre>
# MAGIC <p>This is tied with other routes as the <em>fastest way to reach the target</em>: <code><em>45</em></code> minutes. In it, <code>21</code> minutes are spent switching tools (three times, seven minutes each) and the remaining <code>24</code> minutes are spent moving.</p>
# MAGIC <p><em>What is the fewest number of minutes you can take to reach the target?</em></p>
# MAGIC </article>

# COMMAND ----------

import heapq

def solve(regions, target_x, target_y):
  tools = {
    0: ('climbing gear', 'torch'),
    1: ('climbing gear', 'neither'),
    2: ('torch', 'neither')
  }
  
  states = [(0, 0, 0, 'torch')]
  visited = set()
  
  while states:
    d, x, y, tool = heapq.heappop(states)
    
    if (x, y, tool) in visited:
      continue
    visited.add((x, y, tool))
    
    heapq.heappush(states, (d + 7, x, y, next(new_tool for new_tool in tools[regions[(x, y)]] if new_tool != tool)))
    
    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
      new_x = x + dx
      new_y = y + dy

      if not (0 <= new_x < target_x + 20 and 0 <= new_y < target_y + 20):
        continue
      if tool not in tools[regions[(new_x, new_y)]]:
        continue
      if (new_x, new_y, tool) == (target_x, target_y, 'torch'):
        return d + 1
      heapq.heappush(states, (d + 1, new_x, new_y, tool))

answer = solve(regions, target_x, target_y)
print(answer)
