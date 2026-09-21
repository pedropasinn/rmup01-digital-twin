# TASK-P2-012 — Recepção e integração das entregas U01–U20 do Balcão

**Fase:** 1 residual / contínua · **Prioridade:** média, mas com prazo externo · **Bloco de IDs:** `SRC-1000…1199`, `CLM-1550…1699`

## Objetivo
Receber, julgar e integrar as 20 entregas do Balcão sem contaminar o corpus: cada claim de terceiro passa
por conferência de URL, reavaliação de classe e remapeamento de ID antes de existir no repositório.

## Contexto
Os 20 pedidos U01–U20 estão registrados em `pedidos-chatgpt/PEDIDOS.json` com `run_id` no agenthub, e as
entregas voltam como `<ID>-entrega.zip` em `_entrada/Balcao/`. Cada zip traz `LEIA-ME.md`, `fontes.csv` e
`claims.csv` com **IDs locais**, que colidem com os nossos se forem copiados sem tradução. O que cada
pedido deve fechar está tabelado em `docs/MASTER-RESEARCH-PLAN.md` §3.

## Fontes permitidas
Os zips em `_entrada/Balcao/`; as URLs que eles citam, conferidas por nós.

## Entradas
`pedidos-chatgpt/PEDIDOS.json`; `docs/MASTER-RESEARCH-PLAN.md` §3 (o que cada pedido deve fechar);
`research/source-manifest.csv` e `research/claims.csv` atuais, para deduplicação.

## Saídas obrigatórias
Por entrega processada:
1. Tabela de remapeamento `<ID local> → <SRC-/CLM- do projeto>`, guardada junto ao relatório.
2. Linhas novas em `research/source-manifest.csv` e `research/claims.csv`, **só** para o que sobreviveu ao
   julgamento.
3. Registro do que foi **rejeitado** e por quê, em `docs/FAILURE-LOG.md`.
4. Divergências com o nosso corpus abertas como questão em `docs/OPEN-QUESTIONS.md` — nunca resolvidas por
   sobrescrita silenciosa.
5. Scripts e documentos utilizáveis (U13 `gear_search.py`, U19 `homografia.py`/`dentes.py`, U16 glossário)
   avaliados e, se aproveitados, integrados com atribuição e com os nossos testes por cima.
6. `agent-tasks/review/TASK-P2-012-<ID>.md` por entrega, ou um relatório consolidado por lote.

## Restrições — o julgamento, em quatro passos obrigatórios
1. **URL conferida por nós** (`curl -sIL` ou WebFetch). URL que não abre, claim que não entra.
2. **Classe A–F reavaliada** segundo o nosso `CLAUDE.md` §1, não segundo a do terceiro. Material de
   pesquisa de terceiro **nunca é fonte primária**.
3. **Nenhuma dimensão vinda de desenho de patente ou de registro de desenho**, por mais bem apresentada que
   esteja.
4. **Entrega que afirma um número sem fonte verificável é rejeitada inteira**, não corrigida parcialmente.
   Corrigir parcialmente é como uma reconstrução forense morre: um número bom carrega dez ruins.

Além disso: nenhum parâmetro de `master-parameters.yaml` muda por entrega de terceiro sem que a fonte
primária correspondente seja conferida diretamente por nós.

## Questões abertas endereçadas
Todas as do `MASTER-RESEARCH-PLAN.md` §3, conforme a entrega. Em especial Q-DOC-001 (U01), Q-PAT-001 (U04),
Q-CASE-010 (U05), Q-DOC-002 (U09), Q-OSC-001 (U12), Q-TRN-002 (U13), Q-SEL-001 (U15), Q-TRN-001 (U16).

## Testes
Nenhum `source_id` ou `claim_id` duplicado após a integração; nenhum claim novo sem fonte conferida;
`research/claims.csv` continua parseável e com todas as colunas do esquema.

## Critério de aceitação
Cada entrega processada tem: quantos claims entraram, quantos foram rejeitados e por quê, e quais questões
abertas ela fechou ou estreitou. Uma entrega que não fechou nada é resultado legítimo e fica registrada
como tal.

## Arquivos que podem ser alterados
`research/source-manifest.csv`, `research/claims.csv`, `research/patents/**`, `research/translations/**`,
`solvers/**` (código de terceiro aproveitado, com atribuição), `docs/OPEN-QUESTIONS.md`,
`docs/HYPOTHESES.md`, `docs/FAILURE-LOG.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/**`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/PROJECT-CHARTER.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`,
`docs/MASTER-RESEARCH-PLAN.md`, `engineering/master-parameters.yaml`, `evidence/evidence-ledger.csv`
(entrega de terceiro não escreve no ledger de evidência).
