# -*- coding: utf-8 -*-

#   TASK 1: Data Collection & Dataset Understanding
#   Decodelabs Data Science  Internship
#   Dataset: Titanic (via Seaborn)


import pandas as pd
import seaborn as sns

# ── 1. LOAD DATASET ─────────────────────────────────────────
df = sns.load_dataset('titanic')
print("✅ Dataset loaded successfully!\n")

# ── 2. BASIC INFO ────────────────────────────────────────────
print("=" * 50)
print("📋 DATASET SHAPE (rows, columns):")
print(df.shape)

print("\n📋 FIRST 5 ROWS:")
print(df.head())

# ── 3. COLUMN NAMES & DATA TYPES ─────────────────────────────
print("\n" + "=" * 50)
print("📌 COLUMN NAMES AND DATA TYPES:")
print(df.dtypes)

# ── 4. DATASET SIZE & FEATURES ───────────────────────────────
print("\n" + "=" * 50)
print(f"📊 Total Rows    : {df.shape[0]}")
print(f"📊 Total Columns : {df.shape[1]}")
print(f"📊 Total Cells   : {df.size}")

# ── 5. MISSING VALUES ────────────────────────────────────────
print("\n" + "=" * 50)
print("❓ MISSING VALUES PER COLUMN:")
print(df.isnull().sum())

# ── 6. BASIC STATISTICS ──────────────────────────────────────
print("\n" + "=" * 50)
print("📈 BASIC STATISTICS (Numerical Columns):")
print(df.describe())

# ── 7. WHAT THE DATA REPRESENTS ──────────────────────────────
print("\n" + "=" * 50)
print("📖 WHAT THE DATA REPRESENTS:")
print("""
The Titanic dataset contains information about 891 passengers
aboard the RMS Titanic that sank in April 1912.

Key Columns:
  - survived   : 0 = Did not survive, 1 = Survived
  - pclass     : Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
  - sex        : Gender of the passenger
  - age        : Age in years
  - sibsp      : # of siblings/spouses aboard
  - parch      : # of parents/children aboard
  - fare       : Passenger fare (ticket price)
  - embarked   : Port of Embarkation (C, Q, or S)
  - class      : Same as pclass but as text
  - who        : man, woman, or child
  - alone      : Whether the passenger was traveling alone
""")

print("✅ Task 1 Complete!")
