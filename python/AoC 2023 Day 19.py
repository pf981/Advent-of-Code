# Databricks notebook source
# %pip install z3-solver

# COMMAND ----------

inp = '''px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
'''

# COMMAND ----------

inp = '''bvh{a>2239:lr,m>657:mqd,x>928:lz,ndn}
lvc{m<3522:R,m>3836:R,A}
tg{x<1026:R,R}
cdj{m<3527:R,x<3765:A,R}
fgz{a>3380:A,a>2932:A,A}
nhq{m>3784:R,R}
sg{x<3555:A,x<3581:R,R}
tjk{x>2771:ktf,hm}
rfh{x>603:R,R}
bdz{x>3391:A,R}
zx{m>1145:A,a>1075:A,m>529:vrz,tfb}
kf{a<3575:R,s>3595:R,A}
czz{x<172:A,a>3342:R,x<192:R,R}
sxc{a>1352:R,R}
kvt{a>989:zx,xz}
vgb{x>3255:bzd,a<3822:gsl,sh}
vt{m>1457:A,R}
nhj{a<3658:cz,qmh}
hjr{a>3504:R,x>2702:rts,s>1565:A,A}
zn{m<1304:qh,x>3016:hdl,vkz}
lkq{a<1430:jtt,jch}
glj{x<3090:cqv,x<3301:A,R}
vvz{m<2273:A,A}
dp{x<3685:R,R}
cx{s>3102:ld,a<282:R,m<872:lrh,jl}
jc{m<2153:R,R}
bn{a<873:R,R}
ss{a<2112:mqb,s<3068:qr,a<2316:A,bg}
xpn{x>1071:A,x>943:kdg,nt}
csn{m>3093:A,m>2870:jgp,x>3644:vbn,gdt}
qsq{a>1809:R,a>942:A,m<2294:rmp,A}
ckq{a>3052:xpl,R}
pz{s<2834:R,m<2267:A,A}
qhb{a>2295:zqv,x<535:rcn,x>839:cxq,xdg}
sl{s<1641:dl,m>3164:dd,jk}
lbn{s<2765:R,m<3450:xd,x<3419:fgt,R}
bdf{m>2402:A,jxs}
ktf{s>572:R,R}
mb{a<848:fn,x<3270:lrd,trh}
nn{s>2206:R,m>2243:R,R}
rm{m<3459:A,s<374:A,s>533:R,R}
sb{s<1930:R,x>2795:R,A}
zsl{m<2345:knh,m>2450:ccn,a<3043:hjx,pzh}
xlt{s<1004:A,A}
jgp{s>612:A,x<3685:A,x<3874:R,A}
lv{x<2654:A,s<373:R,s>637:A,R}
cvx{s>1902:dlc,fgz}
nlk{x<2756:rt,s>1940:R,A}
cgv{x>3786:A,R}
tkr{s>1630:R,R}
pgv{m>683:R,R}
jn{s<3024:R,m<2997:A,R}
ksm{a>3696:R,m<2016:dt,x>3653:A,kf}
gn{m<3698:A,s<689:A,R}
hfq{m>1460:zlk,s>3307:R,s>3163:R,gbh}
cp{x>1638:A,s<1846:A,A}
dq{s<3802:A,R}
pcf{s>626:A,A}
kj{m>1679:R,m>1575:R,s>3295:R,R}
hp{s>3555:zbj,s<3443:pm,m>1583:R,A}
ssf{x<2388:R,m>3241:R,A}
tgc{m>1996:R,R}
lfn{a<1593:A,x<168:R,m<3338:A,R}
mcd{a>283:A,s<1152:R,x>2925:A,R}
zxd{x>2963:A,zs}
ltz{s<3041:nqt,s>3194:R,a<3106:hv,jnk}
vkc{s<809:R,a>1247:A,a>937:R,R}
bqv{m<3558:R,a<3147:R,A}
zz{s<698:tcq,A}
gpf{m>1599:A,a<2224:A,x<3263:A,R}
ch{m>3442:A,x<2694:A,psg}
dvp{a>1685:zq,x<2914:tt,x<3416:flt,fb}
hdr{x>3352:R,s>3033:A,R}
cbs{s>2408:R,a>2448:sr,m<1263:xgz,gdq}
mfj{a<2045:R,s<3005:A,R}
gkr{m>989:R,A}
rsh{m<288:A,ktl}
xhd{m>3255:R,s>1342:A,A}
fnp{m<2834:R,m<2874:R,A}
llm{s<1554:xlt,A}
tf{m>3697:R,R}
ckg{a<3301:A,A}
zg{x>1292:qkr,m>1958:nh,x<1181:R,sdn}
npg{a<3756:A,m<1284:A,x>3508:R,R}
shq{x<3533:A,s<3302:R,s>3766:ks,qkg}
pk{a>3350:A,m<1581:fcn,A}
zv{a<1571:gft,x>3565:vcl,x>3460:vd,gd}
ns{m>1805:R,R}
dkq{s>2813:A,m>3105:A,A}
qfn{a>3519:R,R}
rrx{a<3693:A,s>764:R,a<3764:A,A}
mpp{a>380:R,s>3556:A,a>202:A,A}
vrr{m<3344:A,R}
kmt{m>1991:R,A}
mvd{x<2854:A,a>2546:A,s>3317:A,A}
kdg{a>393:R,x<1023:A,R}
pvk{m>628:A,s<856:A,R}
gl{s<3816:A,R}
msq{x>2513:R,qkp}
drd{a<2448:A,a>2626:A,A}
tfb{s>1437:R,x<2689:R,R}
ghm{a>609:A,s<913:A,R}
jzx{a<3475:rl,x<2781:R,m<886:vql,A}
vd{a>2455:vp,x<3521:sth,x>3541:jvd,shq}
xnc{s>2873:R,m<3301:R,R}
mnd{m<1188:lp,A}
cqh{x<3626:A,a>413:vft,qrv}
pf{s<1807:A,s<1965:A,a<355:R,R}
cfc{s>1715:A,x>3628:A,R}
qh{m<836:rrb,m>1045:A,xdv}
tn{x<2760:nn,x<2817:cvf,hmj}
fgt{x>3402:R,R}
xl{a<1144:R,a<1630:R,A}
nlx{a>3248:tdb,x<2881:A,x<3079:lrx,gkr}
hzs{x<2548:fnp,mhd}
fcn{s>2770:R,R}
qm{s>2880:A,x>3027:R,A}
xdg{a>1200:jhv,x>701:dkn,m>2943:rfh,qqf}
xt{x>2825:R,A}
flt{x<3118:vb,mb}
fht{m<621:vzd,gsq}
zsh{s>2543:R,a>325:A,x<2680:R,R}
jl{s<2357:A,s<2803:R,A}
dld{m<1899:xvl,m<2165:qjg,s<3363:fs,zsl}
zs{a>3396:A,m>3659:A,R}
vc{a>664:A,m>870:R,A}
qnc{x<2599:A,A}
dc{x<2762:A,R}
jvb{x>2479:R,A}
nbr{s>1019:A,x>2914:R,A}
gdt{m<2748:R,s>670:R,A}
zp{a<1263:R,jjd}
jhx{m>414:A,x<2984:A,a<1153:A,R}
nnv{s>2001:R,A}
tsz{s>2339:xb,ssn}
vkz{s>1034:bzf,s>364:vkc,a>1136:A,A}
lfz{a>1346:np,m>2295:R,s<1982:A,pz}
nhb{m<1097:R,A}
xgh{x<2794:A,jd}
rgb{s<1936:R,a>2458:A,A}
psg{a<323:R,x>2938:A,A}
mhd{x<2688:A,R}
tcq{m<1167:A,a<1907:A,x<3595:A,R}
fsk{x<2695:A,R}
pmf{x<3777:ht,a>454:A,bhc}
shh{m<3342:nb,zxc}
xgz{m>1109:R,A}
fnq{a<1688:dj,mxs}
jq{x>1016:kk,m<1055:kbz,x>633:tb,zhh}
ht{x<3549:R,A}
jvm{s<2477:A,s>3182:qp,dg}
bh{s<3164:R,A}
mdf{a>439:vmt,m>2154:A,gmg}
kzl{m<296:R,m>464:R,A}
xk{s>3761:A,a>861:A,R}
qjg{a<2969:mrl,a<3461:bgr,x>3035:ksm,kcr}
bkz{m>3278:xpz,m>2939:ngg,m<2760:qnc,hzs}
hfl{a>873:R,s<2216:nnv,s>2340:txj,lsl}
db{a>759:ffr,a<349:cp,m>3429:ct,A}
xpz{x>2686:A,m<3731:A,gzf}
xmb{a<3362:fbb,a<3622:dgx,mv}
zq{x>3004:shh,a<2969:sl,s>847:ncn,xmb}
nz{a>244:zsh,m<338:R,m<526:R,bb}
cph{a<1100:A,A}
bnp{m>3344:R,R}
jml{x>3702:R,s<1822:A,x>3684:R,R}
mfd{m>920:xkr,lj}
pth{s<3135:A,A}
fng{a>2047:prt,db}
vb{s<1084:th,x>3036:rd,s<1810:bx,hfl}
dsn{a<1829:bff,m<3342:R,m>3620:A,rmv}
xgf{x>3811:R,m<3300:jkg,R}
bg{m>1235:A,s<3234:R,R}
bs{s<3712:R,R}
qr{m>1218:A,m>1067:R,s>2909:A,A}
gzf{a>1115:R,m<3891:A,m<3954:A,A}
rgr{a<2087:R,s>3052:R,R}
hx{s<3015:R,R}
jqt{a>2803:A,s<3582:cs,R}
mk{x>3595:sd,x<3419:qrq,x<3482:xtr,lnn}
sd{x>3749:nv,a>1076:R,x>3647:jml,cfc}
sdv{m>1565:jnr,m>895:cbs,m>394:skm,fmt}
jf{m<3278:A,m<3424:R,A}
ccn{m>2523:A,x<3148:R,a<3000:R,tv}
gh{x>2628:A,m>1349:bsr,m<797:A,jvb}
kft{a>3416:A,m<1970:R,m<2081:R,A}
jxs{x<2430:A,a>1099:A,s>2137:A,R}
bcz{m>956:fzz,a>3313:R,pfj}
sh{x<2776:xr,s<852:cxt,s<1257:lbg,hs}
vzd{m>491:A,A}
bc{m>2483:R,s<2926:R,a>1764:R,R}
js{s<1655:A,m<2440:zjz,bc}
hd{a<3067:R,x>3389:kj,m>1683:pt,lbz}
jb{a>2914:A,a>2692:R,x<353:A,R}
pmc{a<3103:jdq,a>3609:vgb,x<3373:fj,kgl}
bgh{x>1677:kb,R}
cc{a>1023:dvj,s>3290:bm,qm}
tdx{x>2659:A,x<2546:R,A}
fr{m>3238:xl,a<1325:bn,x>2169:R,fgl}
jnk{s>3100:A,s>3078:R,a<3586:A,R}
qqt{m>2206:R,R}
vql{x<3126:R,R}
pjl{m<2710:R,A}
ktl{a>3299:A,A}
ssn{m<1673:R,a>1014:A,x<2800:A,xt}
lzk{s>2525:A,a<393:A,A}
zhh{s<1976:hf,pk}
ct{a>616:R,R}
gft{a<822:tm,x<3665:cfr,s<3061:cgv,xgf}
jnr{a<2376:gls,A}
fs{x>3419:zb,x<2893:dfx,glj}
hf{s<805:R,x<319:A,A}
xpg{a>3639:A,x<3156:A,s>3916:A,R}
bb{x<2802:R,s>2772:A,A}
pfj{x<2706:R,m<599:R,m<737:R,R}
vp{m>3406:tf,R}
pgg{x<3332:vn,zv}
ghc{x>2607:gn,m>3602:nhq,R}
gbh{a>380:A,x<2772:R,s<3097:A,R}
tt{s>1475:bkz,hz}
mp{a<802:ch,fsk}
vft{x<3770:A,s>1016:A,m>731:A,R}
jqs{s<2276:kn,s>3356:nxx,a>942:nhb,A}
dlx{x<2602:A,x>2784:R,s<1869:A,R}
dg{x>2712:R,a<1405:A,m<895:A,A}
lmz{x>2788:A,A}
nb{x>3660:A,m<2890:A,A}
lk{m<1416:A,A}
sbp{x>3365:A,a>2600:hdr,R}
gg{s<2388:zn,a>1194:lkq,m>939:qqd,cc}
sx{m>3504:hmz,a>2254:jxj,fr}
zqp{s<470:R,A}
skm{s>2494:R,x>3186:R,s<2079:A,A}
qc{m>2795:A,s<1753:R,A}
bgr{x>3148:kmt,s<3455:A,a<3281:A,gkl}
cg{s>3909:A,A}
jg{s<1706:cb,A}
lkg{x>3557:R,s>3305:A,R}
vnx{a<2212:R,s>3497:R,m>3416:A,R}
dd{s>2093:A,rgb}
rsm{a<3187:R,x>3774:R,A}
tdb{s<1543:R,R}
bm{m>468:R,m>264:qkf,R}
mvc{m<1938:R,x<2565:A,x>2596:A,A}
bzf{m<1960:R,a>1324:A,a>992:A,R}
gc{m<1620:R,A}
ndn{m>514:R,A}
rx{m>2233:gt,mc}
czk{s>3051:R,x>3549:R,A}
mqb{x>2689:A,x>2491:A,A}
hz{x>2704:sc,x<2525:pj,m>3351:ghc,pcf}
qp{m>699:R,a>1489:A,A}
qhq{m<1003:R,s<291:R,m<1197:R,A}
fbb{x<2694:hb,m<3356:dqr,x>2823:hbl,pq}
fmt{x>3448:A,jrm}
xkr{m>1381:xkt,jqs}
mv{m<3359:lv,m<3587:gp,R}
pzh{s<3687:R,s>3867:xpg,s>3763:gl,R}
bsr{a<526:A,A}
mnh{s<712:gqf,bt}
brh{x>1231:A,x<1214:R,m<3153:A,R}
bx{a<588:ldl,xhd}
mxs{s<1828:pmc,s<2828:ktp,m>1446:dld,vpq}
ks{a<1931:R,A}
vmt{a>568:A,m<1947:R,R}
hcj{s>3395:xk,x<3084:A,A}
nh{a<3320:R,A}
rt{x<2548:A,s>2169:R,a>3333:A,R}
sf{m<2732:A,x>1877:R,x<1818:A,R}
ng{x<3516:R,A}
rrb{x<3017:R,m<401:A,R}
vn{a<2321:mp,slz}
jdq{s>1155:gpf,x<3233:nzm,a>2272:mnh,zz}
hmj{s<1338:A,A}
pgt{a>1875:R,R}
cqv{s>3177:A,x>2993:R,x<2951:R,A}
fb{s>1503:hj,psb}
lr{s<2448:R,R}
hjx{s<3654:fkc,s<3783:mr,R}
zxc{s<1084:zqp,R}
nqt{s>2899:R,s<2861:R,a<3115:R,R}
knh{s<3734:A,x>3343:cg,R}
jxj{x<2157:jf,s<1775:A,A}
cl{m>2525:kc,m>2331:tsc,dfv}
kk{s>1682:zf,x>1833:bmn,m<1482:lhf,zg}
vg{x<856:bzr,m<1358:R,nj}
dfx{x<2661:R,x<2780:A,a<2964:A,A}
bj{x<3630:A,x>3825:A,A}
fj{s<1107:xgh,a<3377:nlx,s>1352:hjr,jzx}
zbl{a>3724:R,A}
tk{x<2233:A,A}
xv{m>3202:ghm,x>3613:R,pv}
xbz{s>3076:dc,x<2699:mjz,zt}
gsq{a>603:R,R}
pn{m<576:R,tx}
gkl{s>3784:A,s>3651:A,A}
th{x<2984:A,m<3145:R,a>978:sjl,R}
jch{s<3408:R,m>1482:bs,R}
fzz{m>1216:A,x<3019:R,R}
xz{s>2365:A,R}
rmp{a>614:A,m>2256:A,a<284:R,R}
rmv{s>2125:A,R}
fn{a<402:R,m>3238:A,A}
rl{m<1419:A,a>3438:A,s<1225:A,A}
cfr{a>1108:ng,R}
kcr{m<2028:cch,R}
rcn{s<2490:gcc,a<828:hg,m>2936:rz,bl}
zzv{m<1061:zp,x>2505:fgp,m>2066:bdf,jmt}
dj{x>3131:cxz,a<769:tjx,x<2858:pbb,gg}
fc{m<2765:R,m<2875:R,A}
fsm{a>1876:A,R}
qmh{a>3858:R,m<1407:A,x<3393:qxk,A}
dl{m>3175:lqm,m<2786:dm,x>2607:R,R}
gqf{s<423:R,m<1032:R,a>2568:R,A}
sn{x<2667:A,s>1983:A,a>268:R,R}
qxk{a>3790:A,A}
kn{a<1132:R,m>1117:A,s>1328:A,R}
lrh{s<2139:A,A}
xpl{x>870:A,a>3495:R,x>741:A,A}
gsl{m>1446:rrx,x>2695:nbr,x<2486:R,A}
lbg{m<1051:R,s<1101:A,A}
hbl{a>3105:A,m>3713:R,A}
qlh{s<988:A,x<3705:A,x<3821:gvt,gc}
xvl{x>2956:hd,m>1654:bhd,s>3297:hp,ltz}
pp{m>1828:A,a>1113:R,R}
xmx{a<763:R,m>3395:A,a<1219:A,A}
pps{x<3587:R,qhq}
gvt{m<1547:R,A}
jxt{s<3914:pgt,x<3800:R,x<3911:R,A}
jk{a>2287:tdx,R}
ld{x<3494:R,a>238:A,R}
dhp{m>2698:tpn,kjc}
px{m>1649:tn,jvm}
cv{m<1622:R,m>1794:R,a>1456:R,R}
prt{a<2869:drd,R}
dgx{x<2756:A,x>2851:qfn,x>2811:rm,lmz}
tsc{x>1964:js,s<1509:kg,bgh}
qz{x<1916:fng,sx}
fbn{x>435:A,a>1351:A,s>3219:R,R}
rd{x<3083:xmx,a>869:R,R}
dqr{x<2806:A,x>2934:R,x>2882:R,R}
tv{x>3637:R,m<2478:R,A}
jtt{s>3378:cn,R}
gdq{a>2010:R,a<1818:R,s>2201:A,R}
kgl{s>704:cdx,m<1565:pps,a<3408:grr,zsz}
ts{a>3653:A,x>2607:A,x>2449:A,ssf}
lsl{s<2298:R,R}
bmn{m<1347:rmg,R}
ncn{s<1506:ts,nlk}
dt{m>1954:R,R}
nq{m>1522:A,R}
zt{x>3010:A,a>2223:A,s<2932:R,R}
tpn{a<1472:R,m>2812:R,A}
ktd{m>861:svk,ckl}
ngg{a<567:sn,dlx}
ntf{m<2043:R,a>2432:R,m>2092:R,R}
gt{x<1439:qhb,m>2958:qz,cl}
mrl{s>3241:ntf,tgc}
sth{m>3169:rgr,a<2019:A,R}
lnn{s>2239:vt,sg}
rj{x>2631:mcd,cr}
tm{s<3119:R,m>3116:cdj,m<2921:R,mpp}
lhf{a<3420:pvk,zbl}
hdl{m>2092:R,a<1338:pp,cv}
mz{x>2186:A,m<3822:R,R}
xdv{m<945:A,A}
vgk{x<2421:A,x<2484:A,m>3387:A,A}
zqv{x>484:vrr,snc}
jvd{s>3100:fsm,a>2092:dkq,xnc}
vpq{s>3342:ssj,x>3371:ktd,xg}
xs{a<530:R,x>616:A,R}
sc{s<752:qnf,s<1016:R,A}
hs{a<3909:R,m>1706:A,a<3965:A,A}
pt{x>3152:A,A}
lrd{x>3187:gvd,m>3324:A,x>3159:A,A}
lrx{x>2995:R,A}
lp{a<362:A,A}
zjq{m<1095:R,s>3039:R,vxf}
xr{m<1531:R,A}
xd{m>3024:A,x>3428:A,A}
gcc{a<1159:R,x<344:tkr,a<1700:A,fnm}
bhd{m>1783:R,x>2709:mvd,a<2910:A,R}
vrz{m<775:R,A}
xb{s<3443:R,s<3683:A,R}
kb{s>2920:R,s>2178:A,A}
kff{a<270:lkg,a<455:qqt,R}
ldl{x>2958:A,A}
pvm{s<3011:R,a>2514:A,x<3584:R,A}
cxt{s<296:A,a<3939:R,R}
nzm{x<2673:qg,s>592:lk,qdv}
mjz{a<2191:R,m<404:A,x<2559:A,R}
jlt{x<724:A,A}
jkg{m<3005:R,s<3469:R,m>3115:A,R}
cn{a<1289:R,m>1550:A,A}
rz{x<335:lfn,m>3549:fbn,A}
lbp{s<2281:sb,a>387:gh,m>896:cf,nz}
gvp{m<1705:cx,s<2914:pb,kff}
zb{m>2371:hx,a<3166:pth,x<3643:czk,R}
bjc{a<3135:A,x>3602:A,A}
jr{s<3677:A,a<3134:R,A}
rmg{a<3171:R,A}
ds{s>3580:R,a<2024:A,m<3073:R,vnx}
cr{x>2528:R,a<498:A,A}
kc{x>1752:mx,dhp}
qqd{a>998:ns,x>3001:hcj,x<2908:bh,bq}
mqd{m<774:R,a>1934:R,A}
nnk{x>3584:A,A}
nxx{a>1011:R,s<3732:R,A}
qg{a>2512:R,A}
dlc{x<823:R,R}
dkn{a>466:R,R}
hmz{s<1437:mz,m>3748:A,A}
pq{s>294:R,a<3111:A,R}
svk{m<1197:pvm,m>1307:rsm,s>3088:A,A}
kg{m<2448:A,a>2606:R,R}
grq{x>2855:A,a<479:R,vc}
np{x<1676:A,x>1783:A,s>2424:A,R}
cxz{a>675:mk,s>1575:gvp,td}
slz{m<3069:hmh,s>3119:bqv,x>2727:zxd,msq}
dvj{s<3181:cph,a>1130:jhx,m>619:R,kzl}
hl{x<3826:dp,s<983:ttf,x<3931:jc,A}
xg{a>2686:bcz,m<892:xbz,x>3015:zjq,ss}
td{m<1331:cqh,x<3520:mdf,m>1875:hl,qlh}
jrm{x>2857:A,A}
hm{a<314:R,m<1407:R,A}
fv{x>1294:sxc,x<1251:brh,xxp}
jhv{s>2361:jn,jlt}
snc{x>224:jb,x<97:A,m>3170:R,czz}
jx{x<3462:A,m>1367:A,A}
lqm{s<898:A,m<3554:A,m>3724:R,R}
nv{s>2479:R,s>1416:R,a>1205:A,A}
sr{x<3209:A,a<2927:A,s<2170:R,A}
txj{a>526:R,m>3518:A,A}
xxp{m<3052:A,A}
lz{a<2066:R,m>563:A,R}
qdv{m<1245:R,A}
hb{s<377:R,s<680:R,R}
mx{x>2100:tk,a>2427:qc,x<1966:sf,fc}
vxf{m<1295:A,m<1391:A,R}
bz{s>941:rj,tjk}
jmt{m>1556:A,A}
vcl{s<3447:lvc,a>2420:zgp,s<3755:ds,jxt}
xkt{m>1804:A,A}
nc{x<2556:R,x>2587:A,A}
bff{m>2907:R,R}
lbz{m>1539:A,x>3110:A,x<3053:R,A}
fgl{m>3077:A,x>2072:A,m>3031:R,R}
gvd{m<3092:A,s>888:A,R}
scx{a<2488:A,R}
dfv{x<1964:lfz,x<2157:qsq,vvz}
ckl{x>3751:R,s<3110:nnk,a>3077:A,A}
bhc{a>172:R,A}
cdx{m<1618:A,m>2179:A,kft}
gls{x>3035:R,m>2141:R,m<1850:A,A}
kjc{a>1575:R,x>1633:A,x>1542:R,R}
gd{s>3236:fp,x>3386:lbn,s<2891:jdd,sbp}
hj{a>1015:bnp,pmf}
in{x<2351:rx,m>2575:dvb,fnq}
zf{x>1686:R,R}
lj{m<419:tg,a<1215:fht,a>1779:bvh,pgv}
cf{x<2711:A,R}
cs{s>3433:A,s<3377:A,A}
zbj{a<2916:A,x<2738:A,A}
qqf{m>2571:A,s>1961:A,xs}
qrq{a<1274:A,ddp}
sdn{x>1247:R,a>3428:A,R}
ttf{a>364:A,R}
gp{x>2698:A,R}
qrv{m>723:R,A}
fkc{s<3545:R,R}
ssj{x<3130:jqt,bjc}
bq{s<3307:A,x<2947:A,R}
cvf{a<1453:R,x<2786:A,s>2023:R,R}
qkr{m>1829:R,R}
psb{a>764:csn,a>489:xv,bj}
kbz{m<444:rsh,x<442:jg,m>660:cvx,pn}
vbn{s>875:A,A}
dm{s<921:R,m<2647:R,x<2754:R,A}
khc{s<3674:hfq,s<3832:mnd,grq}
hv{m>1580:R,s>3096:A,m<1509:A,A}
zlk{m<2182:R,A}
fp{x<3415:jr,R}
pj{a>602:vgk,A}
bt{x<3695:A,R}
tp{m>1231:A,a>1380:A,m>686:R,A}
ktp{a<3203:sdv,nhj}
dz{a<3459:R,x<3125:R,A}
zgp{x<3735:R,dq}
hg{s<3383:R,a>512:A,R}
cxq{x>1204:fv,a<1043:xpn,dsn}
zjz{x<2184:R,R}
fgp{m<1737:nc,m>2279:R,mvc}
pm{a>2514:A,m<1528:R,R}
qkf{x>2974:A,x<2903:R,a<916:R,R}
jd{m>1066:R,R}
tjx{s<1467:bz,s<3032:lbp,khc}
pv{x<3495:R,A}
nj{a>3474:A,A}
trh{a<1401:R,x>3354:bdz,s<1484:R,A}
qkp{s<2889:A,m>3449:R,x<2449:R,A}
cch{m>1983:R,a<3715:R,A}
xtr{x>3443:jx,x>3429:nq,a<1025:R,tp}
rts{s>1656:R,s<1455:R,A}
pbb{x<2618:zzv,a>1190:px,x>2753:tsz,kvt}
cb{a>3424:R,s<978:R,s>1461:A,R}
tb{m>1654:ckq,a>3098:vg,llm}
qkg{a<2067:A,m<3066:R,R}
mr{x>3315:R,A}
ffr{a>1577:R,A}
pb{s>2249:lzk,pf}
cz{s<2209:dz,A}
ddp{m<946:R,s>2328:R,A}
bzr{a<3464:R,x<744:A,R}
jdd{s>2693:R,scx}
mc{a<2569:mfd,jq}
gmg{a>245:R,R}
nt{x>897:R,a<564:A,R}
tx{a>3060:R,a<2896:A,x<650:A,A}
grr{m<2028:ckg,A}
dvb{s<2516:dvp,pgg}
fnm{s>961:R,R}
qnf{m>3357:R,R}
bl{a<1446:A,a>1797:mfj,A}
hmh{m>2814:A,a<3083:pjl,R}
zsz{s<272:A,x<3644:R,R}
sjl{a<1275:R,s>629:R,x>3029:A,R}
bzd{x<3693:npg,R}
jjd{x<2486:A,m>459:R,a>1413:R,A}

{x=33,m=357,a=898,s=123}
{x=1453,m=618,a=175,s=457}
{x=1972,m=3090,a=3668,s=2207}
{x=780,m=1219,a=67,s=462}
{x=259,m=606,a=1493,s=225}
{x=920,m=190,a=381,s=1044}
{x=1082,m=2606,a=67,s=753}
{x=1790,m=1604,a=2545,s=1297}
{x=770,m=1139,a=896,s=812}
{x=250,m=2173,a=1294,s=2757}
{x=107,m=1176,a=2753,s=382}
{x=409,m=2,a=259,s=2158}
{x=1207,m=282,a=1739,s=1328}
{x=283,m=807,a=1577,s=740}
{x=420,m=978,a=1691,s=3093}
{x=616,m=1493,a=2390,s=318}
{x=245,m=111,a=841,s=21}
{x=109,m=584,a=3124,s=296}
{x=3775,m=334,a=862,s=461}
{x=870,m=1050,a=293,s=5}
{x=194,m=24,a=564,s=66}
{x=431,m=210,a=1053,s=664}
{x=40,m=320,a=497,s=614}
{x=50,m=2257,a=976,s=414}
{x=367,m=1571,a=1774,s=2559}
{x=1987,m=1832,a=2265,s=776}
{x=1132,m=553,a=192,s=320}
{x=1153,m=1951,a=2569,s=1089}
{x=174,m=239,a=576,s=704}
{x=1139,m=2918,a=2901,s=1685}
{x=1527,m=6,a=129,s=946}
{x=1279,m=921,a=110,s=1479}
{x=1517,m=1295,a=2094,s=78}
{x=1821,m=1679,a=441,s=95}
{x=169,m=504,a=559,s=2508}
{x=1904,m=2298,a=1261,s=170}
{x=851,m=888,a=2152,s=1059}
{x=2080,m=572,a=914,s=52}
{x=2278,m=2282,a=82,s=204}
{x=1232,m=2262,a=120,s=2218}
{x=60,m=1237,a=1518,s=407}
{x=2382,m=1561,a=1366,s=1330}
{x=111,m=732,a=1467,s=3850}
{x=584,m=1484,a=141,s=356}
{x=673,m=741,a=148,s=904}
{x=1617,m=243,a=1375,s=181}
{x=1818,m=1499,a=896,s=6}
{x=1578,m=1155,a=942,s=30}
{x=1315,m=360,a=548,s=1010}
{x=1019,m=2956,a=1568,s=57}
{x=1615,m=733,a=134,s=685}
{x=356,m=2178,a=3022,s=304}
{x=531,m=829,a=2076,s=218}
{x=752,m=918,a=284,s=228}
{x=137,m=2006,a=1010,s=1500}
{x=456,m=1022,a=2627,s=11}
{x=3210,m=101,a=779,s=52}
{x=1284,m=50,a=858,s=2112}
{x=1645,m=413,a=141,s=978}
{x=307,m=406,a=835,s=1663}
{x=1989,m=467,a=225,s=2764}
{x=45,m=2922,a=1346,s=628}
{x=435,m=968,a=909,s=901}
{x=1176,m=264,a=10,s=1248}
{x=1868,m=1276,a=572,s=14}
{x=298,m=801,a=271,s=2182}
{x=83,m=31,a=585,s=809}
{x=659,m=1281,a=645,s=2758}
{x=2628,m=23,a=1733,s=98}
{x=250,m=2089,a=669,s=493}
{x=426,m=3398,a=241,s=1111}
{x=1278,m=3059,a=931,s=2271}
{x=2272,m=1061,a=65,s=3471}
{x=1047,m=2577,a=912,s=951}
{x=30,m=779,a=2106,s=1509}
{x=33,m=787,a=870,s=13}
{x=311,m=88,a=463,s=449}
{x=2253,m=351,a=240,s=306}
{x=305,m=830,a=1168,s=67}
{x=267,m=2168,a=1911,s=161}
{x=44,m=1491,a=309,s=1721}
{x=533,m=33,a=2481,s=944}
{x=199,m=3230,a=1317,s=917}
{x=1216,m=266,a=969,s=15}
{x=1913,m=824,a=66,s=2265}
{x=82,m=309,a=122,s=536}
{x=11,m=164,a=1031,s=509}
{x=2639,m=812,a=16,s=519}
{x=158,m=2246,a=615,s=497}
{x=385,m=1347,a=1169,s=1482}
{x=435,m=1054,a=401,s=604}
{x=290,m=881,a=418,s=1910}
{x=187,m=353,a=752,s=613}
{x=299,m=437,a=1768,s=364}
{x=582,m=1584,a=2231,s=43}
{x=26,m=1826,a=42,s=3069}
{x=378,m=2044,a=1066,s=718}
{x=415,m=177,a=227,s=2249}
{x=2579,m=111,a=2103,s=128}
{x=381,m=1157,a=244,s=14}
{x=398,m=74,a=236,s=79}
{x=46,m=2441,a=1628,s=265}
{x=1383,m=211,a=540,s=343}
{x=154,m=2357,a=415,s=29}
{x=1754,m=3533,a=243,s=1388}
{x=2427,m=142,a=1111,s=634}
{x=173,m=2911,a=874,s=1747}
{x=1165,m=573,a=160,s=85}
{x=770,m=421,a=710,s=1131}
{x=446,m=316,a=41,s=153}
{x=999,m=514,a=233,s=525}
{x=958,m=1257,a=3276,s=34}
{x=1797,m=1404,a=376,s=213}
{x=708,m=912,a=2285,s=337}
{x=1405,m=2061,a=2656,s=2322}
{x=1870,m=1356,a=2084,s=282}
{x=27,m=1130,a=421,s=865}
{x=575,m=153,a=153,s=1204}
{x=792,m=1531,a=681,s=1596}
{x=2028,m=932,a=679,s=1097}
{x=534,m=1484,a=1589,s=2340}
{x=21,m=919,a=498,s=167}
{x=741,m=486,a=328,s=3289}
{x=16,m=820,a=3480,s=277}
{x=3038,m=31,a=1694,s=261}
{x=1598,m=886,a=374,s=1815}
{x=532,m=806,a=87,s=1452}
{x=169,m=632,a=1226,s=1476}
{x=1215,m=183,a=649,s=1033}
{x=21,m=146,a=955,s=55}
{x=598,m=45,a=2787,s=475}
{x=130,m=1341,a=230,s=269}
{x=657,m=2747,a=75,s=104}
{x=554,m=2842,a=121,s=1221}
{x=116,m=361,a=1298,s=778}
{x=1203,m=622,a=741,s=1971}
{x=1243,m=2374,a=1145,s=158}
{x=175,m=2121,a=2383,s=392}
{x=524,m=176,a=307,s=681}
{x=241,m=214,a=1906,s=745}
{x=828,m=32,a=1041,s=220}
{x=103,m=1861,a=102,s=669}
{x=173,m=639,a=1805,s=321}
{x=798,m=1205,a=47,s=225}
{x=46,m=332,a=2653,s=157}
{x=2780,m=236,a=1279,s=94}
{x=1496,m=2402,a=867,s=3020}
{x=1704,m=37,a=408,s=30}
{x=1598,m=607,a=11,s=418}
{x=141,m=1980,a=113,s=579}
{x=457,m=134,a=1748,s=81}
{x=1501,m=1593,a=2275,s=344}
{x=1453,m=347,a=82,s=1996}
{x=1124,m=1346,a=5,s=3303}
{x=734,m=1555,a=593,s=404}
{x=1615,m=2,a=58,s=424}
{x=353,m=1325,a=4,s=129}
{x=572,m=668,a=5,s=275}
{x=277,m=1778,a=635,s=611}
{x=2258,m=92,a=1550,s=70}
{x=106,m=1066,a=139,s=2387}
{x=462,m=407,a=1397,s=206}
{x=833,m=20,a=2708,s=440}
{x=490,m=2711,a=145,s=97}
{x=2125,m=2187,a=1647,s=2103}
{x=361,m=2744,a=46,s=355}
{x=189,m=1302,a=689,s=920}
{x=1811,m=1399,a=1828,s=47}
{x=1905,m=1406,a=71,s=1775}
{x=754,m=561,a=3656,s=180}
{x=517,m=1143,a=772,s=164}
{x=283,m=2697,a=493,s=1224}
{x=1149,m=987,a=736,s=149}
{x=1641,m=308,a=2931,s=49}
{x=1398,m=1135,a=1772,s=3182}
{x=283,m=444,a=1397,s=870}
{x=93,m=857,a=31,s=213}
{x=210,m=1988,a=470,s=10}
{x=697,m=2815,a=1678,s=3250}
{x=581,m=23,a=121,s=221}
{x=48,m=632,a=784,s=1}
{x=19,m=512,a=2035,s=408}
{x=793,m=524,a=2589,s=337}
{x=667,m=590,a=280,s=616}
{x=944,m=562,a=557,s=740}
{x=1946,m=1222,a=3295,s=592}
{x=1389,m=1113,a=234,s=211}
{x=109,m=1582,a=100,s=633}
{x=221,m=2427,a=55,s=450}
{x=220,m=205,a=2606,s=1328}
{x=1654,m=1259,a=2285,s=399}
{x=439,m=1227,a=204,s=622}
{x=1537,m=1443,a=281,s=912}
{x=1014,m=1216,a=2955,s=123}
{x=43,m=868,a=1713,s=280}
{x=2107,m=3147,a=1519,s=1143}
{x=2285,m=201,a=1185,s=832}
{x=139,m=604,a=3479,s=246}
{x=2111,m=613,a=29,s=1234}
{x=115,m=417,a=746,s=1991}
'''

# COMMAND ----------

import re

workflows_raw, objs = inp.split('\n\n')
objs = eval('[' + objs.replace('=', ':').replace('\n', ',')[:-1].replace('x', '"x"').replace('m', '"m"').replace('a', '"a"').replace('s', '"s"') + ']')

workflows = {}
for line in workflows_raw.splitlines():
  name, rest = line.split('{')
  parts = []
  for part in rest[:-1].split(','):
    parts.append(part.split(':'))
  workflows[name] = parts
# workflows

# COMMAND ----------

def resolve(obj, w):
  if w in 'AR':
    return w
  for part in workflows[w]:
    if len(part) == 1:
      return resolve(obj, part[0])

    x = obj['x']
    m = obj['m']
    a = obj['a']
    s = obj['s']
    if eval(part[0]):
      return resolve(obj, part[1])

accepted = 0
for obj in objs:
  if resolve(obj, 'in') == 'A':
    accepted += sum(obj.values())

accepted

# COMMAND ----------

# import z3

# X = z3.Int('X')
# M = z3.Int('M')
# A = z3.Int('A')
# S = z3.Int('S')
# # Eh, I don't think z3 can COUNT solutions

# COMMAND ----------

import math

def count_solutions(ranges, w):
  if any(end <= start for start, end in ranges.values()):
    return 0
  if w == 'A':
    print(ranges)
    return math.prod(end - start for start, end in ranges.values()) # Is it really just the sum of these options? I think it must be because these are DISJOINT
  if w == 'R':
    return 0

  n_solutions = 0
  for part in wfs[w]:
    if len(part) == 1:
      return n_solutions + count_solutions(ranges, part[0])

    c, op, val = part[0]
    next_w = part[1]
    
    if op == '<':
      #if val < ranges[c][1]:
      if ranges[c][0] < val <= ranges[c][1]:
      # if val <= ranges[c][1]:
        n_solutions += count_solutions({x: y.copy() if x != c else [y[0], val] for x, y in ranges.items()}, next_w)
        ranges[c][0] = val
    if op == '>':
      #if val >= ranges[c][0]:
      if ranges[c][0] <= val < ranges[c][1]:
      # if val+1 >= ranges[c][0]:
        n_solutions += count_solutions({x: y.copy() if x != c else [val+1, y[1]] for x, y in ranges.items()}, next_w)
        ranges[c][1] = val+1
    
  
import re
def split_part(parts):
  if len(parts) == 1: return parts
  els = re.match(r'([xmas])([<>])([0-9]+)', parts[0]).groups()
  els = (els[0], els[1], int(els[2]))
  return [els, parts[1]]
wfs = workflows
wfs = {name: [split_part(part) for part in parts] for name, parts in workflows.items()}

count_solutions({'x':[1, 4001], 'm':[1, 4001], 'a':[1, 4001], 's':[1, 4001]}, 'in')

# COMMAND ----------

# %pip install PySMT
