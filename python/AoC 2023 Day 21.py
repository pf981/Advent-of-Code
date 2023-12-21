# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/21

# COMMAND ----------

inp = '''...................................................................................................................................
.....###.........#..#.........#.............#........##....#................##.......#..#.#.....#......#..#..#..##........#........
.#.............#............#...#.#...#.............#....#.................#.......#................#.....#....#.................#.
..#.......#..........#..........#......#.........#........................#.#...##.........#.......#.....#.##..#.............#.....
....#...#..##......#................##......#..#..#........................##.......#.............#..............##................
........#....#........#..#......#....#......#........#.........................#.....#.#.........#.................#..#..##....#...
.......................#...#.....#.....#..........#..#.........#............##.#...........#.....#..#.##..........#......#.#.....#.
..........#..........#....#.##.#...................#..#...........#...............#...........................#.....#.......##.....
.#.##..........#....#.#...#.....#.............#...............#.....................#.......#.#......#..................#..#.......
......#.#.#...................#..#.............................#...............#....#..............................###...........#.
....#...#...................#..................#...........####....#...............#....#..#.................#................#....
.............#..#.#..##.....#...#.......##.#...............#.........##..........#......................##....##....#.......#...#..
....#....#......###.#......#..#....#..#.........#....................................................#............#.........#.#....
.......#.#........##........#..#............#.##.............#..#...#....................#.#.....##.................#..............
....#....#....##...#..#......#.#.......................##......#.......................#..#.#..........#.#...........#..........#..
.#.......#..#......#......#..#............................##..........................#.............#.......#...##.#...............
...#..#...................#....#....#.....##...........#...............#...#...........#.#.#..#.#.#.#.#..#..#...#.#....#...........
.....................#..#.#..#..#..........#........#.................#.......#.......#.#......#.#..#........#............##.......
.......................................#...#.................###...##.#.....##.........##.........#..............#........#........
........#.##.........#........#.....##.............#...#...............#...................#..#.................#.........#.....#..
..#..#.#........#.....#.................................#............#.#....#.#...............##...#.....#............#..#.........
....#......#.....#....................#.........#.................#......................................................#.#....#..
....##...#...##..........#..............................#..#...#....#.......................#.#.#.....#.......#..#............##...
.#.....#.........#........#...#.....###...........#...............#.#...........#.#..........##..#..#................#..........#..
...#..#.#.#.......................................................#.##...#..........##............#..#.....#.........###...#....#..
......###.......#.#....##......#..#....................#........#.............#.#..........................#....#......###..#....#.
........#..........#......#....#.............#..#.................#..............................#.......#.#................#......
.#........#...........#.........#.....................#.........#........##.#.###......................####..#.#....#............#.
..##........#............#.#.......................#.....#.##.................#..#....#............................................
.............#..##....#.#.#...............#..................#.......##.#.....#...................##...##...#.##.............###...
......#..#....##.............................#.............................#..#....#....##.........#...#................#...#.##.#.
..#...........#........................#...........#....#...............#...............#...................#......................
....#...#.#.#...........#.#................###...............#.....##........#........................#.....##...#.#..........#....
.#..#.............#...#....##........#...#.............#............................#..#..#...........#...............##...........
...#......#..........................#.#.....##........#...#.......#...#...........##......#..............#..#.#...#.....#.#....#..
.#.#..............#................##.....#........#.....##...#....................#......#..#..............................#......
.#....................#.............#....#.............##.......#...........#.#......#...................##...#..............#.....
.....#.#...#.........##................#......#.....#...#....##.....................................................##.............
.............#........#............#.#.....#.........##.................##.....###.........#...............#....#..........#.....#.
..#.#...#....#...#......................##............#...#.#..#.........##.................................#......#........#....#.
..#.....#..................................#.#.....................#..#....#.....###..#.#...#..#.....#.......#..#..................
....#....##.#.....#.......................#.#...#......#.......................#.....#.........#....#...............#.......#......
....#.###.#......#...................#.............#...............##.........##........#......#....#..........#........##....###..
.....###....#...#.......................##.#....#.#...#.#..........#...#.....#......#.........#........#............#.....#...#....
...#.#.....#..#..............................##....#......#....#............#..#.#............#...#................................
...............#........##.#####.#......#.........................#....................#.#.#...##.#.##.#.#..................##.....
..#............................#.............#.#....#..........##.......#.#......#.#.#........#..#.#.##..................#.........
..##..##.#.............#..#.....#..#....#.#.#......#........#.................##.............#......#....#.#...........#......#..#.
..........##.#.........#.....##...................#.#...#...........................#........#...........................####......
.#......#.#.#.......#...............#.##..........#........#.................#..#.#.......#.............#....#.....................
.#.....#..#........#..#.....#...........#.#.....#.#.#...#..#..#.....#..........#.#......#............###.#.#...............#.....#.
..................##...#.......#...............#...........#.......#...............#........................................#......
.##.................#..#........#......##.............#..#.#..#....................#....................##.#.............###.......
.#......#...........#..........#...................#.........#.......##...........##..#......#.#....#.....#........................
.........................#.#.....#..#....#...#......#......................#............#................#.........................
....#....................#...#..#..............#..#...#..#..#...............#.....................#...........#..##...........#....
....#.........#...........#.....................#.#....#...#.................##.......#.#.........#...#............##..............
......................#........#...#...................#...#.###....#....#....#...............#....#...#....#......................
..................##......................##.....#...........#..........##..##.#......##............#.##...........................
.#.....................#.......#.................#..#........#...........#.#....#......#........#...........#......................
...........#.........#....#..#.#.#....#..#.......##.........#.............................#....#..#......#.#...#........#..........
.........#.........#.#....#.#.......................#..#......................#.................#....................#.#.#.........
......................#...#...#.........##.....#..............##......#...###......#...#....#.....##...........##........##........
............##..#.#......#...#.............#..#..#.........#...........#...#..#.........#...#......................................
...........#...........#..#......##..........#........#....#....#........#..................#...#.......##..#..#..#......#.........
.................................................................S.................................................................
..............#...#......#..#.....#................##......#............#........#........#..............#......#...........#......
...........#..#......#..#....#.....#..................#.....#...............#....#.....#..........#............#.#......#..#.......
..............#........#.#....#...#............#....#......#..........................................#.............#....#.........
..................#...#...............#.#...#..........#......................#.#.#.#.......#.....#..#........###..................
...................#.........##.#.#.....#..........#...........#.........#.#..#..##......#........#................................
.#.................#.....#.....#.##........#..........#...........#....#.....#...#.....#.........#..#........#.......#.#...........
..................#........#......##.#....##...#.#....#..#.....#....#...................#.....#...##...#.#......................#..
...##..............#..................#......................#.........##...#....#..#....#...........#.#..#........#...........#...
..#..#.............#................#............#............#.......#..#...##.....#.......#.......#.....#..................#.#...
..#.............#...................................#.............#......................................#..........#..............
.....#................#......#..#............#......#..#.##.#......#.......#.....#..#.........................##...........#...#.#.
...#.#............#......##........#.............#.....#..............#......###......#................#..................#......#.
....#...#.........#..#.##...###.#..............#........#..............#.#.........##....#.#.#......#....#.................#...#...
.##...#..#..........##............#........###.....#............#..#.........#............#.#.#........#..#..###............#......
.......#.................#.......#...#.......#..#......#..............#......#..##.................##....#.......................#.
...........................#.....#........#..#..............#.....##..........#....#..............#..#......##.............#.......
......#.................#................#...#.......................#.#.......##..#.........#....#.....##.............#.#.....#...
........................#.#.#.....##.......##.#........##.....#.....#...#....................#..........#..........................
.#...#........#............#.....#...#.....................#...........#.............#.##.#.....#......#.#...................#...#.
.....#..........#...........#...........................#.#.........#.............#..#.#..#...#.#....#..##..........#...........#..
.....#....#..#..................#....#...#......................#.......#..................#.......................#....#....#..#..
...#..............#...........#.#...........#.........#....#.........#.##.#..#......##.........#...##............##..#.#..#.....#..
..#............................#...#.....#......#.........#...#.....................#.....#.....#..#..#.............#..#...........
......#....#.....#.....................#.#.......#.#.#.....##.......#...#.............#..#.......#.............#..........#.#......
...............##..#................#.........#...##......#..#......#.#..#..........###..#..#..##............#..........#...#....#.
.#....#...........#..#.........#.#.#....#....#.........#.#............#....#...............##..................#.....#......#......
........#...#.....#.#................#...#....#..#....#.#..#.........#...#.................#..#.........................#..........
.........##...........................................#.................#...#.....#..#...##......#.........##............#...#.....
..#..#..#...#.#..................#....#.................#.#...#.........#.......#......##..#....#.........#......#....#............
...#...#......#....##...................##....#......#......#......#.......#.................#..#.............#.#..................
.#...#...#..##......#.#................#.#.................##..##.#..#...#.........#.........#..........................#..##......
.....................#..#..............#.......#..#...##.....................##...#....#.......................#..........#........
.......#.........#.#.....##..........#..#......#......#..#......#...#..................#....#......................................
.....#...#.....#........##......................##..................#..#...#.........###.#..#............................#.#....#..
........#....#...........#..#..........#.#.........................................#..#....#.......#...#...#...............###.....
....##..............#..#.................#..........#...........#.....#.....#....#....#.##....................#......#..#..........
..#..#..##..........##....#.#....................#.....#.#.....#............#.#........#............#....................#......#..
..........#..##......##........#....................#..#.#.............#......#........#.........#.....#....##..............##..#..
.#.......#...........#.......#.............#......###.....##.#....#....#..#....#...............................#.#..#...#.#....#...
............#....##...........#.............#.......................#......#.#...#...............##...#.....#...................#..
..#........#.........#....#..........................#....................###................#....................#.#..............
.....#..#.#........#............#.#..##.......#.....#..#...........#.........................#.......#.....#.......#........#...#..
.....##........................#..#.............#..............##.....#.....#.....#........#................#....#..##.#.........#.
..#...#........#.#...........#...#..............#.#.....#.....#.......................................#..#.#..................#....
...........#.#.....#..........#.#.......#.................#.......#.#...........#.............##........#.............#...#..#.#...
....#.....#....##.#........##..#..#.#........................#.........#.......#.........#.....###.....#.#.........................
.......#.....#.........#....#..#....#.....#..........#.#.#.........#.....#....#.........#.................#..........#...#.........
.#......#.........#..#...#......#.............................#...........#...............#.......#...#..........#...#......###....
.....................#..............#.#......#...........#......#....#.#...##.............#...##.#..#.###.#..............#.........
.#...#.............#.....#.....##..#........#............#..##....###....#.................#..#.#...##.#...#..........#...#.#......
.........#..#.....#..........................#.#..........##..#...##......................#...................#.....#............#.
.....#...##............#.........##...###......#...................#..................................#...........##..#............
.......#......................#....#...#..................#........#.#...#...........#.................#........#..........#.#.....
............#..............#.#.#..........#...#............#.......#............#.#.....#..##....#...#.#.....##........#...........
...........##.#..#...........#...#.....#.....#.............#......................#...........#...#.#.....#.......#..#..#..........
...#.#......#..#..#...............................#.............#.#..................#....#.#....#..............#................#.
.....#..................#...##.....#.#..#.#.#...................#..........................#.................#....#.....#..........
.............#..#..#....#.#..#..##...............#...............................#....#........#..#..#.......##.#........#.........
....#....#................##..#.........#.#..#....................#..............#...#......#...#..#...............................
......#....##.........##..............#....#....#.#..#..#....................................#...........#.#.#.#.###......#........
.#.#.....#.#..#.....#.....#.......##...#.......................................##......................#..........#.#....#..##..#..
............#..#.#........#..........#....#..#.....#.....#................#....##...........#...##....##.##....##.....##.#.........
...#....#...##..#.#.........#............#.........#.......................##..#.............................##....#..#.........#..
.......#.#............#...#...##....##.#..##..............#............#..............#....#.....#...#....##....#....#........#....
...................................................................................................................................
'''

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: Step Counter ---</h2><p>You manage to catch the <a href="7">airship</a> right as it's dropping someone else off on their all-expenses-paid trip to Desert Island! It even helpfully drops you off near the <a href="5">gardener</a> and his massive farm.</p>
# MAGIC <p>"You got the sand flowing again! Great work! Now we just need to wait until we have enough sand to filter the water for Snow Island and we'll have snow again in no time."</p>
# MAGIC <p>While you wait, one of the Elves that works with the gardener heard how good you are at solving problems and would like your help. He needs to get his <a href="https://en.wikipedia.org/wiki/Pedometer" target="_blank">steps</a> in for the day, and so he'd like to know <em>which garden plots he can reach with exactly his remaining <code>64</code> steps</em>.</p>
# MAGIC <p>He gives you an up-to-date map (your puzzle input) of his starting position (<code>S</code>), garden plots (<code>.</code>), and rocks (<code>#</code>). For example:</p>
# MAGIC <pre><code>...........
# MAGIC .....###.#.
# MAGIC .###.##..#.
# MAGIC ..#.#...#..
# MAGIC ....#.#....
# MAGIC .##..S####.
# MAGIC .##..#...#.
# MAGIC .......##..
# MAGIC .##.#.####.
# MAGIC .##..##.##.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>The Elf starts at the starting position (<code>S</code>) which also counts as a garden plot. Then, he can take one step north, south, east, or west, but only onto tiles that are garden plots. This would allow him to reach any of the tiles marked <code>O</code>:</p>
# MAGIC <pre><code>...........
# MAGIC .....###.#.
# MAGIC .###.##..#.
# MAGIC ..#.#...#..
# MAGIC ....#O#....
# MAGIC .##.OS####.
# MAGIC .##..#...#.
# MAGIC .......##..
# MAGIC .##.#.####.
# MAGIC .##..##.##.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>Then, he takes a second step. Since at this point he could be at <em>either</em> tile marked <code>O</code>, his second step would allow him to reach any garden plot that is one step north, south, east, or west of <em>any</em> tile that he could have reached after the first step:</p>
# MAGIC <pre><code>...........
# MAGIC .....###.#.
# MAGIC .###.##..#.
# MAGIC ..#.#O..#..
# MAGIC ....#.#....
# MAGIC .##O.O####.
# MAGIC .##.O#...#.
# MAGIC .......##..
# MAGIC .##.#.####.
# MAGIC .##..##.##.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>After two steps, he could be at any of the tiles marked <code>O</code> above, including the starting position (either by going north-then-south or by going west-then-east).</p>
# MAGIC <p>A single third step leads to even more possibilities:</p>
# MAGIC <pre><code>...........
# MAGIC .....###.#.
# MAGIC .###.##..#.
# MAGIC ..#.#.O.#..
# MAGIC ...O#O#....
# MAGIC .##.OS####.
# MAGIC .##O.#...#.
# MAGIC ....O..##..
# MAGIC .##.#.####.
# MAGIC .##..##.##.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>He will continue like this until his steps for the day have been exhausted. After a total of <code>6</code> steps, he could reach any of the garden plots marked <code>O</code>:</p>
# MAGIC <pre><code>...........
# MAGIC .....###.#.
# MAGIC .###.##.O#.
# MAGIC .O#O#O.O#..
# MAGIC O.O.#.#.O..
# MAGIC .##O.O####.
# MAGIC .##.O#O..#.
# MAGIC .O.O.O.##..
# MAGIC .##.#.####.
# MAGIC .##O.##.##.
# MAGIC ...........
# MAGIC </code></pre>
# MAGIC <p>In this example, if the Elf's goal was to get exactly <code>6</code> more steps today, he could use them to reach any of <code><em>16</em></code> garden plots.</p>
# MAGIC <p>However, the Elf <em>actually needs to get <code>64</code> steps today</em>, and the map he's handed you is much larger than the example map.</p>
# MAGIC <p>Starting from the garden plot marked <code>S</code> on your map, <em>how many garden plots could the Elf reach in exactly <code>64</code> steps?</em></p>
# MAGIC </article>

# COMMAND ----------

import collections

lines = inp.splitlines()
plots = {(row, col) for row, line in enumerate(lines) for col, c in enumerate(line) if c in 'S.'}
start_pos = next((row, col) for row, line in enumerate(lines) for col, c in enumerate(line) if c == 'S')

side_len = len(lines) # Assume square
target = 26501365
remainder = 26501365 % side_len

q = collections.deque([(start_pos, 0)])
seen = set() # (steps % 2, pos)

cur_step = 0
reach_counts = []
while q:
  pos, steps = q.popleft()

  if steps > cur_step:
    if cur_step == 64:
      answer1 = len({pos for i, pos in seen if i == cur_step % 2})
    if cur_step % side_len == remainder:
      reach_counts.append(len({pos for i, pos in seen if i == cur_step % 2}))
    cur_step = steps

  if (pos[0] % side_len, pos[1] % side_len) not in plots or (steps % 2, pos) in seen:
    continue
  seen.add((steps%2, pos))

  if len(reach_counts) == 3:
    break

  for d in 'NESW':
    new_pos = (
      pos[0] + (d == 'S') - (d == 'N'),
      pos[1] + (d == 'E') - (d == 'W')
    )
    q.append((new_pos, steps + 1))

print(answer1)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The Elf seems confused by your answer until he realizes his mistake: he was reading from a <span title="Next up: 729.">list</span> of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.</p>
# MAGIC <p>The <em>actual</em> number of steps he needs to get today is exactly <code><em>26501365</em></code>.</p>
# MAGIC <p>He also points out that the garden plots and rocks are set up so that the map <em>repeats infinitely</em> in every direction.</p>
# MAGIC <p>So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:</p>
# MAGIC <pre><code>.................................
# MAGIC .....###.#......###.#......###.#.
# MAGIC .###.##..#..###.##..#..###.##..#.
# MAGIC ..#.#...#....#.#...#....#.#...#..
# MAGIC ....#.#........#.#........#.#....
# MAGIC .##...####..##...####..##...####.
# MAGIC .##..#...#..##..#...#..##..#...#.
# MAGIC .......##.........##.........##..
# MAGIC .##.#.####..##.#.####..##.#.####.
# MAGIC .##..##.##..##..##.##..##..##.##.
# MAGIC .................................
# MAGIC .................................
# MAGIC .....###.#......###.#......###.#.
# MAGIC .###.##..#..###.##..#..###.##..#.
# MAGIC ..#.#...#....#.#...#....#.#...#..
# MAGIC ....#.#........#.#........#.#....
# MAGIC .##...####..##..S####..##...####.
# MAGIC .##..#...#..##..#...#..##..#...#.
# MAGIC .......##.........##.........##..
# MAGIC .##.#.####..##.#.####..##.#.####.
# MAGIC .##..##.##..##..##.##..##..##.##.
# MAGIC .................................
# MAGIC .................................
# MAGIC .....###.#......###.#......###.#.
# MAGIC .###.##..#..###.##..#..###.##..#.
# MAGIC ..#.#...#....#.#...#....#.#...#..
# MAGIC ....#.#........#.#........#.#....
# MAGIC .##...####..##...####..##...####.
# MAGIC .##..#...#..##..#...#..##..#...#.
# MAGIC .......##.........##.........##..
# MAGIC .##.#.####..##.#.####..##.#.####.
# MAGIC .##..##.##..##..##.##..##..##.##.
# MAGIC .................................
# MAGIC </code></pre>
# MAGIC <p>This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked <code>S</code>, though - every other repeated <code>S</code> is replaced with a normal garden plot (<code>.</code>).</p>
# MAGIC <p>Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:</p>
# MAGIC <ul>
# MAGIC <li>In exactly <code>6</code> steps, he can still reach <code><em>16</em></code> garden plots.</li>
# MAGIC <li>In exactly <code>10</code> steps, he can reach any of <code><em>50</em></code> garden plots.</li>
# MAGIC <li>In exactly <code>50</code> steps, he can reach <code><em>1594</em></code> garden plots.</li>
# MAGIC <li>In exactly <code>100</code> steps, he can reach <code><em>6536</em></code> garden plots.</li>
# MAGIC <li>In exactly <code>500</code> steps, he can reach <code><em>167004</em></code> garden plots.</li>
# MAGIC <li>In exactly <code>1000</code> steps, he can reach <code><em>668697</em></code> garden plots.</li>
# MAGIC <li>In exactly <code>5000</code> steps, he can reach <code><em>16733044</em></code> garden plots.</li>
# MAGIC </ul>
# MAGIC <p>However, the step count the Elf needs is much larger! Starting from the garden plot marked <code>S</code> on your infinite map, <em>how many garden plots could the Elf reach in exactly <code>26501365</code> steps?</em></p>
# MAGIC </article>

# COMMAND ----------

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

X = np.array([0, 1, 2]).reshape(-1, 1)
Y = np.array(reach_counts).reshape(-1, 1)
X_poly = PolynomialFeatures(degree=2).fit_transform(X)
model = LinearRegression()
model.fit(X_poly, Y)

z = target // side_len
X2 = PolynomialFeatures(degree=2).fit_transform(np.array(z).reshape(1, -1))
answer2 = int(model.predict(X2)[0][0])
print(answer2)
