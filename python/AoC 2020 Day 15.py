# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/15

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 15: Rambunctious Recitation ---</h2><p>You catch the airport shuttle and try to book a new flight to your vacation island. Due to the storm, all direct flights have been cancelled, but a route is available to get around the storm. You take it.</p>
# MAGIC <p>While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're playing a <em>memory game</em> and are <span title="Of course they are.">ever so excited</span> to explain the rules!</p>
# MAGIC <p>In this game, the players take turns saying <em>numbers</em>. They begin by taking turns reading from a list of <em>starting numbers</em> (your puzzle input). Then, each turn consists of considering the <em>most recently spoken number</em>:</p>
# MAGIC <ul>
# MAGIC <li>If that was the <em>first</em> time the number has been spoken, the current player says <em><code>0</code></em>.</li>
# MAGIC <li>Otherwise, the number had been spoken before; the current player announces <em>how many turns apart</em> the number is from when it was previously spoken.</li>
# MAGIC </ul>
# MAGIC <p>So, after the starting numbers, each turn results in that player speaking aloud either <em><code>0</code></em> (if the last number is new) or an <em>age</em> (if the last number is a repeat).</p>
# MAGIC <p>For example, suppose the starting numbers are <code>0,3,6</code>:</p>
# MAGIC <ul>
# MAGIC <li><em>Turn 1</em>: The <code>1</code>st number spoken is a starting number, <em><code>0</code></em>.</li>
# MAGIC <li><em>Turn 2</em>: The <code>2</code>nd number spoken is a starting number, <em><code>3</code></em>.</li>
# MAGIC <li><em>Turn 3</em>: The <code>3</code>rd number spoken is a starting number, <em><code>6</code></em>.</li>
# MAGIC <li><em>Turn 4</em>: Now, consider the last number spoken, <code>6</code>. Since that was the first time the number had been spoken, the <code>4</code>th number spoken is <em><code>0</code></em>.</li>
# MAGIC <li><em>Turn 5</em>: Next, again consider the last number spoken, <code>0</code>. Since it <em>had</em> been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, <code>4</code>) and the turn number of the time it was most recently spoken before then (turn <code>1</code>). Thus, the <code>5</code>th number spoken is <code>4 - 1</code>, <em><code>3</code></em>.</li>
# MAGIC <li><em>Turn 6</em>: The last number spoken, <code>3</code> had also been spoken before, most recently on turns <code>5</code> and <code>2</code>. So, the <code>6</code>th number spoken is <code>5 - 2</code>, <em><code>3</code></em>.</li>
# MAGIC <li><em>Turn 7</em>: Since <code>3</code> was just spoken twice in a row, and the last two turns are <code>1</code> turn apart, the <code>7</code>th number spoken is <em><code>1</code></em>.</li>
# MAGIC <li><em>Turn 8</em>: Since <code>1</code> is new, the <code>8</code>th number spoken is <em><code>0</code></em>.</li>
# MAGIC <li><em>Turn 9</em>: <code>0</code> was last spoken on turns <code>8</code> and <code>4</code>, so the <code>9</code>th number spoken is the difference between them, <em><code>4</code></em>.</li>
# MAGIC <li><em>Turn 10</em>: <code>4</code> is new, so the <code>10</code>th number spoken is <em><code>0</code></em>.</li>
# MAGIC </ul>
# MAGIC <p>(The game ends when the Elves get sick of playing or dinner is ready, whichever comes first.)</p>
# MAGIC <p>Their question for you is: what will be the <em><code>2020</code>th</em> number spoken? In the example above, the <code>2020</code>th number spoken will be <code>436</code>.</p>
# MAGIC <p>Here are a few more examples:</p>
# MAGIC <ul>
# MAGIC <li>Given the starting numbers <code>1,3,2</code>, the <code>2020</code>th number spoken is <code>1</code>.</li>
# MAGIC <li>Given the starting numbers <code>2,1,3</code>, the <code>2020</code>th number spoken is <code>10</code>.</li>
# MAGIC <li>Given the starting numbers <code>1,2,3</code>, the <code>2020</code>th number spoken is <code>27</code>.</li>
# MAGIC <li>Given the starting numbers <code>2,3,1</code>, the <code>2020</code>th number spoken is <code>78</code>.</li>
# MAGIC <li>Given the starting numbers <code>3,2,1</code>, the <code>2020</code>th number spoken is <code>438</code>.</li>
# MAGIC <li>Given the starting numbers <code>3,1,2</code>, the <code>2020</code>th number spoken is <code>1836</code>.</li>
# MAGIC </ul>
# MAGIC <p>Given your starting numbers, <em>what will be the <code>2020</code>th number spoken?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '20,9,11,0,1,2'

# COMMAND ----------

nums = [int(num) for num in inp.split(',')]

def get_nth(n):
  seen = {num: i for i, num in enumerate(nums[:-1])}
  prev = nums[-1]
  for i in range(len(nums), n):
    value = i - 1 - seen.get(prev, i - 1)
    seen[prev] = i - 1
    prev = value
  return value

answer = get_nth(2020)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Impressed, the Elves issue you a challenge: determine the <code>30000000</code>th number spoken. For example, given the same starting numbers as above:</p>
# MAGIC <ul>
# MAGIC <li>Given <code>0,3,6</code>, the <code>30000000</code>th number spoken is <code>175594</code>.</li>
# MAGIC <li>Given <code>1,3,2</code>, the <code>30000000</code>th number spoken is <code>2578</code>.</li>
# MAGIC <li>Given <code>2,1,3</code>, the <code>30000000</code>th number spoken is <code>3544142</code>.</li>
# MAGIC <li>Given <code>1,2,3</code>, the <code>30000000</code>th number spoken is <code>261214</code>.</li>
# MAGIC <li>Given <code>2,3,1</code>, the <code>30000000</code>th number spoken is <code>6895259</code>.</li>
# MAGIC <li>Given <code>3,2,1</code>, the <code>30000000</code>th number spoken is <code>18</code>.</li>
# MAGIC <li>Given <code>3,1,2</code>, the <code>30000000</code>th number spoken is <code>362</code>.</li>
# MAGIC </ul>
# MAGIC <p>Given your starting numbers, <em>what will be the <code>30000000</code>th number spoken?</em></p>
# MAGIC </article>

# COMMAND ----------

answer = get_nth(30000000)
print(answer)
