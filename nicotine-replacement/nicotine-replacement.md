# nicotine-replacement

Final recommended prescriptions (WET-122 `FINALIZE`): **Australian, 2 items**. One to replace cigarettes, one for cardioprotection in a smoker with **normal lipids**. No vaping, no enlicitide (not on the ARTG: TGA PI/CMI search returns 0 documents), no anti-plaque add-ons.

**Draft for a registered prescriber, not a prescription.** No AHPRA credentials were supplied, so nothing here is signed. The prescriber confirms each line against the patient's assessment and the current Australian PI. Checked 2026-11-24 against the TGA PI, PBS and the Poisons Standard (October 2026). Reviewed by an MDT pass (cardiology, respiratory; `google/gemini-4-neon`); its follow-up and risk-input points were added, and its claims that rosuvastatin is contraindicated in severe renal impairment or with ciclosporin, and that cytisine is Schedule 4, were checked and rejected against those sources.

## Recommended prescriptions

| # | Medicine | Regimen | Australian supply |
|---|---|---|---|
| 1 | **Cytisine 1.5 mg tablet** (Cyventine), 100 tablets | 25-day course: 1 tablet every 2 h (max 6/day) days 1–3; every 2.5 h (max 5) days 4–12; every 3 h (max 4) days 13–16; every 5 h (max 3) days 17–20; 1–2/day days 21–25. **Stop smoking completely by day 5.** If it fails, stop; may repeat after 2–3 months | ARTG-registered. Schedule 3 (Pharmacist Only), so no script is needed; not PBS-subsidised |
| 2 | **Rosuvastatin 10 mg tablet** | 1 tablet orally once daily, long term. Start 5 mg if Asian ancestry, severe renal impairment (CrCl <30) or severe hepatic impairment | PBS General Schedule, unrestricted (item 2628H): 30 tablets, 5 repeats |

### Prescription text

```
Rx 1  Cytisine 1.5 mg film-coated tablet (Cyventine)         [Schedule 3, non-PBS]
Sig:  Take orally with water as labelled on the blister:
        Days 1-3    1 tablet every 2 hours   (max 6 tablets/day)
        Days 4-12   1 tablet every 2.5 hours (max 5 tablets/day)
        Days 13-16  1 tablet every 3 hours   (max 4 tablets/day)
        Days 17-20  1 tablet every 5 hours   (max 3 tablets/day)
        Days 21-25  1-2 tablets daily
      Stop smoking completely no later than day 5. Do not smoke or use nicotine
      products during treatment. If still smoking on day 5, stop cytisine; a new
      course may be started after 2-3 months.
Qty:  100 tablets (1 pack = full 25-day course). Repeats: 0.
Indication: aid to smoking cessation, adult 18-65.
```

```
Rx 2  Rosuvastatin 10 mg tablet                              [PBS 2628H, General Schedule]
Sig:  Take 1 tablet orally once daily, at the same time each day, with or without food.
      Prescribe rosuvastatin 5 mg instead if Asian ancestry, CrCl <30 mL/min,
      severe hepatic impairment or taking ciclosporin.
Qty:  30 tablets. Repeats: 5.
Indication: primary prevention of cardiovascular events (absolute CVD risk >=10% / 5 y,
            or 5-<10% after shared decision).
```

```
Prescriber: [name, address, AHPRA registration no., PBS prescriber no., signature, date]  <- required; not supplied
Patient:    [name, address, DOB, Medicare no.]
```

### 1. Cytisine: stop cigarettes

- **Who:** adults 18–65 who are ready to quit (Cyventine PI §4.1).
- **Do not use with:** unstable angina, recent MI or stroke, clinically significant arrhythmia, pregnancy or breastfeeding (PI §4.3). Not recommended in renal or hepatic impairment, or over 65 (PI §4.2).
- **Caution:** ischaemic heart disease, heart failure, hypertension, diabetes, psychiatric illness (PI §4.4). If any of the contraindications apply, use varenicline or combination NRT instead. In pregnancy or breastfeeding, varenicline is not recommended either, so use NRT.
- **Interactions:** not with anti-tuberculosis drugs. Women on hormonal contraception add a barrier method (PI §4.5). Quitting slows CYP1A2 metabolism, so review clozapine, olanzapine and theophylline doses.
- **Evidence:** in Australia, CO-verified 6-month abstinence was 11.7% on cytisine vs 13.3% on varenicline, with fewer adverse events (noninferiority not shown) ([Courtney 2021](https://doi.org/10.1001/jama.2021.7621)).
- **Support and review:** Quitline 13 7848. Review 1–2 weeks after the quit date for abstinence, adverse effects and mood. Clozapine and olanzapine levels can rise within days of quitting: check a clozapine level before the quit date and again within the first week, and plan any dose reduction with the prescriber in advance.

### 2. Rosuvastatin: cardioprotection with normal lipids

- **Why a statin when lipids are normal:** the 2023 Australian CVD risk guideline treats by **absolute risk**, not cholesterol. It recommends lipid-lowering therapy at 5-year risk ≥10% (Australian CVD Risk Calculator) and says to consider it at 5–<10% ([Australian Prescriber summary](https://australianprescriber.tg.org.au/articles/assessing-communicating-and-managing-cardiovascular-disease-risk-a-practical-summary-of-the-2023-guideline.html)).
- **Australian label:** rosuvastatin is indicated to prevent MI, stroke and revascularisation in men ≥50 and women ≥60 without CVD who have ≥2 risk factors, and smoking counts as one (APX-Rosuvastatin PI §4.1).
- **Evidence with normal LDL-C:**
  - HOPE-3: rosuvastatin 10 mg in intermediate-risk people without CVD (mean LDL-C 3.3 mmol/L), major CV events HR 0.76 ([10.1056/NEJMoa1600176](https://doi.org/10.1056/NEJMoa1600176)).
  - JUPITER: rosuvastatin 20 mg with LDL-C <3.4 mmol/L and hsCRP ≥2 mg/L, HR 0.56 ([10.1056/NEJMoa0807646](https://doi.org/10.1056/NEJMoa0807646)).
- **Do not use with:** active liver disease or transaminases >3× ULN, pregnancy, breastfeeding, or no reliable contraception, fusidic acid (PI §4.3). Limit to 5 mg with ciclosporin.
- **Monitor:** baseline lipids, LFTs and eGFR. Repeat lipids from 6 weeks. Check CK only if muscle symptoms.

## Before prescribing

1. Measure BP, lipids, HbA1c or fasting glucose, eGFR and LFTs, then calculate 5-year CVD risk. If it is <5%, item 2 is not indicated; quitting alone is the cardioprotection. Treat hypertension or diabetes if found.
2. If the patient has known ASCVD, this list does not apply: they need secondary-prevention therapy, and cytisine is contraindicated after recent MI or stroke.
3. Start both items at the same visit. Statins and cytisine have no listed interaction.
4. If rosuvastatin is not tolerated, atorvastatin is the PBS alternative. Active liver disease, pregnancy, breastfeeding and fusidic acid rule out every statin, atorvastatin included.
