# nicotine-replacement

Final plan (WET-122 `/finalize[plan]`): stop combustible cigarettes without vaping, and lower cardiovascular risk with an oral-first lipid ladder that ends in the selected agent, **enlicitide**.

**Prescriber draft, not a prescription.** Section 3.3 is written as a prescribing protocol for an AHPRA-registered medical practitioner (STRATEGY.SEED `prescribe`, ROLE medical doctor, MCHU-24). No AHPRA credentials were supplied, so nothing here is signed or dispensable. A registered prescriber sets drug, dose and targets after assessing the patient. Out of scope: vaping (removed by CONVERGE), psychotherapy and behavioural counselling, and any patient-specific history.

Method. MDT passes by a cardiologist and a respiratory physician (`google/gemini-4-neon` via OpenRouter, given only the verified evidence list), reconciled in §3.2. Each number was checked against the source abstract or label. Preprints are marked **[preprint]**. Australian regulatory facts were checked on TGA, PBS and health.gov.au pages on 2026-11-21.

---

## 1. First principles (0.25)

1. **The smoke kills, not the nicotine.** Most cardiovascular and respiratory harm comes from combustion products (CO, oxidants, particulates, acrolein, nitrosamines). Medicinal nicotine (NRT) and non-nicotine drugs (varenicline, cytisine, bupropion) remove combustion without adding a new inhaled exposure.
2. **No inhaled substitute.** With vaping removed, the airway is fully off-loaded: the only inhaled product is gone, not swapped.
3. **Atherosclerosis is cumulative LDL exposure × time.** ApoB lipoproteins are causal. Benefit tracks the absolute LDL-C lowered and the time it stays lowered, whatever the drug. That is why enlicitide's LDL effect is expected to translate into fewer events, and why that expectation still needs its outcomes trial.
4. **Quitting does not reset arterial age.** Risk falls fast after quitting but stays raised for years, so lipid prophylaxis runs in parallel with cessation, not after it.

## 2. Brute facts (0.25)

### 2.1 Selected agent: enlicitide

| Item | Fact | Source |
|---|---|---|
| Identity | Oral macrocyclic peptide PCSK9 inhibitor (MK-0616). INN salt named on the ticket: enlicitide chloride. Marketed salt: **enlicitide decanoate** (structure image on the ticket), 22.21 mg per 20 mg tablet, with sodium caprate as absorption enhancer | FDA label, Lipfendra, NDA 220848, rev. 7/2026 |
| Status | FDA approved July 2026 (Lipfendra, MSD) for LDL-C lowering in adults with hypercholesterolaemia incl. HeFH. **Not on the ARTG**: TGA PI/CMI repository has 0 documents for enlicitide or Lipfendra | FDA label; TGA search 2026-11-21 |
| Dose | 20 mg once daily. Empty stomach, morning, with water, black coffee or plain tea; swallow whole; wait ≥30 min before other food or drink | FDA label §2 |
| Food effect | Dosing 30 min after a meal cuts AUC 48% and Cmax 50% | FDA label §12.3 |
| LDL-C effect | −56% vs placebo at week 24 (CORALreef Lipids, n=2,904, 97% on statin, baseline 96 mg/dL); HeFH −59.4% (wk 24), −61.5% (wk 52); −64.6% vs ezetimibe −27.8%, bempedoic acid −6.3%, ezetimibe + bempedoic acid −36.5% | [10.1056/NEJMoa2511002](https://doi.org/10.1056/NEJMoa2511002), [10.1001/jama.2025.20620](https://doi.org/10.1001/jama.2025.20620), [10.1016/j.jacc.2026.03.036](https://doi.org/10.1016/j.jacc.2026.03.036) |
| Outcomes | **Not yet shown.** CORALreef Outcomes (NCT06008756) is active, not recruiting; primary completion estimated 2029-11 | FDA label §1; ClinicalTrials.gov |
| Safety | No contraindications. Adverse reactions similar to placebo in CORALreef Lipids; in HeFH, diarrhoea 7% vs 2% and dizziness 9% vs 4% | FDA label §4, §6 |
| Interactions | No clinically meaningful DDIs (atorvastatin, warfarin, digoxin, lithium, levothyroxine, oral semaglutide tested); minimal metabolism; very low CYP/transporter potential | FDA label §12.3 |
| Renal / hepatic | No adjustment: exposure +5–26% across mild–severe CKD; unchanged in Child-Pugh B; Child-Pugh C not studied | FDA label §12.3 |
| Pregnancy | Discontinue when pregnancy is recognised unless benefit outweighs risk; no human lactation data | FDA label §8 |
| Onset | LDL-C effect measurable from 4 weeks | FDA label §2.1 |

### 2.2 Cessation without vaping

| Claim | Number | Source |
|---|---|---|
| Varenicline / bupropion / patch, neuropsychiatric safety | moderate–severe neuropsychiatric AEs (non-psychiatric cohort): varenicline 1.3%, bupropion 2.2%, patch 2.5%, placebo 2.4%; varenicline most effective | EAGLES, [10.1016/S0140-6736(16)30272-0](https://doi.org/10.1016/S0140-6736(16)30272-0) |
| Cessation drugs, CV safety | no rise in serious CV events; NRT raises minor events (palpitations) RR 2.29 | Mills 2014, [10.1161/CIRCULATIONAHA.113.003961](https://doi.org/10.1161/CIRCULATIONAHA.113.003961) |
| Cytisine vs varenicline (Australia, n=1,452) | CO-verified 6-month abstinence 11.7% vs 13.3%; **noninferiority not shown**; fewer adverse events (IRR 0.88) | Courtney 2021 JAMA, [10.1001/jama.2021.7621](https://doi.org/10.1001/jama.2021.7621) |
| Cytisinicline 12 weeks (US) | abstinence weeks 9–12: 32.6% vs 7.0% (ORCA-2), 30.3% vs 9.4% (ORCA-3) | [10.1001/jama.2023.10042](https://doi.org/10.1001/jama.2023.10042), [10.1001/jamainternmed.2025.0628](https://doi.org/10.1001/jamainternmed.2025.0628) |
| Adding varenicline/bupropion to NRT after ACS | lower 1-year mortality and MACE than NRT alone (8,574 matched pairs) | **[preprint]** [10.64898/2026.04.21.26351432](https://doi.org/10.64898/2026.04.21.26351432) |
| Toxicant exposure on NRT only | long-term NRT-only users have much lower NNAL and VOC metabolites than smokers | Shahab 2017, [10.7326/M16-1107](https://doi.org/10.7326/M16-1107) |
| Respiratory symptoms after quitting | quitting vs continued smoking: symptom worsening RR 0.73 | PATH, [10.1016/j.eclinm.2024.102951](https://doi.org/10.1016/j.eclinm.2024.102951) |
| COPD: quitting (n=23,262) | lower exacerbations aHR 0.90, MACCE 0.85, mortality 0.90 | Respir Res 2026, [10.1186/s12931-026-03545-1](https://doi.org/10.1186/s12931-026-03545-1) |

### 2.3 Lipid ladder and adjuncts (outcome evidence)

| Agent | Route | Effect | Evidence | Source |
|---|---|---|---|---|
| Statin | oral | ~22% fewer major vascular events per 1.0 mmol/L LDL-C | hard outcomes | CTT 2010, [10.1016/S0140-6736(10)61350-5](https://doi.org/10.1016/S0140-6736(10)61350-5) |
| Ezetimibe + statin | oral | HR 0.936 (0.89–0.99) at 7 years | hard outcomes | IMPROVE-IT, [10.1056/NEJMoa1410489](https://doi.org/10.1056/NEJMoa1410489) |
| **Enlicitide** | oral | LDL-C −56 to −65% | LDL only | §2.1 |
| Evolocumab / alirocumab | injection | FOURIER HR 0.85; ODYSSEY HR 0.85; VESALIUS-CV (no prior MI/stroke) HR 0.75; GLAGOV plaque regression | hard outcomes | [10.1056/NEJMoa1615664](https://doi.org/10.1056/NEJMoa1615664), [10.1056/NEJMoa1801174](https://doi.org/10.1056/NEJMoa1801174), [10.1056/NEJMoa2514428](https://doi.org/10.1056/NEJMoa2514428), [10.1001/jama.2016.16951](https://doi.org/10.1001/jama.2016.16951) |
| Bempedoic acid | oral | MACE HR 0.87 (statin-intolerant) | hard outcomes | CLEAR Outcomes, [10.1056/NEJMoa2215024](https://doi.org/10.1056/NEJMoa2215024) |
| Colchicine 0.5 mg (anti-inflammatory) | oral | chronic CAD HR 0.69 (LoDoCo2); null in acute MI (CLEAR SYNERGY HR 0.99) | conflicting | [10.1056/NEJMoa2021372](https://doi.org/10.1056/NEJMoa2021372), [10.1056/NEJMoa2405922](https://doi.org/10.1056/NEJMoa2405922) |
| Risk after quitting | heavy smokers stay above never-smoker CVD risk well beyond 5 years | cohort | Framingham, [10.1001/jama.2019.10298](https://doi.org/10.1001/jama.2019.10298) |

### 2.4 Australian access (checked 2026-11-21)

| Item | Status |
|---|---|
| Enlicitide | Not on ARTG. Legal routes: **SAS Category B** (AHPRA-registered prescriber applies; TGA approval letter before supply) or the **Personal Importation Scheme** (valid Australian prescription; ≤3 months' supply per import, ≤15 months per 12 months). Not PBS-subsidised |
| Varenicline | PBS Authority Required (Streamlined), generics (Champix brand gone); course 12 or 24 weeks |
| NRT patches, bupropion | PBS Authority Required (Streamlined); combination with oral NRT is out of pocket |
| Cytisine (Cyventine 1.5 mg) | ARTG-listed 2026; Schedule 3 (pharmacist only), not PBS, RRP $89.99; 25-day course; adults 18–64; avoid in pregnancy, renal or hepatic impairment, unstable angina or recent MI |
| Evolocumab, inclisiran | PBS Authority Required; e.g. LDL-C >1.8 mmol/L with symptomatic ASCVD after ≥12 weeks of maximum tolerated atorvastatin or rosuvastatin, or HeFH criteria |
| Lung cancer screening | NLCSP: age 50–70, asymptomatic, ≥30 pack-years, currently smoking or quit within 10 years; free low-dose CT |

---

## 3. Abstraction (0.5)

### 3.1 Two tracks, run in parallel

```
TRACK A  SMOKING ──► PHARMACOTHERAPY QUIT ──► NICOTINE-FREE
                         (varenicline ± NRT | cytisine | NRT combo)
TRACK B  STATIN ──► + EZETIMIBE ──► + ENLICITIDE (selected) ──► LDL-C at target
```

The tracks don't interact pharmacologically (enlicitide has no meaningful DDIs). Track B starts at the same visit as Track A; it does not wait for the quit date.

### 3.2 MDT reconciliation

| Question | Cardiology | Respiratory | Consensus |
|---|---|---|---|
| Cessation first line | Varenicline (best efficacy, CV-safe) | Varenicline | **Varenicline**, PBS Streamlined, 12 weeks (extend to 24 if abstinent at 12) |
| Alternatives | NRT patch ± oral NRT; bupropion; cytisine second line for stable patients 18–64 | Same; cytisine acceptable if no CV, renal or hepatic exclusion | Combination NRT, then cytisine or bupropion. Cytisine is **not** used after recent MI or with unstable angina |
| Post-ACS combinations | Preprint only; don't anchor protocol on it | Same | Varenicline + NRT allowed on clinical judgement; the preprint is not a rule |
| Where enlicitide sits | After max statin + ezetimibe; behind PBS injectables when the patient qualifies and accepts injections | Same | **Selected oral PCSK9 step**: used when LDL-C stays above target on statin + ezetimibe and the patient declines injections, is PBS-ineligible, or chooses an oral route after consent on outcome gap, cost and access |
| Salt / name | — | Use the marketed salt | Prescribe as **enlicitide 20 mg (as decanoate)**; the chloride name in SELECT is not the marketed salt |
| Monitoring | LDL-C from week 4; palpitations on NRT; GI/dizziness on enlicitide; residual CV risk | CO-verified abstinence; symptoms and exacerbations; NLCSP eligibility; spirometry if symptomatic or ≥40 with smoking history | Both, at shared review visits (§3.3) |
| Evidence gaps flagged | Patient's ASCVD status, baseline LDL-C, absolute risk, renal/hepatic function | Pack-years, baseline spirometry | Collected at visit 1; not in this doc by design (no patient history) |

### 3.3 Prescribing protocol (draft for a registered prescriber)

Unsigned template. The prescriber confirms each line against the current Australian PI, PBS restriction and the patient's assessment.

**Visit 1 (week 0): assess and start both tracks**

- Assess: smoking history and pack-years, absolute CVD risk (Australian CVD risk calculator), ASCVD or HeFH status, fasting lipids including LDL-C, eGFR, LFTs, pregnancy potential, psychiatric history, current medicines (smoking cessation changes CYP1A2 substrates such as clozapine, olanzapine, theophylline).
- Refer: Quitline 13 7848 (PBS requires enrolment in a support program for PBS cessation drugs).
- Screen: NLCSP eligibility; spirometry if respiratory symptoms or age ≥40 with smoking history.

**Track A: cessation (choose one line)**

| Line | Regimen (standard PI dosing) | PBS / supply |
|---|---|---|
| A1, default | Varenicline 0.5 mg daily days 1–3, 0.5 mg twice daily days 4–7, then 1 mg twice daily to week 12; quit date between days 8 and 14. Extend 12 weeks if abstinent | Authority Required (Streamlined); starter pack 0.5 mg ×11 + 1 mg ×42, then 1 mg ×56 |
| A1 + NRT | Add short-acting NRT (gum, lozenge, spray) for cravings | Oral NRT out of pocket |
| A2 | Combination NRT: 24-h patch (21 mg if ≥10 cigarettes/day) + short-acting form, 12 weeks then taper | Patch PBS Streamlined, 12 weeks per course |
| A3 | Cytisine 1.5 mg, 25-day tapering course per PI | S3 pharmacist supply, not PBS. Exclude: age <18 or ≥65, pregnancy/breastfeeding, renal or hepatic impairment, unstable angina, recent MI |
| A4 | Bupropion per PI (not with seizure risk) | PBS Streamlined |

**Track B: lipids (step up at each review if LDL-C above target)**

| Step | Drug | Note |
|---|---|---|
| B1 | High-intensity statin: atorvastatin 40–80 mg or rosuvastatin 20–40 mg daily | PBS. Max tolerated dose |
| B2 | + Ezetimibe 10 mg daily | PBS |
| B3a (selected) | **+ Enlicitide 20 mg (as decanoate) one tablet orally each morning on an empty stomach** with water, black coffee or plain tea; swallow whole; nothing else for 30 min | Not ARTG, not PBS. Supply via SAS Category B (prescriber applies; supply only after TGA approval letter) or Personal Importation (Australian prescription; ≤3 months per import). Record informed consent: no outcome data yet, unsubsidised cost, unregistered product |
| B3b (PBS alternative) | Evolocumab or inclisiran | If PBS criteria are met and injections are acceptable. Outcome-proven |
| Statin-intolerant | Bempedoic acid ± ezetimibe ± enlicitide | Bempedoic acid has hard outcomes |
| Adjunct | Colchicine 0.5 mg daily | Stable CAD only, not acute MI; anti-inflammatory, not lipid-lowering |

Draft enlicitide prescription line (SAS B or personal import):

```
Enlicitide 20 mg tablet (as enlicitide decanoate; Lipfendra, MSD; not ARTG-registered)
Sig: 1 tablet orally once daily in the morning on an empty stomach with water,
     black coffee or plain tea. Swallow whole. No other food or drink for 30 minutes.
Qty: 30 tablets. Repeats: 2 (≤3 months per personal import).
Indication: hypercholesterolaemia, LDL-C above target on maximum tolerated statin + ezetimibe.
Prescriber: [name, AHPRA registration no., signature]   <- required; not supplied
```

**Reviews**

| When | Track A | Track B |
|---|---|---|
| Week 1–2 | Quit date set; varenicline nausea, sleep, mood | — |
| Week 4 | CO-verified abstinence; neuropsychiatric check | LDL-C on enlicitide (effect measurable from week 4); GI upset, dizziness; dosing timing |
| Week 6–12 | Decide 12-week extension (varenicline) or NRT taper | Fasting lipids; step up if above target; LFTs/CK if statin symptoms |
| 6 and 12 months | Relapse check; respiratory symptoms; NLCSP | LDL-C, adherence, cost and supply continuity |

**Stop or switch**

- Enlicitide: stop when pregnancy is recognised (unless benefit outweighs risk); avoid in Child-Pugh C (not studied); switch to a PBS injectable if supply or cost fails.
- Varenicline or bupropion: stop on new or worsening depression, agitation or suicidal thinking.
- Any chest pain, haemoptysis or weight loss: investigate; these preclude screening and need diagnostic work-up.

### 3.4 Why enlicitide is the selected agent, and what would change that

**Why it was selected**

- Largest LDL-C drop of any oral agent (−56 to −65%), about twice ezetimibe and on par with injected PCSK9 drugs.
- No contraindications, no meaningful drug interactions, no renal or moderate hepatic dose adjustment. It sits on top of a statin without changing either drug's exposure.
- A daily tablet, for people who won't use injections.

**What holds it back**

- No outcome data. CORALreef Outcomes (NCT06008756) is active, not recruiting; primary completion is estimated for 2029-11-29. Evolocumab and alirocumab have hard outcomes, including primary prevention (VESALIUS-CV).
- Not registered in Australia (TGA PI/CMI repository: 0 documents for "enlicitide" and "Lipfendra", checked 2026-11-21) and not PBS-listed. Access is SAS Category B or personal import, at full cost.
- The fasting rule is strict: dosing 30 min after a meal halves exposure.

**What would change the selection**

- CORALreef Outcomes positive → enlicitide moves level with the injectables.
- TGA registration and PBS listing → it replaces the SAS/import route and the cost barrier goes.
- Patient meets PBS criteria and accepts injections → B3b (evolocumab or inclisiran) is the evidence-preferred step.

### 3.5 Frontier (MCHU-95 lens)

- **Oral peptides** move antibody-class targets onto a daily pill. Enlicitide relies on a permeation enhancer (sodium caprate), so its food rule is a property of the formulation, not the target.
- **Pending readouts that would change this plan:**
  - CORALreef Outcomes (enlicitide) — the one result that would put it level with the injectables;
  - a TGA registration and PBS listing for enlicitide;
  - PREVAIL (obicetrapib) and Lp(a) outcome trials (muvalaplin), for the watch list.
