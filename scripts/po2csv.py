# Converte .po em CSV (msgid;msgstr;contexto) para traduzir fora, e CSV de volta em .po (csv2po). Sem dependências.
import csv, sys, re
def ler_po(p):
    ents, cur, campo = [], {}, None
    for linha in open(p, encoding="utf-8"):
        s = linha.rstrip("\n")
        if s.startswith("#"): cur.setdefault("comentarios", []).append(s); continue
        m = re.match(r'^(msgctxt|msgid|msgid_plural|msgstr(?:\[\d\])?) "(.*)"$', s)
        if m: campo = m.group(1); cur[campo] = cur.get(campo, "") + m.group(2); continue
        m = re.match(r'^"(.*)"$', s)
        if m and campo: cur[campo] += m.group(1); continue
        if s == "" and cur: ents.append(cur); cur, campo = {}, None
    if cur: ents.append(cur)
    return ents
def des(s): return s.encode().decode("unicode_escape").encode("latin1").decode("utf-8")
def po2csv(po, saida, so_vazios):
    ents = ler_po(po); n = 0
    with open(saida, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";"); w.writerow(["msgid", "msgstr_pt_BR", "msgctxt", "referencia"])
        for e in ents:
            if "msgid" not in e or e["msgid"] == "": continue
            if "msgid_plural" in e: continue
            if so_vazios and e.get("msgstr", "") != "": continue
            ref = next((c[2:].strip() for c in e.get("comentarios", []) if c.startswith("#:")), "")
            w.writerow([des(e["msgid"]), des(e.get("msgstr", "")), des(e.get("msgctxt", "")), ref]); n += 1
    print(saida, n, "linhas")
def esc(s): return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\n")
def csv2po(po, csvp, saida):
    trad = {}
    for r in csv.DictReader(open(csvp, encoding="utf-8-sig"), delimiter=";"):
        if r["msgstr_pt_BR"].strip(): trad[(r["msgctxt"], r["msgid"])] = r["msgstr_pt_BR"].strip()
    out, cur, campo, n = [], {}, None, 0
    linhas = open(po, encoding="utf-8").read().split("\n")
    bloco = []
    def fecha(bloco):
        nonlocal n
        txt = "\n".join(bloco)
        m = re.search(r'^msgid "(.*)"$', txt, re.M); c = re.search(r'^msgctxt "(.*)"$', txt, re.M)
        if m and 'msgid_plural' not in txt:
            chave = (des(c.group(1)) if c else "", des(m.group(1)))
            if chave in trad and re.search(r'^msgstr ""\s*$', txt, re.M) and not re.search(r'^msgstr ""\n"', txt, re.M):
                txt = re.sub(r'^msgstr ""\s*$', 'msgstr "' + esc(trad[chave]) + '"', txt, count=1, flags=re.M); n += 1
        return txt
    for l in linhas:
        if l == "" and bloco: out.append(fecha(bloco)); out.append(""); bloco = []
        else: bloco.append(l)
    if bloco: out.append(fecha(bloco))
    open(saida, "w", encoding="utf-8").write("\n".join(out)); print(saida, n, "traduções aplicadas")
if __name__ == "__main__":
    if sys.argv[1] == "po2csv": po2csv(sys.argv[2], sys.argv[3], len(sys.argv) > 4 and sys.argv[4] == "vazios")
    else: csv2po(sys.argv[2], sys.argv[3], sys.argv[4])
