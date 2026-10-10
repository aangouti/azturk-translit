# AzTurkTranslit Engine 🇦🇿

An open-source, highly modular engine for Azerbaijani bi-directional transliteration (Latin ↔ Perso-Arabic). Engineered explicitly to assist journalists, researchers, and students with precise, unilingual script conversion based on the orthography resolutions from the 2001 Tehran Seminar chaired by Dr. Javad Heyat.

---

## 🏗️ Compilation Pipeline Architecture

The engine functions like a lightweight compiler, moving text through a series of decoupled, single-responsibility modules to ensure absolute linguistic control:

```text
       ┌──────────────────────────────┐
       │          Input Text          │
       └──────────────┬───────────────┘
                      │
                      ▼
       ┌──────────────────────────────┐
       │    1. Tokenizer/Normalizer   │  <── Standardizes Unicode variances
       └──────────────┬───────────────┘
                      │
                      ▼
       ┌──────────────────────────────┐
       │   2. Lexicon / Map Matcher   │  <── Bypasses rules via Dictionary
       └──────────────┬───────────────┘
                      │
                      ▼
       ┌──────────────────────────────┐
       │   3. Structural Rule Engine  │  <── Evaluates position-based vowels
       └──────────────┬───────────────┘
                      │
                      ▼
       ┌──────────────────────────────┐
       │         Output Text          │
       └──────────────────────────────┘
```

---

## 🛠️ Project Goals & Modularity
- **Strictly Unilingual:** Built zero-overhead configuration profiles for Azerbaijani script variants only.
- **Easy Maintenance:** Fix complex structural or etymological edge cases cleanly within standalone modules without mutating core script orchestration.
- **Test-Driven Design:** Decoupled layout permits writing granular unit tests against isolated functions.

## 📝 License
This project is open-source software licensed under the MIT License.
