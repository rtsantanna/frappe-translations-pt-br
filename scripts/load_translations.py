"""Load pt-BR pairs into the `Translation` doctype of a Frappe site (no build, no restart).

Run from the bench, with the bench's Python:

    cd /home/frappe/frappe-bench/sites
    ../env/bin/python /path/to/load_translations.py <site> /path/to/translations-pt-BR.json [--set-default-language]

What it does:
  * deletes the existing `Translation` rows for language pt-BR (so it can be re-run after fixes),
  * bulk-inserts every pair from the JSON (`s` = source text, `c` = msgctxt or "", `t` = translation),
  * clears the translation cache,
  * optionally sets `System Settings.language = pt-BR` (new users default to it; existing users keep theirs).

The pairs override the compiled `.po` catalogs of the installed apps at runtime (Frappe merges user
translations on top), so this is the quickest way to try the translation on a running site.
"""
import json
import sys

import frappe
import frappe.translate
from frappe.utils import now

LANG = "pt-BR"


def main(site, path, set_default):
    frappe.init(site=site)
    frappe.connect()
    try:
        with open(path, encoding="utf-8") as fh:
            rows = json.load(fh)
        if not frappe.db.exists("Language", LANG):
            raise SystemExit(f"Language {LANG} does not exist on this site")
        before = frappe.db.count("Translation", {"language": LANG})
        if before:
            frappe.db.delete("Translation", {"language": LANG})
        ts = now()
        fields = ["name", "creation", "modified", "modified_by", "owner", "docstatus", "idx",
                  "language", "source_text", "context", "translated_text", "contributed", "contribution_status"]
        values = []
        for r in rows:
            values.append([frappe.generate_hash(length=10), ts, ts, "Administrator", "Administrator", 0, 0,
                           LANG, r["s"], r.get("c") or None, r["t"], 0, ""])
        frappe.db.bulk_insert("Translation", fields, values, chunk_size=1000)
        if set_default:
            frappe.db.set_single_value("System Settings", "language", LANG)
        frappe.db.commit()
        frappe.translate.clear_cache()
        frappe.clear_cache()
        after = frappe.db.count("Translation", {"language": LANG})
        sample = frappe.translate.get_all_translations(LANG)
        print(f"before={before} inserted={len(values)} after={after}")
        print("sample:", {k: sample.get(k) for k in ("Deal", "Create Lead", "Salary Slip", "Ticket")})
    except Exception:
        frappe.db.rollback()
        raise
    finally:
        frappe.destroy()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1], sys.argv[2], "--set-default-language" in sys.argv[3:])
