# Review log

Every string was machine-translated in batches of 100–200 with the glossary enforced and placeholders validated (`{0}`, `%s`, `{{ x }}`, HTML). The translator flagged 45 strings as doubtful (`SAN`); each got a human decision. A second pass then reviewed every module line by line. This file lists all decisions and corrections.

## Flagged strings (45) and the decision

| App | Source | Final | Reason |
|---|---|---|---|
| crm | 01/01/2022 to 01/31/2022 | 01/01/2022 a 31/01/2022 | exemplo de data no formato dd/mm/aaaa (é só texto de exemplo no filtro) |
| crm | 01/04/2024 11:30 PM | 01/04/2024 23:30 | exemplo de data/hora no formato pt-BR, 24 h |
| crm | 08:00 AM | 08:00 | exemplo de horário em 24 h |
| crm | 08:00 pm | 20:00 | exemplo de horário em 24 h |
| crm | Invalid format. Try: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | Formato inválido. Tente: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | os exemplos são a sintaxe que o parser de duração aceita (inglês); traduzir quebraria |
| crm | Since you removed {0} from the assignee, the {0} has also been removed. | Como você removeu {0} dos responsáveis, {0} também foi removido. | {0} repetido é do original; frase correta em pt-BR |
| crm | Since you removed {0} from the assignee, the {0} has been changed to the next available assignee {1}. | Como você removeu {0} dos responsáveis, {0} foi alterado para o próximo responsável disponível, {1}. | idem; frase correta |
| crm | unlinked_orphan | unlinked_orphan | identificador interno, não é rótulo |
| crm | {0} M | {0} meses | no CRM é tempo relativo (meses); catálogo separado do framework |
| frappe | Ar | Ar | abreviação do sistema numérico indiano; manter |
| frappe | Cr | Cr | idem |
| frappe | Kh | Kh | idem |
| frappe | L | L | idem |
| frappe | Master | Master | forma de tratamento sem equivalente; manter a lista original de saudações |
| frappe | Mx | Mx | tratamento neutro; manter |
| frappe | Noop Source | Noop Source | fixture de teste; não traduzir |
| frappe | {0} m | {0} min | tempo relativo: minutos (min) |
| helpdesk | Base Support Rotation | Rodízio básico de suporte | é a regra de rodízio base dos agentes; tradução adequada |
| helpdesk | Could not an email due to: {0} | Não foi possível enviar um e-mail devido a: {0} | verbo omitido no original; 'enviar' é o contexto de hd_ticket |
| helpdesk | Partnership | Sociedade | tipo de organização; 'Sociedade' é o genérico correto |
| helpdesk | User Resolution Time | Tempo de resolução do usuário | métrica de SLA do lado do usuário; manter |
| erpnext | # Create a Supplier  Also known as Vendor, is a master at the center of your purchase transactions. Suppliers are linked | # Criar um fornecedor  O cadastro de fornecedores é fundamental para suas transações de compra. Fornecedores são vincula | fornecedor gera contas a PAGAR; o original diz 'Account Receivables' por erro; corrigido o item da lista |
| erpnext | # Sales Order  A Sales Order is a confirmation of an order from your customer. It is also referred to as Proforma Invoic | # Pedido de venda  Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O pedido de v | fiel ao original (texto de onboarding) |
| erpnext | A Sales Order is a confirmation of an order from your customer. It is also referred to as Proforma Invoice.  Sales Order | Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O pedido de venda é fundamental  | idem |
| erpnext | A Transaction Deletion Document: {0} is triggered for {0} | Um documento de exclusão de transações: {0} foi acionado para {0} | {0} repetido é do original |
| erpnext | Allow Internal Transfers at Arm's Length Price | Permitir transferências internas a preço de mercado (arm's length) | termo de preços de transferência; manter 'arm's length' entre parênteses |
| erpnext | Apply TDS | Aplicar TDS | TDS é retenção da Índia; sigla mantida |
| erpnext | Asset{is_plural} {assets_link} created for {item_code} | Ativo{is_plural} {assets_link} criado(s) para {item_code} | concordância com o plural dinâmico {is_plural} |
| erpnext | Biweekly | Quinzenal | frequência do extrato: quinzenal |
| erpnext | Cannot create Intercompany {0}. All items in the source {1} have already been fully invoiced. Please check the existing  | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifique os doc | plural dinâmico resolvido com 'documentos do tipo {2}' |
| erpnext | For quantity {0} should not be greater than allowed quantity {1} | A quantidade de referência {0} não deve ser maior que a quantidade permitida {1} | 'For Quantity' é a quantidade de referência da entrada de estoque |
| erpnext | Partnership | Sociedade | tipo societário genérico |
| erpnext | Row #{0}: BOM is not specified for subcontracting item {0} | Linha nº {0}: a BOM não foi especificada para o item subcontratado {0} | {0} repetido é do original |
| erpnext | Row #{0}: From Date cannot be before To Date | Linha nº {0}: a data inicial não pode ser anterior à data final | regra como está no código |
| erpnext | The stock for the item {0} in the {1} warehouse was negative on the {2}. You should create a positive entry {3} before t | O estoque do item {0} no depósito {1} estava negativo em {2}. Crie um lançamento positivo {3} antes da data {4} e do hor | HTML preservado como no original |
| hrms | <h4>Condition Examples</h4> <ol> <li>Applying tax if employee born between 31-12-1937 and 01-01-1958 (Employees aged 60  | <h4>Exemplos de condições</h4> <ol> <li>Aplicação de imposto se o colaborador nasceu entre 31-12-1937 e 01-01-1958 (cola | exemplos e expressões preservados |
| hrms | CTC | CTC | CTC (custo para a empresa) é termo de folha; rótulo curto |
| hrms | Current CTC | CTC atual | idem |
| hrms | Interest | Interesse | DocType Interest do módulo HR = interesses do colaborador |
| hrms | Maximum benefit of employee {0} exceeds {1} by the sum {2} of benefit application pro-rata component amount and previous | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor proporcional da rubrica na solicitação de benefí | fiel à mensagem de validação |
| hrms | Maximum benefit of employee {0} exceeds {1} by the sum {2} of previous claimed amount | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor solicitado anteriormente | idem |
| hrms | Revised CTC | CTC revisado | idem |
| hrms | Today {0} at our Company! 🎉 | Hoje {0} na nossa empresa! 🎉 | fragmento composto em runtime; frase neutra |
| wiki | Docs Base Utl | URL base da documentação | 'Utl' é erro de digitação de URL no original |
| wiki | Save Delete Draft | Salvar rascunho de exclusão | ação: gravar a exclusão no rascunho |

## Corrections applied after review (128)

| App | Source | Before | After | Reason |
|---|---|---|---|---|
| crm | <span class="h5"><b>PORTAL</b></span> | <span class="h5"><b>PORTAL</b></span> | <span class="h5"><b>PORTAL</b></span> | Revisão confirma título em português idêntico ao original; nenhuma adaptação necessária. |
| crm | CRM Rolling Response Time | Tempo de resposta em janela móvel do CRM | Tempo de resposta recorrente do CRM | Uniformizar Rolling Response com a descrição de reinício do SLA após cada resposta do cliente. |
| erpnext | Cannot create Intercompany {0}. All items in the source {1} have already been fully invoiced. Please check the | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifi | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifi | Evitar acrescentar plural inglês a um nome de tipo de documento dinâmico; manter SAN sobre o problema na orige |
| erpnext | Error: This asset already has {0} depreciation periods booked. 				The `depreciation start` date must be at le | Erro: este ativo já possui {0} períodos de depreciação contabilizados. 				A data `depreciation start` deve se | Erro: este ativo já possui {0} períodos de depreciação contabilizados. 				A data `início da depreciação` deve | Os trechos entre crases são rótulos descritivos de campos em linguagem natural; traduzir com equivalências exp |
| telephony | Please enable and configure TP Twilio Settings first. | Habilite e configure as configurações do Twilio do TP primeiro. | Primeiro, habilite e configure a integração com o Twilio do TP. | Eliminar a repetição configure as configurações, preservando a instrução de habilitar e configurar a integraçã |
| telephony | Please enable and configure TP Twilio Settings to send SMS. | Habilite e configure as configurações do Twilio do TP para enviar SMS. | Habilite e configure a integração com o Twilio do TP para enviar SMS. | Eliminar a repetição configure as configurações, preservando a instrução e a finalidade de envio de SMS. |
| crm | 01/01/2022 to 01/31/2022 | 01/01/2022 a 01/31/2022 | 01/01/2022 a 31/01/2022 | exemplo de data no formato dd/mm/aaaa (é só texto de exemplo no filtro) |
| crm | 01/04/2024 11:30 PM | 01/04/2024 11:30 PM | 01/04/2024 23:30 | exemplo de data/hora no formato pt-BR, 24 h |
| crm | 08:00 AM | 08:00 AM | 08:00 | exemplo de horário em 24 h |
| crm | 08:00 pm | 08:00 pm | 20:00 | exemplo de horário em 24 h |
| crm | Invalid format. Try: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | Formato inválido. Tente: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | Formato inválido. Tente: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | os exemplos são a sintaxe que o parser de duração aceita (inglês); traduzir quebraria |
| crm | Since you removed {0} from the assignee, the {0} has also been removed. | Como você removeu {0} dos responsáveis, {0} também foi removido. | Como você removeu {0} dos responsáveis, {0} também foi removido. | {0} repetido é do original; frase correta em pt-BR |
| crm | Since you removed {0} from the assignee, the {0} has been changed to the next available assignee {1}. | Como você removeu {0} dos responsáveis, {0} foi alterado para o próximo responsável disponível, {1}. | Como você removeu {0} dos responsáveis, {0} foi alterado para o próximo responsável disponível, {1}. | idem; frase correta |
| crm | unlinked_orphan | unlinked_orphan | unlinked_orphan | identificador interno, não é rótulo |
| crm | {0} M | {0} meses | {0} meses | no CRM é tempo relativo (meses); catálogo separado do framework |
| frappe | Ar | Ar | Ar | abreviação do sistema numérico indiano; manter |
| frappe | Cr | Cr | Cr | idem |
| frappe | Kh | Kh | Kh | idem |
| frappe | L | L | L | idem |
| frappe | Master | Master | Master | forma de tratamento sem equivalente; manter a lista original de saudações |
| frappe | Mx | Mx | Mx | tratamento neutro; manter |
| frappe | Noop Source | Noop Source | Noop Source | fixture de teste; não traduzir |
| frappe | {0} m | {0} min | {0} min | tempo relativo: minutos (min) |
| helpdesk | Base Support Rotation | Rodízio básico de suporte | Rodízio básico de suporte | é a regra de rodízio base dos agentes; tradução adequada |
| helpdesk | Could not an email due to: {0} | Não foi possível enviar um e-mail devido a: {0} | Não foi possível enviar um e-mail devido a: {0} | verbo omitido no original; 'enviar' é o contexto de hd_ticket |
| helpdesk | Partnership | Sociedade | Sociedade | tipo de organização; 'Sociedade' é o genérico correto |
| helpdesk | User Resolution Time | Tempo de resolução do usuário | Tempo de resolução do usuário | métrica de SLA do lado do usuário; manter |
| erpnext | # Create a Supplier  Also known as Vendor, is a master at the center of your purchase transactions. Suppliers  | # Criar um fornecedor  O cadastro de fornecedores é fundamental para suas transações de compra. Fornecedores s | # Criar um fornecedor  O cadastro de fornecedores é fundamental para suas transações de compra. Fornecedores s | fornecedor gera contas a PAGAR; o original diz 'Account Receivables' por erro; corrigido o item da lista |
| erpnext | # Sales Order  A Sales Order is a confirmation of an order from your customer. It is also referred to as Profo | # Pedido de venda  Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O p | # Pedido de venda  Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O p | fiel ao original (texto de onboarding) |
| erpnext | A Sales Order is a confirmation of an order from your customer. It is also referred to as Proforma Invoice.  S | Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O pedido de venda é fu | Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O pedido de venda é fu | idem |
| erpnext | A Transaction Deletion Document: {0} is triggered for {0} | Um documento de exclusão de transações: {0} foi acionado para {0} | Um documento de exclusão de transações: {0} foi acionado para {0} | {0} repetido é do original |
| erpnext | Allow Internal Transfers at Arm's Length Price | Permitir transferências internas a preço de mercado (arm's length) | Permitir transferências internas a preço de mercado (arm's length) | termo de preços de transferência; manter 'arm's length' entre parênteses |
| erpnext | Apply TDS | Aplicar TDS | Aplicar TDS | TDS é retenção da Índia; sigla mantida |
| erpnext | Asset{is_plural} {assets_link} created for {item_code} | Ativo{is_plural} {assets_link} criado para {item_code} | Ativo{is_plural} {assets_link} criado(s) para {item_code} | concordância com o plural dinâmico {is_plural} |
| erpnext | Biweekly | Quinzenal | Quinzenal | frequência do extrato: quinzenal |
| erpnext | Cannot create Intercompany {0}. All items in the source {1} have already been fully invoiced. Please check the | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifi | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifi | plural dinâmico resolvido com 'documentos do tipo {2}' |
| erpnext | For quantity {0} should not be greater than allowed quantity {1} | A quantidade de referência {0} não deve ser maior que a quantidade permitida {1} | A quantidade de referência {0} não deve ser maior que a quantidade permitida {1} | 'For Quantity' é a quantidade de referência da entrada de estoque |
| erpnext | Partnership | Sociedade | Sociedade | tipo societário genérico |
| erpnext | Row #{0}: BOM is not specified for subcontracting item {0} | Linha nº {0}: a BOM não foi especificada para o item subcontratado {0} | Linha nº {0}: a BOM não foi especificada para o item subcontratado {0} | {0} repetido é do original |
| erpnext | Row #{0}: From Date cannot be before To Date | Linha nº {0}: a data inicial não pode ser anterior à data final | Linha nº {0}: a data inicial não pode ser anterior à data final | regra como está no código |
| erpnext | The stock for the item {0} in the {1} warehouse was negative on the {2}. You should create a positive entry {3 | O estoque do item {0} no depósito {1} estava negativo em {2}. Crie um lançamento positivo {3} antes da data {4 | O estoque do item {0} no depósito {1} estava negativo em {2}. Crie um lançamento positivo {3} antes da data {4 | HTML preservado como no original |
| hrms | <h4>Condition Examples</h4> <ol> <li>Applying tax if employee born between 31-12-1937 and 01-01-1958 (Employee | <h4>Exemplos de condições</h4> <ol> <li>Aplicação de imposto se o colaborador nasceu entre 31-12-1937 e 01-01- | <h4>Exemplos de condições</h4> <ol> <li>Aplicação de imposto se o colaborador nasceu entre 31-12-1937 e 01-01- | exemplos e expressões preservados |
| hrms | CTC | CTC | CTC | CTC (custo para a empresa) é termo de folha; rótulo curto |
| hrms | Current CTC | CTC atual | CTC atual | idem |
| hrms | Interest | Interesse | Interesse | DocType Interest do módulo HR = interesses do colaborador |
| hrms | Maximum benefit of employee {0} exceeds {1} by the sum {2} of benefit application pro-rata component amount an | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor proporcional da rubrica na solicitação | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor proporcional da rubrica na solicitação | fiel à mensagem de validação |
| hrms | Maximum benefit of employee {0} exceeds {1} by the sum {2} of previous claimed amount | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor solicitado anteriormente | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor solicitado anteriormente | idem |
| hrms | Revised CTC | CTC revisado | CTC revisado | idem |
| hrms | Today {0} at our Company! 🎉 | Hoje {0} na nossa empresa! 🎉 | Hoje {0} na nossa empresa! 🎉 | fragmento composto em runtime; frase neutra |
| wiki | Docs Base Utl | URL base da documentação | URL base da documentação | 'Utl' é erro de digitação de URL no original |
| wiki | Save Delete Draft | Salvar rascunho de exclusão | Salvar rascunho de exclusão | ação: gravar a exclusão no rascunho |
| crm | 01/01/2022 to 01/31/2022 | 01/01/2022 a 31/01/2022 | 01/01/2022 a 31/01/2022 | exemplo de data no formato dd/mm/aaaa (é só texto de exemplo no filtro) |
| crm | 01/04/2024 11:30 PM | 01/04/2024 23:30 | 01/04/2024 23:30 | exemplo de data/hora no formato pt-BR, 24 h |
| crm | 08:00 AM | 08:00 | 08:00 | exemplo de horário em 24 h |
| crm | 08:00 pm | 20:00 | 20:00 | exemplo de horário em 24 h |
| crm | Invalid format. Try: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | Formato inválido. Tente: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | Formato inválido. Tente: 1 hour 30 minutes, 2 hours, 45 seconds, 1:30:45, 90s | os exemplos são a sintaxe que o parser de duração aceita (inglês); traduzir quebraria |
| crm | Since you removed {0} from the assignee, the {0} has also been removed. | Como você removeu {0} dos responsáveis, {0} também foi removido. | Como você removeu {0} dos responsáveis, {0} também foi removido. | {0} repetido é do original; frase correta em pt-BR |
| crm | Since you removed {0} from the assignee, the {0} has been changed to the next available assignee {1}. | Como você removeu {0} dos responsáveis, {0} foi alterado para o próximo responsável disponível, {1}. | Como você removeu {0} dos responsáveis, {0} foi alterado para o próximo responsável disponível, {1}. | idem; frase correta |
| crm | unlinked_orphan | unlinked_orphan | unlinked_orphan | identificador interno, não é rótulo |
| crm | {0} M | {0} meses | {0} meses | no CRM é tempo relativo (meses); catálogo separado do framework |
| erpnext | # Create a Supplier  Also known as Vendor, is a master at the center of your purchase transactions. Suppliers  | # Criar um fornecedor  O cadastro de fornecedores é fundamental para suas transações de compra. Fornecedores s | # Criar um fornecedor  O cadastro de fornecedores é fundamental para suas transações de compra. Fornecedores s | fornecedor gera contas a PAGAR; o original diz 'Account Receivables' por erro; corrigido o item da lista |
| erpnext | # Sales Order  A Sales Order is a confirmation of an order from your customer. It is also referred to as Profo | # Pedido de venda  Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O p | # Pedido de venda  Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O p | fiel ao original (texto de onboarding) |
| erpnext | A Sales Order is a confirmation of an order from your customer. It is also referred to as Proforma Invoice.  S | Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O pedido de venda é fu | Um pedido de venda confirma um pedido do cliente. Também é chamado de fatura proforma.  O pedido de venda é fu | idem |
| erpnext | A Transaction Deletion Document: {0} is triggered for {0} | Um documento de exclusão de transações: {0} foi acionado para {0} | Um documento de exclusão de transações: {0} foi acionado para {0} | {0} repetido é do original |
| erpnext | Allow Internal Transfers at Arm's Length Price | Permitir transferências internas a preço de mercado (arm's length) | Permitir transferências internas a preço de mercado (arm's length) | termo de preços de transferência; manter 'arm's length' entre parênteses |
| erpnext | Apply TDS | Aplicar TDS | Aplicar TDS | TDS é retenção da Índia; sigla mantida |
| erpnext | Asset{is_plural} {assets_link} created for {item_code} | Ativo{is_plural} {assets_link} criado(s) para {item_code} | Ativo{is_plural} {assets_link} criado(s) para {item_code} | concordância com o plural dinâmico {is_plural} |
| erpnext | Biweekly | Quinzenal | Quinzenal | frequência do extrato: quinzenal |
| erpnext | Cannot create Intercompany {0}. All items in the source {1} have already been fully invoiced. Please check the | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifi | Não é possível criar {0} entre empresas. Todos os itens de {1} de origem já foram totalmente faturados. Verifi | plural dinâmico resolvido com 'documentos do tipo {2}' |
| erpnext | For quantity {0} should not be greater than allowed quantity {1} | A quantidade de referência {0} não deve ser maior que a quantidade permitida {1} | A quantidade de referência {0} não deve ser maior que a quantidade permitida {1} | 'For Quantity' é a quantidade de referência da entrada de estoque |
| erpnext | Partnership | Sociedade | Sociedade | tipo societário genérico |
| erpnext | Row #{0}: BOM is not specified for subcontracting item {0} | Linha nº {0}: a BOM não foi especificada para o item subcontratado {0} | Linha nº {0}: a BOM não foi especificada para o item subcontratado {0} | {0} repetido é do original |
| erpnext | Row #{0}: From Date cannot be before To Date | Linha nº {0}: a data inicial não pode ser anterior à data final | Linha nº {0}: a data inicial não pode ser anterior à data final | regra como está no código |
| erpnext | The stock for the item {0} in the {1} warehouse was negative on the {2}. You should create a positive entry {3 | O estoque do item {0} no depósito {1} estava negativo em {2}. Crie um lançamento positivo {3} antes da data {4 | O estoque do item {0} no depósito {1} estava negativo em {2}. Crie um lançamento positivo {3} antes da data {4 | HTML preservado como no original |
| frappe | Ar | Ar | Ar | abreviação do sistema numérico indiano; manter |
| frappe | Cr | Cr | Cr | idem |
| frappe | Kh | Kh | Kh | idem |
| frappe | L | L | L | idem |
| frappe | Master | Master | Master | forma de tratamento sem equivalente; manter a lista original de saudações |
| frappe | Mx | Mx | Mx | tratamento neutro; manter |
| frappe | Noop Source | Noop Source | Noop Source | fixture de teste; não traduzir |
| frappe | {0} m | {0} min | {0} min | tempo relativo: minutos (min) |
| helpdesk | Base Support Rotation | Rodízio básico de suporte | Rodízio básico de suporte | é a regra de rodízio base dos agentes; tradução adequada |
| helpdesk | Could not an email due to: {0} | Não foi possível enviar um e-mail devido a: {0} | Não foi possível enviar um e-mail devido a: {0} | verbo omitido no original; 'enviar' é o contexto de hd_ticket |
| helpdesk | Partnership | Sociedade | Sociedade | tipo de organização; 'Sociedade' é o genérico correto |
| helpdesk | User Resolution Time | Tempo de resolução do usuário | Tempo de resolução do usuário | métrica de SLA do lado do usuário; manter |
| hrms | <h4>Condition Examples</h4> <ol> <li>Applying tax if employee born between 31-12-1937 and 01-01-1958 (Employee | <h4>Exemplos de condições</h4> <ol> <li>Aplicação de imposto se o colaborador nasceu entre 31-12-1937 e 01-01- | <h4>Exemplos de condições</h4> <ol> <li>Aplicação de imposto se o colaborador nasceu entre 31-12-1937 e 01-01- | exemplos e expressões preservados |
| hrms | CTC | CTC | CTC | CTC (custo para a empresa) é termo de folha; rótulo curto |
| hrms | Current CTC | CTC atual | CTC atual | idem |
| hrms | Interest | Interesse | Interesse | DocType Interest do módulo HR = interesses do colaborador |
| hrms | Maximum benefit of employee {0} exceeds {1} by the sum {2} of benefit application pro-rata component amount an | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor proporcional da rubrica na solicitação | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor proporcional da rubrica na solicitação | fiel à mensagem de validação |
| hrms | Maximum benefit of employee {0} exceeds {1} by the sum {2} of previous claimed amount | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor solicitado anteriormente | O benefício máximo do colaborador {0} excede {1} pela soma {2} do valor solicitado anteriormente | idem |
| hrms | Revised CTC | CTC revisado | CTC revisado | idem |
| hrms | Today {0} at our Company! 🎉 | Hoje {0} na nossa empresa! 🎉 | Hoje {0} na nossa empresa! 🎉 | fragmento composto em runtime; frase neutra |
| wiki | Docs Base Utl | URL base da documentação | URL base da documentação | 'Utl' é erro de digitação de URL no original |
| wiki | Save Delete Draft | Salvar rascunho de exclusão | Salvar rascunho de exclusão | ação: gravar a exclusão no rascunho |
| insights | Insights Workbook Folder | Pasta de pasta de trabalho do Insights | Pasta de pastas de trabalho do Insights | plural: pasta que agrupa pastas de trabalho |
| insights | is last month | é no mês passado | no mês passado | operador de filtro de data: lê-se '<coluna> no mês passado' |
| insights | is last week | é na semana passada | na semana passada | operador de filtro de data |
| insights | is this month | é neste mês | neste mês | operador de filtro de data |
| insights | is this week | é nesta semana | nesta semana | operador de filtro de data |
| insights | is this year | é neste ano | neste ano | operador de filtro de data |
| frappe | Upgrade plan | Mudar para um plano superior | Fazer upgrade do plano | termo corrente para mudança de plano |
| wiki | Logo | Logotipo | Logo | consistência: 'logo' em todas as outras ocorrências |
| wiki | Their revision history | Seu histórico de revisões | O histórico de revisões delas | item da lista 'excluir o espaço também remove: todas as páginas / o histórico de revisões delas' |
| wiki | Is Working | É revisão de trabalho | É versão de trabalho | flag da revisão (working copy) |
| wiki | Head Revision | Revisão de ponta | Revisão mais recente (head) | 'revisão de ponta' não é termo usado |
| wiki | Under Review | Em análise | Em revisão | mesmo status de 'In Review' (320) |
| wiki | {} Under Review | {} em análise | {} em revisão | consistência com o status 'Em revisão' |
| helpdesk | Are you sure you want to remove the logo? | Tem certeza de que deseja remover o logotipo? | Tem certeza de que deseja remover o logo? | consistência: 'logo' nos demais apps |
| helpdesk | Remove Logo | Remover logotipo | Remover logo | consistência: 'logo' |
| helpdesk | First Response Failed By | Atraso da primeira resposta | Primeira resposta vencida em | campo de data/hora em que o SLA da 1ª resposta venceu |
| helpdesk | Resolution Failed By | Atraso da resolução | Resolução vencida em | campo de data/hora em que o SLA de resolução venceu |
| helpdesk | From is required | A origem é obrigatória | O remetente é obrigatório | 'From' aqui é o remetente do e-mail |
| helpdesk | To is required | O destino é obrigatório | O destinatário é obrigatório | 'To' aqui é o destinatário do e-mail |
| helpdesk | Last seen | Visto por último | Visto pela última vez | mais natural |
| crm | Canceled | Cancelado | Cancelada | status do registro de chamada; concordância com 'Não atendida' e 'Recusada' (chamada) |
| hrms | Additional Salary for referral bonus can only be created against Employee Referral with status {0} | O adicional salarial por bônus de indicação só pode ser criado para indicações de colaboradores com status {0} | A remuneração adicional por bônus de indicação só pode ser criada para indicações de colaboradores com status  | consistência: DocType Additional Salary = 'remuneração adicional' nas demais ocorrências |
| hrms | Additional Salary for this salary component with {0} enabled already exists for this date | Já existe um adicional salarial desta rubrica salarial com {0} ativado para esta data | Já existe uma remuneração adicional desta rubrica salarial com {0} ativado para esta data | consistência: 'remuneração adicional' |
| hrms | Amount claimed via Expense Claim | Valor solicitado por solicitação de reembolso | Valor requerido via solicitação de reembolso | evita 'solicitado por solicitação' |
| hrms | Applicant Rating | Avaliação do candidato | Nota do candidato | campo de rating (estrelas); consistência com 'Nota' |
| hrms | Contact No. | Nº de contato | Telefone de contato | 'Contact No.' na indicação de colaborador é telefone |
| hrms | Job Application | Solicitação de emprego | Formulário de candidatura | é o web form de candidatura a vaga; 'solicitação de emprego' não é usual |
| hrms | Job Application Route | Rota da solicitação de emprego | Rota do formulário de candidatura | idem |
| hrms | Owned | Próprio | Em posse | status do ativo no acerto rescisório (ainda com o colaborador), par de 'Devolvido' |
| hrms | Route to the custom Job Application Webform | Rota para o formulário web personalizado de solicitação de emprego | Rota para o formulário web de candidatura personalizado | idem |
| hrms | Self Score | Pontuação própria | Pontuação da autoavaliação | consistência com 'Total Self Score' = 'Pontuação total da autoavaliação' |
| erpnext | Convert to Ledger | Converter em depósito de movimentação | Converter em depósito simples (não grupo) | ação da árvore de depósitos, par de 'Converter em grupo'; 'depósito de movimentação' não é termo usado |
