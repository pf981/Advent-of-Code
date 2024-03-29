# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/3

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 3: Gear Ratios ---</h2><p>You and the Elf eventually reach a <a href="https://en.wikipedia.org/wiki/Gondola_lift" target="_blank">gondola lift</a> station; he says the gondola lift will take you up to the <em>water source</em>, but this is as far as he can bring you. You go inside.</p>
# MAGIC <p>It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.</p>
# MAGIC <p>"Aaah!"</p>
# MAGIC <p>You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.</p>
# MAGIC <p>The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can <em>add up all the part numbers</em> in the engine schematic, it should be easy to work out which part is missing.</p>
# MAGIC <p>The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently <em>any number adjacent to a symbol</em>, even diagonally, is a "part number" and should be included in your sum. (Periods (<code>.</code>) do not count as a symbol.)</p>
# MAGIC <p>Here is an example engine schematic:</p>
# MAGIC <pre><code>467..114..
# MAGIC ...*......
# MAGIC ..35..633.
# MAGIC ......#...
# MAGIC 617*......
# MAGIC .....+.58.
# MAGIC ..592.....
# MAGIC ......755.
# MAGIC ...$.*....
# MAGIC .664.598..
# MAGIC </code></pre>
# MAGIC <p>In this schematic, two numbers are <em>not</em> part numbers because they are not adjacent to a symbol: <code>114</code> (top right) and <code>58</code> (middle right). Every other number is adjacent to a symbol and so <em>is</em> a part number; their sum is <code><em>4361</em></code>.</p>
# MAGIC <p>Of course, the actual engine schematic is much larger. <em>What is the sum of all of the part numbers in the engine schematic?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''....401.............425.......323......791......697...............963............................................420........................
...*..................................%......#.....*....290.........................492.............656...@953.....................+830.....
..159...........823...33.717.....572.......806...896......-.....335....834......815.............791....*..............776...................
.........-.....#........*.........*..................715..........*.....*........*.....................5...*.....................688........
....=..=..573..............212.......553.632....622....*.......260....29.........692.129....727...........290.........%32.....%...*..441....
.791..998..............................*............531.......................84.......*..../.......506%......=............240..831..*......
.....................321.586........447...&.-276.21......@..........12.......&.......-..333...................619..94................982....
..........@...........#..*..............525.......*...183............*............407.......23.........%............&......846..............
....97..686.............89.....................-..494..............875....*607.............*.......239.407..................%.......529.....
.....+.........815..703............208.=555.856...........@............133........................*..........672...501........898#...*......
...............*.......*...659.......*....................183..............528.......614.......4....................................39......
...602..........804..313....*.......480..............602.............354......*877................832@.....140...$...........707.......222..
...*....999.................23.264..............516.....*.......-....*....................................*.....722......24....*........*...
436....+................./......./..........765*......37.....843....218..........852*68....290............410...........*.....539....896....
.........../...#........907............587...............&................149...............*.......*..............#780..707................
........349....603.598....................-....203.....178.......431......./...............152......571....926.750.............127..........
.............@........*176.283...................*...%......642......../......20..............................*.........@.............534...
...749..../.194..............*.......337.395*....682.429.=...#..........186.....*.........682..../......498..........%.8.............*......
....*..324..........893*...878......*........659..........65....671.189.......641...........+.859.........$.......149....648........53.+....
...776......$.....................667.................432...........*..............697............282.901...................*889........471.
............103............../........-..................-...748&.257.............&...........739*....*......491*543................997.....
.........2.........813*.....278..316.333.....296.142.+...................673.%....../.....+.........490...................790........*......
......@.*.......................*...............*....643.464............*....25....108..807..179.........931.......289..........365...522...
....367.250.927../.............754.........14...............*.+..........23...................*......&.....*..%..........323................
................939...644..............791..*.551....35...937..806...............&.............536.930...703...565......*...............*640
534$.................*.........$..448.....=......*...................707*658.....33....920..74.....................844................36....
.......572....672...875......770.+................380.............52......................*.......-....251............%........*909......677
.......*.......=........................658.889.........882.....=......................534..*..291...%....*.................289.............
.212......993..............438./..........*....@..532......*586.163....213...307...........167.....981.700..................................
....*.....*..................-..12...611...196.......*309.....................+.......*685............................403....243..+385......
59...428..14...22.747....990............*........575...............................247.....985....&..................*.......*..............
.................*........%...539.......416.712.....*2..408.......%....................999.......275......738.....715......670..............
..357........653..............*....374..........285................785.........384......*.............277*........................765.137...
...@..........*..@632......361.......=..............35.........329..............................=858..............798.................*.....
......................216*.......459..................*..........&........479.....255......302......................*.530.........269..453..
............./.573........153.....*........#.......462...%..........45......+.122*............*672....545........157.....*862.....*.........
820....%...977.+...................726...790.199.........631....308..................755..............*...460..................643....#237..
.......229.............727..425............../..........................228........#..$...............385....&...........695................
...................978.*....*....................700....*.........256..@.........625......311.170...+................642*...................
.492.....983.........-.577.743..................*....267.521........%....479.......................696.980......................*...........
....*820.#....................................236.................*......*...856.............137...........489......409........177..450.....
974.........479.$......182..456......./.............*755..617..333.849.........*...............*..........*..........=...-...........*......
...+..........*..83.#....@.=...........893.......610.........*.................727....6*..488.839...449..541../97......560.........449......
............208......168......971..........................547..........559............................=...........237...................641
.......336...................*....563..993.911.=......853................*...............391...@572.................*.......*......614..*...
........$...........579.....810....-......*....480....*......649.138..410..201..604........*..............450#.....485...124.841..*......790
..399...........928.............67..................#..295......*............*...#....333...83...#111.............................635.......
...=........./.....*..807...529..*......642#......603......704.........@....599......&.................=....................................
..............233.618..../........114........566......100..*.....423.26...............................168................555$..........#625.
.....608*372..................543..........*.*............4.....*.......+374.......436*...................680.135....................*......
.................................@...385.309..111......69....991..127........693#......985....25..856*96.+.......*860..........%..278.160...
.......351.......495=.772..............*...............*...........*...........................@............569...............905...........
........................*.$402........640.*.............366.........350...623&...250.............446*341.....=.........................292..
....#..*...595.289...347..........75.......844......307..........................*....585.....*..................766+...................*...
.148..906.....*..........232.449...*...........................................326..$...-..102.595.....406............-...........650....682
..........619...23........$...*.....138.893.......890...79....53.........118........966................+..............233............*......
.........*......../..........62..........*........*....*.............@..*....................245...........-....806.........98........318...
....534+.264..993...420.................675..77..659..263..........615.405...............=..*......%..75...614.*..................4.........
...............*..............421.........................834*287.......................813..651.902...*........134.....$...........334.....
....631....=..443........................352..........941...............317.......*286...............562.855............690....387.....*....
.27...$.430......................89....-....*90...&......%..........155.......899.......%59....*986.................775..............25.....
...*....................-.....+...*...952.........62.........478...........&...../..........694.........775.....640..$......................
....102..........+197....109.270.453.....................................641.......123..........573....*.......=............880.403+........
.........87.186..........................709.+219........224.726...882.............*...868..203*....732............928*607..*...............
..819....*..*.............*....81........*....................-../..%...+..........700.=.......................149............*....438..=...
....#.875..223.106.........646......%.....519...579.............38.....883.626@....................149..........=..........205.272./....480.
.......................965.........332.........*......221.292...........................594..945......*931..365....814*214..................
..228*....29............*....79...........+.....811.....*..*..592..........681.............*....#.427........*................170..58.......
......563...*........817..93*...+60..507...898........796.942...*..=335.......@...490....488.......-......974....817...........*....+.......
...........519..&...................*..........948.............454......184.........*.........=.......................409......947..........
...............272..........257....712............+.@.....338..............*381...824..923..756.............971*181....=....+......430......
....228.............709.......&......................685.....*..597....135......+.....*..........+......471..................452..*......923
....*..................#...........271.....................167.*.........*.......325.935..........224......*.....749&...-..........587......
..464.../199..$..........50...........*..794..........36.......733....................................@....414...........605................
...............765.%.......=.215*717........*715....................210......845.......................643........66...........*908.........
.........215........761............................544....781...390*.....576..*....869..781....517................*.....356.664.......=.....
..............316...........235/...............715*.....-....*.............*..130..........*..@..........&.........564.*...............89...
...................................&....169...........353....390....57.71.847...........716.........466..516..651......447..................
.......459..................101.379.....*......324...................#.#............943..............*...........%.........$625.../...586...
........*.....173...................198..306...*....313........51............629...*..........-958..228.178.......................967.......
......714...@.........206.......934*.........109...........*.........../......*....832...................*........934.....921..........897..
...........487............700......................*507..415....349%...179...961................437.......489.......*............../...*....
.................*440.952*................667...533.....................................359.618....*927.........................968...412...
...........-..778..................667.....@..........764..401.........279.......#.748.....*................534*.....444....................
...835..779......../.....443.........*.........................53/......=......774......=....784...204..385.....929..........+...861........
......%..........74..947*.....187&.874..........&.........................545........752.......$....$...*..................308.....*..284...
........#.................190...........445$..784...51*226...................*............*245..........435.......=...200..........88.*.....
640.....310...&...........*......296..........................................107......943..........244...........662......=..440+....302...
...*..........67........381..............856....349...........790*...911........................901...*......733........844.................
.327..............885........169.....419........*.....62..........70..@..664...........=...422%...*....617.....*....................230*....
...........916...@.............................95....@.....+.........................355.........104...........149......................569.
.............*.........................230.../..............350..............................432.....710............=.........=.............
..925..545..634.....@..297*933...........*....839...33...........34.....162.......577..248.....#...........814...524..........790......9/...
...*...............66....................421............606+..*../.......&.........*....&..129..............=......................529......
659..........253...........$504.......*......................379....&........./..860......+..............&...............%.....658*....310..
........208...*........................354..........................647......326...............911.....503.......11.......293...............
....*.....&.617..511.........885.906......................166/......................589..........*..........749....*931..........915........
.852.908........................*................../........................297.470*........#628..269...613......#................*.........
.........................716.................689...460...737*502...510.............../...........................778.......373..734.....+...
..520=.........../.....*....*226........326.....+.................+............971...362........800$..904.303.........*874..........=..548..
............554.889.720.854......808.....*..258............284*........639/...*...........................*........603.............839......
...........*........................*690.71..*.........314.....795.86.........53.................786%...134...................890*..........
663.....225...%........513...................951..........*........*...............275.995...764.....................=............30........
...*...........353....*...........%......................468.....87..225........31..=.....%.=......../.......886.....84.....................
..694......166........243........380...275..287..............261.....@.....888....*............162...278.......&..........351.534........197
........$.......209.-......261...........*.......876.....15.....*.........*........712.....870...*.......897.....46...........#.............
......450.........%..463.....%.679....119.....=.*....@...@.........871...408..995*...........*...922.+..........*...66.466..................
..............803.........................$.250...493...............&.............356.519.552........737.......153....*.............+.......
......982........*.....................540...................641.......................*......&....................................851../...
..............638..............=.306....................+938..@................*520....511.174......*..........-......*503...832.........219
.292..239...................775..*......334..../582...................173...859..................238.678......117..429.......%...708.534....
........*........240....491.....546...................+................*.............%....498.............................55........*.....74
.816.....406.......*...&..............181...........765.......776....+..636...&337...264..*............*716..$908...........*...............
...................860....................980...................$..323....................163.......851............*.......396......501.....
...-..20*197................722..........*...............................&.....408..............109.......794*155..590........./....$.......
.482...........257..........*............999./850.........482..........933........*.*982...../.....*..........................826.......908.
.......%597......@..345.329..172.....295...........349....*.....=527........174.727........645...167......@..........*......................
.....................*.....+..........$.............*....725...............*............$............+.447..723...346.759............967....
............638..............................589.....................................=..312..+....951..........=..........809*..........#...
.............@............325..........322.........&......................508......359......768........8..&.........992.....................
.783.32...................*............*.........656.............98*178.....%.....................74*.....2...410&....@............+........
...*...*..54*525...112..720...66......641.+280.......................................................467.......................580..348.....
..699.673......................................491..869............#......171..............98............473......%..............$..........
........................%.....214.......303$......#..%.......191.852..560*.......835..550...$.150.........#........291.......240............
.......579...982.........713....*...536.......................+...................*....#........$..840.......43................*............
......$.........*....*.......606......+....48...........993.......838*744.880....969........@........*......*....*726..........168...&......
...............395.579............340......*........386.=...420..............*........833..835........257...842....................810...635
......#......................%...........983...632.@........*........-...%..157...193*...........................@..137....209..............
.....819.....................278..377........................578...195..230........................$......586.985...............263.417.....
................592....../............*......../.............................922.......350........138.156*............698...78*.........$571
....................405/..573.764....257.@940...34.977$..441....304.............*.....*................................*.......93..600......
...643....675...262..........................................................993.....556...........314........278.258.322............*......
...*.........*.....&................/.....................222.........959................@..121.......*...930.......#.......170*462.....588.
384....+..19.863..............407=.283.........972...340....#....427*....*737...........558...%.....91......*...........................=...
.....812...@.........298..563....................*......*............506..........845......................634...&............624+...&......
.....................*.....=.....*.............492.563...950..827*...............+....................968......652..................49......
.730.........498..382.........399.......824.........&...................390.630........248...........*.......-......448......-..............
................*......333..........832*.....#...............$...565.....*...............*............701..564.........*.115..718.......313.
.960...*965....993......*.....*..............604..........730...*..................234&..662.....+..............=69.930...*.......967*......
.....30..............355...978...........67.........419........239..........732...............645..........................484........664...
'''

# COMMAND ----------

import dataclasses


@dataclasses.dataclass(frozen=True)
class Number:
    row: int
    start_col: int
    end_col: int
    value: int


def get_number(pos, digits):
    start_col = pos[1]
    while (pos[0], start_col - 1) in digits:
        start_col -= 1

    end_col = pos[1]
    while (pos[0], end_col + 1) in digits:
        end_col += 1

    return Number(
        row=pos[0],
        start_col=start_col,
        end_col=end_col,
        value=int(''.join(digits[pos[0], col] for col in range(start_col, end_col + 1)))
    )


m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
symbols = {pos for pos, c in m.items() if c not in '0123456789.'}
digits = {pos: c for pos, c in m.items() if c in '0123456789'}

numbers = {}
for pos, c in digits.items():
    if pos in numbers:
        continue

    number = get_number(pos, digits)
    for col in range(number.start_col, number.end_col + 1):
        numbers[(number.row, col)] = number

valid_numbers = {numbers[(row + dr, col + dc)] for row, col in symbols for dr in range(-1, 2) for dc in range(-1, 2) if (row + dr, col + dc) in numbers}
answer = sum(number.value for number in valid_numbers)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.</p>
# MAGIC <p>You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.</p>
# MAGIC <p>Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.</p>
# MAGIC <p>The missing part wasn't the only issue - one of the gears in the engine is wrong. A <em>gear</em> is any <code>*</code> symbol that is adjacent to <em>exactly two part numbers</em>. Its <em>gear ratio</em> is the result of <span title="They're magic gears.">multiplying</span> those two numbers together.</p>
# MAGIC <p>This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.</p>
# MAGIC <p>Consider the same engine schematic again:</p>
# MAGIC <pre><code>467..114..
# MAGIC ...*......
# MAGIC ..35..633.
# MAGIC ......#...
# MAGIC 617*......
# MAGIC .....+.58.
# MAGIC ..592.....
# MAGIC ......755.
# MAGIC ...$.*....
# MAGIC .664.598..
# MAGIC </code></pre>
# MAGIC <p>In this schematic, there are <em>two</em> gears. The first is in the top left; it has part numbers <code>467</code> and <code>35</code>, so its gear ratio is <code>16345</code>. The second gear is in the lower right; its gear ratio is <code>451490</code>. (The <code>*</code> adjacent to <code>617</code> is <em>not</em> a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces <code><em>467835</em></code>.</p>
# MAGIC <p><em>What is the sum of all of the gear ratios in your engine schematic?</em></p>
# MAGIC </article>

# COMMAND ----------

import math


gears = {pos for pos, c in m.items() if c == '*'}
gear_ratios = 0
for row, col in gears:
    neighbors = {numbers[row + dr, col + dc] for dr in range(-1, 2) for dc in range(-1, 2) if (row + dr, col + dc) in numbers}
    if len(neighbors) == 2:
        gear_ratios += math.prod(number.value for number in neighbors)

answer = gear_ratios
print(answer)
