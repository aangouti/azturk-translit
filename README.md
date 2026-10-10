# AzTurkTranslit Engine 🇦🇿

An open-source, highly modular system engineered explicitly to handle bi-directional conversion between **Azerbaijani Latin script** and **Perso-Arabic script**. This software is architected to assist journalists, students, and researchers with precise single-language script transformations.

The internal conversion rules are meticulously structured around the formal standardization resolutions established during the **Second Azerbaijani Orthography Seminar (Tehran, 2001)**.

---

## 🏗️ Compilation Pipeline Architecture

The engine functions like a lightweight compiler, moving text through a series of decoupled, single-responsibility modules to ensure absolute linguistic control:

Use code with caution.
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

---

## 🛠️ Project Goals & Modularity
- **Strictly Unilingual:** Built zero-overhead configuration profiles for Azerbaijani script variants only.
- **Easy Maintenance:** Fix complex structural or etymological edge cases cleanly within standalone modules without mutating core script orchestration.
- **Test-Driven Design:** Decoupled layout permits writing granular unit tests against isolated functions.

## 📝 License
This project is open-source software licensed under the MIT License.
