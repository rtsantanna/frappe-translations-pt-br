"""Build json/translations-pt-BR.json from the csv/*.csv files.

    python3 -I scripts/csv_to_json.py

Rules: skip empty translations and pairs where the translation equals the source; the first
occurrence of a (source, context) pair wins, in the app order below.
"""
import csv
import json
from collections import Counter
from pathlib import Path

ORDER = ["crm", "frappe", "helpdesk", "telephony", "insights", "wiki", "hrms", "erpnext", "drive"]
ROOT = Path(__file__).resolve().parent.parent

seen = {}
dup = skipped = 0
for app in ORDER:
    path = ROOT / "csv" / f"{app}-pt_BR.csv"
    if not path.exists():
        continue
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh, delimiter=";"):
            s, t, c = row["msgid"], row["msgstr_pt_BR"].strip(), row.get("msgctxt", "") or ""
            if not t or t == s:
                skipped += 1
                continue
            if (s, c) in seen:
                dup += 1
                continue
            seen[(s, c)] = {"s": s, "c": c, "t": t, "m": app}

rows = list(seen.values())
out = ROOT / "json" / "translations-pt-BR.json"
out.parent.mkdir(exist_ok=True)
with open(out, "w", encoding="utf-8") as fh:
    json.dump(rows, fh, ensure_ascii=False)
print(f"{out}: {len(rows)} pairs ({dup} duplicates and {skipped} empty/identical skipped)")
print(Counter(r["m"] for r in rows))
