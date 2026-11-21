# nicotine-replacement

Replacing combustible cigarettes, plus oral prophylaxis for cardiovascular risk (WET-122).

Informational only, not medical advice. Drug choice, dose and LDL-C targets are for a clinician to set. Out of scope: psychotherapy and behavioural counselling, and any patient-specific history.

Method. MDT passes by a cardiologist and a respiratory physician (`google/gemini-4-neon` via OpenRouter, given only the verified evidence list), reconciled here. Each number below was checked against the source abstract. Preprints are marked **[preprint]** and are not peer reviewed. X posts are used only to gauge signal and are never cited as evidence. Searches ran on 2026-11-21: medRxiv through Europe PMC (`PUBLISHER:"medRxiv"`), PubMed as fallback.

---

## 1. First principles (0.25)

1. **The smoke kills, not the nicotine.** Most cardiovascular and respiratory harm comes from combustion products: CO, oxidants, particulates, acrolein and other VOCs, and tobacco-specific nitrosamines. Nicotine sustains dependence and has haemodynamic effects (heart rate, BP). Remove combustion first and the nicotine second.
2. **Exposure is a dose.** Risk scales with toxicant dose. Switching completely gives the largest drop. Dual use (cigarettes plus vape) mostly keeps the toxicant dose.
3. **Atherosclerosis is cumulative LDL exposure × time, amplified by inflammation.** ApoB-containing lipoproteins are causal for plaque. Benefit is roughly proportional to the absolute LDL-C lowered and how long it stays lowered, whatever the drug. Residual risk is partly inflammatory (NLRP3/IL-1β/IL-6), which is the rationale for colchicine.
4. **Quitting does not reset arterial age.** After quitting, risk falls fast but stays raised for years. That is why the prophylaxis subtask exists.

## 2. Brute facts (0.25)

### 2.1 Replacing cigarettes

| Claim | Number | Source |
|---|---|---|
| Nicotine vape vs NRT for quitting (meta-analysis) | RR 1.61 (1.23–2.12), 11 RCTs, n=4,114, high certainty; about +4 quitters per 100 | Cochrane 2026, [10.1002/14651858.CD010216.pub11](https://doi.org/10.1002/14651858.CD010216.pub11) |
| Vape vs NRT, pragmatic RCT | 1-year abstinence 18.0% vs 9.9%, RR 1.83 (1.30–2.58); 80% of vape quitters still vaping at 52 weeks vs 9% of NRT quitters still using NRT | Hajek 2019 NEJM, [10.1056/NEJMoa1808779](https://doi.org/10.1056/NEJMoa1808779) |
| Vaping frequency matters | daily vaping +12.5 pp cessation (6.2–18.7); vaping 1–5 days/month no benefit (−2.4 pp, ns) | **[preprint]** PATH causal forest, [10.64898/2026.09.02.26362051](https://doi.org/10.64898/2026.09.02.26362051) |
| Toxicant exposure | long-term vape-only and NRT-only users have much lower NNAL and VOC metabolites than smokers or dual users; nicotine intake similar | Shahab 2017 Ann Intern Med, [10.7326/M16-1107](https://doi.org/10.7326/M16-1107) |
| Vascular function after switching | 1 month: FMD +1.49% (0.93–2.04), PWV −0.53 m/s; no nicotine vs nicotine-free difference | VESUVIUS, George 2019 JACC, [10.1016/j.jacc.2019.09.067](https://doi.org/10.1016/j.jacc.2019.09.067) |
| Varenicline / bupropion / patch, neuropsychiatric safety | moderate–severe neuropsychiatric AEs (non-psychiatric cohort): varenicline 1.3%, bupropion 2.2%, patch 2.5%, placebo 2.4%; varenicline most effective | EAGLES, Anthenelli 2016 Lancet, [10.1016/S0140-6736(16)30272-0](https://doi.org/10.1016/S0140-6736(16)30272-0) |
| Cessation drugs, CV safety | no rise in serious CV events; MACE RR bupropion 0.45 (0.21–0.85), varenicline 1.34 (0.66–2.66), NRT 1.95 (0.26–4.30); NRT raises minor events (palpitations) RR 2.29 | Mills 2014 Circulation, [10.1161/CIRCULATIONAHA.113.003961](https://doi.org/10.1161/CIRCULATIONAHA.113.003961) |
| Cytisinicline 12 weeks | abstinence weeks 9–12: 32.6% vs 7.0% (ORCA-2), 30.3% vs 9.4% (ORCA-3) | [10.1001/jama.2023.10042](https://doi.org/10.1001/jama.2023.10042), [10.1001/jamainternmed.2025.0628](https://doi.org/10.1001/jamainternmed.2025.0628) |
| Cytisinicline to stop vaping | RCT in adults who vape (ORCA-V1) | [10.1001/jamainternmed.2024.1313](https://doi.org/10.1001/jamainternmed.2024.1313) |
| Adding varenicline/bupropion to NRT after ACS | 8,574 matched pairs; lower 1-year mortality and MACE than NRT alone (reported HR 1.26 and 1.16 for NRT-alone vs combination) | **[preprint]** TriNetX, [10.64898/2026.04.21.26351432](https://doi.org/10.64898/2026.04.21.26351432) |
| Nicotine pouches as a quit aid (GB) | use in quit attempts rose from 2.4% to 6.7% (2021–26); unadjusted success 33.5% vs 27.0% | **[preprint]** [10.64898/2026.10.21.26366107](https://doi.org/10.64898/2026.10.21.26366107) |
| Short-term health by transition (UKHLS) | exclusive vape: mental health score +1.04; dual use: mental health −1.02 and lower EQ-5D; no short-term physical-score gain in any group | **[preprint]** target-trial emulation, [10.64898/2026.02.12.26345898](https://doi.org/10.64898/2026.02.12.26345898) |

### 2.2 Respiratory

| Claim | Number | Source |
|---|---|---|
| Respiratory symptom worsening vs continued smoking | switching to vape RR 0.69 (0.52–0.91); quitting RR 0.73 | PATH, EClinicalMedicine 2025, [10.1016/j.eclinm.2024.102951](https://doi.org/10.1016/j.eclinm.2024.102951) |
| COPD: switch vs quit (n=23,262) | quitters: lower exacerbations aHR 0.90, MACCE 0.85, mortality 0.90; vape switchers: lower MACCE but **no** drop in exacerbations (aHR 0.98) or lung cancer (0.94) | Respir Res 2026, [10.1186/s12931-026-03545-1](https://doi.org/10.1186/s12931-026-03545-1) |
| Vaping duration and incident COPD (age ≥40, smoking history) | with baseline respiratory symptoms aHR 1.28 (1.16–1.40); without symptoms aHR 1.01 | **[preprint]** [10.64898/2026.02.04.26345592](https://doi.org/10.64898/2026.02.04.26345592) |
| Airway irritation | throat/mouth irritation 65.3% (vape) vs 51.2% (NRT) | Hajek 2019 |
| Nasal mucosal cytokines | distinct profiles in vape-only and dual users vs never users (n=64) | **[preprint]** [10.1101/2025.10.23.25338090](https://doi.org/10.1101/2025.10.23.25338090) |
| EVALI | vitamin E acetate in BAL fluid in 48/51 cases; THC exposure in 94%. A cutting-agent problem with illicit THC products, not regulated nicotine liquids | Blount 2020 NEJM, [10.1056/NEJMoa1916433](https://doi.org/10.1056/NEJMoa1916433) |
| Arrhythmia in young people who vape | OR 1.82 for heart rhythm diagnoses (TriNetX, adolescents and young adults, n=114,404; observational) | **[preprint]** [10.64898/2026.03.12.26348232](https://doi.org/10.64898/2026.03.12.26348232) |

### 2.3 Prophylaxis (cardiovascular risk)

| Agent | Route | Effect | Outcome evidence | Source |
|---|---|---|---|---|
| Statin | oral | per 1.0 mmol/L LDL-C lowered, about 22% fewer major vascular events; more vs less intensive −15% | hard outcomes | CTT 2010 Lancet, [10.1016/S0140-6736(10)61350-5](https://doi.org/10.1016/S0140-6736(10)61350-5) |
| Ezetimibe + statin | oral | LDL 53.7 vs 69.5 mg/dL; 7-year events 32.7% vs 34.7%, HR 0.936 (0.89–0.99) | hard outcomes | IMPROVE-IT 2015, [10.1056/NEJMoa1410489](https://doi.org/10.1056/NEJMoa1410489) |
| **Enlicitide** (oral PCSK9 inhibitor, macrocyclic peptide) | oral, daily | LDL-C −55.8 pp vs placebo at week 24 (n=2,909); HeFH −59.4 pp (week 24), −61.5 pp (week 52); day 56 −64.6% vs ezetimibe −27.8%, bempedoic acid −6.3%, ezetimibe + bempedoic acid −36.5% | **LDL only; outcomes trial not yet reported**; approved (first oral PCSK9 inhibitor) | CORALreef Lipids NEJM 2026 [10.1056/NEJMoa2511002](https://doi.org/10.1056/NEJMoa2511002); HeFH JAMA 2026 [10.1001/jama.2025.20620](https://doi.org/10.1001/jama.2025.20620); vs oral nonstatins JACC 2026 [10.1016/j.jacc.2026.03.036](https://doi.org/10.1016/j.jacc.2026.03.036); approval review [10.5582/ddt.2026.01051](https://doi.org/10.5582/ddt.2026.01051) |
| Evolocumab / alirocumab (injected PCSK9 mAbs, for comparison) | injection | FOURIER HR 0.85; ODYSSEY HR 0.85 (death HR 0.85); VESALIUS-CV (no prior MI/stroke, n=12,257) 3-point MACE HR 0.75 (0.65–0.86); GLAGOV plaque volume −0.95% vs +0.05% | hard outcomes + plaque regression | [10.1056/NEJMoa1615664](https://doi.org/10.1056/NEJMoa1615664), [10.1056/NEJMoa1801174](https://doi.org/10.1056/NEJMoa1801174), [10.1056/NEJMoa2514428](https://doi.org/10.1056/NEJMoa2514428), [10.1001/jama.2016.16951](https://doi.org/10.1001/jama.2016.16951) |
| Bempedoic acid | oral | LDL −21 pp; MACE 11.7% vs 13.3%, HR 0.87 (statin-intolerant, n=13,970) | hard outcomes | CLEAR Outcomes 2023, [10.1056/NEJMoa2215024](https://doi.org/10.1056/NEJMoa2215024) |
| Colchicine 0.5 mg | oral | chronic CAD HR 0.69 (LoDoCo2); post-MI HR 0.77 (COLCOT) but HR 0.99 in CLEAR SYNERGY (acute MI, n=7,062); 6-RCT meta HR 0.75 | conflicting | [10.1056/NEJMoa2021372](https://doi.org/10.1056/NEJMoa2021372), [10.1056/NEJMoa1912388](https://doi.org/10.1056/NEJMoa1912388), [10.1056/NEJMoa2405922](https://doi.org/10.1056/NEJMoa2405922), [10.1093/eurheartj/ehaf174](https://doi.org/10.1093/eurheartj/ehaf174) |
| Colchicine, newer meta-analyses | oral | 5 RCTs: HR 0.68 but HKSJ CI 0.27–1.70, I² 81%, GI discontinuation RR 1.95; 10 RCTs: RR 0.73, NNT 52 | — | **[preprint]** [10.64898/2026.03.25.26348968](https://doi.org/10.64898/2026.03.25.26348968), **[preprint]** [10.1101/2024.12.19.24319310](https://doi.org/10.1101/2024.12.19.24319310) |
| Obicetrapib (CETP inhibitor) | oral | LDL −32.6 pp (BROADWAY, n=2,530); fixed-dose combination with ezetimibe −48.6% vs placebo (TANDEM) | LDL only; outcomes trial (PREVAIL) pending | [10.1056/NEJMoa2415820](https://doi.org/10.1056/NEJMoa2415820), [10.1016/S0140-6736(25)00721-4](https://doi.org/10.1016/S0140-6736(25)00721-4) |
| Muvalaplin (Lp(a) formation inhibitor) | oral | Lp(a) −47.6 / −81.7 / −85.8% at 10 / 60 / 240 mg | Lp(a) only; investigational | KRAKEN JAMA 2025, [10.1001/jama.2024.24017](https://doi.org/10.1001/jama.2024.24017) |
| Risk after quitting | quitting lowers CVD within 5 years, but heavy smokers stay above never-smoker risk for well beyond 5 years | — | cohort | Framingham, Duncan 2019 JAMA, [10.1001/jama.2019.10298](https://doi.org/10.1001/jama.2019.10298) |

---

## 3. Abstraction (0.5)

### 3.1 The replacement plan as a state machine

```
SMOKING ──► SWITCH (complete, daily) ──► NICOTINE-ONLY ──► NICOTINE-FREE
   │              │                         ▲
   └──► DUAL ◄────┘  (failure state: keeps most toxicant dose; exit it fast)
```

- **SMOKING → SWITCH.** Pick one primary route:
  - **Route A, airway-sparing:** varenicline or cytisinicline (12-week course), with combination NRT (patch plus a short-acting form) as needed. Respiratory's first choice.
  - **Route B, highest quit yield vs NRT:** a nicotine vape used **daily** at a dose high enough to stop cravings. Cardiology accepts this as first-line for people who have failed or declined Route A.
  - Routes can be combined: varenicline with NRT, or a vape with a cessation drug. After ACS, adding varenicline or bupropion to NRT was associated with lower mortality **[preprint]**.
- **DUAL is the failure state.** It keeps the toxicant dose and was linked to worse quality of life **[preprint]**. Leave it in either direction: upward (more vaping or NRT) or downward.
- **NICOTINE-ONLY → NICOTINE-FREE.** Taper vape nicotine strength, or use cytisinicline (ORCA-V1). The respiratory case: switching to a vape did not lower COPD exacerbations or lung cancer, but quitting did, and long-term vaping with symptoms is linked to incident COPD **[preprint]**.
- **Product hygiene.** Use regulated nicotine liquids only; no THC or illicit cartridges (EVALI). Nicotine pouches are a non-inhaled option with only observational quit data **[preprint]**.

### 3.2 MDT reconciliation

| Question | Cardiology | Respiratory | Consensus |
|---|---|---|---|
| First choice | Fastest complete stop to combustion; a vape is fine | Non-inhaled drug first (varenicline or cytisinicline) | Both are acceptable first lines; what matters is complete, daily replacement of every cigarette |
| How long to vape | Tolerant of long-term vaping to prevent relapse | Time-limited bridge, then stop | Bridge, with planned step-down; never step down into dual use |
| Monitoring | BP, HR, lipids, CV risk score | Cough, sputum, wheeze, dyspnoea; baseline post-bronchodilator spirometry if age ≥40 with a smoking history | Both; symptoms while vaping are a trigger to stop vaping |
| Polypharmacy | Prioritise lipid lowering, since risk persists after quitting | Lipid drugs must not displace the nicotine step-down | Run both tracks in parallel; they don't interact |

### 3.3 Prophylaxis ladder (oral first)

Targets follow ESC/EAS 2019 risk tiers ([10.1093/eurheartj/ehz455](https://doi.org/10.1093/eurheartj/ehz455)):

| Risk tier | LDL-C target |
|---|---|
| Very high | <1.4 mmol/L (55 mg/dL) and ≥50% reduction |
| High | <1.8 mmol/L (70 mg/dL) |
| Moderate | <2.6 mmol/L (100 mg/dL) |

Smoking moves people up a tier, and that effect persists after quitting.

1. **Statin.** Hard outcomes; the base for every tier.
2. **+ Ezetimibe.** Oral, cheap, hard outcomes (IMPROVE-IT).
3. **+ PCSK9 inhibition.**
   - **Oral enlicitide** gives the largest oral LDL drop available, at injectable-class magnitude (−56 to −65%), but outcome data are still pending.
   - **Injected mAbs** have outcome proof, including primary prevention (VESALIUS-CV) and plaque regression (GLAGOV).
   - Choose by whether outcome proof or the oral route matters more.
4. **Statin-intolerant:** bempedoic acid (hard outcomes) ± ezetimibe ± enlicitide.
5. **Residual inflammatory risk, stable CAD:** colchicine 0.5 mg (LoDoCo2). Not routinely in acute MI (CLEAR SYNERGY was null). GI intolerance is common.
6. **Watch list (oral, LDL or Lp(a) data only so far):**
   - obicetrapib, alone or with ezetimibe;
   - muvalaplin, for high Lp(a). Measure Lp(a) once.

"Oral anti-plaque" in evidence terms: plaque regression has been shown for intensive LDL lowering with PCSK9 mAbs (GLAGOV). For oral agents, plaque regression is inferred from the LDL drop, not yet imaged in outcome-scale trials.

### 3.4 Frontier (MCHU-95 lens)

- **Oral peptides** (enlicitide is a macrocyclic peptide) move targets that once needed antibodies onto a daily pill.
- **Target-trial emulation and causal forests** (UKHLS, PATH preprints above) are how the vaping field is answering causal questions that RCTs can't reach.
- **Pending readouts that would change this document:**
  - CORALreef Outcomes (enlicitide);
  - PREVAIL (obicetrapib);
  - Lp(a) outcome trials;
  - long-term RCTs of vaping with hard CV or respiratory endpoints (none exist yet).

### 3.5 X signal (2026-11-14 → 11-20, not evidence)

- **Enlicitide:** discussion of a "57% LDL drop" and the "first FDA-approved oral PCSK9 inhibitor", alongside AHA 2026 sessions.
- **Obicetrapib:** glycaemia-neutral data (EJPC), plus a reported launch in Germany.
- **Vaping:** viral posts about small studies on lung function (n=22) and vascular effects (n=17), criticised by independent experts for sample size.

None of these posts changes the tables above.
