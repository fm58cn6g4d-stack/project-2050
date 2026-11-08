#!/usr/bin/env python3
"""Exploratory scenario estimate of the Senate in January 2029, from the 2028 map.

Role: the arithmetic behind dossiers/scenario/5-senate-2028.md. Status: exploratory (stage B follow-up,
November 8, 2026); not a core model and not a forecast. Inputs are typed in below from the sources that
file cites: 2024 presidential margins, unofficial 2026 statewide margins (NBC, read 2026-11-08), and the
project's own incumbency adjustments (labeled assumptions). Recheck once 2026 results are certified.

Method: each seat's expected Democratic margin is a blend of the state's 2024 presidential lean (weight 0.7)
and its 2026 statewide results relative to the national House vote (weight 0.3), plus the national
environment E (the 2028 Democratic presidential margin) and an incumbency adjustment. Each run draws a
national error (SD 2.5) shared by all seats and a state error (SD 7). Democrats not up in 2028: 38 if
Republicans win the uncalled 2026 Alaska and Mississippi seats, 40 if Democrats win both.

  python3 dossiers/scenario/tools/senate_2028_sim.py      (standard library only; about a minute)
"""
import random, math, statistics as st
ENVS=(-3,0,3,6)  # 2028 national environment, Democratic presidential margin in points
NAT24=-1.48  # 2024 national D margin
NAT26=13.0   # prelim 2026 House D margin (IBTimes, prelim)
# state: (inc party, pres24 D margin, [2026 statewide D margins], incumbency adj toward D (+ = helps D), note)
S={
'AL':('R',-30.47,[-9.4,-4.0],-3,'Britt'),
'AK':('R',-13.13,[0.3],-4,'Murkowski (unique brand)'),
'AZ':('D',-5.53,[13.1],3,'Kelly'),
'AR':('R',-30.64,[-11.9,-15.3],-3,'Boozman'),
'CA':('D',20.14,[31.0],3,'Padilla'),
'CO':('D',10.99,[25.4,27.8],3,'Bennet'),
'CT':('D',14.51,[19.2],3,'Blumenthal'),
'FL':('R',-13.10,[-2.9,-1.3],-2,'Moody'),
'GA':('D',-2.20,[18.0,8.6],3,'Warnock'),
'HI':('D',23.11,[45.2],3,'Schatz'),
'ID':('R',-36.49,[-23.0,-24.8],-3,'Crapo'),
'IL':('D',10.90,[24.3,23.5],3,'Duckworth'),
'IN':('R',-18.96,[],-3,'Young'),
'IA':('R',-13.21,[4.1,11.0],-1,'Grassley (age 95 in 2028; treated as likely open)'),
'KS':('R',-16.12,[5.0,0.6],-3,'Moran'),
'KY':('R',-30.53,[-12.1],-3,'Paul'),
'LA':('R',-22.01,[-1.8],-3,'Kennedy'),
'MD':('D',28.54,[31.6],3,'Van Hollen'),
'MO':('R',-18.41,[],-3,'Schmitt'),
'NV':('D',-3.10,[7.6],3,'Cortez Masto'),
'NH':('D',2.78,[13.7,-4.3],3,'Hassan'),
'NY':('D',12.60,[19.6],3,'Schumer'),
'NC':('R',-3.21,[19.6],-3,'Budd'),
'ND':('R',-36.45,[],-3,'Hoeven'),
'OH':('D',-11.21,[4.8,7.9],3,'Brown'),
'OK':('R',-34.26,[-17.9,-6.0],-3,'Lankford'),
'OR':('D',14.30,[19.4,9.6],3,'Wyden'),
'PA':('D',-1.71,[22.1],1,'Fetterman (weak base; primary risk)'),
'SC':('R',-17.87,[4.5,-4.5],-3,'Scott'),
'SD':('R',-29.19,[-21.0,-27.0],-3,'Thune'),
'TN*':('R',-29.72,[-12.2,-2.5],-1,'Blackburn appointee (special)'),
'UT':('R',-21.59,[],-3,'Lee'),
'VT':('D',31.51,[],3,'Welch'),
'WA':('D',18.22,[],3,'Murray'),
'WI':('R',-0.86,[8.0],0,'Johnson (signaled retirement; open)'),
}
W24=0.7
def lean(s):
    inc,p24,m26,adj,_=S[s]
    L=p24-NAT24
    if m26:
        L26=sum(m26)/len(m26)-NAT26
        B=W24*L+(1-W24)*L26
    else:
        L26=None; B=L
    return L,L26,B
def phi(x): return 0.5*(1+math.erf(x/math.sqrt(2)))
SIG_S=7.0; SIG_N=2.5
DNOT=(38,40); # D seats not up (AK/MS R vs D)
rows=[]
for E in ENVS:
    for s in S:
        L,L26,B=lean(s); adj=S[s][3]
        M=B+E+adj
        rows.append((E,s,L,L26,B,adj,M,phi(M/math.hypot(SIG_S,SIG_N))))
# print table
print('state inc L24 L26 Blend adj | M(D+0) P | M(D+3) P | M(D+6) P')
for s in S:
    L,L26,B=lean(s); adj=S[s][3]
    out=f"{s:4} {S[s][0]} {L:6.1f} {('%6.1f'%L26) if L26 is not None else '   n/a'} {B:6.1f} {adj:+d} |"
    for E in ENVS:
        M=B+E+adj; out+=f" {M:+6.1f} {phi(M/math.hypot(SIG_S,SIG_N)):.2f} |"
    print(out)
random.seed(1)
N=200000
res={}
for E in ENVS:
    for base in DNOT:
        tot=[]
        for _ in range(N):
            n=random.gauss(0,SIG_N); d=base
            for s in S:
                L,L26,B=lean(s); M=B+E+S[s][3]+n+random.gauss(0,SIG_S)
                if M>0: d+=1
            tot.append(d)
        tot.sort()
        q=lambda p: tot[int(p*N)]
        pr=lambda k: sum(1 for t in tot if t>=k)/N
        res[(E,base)]=(st.mean(tot),q(.05),q(.5),q(.95),pr(50),pr(51),pr(52),pr(55),pr(58),pr(60))
for k,v in res.items():
    print(k, 'mean %.1f p5 %d med %d p95 %d | P>=50 %.2f P>=51 %.2f P>=52 %.2f P>=55 %.2f P>=58 %.2f P>=60 %.2f'%v)
