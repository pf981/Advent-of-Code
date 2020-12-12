# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/8
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 8: Space Image Format ---</h2><p><span title="I'm not sorry.">The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars.</span> You land your ship near the rover.</p>
# MAGIC <p>When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a <a href="https://en.wikipedia.org/wiki/BIOS">BIOS</a> password. The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.</p>
# MAGIC <p>Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format.  None of the Elves seem to remember why this is the case. They send you the instructions to decode it.</p>
# MAGIC <p>Images are sent as a series of digits that each represent the color of a single pixel.  The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.</p>
# MAGIC <p>Each image actually consists of a series of identically-sized <em>layers</em> that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.</p>
# MAGIC <p>For example, given an image <code>3</code> pixels wide and <code>2</code> pixels tall, the image data <code>123456789012</code> corresponds to the following image layers:</p>
# MAGIC <pre><code>Layer 1: 123
# MAGIC          456
# MAGIC 
# MAGIC Layer 2: 789
# MAGIC          012
# MAGIC </code></pre>
# MAGIC <p>The image you received is <em><code>25</code> pixels wide and <code>6</code> pixels tall</em>.</p>
# MAGIC <p>To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the <em>fewest <code>0</code> digits</em>.  On that layer, what is <em>the number of <code>1</code> digits multiplied by the number of <code>2</code> digits?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>1548</code>.</p><p class="day-success">The first half of this puzzle is complete! It provides one gold star: *</p>
# MAGIC <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: <code>0</code> is black, <code>1</code> is white, and <code>2</code> is transparent.</p>
# MAGIC <p>The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a <em>black</em> pixel at that position.</p>
# MAGIC <p>For example, given an image <code>2</code> pixels wide and <code>2</code> pixels tall, the image data <code>0222112222120000</code> corresponds to the following image layers:</p>
# MAGIC <pre><code>Layer 1: <em>0</em>2
# MAGIC          22
# MAGIC 
# MAGIC Layer 2: 1<em>1</em>
# MAGIC          22
# MAGIC 
# MAGIC Layer 3: 22
# MAGIC          <em>1</em>2
# MAGIC 
# MAGIC Layer 4: 00
# MAGIC          0<em>0</em>
# MAGIC </code></pre>
# MAGIC <p>Then, the full image can be found by determining the top visible pixel in each position:</p>
# MAGIC <ul>
# MAGIC <li>The top-left pixel is <em>black</em> because the top layer is <code>0</code>.</li>
# MAGIC <li>The top-right pixel is <em>white</em> because the top layer is <code>2</code> (transparent), but the second layer is <code>1</code>.</li>
# MAGIC <li>The bottom-left pixel is <em>white</em> because the top two layers are <code>2</code>, but the third layer is <code>1</code>.</li>
# MAGIC <li>The bottom-right pixel is <em>black</em> because the only visible pixel in that position is <code>0</code> (from layer 4).</li>
# MAGIC </ul>
# MAGIC <p>So, the final image looks like this:</p>
# MAGIC <pre><code>01
# MAGIC 10
# MAGIC </code></pre>
# MAGIC <p><em>What message is produced after decoding your image?</em></p>
# MAGIC </article>
# MAGIC <form method="post" action="8/answer"><input type="hidden" name="level" value="2"><p>Answer: <input type="text" name="answer" autocomplete="off"> <input type="submit" value="[Submit]"></p></form>
# MAGIC <p>Although it hasn't changed, you can still <a href="8/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Space+Image+Format%22+%2D+Day+8+%2D+Advent+of+Code+2019&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2019%2Fday%2F8&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+Part+One+of+%22Space+Image+Format%22+%2D+Day+8+%2D+Advent+of+Code+2019+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2019%2Fday%2F8'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "222222222222222120222222220212222222022222222222222222221222212222022222012202022022212222122202222222222200022220222222202202122212222122122222222222212222222222222121222220222202222222222222222222222222221222212222122222002212022022202222122222212222222201122221222222212202222222222022022222222222212222222222222220222221222202222222222222222222222222220222212222222222212202022022212222122202212222222200022220222222212222022212222022222222222222222222222222222220222221221202222222222222222222222222220222212222222222022212122122212222222222202222222222022220222222202202222222222022122222222222212222222222222021222221222202222222222222222222222222222222222222122222102212122022202222122202212222222200222222222222202202222212222222122222222222212222222222222022222222220212222222222222222222222222211202212202121222022210222122222222022222222222222211222220222222222202122202222022222222222222222222222222222022222220221202222222122222222222222222222222222222120222122212122022202222222212202222222211122221222222202212122202220122022222222222222222222222222220222222222212222222122222222222222222001212212212022222122220222222202222222222212222222220222221222222202212222212220222122222222222202222222222222120222220222212222222122222222222222222121212222202221222112220222122212222022202212222222201122220222222212202122222220222122222222222212222222222222021222220221222222222222222222222222222120202222202122222222210122222202222022202222222222222022221222222222202122202222022122222222222212222222222222021222220222222222222022222222222222222112222202222022222012201122222222222122212202220222220222222222222222222022212222022122222222222202222222222222222222220022202222222122222222222222222121222212222220222122221222022212222122212202221222100022221222222202202222222222022222222222222222222222222222221222222022212220222122222222222202222102212202202222222112221122222222222222202202221222022022221222220202222122212220222222222222222212222222222222122222222222212221222022222222222222222212202212202022222112210122222212222222222202221222112122220222220222202122202220120122222222222012222222222222120222222220222221222222222222222202222111222202222120222002200222022202222222222212222222000222221222220222212122212221121022222222222102222222222222021222222222222220222122222222222202222112222202212021222002202022022212222222222212210222012022221222222202222112202222022222222222222222222222222222021222220021222221222022222222222212222221222222202121222112210122122012222222222202212222120222221222222222222002212222220222222222222102222122222222021222221020222221222122222222222212222210212212222021222022212222122202222222212212220222011222221222222212202012202221120122222222222202222022222222022222222121222222222022222222222202222212212222202220222202200222222122222122212222221222001122221222221202212122202221121122222222222102222122222222121222221020212220222020222222220222222122222202202220222012210122122022222022222222202222202222220222221202202212212222120222222222222012222022222222221222120221202221222021222222220202222102222222212022222122202222122122222022212222222222020022221222221222202222202221120202222222222122222122222222121222022020202220222221222222220222222210222202222121222002210022122112222122212212212222000222222222221222202002222222121102222222222102222122222222122222122222212221222021222222220222222101212202202221222012211022122002222022222202221222120222222222222202212002202222122022222222222022222022222222120222122221212221222120220222221202222222222202212022222112211022022002222222202202201222022122222222220222202002202220222202222222222002222122222222022222220021222221222121221222222212222212202212222221222002220022022212222222212212220222112122221222222212202222202222220122222222222122222022222222220222120021202222222020222222220222222210222202202120222222212122122022222022202222200222110222222222222202202012202221121112222222222222222222222222020222120020212222222221222222222222222200212212222120222222211222122002222022222222211222212122221222221202212222202220021022222222222102222122222222122222121120212221222220222222202212222011212212202221222202210122122212222022202202221222121122222222221212222122212222222112222222222011222222222022221222222122212220222020221222210202222101212202012120222012202122022202222122202202210222120222222222220202222202222221120012222222222012222022222022120222122122202221222122212222212202222200202222222021222202211122022222222222202202210222101022222222222222202022222220221012222222222012222022222120022222120222222222222022202222201202222202202222212121222122210022122012222122222202211222021222221022221222222102222221220112222222222020222222222121121222220022212222222122220222200212222212222202002221012010200022222122222022222222201222010222220022222222222102222221122022222222222121222122222120020222022020202221222021201222221221222101202212102022020100212022122122222022222222222222011122221022222202222022222220222122222222222110222022222021222222220022222221222220220222212210222202222212112220010100221222022022222022222212202222112022221222222202222202212220120122222212022102222022222220221222220222222221222021212222210212222012202212102222100120212222022112222022222212200222121022220022220212202102202220122202222202222222222222222020221222221120222221222221202222222220222012202212012121020012202122122012222122212202221222201222221022220202222102202221021012222202122211222122222121120222121121212221222121212222222200222202202202122020110222201222022012122022202202221222020122220022221212212002222221222202222202122201222122222121120222122221222220222020211222200211222012212212202021112220201222022112022222222222210222222022220122220212222122202220222112222222022020222222222021021222222121212220222220212222212201222122212222122220102022221122022222122122212202210222110122222122220222222012202221021012222202222212222122222121022222120222212221222020210222210202222001212212012000200101201222122122222122222222212222101222222122210212222222202222121012222222222121222222212121122222020122212220222222210222220200222221222202102222211001202122022012122022202222200222121222220222202202202002222221221222222202222020222222212022222222020021202221222222212222222201222222212212002010111002221222222112222222202212202222111222222222201212202002212222022202222222222112222222202120021222120220202220222122202222222221222202212202112222021110220022122122122122222222202222221022221122212222212012202220021122222212222021222222212120121222222221222222222220201222211200222102212222102121010100212222022112122222202202200222011222220022211202222022202222222202222222122001222222222022222222021221222220222021211222212200222100212212022101221020212222122022022222212222202222211222220022202222202212202221221002222202122220222022212222120222022122202220222020212222221220222020212212202112101020200022222102222122202202210022112022220022200202222022212220221212222202222001222122202122120222021121202220202222202222202220222211222212202120120211201222022202122222212202201022112022221122221202222212212222222102222202222211222022220122220222022021202221212222222222222210222122222222022122001211222122022012122122202202212122200002220022211212222012212221020212222222222121222222200220020222120120202220202120210222222222222101222202002101200022222222222012122022222222211122201202221222210212202212202221120020222222122012222222220022122222120222202220202222201222220221222220222212212110000110200022122212022122212202220122021202221022221222222022202220020200222202222221222022212222021222220222212221212221201222200222222210202212112212022200210222022002022022212222200022222212220222222202222202202221221002220012122102222122211120200222020221202220222222220222211222222002212202102112112102202222222002022022222222202022201202221222201222212102222221220002220112022022222022201120002222122220222222222022012222211202222220222212202202102110201222022102022022112222201022211222221122200212202022222222121222221222122020222222222122102222022121222220222120002222202220222112202222022110012121202122122202122222112212211022201122220122222200212112222212022201221102222212222122212221222222021120222222222221201222222220202220202212122122200120211122222122222222112212221022020122220122200200222002222202220020220112122001222222220022211222122020002220202020121222212221202112202212222022001100220122122122222022222212222222021122221122220221202112212201022012222102222010222222210120012222122122212221212121102222211202212100202212112101202221221122222202122122012212211022002202222222200202202212202222222020222022222022222222221121121222020021012222212122221222222211202200212202002112010202200122222012022222202202200022122212221222212111222122202212020211222022022122222122222122012222121121202221222020011222202211212200212202022220112020210122022122122122202202222222020022221122200220212222212202122021212022022021222122210120222222222122112220202020112222221202202202222202102120212121212022222222122022102202220022220122220222222122222102222212220102220102022222222222210222202222020121102220222222000222222201212210222222202012012011201122122222022222102212211222002022221022211210212202222201222200200002012011222222202121121222020221002222212121220222222200222110222202002101021122221022222102222222222202201222020222222222200210212122212220120010200112222022222022201020121222022221002222202022120222201201222010212222002220112100211022122112022122002222201222112102221022202202212202212212220211200102212011222122211122221222122021122220202121221222201222212021222202202022201202210122222212022022112212222222100122221222222002212022222200121022202222112121222022211222121222222020022222202020222222201221202010202222012210001020222122022012022022022202220022100112222022200221212022022211102220202212102010222222222122200222221022112222212022122222200200222101222212002211210000211222222202022122022112201122110212222022211201202112222210201202202022212022222022212021221222021121102220212122212222210211222212222202222210201112211102122012222222002212220022021112221022210100222112212220001111211102112212222222211020100222220220002222212222101222210221202022212212112212000022212102022002022022202202211122100002222020201211212022202212222110200022012210221022221021120222120220212120222122102222222220202102222212012101121120202002022122222222222002021022010112221120212122202012122211002010212012112121220212221020020222120022122122202022000222200201202202212202122201222221211022222102122122012222011022012102220021221022212112102200222210202122202212221012222211022222020120202021222221112222210221202222212212012012121211202202222122022122102222020022220122221220211122222012022202021012201012012122221022220102101220012021002121212021222222210212212102212212002012111101212202222122122122212202211122221002222020200121212112222220000122211012222222220022201121001220201220202120202021002222220220212120122202222201202020210002122222122122222012221222110212221020210100222012002211020222221222122001221102222100021222002220222122222222100222201212202002202222112110211200220222122012222222002112122122021112222021210022222122112210200211210012202021221011210111210222112020202022202120100222211212222222212222102200020111211102122112122022222022101022001002222222202221222022222210120112211002212210222100200101222222212222012220222121002222210200202022112202212212011120200022022112020122022002121122100202220121221110222202022220201212210102212200220121212112100222110221012222222121001222221221202122202202012200122011222022222002220122212012110222220221222021012000222222122222101211122222112210222202200021001221210020002121212022102222222211212212212212122000122200222112122122220122202012221222002020220120102121212212102220021122022222022010222211200000111221000120012120212222110222221221200110222222122120022102221002222022222222002002010122210202222120001101212122102200210222022212002010222222220111122222002120112020212222200220200200222101012212022110221202210122222222221122212212211022010122222220202012202002202201102222110222012121222220211120212222211021012122202020121221212202201120020212012210201002110112022122120022222212200222012120220222000102222202012211211112201010112012221002210022012221022120122020202020122220202210211111001202102012100200110002022002021022212202210022200221222120000112202022002212002121010120202111221102212000200222021222112121222222221222201201201121201212002001221122201012122112222022222212122122121012222122011110202022012212201001210100202022222221210221020222110121012121222120100220202221201112011222012012021210220122222022021122212002200122202122222120001000212122202220110201100022012222222201211222110222110021212120202121220222222211211220021212202010010010011102022002220222012112020122101212221121201111202112222201201222101000022111220101211110202221021120102021202022021222210202220120212222112120202111000022022202220222102122100122011122220122202100222012002211012222222002012222221012201201212222221122222122212022010020222211212011102212002200100211002112022212120122122222202022110212221022120221222002212212121102002001122022221122221110201220120220102022202122122021210220222202112222212101211112000002022022020122022112112220012212221221101200202202102201012222211102102022221100201101200222211120222021212022010022212210200111120212212121011000101122022102121122022102100222221110221120021220222122222201011202110011112220222212200002002221122022222021202121122121210212220212000212122010221210120202022222021022222012000120212220222021120122220202202221210221101221012222020201200002010201201222012120212021000221221221222201010222012111200202221012122112220222022012220122112122222021001102220012012212221110000020012010120002210212011222100122022120202121221222201201202202002222222222211110201202122212121022012011122222121000220122000102200022022210001122212221202201220101201002121200210022022221202120202121212212212010110202022222120211211122022012122122112212010222010220220220102100220202112222120100011200202110120221200210011200202022022022222222001222200210222110110222212020122002000222222212020122202122112121011000222021101202221222212222110100221120102010220020202111100222212022012022222220211222202222210002010222002201222110102022022112220020002001121222200211222220101100201102222222011201001221002220120220212112110211101022002120222021200122211202222021222212002011201011212021222112021022211202100120210200221022200212211102102212211122202021002020221001222022212220210021002220202022012211222221220001120202212201202210000201222212022222021202112120012212220120000110210012102211111200100010012010221222222121220202110222102120212120011102200202202202222112212201100201022201222102022220121020202021211001222120122102201102202212000202021101112202020200222221122202210122002022212112102202220212222121200002202202001211222012122012120221112121222022211210221121212200110122102220202111010220010201001201001100010120201012120201021020111021100120000200112010211101122001102102200110200200000121122212011022011112021022122210001101000112120101202"
width <- 25
height <- 6

# COMMAND ----------

# input <- "123456789012"
# width <- 3
# height <- 2

# COMMAND ----------

even_split <- function(x, n) {
  starts <- seq(from = 1, to = nchar(x), by = n)
  str_sub(x, starts, starts + n - 1)
}

# COMMAND ----------

input %>%
  even_split(width * height) %>%
  as_tibble() %>%
  mutate(
    n_0 = str_count(value, "0"),
    n_1 = str_count(value, "1"),
    n_2 = str_count(value, "2")
  ) %>%
  arrange(n_0) %>%
  head(1) %>%
  summarise(result = n_1 * n_2) %>%
  pull(result)

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# input <- "0222112222120000"
# width <- 2
# height <- 2

# COMMAND ----------

result <-
  input %>%
  even_split(width * height) %>%
  str_split("") %>%
  map(function(x) {
    modify_if(x, ~. == "2", ~NA)
  }) %>%
  reduce(coalesce) %>%
  str_c(collapse = "")

# COMMAND ----------

result %>% even_split(width) %>% str_c(collapse = "\n") %>% cat()

# COMMAND ----------

result %>%
  even_split(width) %>%
  str_c(collapse = "\n") %>%
  str_replace_all("1", "#") %>%
  str_replace_all("0", " ") %>%
  cat()
#> CEKUA