# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 15: Dueling Generators ---</h2><p>Here, you encounter a pair of dueling <span title="I guess they *are* a little banjo-shaped. Why do you ask?">generators</span>. The generators, called <em>generator A</em> and <em>generator B</em>, are trying to agree on a sequence of numbers. However, one of them is malfunctioning, and so the sequences don't always match.</p>
# MAGIC <p>As they do this, a <em>judge</em> waits for each of them to generate its next value, compares the lowest 16 bits of both values, and keeps track of the number of times those parts of the values match.</p>
# MAGIC <p>The generators both work on the same principle. To create its next value, a generator will take the previous value it produced, multiply it by a <em>factor</em> (generator A uses <code>16807</code>; generator B uses <code>48271</code>), and then keep the remainder of dividing that resulting product by <code>2147483647</code>. That final remainder is the value it produces next.</p>
# MAGIC <p>To calculate each generator's first value, it instead uses a specific starting value as its "previous value" (as listed in your puzzle input).</p>
# MAGIC <p>For example, suppose that for starting values, generator A uses <code>65</code>, while generator B uses <code>8921</code>. Then, the first five pairs of generated values are:</p>
# MAGIC <pre><code>--Gen. A--  --Gen. B--
# MAGIC    1092455   430625591
# MAGIC 1181022009  1233683848
# MAGIC  245556042  1431495498
# MAGIC 1744312007   137874439
# MAGIC 1352636452   285222916
# MAGIC </code></pre>
# MAGIC <p>In binary, these pairs are (with generator A's value first in each pair):</p>
# MAGIC <pre><code>00000000000100001010101101100111
# MAGIC 00011001101010101101001100110111
# MAGIC 
# MAGIC 01000110011001001111011100111001
# MAGIC 01001001100010001000010110001000
# MAGIC 
# MAGIC 00001110101000101110001101001010
# MAGIC 01010101010100101110001101001010
# MAGIC 
# MAGIC 01100111111110000001011011000111
# MAGIC 00001000001101111100110000000111
# MAGIC 
# MAGIC 01010000100111111001100000100100
# MAGIC 00010001000000000010100000000100
# MAGIC </code></pre>
# MAGIC <p>Here, you can see that the lowest (here, rightmost) 16 bits of the third value match: <code>1110001101001010</code>. Because of this one match, after processing these five pairs, the judge would have added only <code>1</code> to its total.</p>
# MAGIC <p>To get a significant sample, the judge would like to consider <em>40 million</em> pairs. (In the example above, the judge would eventually find a total of <code>588</code> pairs that match in their lowest 16 bits.)</p>
# MAGIC <p>After 40 million pairs, <em>what is the judge's final count</em>?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Generator A starts with 116
Generator B starts with 299
"

# COMMAND ----------

s <- str_extract_all(input, "\\d+") %>% first() %>% parse_number()
a_start <- s[1]
b_start <- s[2]
lst(a_start, b_start)

# COMMAND ----------

a_factor <- 16807
b_factor <- 48271
denominator <- 2147483647
mod <- 2^16

# COMMAND ----------

a <- a_start
b <- b_start
match_count <- 0
for (i in seq_len(40000000)) {
  a <- (a_factor * a) %% denominator
  b <- (b_factor * b) %% denominator
  match_count <- match_count + ((a %% mod) == (b %% mod))
}

answer <- match_count
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>In the interest of trying to align a little better, the generators get more picky about the numbers they actually give to the judge.</p>
# MAGIC <p>They still generate values in the same way, but now they only hand a value to the judge when it meets their <em>criteria</em>:</p>
# MAGIC <ul>
# MAGIC <li>Generator A looks for values that are multiples of <code><em>4</em></code>.</li>
# MAGIC <li>Generator B looks for values that are multiples of <code><em>8</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>Each generator functions completely <em>independently</em>: they both go through values entirely on their own, only occasionally handing an acceptable value to the judge, and otherwise working through the same sequence of values as before until they find one.</p>
# MAGIC <p>The judge still waits for each generator to provide it with a value before comparing them (using the same comparison method as before). It keeps track of the order it receives values; the first values from each generator are compared, then the second values from each generator, then the third values, and so on.</p>
# MAGIC <p>Using the example starting values given above, the generators now produce the following first five values each:</p>
# MAGIC <pre><code>--Gen. A--  --Gen. B--
# MAGIC 1352636452  1233683848
# MAGIC 1992081072   862516352
# MAGIC  530830436  1159784568
# MAGIC 1980017072  1616057672
# MAGIC  740335192   412269392
# MAGIC </code></pre>
# MAGIC <p>These values have the following corresponding binary values:</p>
# MAGIC <pre><code>01010000100111111001100000100100
# MAGIC 01001001100010001000010110001000
# MAGIC 
# MAGIC 01110110101111001011111010110000
# MAGIC 00110011011010001111010010000000
# MAGIC 
# MAGIC 00011111101000111101010001100100
# MAGIC 01000101001000001110100001111000
# MAGIC 
# MAGIC 01110110000001001010100110110000
# MAGIC 01100000010100110001010101001000
# MAGIC 
# MAGIC 00101100001000001001111001011000
# MAGIC 00011000100100101011101101010000
# MAGIC </code></pre>
# MAGIC <p>Unfortunately, even though this change makes more bits similar on average, none of these values' lowest 16 bits match. Now, it's not until the 1056th pair that the judge finds the first match:</p>
# MAGIC <pre><code>--Gen. A--  --Gen. B--
# MAGIC 1023762912   896885216
# MAGIC 
# MAGIC 00111101000001010110000111100000
# MAGIC 00110101011101010110000111100000
# MAGIC </code></pre>
# MAGIC <p>This change makes the generators much slower, and the judge is getting impatient; it is now only willing to consider <em>5 million</em> pairs. (Using the values from the example above, after five million pairs, the judge would eventually find a total of <code>309</code> pairs that match in their lowest 16 bits.)</p>
# MAGIC <p>After 5 million pairs, but using this new generator logic, <em>what is the judge's final count</em>?</p>
# MAGIC </article>

# COMMAND ----------

a <- a_start
b <- b_start
match_count <- 0
for (i in seq_len(5000000)) {
  repeat {
    a <- (a_factor * a) %% denominator
    if (a %% 4 == 0) break
  }
  repeat {
    b <- (b_factor * b) %% denominator
    if (b %% 8 == 0) break
  }
  
  match_count <- match_count + ((a %% mod) == (b %% mod))
}

answer <- match_count
answer
