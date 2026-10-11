# frappe-translations-pt-br

Tradução **completa para o português do Brasil** de um conjunto Frappe autogerenciado:
**Frappe CRM, Helpdesk, ERPNext, HRMS, Insights, Wiki, Telephony, Drive** e o próprio
**Frappe Framework**, nas versões listadas no [README.md](README.md), revisada linha a linha.

## Por que

Os catálogos pt-BR oficiais vivem no Crowdin e estão longe de completos nos apps mais
novos: o Frappe CRM `v1.87.0` tem 1.781 textos e 1.311 estavam sem português; Helpdesk,
Insights, Wiki e Telephony estão na mesma situação, e o próprio framework tinha 815
lacunas. O resultado são telas metade em inglês. Este repositório fecha todas as lacunas
dessas versões e mantém o mesmo termo em todos os apps (*Negócio*, *Organização*,
*Colaborador*, *Chamado*, *Depósito*…).

## O que tem aqui

- `po/<app>/pt_BR.po` — catálogo completo por app (oficial + lacunas preenchidas), para substituir o do app.
- `csv/<app>-pt_BR.csv` — só o que foi acrescentado: `msgid;msgstr_pt_BR;msgctxt;referência`.
- `json/translations-pt-BR.json` — os mesmos 9.385 pares, sem duplicatas, para o doctype `Translation`.
- `scripts/load_translations.py` — carrega o JSON num site, sem build e sem reiniciar.
- `scripts/po2csv.py` — conversor `.po` ⇄ `.csv`, sem dependências.
- `docs/GLOSSARY.md` — o glossário aplicado; `docs/REVIEW.md` — cada ressalva e cada correção, com o motivo.

## Como usar

**Em um minuto, num site no ar** (doctype `Translation`, que o Frappe sobrepõe aos catálogos de todos os apps):

```bash
cd ~/frappe-bench/sites
../env/bin/python /caminho/scripts/load_translations.py <site> /caminho/json/translations-pt-BR.json --set-default-language
```

O script apaga os pares pt-BR anteriores, insere os 9.385 em lote, limpa o cache e, com a
opção, torna pt-BR o idioma padrão do site. Pode ser repetido depois de qualquer ajuste.
Usuário que já tem idioma definido mantém o dele; coloque `pt-BR` no usuário para ver.

**Definitivo** (vai na imagem): copie `po/<app>/pt_BR.po` para `apps/<app>/<app>/locale/pt_BR.po`,
rode `bench compile-po-to-mo --app <app>` e `bench build`. No ERPNext e HRMS **v15** a
tradução ainda vem de `translations/pt-BR.csv`; converta com `scripts/po2csv.py po2csv`.

## Como foi feito

Extração do `main.pot` de cada app na versão indicada; só os textos vazios no oficial foram
traduzidos, em lotes de 100 a 200, com glossário fixo, memória de tradução entre os apps e
validação automática de `{0}`, `%s`, `{{ x }}`, HTML e `\n`. O tradutor marcou 45 textos
com dúvida e cada um recebeu decisão humana; depois uma revisão completa, módulo a módulo,
gerou 128 correções, todas registradas em `docs/REVIEW.md`. O resultado foi carregado num
site real com os oito apps e conferido na tela.

Convenções: botões no infinitivo, tratamento *você*, datas `dd/mm/aaaa`, moeda `R$`,
*Confirmar* para submit e *Retificar* para amend, **Lead = Lead**, **Deal = Negócio**,
**Organization = Organização**, **Employee = Colaborador**, **Ticket = Chamado**.

## Contribuir

Correções são bem-vindas por pull request nos arquivos de `csv/` (placeholders intactos,
glossário respeitado). A intenção é levar o resultado ao Crowdin do Frappe para que chegue
às versões oficiais.

Scripts e documentação sob MIT; os catálogos seguem a licença do app a que pertencem
([LICENSE](LICENSE)). Os produtos são obra da [Frappe](https://github.com/frappe) e de suas comunidades.
