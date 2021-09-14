# Databricks notebook source
# MAGIC %md https://adventofcode.com/2017/day/6

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 6: Memory Reallocation ---</h2><p>A debugger program here is having an issue: it is trying to repair a memory reallocation routine, but it keeps getting stuck in an infinite loop.</p>
# MAGIC <p>In this area, there are <span title="There are also five currency banks, two river banks, three airplanes banking, a banked billards shot, and a left bank.">sixteen memory banks</span>; each memory bank can hold any number of <em>blocks</em>. The goal of the reallocation routine is to balance the blocks between the memory banks.</p>
# MAGIC <p>The reallocation routine operates in cycles. In each cycle, it finds the memory bank with the most blocks (ties won by the lowest-numbered memory bank) and redistributes those blocks among the banks. To do this, it removes all of the blocks from the selected bank, then moves to the next (by index) memory bank and inserts one of the blocks. It continues doing this until it runs out of blocks; if it reaches the last memory bank, it wraps around to the first one.</p>
# MAGIC <p>The debugger would like to know how many redistributions can be done before a blocks-in-banks configuration is produced that <em>has been seen before</em>.</p>
# MAGIC <p>For example, imagine a scenario with only four memory banks:</p>
# MAGIC <ul>
# MAGIC <li>The banks start with <code>0</code>, <code>2</code>, <code>7</code>, and <code>0</code> blocks. The third bank has the most blocks, so it is chosen for redistribution.</li>
# MAGIC <li>Starting with the next bank (the fourth bank) and then continuing to the first bank, the second bank, and so on, the <code>7</code> blocks are spread out over the memory banks. The fourth, first, and second banks get two blocks each, and the third bank gets one back. The final result looks like this: <code>2 4 1 2</code>.</li>
# MAGIC <li>Next, the second bank is chosen because it contains the most blocks (four). Because there are four memory banks, each gets one block. The result is: <code>3 1 2 3</code>.</li>
# MAGIC <li>Now, there is a tie between the first and fourth memory banks, both of which have three blocks. The first bank wins the tie, and its three blocks are distributed evenly over the other three banks, leaving it with none: <code>0 2 3 4</code>.</li>
# MAGIC <li>The fourth bank is chosen, and its four blocks are distributed such that each of the four banks receives one: <code>1 3 4 1</code>.</li>
# MAGIC <li>The third bank is chosen, and the same thing happens: <code>2 4 1 2</code>.</li>
# MAGIC </ul>
# MAGIC <p>At this point, we've reached a state we've seen before: <code>2 4 1 2</code> was already seen. The infinite loop is detected after the fifth block redistribution cycle, and so the answer in this example is <code>5</code>.</p>
# MAGIC <p>Given the initial block counts in your puzzle input, <em>how many redistribution cycles</em> must be completed before a configuration is produced that has been seen before?</p>
# MAGIC </article>

# COMMAND ----------

inp = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'

# COMMAND ----------

import itertools

def redistribute(block_counts):
    i = block_counts.index(max(block_counts))
    remaining = block_counts[i]
    block_counts[i] = 0

    while remaining:
        i = (i + 1) % len(block_counts)
        block_counts[i] += 1
        remaining -= 1

def count_cycles(block_counts):
    block_counts = block_counts.copy()
    seen = {}
    for cycles in itertools.count():
        h = tuple(block_counts)
        if h in seen:
            return cycles, cycles - seen[h]
        seen[h] = cycles

        redistribute(block_counts)

block_counts = [int(x) for x in inp.split("\t")]
cycles, loop_size = count_cycles(block_counts)

answer = cycles
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?</p>
# MAGIC <p>In the example above, <code>2 4 1 2</code> is seen again after four cycles, and so the answer in that example would be <code>4</code>.</p>
# MAGIC <p><em>How many cycles</em> are in the infinite loop that arises from the configuration in your puzzle input?</p>
# MAGIC </article>

# COMMAND ----------

answer = loop_size
print(answer)
