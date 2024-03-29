// Databricks notebook source
// MAGIC %md https://adventofcode.com/2015/day/4

// COMMAND ----------

// MAGIC %md <article class="day-desc"><h2>--- Day 4: The Ideal Stocking Stuffer ---</h2><p>Santa needs help <a href="https://en.wikipedia.org/wiki/Bitcoin#Mining">mining</a> some <span title="Hey, mined your own business!">AdventCoins</span> (very similar to <a href="https://en.wikipedia.org/wiki/Bitcoin">bitcoins</a>) to use as gifts for all the economically forward-thinking little girls and boys.</p>
// MAGIC <p>To do this, he needs to find <a href="https://en.wikipedia.org/wiki/MD5">MD5</a> hashes which, in <a href="https://en.wikipedia.org/wiki/Hexadecimal">hexadecimal</a>, start with at least <em>five zeroes</em>.  The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: <code>1</code>, <code>2</code>, <code>3</code>, ...) that produces such a hash.</p>
// MAGIC <p>For example:</p>
// MAGIC <ul>
// MAGIC <li>If your secret key is <code>abcdef</code>, the answer is <code>609043</code>, because the MD5 hash of <code>abcdef609043</code> starts with five zeroes (<code>000001dbbfa...</code>), and it is the lowest such number to do so.</li>
// MAGIC <li>If your secret key is <code>pqrstuv</code>, the lowest number it combines with to make an MD5 hash starting with five zeroes is <code>1048970</code>; that is, the MD5 hash of <code>pqrstuv1048970</code> looks like <code>000006136ef...</code>.</li>
// MAGIC </ul>
// MAGIC </article>

// COMMAND ----------

val input: String = "yzbqklnj"

// COMMAND ----------

def md5(s: String): String =
  java
    .security
    .MessageDigest
    .getInstance("MD5")
    .digest(s.getBytes)
    .map("%02X".format(_))
    .mkString

def solve(prefix: String): Int =
  Stream // LazyList
    .from(1)
    .find(i => md5(input + i).startsWith(prefix))
    .get

val answer1: Int = solve("00000")
println(answer1)

// COMMAND ----------

// MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now find one that starts with <em>six zeroes</em>.</p>
// MAGIC </article>

// COMMAND ----------

val answer2: Int = solve("000000")
println(answer2)
