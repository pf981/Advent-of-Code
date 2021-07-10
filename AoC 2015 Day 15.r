# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 15: Science for Hungry People ---</h2><p>Today, you set out on the task of perfecting your milk-dunking cookie recipe.  All you have to do is find the right balance of ingredients.</p>
# MAGIC <p>Your recipe leaves room for exactly <code>100</code> teaspoons of ingredients.  You make a list of the <em>remaining ingredients you could use to finish the recipe</em> (your puzzle input) and their <em>properties per teaspoon</em>:</p>
# MAGIC <ul>
# MAGIC <li><code>capacity</code> (how well it helps the cookie absorb milk)</li>
# MAGIC <li><code>durability</code> (how well it keeps the cookie intact when full of milk)</li>
# MAGIC <li><code>flavor</code> (how tasty it makes the cookie)</li>
# MAGIC <li><code>texture</code> (how it improves the feel of the cookie)</li>
# MAGIC <li><code>calories</code> (how many calories it adds to the cookie)</li>
# MAGIC </ul>
# MAGIC <p>You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future.  The <em>total score</em> of a cookie can be found by adding up each of the properties (negative totals become <code>0</code>) and then multiplying together everything except calories.</p>
# MAGIC <p>For instance, suppose you have <span title="* I know what your preference is, but...">these two ingredients</span>:</p>
# MAGIC <pre><code>Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# MAGIC Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# MAGIC </code></pre>
# MAGIC <p>Then, choosing to use <code>44</code> teaspoons of butterscotch and <code>56</code> teaspoons of cinnamon (because the amounts of each ingredient must add up to <code>100</code>) would result in a cookie with the following properties:</p>
# MAGIC <ul>
# MAGIC <li>A <code>capacity</code> of <code>44*-1 + 56*2 = 68</code></li>
# MAGIC <li>A <code>durability</code> of <code>44*-2 + 56*3 = 80</code></li>
# MAGIC <li>A <code>flavor</code> of <code>44*6 + 56*-2 = 152</code></li>
# MAGIC <li>A <code>texture</code> of <code>44*3 + 56*-1 = 76</code></li>
# MAGIC </ul>
# MAGIC <p>Multiplying these together (<code>68 * 80 * 152 * 76</code>, ignoring <code>calories</code> for now) results in a total score of  <code>62842880</code>, which happens to be the best score possible given these ingredients.  If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.</p>
# MAGIC <p>Given the ingredients in your kitchen and their properties, what is the <em>total score</em> of the highest-scoring cookie you can make?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8
"

# COMMAND ----------

Rcpp::cppFunction("
int solve() {
  int best_score = 0;
  for (int a = 0; a < 100; ++a) {
    for (int b = 0; b < 100; ++b) {
      for (int c = 0; c < 100; ++c) {
        for (int d = 0; d < 100; ++d) {
          if (a + b + c + d == 100) {
            best_score = std::max(
              std::max(a*2 + b*0 +c*0 + d*0, 0) * std::max(a*0 + b*5 + c*0 + d*-1, 0) * std::max(a*-2 + b*-3 + c*5 + d*0, 0) * std::max(a*0 + b*0 + c*-1 + d*5, 0),
              best_score
            );
          }
        }
      }
    }
  }

  return best_score;
} 
")

# COMMAND ----------

answer <- solve()
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Your cookie recipe becomes wildly popular!  Someone asks if you can make another recipe that has exactly <code>500</code> calories per cookie (so they can use it as a meal replacement).  Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).</p>
# MAGIC <p>For example, given the ingredients above, if you had instead selected <code>40</code> teaspoons of butterscotch and <code>60</code> teaspoons of cinnamon (which still adds to <code>100</code>), the total calorie count would be <code>40*8 + 60*3 = 500</code>.  The total score would go down, though: only <code>57600000</code>, the best you can do in such trying circumstances.</p>
# MAGIC <p>Given the ingredients in your kitchen and their properties, what is the <em>total score</em> of the highest-scoring cookie you can make with a calorie total of <code>500</code>?</p>
# MAGIC </article>

# COMMAND ----------

Rcpp::cppFunction("
int solve() {
  int best_score = 0;
  for (int a = 0; a < 100; ++a) {
    for (int b = 0; b < 100; ++b) {
      for (int c = 0; c < 100; ++c) {
        for (int d = 0; d < 100; ++d) {
          if (a + b + c + d == 100 && a*3 + b*3 + c*8 + d*8 == 500) {
            best_score = std::max(
              std::max(a*2 + b*0 +c*0 + d*0, 0) * std::max(a*0 + b*5 + c*0 + d*-1, 0) * std::max(a*-2 + b*-3 + c*5 + d*0, 0) * std::max(a*0 + b*0 + c*-1 + d*5, 0),
              best_score
            );
          }
        }
      }
    }
  }

  return best_score;
} 
")

# COMMAND ----------

answer <- solve()
answer
