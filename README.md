# frappe-translations-pt-br

Complete **Brazilian Portuguese (pt-BR)** translation for a self-hosted Frappe stack:
**Frappe CRM, Helpdesk, ERPNext, HRMS, Insights, Wiki, Telephony, Drive** and the **Frappe
Framework** itself — built against the released versions below, reviewed line by line, and
delivered in three forms so you can pick the one that fits your deployment.

Em português: [LEIA-ME.md](LEIA-ME.md).

## Why this exists

The upstream pt-BR catalogs are maintained on Crowdin and are far from complete for the
newer apps — Frappe CRM `v1.87.0` ships 1,781 strings and 1,311 of them had no Brazilian
Portuguese text; Helpdesk, Insights, Wiki and Telephony are in the same situation, and the
framework itself had 815 gaps. Users end up with screens that are half English, half
Portuguese. This repository fills every gap for the versions listed here and keeps the
translated strings consistent across apps (the same term for *Deal*, *Organization*,
*Employee*, *Ticket*, *Warehouse*… everywhere).

## What is included

| App | Version the strings were extracted from | Strings in catalog | Translated | Added by this repo |
|---|---|---|---|---|
| frappe (framework) | v15.122.0 | 6,292 | 6,282 | 815 |
| crm | v1.87.0 | 1,781 | 1,781 | 1,311 |
| helpdesk | v1.30.2 | 1,379 | 1,375 | 1,034 |
| erpnext | v15.122.0 | 9,085 | 9,000 | 3,818 |
| hrms | v15.64.3 | 2,536 | 2,527 | 1,563 |
| insights | v3.14.2 | 686 | 686 | 514 |
| wiki | v3.4.0 | 897 | 896 | 898 |
| telephony | 0.0.1 | 139 | 139 | 139 |
| drive | main (2025-10) | 214 | 213 | 158 |

"Added by this repo" counts the strings that had no pt-BR text upstream. The few that remain
untranslated are plural forms and format examples that must stay as they are.

```
po/<app>/pt_BR.po        complete catalog per app (upstream pt-BR + the gaps filled) — drop-in replacement
csv/<app>-pt_BR.csv      only the strings added here: msgid;msgstr_pt_BR;msgctxt;reference
json/translations-pt-BR.json   the same 9,385 pairs, deduplicated, for the Translation doctype
scripts/load_translations.py   loads the JSON into a site (no build, no restart)
scripts/po2csv.py        .po ⇄ .csv converter (no dependencies)
scripts/csv_to_json.py   rebuilds the JSON from the CSVs
docs/GLOSSARY.md         the term list enforced during translation
docs/REVIEW.md           every flagged string and every correction, with the reason
```

## How to use

### 1. Try it on a running site in a minute (Translation doctype)

Frappe merges rows of the `Translation` doctype on top of the compiled catalogs at runtime,
for every app. From the bench:

```bash
cd ~/frappe-bench/sites
../env/bin/python /path/to/scripts/load_translations.py <site-name> /path/to/json/translations-pt-BR.json --set-default-language
```

The script deletes the previous pt-BR rows, inserts the 9,385 pairs in bulk, clears the
translation cache and (with the flag) makes pt-BR the site default. Re-run it after any fix.
Users whose language is already set keep it; set `pt-BR` on the user to see the result.

### 2. Permanent: put the `.po` in the app (build)

Copy `po/<app>/pt_BR.po` over `apps/<app>/<app>/locale/pt_BR.po` and compile:

```bash
bench compile-po-to-mo --app crm      # repeat per app
bench build                           # the CRM/Helpdesk/Insights/Wiki front-ends bundle translations at build time
```

For ERPNext and HRMS **v15**, translations still come from `translations/pt-BR.csv`; the
`.po` here is complete (upstream CSV + the gaps) and is what `develop` already uses. Convert
with `scripts/po2csv.py po2csv` if you need the CSV form.

### 3. Pick and choose

The `csv/` files carry the reference (`file:line`) of each string, so you can review or
cherry-pick with a spreadsheet and convert back with `scripts/po2csv.py csv2po`.

## How it was made

1. `main.pot` extracted from each app at the version above (`bench generate-pot-file`),
   compared with the upstream `pt_BR.po` / `pt-BR.csv`; only the empty entries went to work.
2. Machine translation in batches of 100–200 strings with a fixed glossary
   ([docs/GLOSSARY.md](docs/GLOSSARY.md)), a translation memory across apps and automatic
   validation of placeholders (`{0}`, `%s`, `%(name)s`, `{{ x }}`, HTML tags, `\n`).
3. The translator flagged 45 doubtful strings; each received a human decision.
4. A full linguistic review, module by module, produced 128 corrections — all listed with
   the reason in [docs/REVIEW.md](docs/REVIEW.md).
5. Loaded on a real site with the eight apps installed and checked on screen.

Conventions: buttons and actions in the infinitive (*Salvar*, *Excluir*), *você* form,
dates as `dd/mm/aaaa`, currency `R$`, document actions *Confirmar* (submit) / *Retificar*
(amend), **Lead = Lead**, **Deal = Negócio**, **Organization = Organização**,
**Employee = Colaborador**, **Ticket = Chamado**, **Warehouse = Depósito**. System names
(DocType, Frappe, ERPNext, Twilio, Exotel) and role names are not translated.

## Contributing upstream

Frappe manages translations on [Crowdin](https://crowdin.com/project/frappe); this
repository is the staging area. Corrections are welcome as pull requests on the `csv/`
files (keep the placeholders intact and the glossary consistent), and the plan is to push
the result to Crowdin so it reaches the official releases.

## Credits and license

Translation, review and tooling by Ricardo Sant'Anna. Scripts and documentation are MIT.
The catalogs under `po/` and `csv/` are offered under the license of the app each one
belongs to (see [LICENSE](LICENSE)), so they can be merged upstream as they are. All the
products are the work of [Frappe](https://github.com/frappe) and their communities.
