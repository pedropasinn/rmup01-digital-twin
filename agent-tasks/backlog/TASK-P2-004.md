# TASK-P2-004 — Z-budget v0 com as duas colunas de cristal

**Fase:** 3 · **Prioridade:** alta · **Bloco de IDs:** `CLM-1150…1199`
**Gate que libera:** G-R4 · **Testes:** V-Z01…V-Z05

## Objetivo
Implementar o `engineering/stack-height.csv` e os testes automáticos de Z-budget, carregando **em paralelo**
as duas hipóteses de espessura do cristal das horas, conforme DEC-005 e `CAD-RECONSTRUCTION-PLAN.md` §4.

## Contexto
O orçamento vertical deste relógio não é uma pilha só: é uma pilha por coluna. A coluna do balanço fecha em
1,56 mm de material declarado, deixando 0,19 mm para todas as folgas. A coluna da indicação, na Hipótese A
(cristal 0,45 mm), exige que a região da indicação seja pelo menos 0,06 mm mais baixa que o ponto mais alto
do calibre — uma previsão testável que tem apoio indireto em CLM-0420 (eixo da indicação apoiado contra o
cristal). Esta é a razão pela qual Q-CRY-001 **não precisa** ser decidida agora.

## Fontes permitidas
`engineering/master-parameters.yaml`, `docs/FACTS.md`, `docs/CAD-RECONSTRUCTION-PLAN.md`,
`engineering/bom-reconstructed.csv`. Nenhuma fonte externa: este pacote é aritmética sobre o que já temos.

## Entradas
1,75 mm (relógio) · 1,18 mm (calibre) · 0,18 mm (parede mínima) · 0,45 mm **ou** 0,20 mm (cristal das
horas) · 0,20/0,30 mm (cristal do balanço) · rebaixo interno de profundidade desconhecida.

## Saídas obrigatórias
1. `engineering/stack-height.csv` preenchido, com uma linha por peça de cada coluna e os campos
   `z_min`, `z_max`, `thickness`, `clearance_below`, `clearance_above`, classe, status.
2. `tests/stack_height/test_zbudget.py` — V-Z01…V-Z05, rodando **duas vezes**, uma por hipótese, e
   reportando em qual delas cada coluna fecha.
3. `tests/stack_height/test_no_hidden_placeholders.py` — reprova qualquer soma que use camada classe `F`
   como se fosse medida.
4. Relatório `engineering/Z-BUDGET-v0.md` com as duas colunas lado a lado e as consequências de cada uma.
5. `agent-tasks/review/TASK-P2-004.md`.

## Restrições
- **Nenhuma folga em zero por conveniência.** Folga zero é afirmação de contato e exige `interface_id`.
- Toda camada de espessura desconhecida entra como `F — PLACEHOLDER` declarado, nunca como estimativa
  silenciosa. O "talvez 0,05 mm" do rebaixo é chute de terceiro e **não entra**.
- Não escolher uma das duas hipóteses de cristal. Carregar as duas é o entregável.
- Não inventar espessura de platina: ela é Q-BASE-003 e fica como incógnita do sistema.

## Questões abertas endereçadas
Q-CRY-001, Q-BASE-003, Q-CASE-003, Q-IND-004, Q-OSC-004, Q-ESC-006.

## Testes
Os próprios V-Z01…V-Z05. O pacote está errado se algum teste passar por acidente com placeholder.

## Critério de aceitação
Um `stack-height.csv` em que qualquer pessoa consiga apontar, linha a linha, de onde veio cada milímetro, e
um conjunto de testes que reprova um relógio de 1,76 mm.

## Arquivos que podem ser alterados
`engineering/stack-height.csv`, `engineering/Z-BUDGET-v0.md`, `tests/stack_height/**`,
`docs/OPEN-QUESTIONS.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-004.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/CAD-RECONSTRUCTION-PLAN.md`,
`engineering/master-parameters.yaml` (este pacote consome parâmetros, não os cria).
