# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/4

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 4: Secure Container ---</h2><p>You arrive at the Venus fuel depot only to discover it's protected by a password.  The Elves had written the password on a sticky note, but someone <span title="Look on the bright side - isn't it more secure if nobody knows the password?">threw it out</span>.</p>
# MAGIC <p>However, they do remember a few key facts about the password:</p>
# MAGIC <ul>
# MAGIC <li>It is a six-digit number.</li>
# MAGIC <li>The value is within the range given in your puzzle input.</li>
# MAGIC <li>Two adjacent digits are the same (like <code>22</code> in <code>1<em>22</em>345</code>).</li>
# MAGIC <li>Going from left to right, the digits <em>never decrease</em>; they only ever increase or stay the same (like <code>111123</code> or <code>135679</code>).</li>
# MAGIC </ul>
# MAGIC <p>Other than the range rule, the following are true:</p>
# MAGIC <ul>
# MAGIC <li><code>111111</code> meets these criteria (double <code>11</code>, never decreases).</li>
# MAGIC <li><code>2234<em>50</em></code> does not meet these criteria (decreasing pair of digits <code>50</code>).</li>
# MAGIC <li><code>123789</code> does not meet these criteria (no double).</li>
# MAGIC </ul>
# MAGIC <p><em>How many different passwords</em> within the range given in your puzzle input meet these criteria?</p>
# MAGIC </article>

# COMMAND ----------

inp = '130254-678275'

# COMMAND ----------

import re

def satisfies_criteria(candidate):
  contains_double = re.search(r'(.)\1', candidate)
  is_non_decreasing = all(a <= b for a, b in zip(candidate, candidate[1:]))
  return bool(contains_double and is_non_decreasing)

range_min, range_max = (int(x) for x in inp.split('-'))

answer = sum(satisfies_criteria(str(candidate)) for candidate in range(range_min, range_max+1))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>An Elf just remembered one more important detail: the two adjacent matching digits <em>are not part of a larger group of matching digits</em>.</p>
# MAGIC <p>Given this additional criterion, but still ignoring the range rule, the following are now true:</p>
# MAGIC <ul>
# MAGIC <li><code>112233</code> meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.</li>
# MAGIC <li><code>123<em>444</em></code> no longer meets the criteria (the repeated <code>44</code> is part of a larger group of <code>444</code>).</li>
# MAGIC <li><code>111122</code> meets the criteria (even though <code>1</code> is repeated more than twice, it still contains a double <code>22</code>).</li>
# MAGIC </ul>
# MAGIC <p><em>How many different passwords</em> within the range given in your puzzle input meet all of the criteria?</p>
# MAGIC </article>

# COMMAND ----------

answer = sum(satisfies_criteria(re.sub(r'(.)\1\1+', r'\1', str(candidate))) for candidate in range(range_min, range_max+1))
print(answer)
