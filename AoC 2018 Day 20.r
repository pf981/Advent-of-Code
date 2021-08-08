# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 20: A Regular Map ---</h2><p>While you were learning about instruction pointers, the Elves made considerable progress. When you look up, you discover that the North Pole base construction project has completely surrounded you.</p>
# MAGIC <p>The area you are in is made up entirely of <em>rooms</em> and <em>doors</em>. The rooms are arranged in a grid, and rooms only connect to adjacent rooms when a door is present between them.</p>
# MAGIC <p>For example, drawing rooms as <code>.</code>, walls as <code>#</code>, doors as <code>|</code> or <code>-</code>, your current position as <code>X</code>, and where north is up, the area you're in might look like this:</p>
# MAGIC <pre><code>#####
# MAGIC #.|.#
# MAGIC #-###
# MAGIC #.|X#
# MAGIC #####
# MAGIC </code></pre>
# MAGIC <p>You get the attention of a passing construction Elf and ask for a map. "I don't have time to draw out a map of this place - it's <em>huge</em>. Instead, I can give you directions to <em>every room in the facility</em>!" He writes down some directions on a piece of parchment and runs off. In the example above, the instructions might have been <code>^WNE$</code>, a <a href="https://en.wikipedia.org/wiki/Regular_expression">regular expression</a> or "<em>regex</em>" (your puzzle input).</p>
# MAGIC <p>The regex matches routes (like <code>WNE</code> for "west, north, east") that will take you from your current room through various doors in the facility. In aggregate, the routes will take you through <em>every door in the facility at least once</em>; mapping out all of these routes will let you build a proper map and find your way around.</p>
# MAGIC <p><code>^</code> and <code>$</code> are at the beginning and end of your regex; these just mean that the regex doesn't match anything outside the routes it describes. (Specifically, <code>^</code> matches the start of the route, and <code>$</code> matches the end of it.) These characters will not appear elsewhere in the regex.</p>
# MAGIC <p>The rest of the regex matches various sequences of the characters <code>N</code> (north), <code>S</code> (south), <code>E</code> (east), and <code>W</code> (west). In the example above, <code>^WNE$</code> matches only one route, <code>WNE</code>, which means you can move <em>west, then north, then east</em> from your current position. Sequences of letters like this always match that exact route in the same order.</p>
# MAGIC <p>Sometimes, the route can <em>branch</em>. A branch is given by a <em>list of options</em> separated by pipes (<code>|</code>) and wrapped in parentheses. So, <code>^N(E|W)N$</code> contains a branch: after going north, you must choose to go <em>either east or west</em> before finishing your route by going north again. By tracing out the possible routes after branching, you can determine where the doors are and, therefore, where the rooms are in the facility.</p>
# MAGIC <p>For example, consider this regex: <code>^ENWWW(NEEE|SSE(EE|N))$</code></p>
# MAGIC <p>This regex begins with <code>ENWWW</code>, which means that from your current position, all routes must begin by moving east, north, and then west three times, in that order. After this, there is a branch.  Before you consider the branch, this is what you know about the map so far, with doors you aren't sure about marked with a <code>?</code>:</p>
# MAGIC <pre><code>#?#?#?#?#
# MAGIC ?.|.|.|.?
# MAGIC #?#?#?#-#
# MAGIC     ?X|.?
# MAGIC     #?#?#
# MAGIC </code></pre>
# MAGIC <p>After this point, there is <code>(NEEE|SSE(EE|N))</code>. This gives you exactly two options: <code>NEEE</code> and <code>SSE(EE|N)</code>. By following <code>NEEE</code>, the map now looks like this:</p>
# MAGIC <pre><code>#?#?#?#?#
# MAGIC ?.|.|.|.?
# MAGIC #-#?#?#?#
# MAGIC ?.|.|.|.?
# MAGIC #?#?#?#-#
# MAGIC     ?X|.?
# MAGIC     #?#?#
# MAGIC </code></pre>
# MAGIC <p>Now, only <code>SSE(EE|N)</code> remains. Because it is in the same parenthesized group as <code>NEEE</code>, it starts from the same room <code>NEEE</code> started in. It states that starting from that point, there exist doors which will allow you to move south twice, then east; this ends up at another branch. After that, you can either move east twice or north once. This information fills in the rest of the doors:</p>
# MAGIC <pre><code>#?#?#?#?#
# MAGIC ?.|.|.|.?
# MAGIC #-#?#?#?#
# MAGIC ?.|.|.|.?
# MAGIC #-#?#?#-#
# MAGIC ?.?.?X|.?
# MAGIC #-#-#?#?#
# MAGIC ?.|.|.|.?
# MAGIC #?#?#?#?#
# MAGIC </code></pre>
# MAGIC <p>Once you've followed all possible routes, you know the remaining unknown parts are all walls, producing a finished map of the facility:</p>
# MAGIC <pre><code>#########
# MAGIC #.|.|.|.#
# MAGIC #-#######
# MAGIC #.|.|.|.#
# MAGIC #-#####-#
# MAGIC #.#.#X|.#
# MAGIC #-#-#####
# MAGIC #.|.|.|.#
# MAGIC #########
# MAGIC </code></pre>
# MAGIC <p>Sometimes, a list of options can have an <em>empty option</em>, like <code>(NEWS|WNSE|)</code>. This means that routes at this point could effectively skip the options in parentheses and move on immediately.  For example, consider this regex and the corresponding map:</p>
# MAGIC <pre><code>^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$
# MAGIC 
# MAGIC ###########
# MAGIC #.|.#.|.#.#
# MAGIC #-###-#-#-#
# MAGIC #.|.|.#.#.#
# MAGIC #-#####-#-#
# MAGIC #.#.#X|.#.#
# MAGIC #-#-#####-#
# MAGIC #.#.|.|.|.#
# MAGIC #-###-###-#
# MAGIC #.|.|.#.|.#
# MAGIC ###########
# MAGIC </code></pre>
# MAGIC <p>This regex has one main route which, at three locations, can optionally include additional detours and be valid: <code>(NEWS|)</code>, <code>(WNSE|)</code>, and <code>(SWEN|)</code>. Regardless of which option is taken, the route continues from the position it is left at after taking those steps. So, for example, this regex matches all of the following routes (and more that aren't listed here):</p>
# MAGIC <ul>
# MAGIC <li><code>ENNWSWWSSSEENEENNN</code></li>
# MAGIC <li><code>ENNWSWW<em>NEWS</em>SSSEENEENNN</code></li>
# MAGIC <li><code>ENNWSWW<em>NEWS</em>SSSEENEE<em>SWEN</em>NNN</code></li>
# MAGIC <li><code>ENNWSWWSSSEEN<em>WNSE</em>EENNN</code></li>
# MAGIC </ul>
# MAGIC <p>By following the various routes the regex matches, a full map of all of the doors and rooms in the facility can be assembled.</p>
# MAGIC <p>To get a sense for the size of this facility, you'd like to determine which room is <em>furthest</em> from you: specifically, you would like to find the room for which the <em>shortest path to that room would require passing through the most doors</em>.</p>
# MAGIC <ul>
# MAGIC <li>In the first example (<code>^WNE$</code>), this would be the north-east corner <code><em>3</em></code> doors away.</li>
# MAGIC <li>In the second example (<code>^ENWWW(NEEE|SSE(EE|N))$</code>), this would be the south-east corner <code><em>10</em></code> doors away.</li>
# MAGIC <li>In the third example (<code>^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$</code>), this would be the north-east corner <code><em>18</em></code> doors away.</li>
# MAGIC </ul>
# MAGIC <p>Here are a few more examples:</p>
# MAGIC <pre><code>Regex: ^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$
# MAGIC Furthest room requires passing 23 doors
# MAGIC 
# MAGIC #############
# MAGIC #.|.|.|.|.|.#
# MAGIC #-#####-###-#
# MAGIC #.#.|.#.#.#.#
# MAGIC #-#-###-#-#-#
# MAGIC #.#.#.|.#.|.#
# MAGIC #-#-#-#####-#
# MAGIC #.#.#.#X|.#.#
# MAGIC #-#-#-###-#-#
# MAGIC #.|.#.|.#.#.#
# MAGIC ###-#-###-#-#
# MAGIC #.|.#.|.|.#.#
# MAGIC #############
# MAGIC </code></pre>
# MAGIC <pre><code>Regex: ^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$
# MAGIC Furthest room requires passing 31 doors
# MAGIC 
# MAGIC ###############
# MAGIC #.|.|.|.#.|.|.#
# MAGIC #-###-###-#-#-#
# MAGIC #.|.#.|.|.#.#.#
# MAGIC #-#########-#-#
# MAGIC #.#.|.|.|.|.#.#
# MAGIC #-#-#########-#
# MAGIC #.#.#.|X#.|.#.#
# MAGIC ###-#-###-#-#-#
# MAGIC #.|.#.#.|.#.|.#
# MAGIC #-###-#####-###
# MAGIC #.|.#.|.|.#.#.#
# MAGIC #-#-#####-#-#-#
# MAGIC #.#.|.|.|.#.|.#
# MAGIC ###############
# MAGIC </code></pre>
# MAGIC <p><em>What is the largest number of doors you would be required to pass through to reach a room?</em> That is, find the room for which the shortest path from your starting location to that room would require passing through the most doors; what is the fewest doors you can pass through to reach it?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "^SEESSWNWSSEESWWSEESSWSWNN(E|WNWNENWNNWNNWNWWNNEES(W|EES(W|SE(NNNNWNNENEEENWWNWNWSWSWSSSWS(WWSSSSESE(SSE(NN|ESSSWWNWWNWSWNNWNNWWWSWNWSSESSWSWWNEN(NWSWSWSESEESESSSWNNWWN(E|WWSSWSESESSWNWWSSE(N|SSENNEENENESSESENESESSWNWSWSSSWWSSESWSESWSSESENESSSSEENESSWSESWWSESWSWSSEESSSSSWSESWWNWWS(WWWNEENEENE(NNE(NWWWWSWNWWSESWSWNNNNWWSSWNWWNEENWWNENESESENEENNESEEEE(SWSESWWWNW(SWNW|NEES)|ENNWSWWWNWNWSWNNENNNWSWWSSSE(NNEWSS|)SSW(SEENSWWN|)NWNNNNWNENNWNWSWNNWSWNWWWNNWNEENENWWWWS(EE|WWNNNNNEESEENWNWNWNEEENNWNWWNENWWNWWWSEESWSWSESWWWNWSWWNWWNWSWWNWSSSENEEEESWSWW(NEWS|)SSWNNWW(SSSSEN(EESWSSSEEEENEENNNEENWNENN(WSWW(NEWS|)SW(SSE(NENSWS|)SSWWW(NE(NNW(NEWS|)S|E)|S(WNSE|)E)|N)|ESESSSW(NN|SESWSWSSWN(NNENWESWSS|)WWSWWWWWSEESWSESWWNNWNW(SSESWSSESWSSSSSENEENWWNNENESS(EESWSSENESENESSENNESSENNENNWSWWWNWNW(SSEWNN|)NENWNW(NEENEEEESWSSSS(EEENESSEENNEEENWWWNNNEN(WWSSSS(WNNNNNN(EES(ENSW|)W|NNW(NENNNW(NENN(W(S|W)|NNE(S(SSSEWNNN|)EE(NWES|)E|N(W|N)))|SS)|WSWSESS(WWN(WSWWN(ENSW|)WWSSEN|E)|SSSE(NNNNNN|SWSWNN))))|SS)|ESSS(WNSE|)ENESSEN(N|ESE(N|ESWSWWN(E|WSWSWW(NEWS|)SSENESSENESEENWNEEESWSSE(NE(SEWN|)NNNWN(NNEWSS|)WSWWWSWN(SENEEEWWWSWN|)|SWSSSWWWNEENNWWWS(EE|WSSSSWWWNWNEEE(SWEN|)NWNWNNWSSWNWSSSE(NEEWWS|)SWWNNWNEN(WWSSWWWSWSEEESSWWSSEESES(EENESENNENESENN(WWNWWSESWWS(E|W(S|NW(WW|NNE(ESWENW|)NNW(S|WW)|S)))|ESSENNEEESWSEEESS(EEEENEN(ESE(SWWEEN|)NEEN(EEN(NESNWS|)WW|W)|NN(NN|WWSWSS(ENENSWSW|)WNNNENWWW(SESWENWN|)WWWN(EEEE|NN)))|WNWSWNW(WWS(EE|WWN(WSNE|)E)|NN)))|WWWWWWNEE(NWNENN(WSWSSWWWNENNE(SS|NWNEEE(SWSNEN|)NNNN(WWSWWW(NEENEWSWWS|)SSSSE(NNNEES(ENNSSW|)W|SSW(SSSSEEENWW(EESWWWEEENWW|)|N))|ESS(S|EEENWWN(SEESWWEENWWN|))))|EE)|EE))|NEN(NEN(WNSE|)ESE(S(WWSNEE|)EESS(WNSE|)(ENEEEE|S)|N)|W))))))))|W(SEWN|)WNENWN(NESNWS|)W)|WS(ESSWNSENNW|)WWN(E|W))|W)|NNE(NWNEWSES|)S)))|NN)|NNNNNNNNEENNEEENNNNNWNEEESSW(N|SSEESSSENNNNW(NNESENNNNEESWSESSESSWNW(NN|WSSSESS(EENESEEES(ESEESW(W|SESEENNW(NNNENWWSSWNWNWNENES(EEENNNNWNEENWNNNWSWWWSWSWSSSSWNW(NENWWNEENNNES(ENNNNENNENNWNWWWWWNWSWSSWSWSWSWWNWNENWWSSWNWSWSSEESENE(NWWWEEES|)SESESWWWS(EEEENNE(SSSWENNN|)EENWNW(SWNW(S|W)|NEEN(W|EENEESSSWWW(NEENSWWS|)(SEE(EENNNNNWN(EES(SS|E)|WSWNWSSW(ENNESEWNWSSW|))|SW(SESWENWN|)W)|W)))|WSSSWSEE(N|SWS(WNWNNW(SSSSSENN(SSWNNNSSSENN|)|NENWNEE(NEN(WNWW(SSENSWNN|)NNNNNNENNNNW(NNENEENENWWSWNNENENESES(SSSSEENWNNNESSESSESWWSSWWNENWWSWSESSES(ENN(ESENESS(ENNENNEES(ESEENWNWNNNNNEENENEENNNWSWNNNWNWWNENESENESENNESENNEESEESESWSEENNEENNNEESWSSENENEESESWW(SW(N|WWSWSSWSSWWWWSWWWSW(SWSW(WSWSW(SSEEEESSS(WWNENWW(EESWSEWNENWW|)|SESESEENNW(WNNENWNEEESESSESSENNNNESSEEESWSESSSWNWSWSWWWNNN(ESE(SWEN|)EN(W|E(NNWSNESS|)E)|W(NN(ESNW|)NW(N(N|E)|W)|SSWSWSES(WWWSWNW(S|NEEENWN(WSNE|)N(ESENEWSWNW|)N)|EEEEESEEENWWN(WWWWWN|NESEESSENENESSSSWWWWN(EEENSWWW|)WSWSESEEN(EEEES(ENNNNESENENEEE(SWWSWSWSS(WNNSSE|)ENENEE(NWES|)SSW(W|N|SSESEN(NWES|)ESSEES)|NWWWNWWSS(ENSW|)WW(NNE(NNNWNENWWSSWWW(NEENNENNNENNWSWSWNWSSS(E(SSWN|ENW)|WNWNW(SSEWNN|)WNNNESEE(NWNNWWNEENNW(SWWWWSSWNWWSWSWSESWS(SSSS|WNNWSWS(W|E)|EEENWNNE(N|ES(ENENNESS(SSW(SW(NWSNES|)SE(ENSW|)SS|N)|EE)|W)))|NEESEEESENESESSEENNESSSEENNW(S|NEESEESSESWSWSESENNEENWNNESENESESWWSSWWSSSSSSS(ENNNNEEESWSS(WNNSSE|)ENENNNESSEESSSENNESENNNWNWWNNWS(SSEESE|WNNENNWSW(SSSWSWWWNEENENW(ESWSWWEENENW|)|NNWNNEES(SENNENNENEENWNENWNWSSSWSWNNWNNESE(S|NNNWNENNWNNEENNENENENEESESESSSSWSSSWWWNWNWN(W(SSESSW(SEEEN(WNSE|)EEESSWW(NEWS|)W(SSSENEN(EESENENEENWWNENWNNENENWWSW(NNEEEESSSENESSWSSSEEESWWWW(NNNW(N(E|N|W)|S)|SESWSWNNWSWSWWSSEEN(W|E(N|EESWSSWWN(ENSW|)WSWSEESSESSESEESEEENNWNWS(SEWN|)WNNENNESSEENEESSEEEEENNESSENNNWWNWSWSS(ENSW|)WWNNNWWNNENEESS(S(SS|ENNNNWWNWWS(SWNWSSSWNNNW(NEEN(E(S|NEEES(WW|ESEENWNENNNENWWWSSS(ENNSSW|)(WWWNENWWNNWW(NNEES(EENNEEENNNEEENNWSWWNWNWSWWNENNNENNNENEEESSSSWSEESEESSSESSSSWNWWWW(SEESWSWWS(EEEEN(N(ESESEEENNENWWNEENNNEESENEEEESSEENENWNENWNENWWWNNNESSENENE(SS(SSSSSSSWSSSE(NN|SWWNNNWWSWNNWSWWWSSESENE(NWWEES|)EESE(NN|SWSEENEESSW(WWSEESWWWWSESWWNWSWWNWWSWWNENWWWNENWWN(WWSSWSSENESE(NNWNSESS|)EESWWWWSSW(SSW(NN|SEENEN(W|NNEEEEESESSSWWSEESSSENEESWSESSESSSWNWWSWSWSESWWSSSESWWNWNENWWSWNNWNNENWWSSSWNWSWNWSSESWWSSSSSSENNESEESESENNWNNWW(SEWN|)NENNEN(ESSWSESES(SSEEENEESWSWWWSW(N|SSENESSSWNWSSWNWNWNWWSWWWSSEEN(W|ESEE(NWNSES|)SWSSESSWSEENEEENWNEENWWWW(SSENSWNN|)(W|N(N|EEENESESENEESESEESWSWNWNW(N|SSESWSEEEN(EESEESWWSSSENEEESENENWNWSW(NNNNNWWS(ESWENW|)W(W|NNENWWWNWNEEES(W|ENENEESSSWW(NENSWS|)SEESENENE(NWW(NNNENWNENE(SSSSSWN(SENNNNSSSSWN|)|NWNNNE(NWNNWNEE(SS|NWNNWNNWSSWNNNWNW(NNWNNNNENNNEENWNEESEENWNNEE(N(NN|WWWSSWWWWSWSWW(NN(N|W|E(S|E))|SSSSENNNEE(NENSWS|)SSW(S|N)))|S(SSSWWSESSSE(NNN|SWSWNWWSESWS(EESEE(NWN(ENSW|)W|SSW(SESS|NWWNW))|WNNWNEN(W|NESEENNW(S|N(WSWNSENE|)N))))|W))|SSESSWWWSESSSESWSEESSWSEENNEE(NWWNWNNNN(WSSNNE|)EES(ENSW|)WSES(SEWN|)W|SWSESWS(SSSWWNENNNWSWNWWNWSWSWSWN(WSW(NWES|)SSENESSS(WNWSNESE|)ENNNENESSS(WNSE|)EEENNN(E|WSW(SEWN|)NN(W|E))|NENNE(NWWWWWN(EEEENNENN(WWSEWNEE|)NNNE(SSSESSSSW(WNENNSSWSE|)SSENE(SS|E)|EEE|N)|NW(SSSE|WNE))|S))|E))))|SS))|S)|SSSSSS(WNNWSWNNEEN(SWWSSEWNNEEN|)|SSSSSSWNWN(ENSW|)WSSESESSE(NN|SSWWSWNWNEE(NNWSWWWSESSESWSEEESESSE(SSWNWSSEESWSWWSSSSSSSSWNNNWNWNEE(S|NWWWSSSESSSSWWWNWSWNNWNWWNWNEENNNESSESS(EEE(NWNENWNWNNNEEENENEEE(NN(ESNW|)NWSWS(WNWNNNE(SSEWNN|)NNWSWSWSWNNENNE(S|NE(S|NNNWSSWWS(WWNENNWSWWNENNNNEESEEE(NNWW(SEWN|)WWWWWNWWSESESWSWWWSESSWNWWSSWWSWNNEENWWWWSSE(N|SSWWSSSWNWSWSESSESSWWN(NWN(E|WSSESSEEEENENNW(S|NN(WSNE|)ENNNEEEEN(ESSESWWSSSESSSSWNNNWWNNE(NWNN(E(E|S)|WSSS(SSSSESE(NNWESS|)SSESWSWWSEESSSWSWSWNWSWWWNEENENWNEE(NWNNNWSSSWSWWNWNNNNESENN(WWNNWNWSWNNENWWNWWSWNWSWSWNNENNEENNNESSENNESENENNWWNEEENNEESEEESSWWSWSESEE(SWWWNWNW(NNE(N(N|E(S|EE))|S)|SWSSENESE(SSWW(N(WW(SEWN|)WWW(NEEENW|WW)|E)|SS)|E))|NN(WSNE|)E(SEWN|)NNNNNNNNWSWNWSWNNENWWWWWSSESWWNWWWWNWSSESEEN(W|ESSEEN(W|ES(ENNNE(NWWEES|)SSES(W|EEN(ESSWWEENNW|)W)|SSWNWWWNWSSWSSWNNWNNN(ESESWENWNW|)NNNNEEEEENWNEEENESS(WWSSWWW(EEENNEWSSWWW|)|ENESEEENNNNWNNNNWSWWNWWWWWSSSWSEENEENWWNEEESSSS(WW(NEWS|)SWNWWS(E|WSWS(EENSWW|)WWNNWNNW(SSSESSSWNW(NEWS|)WWWWNWSWSEEEESSESSSESSSWSWNNWWSWNNWNNNEEE(NNWWWS(WNWSWWWNWSWNNWWNW(NEEEENNN(EESSSEENWNE(NWES|)EEES(WWS(SSWNWWW(W(WW|SEESEN)|NNN)|E)|E(ESNW|)N)|NWSSWWW(SEEEWWWN|)(NENE(NE(E|NW(WS|NE))|S)|W))|SSESE(S(WWWN(NWWW(S|NENWW(S|N))|E)|EEEESENESE(SWWWSWWW(NN(ESENSWNW|)W|SEESSESESSSSSSSWSSWW(SESESWSW(NN|SEEESESWWSESWSESSSWSEESENNWNNNNNENEEENNWSWNNWW(SESNWN|)W(NEENNWSWN(W|NNESENNESSEENWNENEEENNNNWSSWNWWWWSEES(SWNWSW(S|NNNNNNNENE(NWNWWSS(EN|S|WN)|SEEE(SEES(WWSWNWWW(NEEE|SEE)|ENNESSESSSWW(NENWESWS|)SSSWSSSEEESSESSENEEENNWNWNEN(WWWWW(NENE(N(WWSNEE|)NNNNNWNNWNNNNEE(NWNN(WW(SESWS|NWS)|E(S|NN))|SSW(N|SEESWSEEE(SWWSS(ENESNWSW|)SS|EEE(EE|NNW(WSE|NEE)))))|S)|WSEEEESWSESE(N|E))|EEN(E(N|SE(SWWS(WNSE|)ESSENNESSSWSWNW(SWSWNWSWWSESWSWWNENNWSWSWNWW(SWWSSWN(N|WSSEEEESWSWW(N(W|E)|SSENESENESSEENEESWS(WWWWWWN(EE|WWWWNWSS(WWNENNWSW(SS|NNENE(N(ESNW|)WNENNNN(WSW(SESW(W(W|N)|SSS)|N)|E)|S))|EEEE))|EENESEEENENWWW(SEWN|)NNNWSWNWNN(EEEES(WWW|ESSS(WNNSSE|)ENNENNW(S|WNEEESSESWSWSEENENNENNN(ESSSSWSESWWSSS(EENN(WSNE|)ESSEENNW(NWN(NNNEENWW(EESWWSNEENWW|)|EESEEEN(EEEN(ESSWWWSWSS(EEENW(NEEEESES(WWWNEWSEEE|)EEEENNESSEEEENNEEEESEEES(WWWWWN(WSNE|)E|ENEE(SWEN|)NNWWWS(EE|WNW(WWWWWWSSWWNENWNN(ESNW|)WSWS(WNNEN(EE|NWNWNNWNWWSESWSWSW(S(EESWSES(W|EENE(SSESWWNW(ESEENWESWWNW|)|NN(E|NWSSW(S|NN(NENSWS|)W))))|W)|NNNE(S|N(NENESENENEEENEESWS(WSWNWSS(WNSE|)S(ENESNWSW|)S|EE(SSESSNNWNN|)NNNNNWWWWSEEESWWWSWNWWNWW(NEENNESE(SWSEWNEN|)EENWWNWWW(NENWNNNEN(WW(S(WW|SS)|N)|ENENN(WSNE|)E(SSSEESSESWWWNENWW(SSW(WNENSWSE|)SEES(ENESS(ENE(SSEESE(SWSS(ENENSWSW|)WNNNWWWNE(WSEEESNWWWNE|)|NN)|N(NNESNWSS|)W)|WW)|WW)|N)|EN(W|NN)))|SSWNWNE(WSESENSWNWNE|))|SSS(W(S|W)|EN(E(S|E)|N))))|W))))|E)|N(NNN|EEENESENNNWSWNNENNNN(WSSSNNNE|)E(SSSS|N))|S)))|W)|WWNENW)|W)|WW))|S)|WNNWSSW(NN|W))|WSW(SEWN|)NNENN(NNNNESSSSSS(NNNNNNWESSSSSS|)|WSWWWSS(EENWESWW|)WNWWSESWW(EENWNEWSESWW|)))))|WWNWW(N|S(WNWSNESE|)SE(EESWSW(NWSWENES|)S(EEE(EESW|NW)|S)|N))))))|NENWNEENN(EESSESWW(WSEWNE|)NN|WNNNW(NEWS|)SSSWS(EE|W(SEWN|)NW(NEEWWS|)S)))|NN)|N))|WW)))|N)))|E(N|EE)))|W))|NENWNEENWWNENNWSWNNEE(ESSSNNNW|)NWNNWSWWSW(NNEEWWSS|)SSW(NWES|)SESSW(N|S(W|EENEN(ESSWSESWW(N|S(EE|S))|NW(NNE(NEWS|)S|S))))))|N))|N))|EE)|SWS(WNSE|)SEE(ESNW|)N(NN|W))|NNESESSENEE(SWSWSNENEN|)NWNNESENNNEEENNEEEEESS(ENESEENWNEESEN(NNNNNNWWNWNNWNEESSEE(SWEN|)ENNNWNENENWNN(WN(W(SSESWS(WSWS(WNWWN(EEE|WN(WNWSWWWNWNENNN(NWWNNWN(NESENNE(N|SSS(SWNSEN|)E)|WWSESWW(N|SSSEENN(WSNE|)E(SESE(SWSWN(WWSSW(SEEN(ESE(N|SE(N|SEEEEN(ESSE(EESSWWWN(EE|WWSSSSEESSEENWNENN(ESSE(ESSENESSWWWNW(NEWS|)SWSES(WWWNENWWSSWNWNENN(ESNW|)WWWNWWSSWWWWSEESESEENEE(NWN(W(N|SW(S|W))|EE)|S(WSS(ENSW|)WNWWWNWNWWWNWN(WS(SESSS(WNNSSE|)ES(ENNN(WSNE|)ESSSEES(WS(WNWSNESE|)ES(S|W)|ENE(NWWWNSEEES|)S)|W)|W)|EE(NNN(EESS(WNSE|)ENE(NEN(WWSNEE|)NENEEN(E(EE|SSWWSWSEEE(SW|NW))|WWW(S|N(NWES|)E))|S)|NWN(NESNWS|)WS(SEWN|)W)|S))|E))|SENEEENWWW(EEESWWEENWWW|))|NN)|WSWNW(N|S)))|N)|WWW)))|N)|NWN(E|NNN))|N)|N)|N)))|EESWSSE(SW|ENW))|E))|EE(SSENSWNN|)N)|E)|W)|N)|EEEESSEES(WWSWW(WSEEEWWWNE|)NENNW(S|W)|ENEEENWWWWN(WSNE|)EEEENWNNEES(W|E(SEESESS(WWSWW(S(E|WNWSW(N|SS(ENES(EN|SWW)|W)))|NNE(S|E(NWWNSEES|)E))|E)|NNWWWW(NENE(NNN(ESSENSWNNW|)WSW(N|S(SWSWENEN|)E)|S)|SSS)))))|EEESEE(NWNWESES|)S(WWWNWSS(WNWSSWWN(WSSSENESSSW(SSSSES(WWNSEE|)ENEEENWNNNWSSSWNN(WSSNNE|)NN(NN|EEESE(N|SWSE(SSSESEESWWSEEE(S(ENSW|)WWWSWS(EENSWW|)WWNENENNWSWSWNNW(SSSSEN|NENEES(WSNE|)E)|NNN(EN(W|ESENNESSSE(NNNNW(NEWS|)W|EEEEEN))|WW))|E)))|N)|E)|E)|ENESS(S|W)))|W(WN(WWSEWNEE|)E|S))))|ESENNWNNESE(N|SSESSWN(SENNWNSESSWN|))))))))|EES(WSSSW(WNEWSE|)S|ENE(ESESSWNW(N|SS)|N)))|EESWWSE(WNEENWESWWSE|))|W))|S)|WW)))|E))|SES(WWNWWW(N|SEESESW(ENWNWWEESESW|))|ESENN(E(NWES|)SSS(WWSEEWWNEE|)E|W)))|E)))|E)|SSWS(WN(NEWS|)WSWWS(WNSE|)EES(ENESNWSW|)WW|EE))|SWW(SEESENN(SSWNWWEESENN|)|W))|W(N|W)))|NNNWN(NESNWS|)WW)|E))))))|WW)|W))))))|W)|WWSSWWSSEN(SWNNEEWWSSEN|))))|NN)|N|EEESSEESENEES(ENNWNWN(EEEE(NWES|)SW(W|SEESWWS(NEENWWEESWWS|))|NW(NNNN(N|EEENEE)|SW(N|SS(WNSE|)E(E|N))))|W|S))|N)))|W)|NNNWSSW(S|NWN(E|WSWWN(E|WWSWNWWSSWSEEEEN(WWNSEE|)E(N|SSESSWWN(NWSWNWSSSEE(NWES|)SEEN(ESES(WWWWWNWWS(E|SWW(NENNNE(NNWSWNWNENE(S|NN(ESNW|)WWS(E|SWWSSE(N|SW(WNNNNEENWWWWWWWWWWWSEEE(E|SWWWSSENES(ENSW|)SWSESWWWWNWNWWNWNWSSSWNWWNNWWNEENEEEN(WWWWWWS(EE|WNWSWSSWSWNWWNEEENN(WWS(WNWSSWNNWSSWWWWNEN(EESWENWW|)WWSWNWSSESE(N|SWSESWSWNWNNN(ESSNNW|)WWSWSWWNNE(ENWNWSWWWWWNN(WWWWWSSWSWNWSWWSESWSESSWNWWSESESWSWNNWWNWNNNWSSSWSWSESSWNWSSSWNWNENNNE(S|NNE(S|ENWWNENNNNN(EEESESEENWN(EEEEES(EENWESWW|)WWS(W(SWSWSS(W(SESNWN|)NNN(E|WWS(W(S|NNE(NWES|)E)|E))|EEN(W|N))|N)|E)|W)|WSWNWSWNWWWSEESSWWWSESWWWWNWW(NNNNEEESSE(SW(SEWN|)WWNNES|E(NWNEWSES|)EE)|SSE(ESENESESWSWNWSSSWNNNW(NEWS|)SSSSEEENNEEEN(NEENWN(EESES(WSESSWWSWWWSSEESENN(E(SESWSWWWNWWWWNN(WSSSW(SSESSW(N|SSSSENESSSEENENNWNW(SS(E|S)|NNW(SSWNSENN|)NEENWWN(W|NESENESESEEEEN(WWW|ESENEEESSWSES(EENNW(NEENWNW(WWWWW(NEEEEEEESESSSWS(S|EENNENENENNWSWW(NW(S|WNN(WSWW(NENEN(ESNW|)WW(NEWS|)S|WS(WNSE|)EEE)|ESEE(EEENENWWNEENNEESSENNENWWNWSWWW(NNEN(W|EEES(WWSWENEE|)EENNW(S|W(W|NEN(W|ESE(N|SSSEENN(WSNE|)EEESSWNWSSSSSSEENEESSEENWNENNWN(ENE(SSSE(N|SSSSSSEESWWWNWWSSSWSEEESSSWWNWN(EESNWW|)WS(WNWNEENWWWNNEES(W|ENNNE(SSS|EN(WWN(WWWSWWWNW(NEN(W|NNN(WW|EESWSESSSWNN(SSENNNSSSWNN|)))|SSESWSEENE(EN(ENESSW|WW)|SSSS(SENSWN|)WWNN(ESNW|)WSWWSSWS(SEEN(NNEWSS|)W|WWNENWW(SW(N|W)|NENNNESES(S(WNSE|)S|EENNW(WN(NN(ESSENN|NN)|W)|S))))))|N)|EE(SWEN|)NNN)))|SESWSWSSWWSS(ENEES(ESE(SS|EENESENEEEENNWWNWSS(EE|WNNNWN(EENWWNNNESSENEESESEEENEENNEE(SWSS(SSSWSESE(N|SESWWNWWWSWNW(SWS(WWN(W|E)|EEEE(NEWS|)SWWWWS)|NEEE(E|NNNENW(NEWS|)WSSWNWN(WWS(W(W|NN(N|E))|ES(ESEEWWNW|)W)|E))))|E(E|N))|NNWNENWWNENWWWWWNNNESES(ENESEESSEE(SWEN|)NNE(S|ENNNNESS(S|ENEES(W|ENNWWNNN(WWNENWWSSSES(WWSSWSS(ENSW|)W(WNNNE(ENN(ENSW|)WWS(WSSWWNWWS(ESEEES|WWWW(SESSSWWW(SEEESEEN(WNNNNSSSSE|)EESE(N|SWW(SWNWSWSEESS(WNWWWNN(E(S|N(N|E))|WSWNWW(SEWN|)N)|E(SWEN|)NNESE(SWEN|)NE(N(WW|N)|E))|N))|NEN(NNWSS|ES))|NENENNEN(WWSSNNEE|)EESWSES(WW(SWEN|)N|EE(S|NWNNESE(E|S)))))|E)|SS)|SS)|E(N|S))|ESSEESEEESWSWSS(ESENN(NEESWSSENESENESSEEE(S(WWWWW(SEWN|)N(WWWWWN|E)|S)|ENNEN(WWWSS(ENSW|)WNNWNEN(ESNW|)WWW(SESWENWN|)WN(W(S|N(WNSE|)E)|E)|ESSWSE))|W)|WN(NNEWSS|)W)))))|W)|E)|WWWSWSWSESEE(SWEN|)NN(WSNE|)E(ESWSE|NW))))|W)|WNWN(WSNE|)NE(EENSWW|)S)))|N)|WSWWS(EEE|W(NNEEWWSS|)S)))))))|SESWWSSWS(W|EE))|S)))|S(S|E)))|W)|S)|S)|WWWSWWSESSWSSSWSEENNNESSESSW(WWSEEE(ENNNNEE(NWWW(N(EE|NN(NE|WSS))|S)|SS(EE|W(N|S(E|S))))|SWSESWWNWS(WNN(EE|NNW(SS|WWNNEE(SWEN|)NNWW(S(E|W(N|WS(ESNW|)WWWW(SE(E|SWSSSS)|NE(NWNEWSES|)EE)))|NNNNESENE(NEENEEN(NEWS|)WWWSWWN(WSWNW(N|SS(WNSE|)(EEE|S))|E)|SS(S(WNWSNESE|)SS|E)))))|SEES(ENSW|)WWSSWNWS(NESENNSSWNWS|)))|N))))))|NNN)|ESENNNEEENE(NWES|)E)|N)|WW)|ENNWNNE(NN(ESSNNW|)WSW(SSWWNE|N)|S))|W(S|W))|W)|N)))))|EEEE(SWWWEEEN|)EEESESENN(ESSNNW|)W)|S))|E)|E))|EEEEEESSWSS(WWNWNN(WSWWWSESW(ENWNEEWWSESW|)|ESE(NEWS|)S)|SE(SENSWN|)NN)))|SEE(N|ESWS(E|S))))))|S)|SES(ENSW|)WSSS(SENSWN|)W))|ENE(SSS|NWWNNNNN(WSNE|)EE))|W)|E))))))|N)|W)|WNW(NEEEWWWS|)SS(WWNEWSEE|)SS)|NEEEN(ESNW|)NNNWWNWS(S|WNWWNEENWNNESENNW(ESSWNWESENNW|)))|W)|SESWS(WN|EES))|S)))|WW)|SW(SSE(S(WSW(WWSEE(SS(WNSE|)S|E)|NN)|EEE(S(WSNE|)EE|NN))|N)|N))|E))|W(N|W)))))|SSW(SESSW(SEWN|)N|N))|W)|W)|N)|W)|NNESES(SEE(SWEN|)NWNNWN(EE(ESWSEWNENW|)NW(W|N)|W)|W)))|W)))|SWSSSWNW(SSEWNN|)WNENNNNNWNNWWSESSESWSS(ENSW|)WNNNWN(E|NNWSSSSESWW(NNNWWNNEE(SWEN|)NNW(S|NNWN(EESE(N|S(SSENENEE(N(WWWSNEEE|)NE(NWES|)S|SWS(EESEESW(SESWSS(ENSW|)SS|W)|W))|W))|NNWWWSSW(WNENWNEE(WWSESWENWNEE|)|SEE(SWWEEN|)NE(NWES|)S)))|SSEE(EESW|NW))))))|S(S|WW)))|SEESE(NESNWS|)SWW(S|W(NEWS|)W))|S)|SSS))|WWSESWWSWSWNNN(E(ENSW|)S|WSWSSE(N|SSS(E(E|NN)|SWNWWNEN(ESNW|)NNWSSWSWWW(NNNNNENESEES(WSWNWSSSENE(WSWNNNSSSENE|)|ENENWNWNN(WWSES(SEWN|)WWNNW(NEEEEWWWWS|)S|E(S|E)))|SEESSSENESSWWWSW(NNNE(NWWSNEES|)S|SESSSWWSSEEN(ESSEESENESESWSESWWNWN(E|WWN(WWSW(SSSW(N|WSEEEENENWN(WSSNNE|)(N|EESESESENESSESWWSW(NWN(NW(WSEWNE|)N|EE)|SSENEEN(W|ENNE(SSSSW(N|SESEESE(S(ENESNWSW|)WSWNWN(WNSE|)E|NNWWN(EE|N)))|NNNNNWW(SESWSESW(ENWNENSWSESW|)|NNEN(NEN(W|E(N|ES(E|WSWSEE(SWWWEEEN|)N)))|WW(S|WWNWNNWS(SSEWNN|)WNNNEES(E(SSESNWNN|)NN(WWW|E(NNN(W(NWWNSEES|)SS|E)|E))|W)))))))))|NWWWWN(EENNE(SSEEEWWWNN|)NWWN(ENNESE(S(ENSW|)W|N)|W)|WW(S(S|E)|N)))|E))|W)))))))|W)))))|S))|N)|N)|NNNNWNW(S|N(W|EEEESW(W|SESE(SWWNSEEN|)NNE(NWNENWW(SWWEEN|)N|SSEEENWN(WS|EENNE)))))))|N)|W)|SWSW(NNEWSS|)S)|W)|WWNNW(SSS(WSNE|)E|NNN(NE(ENSW|)S|W)))|WW)|SSS)|EE)|SS))|E)))|S)|SSS(WW(N(WNSE|)E|S)|EE(SWEN|)N(W|ENEEEE(SWEN|)NWNNWW(NENEESW(ENWWSWENEESW|)|SS(EN|WNN)))))|S)|S))|W)|SSWSE(E|S(S|WWNNNWSWNWNWN(WWSSWWSES(E(EN(W|E(NWNSES|)SE(ES(E(S|N)|W)|N))|S)|W)|EE(NNWSNESS|)SEEE(N|S))))))|W)))))|SS)|S)|E)))|E))|N)|EE(SEWN|)NNNENE)|S(SS|W)))))$"

# COMMAND ----------

get_paths <- function(s) {
  xs <- NULL
  ys <- NULL
  
  from_xs <- NULL
  from_ys <- NULL
  to_xs <- NULL
  to_ys <- NULL
  
  x <- 0
  y <- 0
  
  prev_x <- x
  prev_y <- y
  
  vs <- s %>% str_remove_all("\\^|\\$") %>% str_split("") %>% first()
  for (v in vs) {
    if (v == "(") {
      xs <- c(xs, x)
      ys <- c(ys, y)
    } else if (v == ")") {
      x <- xs[length(xs)]
      y <- ys[length(ys)]
      xs <- head(xs, -1)
      ys <- head(ys, -1)
    } else if (v == "|") {
      x <- xs[length(xs)]
      y <- ys[length(ys)]
    } else {
      x <- x + (v == "E") - (v == "W")
      y <- y + (v == "S") - (v == "N")
      
      from_xs <- c(from_xs, prev_x)
      from_ys <- c(from_ys, prev_y)
      to_xs <- c(to_xs, x)
      to_ys <- c(to_ys, y)
    }
    prev_x <- x
    prev_y <- y
  }
  
  tibble(from_x = from_xs, from_y = from_ys, to_x = to_xs, to_y = to_ys)
}

# COMMAND ----------

paths <- get_paths(input)
from <- str_c(paths$from_x, paths$from_y, sep = ",")
to <- str_c(paths$to_x, paths$to_y, sep = ",")
lst(from, to)

# COMMAND ----------

visited <- NULL
visited_d <- NULL
poss <- c("0,0")
ds <- c(0)

while (length(ds) > 0) {
  pos <- poss[1]
  d <- ds[1]
    
  poss <- poss[-1]
  ds <- ds[-1]

  if (pos %in% visited) next
  
  visited <- c(visited, pos)
  visited_d <- c(visited_d, d)
  
  new_poss <- to[from == pos]
  poss <- c(poss, new_poss)
  ds <- c(ds, rep(d + 1, length(new_poss)))
}

answer <- max(visited_d)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Okay, so the facility is <span title="Really, really big. No, bigger than that. Even bigger. Keep going. Move. No, more. Look, we're talking krakens and dreadnoughts for housepets. It was big!"><em>big</em></span>.</p>
# MAGIC <p><em>How many rooms have a shortest path from your current location that pass through at least <code>1000</code> doors?</em></p>
# MAGIC </article>

# COMMAND ----------

answer <- sum(visited_d >= 1000)
answer
