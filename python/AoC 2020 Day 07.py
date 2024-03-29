# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/7

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 7: Handy Haversacks ---</h2><p>You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to <em>issues in luggage processing</em>.</p>
# MAGIC <p>Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!</p>
# MAGIC <p>For example, consider the following rules:</p>
# MAGIC <pre><code>light red bags contain 1 bright white bag, 2 muted yellow bags.
# MAGIC dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# MAGIC bright white bags contain 1 shiny gold bag.
# MAGIC muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# MAGIC shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# MAGIC dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# MAGIC vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# MAGIC faded blue bags contain no other bags.
# MAGIC dotted black bags contain no other bags.
# MAGIC </code></pre>
# MAGIC <p>These rules specify the required contents for 9 bag types. In this example, every <code>faded blue</code> bag is empty, every <code>vibrant plum</code> bag contains 11 bags (5 <code>faded blue</code> and 6 <code>dotted black</code>), and so on.</p>
# MAGIC <p>You have a <code><em>shiny gold</em></code> bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one <code>shiny gold</code> bag?)</p>
# MAGIC <p>In the above rules, the following options would be available to you:</p>
# MAGIC <ul>
# MAGIC <li>A <code>bright white</code> bag, which can hold your <code>shiny gold</code> bag directly.</li>
# MAGIC <li>A <code>muted yellow</code> bag, which can hold your <code>shiny gold</code> bag directly, plus some other bags.</li>
# MAGIC <li>A <code>dark orange</code> bag, which can hold <code>bright white</code> and <code>muted yellow</code> bags, either of which could then hold your <code>shiny gold</code> bag.</li>
# MAGIC <li>A <code>light red</code> bag, which can hold <code>bright white</code> and <code>muted yellow</code> bags, either of which could then hold your <code>shiny gold</code> bag.</li>
# MAGIC </ul>
# MAGIC <p>So, in this example, the number of bag colors that can eventually contain at least one <code>shiny gold</code> bag is <code><em>4</em></code>.</p>
# MAGIC <p><em>How many bag colors can eventually contain at least one <code>shiny gold</code> bag?</em> (The list of rules is quite long; make sure you get all of it.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '''pale chartreuse bags contain 3 faded orange bags.
drab gold bags contain 5 dark aqua bags.
mirrored magenta bags contain 3 dotted violet bags.
posh black bags contain 3 dark lavender bags, 3 mirrored coral bags, 1 dotted chartreuse bag.
striped yellow bags contain 5 pale red bags, 2 light lime bags, 5 clear indigo bags.
bright aqua bags contain 2 vibrant orange bags, 4 clear lavender bags, 1 pale gray bag.
dim silver bags contain 2 bright blue bags, 3 faded olive bags, 1 faded cyan bag.
light beige bags contain 2 bright silver bags, 4 vibrant crimson bags.
dull cyan bags contain 2 drab beige bags, 3 mirrored turquoise bags, 2 mirrored indigo bags.
dark black bags contain 5 dull turquoise bags, 4 faded cyan bags, 4 plaid coral bags.
dotted bronze bags contain 3 light blue bags, 2 dull teal bags, 3 dull chartreuse bags, 1 plaid green bag.
light purple bags contain 3 clear tan bags, 3 dull tan bags.
wavy orange bags contain 3 wavy tan bags, 3 faded green bags, 1 shiny brown bag, 2 dim tan bags.
drab beige bags contain 1 vibrant tan bag, 3 pale chartreuse bags, 3 plaid indigo bags, 2 mirrored chartreuse bags.
light coral bags contain 4 faded green bags, 1 pale crimson bag, 3 light bronze bags, 4 posh blue bags.
wavy coral bags contain 5 vibrant cyan bags, 5 light blue bags, 1 dotted turquoise bag.
dotted plum bags contain 1 clear orange bag, 2 drab black bags, 5 dull chartreuse bags, 5 plaid fuchsia bags.
striped olive bags contain 4 clear brown bags, 2 shiny beige bags.
vibrant maroon bags contain 2 dotted beige bags, 4 plaid olive bags, 5 dull black bags, 5 mirrored aqua bags.
drab purple bags contain 2 light green bags, 1 clear orange bag.
shiny violet bags contain 5 drab white bags, 5 dark aqua bags, 3 muted gray bags, 4 wavy orange bags.
muted maroon bags contain 2 plaid red bags, 3 bright silver bags, 5 posh yellow bags, 1 bright yellow bag.
clear black bags contain 1 bright plum bag, 1 faded brown bag, 4 wavy chartreuse bags.
dotted maroon bags contain 5 mirrored turquoise bags.
drab silver bags contain 2 vibrant violet bags, 2 muted orange bags, 4 dull purple bags.
faded purple bags contain 1 bright lime bag, 2 striped brown bags, 5 dull maroon bags, 2 shiny olive bags.
dull maroon bags contain 1 clear lime bag.
pale salmon bags contain 5 striped blue bags, 5 posh blue bags.
plaid orange bags contain 1 pale coral bag, 3 shiny orange bags.
drab black bags contain 5 vibrant orange bags, 1 dotted tomato bag, 2 dim red bags, 3 muted blue bags.
dotted teal bags contain 3 light fuchsia bags, 5 vibrant tan bags.
plaid tan bags contain 5 dark brown bags.
shiny coral bags contain 2 pale green bags, 1 muted lavender bag.
plaid plum bags contain 5 drab lavender bags, 2 shiny teal bags, 1 plaid tan bag.
dim olive bags contain 1 dark beige bag, 1 drab coral bag, 5 muted chartreuse bags, 4 bright teal bags.
dim bronze bags contain 1 striped turquoise bag, 4 muted turquoise bags.
muted red bags contain 5 dark gray bags, 4 muted gray bags, 5 muted blue bags.
shiny crimson bags contain 2 dark aqua bags, 4 faded fuchsia bags, 3 faded tomato bags.
vibrant teal bags contain 1 dark cyan bag, 4 wavy lime bags, 1 bright crimson bag.
dark yellow bags contain 2 striped coral bags, 1 drab tomato bag.
posh orange bags contain 3 wavy lime bags, 3 clear lavender bags, 5 bright indigo bags.
shiny orange bags contain 3 striped gold bags.
wavy magenta bags contain 2 vibrant crimson bags, 3 mirrored teal bags, 1 shiny lime bag.
clear indigo bags contain 2 pale green bags.
wavy red bags contain 5 plaid indigo bags.
wavy crimson bags contain 2 dim teal bags.
clear chartreuse bags contain 2 dull gray bags, 4 plaid lime bags, 3 striped cyan bags.
muted beige bags contain 2 drab white bags.
dim plum bags contain 3 vibrant green bags, 1 clear red bag.
dotted white bags contain 5 wavy magenta bags.
shiny chartreuse bags contain 2 striped tan bags, 2 dim maroon bags, 5 plaid bronze bags, 4 dark white bags.
pale green bags contain 5 drab crimson bags, 3 dull teal bags, 4 plaid red bags.
clear purple bags contain 3 light indigo bags.
striped brown bags contain 1 light yellow bag.
bright plum bags contain 4 faded olive bags, 2 dotted crimson bags, 3 pale green bags, 1 light yellow bag.
posh crimson bags contain 3 bright aqua bags.
dotted olive bags contain 4 striped tomato bags, 4 faded chartreuse bags, 2 dull bronze bags, 2 shiny olive bags.
striped magenta bags contain 2 posh indigo bags, 3 dotted tomato bags.
vibrant chartreuse bags contain 5 light crimson bags, 5 light bronze bags.
light cyan bags contain 1 faded red bag, 1 light silver bag.
faded teal bags contain 5 vibrant crimson bags, 3 drab gray bags, 5 striped turquoise bags, 1 pale plum bag.
mirrored aqua bags contain 1 vibrant white bag.
dull violet bags contain 2 dull orange bags, 1 light green bag.
clear orange bags contain 5 dark green bags.
muted silver bags contain 4 striped indigo bags, 3 mirrored lime bags, 1 bright lavender bag.
posh green bags contain 4 drab gold bags, 4 dim black bags, 4 faded gold bags.
dark bronze bags contain 1 faded plum bag, 5 mirrored teal bags, 5 striped indigo bags, 4 muted salmon bags.
shiny teal bags contain 4 plaid tomato bags, 3 clear brown bags, 4 dull silver bags, 2 wavy orange bags.
light gold bags contain 4 pale tan bags, 3 vibrant gray bags, 5 wavy tan bags, 5 dark violet bags.
bright indigo bags contain 5 shiny silver bags, 4 wavy indigo bags, 5 dark gold bags.
bright gray bags contain 5 shiny lime bags, 4 dull aqua bags.
dotted orange bags contain 1 dim red bag, 4 striped blue bags, 3 bright lavender bags.
dark indigo bags contain 4 drab indigo bags, 1 dotted turquoise bag.
pale lavender bags contain 2 vibrant green bags, 4 dim yellow bags, 1 mirrored yellow bag, 1 bright blue bag.
dotted silver bags contain 2 posh blue bags, 3 posh maroon bags.
plaid salmon bags contain 4 light yellow bags.
plaid magenta bags contain 3 striped gold bags, 2 mirrored black bags, 3 dull tan bags.
wavy blue bags contain 3 faded teal bags, 4 drab blue bags, 1 dotted gold bag.
muted black bags contain 1 drab teal bag, 3 muted lime bags.
clear violet bags contain 3 bright lavender bags, 1 vibrant plum bag, 3 wavy white bags, 1 shiny chartreuse bag.
bright teal bags contain 1 muted chartreuse bag, 4 dull indigo bags, 5 striped tomato bags, 1 drab white bag.
drab lime bags contain 3 posh maroon bags.
shiny tan bags contain 3 faded chartreuse bags, 3 wavy orange bags, 4 drab white bags, 4 light chartreuse bags.
light green bags contain 4 dotted tan bags, 1 dim salmon bag.
pale tan bags contain 3 posh green bags.
light gray bags contain 3 posh brown bags, 3 dim green bags, 3 mirrored tan bags, 1 mirrored yellow bag.
clear gray bags contain 4 dim brown bags.
drab magenta bags contain 4 dark aqua bags, 5 faded tomato bags.
pale violet bags contain 2 bright violet bags, 1 bright indigo bag, 2 muted salmon bags.
vibrant black bags contain 1 bright magenta bag, 4 vibrant crimson bags, 4 clear blue bags, 2 light chartreuse bags.
striped white bags contain 3 plaid yellow bags, 3 muted orange bags, 1 shiny gold bag, 5 light white bags.
wavy turquoise bags contain 5 wavy tan bags, 4 posh chartreuse bags, 5 posh red bags, 3 muted purple bags.
light white bags contain 3 shiny brown bags, 1 striped tan bag, 2 bright lime bags, 5 shiny yellow bags.
faded orange bags contain 3 dim silver bags, 5 wavy tomato bags, 4 wavy chartreuse bags, 1 shiny black bag.
mirrored fuchsia bags contain 2 plaid lime bags, 3 vibrant salmon bags.
dull aqua bags contain 5 clear brown bags, 3 dull indigo bags, 3 dull green bags, 2 muted gold bags.
dim gray bags contain 5 dark bronze bags, 4 dark silver bags, 3 wavy cyan bags.
dull tomato bags contain 4 drab tan bags, 3 striped brown bags.
dim gold bags contain 3 shiny tomato bags, 2 dim tomato bags.
striped beige bags contain 3 shiny violet bags, 3 striped aqua bags, 3 muted blue bags, 3 shiny gold bags.
mirrored coral bags contain 2 muted coral bags, 3 shiny teal bags.
vibrant white bags contain 1 clear brown bag, 3 drab gold bags, 2 wavy crimson bags, 5 light plum bags.
posh tan bags contain 3 dim salmon bags, 1 faded gold bag, 1 drab gray bag, 4 shiny coral bags.
drab tan bags contain 4 bright magenta bags, 3 dull green bags, 1 drab crimson bag, 4 dark green bags.
striped coral bags contain 2 drab tan bags, 4 wavy purple bags.
dark white bags contain 1 bright magenta bag.
striped red bags contain 3 plaid black bags.
drab coral bags contain 4 dotted violet bags, 2 pale magenta bags, 5 posh purple bags, 4 light lime bags.
pale yellow bags contain 5 plaid black bags, 3 shiny olive bags, 3 clear brown bags.
faded coral bags contain 2 pale salmon bags, 5 dim teal bags, 3 vibrant crimson bags.
faded black bags contain 2 wavy white bags, 5 faded brown bags, 4 drab beige bags.
dim salmon bags contain 4 vibrant white bags, 3 wavy salmon bags, 2 wavy lime bags, 2 bright purple bags.
dim black bags contain 3 dull tan bags, 2 striped beige bags, 2 plaid brown bags.
plaid cyan bags contain 2 muted coral bags, 3 dim red bags.
dotted gold bags contain 3 dotted orange bags, 3 striped coral bags, 1 clear magenta bag, 1 dotted crimson bag.
mirrored white bags contain 4 clear brown bags, 2 drab crimson bags, 4 shiny gold bags, 2 posh red bags.
vibrant olive bags contain 4 striped indigo bags, 5 dim salmon bags, 5 bright magenta bags.
dim teal bags contain 5 striped blue bags, 4 dull aqua bags, 5 dark cyan bags, 2 wavy magenta bags.
faded chartreuse bags contain no other bags.
clear yellow bags contain 5 wavy olive bags, 1 drab tomato bag, 2 plaid red bags.
mirrored bronze bags contain 1 vibrant beige bag, 5 clear cyan bags, 3 muted aqua bags, 5 striped turquoise bags.
vibrant tan bags contain 2 dull tomato bags, 5 dark aqua bags, 3 muted gray bags.
light olive bags contain 4 dark white bags, 2 dim teal bags.
light lavender bags contain 5 wavy indigo bags, 3 posh olive bags, 4 striped brown bags.
dotted gray bags contain 1 dim red bag, 5 light tomato bags, 2 dull gray bags, 4 light black bags.
plaid olive bags contain 5 wavy purple bags, 2 posh blue bags, 3 faded purple bags, 1 pale fuchsia bag.
muted salmon bags contain 5 shiny tan bags.
dark olive bags contain 4 mirrored black bags.
striped turquoise bags contain 4 pale olive bags, 2 pale tomato bags, 3 bright yellow bags.
plaid fuchsia bags contain 4 clear silver bags.
vibrant magenta bags contain 1 vibrant green bag, 2 muted silver bags, 4 light plum bags, 5 pale teal bags.
vibrant bronze bags contain 2 dull gold bags, 2 bright coral bags.
mirrored purple bags contain 1 drab tomato bag, 3 faded silver bags.
light lime bags contain 5 shiny violet bags, 4 wavy aqua bags.
pale gold bags contain 3 vibrant brown bags, 5 dim red bags.
dim orange bags contain 4 dark cyan bags, 3 light chartreuse bags, 3 wavy orange bags, 5 dark green bags.
clear fuchsia bags contain 4 posh blue bags, 4 mirrored lavender bags.
pale bronze bags contain 3 pale silver bags, 2 dotted tomato bags, 4 plaid gold bags.
dotted aqua bags contain 3 drab magenta bags, 3 dull green bags.
posh silver bags contain 5 striped lavender bags, 1 dotted maroon bag.
dim coral bags contain 1 wavy bronze bag, 5 striped gray bags, 2 light indigo bags, 2 dim orange bags.
bright green bags contain 5 drab plum bags.
striped teal bags contain 1 light fuchsia bag, 5 vibrant aqua bags, 3 mirrored white bags.
dim crimson bags contain 5 posh gray bags.
drab salmon bags contain 3 bright olive bags, 5 dim tan bags.
muted green bags contain 2 dark beige bags, 4 posh coral bags.
light tan bags contain 5 wavy white bags, 3 dim indigo bags, 3 bright green bags, 5 clear lavender bags.
posh teal bags contain 4 pale salmon bags.
muted cyan bags contain 4 posh yellow bags.
bright turquoise bags contain 3 posh indigo bags, 2 mirrored salmon bags, 2 dim magenta bags.
vibrant salmon bags contain 5 light tomato bags.
dark violet bags contain 3 light bronze bags, 5 dark gold bags, 1 striped magenta bag, 4 faded lavender bags.
faded maroon bags contain 5 plaid teal bags, 5 light turquoise bags, 5 posh white bags, 4 drab orange bags.
dotted magenta bags contain 4 shiny chartreuse bags, 5 drab turquoise bags, 4 bright tomato bags, 2 striped maroon bags.
dotted beige bags contain 5 clear white bags.
bright magenta bags contain no other bags.
dull red bags contain 2 muted lavender bags.
drab green bags contain 2 dotted cyan bags, 4 striped white bags, 3 muted magenta bags.
posh brown bags contain 5 muted lavender bags, 2 posh red bags, 5 drab magenta bags.
faded tan bags contain 3 bright purple bags, 5 plaid tomato bags, 3 dull teal bags.
faded brown bags contain 2 light silver bags, 5 mirrored tan bags, 2 clear tan bags, 2 drab gold bags.
striped black bags contain 3 vibrant yellow bags, 3 dull blue bags, 1 dull aqua bag, 5 dull teal bags.
faded white bags contain 1 muted maroon bag, 1 dark gray bag, 5 dark white bags.
drab aqua bags contain 3 muted white bags, 4 dark cyan bags, 5 pale tomato bags.
dull teal bags contain 2 plaid red bags, 5 mirrored teal bags.
vibrant plum bags contain 2 dim salmon bags, 3 light purple bags, 2 muted gray bags.
plaid crimson bags contain 5 shiny blue bags, 1 dull bronze bag.
wavy violet bags contain 3 dotted tomato bags, 3 striped brown bags.
clear cyan bags contain 1 drab crimson bag, 2 shiny lime bags.
shiny green bags contain 5 muted gray bags.
posh purple bags contain 2 vibrant white bags.
plaid lime bags contain 2 clear crimson bags, 3 bright magenta bags, 5 shiny silver bags, 1 posh blue bag.
dotted violet bags contain 1 dark teal bag, 5 faded crimson bags.
pale maroon bags contain 5 mirrored lime bags, 5 clear olive bags, 5 shiny orange bags, 4 mirrored fuchsia bags.
wavy indigo bags contain 5 plaid lime bags, 5 plaid fuchsia bags, 2 faded chartreuse bags, 4 dotted tomato bags.
faded silver bags contain 5 striped lavender bags, 4 muted lavender bags, 5 plaid brown bags.
drab violet bags contain 1 posh white bag.
bright white bags contain 3 light cyan bags, 1 dark indigo bag, 2 pale turquoise bags, 1 pale brown bag.
faded olive bags contain 2 clear lime bags, 4 muted chartreuse bags.
muted violet bags contain 1 clear lavender bag, 1 dark green bag, 3 dark cyan bags.
shiny gray bags contain 2 dull tan bags, 1 shiny olive bag.
plaid blue bags contain 3 dark aqua bags, 4 muted silver bags, 5 pale beige bags, 1 drab chartreuse bag.
posh fuchsia bags contain 5 posh red bags, 2 muted gray bags.
faded blue bags contain 1 plaid fuchsia bag, 1 mirrored turquoise bag, 2 plaid indigo bags, 1 dark aqua bag.
bright brown bags contain 4 drab violet bags, 5 shiny lime bags, 2 bright beige bags.
mirrored teal bags contain 5 dark gray bags.
bright violet bags contain 2 dotted crimson bags, 3 striped coral bags, 5 shiny maroon bags, 3 dull lavender bags.
striped plum bags contain 2 dim orange bags, 4 clear blue bags, 3 shiny violet bags.
plaid green bags contain 2 bright teal bags, 5 striped lime bags.
muted fuchsia bags contain 4 clear gold bags, 2 vibrant plum bags, 5 bright black bags.
bright purple bags contain 3 vibrant crimson bags, 1 dotted maroon bag, 4 dark gold bags.
faded cyan bags contain 4 dim teal bags.
wavy fuchsia bags contain 5 dull yellow bags, 2 light yellow bags, 5 bright black bags.
wavy salmon bags contain 1 shiny black bag, 3 bright teal bags, 5 clear yellow bags, 1 dull maroon bag.
dark fuchsia bags contain 1 muted violet bag, 3 light cyan bags.
clear salmon bags contain 4 light beige bags, 4 vibrant green bags, 3 pale yellow bags, 1 muted turquoise bag.
pale purple bags contain 1 bright blue bag, 5 pale bronze bags.
posh salmon bags contain 3 faded cyan bags, 4 posh maroon bags, 1 plaid green bag, 2 shiny silver bags.
bright blue bags contain 3 vibrant green bags, 2 drab gray bags.
shiny brown bags contain no other bags.
dark gold bags contain 5 vibrant aqua bags, 2 posh yellow bags.
mirrored violet bags contain 2 pale silver bags, 1 posh fuchsia bag.
bright fuchsia bags contain 3 muted brown bags, 3 plaid purple bags, 2 faded coral bags, 3 mirrored turquoise bags.
dim beige bags contain 2 dull lime bags, 3 dim gold bags, 3 plaid fuchsia bags, 1 posh yellow bag.
shiny white bags contain 1 pale fuchsia bag, 3 shiny beige bags, 3 posh aqua bags, 5 clear tan bags.
posh red bags contain 3 bright magenta bags, 2 dark aqua bags, 4 dark cyan bags.
vibrant fuchsia bags contain 3 striped indigo bags.
faded tomato bags contain 3 wavy olive bags, 5 shiny brown bags, 5 shiny tan bags.
dull purple bags contain 4 plaid teal bags, 4 dull indigo bags, 3 dull bronze bags, 4 faded tan bags.
shiny magenta bags contain 4 pale tomato bags, 4 shiny brown bags.
wavy tan bags contain no other bags.
dull salmon bags contain 3 faded crimson bags, 5 shiny fuchsia bags, 4 dotted silver bags.
pale magenta bags contain 2 faded chartreuse bags.
vibrant purple bags contain 3 muted orange bags, 5 dotted brown bags.
shiny turquoise bags contain 4 dotted turquoise bags, 1 dotted purple bag, 4 dim black bags.
shiny black bags contain 2 clear brown bags, 4 vibrant yellow bags, 1 vibrant aqua bag, 5 mirrored teal bags.
shiny cyan bags contain 3 dotted coral bags.
dim magenta bags contain 3 bright purple bags, 2 wavy white bags, 2 shiny fuchsia bags, 2 shiny yellow bags.
pale beige bags contain 3 dim orange bags, 5 wavy purple bags.
wavy bronze bags contain 5 posh yellow bags, 1 pale green bag, 5 dark cyan bags.
dull blue bags contain 4 wavy tan bags.
striped lime bags contain 5 striped crimson bags, 1 bright plum bag, 5 plaid yellow bags.
faded magenta bags contain 1 plaid green bag, 2 vibrant silver bags, 1 dim turquoise bag.
muted white bags contain 5 bright lime bags, 4 light fuchsia bags, 4 light violet bags, 4 dark aqua bags.
pale fuchsia bags contain 1 striped tomato bag, 1 drab crimson bag, 4 shiny yellow bags.
posh cyan bags contain 5 dark maroon bags.
dim indigo bags contain 3 dark gold bags, 5 bright maroon bags.
faded fuchsia bags contain 4 plaid tomato bags, 2 mirrored red bags.
shiny red bags contain 5 dull olive bags, 1 posh tan bag, 4 bright green bags.
posh maroon bags contain 4 clear blue bags, 5 muted chartreuse bags.
shiny indigo bags contain 4 wavy orange bags.
dim violet bags contain 1 dotted chartreuse bag, 2 mirrored lime bags, 1 drab chartreuse bag.
dim lime bags contain 4 posh fuchsia bags, 5 dull blue bags, 2 dull silver bags, 2 bright lime bags.
muted blue bags contain 5 mirrored lime bags.
dotted fuchsia bags contain 2 wavy magenta bags.
bright beige bags contain 1 mirrored maroon bag.
light bronze bags contain 1 posh maroon bag, 1 dotted maroon bag, 3 clear silver bags.
posh olive bags contain 2 wavy orange bags.
shiny salmon bags contain 2 light teal bags, 5 dark violet bags.
plaid tomato bags contain 5 shiny tan bags, 5 drab white bags.
striped blue bags contain 3 dark cyan bags, 2 pale magenta bags, 3 striped indigo bags.
bright lime bags contain 4 dark cyan bags.
vibrant crimson bags contain no other bags.
mirrored salmon bags contain 1 pale gray bag, 5 dark plum bags.
dim brown bags contain 4 faded fuchsia bags, 4 dull indigo bags.
clear aqua bags contain 1 mirrored black bag, 1 light bronze bag, 2 mirrored maroon bags, 4 mirrored white bags.
clear red bags contain 1 bright lavender bag.
dark maroon bags contain 1 light chartreuse bag.
bright silver bags contain 1 wavy tan bag, 3 plaid black bags, 2 dark gray bags.
faded lime bags contain 1 pale silver bag, 3 drab teal bags.
plaid lavender bags contain 1 plaid fuchsia bag.
faded yellow bags contain 4 dull blue bags.
dark blue bags contain 1 dotted red bag, 1 bright indigo bag, 2 posh tan bags.
light aqua bags contain 3 shiny olive bags, 2 dotted brown bags, 1 dull green bag.
striped gray bags contain 5 faded crimson bags, 4 clear white bags.
dark chartreuse bags contain 5 faded lime bags.
plaid chartreuse bags contain 3 shiny teal bags.
wavy gray bags contain 5 plaid lime bags, 5 wavy olive bags, 5 dim orange bags.
dull yellow bags contain 5 faded chartreuse bags, 2 clear crimson bags, 4 faded fuchsia bags.
muted magenta bags contain 4 mirrored teal bags, 3 drab silver bags, 3 drab lavender bags, 2 mirrored orange bags.
pale turquoise bags contain 3 bright lavender bags, 1 shiny tan bag, 4 posh teal bags, 2 posh cyan bags.
light turquoise bags contain 1 plaid gold bag.
pale brown bags contain 4 muted orange bags.
posh chartreuse bags contain 1 plaid lime bag, 4 shiny gray bags, 3 pale bronze bags, 3 vibrant bronze bags.
posh gray bags contain 3 dim salmon bags.
wavy tomato bags contain 3 vibrant salmon bags, 5 vibrant yellow bags, 2 vibrant green bags, 3 striped brown bags.
dotted indigo bags contain 5 shiny fuchsia bags, 1 posh lime bag, 1 muted beige bag.
pale lime bags contain 4 wavy fuchsia bags.
dull lime bags contain 2 light bronze bags, 3 light beige bags, 4 wavy tomato bags.
shiny olive bags contain 5 dull aqua bags, 5 muted gray bags, 5 posh olive bags.
muted teal bags contain 3 dull teal bags, 5 bright magenta bags.
dull white bags contain 5 striped yellow bags, 1 dim aqua bag.
shiny silver bags contain 4 shiny olive bags, 4 wavy orange bags, 2 mirrored red bags.
dim turquoise bags contain 4 drab gold bags.
clear brown bags contain no other bags.
mirrored olive bags contain 4 dim aqua bags.
striped purple bags contain 5 wavy tan bags.
faded violet bags contain 4 dull tan bags.
faded salmon bags contain 5 striped fuchsia bags, 1 muted lime bag.
mirrored yellow bags contain 2 dark orange bags.
wavy gold bags contain 2 muted salmon bags.
pale tomato bags contain 1 vibrant crimson bag, 5 light black bags, 3 dotted brown bags.
clear bronze bags contain 1 mirrored black bag, 3 wavy red bags, 4 faded white bags, 5 vibrant bronze bags.
mirrored silver bags contain 3 wavy salmon bags, 4 drab brown bags, 1 striped green bag, 4 mirrored lime bags.
dull bronze bags contain 1 dim orange bag, 1 light maroon bag, 5 wavy bronze bags, 2 posh blue bags.
posh lime bags contain 2 dark bronze bags.
light teal bags contain 4 dotted cyan bags, 4 dark crimson bags, 4 striped orange bags, 4 pale black bags.
dark lime bags contain 2 posh red bags.
vibrant yellow bags contain 4 dull indigo bags.
vibrant green bags contain 3 bright silver bags, 1 striped fuchsia bag, 5 dim tan bags.
mirrored lavender bags contain 1 dull maroon bag, 1 bright silver bag, 4 drab teal bags, 2 posh blue bags.
bright salmon bags contain 1 dark aqua bag.
clear green bags contain 3 vibrant blue bags, 4 dotted salmon bags, 5 striped violet bags.
clear lavender bags contain 2 faded silver bags, 5 dim tan bags, 4 drab white bags.
dim chartreuse bags contain 4 dark gray bags.
posh blue bags contain 1 clear silver bag, 5 clear crimson bags, 2 light beige bags.
dim maroon bags contain 5 dotted fuchsia bags.
muted crimson bags contain 1 dark cyan bag.
drab cyan bags contain 4 wavy brown bags.
faded lavender bags contain 3 posh coral bags, 2 dotted violet bags, 3 pale gray bags, 4 plaid beige bags.
dim aqua bags contain 5 dim tan bags, 3 posh olive bags.
posh magenta bags contain 3 bright orange bags, 4 bright salmon bags, 1 vibrant beige bag.
plaid purple bags contain 2 mirrored gray bags, 5 mirrored tan bags.
muted tomato bags contain 1 dotted tomato bag, 4 bright magenta bags, 1 striped turquoise bag.
dull black bags contain 5 wavy coral bags, 4 wavy beige bags, 1 drab lavender bag, 4 dark beige bags.
mirrored maroon bags contain 4 shiny teal bags, 3 light blue bags, 1 light aqua bag, 3 faded tan bags.
posh aqua bags contain 3 dotted orange bags, 4 wavy crimson bags, 5 pale magenta bags, 5 posh fuchsia bags.
muted lavender bags contain 4 faded green bags, 1 dark aqua bag, 4 posh maroon bags, 2 dark white bags.
posh tomato bags contain 2 posh black bags.
dull gold bags contain 1 faded turquoise bag, 4 drab brown bags, 4 shiny turquoise bags.
plaid violet bags contain 3 bright plum bags, 4 clear olive bags, 4 drab bronze bags.
pale silver bags contain 5 wavy olive bags, 5 dull indigo bags, 1 light plum bag, 4 dark gray bags.
dull brown bags contain 1 dim orange bag.
shiny beige bags contain 5 faded purple bags.
striped cyan bags contain 1 muted black bag, 4 dull aqua bags.
dotted green bags contain 4 wavy white bags, 2 shiny violet bags, 4 muted chartreuse bags.
dotted chartreuse bags contain 5 dull bronze bags.
plaid aqua bags contain 2 shiny indigo bags, 5 muted lavender bags, 3 light blue bags, 4 vibrant salmon bags.
mirrored beige bags contain 2 light white bags, 1 wavy coral bag.
light orange bags contain 3 drab salmon bags, 3 clear lavender bags, 4 dark beige bags, 1 clear purple bag.
dark tan bags contain 1 posh olive bag.
muted lime bags contain 3 faded chartreuse bags, 4 muted silver bags, 3 vibrant salmon bags, 1 mirrored blue bag.
posh gold bags contain 5 vibrant magenta bags.
faded beige bags contain 5 faded black bags, 4 clear coral bags, 4 bright olive bags, 1 faded lime bag.
vibrant turquoise bags contain 3 clear cyan bags, 1 dotted fuchsia bag.
faded bronze bags contain 4 posh teal bags, 3 plaid tomato bags, 4 dark bronze bags.
shiny blue bags contain 3 drab indigo bags, 1 dark lime bag.
plaid yellow bags contain 1 plaid lime bag.
shiny aqua bags contain 1 vibrant tomato bag, 4 dark aqua bags, 5 vibrant cyan bags, 4 striped coral bags.
mirrored indigo bags contain 5 vibrant turquoise bags.
wavy cyan bags contain 1 light yellow bag, 4 faded fuchsia bags, 2 clear silver bags, 3 vibrant fuchsia bags.
dull gray bags contain 2 mirrored turquoise bags, 2 posh yellow bags.
dim yellow bags contain 4 light silver bags.
striped crimson bags contain 3 dim salmon bags.
pale coral bags contain 4 vibrant violet bags, 4 posh teal bags, 3 drab aqua bags.
faded aqua bags contain 3 bright magenta bags, 4 muted aqua bags, 3 light salmon bags, 3 light black bags.
drab orange bags contain 2 drab purple bags, 5 light black bags, 5 dull blue bags, 1 bright purple bag.
drab bronze bags contain 3 clear violet bags, 3 drab crimson bags, 3 dotted yellow bags, 5 muted salmon bags.
drab blue bags contain 3 faded violet bags, 4 bright lavender bags, 2 vibrant cyan bags.
pale olive bags contain 4 shiny yellow bags, 1 dull yellow bag, 2 striped tomato bags.
light salmon bags contain 2 shiny gold bags, 2 light silver bags, 4 wavy magenta bags.
wavy brown bags contain 4 dim indigo bags, 3 pale olive bags, 3 mirrored orange bags.
vibrant beige bags contain 5 light lavender bags, 3 wavy bronze bags, 1 plaid yellow bag, 2 dark aqua bags.
clear tan bags contain 3 posh fuchsia bags, 1 pale fuchsia bag.
dotted turquoise bags contain 3 light maroon bags.
dull magenta bags contain 2 dark tomato bags.
dull chartreuse bags contain 5 light chartreuse bags, 2 dotted chartreuse bags.
bright red bags contain 1 dotted brown bag, 1 posh yellow bag, 5 light white bags, 4 shiny maroon bags.
bright bronze bags contain 4 bright salmon bags, 4 plaid bronze bags, 2 dim chartreuse bags.
vibrant gold bags contain 2 faded purple bags, 3 mirrored maroon bags, 3 dull gray bags.
vibrant cyan bags contain 2 faded olive bags, 4 dull silver bags, 3 mirrored lime bags, 4 faded red bags.
mirrored plum bags contain 3 dark orange bags, 5 plaid lavender bags, 5 dim red bags.
clear white bags contain 3 striped beige bags.
drab fuchsia bags contain 4 striped magenta bags, 2 vibrant violet bags, 4 pale aqua bags.
dark purple bags contain 5 striped violet bags.
mirrored tomato bags contain 5 drab olive bags.
dull olive bags contain 4 wavy purple bags.
wavy maroon bags contain 4 pale gold bags.
vibrant blue bags contain 1 faded lime bag, 4 light plum bags.
clear teal bags contain 4 dark green bags, 5 clear brown bags.
clear beige bags contain 4 shiny cyan bags, 3 striped salmon bags.
drab indigo bags contain 5 drab tan bags, 4 shiny black bags, 4 striped brown bags.
muted bronze bags contain 4 dark chartreuse bags, 5 pale crimson bags, 4 vibrant gold bags.
muted olive bags contain 3 wavy olive bags, 5 dark bronze bags, 4 bright aqua bags, 1 dotted yellow bag.
dull beige bags contain 1 dull purple bag.
dotted yellow bags contain 3 dim plum bags, 2 plaid lavender bags.
wavy lavender bags contain 1 vibrant violet bag, 4 posh blue bags, 1 posh plum bag.
dim fuchsia bags contain 5 pale yellow bags, 4 faded plum bags, 5 bright lime bags.
plaid gray bags contain 5 dark violet bags, 2 dotted crimson bags, 4 dull fuchsia bags, 1 drab magenta bag.
vibrant coral bags contain 2 shiny cyan bags, 4 pale magenta bags, 5 striped coral bags, 3 pale teal bags.
drab yellow bags contain 4 clear orange bags, 5 faded fuchsia bags.
dark red bags contain 5 mirrored maroon bags, 3 clear blue bags, 2 striped crimson bags, 2 dotted violet bags.
mirrored cyan bags contain 5 dotted maroon bags, 5 posh turquoise bags, 2 faded gray bags.
muted yellow bags contain 1 light cyan bag, 2 dim orange bags, 5 dull olive bags, 5 light green bags.
wavy aqua bags contain 2 muted cyan bags, 4 mirrored green bags, 5 muted tomato bags.
vibrant lavender bags contain 1 dotted gold bag, 1 light chartreuse bag, 3 mirrored gray bags.
bright black bags contain 1 striped lavender bag, 2 shiny tan bags, 4 bright lime bags.
wavy chartreuse bags contain 4 mirrored red bags.
dull turquoise bags contain 5 faded red bags, 1 light brown bag, 1 clear magenta bag.
dull silver bags contain 4 dark gray bags, 1 faded green bag.
pale black bags contain 1 plaid indigo bag, 3 light tomato bags, 4 drab blue bags.
clear tomato bags contain 1 dim tan bag, 1 clear lavender bag, 1 striped fuchsia bag, 5 clear orange bags.
dark cyan bags contain 4 shiny brown bags.
pale blue bags contain 1 clear green bag.
dotted lavender bags contain 3 dotted maroon bags, 5 wavy salmon bags, 2 pale tomato bags, 5 mirrored blue bags.
pale orange bags contain 4 pale silver bags, 4 striped lime bags.
drab chartreuse bags contain 2 dark gold bags, 5 clear crimson bags, 3 dull green bags.
striped violet bags contain 4 plaid lime bags.
muted gold bags contain no other bags.
mirrored gray bags contain 1 light green bag, 1 striped beige bag.
bright lavender bags contain 2 clear blue bags.
striped gold bags contain 3 muted turquoise bags.
dim white bags contain 1 vibrant lavender bag.
wavy beige bags contain 4 light chartreuse bags, 5 dark lime bags.
dim tomato bags contain 2 wavy aqua bags, 3 faded salmon bags.
light blue bags contain 2 wavy purple bags, 1 dull olive bag.
drab brown bags contain 5 drab magenta bags, 2 muted teal bags.
wavy olive bags contain 3 pale green bags, 5 muted gray bags.
bright chartreuse bags contain 1 clear yellow bag, 2 dotted olive bags, 1 posh olive bag.
posh violet bags contain 5 muted tomato bags, 5 light aqua bags, 3 pale cyan bags, 2 mirrored chartreuse bags.
dotted blue bags contain 4 plaid yellow bags, 3 vibrant bronze bags, 2 dull maroon bags, 3 shiny silver bags.
pale white bags contain 3 plaid brown bags, 2 mirrored aqua bags, 2 dim turquoise bags.
dull lavender bags contain 1 light blue bag, 5 drab tan bags, 3 light yellow bags.
pale cyan bags contain 5 pale green bags, 5 dull tomato bags, 4 vibrant orange bags.
mirrored tan bags contain 1 mirrored blue bag, 5 wavy purple bags.
plaid maroon bags contain 5 bright orange bags, 1 dull fuchsia bag, 5 dull indigo bags, 4 light white bags.
drab plum bags contain 5 pale silver bags, 1 clear yellow bag, 5 dotted fuchsia bags.
muted aqua bags contain 2 posh blue bags, 3 muted chartreuse bags, 1 drab tan bag, 3 dotted brown bags.
striped lavender bags contain 3 posh yellow bags, 5 drab white bags, 1 muted gold bag.
posh bronze bags contain 1 mirrored lime bag, 2 muted cyan bags, 3 muted aqua bags.
dotted brown bags contain 1 dotted orange bag, 3 striped blue bags, 3 dotted teal bags, 4 wavy magenta bags.
light chartreuse bags contain no other bags.
dotted purple bags contain 3 muted lavender bags.
vibrant violet bags contain 3 light violet bags.
dark green bags contain 3 mirrored teal bags, 3 bright magenta bags, 2 light chartreuse bags.
faded indigo bags contain 3 faded fuchsia bags, 4 dim magenta bags.
bright cyan bags contain 4 vibrant olive bags, 4 faded olive bags, 1 posh teal bag.
drab white bags contain no other bags.
clear magenta bags contain 1 dotted maroon bag, 2 wavy olive bags, 5 drab white bags.
light yellow bags contain 4 shiny brown bags, 4 light fuchsia bags, 1 mirrored turquoise bag, 2 drab teal bags.
dark beige bags contain 4 dim crimson bags, 5 mirrored turquoise bags, 3 posh yellow bags, 1 dull chartreuse bag.
dark teal bags contain 5 mirrored tan bags, 5 vibrant tomato bags, 2 bright violet bags, 2 striped silver bags.
pale plum bags contain 2 drab white bags.
light red bags contain 2 striped blue bags, 2 bright violet bags, 4 clear orange bags.
plaid brown bags contain 4 light maroon bags, 5 dull bronze bags, 3 plaid black bags.
plaid bronze bags contain 4 muted salmon bags, 1 light violet bag, 4 plaid black bags.
bright orange bags contain 5 light green bags, 2 wavy plum bags, 5 faded coral bags.
plaid black bags contain 5 dark green bags, 3 dull indigo bags, 3 dim tan bags.
shiny lime bags contain 5 bright lime bags.
shiny fuchsia bags contain 2 dotted tan bags, 3 drab white bags.
bright gold bags contain 1 drab magenta bag, 4 pale salmon bags.
shiny gold bags contain 1 drab white bag, 2 wavy purple bags, 2 muted gray bags, 5 clear crimson bags.
plaid beige bags contain 3 dotted yellow bags.
vibrant silver bags contain 2 muted gold bags, 5 dim teal bags, 4 mirrored white bags, 2 clear blue bags.
dotted black bags contain 1 wavy crimson bag, 5 vibrant purple bags.
mirrored brown bags contain 4 drab aqua bags, 4 dark teal bags, 5 striped plum bags.
dotted red bags contain 5 bright lime bags, 5 vibrant magenta bags, 1 striped turquoise bag.
bright tan bags contain 2 dull yellow bags, 2 posh tomato bags.
striped aqua bags contain 3 clear blue bags, 1 dark maroon bag.
dotted coral bags contain 1 vibrant silver bag, 3 dark green bags, 4 posh gray bags, 2 light red bags.
mirrored lime bags contain 3 mirrored white bags, 1 plaid tomato bag, 2 shiny yellow bags, 2 vibrant black bags.
dark gray bags contain 3 faded green bags, 3 vibrant crimson bags.
wavy lime bags contain 5 wavy salmon bags, 2 faded tomato bags.
dotted lime bags contain 5 drab brown bags, 1 faded salmon bag, 2 wavy violet bags, 4 posh olive bags.
light black bags contain 5 striped indigo bags.
shiny yellow bags contain 5 wavy tan bags, 5 drab white bags, 4 posh olive bags.
bright yellow bags contain 3 posh red bags, 2 plaid black bags.
dull tan bags contain 4 clear brown bags, 3 wavy tan bags.
shiny tomato bags contain 2 shiny orange bags, 4 light lavender bags, 1 plaid lavender bag.
vibrant aqua bags contain 5 pale green bags, 3 drab crimson bags, 2 shiny brown bags.
striped salmon bags contain 2 posh orange bags.
light silver bags contain 1 shiny yellow bag, 4 mirrored turquoise bags, 1 bright coral bag, 2 posh maroon bags.
striped fuchsia bags contain 3 drab white bags, 3 faded chartreuse bags, 4 vibrant black bags, 3 wavy tan bags.
bright tomato bags contain 3 light beige bags, 4 drab teal bags.
shiny plum bags contain 4 clear bronze bags.
vibrant red bags contain 3 bright magenta bags.
mirrored orange bags contain 2 mirrored white bags, 3 dotted brown bags, 3 bright silver bags, 4 pale teal bags.
dull indigo bags contain no other bags.
wavy yellow bags contain 4 wavy white bags.
muted turquoise bags contain 2 posh red bags, 3 dark green bags, 4 mirrored white bags.
striped indigo bags contain 3 dark cyan bags, 5 clear blue bags, 2 faded chartreuse bags.
mirrored green bags contain 4 mirrored chartreuse bags, 3 striped red bags.
plaid white bags contain 1 vibrant salmon bag, 1 dark yellow bag, 2 vibrant violet bags.
dark plum bags contain 4 muted coral bags, 4 mirrored blue bags, 1 vibrant aqua bag.
drab turquoise bags contain 1 dotted purple bag, 1 light plum bag.
light maroon bags contain 2 wavy purple bags, 2 dim orange bags, 1 mirrored white bag, 3 striped tomato bags.
shiny maroon bags contain 2 bright blue bags.
drab crimson bags contain 1 bright magenta bag, 3 drab white bags.
dark aqua bags contain 3 shiny brown bags, 5 dark gray bags.
posh turquoise bags contain 2 shiny gray bags.
muted indigo bags contain 4 wavy purple bags.
dotted salmon bags contain 1 vibrant violet bag, 1 mirrored lavender bag.
plaid indigo bags contain 2 wavy indigo bags, 2 dark white bags, 3 wavy tan bags, 3 vibrant crimson bags.
muted brown bags contain 3 posh yellow bags, 4 shiny lime bags, 5 striped lavender bags.
vibrant gray bags contain 1 mirrored silver bag, 2 light coral bags, 1 faded gold bag, 1 dull fuchsia bag.
drab tomato bags contain 1 wavy tan bag, 1 shiny tan bag, 1 clear crimson bag.
wavy white bags contain 3 muted blue bags, 2 wavy plum bags, 4 dim silver bags, 3 mirrored tan bags.
shiny lavender bags contain 1 posh coral bag, 2 dotted crimson bags, 2 plaid red bags, 1 striped silver bag.
dull fuchsia bags contain 4 light bronze bags, 3 clear gray bags, 1 bright coral bag.
drab teal bags contain 5 muted chartreuse bags, 4 dull silver bags, 5 vibrant black bags, 3 shiny olive bags.
clear crimson bags contain 4 clear brown bags, 3 drab crimson bags, 4 clear blue bags, 1 vibrant black bag.
posh beige bags contain 5 plaid teal bags.
clear silver bags contain 3 plaid tomato bags, 3 bright silver bags, 1 mirrored white bag.
mirrored red bags contain 2 striped indigo bags, 2 drab teal bags.
posh indigo bags contain 3 faded red bags.
dark silver bags contain 5 wavy tan bags, 2 dotted maroon bags.
drab red bags contain 2 dotted chartreuse bags, 3 mirrored tan bags, 5 pale plum bags.
plaid turquoise bags contain 4 dim silver bags, 1 bright orange bag.
dim blue bags contain 1 muted lavender bag, 1 wavy plum bag.
plaid coral bags contain 2 shiny coral bags.
striped silver bags contain 2 muted brown bags.
vibrant tomato bags contain 1 muted black bag.
dark turquoise bags contain 2 light silver bags.
vibrant lime bags contain 2 light beige bags, 3 bright green bags, 5 faded purple bags.
mirrored chartreuse bags contain 2 wavy tan bags, 5 dim tan bags.
light plum bags contain 5 faded green bags.
dim tan bags contain 1 faded chartreuse bag, 2 clear brown bags, 1 faded green bag, 2 muted gold bags.
shiny bronze bags contain 5 drab aqua bags.
dotted tomato bags contain 4 wavy magenta bags.
mirrored crimson bags contain 1 dim bronze bag.
light crimson bags contain 3 posh red bags.
dull coral bags contain 3 striped crimson bags, 4 mirrored salmon bags.
drab lavender bags contain 3 dim salmon bags.
dotted crimson bags contain 3 dark cyan bags, 4 posh blue bags, 2 light fuchsia bags.
dotted tan bags contain 2 posh fuchsia bags, 4 dim black bags.
dark coral bags contain 2 mirrored green bags, 4 shiny white bags, 2 shiny tomato bags.
striped orange bags contain 1 muted violet bag, 5 pale cyan bags, 2 drab tomato bags, 3 faded violet bags.
pale aqua bags contain 3 shiny fuchsia bags, 4 shiny violet bags.
wavy plum bags contain 4 light chartreuse bags, 5 vibrant tan bags, 4 muted lime bags.
mirrored turquoise bags contain 4 shiny brown bags, 4 drab tan bags.
dark magenta bags contain 5 faded violet bags, 2 posh lavender bags.
striped bronze bags contain 3 light silver bags, 3 mirrored brown bags, 3 posh purple bags, 4 drab turquoise bags.
faded red bags contain 2 dark cyan bags, 2 striped tan bags, 4 mirrored violet bags.
faded turquoise bags contain 1 striped crimson bag.
clear gold bags contain 3 clear crimson bags, 5 faded green bags, 4 dim tan bags.
clear coral bags contain 3 striped salmon bags.
faded gray bags contain 4 light salmon bags, 5 clear orange bags, 1 dim yellow bag, 2 wavy green bags.
posh lavender bags contain 2 clear silver bags, 1 wavy indigo bag, 4 faded brown bags, 2 light white bags.
pale red bags contain 3 clear orange bags.
dim lavender bags contain 1 posh silver bag.
vibrant orange bags contain 2 pale magenta bags.
pale gray bags contain 2 dark aqua bags, 2 mirrored turquoise bags, 2 striped fuchsia bags, 5 wavy purple bags.
pale teal bags contain 2 striped brown bags, 4 shiny brown bags.
muted tan bags contain 3 dotted purple bags, 5 clear blue bags, 5 bright plum bags.
dotted cyan bags contain 1 mirrored chartreuse bag, 2 dotted gray bags, 5 pale tomato bags, 1 mirrored lime bag.
dark brown bags contain 4 vibrant orange bags, 3 faded olive bags, 5 posh blue bags.
dull orange bags contain 5 posh coral bags, 5 vibrant green bags, 3 dull maroon bags, 1 striped tomato bag.
plaid silver bags contain 1 muted turquoise bag, 1 wavy green bag.
dull crimson bags contain 4 faded red bags, 1 dotted plum bag, 2 plaid orange bags, 1 posh yellow bag.
muted orange bags contain 4 pale yellow bags, 1 dark maroon bag, 5 mirrored white bags.
wavy black bags contain 4 mirrored blue bags, 4 drab chartreuse bags, 4 dull aqua bags.
light magenta bags contain 2 muted coral bags, 3 wavy violet bags.
faded crimson bags contain 2 dim orange bags, 3 vibrant crimson bags, 4 clear lime bags, 5 wavy olive bags.
light fuchsia bags contain 2 dull green bags, 4 dull indigo bags.
mirrored black bags contain 1 wavy magenta bag, 3 light bronze bags, 3 dull teal bags.
striped tan bags contain 5 vibrant yellow bags, 3 dull silver bags, 5 mirrored teal bags.
dark crimson bags contain 1 mirrored teal bag, 2 muted maroon bags, 5 dull green bags.
light indigo bags contain 5 dotted purple bags.
light brown bags contain 4 dark fuchsia bags, 1 bright olive bag.
wavy purple bags contain 3 vibrant black bags, 5 dull teal bags, 1 bright magenta bag.
posh white bags contain 5 muted purple bags, 5 drab silver bags.
faded gold bags contain 2 dull teal bags, 5 muted orange bags, 3 mirrored lavender bags, 2 clear orange bags.
clear maroon bags contain 2 dim crimson bags, 3 dim maroon bags, 5 wavy salmon bags, 5 mirrored black bags.
bright maroon bags contain 5 dark bronze bags, 4 pale coral bags.
clear turquoise bags contain 1 muted gold bag.
bright coral bags contain 3 striped lavender bags, 4 drab tomato bags, 1 bright lime bag.
wavy teal bags contain 3 faded tan bags.
mirrored gold bags contain 4 faded violet bags.
dark orange bags contain 5 muted purple bags, 1 drab turquoise bag, 5 pale beige bags.
dull green bags contain 1 faded chartreuse bag.
posh plum bags contain 1 dull turquoise bag.
plaid red bags contain 4 wavy orange bags.
faded green bags contain 2 wavy tan bags, 2 muted gold bags.
drab maroon bags contain 5 striped fuchsia bags, 5 light indigo bags.
clear blue bags contain 5 bright magenta bags, 2 muted gold bags, 1 faded chartreuse bag.
shiny purple bags contain 3 mirrored lavender bags, 3 light crimson bags, 2 light turquoise bags, 1 drab aqua bag.
wavy silver bags contain 5 mirrored tan bags, 2 dotted crimson bags, 3 pale magenta bags, 5 vibrant plum bags.
drab gray bags contain 4 mirrored red bags, 4 plaid yellow bags, 4 muted silver bags, 3 light black bags.
striped maroon bags contain 5 dull teal bags, 1 bright indigo bag, 3 clear gray bags.
striped tomato bags contain 2 clear gold bags, 4 plaid red bags, 1 vibrant yellow bag, 2 dark aqua bags.
vibrant brown bags contain 4 vibrant orange bags.
wavy green bags contain 5 striped coral bags, 5 clear brown bags, 4 drab gold bags, 3 faded green bags.
dark tomato bags contain 3 wavy gray bags, 4 clear yellow bags, 4 light fuchsia bags, 1 drab plum bag.
plaid gold bags contain 3 faded red bags.
light tomato bags contain 1 striped black bag.
clear olive bags contain 2 drab lime bags.
dim red bags contain 4 light yellow bags, 5 vibrant yellow bags, 3 dark green bags, 2 vibrant aqua bags.
vibrant indigo bags contain 1 vibrant silver bag.
pale crimson bags contain 4 wavy green bags, 1 striped fuchsia bag, 4 posh indigo bags.
clear lime bags contain 1 wavy tan bag.
muted gray bags contain 1 faded green bag, 2 dull silver bags, 4 drab crimson bags.
striped chartreuse bags contain 2 vibrant silver bags, 2 shiny tan bags, 3 muted silver bags, 2 shiny maroon bags.
muted coral bags contain 5 dark maroon bags, 1 clear lavender bag, 4 bright teal bags, 4 faded cyan bags.
posh coral bags contain 2 clear brown bags.
bright crimson bags contain 2 vibrant salmon bags.
muted plum bags contain 1 pale silver bag.
dull plum bags contain 2 shiny cyan bags, 3 faded salmon bags.
bright olive bags contain 3 dim brown bags, 5 dark brown bags, 1 muted white bag.
clear plum bags contain 5 clear chartreuse bags, 5 striped aqua bags.
muted chartreuse bags contain 1 faded crimson bag, 1 dark cyan bag.
muted purple bags contain 1 bright plum bag, 2 light olive bags, 2 striped red bags, 4 pale magenta bags.
posh yellow bags contain 4 wavy purple bags, 3 dark green bags, 3 striped tomato bags, 3 light chartreuse bags.
light violet bags contain 5 plaid black bags, 1 muted brown bag, 1 vibrant aqua bag.
drab olive bags contain 1 dim brown bag, 2 dull blue bags.
pale indigo bags contain 3 dark magenta bags, 2 dull blue bags.
mirrored blue bags contain 5 clear crimson bags, 1 clear orange bag, 3 drab tomato bags.
striped green bags contain 2 shiny black bags, 4 dotted chartreuse bags, 4 wavy white bags.
plaid teal bags contain 4 dark green bags, 5 muted chartreuse bags, 5 vibrant aqua bags, 4 dotted olive bags.
faded plum bags contain 2 drab white bags, 4 light blue bags, 2 clear lavender bags, 3 vibrant white bags.
dim green bags contain 2 faded green bags, 2 bright magenta bags.
dark lavender bags contain 2 muted lime bags, 2 faded tomato bags, 5 wavy purple bags, 3 light olive bags.
dim purple bags contain 4 dotted plum bags.
dark salmon bags contain 1 dull violet bag, 3 bright indigo bags.
dim cyan bags contain 5 dim crimson bags, 2 clear brown bags, 1 muted brown bag, 4 light silver bags.'''

# COMMAND ----------

import re

rules = {}
for line in inp.splitlines():
  bag, text = line.split(' bags contain ')
  contains = {}
  for s in text.split(', '):
    if s == 'no other bags.':
      break
    d, name = re.findall(r'(\d+) (.+) bags?\.?', s)[0]
    contains[name] = int(d)
  rules[bag] = contains


def contains_shiny_gold(bag):
  for b2 in rules[bag]:
    if b2 == 'shiny gold' or contains_shiny_gold(b2):
      return True
  return False


answer = sum(contains_shiny_gold(bag) for bag in rules)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!</p>
# MAGIC <p>Consider again your <code>shiny gold</code> bag and the rules from the above example:</p>
# MAGIC <ul>
# MAGIC <li><code>faded blue</code> bags contain <code>0</code> other bags.</li>
# MAGIC <li><code>dotted black</code> bags contain <code>0</code> other bags.</li>
# MAGIC <li><code>vibrant plum</code> bags contain <code>11</code> other bags: 5 <code>faded blue</code> bags and 6 <code>dotted black</code> bags.</li>
# MAGIC <li><code>dark olive</code> bags contain <code>7</code> other bags: 3 <code>faded blue</code> bags and 4 <code>dotted black</code> bags.</li>
# MAGIC </ul>
# MAGIC <p>So, a single <code>shiny gold</code> bag must contain 1 <code>dark olive</code> bag (and the 7 bags within it) plus 2 <code>vibrant plum</code> bags (and the 11 bags within <em>each</em> of those): <code>1 + 1*7 + 2 + 2*11</code> = <code><em>32</em></code> bags!</p>
# MAGIC <p>Of course, the actual rules have a <span title="100%">small</span> chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!</p>
# MAGIC <p>Here's another example:</p>
# MAGIC <pre><code>shiny gold bags contain 2 dark red bags.
# MAGIC dark red bags contain 2 dark orange bags.
# MAGIC dark orange bags contain 2 dark yellow bags.
# MAGIC dark yellow bags contain 2 dark green bags.
# MAGIC dark green bags contain 2 dark blue bags.
# MAGIC dark blue bags contain 2 dark violet bags.
# MAGIC dark violet bags contain no other bags.
# MAGIC </code></pre>
# MAGIC <p>In this example, a single <code>shiny gold</code> bag must contain <code><em>126</em></code> other bags.</p>
# MAGIC <p><em>How many individual bags are required inside your single <code>shiny gold</code> bag?</em></p>
# MAGIC </article>

# COMMAND ----------

import functools

@functools.cache
def count_bags(bag):
  n_bags = 0
  for b2 in rules[bag]:
    n = rules[bag][b2]
    n_bags += n + n * count_bags(b2)
  return n_bags

answer = count_bags('shiny gold')
print(answer)
