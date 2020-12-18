# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/16
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 16: Ticket Translation ---</h2><p>As you're walking to yet another connecting flight, you realize that one of the legs of your re-routed trip coming up is on a high-speed train. However, the train ticket you were given is in a language you don't understand. You should probably figure out what it says before you get to the train station after the next flight.</p>
# MAGIC <p>Unfortunately, you <span title="This actually happened to me once, but I solved it by just asking someone.">can't actually <em>read</em> the words on the ticket</span>. You can, however, read the numbers, and so you figure out <em>the fields these tickets must have</em> and <em>the valid ranges</em> for values in those fields.</p>
# MAGIC <p>You collect the <em>rules for ticket fields</em>, the <em>numbers on your ticket</em>, and the <em>numbers on other nearby tickets</em> for the same train service (via the airport security cameras) together into a single document you can reference (your puzzle input).</p>
# MAGIC <p>The <em>rules for ticket fields</em> specify a list of fields that exist <em>somewhere</em> on the ticket and the <em>valid ranges of values</em> for each field. For example, a rule like <code>class: 1-3 or 5-7</code> means that one of the fields in every ticket is named <code>class</code> and can be any value in the ranges <code>1-3</code> or <code>5-7</code> (inclusive, such that <code>3</code> and <code>5</code> are both valid in this field, but <code>4</code> is not).</p>
# MAGIC <p>Each ticket is represented by a single line of comma-separated values. The values are the numbers on the ticket in the order they appear; every ticket has the same format. For example, consider this ticket:</p>
# MAGIC <pre><code>.--------------------------------------------------------.
# MAGIC | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# MAGIC |                                                        |
# MAGIC | ??: 301  ??: 302             ???????: 303      ??????? |
# MAGIC | ??: 401  ??: 402           ???? ????: 403    ????????? |
# MAGIC '--------------------------------------------------------'
# MAGIC </code></pre>
# MAGIC <p>Here, <code>?</code> represents text in a language you don't understand. This ticket might be represented as <code>101,102,103,104,301,302,303,401,402,403</code>; of course, the actual train tickets you're looking at are <em>much</em> more complicated. In any case, you've extracted just the numbers in such a way that the first number is always the same specific field, the second number is always a different specific field, and so on - you just don't know what each position actually means!</p>
# MAGIC <p>Start by determining which tickets are <em>completely invalid</em>; these are tickets that contain values which <em>aren't valid for any field</em>. Ignore <em>your ticket</em> for now.</p>
# MAGIC <p>For example, suppose you have the following notes:</p>
# MAGIC <pre><code>class: 1-3 or 5-7
# MAGIC row: 6-11 or 33-44
# MAGIC seat: 13-40 or 45-50
# MAGIC 
# MAGIC your ticket:
# MAGIC 7,1,14
# MAGIC 
# MAGIC nearby tickets:
# MAGIC 7,3,47
# MAGIC 40,<em>4</em>,50
# MAGIC <em>55</em>,2,20
# MAGIC 38,6,<em>12</em>
# MAGIC </code></pre>
# MAGIC <p>It doesn't matter which position corresponds to which field; you can identify invalid <em>nearby tickets</em> by considering only whether tickets contain <em>values that are not valid for any field</em>. In this example, the values on the first <em>nearby ticket</em> are all valid for at least one field. This is not true of the other three <em>nearby tickets</em>: the values <code>4</code>, <code>55</code>, and <code>12</code> are are not valid for any field. Adding together all of the invalid values produces your <em>ticket scanning error rate</em>: <code>4 + 55 + 12</code> = <em><code>71</code></em>.</p>
# MAGIC <p>Consider the validity of the <em>nearby tickets</em> you scanned. <em>What is your ticket scanning error rate?</em></p>
# MAGIC </article>
# MAGIC <p>To begin, <a href="16/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <form method="post" action="16/answer"><input type="hidden" name="level" value="1"><p>Answer: <input type="text" name="answer" autocomplete="off"> <input type="submit" value="[Submit]"></p></form>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=%22Ticket+Translation%22+%2D+Day+16+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F16&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=%22Ticket+Translation%22+%2D+Day+16+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F16'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "departure location: 36-626 or 651-973
departure station: 38-134 or 142-966
departure platform: 32-465 or 489-972
departure track: 40-420 or 446-973
departure date: 38-724 or 738-961
departure time: 30-358 or 377-971
arrival location: 48-154 or 166-965
arrival station: 48-669 or 675-968
arrival platform: 27-255 or 276-965
arrival track: 37-700 or 720-955
class: 50-319 or 332-958
duration: 35-822 or 835-949
price: 40-791 or 802-951
route: 42-56 or 82-968
row: 40-531 or 555-968
seat: 49-681 or 695-962
train: 31-567 or 593-953
type: 42-840 or 855-949
wagon: 31-165 or 176-962
zone: 48-870 or 896-970

your ticket:
127,89,149,113,181,131,53,199,103,107,97,179,109,193,151,83,197,101,211,191

nearby tickets:
835,933,819,240,276,334,830,786,120,791,301,770,249,767,177,84,838,85,596,352
193,697,654,130,5,907,754,925,817,663,938,595,930,868,56,128,598,197,381,452
922,462,747,775,599,787,765,815,298,930,198,89,654,353,56,285,571,411,560,419
515,287,391,452,91,319,143,614,50,910,450,926,617,288,922,137,738,761,248,751
50,945,117,899,420,675,177,521,774,677,56,279,768,391,282,151,107,920,904,976
595,243,760,96,816,786,600,940,347,413,132,722,16,668,896,250,815,619,804,186
244,907,377,226,188,595,509,406,777,691,791,383,247,122,609,597,340,803,817,512
773,222,819,757,50,562,108,867,195,455,389,454,564,581,557,622,897,914,54,927
778,865,451,741,520,199,355,870,723,513,618,784,377,413,758,124,296,180,566,584
861,236,213,302,196,637,525,840,530,926,905,341,812,222,749,104,677,459,150,200
455,446,440,402,309,143,497,382,198,246,511,228,243,129,317,491,932,109,516,102
117,177,462,196,283,777,655,122,780,111,94,153,391,335,433,455,306,810,344,790
292,349,232,999,463,240,209,101,530,662,805,209,148,505,501,287,560,499,815,593
744,128,616,866,777,54,467,94,125,662,89,84,909,528,181,521,784,555,347,659
721,909,415,252,53,346,499,564,584,857,283,911,201,897,420,939,867,420,447,280
639,416,317,392,837,127,775,382,300,407,809,666,836,774,399,666,698,526,558,116
261,522,939,567,244,97,152,129,401,305,772,184,390,835,294,240,776,947,816,149
902,560,193,118,556,512,181,379,975,448,101,677,839,756,901,695,297,355,669,866
291,293,103,788,403,778,379,101,107,458,110,720,104,990,809,927,838,211,304,287
657,152,125,945,816,395,263,308,409,783,414,496,507,663,252,403,348,611,417,456
743,410,117,779,933,282,113,948,756,622,111,309,286,764,656,703,867,341,791,782
782,664,761,491,350,6,940,920,700,213,932,234,193,182,839,754,760,516,343,297
669,724,496,285,767,519,601,160,178,96,105,351,245,127,613,337,113,313,101,108
616,207,838,618,912,149,184,344,761,222,302,660,625,669,221,778,792,89,786,759
144,280,907,336,910,821,129,130,334,85,301,319,900,312,858,277,391,662,626,169
751,514,769,242,515,154,176,194,281,381,153,386,299,178,731,457,120,243,492,239
339,767,662,838,171,840,234,226,295,184,187,779,916,384,396,780,496,942,512,128
398,613,661,280,743,92,397,305,115,924,698,335,210,523,620,753,454,141,613,305
897,462,92,234,779,253,291,921,401,838,249,123,747,596,738,510,78,276,559,114
141,788,283,409,860,103,337,838,343,560,150,595,332,930,820,810,756,220,147,406
557,926,230,778,124,459,722,86,118,240,220,914,353,129,803,688,215,407,749,817
341,217,561,516,559,14,188,491,870,762,505,112,235,391,864,745,768,124,306,310
406,901,417,338,598,766,390,746,613,922,405,518,618,783,738,336,561,50,667,633
900,145,607,820,681,755,562,763,337,287,454,742,741,604,982,347,517,661,902,384
188,205,505,85,446,449,198,418,84,773,832,748,943,221,212,607,378,123,383,945
766,502,87,305,522,202,679,212,86,653,808,531,929,180,865,934,785,486,201,723
219,457,386,55,51,975,99,252,208,418,929,82,354,783,189,721,112,184,127,392
505,744,933,145,123,565,770,924,105,185,913,134,306,835,567,524,909,863,982,786
898,915,562,289,117,675,399,567,146,104,780,54,465,519,600,897,878,605,307,242
243,82,367,720,918,378,936,621,944,743,503,104,511,231,410,336,458,769,448,296
557,408,526,564,347,655,937,222,745,381,297,942,740,931,527,305,540,415,497,380
305,286,567,239,311,741,924,385,309,861,937,245,302,154,486,919,790,277,563,465
750,303,55,310,809,755,397,561,616,941,806,134,144,399,624,449,716,806,240,465
717,99,203,664,679,766,399,225,603,384,51,312,213,604,462,176,609,181,453,414
19,205,300,230,835,88,944,82,558,904,459,490,679,523,790,213,917,89,614,276
805,574,240,335,489,911,200,510,723,756,602,191,496,408,651,248,123,742,904,761
127,508,607,102,691,945,278,151,96,453,145,56,497,118,419,840,222,594,190,862
748,355,206,107,523,929,656,592,246,101,754,748,455,343,782,109,698,280,227,678
669,920,353,389,514,625,511,387,342,817,105,819,491,511,491,910,248,402,531,273
387,250,565,507,561,225,976,319,51,662,531,514,896,118,620,776,195,614,501,786
654,384,741,923,746,90,304,913,494,153,114,19,222,755,179,930,835,770,813,660
150,563,931,349,148,242,400,186,500,946,273,564,131,752,339,838,240,528,210,521
399,358,410,683,596,739,96,802,870,394,513,249,786,292,180,315,404,89,909,496
696,227,820,194,594,626,867,80,112,279,762,230,276,177,390,97,391,783,247,297
211,912,146,563,86,597,942,282,527,561,577,905,127,947,388,662,901,184,755,134
655,664,803,743,290,866,132,783,131,205,855,124,743,388,819,485,822,791,611,201
319,287,151,242,233,297,519,313,499,390,459,138,812,814,345,558,770,87,414,292
724,498,521,236,465,109,229,377,406,915,683,614,679,224,410,781,774,802,752,196
594,821,633,105,282,502,661,188,95,750,245,224,508,669,758,55,760,300,516,415
820,279,351,815,226,869,522,745,939,778,459,118,944,914,629,897,558,618,340,308
856,663,612,870,499,180,82,720,909,658,621,128,791,937,939,59,94,401,252,751
86,497,561,88,455,183,918,352,309,410,301,987,301,859,310,492,697,295,335,292
514,749,530,492,600,991,933,152,668,102,655,88,206,244,791,411,254,771,617,678
820,913,288,509,343,784,622,667,155,353,903,817,447,300,811,803,911,195,403,743
208,294,652,763,448,562,788,204,626,503,837,454,809,406,272,460,222,770,775,597
614,494,747,93,211,334,625,349,295,290,346,764,408,98,406,290,16,382,83,790
115,739,773,219,129,492,225,674,464,95,931,516,806,495,303,602,555,662,566,228
530,909,98,897,142,84,714,420,937,186,613,149,839,210,397,818,87,948,292,126
286,305,949,506,497,119,219,395,612,223,454,667,663,514,346,391,127,174,521,501
941,511,915,626,99,82,727,92,188,215,130,357,790,619,839,133,838,495,521,390
210,939,811,495,599,188,354,150,610,753,446,143,698,291,153,382,903,130,916,4
182,131,231,126,839,745,195,413,153,669,133,234,309,209,514,818,485,397,748,947
298,391,617,920,457,680,219,320,945,699,923,781,779,335,869,282,292,336,350,85
212,419,986,314,721,315,659,133,249,144,756,463,924,667,862,450,143,181,334,388
911,861,791,867,453,664,498,780,355,493,397,693,98,555,384,209,940,868,345,286
557,661,515,494,816,942,404,244,507,143,654,764,696,402,124,150,167,200,102,509
512,828,389,566,242,922,931,565,780,301,410,503,183,343,778,626,84,146,129,221
128,599,202,289,910,519,907,498,488,748,149,777,745,596,611,456,120,53,678,283
724,191,613,300,806,865,124,778,104,750,758,597,604,747,764,157,195,177,680,932
227,457,50,283,143,741,523,134,680,947,558,600,761,617,226,416,136,923,211,405
379,338,307,56,626,761,379,855,997,454,303,864,869,941,610,192,339,868,351,566
280,696,698,596,592,896,509,124,401,723,418,748,555,501,937,408,404,608,143,253
940,186,411,464,387,602,184,354,142,757,220,184,223,182,301,442,378,740,738,142
450,123,938,377,91,548,837,626,594,593,418,790,297,82,124,190,254,531,345,397
762,508,206,357,224,830,761,912,624,245,667,247,247,618,290,938,107,910,288,55
773,318,906,301,383,856,202,866,562,305,181,152,52,382,313,906,228,825,188,769
55,502,393,821,937,942,936,147,516,458,182,502,919,788,173,402,395,565,932,860
199,607,614,404,663,392,668,504,142,462,205,299,787,318,771,126,211,694,194,526
184,805,452,594,857,706,230,88,771,337,755,341,748,654,315,213,502,407,309,380
283,696,709,111,761,460,558,190,700,118,898,723,697,566,176,318,865,776,296,230
607,394,753,122,353,293,298,207,903,349,106,496,333,984,920,461,758,699,334,749
460,406,771,196,106,507,499,558,656,357,506,813,857,784,303,634,941,312,786,914
919,769,919,451,94,672,406,743,113,101,739,596,182,332,555,89,185,698,291,530
933,460,248,279,314,897,763,748,669,767,383,121,764,244,58,402,902,658,124,496
917,761,769,307,698,396,190,171,747,523,555,453,933,501,594,301,98,601,750,608
621,791,125,51,748,799,187,216,598,420,151,380,658,658,720,201,464,317,109,604
219,491,747,92,625,97,430,284,453,196,619,454,382,448,948,334,499,557,944,109
294,614,334,623,302,501,502,821,702,357,699,839,784,278,761,403,235,401,412,228
817,346,595,489,124,791,616,209,384,751,132,492,587,598,855,814,603,316,378,123
941,302,130,240,609,171,179,417,565,870,623,194,698,297,499,410,409,345,116,279
295,600,557,696,603,266,599,219,407,779,220,450,314,198,807,610,462,319,750,863
407,945,134,813,113,392,495,243,600,123,116,249,145,387,398,228,104,696,393,140
180,382,801,816,625,787,564,528,128,392,94,745,655,594,278,759,754,899,661,680
785,760,409,666,241,529,940,702,668,938,755,240,393,293,356,134,669,836,498,677
939,596,856,666,821,141,912,566,744,818,912,525,382,276,312,819,420,751,287,603
802,306,558,23,125,286,811,816,840,287,915,838,931,561,936,608,785,214,754,354
384,923,914,314,197,301,745,154,109,391,519,254,23,912,393,899,352,451,593,394
758,921,446,145,238,857,413,946,785,506,170,651,912,276,927,531,218,804,317,153
758,216,767,508,344,900,565,192,293,338,906,857,235,662,665,395,119,561,665,701
901,930,675,446,815,418,116,741,802,743,869,569,317,287,784,389,783,91,386,240
234,564,224,896,812,813,391,625,174,185,53,923,221,744,492,784,751,382,493,788
395,285,582,85,108,822,770,593,222,129,355,277,227,119,334,82,757,944,305,760
511,489,253,491,451,676,416,821,204,924,2,668,496,126,384,755,178,378,388,665
456,170,773,52,604,379,203,817,103,149,521,561,152,932,663,597,458,316,84,905
301,680,903,109,151,90,200,184,858,100,236,398,238,555,312,612,308,228,771,164
821,930,489,278,284,840,599,344,347,658,790,781,605,998,606,458,456,865,503,122
404,319,212,755,55,655,20,864,930,599,625,817,924,906,523,745,507,108,901,905
721,185,420,209,192,177,641,680,89,242,300,927,352,191,395,284,384,698,563,463
773,819,906,781,900,109,413,137,776,147,213,240,227,924,307,316,652,339,496,900
453,696,743,738,297,609,913,414,418,920,406,665,152,939,233,123,993,399,561,50
346,619,815,511,347,410,771,559,276,160,747,450,354,50,941,194,900,945,819,393
307,215,145,224,446,246,373,378,237,769,607,233,201,203,615,199,527,229,123,97
756,381,107,564,868,788,751,626,567,309,764,948,394,284,155,245,944,742,460,512
839,912,234,179,611,88,416,527,899,499,598,499,154,187,789,741,905,704,388,663
122,490,769,285,898,699,606,99,462,809,132,915,132,453,664,786,453,239,104,687
205,508,835,860,757,740,337,54,917,413,513,814,905,942,319,556,156,353,199,113
524,379,898,817,941,721,521,379,185,744,458,904,8,898,56,567,219,229,237,763
56,294,235,525,243,761,244,315,311,696,818,301,460,100,182,268,307,608,925,408
722,791,290,565,593,508,493,114,114,934,949,739,936,195,765,520,509,591,195,415
907,247,773,940,904,655,299,342,920,712,930,280,318,758,460,339,311,858,700,838
901,669,307,254,461,120,89,625,869,839,229,248,616,307,306,412,644,232,739,244
484,417,751,344,281,319,666,607,216,811,669,491,679,194,679,277,238,741,242,404
51,597,721,154,200,781,936,528,145,335,718,301,224,926,934,142,205,606,278,803
304,761,682,295,783,56,558,127,786,218,247,756,449,205,389,459,116,494,681,222
613,738,216,566,816,117,576,530,92,390,771,453,234,393,920,518,458,309,531,790
748,231,498,54,347,599,923,419,125,940,446,489,200,186,616,240,609,856,985,134
914,121,405,618,523,87,740,337,655,381,88,392,291,525,588,238,150,306,203,558
91,447,563,514,181,745,561,273,593,54,108,911,410,787,738,807,811,786,818,741
582,681,675,285,605,786,947,379,918,110,749,811,399,614,333,610,524,308,738,653
185,654,505,942,199,381,96,202,281,51,922,898,446,922,555,916,316,124,180,438
609,740,919,997,940,199,531,284,934,338,567,864,310,909,814,840,144,761,96,864
818,386,868,512,603,215,222,187,213,896,105,224,898,249,103,601,125,156,219,767
621,814,419,132,564,421,661,385,357,525,720,949,904,205,521,918,659,248,557,408
153,757,867,181,455,653,112,528,997,127,788,245,520,921,207,510,611,118,354,925
698,808,207,924,212,401,332,764,523,622,353,918,908,930,831,750,250,724,802,803
860,613,749,767,927,816,836,765,338,411,914,123,290,355,699,169,669,868,356,855
285,228,602,489,155,745,910,211,99,298,394,215,209,722,660,412,352,654,188,602
946,768,914,56,902,277,379,867,109,221,557,273,624,813,449,607,383,752,344,820
764,461,772,284,381,756,740,386,126,189,494,833,292,741,298,411,745,347,617,318
386,244,262,607,333,398,746,514,920,176,146,868,489,86,338,197,839,197,558,458
411,94,134,246,789,345,606,304,208,490,820,157,277,838,920,490,339,651,240,249
530,593,780,571,781,528,299,117,253,749,247,405,346,396,221,143,305,595,289,505
810,238,236,240,105,769,130,601,500,742,901,611,949,519,981,84,348,98,940,387
523,111,354,462,866,460,409,988,102,494,409,857,837,133,52,132,667,932,779,314
623,840,558,924,197,493,820,679,664,146,88,121,758,745,511,834,86,789,567,624
814,772,286,810,347,513,602,668,456,244,355,815,619,420,719,626,616,525,243,389
695,452,238,377,624,159,530,282,236,215,292,508,521,146,224,88,699,133,564,392
211,115,456,405,225,238,766,818,857,246,181,114,94,116,146,354,7,301,529,318
386,451,529,298,56,180,219,440,738,756,406,607,225,936,720,456,761,417,617,464
131,254,947,401,818,343,97,801,835,119,739,205,96,822,666,929,86,753,209,110
607,929,251,769,231,809,859,783,830,142,344,280,99,107,503,388,507,498,489,926
738,676,310,805,922,190,2,205,742,492,767,927,595,868,523,652,251,142,216,348
660,105,652,509,402,666,758,317,89,864,212,495,503,758,567,91,668,748,227,982
754,609,116,529,866,623,747,355,355,561,132,203,515,93,458,921,364,216,410,103
817,523,195,112,567,494,855,507,400,170,655,340,295,817,921,906,279,280,527,291
342,916,496,82,296,562,289,204,941,769,994,206,697,781,785,213,204,907,561,316
342,598,124,756,495,745,821,295,250,764,980,224,806,102,665,293,558,603,459,922
802,754,204,806,348,775,91,461,318,784,667,652,526,686,451,922,697,127,409,903
919,142,395,397,491,897,133,739,662,498,816,248,663,199,386,580,651,566,314,745
511,528,611,255,104,603,610,901,446,834,515,250,920,563,92,344,402,820,928,902
616,127,183,213,412,748,922,195,898,147,120,51,353,412,912,904,617,315,0,125
254,906,53,695,212,64,513,281,143,908,214,249,357,860,808,749,51,941,414,695
210,278,396,307,222,517,313,919,675,502,297,511,318,561,915,398,665,900,866,826
523,121,291,749,396,911,409,453,232,20,53,351,805,305,183,296,927,680,282,740
941,785,354,184,494,491,788,546,812,784,83,287,341,784,667,82,908,333,122,667
288,912,757,617,594,781,283,115,620,106,741,237,126,354,603,415,24,305,816,808
399,211,698,300,769,503,837,281,457,225,142,491,288,448,91,869,834,904,751,287
606,763,472,55,204,618,696,299,384,101,935,182,337,909,115,458,345,598,56,760
347,740,452,252,130,151,921,939,112,334,904,481,508,210,303,742,866,314,216,903
240,921,212,168,379,679,104,459,835,724,897,276,452,748,522,510,127,145,739,861
598,287,503,184,668,790,160,396,341,617,595,520,810,604,698,748,788,531,461,123
687,791,517,289,915,771,453,516,764,209,87,505,818,666,749,721,903,491,112,112
127,239,178,119,495,363,393,352,839,742,204,114,229,247,127,126,278,96,462,775
992,869,120,92,525,115,766,866,516,277,461,766,812,564,83,621,865,282,805,755
184,452,295,112,219,787,223,855,761,858,301,307,379,398,201,593,268,130,666,516
461,908,730,126,807,332,667,855,454,910,948,180,840,455,918,507,912,226,778,152
222,698,98,410,0,612,497,297,280,599,783,835,116,787,178,334,930,387,121,563
149,463,127,348,214,921,19,722,514,927,186,147,868,603,341,559,419,463,343,651
131,160,204,382,202,810,595,341,614,280,509,248,150,676,509,933,556,176,297,762
819,411,292,522,187,212,54,96,662,665,901,617,594,455,914,556,419,452,986,448
664,678,816,450,862,408,514,369,514,512,318,411,86,920,904,506,176,859,218,312
669,699,101,91,231,210,135,113,516,128,614,145,656,348,923,391,603,664,530,133
598,835,289,617,677,210,790,832,105,614,809,130,452,934,351,113,287,304,461,604
301,567,144,815,193,929,305,527,112,597,870,169,416,149,747,229,900,865,767,513
242,821,858,302,781,111,238,687,249,555,211,607,113,522,773,207,462,337,808,908
280,940,197,279,382,91,785,723,619,110,995,296,768,289,902,595,447,82,622,869
98,50,496,804,237,821,168,414,148,231,238,408,224,419,698,110,621,189,107,243
403,386,352,415,856,342,559,186,897,676,384,710,351,519,515,558,802,721,353,784
779,940,540,606,213,695,675,449,99,199,202,187,286,92,131,945,110,789,698,246
763,99,174,678,901,855,287,777,191,223,232,757,319,230,413,808,623,524,653,396
144,226,312,455,193,900,820,206,669,779,815,677,856,738,749,115,684,462,918,230
722,778,832,337,221,390,243,818,668,666,345,118,930,239,564,90,523,762,183,84
652,559,491,564,54,214,790,385,690,498,559,698,116,304,356,244,254,746,738,754
446,450,152,447,313,840,678,602,312,131,494,751,347,53,462,918,214,426,145,665
284,297,332,750,153,306,394,728,334,124,287,401,416,448,243,700,131,282,213,565
420,691,652,859,515,406,205,340,387,697,662,918,224,402,501,133,310,785,897,338
856,222,176,420,752,152,115,299,753,568,349,653,762,784,348,245,230,233,130,104
524,565,563,185,291,600,403,243,131,219,617,720,120,102,367,524,196,500,758,54
238,312,73,356,785,934,414,130,838,302,149,286,232,416,133,52,772,782,594,401
186,289,463,252,299,981,118,856,415,899,292,904,920,751,410,143,922,530,771,450
564,770,90,948,121,345,680,697,942,626,907,286,776,334,188,914,729,898,808,284
908,154,283,131,102,190,458,118,151,152,305,810,613,305,176,663,463,265,595,680
515,400,105,415,817,488,221,448,766,189,93,520,224,772,596,919,307,609,491,105
222,401,192,457,298,665,945,51,179,608,394,597,869,56,248,299,439,354,754,742
524,187,771,335,653,562,290,896,85,812,303,292,555,776,136,944,132,220,507,229
338,595,198,51,749,113,677,919,236,412,518,817,652,104,908,724,673,934,133,557
742,758,462,864,654,131,744,619,489,752,243,936,177,678,721,729,859,214,563,902
899,456,231,335,386,147,656,287,197,238,279,313,603,450,408,747,329,926,762,203
775,182,314,144,527,576,196,510,121,781,356,356,763,351,497,179,917,310,127,393
776,751,456,147,776,309,381,389,122,782,656,739,212,396,133,148,293,119,939,474
133,97,903,248,669,490,302,946,270,248,922,526,396,292,664,776,418,927,787,788
172,518,525,290,668,508,202,82,111,452,940,152,91,145,118,219,611,206,501,103
721,143,218,681,296,290,809,897,191,599,143,499,298,224,991,282,111,919,346,355
764,656,931,415,119,218,103,469,385,127,789,54,652,97,514,303,864,724,335,56
857,758,788,651,861,457,310,153,206,501,82,489,696,197,696,362,287,98,179,458
561,233,349,319,741,749,205,531,339,615,302,898,300,911,694,914,676,353,771,655
902,782,159,200,83,52,245,455,96,380,925,354,679,406,395,253,504,699,462,555
418,305,185,918,514,651,561,241,151,990,187,720,409,764,814,524,392,772,84,208
155,222,301,285,97,221,595,129,388,512,456,219,867,815,228,818,107,788,182,205
768,154,738,249,559,729,312,347,505,199,749,224,936,940,454,203,230,804,528,782
183,185,417,122,354,700,919,557,232,607,741,922,213,599,778,797,505,245,855,121
402,623,786,408,451,689,896,87,761,782,192,652,251,232,193,55,765,228,754,227
374,377,248,626,299,930,142,738,782,752,285,214,121,513,180,357,767,191,449,107
279,790,379,116,777,209,691,118,622,213,741,51,209,929,197,664,346,655,403,154
825,304,202,555,857,447,564,210,724,755,696,516,133,742,393,931,455,565,122,771
751,197,183,522,402,230,293,948,771,232,160,948,864,561,897,218,819,202,655,249
202,527,311,241,861,527,234,129,770,6,102,802,86,521,750,808,196,85,229,500
911,103,945,207,519,333,867,464,489,152,865,996,104,450,668,204,303,147,126,176
433,189,317,461,942,278,180,665,618,188,664,928,668,54,251,195,299,400,146,235
774,212,205,511,315,558,990,125,416,932,396,771,661,465,54,382,752,207,353,563
95,236,566,117,112,246,522,643,738,665,528,86,340,749,802,528,835,98,146,463
283,908,141,177,780,251,114,282,101,90,948,99,747,446,652,290,355,282,905,740
"

# COMMAND ----------

# input <- "class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50

# your ticket:
# 7,1,14

# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12
# "

# COMMAND ----------

input <- "class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"

# COMMAND ----------

str_lines <- input %>% str_split("\n\n") %>% unlist() %>% map(read_lines)
str_lines

# COMMAND ----------

constraints <-
  str_lines[[1]] %>%
  as_tibble() %>%
  separate(value, c("type", "value"), ": ") %>%
  mutate(
    type_id1 = row_number(),
    value = str_split(value, " or ") %>% map(~str_split(., "-") %>% map(parse_integer) %>% map(~seq(.[[1]], .[[2]])) %>% unlist())
  ) %>%
  unnest(value)
constraints

# COMMAND ----------

your_ticket <- str_lines[[2]][[2]] %>% str_split(",") %>% unlist() %>% parse_integer() %>% enframe(name = "type_id2") %>% add_column(ticket_id = 0)
your_ticket

# COMMAND ----------

nearby_tickets <-
  str_lines[[3]][-1] %>%
  str_split(",") %>%
  imap_dfr(~parse_integer(.x) %>% enframe(name = "type_id2") %>% add_column(ticket_id = .y))
nearby_tickets

# COMMAND ----------

error_values <- nearby_tickets$value %>% discard(~. %in% constraints$value)
error_values

# COMMAND ----------

sum(error_values)

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that you've identified which tickets contain invalid values, <em>discard those tickets entirely</em>. Use the remaining valid tickets to determine which field is which.</p>
# MAGIC <p>Using the valid ranges for each field, determine what order the fields appear on the tickets. The order is consistent between all tickets: if <code>seat</code> is the third field, it is the third field on every ticket, including <em>your ticket</em>.</p>
# MAGIC <p>For example, suppose you have the following notes:</p>
# MAGIC <pre><code>class: 0-1 or 4-19
# MAGIC row: 0-5 or 8-19
# MAGIC seat: 0-13 or 16-19
# MAGIC 
# MAGIC your ticket:
# MAGIC 11,12,13
# MAGIC 
# MAGIC nearby tickets:
# MAGIC 3,9,18
# MAGIC 15,1,5
# MAGIC 5,14,9
# MAGIC </code></pre>
# MAGIC <p>Based on the <em>nearby tickets</em> in the above example, the first position must be <code>row</code>, the second position must be <code>class</code>, and the third position must be <code>seat</code>; you can conclude that in <em>your ticket</em>, <code>class</code> is <code>12</code>, <code>row</code> is <code>11</code>, and <code>seat</code> is <code>13</code>.</p>
# MAGIC <p>Once you work out which field is which, look for the six fields on <em>your ticket</em> that start with the word <code>departure</code>. <em>What do you get if you multiply those six values together?</em></p>
# MAGIC </article>

# COMMAND ----------

nearby_tickets %>%
  inner_join(constraints)

# COMMAND ----------

type_matches <-
  nearby_tickets %>%
  inner_join(constraints) %>%
  count(type_id2, type_id1, type) %>%
  arrange(type_id1, desc(n))
type_matches

# COMMAND ----------

type_matches %>% transmute(candidate_type_id = type_id2, type, n)

# COMMAND ----------

type_matches %>% filter(n == max(n))

# COMMAND ----------

# count_matches <- function(types) {
#   types_df <- enframe(types, name = "type_id2", value = "type")
  
#   inner_join(type_matches, types_df) %>%
#     summarise(n = sum(n)) %>%
#     pull(n)
# }

# COMMAND ----------

# install.packages("gtools")

# COMMAND ----------

# all_types <- unique(type_matches$type)

# COMMAND ----------

# all_types %>% length()

# COMMAND ----------

# MAGIC %md This **will not** work. There are like `2*10^18` permutations.

# COMMAND ----------

# type_perms <- gtools::permutations(n = length(all_types), r = length(all_types), v = all_types) %>% asplit(1)

# COMMAND ----------

# best <- type_perms[[type_perms %>% map_int(count_matches) %>% which.max()]] %>% enframe(name = "type_id2", value = "type")
# best

# COMMAND ----------

# constraints %>% inner_join(best) %>% inner_join(nearby_tickets)

# COMMAND ----------

# result <- your_ticket %>% inner_join(best) %>% filter(str_starts("departure"))
# result

# COMMAND ----------

# result %>% pull(value) %>% reduce(`*`)