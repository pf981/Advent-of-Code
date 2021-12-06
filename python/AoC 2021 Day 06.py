# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 6: Lanternfish ---</h2><p>The sea floor is getting steeper. Maybe the sleigh keys got carried this way?</p>
# MAGIC <p>A massive school of glowing <a href="https://en.wikipedia.org/wiki/Lanternfish" target="_blank">lanternfish</a> swims past. They must spawn quickly to reach such large numbers - maybe <em>exponentially</em> quickly? You should model their growth rate to be sure.</p>
# MAGIC <p>Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes. Surely, <span title="I heard you like lanternfish.">each lanternfish creates a new lanternfish</span> once every <em>7</em> days.</p>
# MAGIC <p>However, this process isn't necessarily synchronized between every lanternfish - one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4. So, you can model each fish as a single number that represents <em>the number of days until it creates a new lanternfish</em>.</p>
# MAGIC <p>Furthermore, you reason, a <em>new</em> lanternfish would surely need slightly longer before it's capable of producing more lanternfish: two more days for its first cycle.</p>
# MAGIC <p>So, suppose you have a lanternfish with an internal timer value of <code>3</code>:</p>
# MAGIC <ul>
# MAGIC <li>After one day, its internal timer would become <code>2</code>.</li>
# MAGIC <li>After another day, its internal timer would become <code>1</code>.</li>
# MAGIC <li>After another day, its internal timer would become <code>0</code>.</li>
# MAGIC <li>After another day, its internal timer would reset to <code>6</code>, and it would create a <em>new</em> lanternfish with an internal timer of <code>8</code>.</li>
# MAGIC <li>After another day, the first lanternfish would have an internal timer of <code>5</code>, and the second lanternfish would have an internal timer of <code>7</code>.</li>
# MAGIC </ul>
# MAGIC <p>A lanternfish that creates a new fish resets its timer to <code>6</code>, <em>not <code>7</code></em> (because <code>0</code> is included as a valid timer value). The new lanternfish starts with an internal timer of <code>8</code> and does not start counting down until the next day.</p>
# MAGIC <p>Realizing what you're trying to do, the submarine automatically produces a list of the ages of several hundred nearby lanternfish (your puzzle input). For example, suppose you were given the following list:</p>
# MAGIC <pre><code>3,4,3,1,2</code></pre>
# MAGIC <p>This list means that the first fish has an internal timer of <code>3</code>, the second fish has an internal timer of <code>4</code>, and so on until the fifth fish, which has an internal timer of <code>2</code>. Simulating these fish over several days would proceed as follows:</p>
# MAGIC <pre><code>Initial state: 3,4,3,1,2
# MAGIC After  1 day:  2,3,2,0,1
# MAGIC After  2 days: 1,2,1,6,0,8
# MAGIC After  3 days: 0,1,0,5,6,7,8
# MAGIC After  4 days: 6,0,6,4,5,6,7,8,8
# MAGIC After  5 days: 5,6,5,3,4,5,6,7,7,8
# MAGIC After  6 days: 4,5,4,2,3,4,5,6,6,7
# MAGIC After  7 days: 3,4,3,1,2,3,4,5,5,6
# MAGIC After  8 days: 2,3,2,0,1,2,3,4,4,5
# MAGIC After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# MAGIC After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# MAGIC After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# MAGIC After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# MAGIC After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# MAGIC After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# MAGIC After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# MAGIC After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# MAGIC After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# MAGIC After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8
# MAGIC </code></pre>
# MAGIC <p>Each day, a <code>0</code> becomes a <code>6</code> and adds a new <code>8</code> to the end of the list, while each other number decreases by 1 if it was present at the start of the day.</p>
# MAGIC <p>In this example, after 18 days, there are a total of <code>26</code> fish. After 80 days, there would be a total of <code><em>5934</em></code>.</p>
# MAGIC <p>Find a way to simulate lanternfish. <em>How many lanternfish would there be after 80 days?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '1,1,1,1,2,1,1,4,1,4,3,1,1,1,1,1,1,1,1,4,1,3,1,1,1,5,1,3,1,4,1,2,1,1,5,1,1,1,1,1,1,1,1,1,1,3,4,1,5,1,1,1,1,1,1,1,1,1,3,1,4,1,1,1,1,3,5,1,1,2,1,1,1,1,4,4,1,1,1,4,1,1,4,2,4,4,5,1,1,1,1,2,3,1,1,4,1,5,1,1,1,3,1,1,1,1,5,5,1,2,2,2,2,1,1,2,1,1,1,1,1,3,1,1,1,2,3,1,5,1,1,1,2,2,1,1,1,1,1,3,2,1,1,1,4,3,1,1,4,1,5,4,1,4,1,1,1,1,1,1,1,1,1,1,2,2,4,5,1,1,1,1,5,4,1,3,1,1,1,1,4,3,3,3,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,5,1,3,1,4,3,1,3,1,5,1,1,1,1,3,1,5,1,2,4,1,1,4,1,4,4,2,1,2,1,3,3,1,4,4,1,1,3,4,1,1,1,2,5,2,5,1,1,1,4,1,1,1,1,1,1,3,1,5,1,2,1,1,1,1,1,4,4,1,1,1,5,1,1,5,1,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,3,2,4,1,1,2,1,1,3,2'

# COMMAND ----------

def count_fishes(fishes, days):
  timers = [0] * 9

  for fish in fishes:
    timers[fish] += 1

  for _ in range(days):
    new_timers = timers.pop(0)
    timers += [new_timers]
    timers[6] += new_timers

  return sum(timers)

fishes = [int(fish) for fish in inp.split(',')]

answer = count_fishes(fishes, 80)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?</p>
# MAGIC <p>After 256 days in the example above, there would be a total of <code><em>26984457539</em></code> lanternfish!</p>
# MAGIC <p><em>How many lanternfish would there be after 256 days?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = count_fishes(fishes, 256)
print(answer)
