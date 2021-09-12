# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/3

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 3: Spiral Memory ---</h2><p>You come across an experimental new kind of memory stored on an <span title="Good thing we have all these infinite two-dimensional grids lying around!">infinite two-dimensional grid</span>.</p>
# MAGIC <p>Each square on the grid is allocated in a spiral pattern starting at a location marked <code>1</code> and then counting up while spiraling outward. For example, the first few squares are allocated like this:</p>
# MAGIC <pre><code>17  16  15  14  13
# MAGIC 18   5   4   3  12
# MAGIC 19   6   1   2  11
# MAGIC 20   7   8   9  10
# MAGIC 21  22  23---&gt; ...
# MAGIC </code></pre>
# MAGIC <p>While this is very space-efficient (no squares are skipped), requested data must be carried back to square <code>1</code> (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the <a href="https://en.wikipedia.org/wiki/Taxicab_geometry">Manhattan Distance</a> between the location of the data and square <code>1</code>.</p>
# MAGIC <p>For example:</p>
# MAGIC <ul>
# MAGIC <li>Data from square <code>1</code> is carried <code>0</code> steps, since it's at the access port.</li>
# MAGIC <li>Data from square <code>12</code> is carried <code>3</code> steps, such as: down, left, left.</li>
# MAGIC <li>Data from square <code>23</code> is carried only <code>2</code> steps: up twice.</li>
# MAGIC <li>Data from square <code>1024</code> must be carried <code>31</code> steps.</li>
# MAGIC </ul>
# MAGIC <p><em>How many steps</em> are required to carry the data from the square identified in your puzzle input all the way to the access port?</p>
# MAGIC </article>

# COMMAND ----------

inp = 289326

# COMMAND ----------

def coords():
  x, y = (1, 0)
  while True:
    yield (x, y)
    dx = (y <= -x and x >= y) - (y > -x and y >= x)
    dy = (y > -x and x > y) - (y <= -x and x < y)
    x += dx
    y += dy

def solve(target):
  num = 1
  for x, y in coords():
    num += 1
    if num == target:
      return abs(x) + abs(y)

answer = solve(inp)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As a stress test on the system, the programs here clear the grid and then store the value <code>1</code> in square <code>1</code>. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.</p>
# MAGIC <p>So, the first few squares' values are chosen as follows:</p>
# MAGIC <ul>
# MAGIC <li>Square <code>1</code> starts with the value <code>1</code>.</li>
# MAGIC <li>Square <code>2</code> has only one adjacent filled square (with value <code>1</code>), so it also stores <code>1</code>.</li>
# MAGIC <li>Square <code>3</code> has both of the above squares as neighbors and stores the sum of their values, <code>2</code>.</li>
# MAGIC <li>Square <code>4</code> has all three of the aforementioned squares as neighbors and stores the sum of their values, <code>4</code>.</li>
# MAGIC <li>Square <code>5</code> only has the first and fourth squares as neighbors, so it gets the value <code>5</code>.</li>
# MAGIC </ul>
# MAGIC <p>Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:</p>
# MAGIC <pre><code>147  142  133  122   59
# MAGIC 304    5    4    2   57
# MAGIC 330   10    1    1   54
# MAGIC 351   11   23   25   26
# MAGIC 362  747  806---&gt;   ...
# MAGIC </code></pre>
# MAGIC <p>What is the <em>first value written</em> that is <em>larger</em> than your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

import collections

def solve2(target):
  nums = collections.defaultdict(int)
  nums[(0, 0)] = 1

  for x, y in coords():
    num = sum(nums[(x+dx, y+dy)] for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)))
    nums[(x, y)] = num
    
    if num > target:
      return num

answer = solve2(inp)
answer
