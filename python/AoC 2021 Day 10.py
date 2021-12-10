# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 10: Syntax Scoring ---</h2><p>You ask the submarine to determine the best route out of the deep-sea cave, but it only replies:</p>
# MAGIC <pre><code>Syntax error in navigation subsystem on line: <span title="Some days, that's just how it is.">all of them</span></code></pre>
# MAGIC <p><em>All of them?!</em> The damage is worse than you thought. You bring up a copy of the navigation subsystem (your puzzle input).</p>
# MAGIC <p>The navigation subsystem syntax is made of several lines containing <em>chunks</em>. There are one or more chunks on each line, and chunks contain zero or more other chunks. Adjacent chunks are not separated by any delimiter; if one chunk stops, the next chunk (if any) can immediately start. Every chunk must <em>open</em> and <em>close</em> with one of four legal pairs of matching characters:</p>
# MAGIC <ul>
# MAGIC <li>If a chunk opens with <code>(</code>, it must close with <code>)</code>.</li>
# MAGIC <li>If a chunk opens with <code>[</code>, it must close with <code>]</code>.</li>
# MAGIC <li>If a chunk opens with <code>{</code>, it must close with <code>}</code>.</li>
# MAGIC <li>If a chunk opens with <code>&lt;</code>, it must close with <code>&gt;</code>.</li>
# MAGIC </ul>
# MAGIC <p>So, <code>()</code> is a legal chunk that contains no other chunks, as is <code>[]</code>. More complex but valid chunks include <code>([])</code>, <code>{()()()}</code>, <code>&lt;([{}])&gt;</code>, <code>[&lt;&gt;({}){}[([])&lt;&gt;]]</code>, and even <code>(((((((((())))))))))</code>.</p>
# MAGIC <p>Some lines are <em>incomplete</em>, but others are <em>corrupted</em>. Find and discard the corrupted lines first.</p>
# MAGIC <p>A corrupted line is one where a chunk <em>closes with the wrong character</em> - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.</p>
# MAGIC <p>Examples of corrupted chunks include <code>(]</code>, <code>{()()()&gt;</code>, <code>(((()))}</code>, and <code>&lt;([]){()}[{}])</code>. Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.</p>
# MAGIC <p>For example, consider the following navigation subsystem:</p>
# MAGIC <pre><code>[({(&lt;(())[]&gt;[[{[]{&lt;()&lt;&gt;&gt;
# MAGIC [(()[&lt;&gt;])]({[&lt;{&lt;&lt;[]&gt;&gt;(
# MAGIC {([(&lt;{}[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt;
# MAGIC (((({&lt;&gt;}&lt;{&lt;{&lt;&gt;}{[]{[]{}
# MAGIC [[&lt;[([]))&lt;([[{}[[()]]]
# MAGIC [{[{({}]{}}([{[{{{}}([]
# MAGIC {&lt;[[]]&gt;}&lt;{[{[{[]{()[[[]
# MAGIC [&lt;(&lt;(&lt;(&lt;{}))&gt;&lt;([]([]()
# MAGIC &lt;{([([[(&lt;&gt;()){}]&gt;(&lt;&lt;{{
# MAGIC &lt;{([{{}}[&lt;[[[&lt;&gt;{}]]]&gt;[]]
# MAGIC </code></pre>
# MAGIC <p>Some of the lines aren't corrupted, just incomplete; you can ignore these lines for now. The remaining five lines are corrupted:</p>
# MAGIC <ul>
# MAGIC <li><code>{([(&lt;{}[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt;</code> - Expected <code>]</code>, but found <code>}</code> instead.</li>
# MAGIC <li><code>[[&lt;[([]))&lt;([[{}[[()]]]</code> - Expected <code>]</code>, but found <code>)</code> instead.</li>
# MAGIC <li><code>[{[{({}]{}}([{[{{{}}([]</code> - Expected <code>)</code>, but found <code>]</code> instead.</li>
# MAGIC <li><code>[&lt;(&lt;(&lt;(&lt;{}))&gt;&lt;([]([]()</code> - Expected <code>&gt;</code>, but found <code>)</code> instead.</li>
# MAGIC <li><code>&lt;{([([[(&lt;&gt;()){}]&gt;(&lt;&lt;{{</code> - Expected <code>]</code>, but found <code>&gt;</code> instead.</li>
# MAGIC </ul>
# MAGIC <p>Stop at the first incorrect closing character on each corrupted line.</p>
# MAGIC <p>Did you know that syntax checkers actually have contests to see who can get the high score for syntax errors in a file? It's true! To calculate the syntax error score for a line, take the <em>first illegal character</em> on the line and look it up in the following table:</p>
# MAGIC <ul>
# MAGIC <li><code>)</code>: <code>3</code> points.</li>
# MAGIC <li><code>]</code>: <code>57</code> points.</li>
# MAGIC <li><code>}</code>: <code>1197</code> points.</li>
# MAGIC <li><code>&gt;</code>: <code>25137</code> points.</li>
# MAGIC </ul>
# MAGIC <p>In the above example, an illegal <code>)</code> was found twice (<code>2*3 = <em>6</em></code> points), an illegal <code>]</code> was found once (<code><em>57</em></code> points), an illegal <code>}</code> was found once (<code><em>1197</em></code> points), and an illegal <code>&gt;</code> was found once (<code><em>25137</em></code> points). So, the total syntax error score for this file is <code>6+57+1197+25137 = <em>26397</em></code> points!</p>
# MAGIC <p>Find the first illegal character in each corrupted line of the navigation subsystem. <em>What is the total syntax error score for those errors?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''[[{(<({[(([[([()<>][()<>])]][<{[[]<>]}<<[]{}>>>])[({<[{}[]]<{}<>>><{()[]}[{}[]]>}<<(<>[])[[]{}]>{(<
{{{[[<{<{({({(<>{})}<(()[])([]<>)>)})(<[([{}()]([]{}))[([][])([]<>)]]((<{}<>>[[]{}])({<>()}{()}))>
[(<<[(<[[[<{(([]{})){<{}{}>{()<>}})><(<[()()][<>]>([[]]))[(([]<>)(<><>))((<>)({}[]))]>]{<<{{()[]}<[]<>>}
{{({{{([<((<[[<>[]](<>[])]><<(()<>)<<><>>>{(()<>)(<>{})}>))>]({(([{{()()}>{{{}{}}{<><>}}]{({()<>
<<{(<<{<<{([{{(){}}{()()}}{<[]{}>(<>{}))][({<>{}}[[]<>])<{{}{}}{{}()}>])[<<{{}{}}[()[]]>{{
[[<{[<((<[[{{{{}{}}{{}[]}}}[[<{}<>>]]]({<([][]){{}<>}>((()<>)<<>[]>)})]><[({{<{}()>{()()}}})]{(<({[]{}}[{
<<[{([[[[[<{[([]())({}[])]{[{}[]]}}<(<[]{}>({}{})){{[]<>}[()]}>>{(<{[]}[<>[]]>)}][(([[{}[]]<[]
[(<[<{{((<{<[<{}[]>[<>{}]][<{}<>>]><<({}[])[[]<>]>}}>)<(([{<{}<>>(()[])}[[{}()]([])]]<<{<>()}({}{})>
<{{[[<(<<<([({{}())([]{})){<()<>>{<>{}}}]<{[[]{}][[]<>]}{<{}()>{[]()}}>)<<{(<>())[<><>]}[{{}[]}(<>(
{{{{<{{<{<<[[[{}()]<[][])]<{(){}}{[]{}}>][{<[]()>{<>{}}}]>><{(<<<>[]>{(){}}>{{[]()}[<><>]}){(<{}()>){[[][]](
{(<{{([[(<{[((()<>){()()})<[<>{}]{()}>]<{[()[]]}>}([{<()>{{}[]}}[([][]){()[]}]]{{<<>[]>}{([]{}){<><>}}})
[(((({[{<<{[{([]())(<>[])}[<{}()>{()()}]]}>>[<[[{{{}()}{()<>}}(<()<>>[{}[]])]{[({}<>)<<>>]}]<({<<><>
<([[[((<[<<((<[][]>))<<{[][]}>>>{<([()()>)>}><([[[()[]]({}())]({<>{}}{()[]})]{{{<><>}[[]()]}[[[]
(((<({([[({{({[][]})(({}())[()<>])}(<[[][]]>(<{}>[<>{}]))})](<{((<<><>>[()()]){<[]<>>[[]<>]})}([<
[[{[[{[[{[{{[<{}()><()[]>]}}]<<{{<<><>>{{}{}}}[(<>{})(()())]}[{([]<>)[{}()]}<[[]][()()]>]><<{{[]{}}
((<<((<(<[{[({()<>}{()()}){<{}{}>}]}[{<[<>()][[]()]>}]]{[{[<()>{[]{}}]}<{[{}{}}}[([]{})(<><>)]>](({(<>{})
[[<[<({[[<<{[[()()]{(){}}]<[{}<>](()())>>(<[()[]][[]()]>)>[{(([][])([]{}))}[<<<><>><()<>>>(<<>[]>)]
[({(<{(<{[{[{([]){{}{}}}(<[][]>(<>[]))](<{<>[]}<[]()>>{<()><{}>})}{[([<>{}]{[]()})[(<>{})<[]()>]][{[()<>
[[<<{[(<({(((([]{})[[][]])<<{}{}>{[]()}>))})<[(<<(<>[])<[]()>><((){})[()<>]>>{<({}[])>{<<>{}>{(){}}}}
<<([[({(<{<[[({}()){()[]}]]>((<<()[]>(<>{})>(([]())))(((()<>)({}[]))))}>{<{((([])<()[]>)<({}())<()<
<<({[<{<({{{{[()()]<<>[]>}[{{}<>}[()()]]}{(([]()))})})[[[{[<<>[]>[<>()]]<{[]{}}[<>{}]>}]([{{[][]}{
{((((([[([<{([<>{}]<{}[]>){({}())[{}[]]}}{(<()()>({}[]))<{<><>}(<>[])>}>([<{()<>}[()[]]><[()<>]>]{[{
{[((((({<[{<{[(){}][[]()]}[({}[])]>{[[<>{}]{{}}]{[<>[]]<<>[]>}}}({[([]{})]{[[]<>]<[]{}>}}(<(()[])[{}()]
((<<{<{{{<(<<[<>()]{{}<>}>({<>{}}[[]()])>(<<{}<>>({}<>)><[{}<>]{(){}}>))<(((()[])([]())){(<
{(<(<([{{{((([<>[]]([]<>))({<>[]}<<>[]>)}{<(<><>)<<>{}>>(({}[])(()<>))}){[{{{}{}}}]{[<{}()>(<>{})][{[]}]}
{{{([([(<[<[{<()>{()()}}<[()()]<<><>>>]{<<()<>>>(((){}){()<>})}>{<{({}[])<<><>>}((()())<{}{}>)>
{(({(<<([[({<{[][]}<<><>>>}(<({}<>){{}<>}>{<<><>>(<>())}))<{{[{}<>]<[]()>}<<{}{}>>}[{<{}[]><(){}>}{
[[[([[(([<[<{<<>{}><{}[]>}>((<[][]>[{}[]]))]{({<<><>>[()[])}[{{}()}<{}>])}>]){[{{((<<>{}>([]<>))([
([<<<[(<(<{[[({}{}](<>)]{{{}<>}({}{})}][({()}{[]()})[({})]]}{<[(<><>)({}{})]<{<>}{[]}>>}>)>){{<[(<{(()()
{{{<{(<(([<<<{{}[]}[<>{}]}>([<<>()>{<>()}]<<<><>>[{}<>]>)>{[([<>()]{()[]}){{<>{}}[<>[]]}]}][(<[(()
<<<[[{(([<<{{(()())[{}[]]}{[[]<>]<<>>}}[(<<>><{}<>>){{{}[]}[{}()])]>([(<{}()>[[]()])[(()())
{{{([[[<{(<<{[[]()](<>{})})[(<[]{}><[]{}>)[<[]{}>{{}()}]]>[[[(()()){{}{}}][[<>[]](())]]<([{}()][{
([{{([[[({[(((<>)(()<>)){[{}{}](()())}){(((){})([]()))[(<>{})<[][]>]}]([({[]()}[(){}])<[{}()>(()<>)>
[[[<<(({<<(([({}[])<(){}>][[{}]([]())])<{{[]()}[[]]><{<><>}<()[]>>>)>{<{<[[][]]<{}<>>>([[]<>]{{}<
[[[<[<([{<[{{{()<>}({}<>)}}(<{{}<>}{[]()}>[<()())(<>())])]>[[(<{()}<[]()>><[()[]]<<>{}>>){<[()<
{{(<({((<[<<[([][])<[]<>>](<<>[]>)>>{<([(){}]{[]{}})>{[({}<>)]<[(){}]{{}}}}}]>)[[[[<{<[][]>(
[[[[{{{{([(((({}<>){()()})[{()()}([]<>)])[{<{}{}><[]{}>}([()<>][[]()])])]))}(<[[[{[[()[]]<()[]>]}]{((
({{[(((([<({{(<>())<{}()>}([{}{}]<{}{}>)}[{[{}{}]}<[[]]<()[]>>])[([<{}{}><[]{}>])<<[(){}]({}{}
(<<({<({[({[{{()[]}[()<>]}<{<>{}}({}{})>](<{<>{}}>[{{}<>}{(){}}])})(({<<{}[]>{<>()}>}{{<<>()>
[[[[<<<({<({({[]}[[]{}])(<{}()>[{}{}])}[[({}())][{<>{}}{[]<>}]])>})<([<(<(()[])([]())>)<[[{}[]][{}<>]][[(
{<{<{<[[{[[<(([]{})){[()[]][{}[]]}><[{<>{}}({}{})]{({}())<<>[]>}>]]}(([<[{<>()}{(){}}]<<[]{}>(()())>>]
{<<<{<{<(<{([(<>)<[][]>][(()[]){{}<>}])}(((({}<>)<[][]>){([]<>){()<>}})<<<<>()>{{}()}>{<[]()><[]()>}>)})[<{
([<<[[{{<[{(<{[]()}>)<<<<>()>([]<>)>>}]{(({{<>()](()<>)}(({}())[[]()])))}>{(<[<(<><>)[{}<>]
[{<<{[[<[<<{{<<>()>}[[{}[]]({}{})]}([[<>[]]][(<><>)<()()>])>[({[<><>][[]<>]})({<[][]>(()<>)})]>}>][{(([<[{
{([[[<[(([[<<<()<>>[<>()]>[<()<>><(){}>]>[<<[][]>(<><>)>]][(([<>()]<<>()>))<([{}()]{{}{}}){<()[]){[]()}}>]]{[
{{<<[<{{([({[([]<>)[{}()]]{[()[]>[()()]}}<[[<>{}](<><>)]>)[<(<<><>><[]{}>)([<>{}])><<{[]}[{}()]>{<<>{}>[<>[]
{{<(<<((<[<<<[{}[]]<<><>>>[({}[]){{}()}]>>]>){(<([(<<>[]><{}>)({<><>}<{}[]>)]{{([]{}>(()())}
[(<<<{[<([[(({()()}<{}[]>){[{}<>]([]<>)})({(<>[])(()<>)}[([][])<())])]])({[<(([][]){()()})>{[[(
[<[[(({[<<([{({}[])[{}{}]}{<<>[]>[{}{}]}])[[({{}}<[]>){<[]()>{{}{}}}]<{[<>[]](<>())}<[()()][()<>]>>]>(<[[[[
{<{[([[<<<{<<({}{})(<>())>{<<><>><{}{}>}>{({()()}<{}()>)<(<>{}){<>[]}}}}({[{[]{}}{()<>}](<<><>>(
{{<<([{([[(([{()<>}<(){}>]<<()()>(()<>)>)({[{}()]}<<()[]><()()>>))][[<(((){})<[][]>)><(<<><>>
{(([{({<{[({[(<><>)(()()]]<[<>[]][{}<>]>})]}>{(([[(<()[]>(()<>)){{[]<>}(<>())}]([<[]()>[{}[
{{({{{<{{{[([[<><>]]<{[][]}[[]<>]>)(<<<><>><<><>>>[(()())({}<>)])]((<(<><>)<(){}>>[{{}{}}[{}<>]])([<()[]>
{(<<{{<<{{{{<<[]<>>[{}()]><<()[]>{{}[]}>}}}}([({<<{}{}>[()]>[[{}[]]<[]{}>]}(<{()()}<()[]>>))]{
{<<([((<<[<{({{}[]}<()()>)(([]{})<{}[]>)}<(((){})[()<>])>><(<(<><>)<<><>>>){[((){})([]<>)](([][])[<
<{[{<{<<({<<([{}()]{[]{}})[({}())<{}()>]>>[[[(()[])[()<>]](<[][]><{}()>)][(([]()]([]))]]})>>{<[<[((<{}<>>{(
[{[[[({<<[[([{<>{}}[[]]]<<{}<>><[]<>>>)(<<{}()>[()<>]>[<(){}>])][<{<()()><<>[]>}<[[][]][<>()]>><[[{}()](<>)
<{{[{[{[([[[([<><>]({}[]))([[][]](<>{})}][[{[]()}{{}()}][{[][]}<{}<>>]]][(({[]<>}[<>()])[<()<>><[][]>])<(({}
{(({[{(<[<(<[{<><>}<{}[]>]<[{}<>]((){})>>([{()}(<><>)])){<[<()<>>[{}()]]({<>{}}(<><>))>{{(<
<<[[(<{<({<<[[<>()]((){})]>{[({})<{}<>>]((<>{}){[]<>})>>})>}>({{(<<{([()[]])[{{}[]}(<>[])]}>>)}<((<<<
[[([{{((<(<({{[]<>}}<{<>()}([]())>)<[<<>()>(<>{})][[()()]<<>{}>]>>)>(<[[{[{}{}]({}[])}({{}{}}[[]()
<{[[{[([<([{<<()()>><<<>[]>>}][[((<>)(<><>))<({}{})<()<>>>]<{[<>()]<[]{}>}>])({[[{[]{}}]]}{({[<>()
<<[<{<([([<({<(){}>{[]()}}<<{}<>><[]<>>>)>{{<[(){}]{<>()}>(<<>()>[{}<>])]}](<(<(()())<<><>>
[{[<[<[<<(<[(<<>{}>)[<{}{}>({}{})]]})>[[(((<<>[]>[<>()])<{(){}}<(){}>>){{(<><>)}[(<>()){{}<>}]})
{<{<({{(<(<([[<>()][[]()]][(()[])[[]<>]])[([[]{}]{{}<>})]>[[<({}()){<><>}><{()[]}({}())>]([{<>{}}
({(([(<[[{{<([[]()]{{}{}})[{{}{}}[{}<>]]>[{([]<>)(()())}(<<><>>{<>{}})]}<<({()()}{()<>})[(<>
[<[<((({{<{([({}())([]{})]<(()())(<>())>)({<()[]>{<>[]}})}<[([()<>]{{}<>})](<{[]()}(<>())>)>>[({[([])(
({[<[(<((<{(<[()[]>[{}<>]>)<{<[]<>>{<>[]}}(({}{}))>}{{<[[]{}][{}{}]>{(())<[]()>}}}><<<{(<>[])<[]()>}({[][
(<<<({({<[[<<(<><>}<()<>>>{<{}<>><[]<>>}>[<<[]<>>(()[])>{<()()>}]]]{{(([<>[]]<[]{}>){({}{})([][]
({<[[<[({[{<{(()<>)}[(()[])<<>{}>]>}({{(<><>)[<><>]}[{[]()}<(){}>]}{{[()()]<(){}>}[[{}[]]([]{})]})]([[<{{}()}
[[[(<({(({{{<{()<>}[<>{}]><<[][]>({}[])>}[[[{}{}]<<>{}>][[(){}]]]}[<([{}{}][[]])[{<><>}[()[]]]>]}<<[({{
[<[[{[(([[<{(<{}{}>)}(<{(){}}([][])>{<(){}><<>{}>})>([([{}{}])(<[]><(){}>)])][({<<{}<>><[]<>>>[[[]{}]{[]{}}]
[{{[(<<{{{[([(()())<<><>>])<([()()]((){}))<([][]){[]<>}>>]{<<{(){}}(<><>)>({()<>}<()[]})>}}}}[{{<<
<[{[(({({<(<<<{}{}>{{}{}}>{([])({})}>{[{<>>(<>)]{[<>{}]<{}<>>}})[<({{}[]}<{}{}>)<([]())({}())>>({<[]
(<[<({[{{(((({{}[]}{{}<>}){(<>[])})[[({}<>)[[]<>]]<[{}]{[][]}>])(<[(<>()){<>()}]<(<><>){(){}}>>
[([{([{[<{<[<(<>{}){{}[]}>{([][]){()}}]{[<[]{}><<>{}>]{[(){}){[]{}}}}>([<[{}]<{}[]>>{<[][]>{()[]}}][{{<>()}{{
<{{(({({[<(({({}[]){{}<>}}[(<>()){[]{}}]))[[<{()()}[{}{}]>(<{}{}>(<>[]))]<<{()()}<{}{}>><{<><>}<<>[]
{{[[<[<[{[<{{[[]<>]<[]>}[({}{})(<>)]}>](<<((<>)<[]<>>)[<{}()><<>[]>]>[<{<>()}<(){}>>[[()<>]]]>(<[{
({[<(<{<[<<<(<<>()><[]<>>)<<()<>>({}[])>>(<[()()]{<><>}>)>>]>(<<({[<{}[]>{()}]}<<{()<>}({}())>({[]<>}([]()))>
<{<{{[({{(<{<<<><>><(){}>>[([][])([]{})]}<{([][]){{}}}<<[]()>([][])>>>[<{{[]()}[()<>]}<[<>{}]([]{})>>])
{({[{(<[<<<<(([]<>)<{}{}>)>((({}{})<{}<>>)<<{}{}>>}>{{[<()()>[{}()]]}((<<>()>[(){}])<{[]<>}[<>{}]>)}>>{<<{
((([<[[[<{{<<<{}[]><<>{}>>(([]<>)[[]])>((<{}[]><{}>)(({}[])[()[]]))}{{<(<>[])(<><>)>(<<>[]
[[([{<(<(<[({[[][]]{()<>}}{{<>[]}<[][]>})]>)<{[((((){})([]<>))[<<><>>(<><>)]>[{<{}[]><[][]>
[<<(<(({{{<((([]())[<>{}])<[[][]]{()()}>)><[<((){})<()()]>[<[]>[(){}]]]({([]())([]{})}([<>(
(<{<<{<((({(<{(){}}[()<>]>{[[]<>][()[]]})<<{[][]}{{}[]}>[(<><>)<{}{}>]>}(<[{{}<>}{[]()}]({()[]}((
<[[([<<[{{<(<[()[]]{<><>}>([<>[]]<{}[]>))[({{}()}<[]<>>)<(<>{})>]>{{{<<>{}>(<>)}<{<>()}[<>()]>}<[<<>()
[[((<({<[{{<[[[]()][<>]](<()()>[{}<>])>{<(()<>)>([()<>]{()[]})}}{[[(()<>><[]<>>]]<{(<><>){{}<>}}
[<{([{[{<<<(<[<><>]({}())>{([]<>][[]{}]})[<{[]<>}[<>{}]>[<[][]>]]>>({([(<><>){<>{}}][{{}[]}({}<>)
{({{<[([{([<<{<>()}>[{<>[]}[{}[]]]>](<{{[]{}}[{}<>]}({<>[]}[{}[]])>[<([][])({}{})><<{}()>(()<>)
(<({[<(<[<[{([[]{}][{}[]])([{}[]])}{({<>[]}{()[]})[[<><>](()<>)]}]><(({[()[]]}([{}()][{}{}]))<[(()<>)]>)[[<
<(<(<<({({[<{<<><>>[()<>]}{<[]()><<><>>}>[(([][])<{}[]>)(({}{})<<>()>)]](<<(<><>){[]<>}>([[][]][<>()])>{<(
[({<[[<{[[{[{{<>()}{{}[]}}](([{}[]}{[][]})<{<>[]}({}<>)>)}{[(([]{})<{}[]>)<<{}>{(){}}>]}]<[
<[({<<[[({{{((<><>)<[]<>>)<<{}><{}<>>>}(([(){}]{()})[{[][]}[[]<>]])}}[[<[<()[]>[{}()]]><{<{}<>><<>[]>}{[[]
<[{[[[[[<{[<([<>()]([]{}))<{[]{}}<[][]>>>([{[]<>}([]<>)]{[{}()][<>{}]}}]<[[(<><>)[{}{}]][(()(
{<{{[<({{<[([{()()}[{}<>]]{({}())<(){}>})[[{(){}}<[]<>>}<(<>()){{}{}}>]]{{(([]{})[[]()])[{{}{}}[[]{}]]}{<[
(([<([<<{[{{[({}{})][(<>{})]}}]{{([<<>{}>(<>())])}}}>[{<<(({{}<>}<<>[]>){({}())<{}()>})><(<[()<>]><{()<>}<
[<[{[[[({[{[(((){}){(){}}){{<><>}{{}[]}}]<{({}()){<>{}}}>}<{[{[]{}}({}{})])>]}{(<(((()[]){{}[]})[<()<>
({<<([{{{{({[{<>[]}[{}{}]]{<[]{}><{}{}>}}[<[<>()](<><>)><[{}{}]>])(<{[<>()]<<>()>}<(<>[])>>(([()'''

# COMMAND ----------

close_to_error_score = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}
open_to_close = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>',
}

error_score = 0
for line in inp.splitlines():
  expected_closes = []
  for c in line:
    if c in ')]}>':
      if c != expected_closes.pop():
        error_score += close_to_error_score[c]
        break
    else:
      expected_closes += open_to_close[c]

answer = error_score
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, discard the corrupted lines.  The remaining lines are <em>incomplete</em>.</p>
# MAGIC <p>Incomplete lines don't have any incorrect characters - instead, they're missing some closing characters at the end of the line. To repair the navigation subsystem, you just need to figure out <em>the sequence of closing characters</em> that complete all open chunks in the line.</p>
# MAGIC <p>You can only use closing characters (<code>)</code>, <code>]</code>, <code>}</code>, or <code>&gt;</code>), and you must add them in the correct order so that only legal pairs are formed and all chunks end up closed.</p>
# MAGIC <p>In the example above, there are five incomplete lines:</p>
# MAGIC <ul>
# MAGIC <li><code>[({(&lt;(())[]&gt;[[{[]{&lt;()&lt;&gt;&gt;</code> - Complete by adding <code>}}]])})]</code>.</li>
# MAGIC <li><code>[(()[&lt;&gt;])]({[&lt;{&lt;&lt;[]&gt;&gt;(</code> - Complete by adding <code>)}&gt;]})</code>.</li>
# MAGIC <li><code>(((({&lt;&gt;}&lt;{&lt;{&lt;&gt;}{[]{[]{}</code> - Complete by adding <code>}}&gt;}&gt;))))</code>.</li>
# MAGIC <li><code>{&lt;[[]]&gt;}&lt;{[{[{[]{()[[[]</code> - Complete by adding <code>]]}}]}]}&gt;</code>.</li>
# MAGIC <li><code>&lt;{([{{}}[&lt;[[[&lt;&gt;{}]]]&gt;[]]</code> - Complete by adding <code>])}&gt;</code>.</li>
# MAGIC </ul>
# MAGIC <p>Did you know that autocomplete tools <em>also</em> have contests? It's true! The score is determined by considering the completion string character-by-character. Start with a total score of <code>0</code>. Then, for each character, multiply the total score by 5 and then increase the total score by the point value given for the character in the following table:</p>
# MAGIC <ul>
# MAGIC <li><code>)</code>: <code>1</code> point.</li>
# MAGIC <li><code>]</code>: <code>2</code> points.</li>
# MAGIC <li><code>}</code>: <code>3</code> points.</li>
# MAGIC <li><code>&gt;</code>: <code>4</code> points.</li>
# MAGIC </ul>
# MAGIC <p>So, the last completion string above - <code>])}&gt;</code> - would be scored as follows:</p>
# MAGIC <ul>
# MAGIC <li>Start with a total score of <code>0</code>.</li>
# MAGIC <li>Multiply the total score by 5 to get <code>0</code>, then add the value of <code>]</code> (2) to get a new total score of <code>2</code>.</li>
# MAGIC <li>Multiply the total score by 5 to get <code>10</code>, then add the value of <code>)</code> (1) to get a new total score of <code>11</code>.</li>
# MAGIC <li>Multiply the total score by 5 to get <code>55</code>, then add the value of <code>}</code> (3) to get a new total score of <code>58</code>.</li>
# MAGIC <li>Multiply the total score by 5 to get <code>290</code>, then add the value of <code>&gt;</code> (4) to get a new total score of <code>294</code>.</li>
# MAGIC </ul>
# MAGIC <p>The five lines' completion strings have total scores as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>}}]])})]</code> - <code>288957</code> total points.</li>
# MAGIC <li><code>)}&gt;]})</code> - <code>5566</code> total points.</li>
# MAGIC <li><code>}}&gt;}&gt;))))</code> - <code>1480781</code> total points.</li>
# MAGIC <li><code>]]}}]}]}&gt;</code> - <code>995444</code> total points.</li>
# MAGIC <li><code>])}&gt;</code> - <code>294</code> total points.</li>
# MAGIC </ul>
# MAGIC <p>Autocomplete tools are an odd bunch: the winner is found by <em>sorting</em> all of the scores and then taking the <em>middle</em> score. (There will always be an odd number of scores to consider.) In this example, the middle score is <code><em>288957</em></code> because there are the same number of scores smaller and larger than it.</p>
# MAGIC <p>Find the completion string for each incomplete line, score the completion strings, and sort the scores. <em>What is the middle score?</em></p>
# MAGIC </article>

# COMMAND ----------

import statistics

close_to_score = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}

scores = []
for i, line in enumerate(inp.splitlines()):
  expected_closes = []
  has_error = False
  for c in line:
    if c in ')]}>':
      if c != expected_closes.pop():
        has_error = True
        break
    else:
      expected_closes += open_to_close[c]
      
  if not has_error:
    score = 0
    for c in expected_closes[::-1]:
      score *= 5
      score += close_to_score[c]
    scores.append(score)

answer = statistics.median(scores)
print(answer)
