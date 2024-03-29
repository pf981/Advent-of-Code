# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/23

# COMMAND ----------

inp = '''.##.#.#####..##.#.#...#.##....#.######.##.#.#.##..#.#.##.#.######.#.###.##
.#.#..#####....###.####.###..##.....#####..#.#####.##...#.##.#.##....####.
........##..#.###.#.#..#..#.######..#.##.#.#####.#..##...#.#.##...###.#...
.#..#....#.......#..#...##.#.##.#..##..#.###.######.#.#.#####....#...####.
##......##.####...##.###....##.#.####..###...#..#.#...#..#.##..###.#.####.
#...#..##.######.#...##...#.#........##...#.###..#.##..##.##...#######.##.
#....#.#..###...####.....#..##.##......#.....###.##.....#.####..##..#..#..
...##.#.##.#.#...##....#.#.###.###.##..#.##.###...#..#..##..#....#.##.##.#
#....#########.####..#....##.###.##.....###.#..##...##.#####.###..##.....#
###.######.###.#####..####.#....#.###..#..###.#.####.###..#.##...##.#..#..
.##....#..##..#....######.##..###.#.#.#...###...#.###.##.#....#.##.#.####.
.......##...##..#..####.##........##...##.#.###.#####.####.##...####.#....
###.#......#..#.#.#.####...#####.#.####.#.####....#.....#.######....##.##.
###...#.##.####..#..##.#.#.#...#.###..##..##.###....##.....##..#.##..#.#..
#########.#.####..##.#.#...##.##....####..#####..#....#.#...######.###....
#.##....###..####.#..#####.#..##.###....#.#.###..##.#....###.#.#.#.#..##..
##.###....###..##..###..#.#..##.#.##.#..#.......#.##.######.#...#...#.####
##.......#.....####...#...#.##.#..##.##........####..#.....#...##.#...#.##
.##..#.#....##.....##.##.#.#.###...##...#..####...#.#.#..######.#...##....
.#....##.#.#.#..#.#.#....#....###.##.###....#.....###.#...#.##..#..####..#
..##...##..###..#####.########.##....#.#...##.##..#.#.##...##..#...##.##.#
#.#...##....#...###....#...#.##.#.##.######.##...#####...##.##...#######..
.#.#.######.##..#.####.#.##.##.##.#...####......##.....##...####..##.####.
.###.###..##.....#####...####..##...##.##.##..##...#..#.#..##.....###.#.##
#.#.####.##.#.###.###.#..#.#....#######.###......#.##.....######.....##...
##..#.#.#..#....##.....#.###.#..##.....##############.#.#.####.##..#.##.##
#.....#.#..#.##..##..##..##...###....###..##.##...##.##....#..#######..##.
##.##..###.#..###.##.####.#.#.........##.#......#.###.#..##..#...##..#.##.
..#.###.##.####.####.#..#.###...#.#.###.#.##..#....#.#.#...#....###....###
#..#...##.#....###.#.###..#...###.##.#.######......#.##.#..#..#.###.######
#.#...#.##..#....###....#.#.#.....########.#..##...#.#..############.#####
..####.#....#####.#.#.#....#..#.##....#..#..###.####.#....##.##...#.#.##.#
.##...#.#..#.###..#...#..#.#.#....#..#.###.##.#.####.#.###..#..#.....##..#
###..#.##...#.###.###...##..#.####....#.####......#..###...#...#.#....#.##
...#.######...#.########..######...##.....###.####.#.###...#.###.###.#....
##.#####...###.##.#.####..#...#.#####.##.....#....####.#####.####.###..#.#
....###...#.#..#.##.#...#....#.#.#..##########.....#..##..##..##.##.##.#..
#....#..##.#...###..####.#......########.#.......###..#...##.#.#..#.....#.
....#.......###.##.##.###.#.####.#...##.#.#..#.#.#.#.....##.#.#...#.#.#.##
###.#.##..##..####.#####.#.##.###..#.#######.##...#.#####.##.##.###..#...#
####.#.#..#..##.##..#.#.##.#.###.#...#.#..##.######.#.###.#..#..####..#..#
#......#.###.#.##...##..##...#.#..#.#.###...#..##..##.###.#.#..#.####.#..#
.###.#.#.....#.#####.....#.#..#...#...####...#.####....#..#.#...#.#.#..###
##....######.#.....##.....#.###...#..###.#.##...##..#.###.....#..#..#.#...
##..#.#.##....#.#...##.##.##.##.#.#.##..#.#..#..##.##..##..#.##..#....##.#
#.##.#.#.###...######...##.#.#.##.#.#..#...#.###..##.##.#....#..#..#.#...#
..##...#....#.##.##..##...##.......#..#####...#.#...###..#.#.##...#..#....
#.#.....##.##.#.#.#...##.#....#...#.#.##..#.####.#.#.##..#.##.##.###....##
..#.##..#.#..##.#..##....###.##...#.##...#.#....##.###.#.#.##...##.##..#.#
.######.###........#.#.....#.#.......#.##.########.#...#.#..##.##.##..####
#..##.....##....###.###.#.#..##..##..#.#.#.##.#.....##.###.#.##.##.#.#...#
.......###..##.##.####.#.#####.#..#...#####...#...#..#.##.####..##.##..##.
##....#####.##....#..###.####.###.###..#.#.#..#.#.##..#..###.#########.#..
#.###..###...#.#..#.#...#.#.##.#.######.####..#..##..##.#......###.#..#...
.##..#####..#.#....###.###.##.....##..#.##....#..##.#...####...##.#.......
##.####..##...##.#...######.###.###.#.###..####.####.##..###.##.##..######
##.#.####.#.#..#.#.###.......###......####.#.#.##.#...##..##..##.....#.#.#
.###....####.#...#.#......#####.##.##.#...###..##...##...#####....##.#..##
#..###..##....#...##.###..##.##.##########..#..##...#....##....#.......##.
###.###..#.#..#....##.#......#.###.#.#.#.#.##...#..#..##......###.##..#.#.
....##......#......#....#.##.####.####.##.###.#.##.#..#.#.#..........#.#.#
#...####...#.###..##....##..##.#####.###.#...#..#.....##.#.###.##.#...#.##
.###..##.#.###.#....#..#.###.######.##.#####..#..#.#..##.#..######.##....#
.#....###..#.#.###....##.#...###.#.#...##.#.##.##.#.#.##.#.#...#.#........
..#.##...#....##.#..#.#.#.......#..#......#..#..#..#.#.##....#.#.#...###..
##.#.#..##.##.#....#.#...........###....#..##.##.######.##.##..####.#.....
..##...###....###.#####..###......###.#..##...##....##.#.#.###....#..##..#
.#....#.#.#.###..##.##.#....#.##.##....#.#.##..###..##...###.#...#....##..
#...#...####...####...#.#.#.#####....####..#..##.###.#.#....##...#.##..##.
###..#####..#.#.#...#.#.#...#...###.####.###..#...###.####.####..##.#..#..
#...#####...##..#.###.#.#.#.#..####..##......#####....#####.####.####...##
..........#..#..#..##.#.##...##...#..#.#...#####.....#####..#...##.##.#..#
.#.##.###...#.##.#....###.#.##.##.#.####.#..##.#..#..#.#.##........#.#####
.###########.##.###.#..#.###....#......#.##.....####.####..##.....#####.#.'''

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: Unstable Diffusion ---</h2><p>You enter a large crater of gray dirt where the grove is supposed to be. All around you, plants you imagine were expected to be full of fruit are instead withered and broken. A large group of Elves has formed in the middle of the grove.</p>
# MAGIC <p>"...but this volcano has been dormant for months. Without ash, the fruit can't grow!"</p>
# MAGIC <p>You look up to see a massive, snow-capped mountain towering above you.</p>
# MAGIC <p>"It's not like there are other active volcanoes here; we've looked everywhere."</p>
# MAGIC <p>"But our scanners show active magma flows; clearly it's going <em>somewhere</em>."</p>
# MAGIC <p>They finally notice you at the edge of the grove, your pack almost overflowing from the random <em class="star">star</em> fruit you've been collecting. Behind you, elephants and monkeys explore the grove, looking concerned. Then, the Elves recognize the ash cloud slowly spreading above your recent detour.</p>
# MAGIC <p>"Why do you--" "How is--" "Did you just--"</p>
# MAGIC <p>Before any of them can form a complete question, another Elf speaks up: "Okay, new plan. We have almost enough fruit already, and ash from the plume should spread here eventually. If we quickly plant new seedlings now, we can still make it to the extraction point. Spread out!"</p>
# MAGIC <p>The Elves each reach into their pack and pull out a tiny plant. The plants rely on important nutrients from the ash, so they can't be planted too close together.</p>
# MAGIC <p>There isn't enough time to let the Elves figure out where to plant the seedlings themselves; you quickly scan the grove (your puzzle input) and note their positions.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>....#..
# MAGIC ..###.#
# MAGIC #...#.#
# MAGIC .#...##
# MAGIC #.###..
# MAGIC ##.#.##
# MAGIC .#..#..
# MAGIC </code></pre>
# MAGIC <p>The scan shows Elves <code>#</code> and empty ground <code>.</code>; outside your scan, more empty ground extends a long way in every direction. The scan is oriented so that <em>north is up</em>; orthogonal directions are written N (north), S (south), W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.</p>
# MAGIC <p>The Elves follow a time-consuming process to figure out where they should each go; you can speed up this process considerably. The process consists of some number of <em>rounds</em> during which Elves alternate between considering where to move and actually moving.</p>
# MAGIC <p>During the <em>first half</em> of each round, each Elf considers the eight positions adjacent to themself. If no other Elves are in one of those eight positions, the Elf <em>does not do anything</em> during this round. Otherwise, the Elf looks in each of four directions in the following order and <em>proposes</em> moving one step in the <em>first valid direction</em>:</p>
# MAGIC <ul>
# MAGIC <li>If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving <em>north</em> one step.</li>
# MAGIC <li>If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving <em>south</em> one step.</li>
# MAGIC <li>If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving <em>west</em> one step.</li>
# MAGIC <li>If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving <em>east</em> one step.</li>
# MAGIC </ul>
# MAGIC <p>After each Elf has had a chance to propose a move, the <em>second half</em> of the round can begin. Simultaneously, each Elf moves to their proposed destination tile if they were the <em>only</em> Elf to propose moving to that position. If two or more Elves propose moving to the same position, <em>none</em> of those Elves move.</p>
# MAGIC <p>Finally, at the end of the round, the <em>first direction</em> the Elves considered is moved to the end of the list of directions. For example, during the second round, the Elves would try proposing a move to the south first, then west, then east, then north. On the third round, the Elves would first consider west, then east, then north, then south.</p>
# MAGIC <p>As a smaller example, consider just these five Elves:</p>
# MAGIC <pre><code>.....
# MAGIC ..##.
# MAGIC ..#..
# MAGIC .....
# MAGIC ..##.
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>The northernmost two Elves and southernmost two Elves all propose moving north, while the middle Elf cannot move north and proposes moving south. The middle Elf proposes the same destination as the southwest Elf, so neither of them move, but the other three do:</p>
# MAGIC <pre><code>..##.
# MAGIC .....
# MAGIC ..#..
# MAGIC ...#.
# MAGIC ..#..
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>Next, the northernmost two Elves and the southernmost Elf all propose moving south. Of the remaining middle two Elves, the west one cannot move south and proposes moving west, while the east one cannot move south <em>or</em> west and proposes moving east. All five Elves succeed in moving to their proposed positions:</p>
# MAGIC <pre><code>.....
# MAGIC ..##.
# MAGIC .#...
# MAGIC ....#
# MAGIC .....
# MAGIC ..#..
# MAGIC </code></pre>
# MAGIC <p>Finally, the southernmost two Elves choose not to move at all. Of the remaining three Elves, the west one proposes moving west, the east one proposes moving east, and the middle one proposes moving north; all three succeed in moving:</p>
# MAGIC <pre><code>..#..
# MAGIC ....#
# MAGIC #....
# MAGIC ....#
# MAGIC .....
# MAGIC ..#..
# MAGIC </code></pre>
# MAGIC <p>At this point, no Elves need to move, and so the process ends.</p>
# MAGIC <p>The larger example above proceeds as follows:</p>
# MAGIC <pre><code>== Initial State ==
# MAGIC ..............
# MAGIC ..............
# MAGIC .......#......
# MAGIC .....###.#....
# MAGIC ...#...#.#....
# MAGIC ....#...##....
# MAGIC ...#.###......
# MAGIC ...##.#.##....
# MAGIC ....#..#......
# MAGIC ..............
# MAGIC ..............
# MAGIC ..............
# MAGIC 
# MAGIC == End of Round 1 ==
# MAGIC ..............
# MAGIC .......#......
# MAGIC .....#...#....
# MAGIC ...#..#.#.....
# MAGIC .......#..#...
# MAGIC ....#.#.##....
# MAGIC ..#..#.#......
# MAGIC ..#.#.#.##....
# MAGIC ..............
# MAGIC ....#..#......
# MAGIC ..............
# MAGIC ..............
# MAGIC 
# MAGIC == End of Round 2 ==
# MAGIC ..............
# MAGIC .......#......
# MAGIC ....#.....#...
# MAGIC ...#..#.#.....
# MAGIC .......#...#..
# MAGIC ...#..#.#.....
# MAGIC .#...#.#.#....
# MAGIC ..............
# MAGIC ..#.#.#.##....
# MAGIC ....#..#......
# MAGIC ..............
# MAGIC ..............
# MAGIC 
# MAGIC == End of Round 3 ==
# MAGIC ..............
# MAGIC .......#......
# MAGIC .....#....#...
# MAGIC ..#..#...#....
# MAGIC .......#...#..
# MAGIC ...#..#.#.....
# MAGIC .#..#.....#...
# MAGIC .......##.....
# MAGIC ..##.#....#...
# MAGIC ...#..........
# MAGIC .......#......
# MAGIC ..............
# MAGIC 
# MAGIC == End of Round 4 ==
# MAGIC ..............
# MAGIC .......#......
# MAGIC ......#....#..
# MAGIC ..#...##......
# MAGIC ...#.....#.#..
# MAGIC .........#....
# MAGIC .#...###..#...
# MAGIC ..#......#....
# MAGIC ....##....#...
# MAGIC ....#.........
# MAGIC .......#......
# MAGIC ..............
# MAGIC 
# MAGIC == End of Round 5 ==
# MAGIC .......#......
# MAGIC ..............
# MAGIC ..#..#.....#..
# MAGIC .........#....
# MAGIC ......##...#..
# MAGIC .#.#.####.....
# MAGIC ...........#..
# MAGIC ....##..#.....
# MAGIC ..#...........
# MAGIC ..........#...
# MAGIC ....#..#......
# MAGIC ..............
# MAGIC </code></pre>
# MAGIC <p>After a few more rounds...</p>
# MAGIC <pre><code>== End of Round 10 ==
# MAGIC .......#......
# MAGIC ...........#..
# MAGIC ..#.#..#......
# MAGIC ......#.......
# MAGIC ...#.....#..#.
# MAGIC .#......##....
# MAGIC .....##.......
# MAGIC ..#........#..
# MAGIC ....#.#..#....
# MAGIC ..............
# MAGIC ....#..#..#...
# MAGIC ..............
# MAGIC </code></pre>
# MAGIC <p>To make sure they're on the right track, the Elves like to check after round 10 that they're making good progress toward covering enough ground. To do this, count the number of empty ground tiles contained by the smallest rectangle that contains every Elf. (The edges of the rectangle should be aligned to the N/S/E/W directions; the Elves do not have the patience to calculate <span title="Arbitrary Rectangles is my Piet Mondrian cover band.">arbitrary rectangles</span>.) In the above example, that rectangle is:</p>
# MAGIC <pre><code>......#.....
# MAGIC ..........#.
# MAGIC .#.#..#.....
# MAGIC .....#......
# MAGIC ..#.....#..#
# MAGIC #......##...
# MAGIC ....##......
# MAGIC .#........#.
# MAGIC ...#.#..#...
# MAGIC ............
# MAGIC ...#..#..#..
# MAGIC </code></pre>
# MAGIC <p>In this region, the number of empty ground tiles is <code><em>110</em></code>.</p>
# MAGIC <p>Simulate the Elves' process and find the smallest rectangle that contains the Elves after 10 rounds. <em>How many empty ground tiles does that rectangle contain?</em></p>
# MAGIC </article>

# COMMAND ----------

import collections


def needs_to_move(row, col, elves):
  return any(pos in elves for pos in [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)])


def get_proposal(row, col, round_num, elves):
  propose = [None] * 4

  if all(pos not in elves for pos in [(row - 1, col), (row - 1, col + 1), (row - 1, col - 1)]):
    propose[0] = (row - 1, col)

  if all(pos not in elves for pos in [(row + 1, col), (row + 1, col + 1), (row + 1, col - 1)]):
    propose[1] = (row + 1, col)

  if all(pos not in elves for pos in [(row, col - 1), (row - 1, col - 1), (row + 1, col - 1)]):
    propose[2] = (row, col - 1)

  if all(pos not in elves for pos in [(row, col + 1), (row - 1, col + 1), (row + 1, col + 1)]):
    propose[3] = (row, col + 1)

  for _ in range(4):
    if propose[round_num % 4]:
      break
    round_num += 1
  return propose[round_num % 4]
  

def simulate(elves, round_num):
  is_done = True
  proposals = {} # new_pos: old_pos
  for row, col in elves:
    if not needs_to_move(row, col, elves):
      continue
    is_done = False

    if proposal := get_proposal(row, col, round_num, elves):
      proposals[proposal] = (row, col) if proposal not in proposals else None

  new_elves = {new_pos for new_pos, old_pos in proposals.items() if old_pos}
  new_elves.update(elves - set(proposals.values()))

  return frozenset(new_elves), is_done


start_elves = frozenset({(row, col) for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line) if c == '#'})
elves = start_elves
for round_num in range(10):
  elves, _ = simulate(elves, round_num)

side_lengths = [(1 + max(dim) - min(dim)) for dim in zip(*elves)]
answer = side_lengths[0] * side_lengths[1] - len(elves)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>It seems you're on the right track. Finish simulating the process and figure out where the Elves need to go. How many rounds did you save them?</p>
# MAGIC <p>In the example above, the <em>first round where no Elf moved</em> was round <code><em>20</em></code>:</p>
# MAGIC <pre><code>.......#......
# MAGIC ....#......#..
# MAGIC ..#.....#.....
# MAGIC ......#.......
# MAGIC ...#....#.#..#
# MAGIC #.............
# MAGIC ....#.....#...
# MAGIC ..#.....#.....
# MAGIC ....#.#....#..
# MAGIC .........#....
# MAGIC ....#......#..
# MAGIC .......#......
# MAGIC </code></pre>
# MAGIC <p>Figure out where the Elves need to go. <em>What is the number of the first round where no Elf moves?</em></p>
# MAGIC </article>

# COMMAND ----------

import itertools

elves = start_elves
for round_num in itertools.count():
  elves, is_done = simulate(elves, round_num)
  if is_done:
    break

answer = round_num + 1
print(answer) # 12 seconds
