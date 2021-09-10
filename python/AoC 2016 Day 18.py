# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/18

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 18: Like a Rogue ---</h2><p>As you enter this room, you hear a loud click! Some of the tiles in the floor here seem to be pressure plates for <a href="https://nethackwiki.com/wiki/Trap">traps</a>, and the trap you just triggered has run out of... whatever it tried to do to you. You doubt you'll be so lucky next time.</p>
# MAGIC <p>Upon closer examination, the traps and safe tiles in this room seem to follow a pattern. The tiles are arranged into rows that are all the same width; you take note of the safe tiles (<code>.</code>) and traps (<code>^</code>) in the first row (your puzzle input).</p>
# MAGIC <p>The type of tile (trapped or safe) in each row is based on the types of the tiles in the same position, and to either side of that position, in the previous row. (If either side is off either end of the row, it counts as "safe" because there isn't a trap embedded in the wall.)</p>
# MAGIC <p>For example, suppose you know the first row (with tiles marked by letters) and want to determine the next row (with tiles marked by numbers):</p>
# MAGIC <pre><code>ABCDE
# MAGIC 12345
# MAGIC </code></pre>
# MAGIC <p>The type of tile <code>2</code> is based on the types of tiles <code>A</code>, <code>B</code>, and <code>C</code>; the type of tile <code>5</code> is based on tiles <code>D</code>, <code>E</code>, and an imaginary "safe" tile. Let's call these three tiles from the previous row the <em>left</em>, <em>center</em>, and <em>right</em> tiles, respectively. Then, a new tile is a <em>trap</em> only in one of the following situations:</p>
# MAGIC <ul>
# MAGIC <li>Its <em>left</em> and <em>center</em> tiles are traps, but its <em>right</em> tile is not.</li>
# MAGIC <li>Its <em>center</em> and <em>right</em> tiles are traps, but its <em>left</em> tile is not.</li>
# MAGIC <li>Only its <em>left</em> tile is a trap.</li>
# MAGIC <li>Only its <em>right</em> tile is a trap.</li>
# MAGIC </ul>
# MAGIC <p>In any other situation, the new tile is safe.</p>
# MAGIC <p>Then, starting with the row <code>..^^.</code>, you can determine the next row by applying those rules to each new tile:</p>
# MAGIC <ul>
# MAGIC <li>The leftmost character on the next row considers the left (nonexistent, so we assume "safe"), center (the first <code>.</code>, which means "safe"), and right (the second <code>.</code>, also "safe") tiles on the previous row. Because all of the trap rules require a trap in at least one of the previous three tiles, the first tile on this new row is also safe, <code>.</code>.</li>
# MAGIC <li>The second character on the next row considers its left (<code>.</code>), center (<code>.</code>), and right (<code>^</code>) tiles from the previous row. This matches the fourth rule: only the right tile is a trap. Therefore, the next tile in this new row is a trap, <code>^</code>.</li>
# MAGIC <li>The third character considers <code>.^^</code>, which matches the second trap rule: its center and right tiles are traps, but its left tile is not. Therefore, this tile is also a trap, <code>^</code>.</li>
# MAGIC <li>The last two characters in this new row match the first and third rules, respectively, and so they are both also traps, <code>^</code>.</li>
# MAGIC </ul>
# MAGIC <p>After these steps, we now know the next row of tiles in the room: <code>.^^^^</code>. Then, we continue on to the next row, using the same rules, and get <code>^^..^</code>. After determining two new rows, our map looks like this:</p>
# MAGIC <pre><code>..^^.
# MAGIC .^^^^
# MAGIC ^^..^
# MAGIC </code></pre>
# MAGIC <p>Here's a larger example with ten tiles per row and ten rows:</p>
# MAGIC <pre><code>.^^.^.^^^^
# MAGIC ^^^...^..^
# MAGIC ^.^^.^.^^.
# MAGIC ..^^...^^^
# MAGIC .^^^^.^^.^
# MAGIC ^^..^.^^..
# MAGIC ^^^^..^^^.
# MAGIC ^..^^^^.^^
# MAGIC .^^^..^.^^
# MAGIC ^^.^^^..^^
# MAGIC </code></pre>
# MAGIC <p>In ten rows, this larger example has <code>38</code> safe tiles.</p>
# MAGIC <p>Starting with the map in your puzzle input, in a total of <code>40</code> rows (including the starting row), <em>how many safe tiles</em> are there?</p>
# MAGIC </article>

# COMMAND ----------

inp = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'

# COMMAND ----------

import collections

def count_safe(s, n_rows):
  traps = collections.defaultdict(bool, enumerate(c == '^' for c in s))
  indexes = list(range(len(s)))
  safe_count = sum(not traps[i] for i in indexes)
  
  for _ in range(n_rows - 1):
    new_traps = collections.defaultdict(bool)
    
    for i in indexes:
      neighbors = (traps[i - 1], traps[i], traps[i + 1])
      if neighbors in [(1, 1, 0), (0, 1, 1), (1, 0, 0), (0, 0, 1)]:
        new_traps[i] = True
        
    traps = new_traps
    safe_count += sum(not traps[j] for j in indexes)
  return safe_count

answer = count_safe(inp, 40)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p><em>How many safe tiles</em> are there in a total of <span title="You feel a wrenching sensation."><code>400000</code> rows</span>?</p>
# MAGIC </article>

# COMMAND ----------

answer = count_safe(inp, 400000)
answer
