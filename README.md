# 🏥 Health Samjho — Medicine, Tests, Diseases & Nutrition Platform

**Simple English + Hindi mein health samjho.** Content reviewed by a Registered Pharmacist.

A free, SEO-friendly health information platform with 4 modules:
- 💊 **Medicine Decoder** — brand → salt, dose, side effects, interactions
- 🧪 **Blood Report Decoder** — reference ranges, low/high meaning
- 🦠 **Disease Library** — causes, symptoms, prevention
- 🥗 **Nutrition** — Indian foods & nutrients

---

## 📁 Project Structure

```
health-samjho/
├── index.html            ← final single-file site (build.py se banta hai)
├── unified-template.html ← template (data isliye nahi hota, build se bhar jata hai)
├── build.py              ← data files ko index.html mein combine karta hai
├── README.md
└── data/
    ├── medicines.json    ← 💊 medicines (brand + generic + dose + side effects)
    ├── tests.json        ← 🧪 blood tests (reference ranges + interpretation)
    ├── diseases.json     ← 🦠 diseases (causes + symptoms + prevention)
    └── nutrition.json    ← 🥗 foods (nutrients per 100g)
```

---

## 🚀 How to build

```bash
python3 build.py
```

Ye `data/*.json` ko padh kar `index.html` banata hai (single file, no server needed).

---

## 📄 Data format

### Medicine (medicines.json)
```json
{
  "slug": "paracetamol",
  "generic_name": "Paracetamol",
  "salts": ["Paracetamol"],
  "isCombination": false,
  "category": "Analgesic / Antipyretic",
  "primaryUse": "Pain & Fever",
  "uses": { "en": ["Fever"], "hi": ["बुखार"] },
  "howItWorks": { "en": "...", "hi": "..." },
  "howToTake": { "en": ["..."], "hi": ["..."] },
  "dosage": [{ "population": "Adult", "dose": "500–1000 mg", "frequency": "every 4–6h", "maximum": "4000 mg/day" }],
  "sideEffectsCommon": [{ "en": "...", "hi": "..." }],
  "adverseSerious": [{ "en": "...", "hi": "...", "emergency": true }],
  "warnings": { "en": ["..."], "hi": ["..."] },
  "contraindications": { "en": ["..."], "hi": ["..."] },
  "drugInteractions": [{ "drug": "Warfarin", "effect": "...", "severity": "Major" }],
  "foodInteractions": { "en": ["..."], "hi": ["..."] },
  "monitoring": { "en": ["..."], "hi": ["..."] },
  "specialPopulations": { "pregnancy": {"en":"..","hi":".."}, "breastfeeding": {}, "children": {}, "elderly": {}, "renal": {}, "hepatic": {} },
  "whenToContactDoctor": { "en": ["..."], "hi": ["..."] },
  "relatedMedicines": [{ "name": "Ibuprofen", "note": "Same class — NSAID" }],
  "storage": "...",
  "brands": [{ "name": "Dolo 650", "strength": "650 mg", "form": "Tablet", "manufacturer": "Micro Labs" }],
  "source": "FDA (openFDA) · WHO EML",
  "status": "verified"
}
```

### Test (tests.json)
```json
{
  "slug": "hemoglobin",
  "name": "Hemoglobin (Hb)",
  "category": "CBC",
  "unit": "g/dL",
  "normalMin": 12.0,
  "normalMax": 17.0,
  "whatIsIt": { "en": "...", "hi": "..." },
  "whyTested": ["Anemia check"],
  "referenceInterval": { "male": "13–17", "female": "12–15", "caveat": "..." },
  "interpretation": { "low": {"en":"..","hi":".."}, "within": {}, "high": {} },
  "relatedTests": ["MCV", "Ferritin"],
  "questionsForDoctor": ["..."],
  "source": "ICMR / standard lab reference"
}
```

### Disease (diseases.json)
```json
{
  "slug": "diabetes",
  "name": "Diabetes Mellitus",
  "hindi": "डायबिटीज",
  "category": "Metabolic",
  "whatIsIt": { "en": "...", "hi": "..." },
  "causes": ["..."],
  "riskFactors": ["..."],
  "symptoms": ["..."],
  "warningSigns": ["..."],
  "diagnosis": "...",
  "tests": ["Fasting Glucose", "HbA1c"],
  "treatmentOverview": "...",
  "lifestyle": ["..."],
  "prevention": ["..."],
  "relatedMedicines": ["Metformin"],
  "whenUrgent": "...",
  "questionsForDoctor": ["..."],
  "source": "WHO · ICMR"
}
```

### Nutrition (nutrition.json)
```json
{
  "slug": "spinach",
  "name": "Spinach",
  "hindi": "पालक",
  "category": "Vegetables",
  "per100g": { "calories": 23, "protein": 2.9, "iron": 2.7, "calcium": 99 },
  "richIn": ["Iron", "Vitamin A"],
  "goodFor": ["Anemia"],
  "source": "NIN / IFCT"
}
```

---

## 🔒 Data Accuracy Rules (important)

1. **No guess, no unverified data** — sirf verified sources (FDA/WHO/ICMR/NFI)
2. **"Not Available"** — verified info nahi ho to guess mat karo, khali chhodo
3. **Every field bilingual** (English + Hindi/Hinglish)
4. **Dose = indication-specific** (structured, not flat text)
5. **Accuracy over reassurance** — "safe hai" mat likho, accurate likho

---

## 📚 Data Sources

- **Medicine:** FDA (openFDA), WHO EML, NFI (National Formulary of India), CDSCO
- **Tests:** ICMR, standard lab reference ranges
- **Diseases:** WHO, ICMR, MoHFW
- **Nutrition:** NIN (National Institute of Nutrition), IFCT

---

## ⚠️ Disclaimer

This information is for education only. It is not medical advice, diagnosis or a prescription.
Always consult your doctor or a qualified healthcare professional.

---

## 🎯 Roadmap

- [x] Medicine Decoder (32 medicines)
- [x] Blood Report Decoder (47 tests)
- [x] Disease Library (30 diseases)
- [x] Nutrition (22 foods)
- [ ] Scale to 500+ medicines (brand mapping import)
- [ ] Scale to 300+ tests
- [ ] 100+ diseases
- [ ] Firebase backend + user accounts
- [ ] AI "Ask" (RAG over verified data)

---

**Made in India 🇮🇳 · Reviewed by a Registered Pharmacist**
