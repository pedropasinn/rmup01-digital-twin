# TASK-P2-002 — Calibração de IMG-0004: contorno da caixa, comandos, cristais e parafusos

**Fase:** 3–4 · **Prioridade:** alta · **Bloco de IDs:** `CLM-1050…1099`, `EVD-1050…1099`
**Gate que libera:** G-R3 · **Testes:** V-G02, V-G05

## Objetivo
Extrair, por homografia calibrada, as primeiras dimensões classe C do projeto: contorno externo da luneta,
centros e diâmetros dos dois comandos, aberturas dos dois cristais, posição dos parafusos spline, e a
repartição da folga movimento–caixa.

## Contexto
IMG-0004 (`illup068.jpg`, 2500 × 1216) é uma explodida em plano, câmera aparentemente nadir, com luneta,
junta, as duas rodas de comando, o fundo e o movimento **no mesmo plano e na mesma escala**. É a imagem
mais importante para a Fase 4 e a candidata número 1 a calibração usando 41,45 × 28,85 mm. IMG-0027
(movimento dentro da caixa, vista quase nadir) é o complemento que fecha Q-BASE-002.

## Fontes permitidas
IMG-0004, IMG-0006 (macro dos comandos), IMG-0027, IMG-0009/IMG-0011 (par ortogonal, para conferência).
`research/images/catalogo.csv`, `evidence/image-landmarks/candidatos.csv`.

## Entradas
Âncoras: 41,45 × 28,85 mm (movimento) e 51,00 × 39,00 mm (caixa) — duas âncoras independentes na mesma
imagem, o que permite verificação cruzada da escala. Landmarks LMK-IMG0004-001…006, LMK-IMG0006-001/002,
LMK-IMG0027-001. `solvers/image_metrology/homografia.py` (de TASK-P2-001).

## Saídas obrigatórias
1. `evidence/measurements/P2-002-caixa.csv` — contorno da luneta amostrado, com incerteza.
2. Parâmetros novos em `engineering/master-parameters.yaml`, todos classe **C**: `P_SEL_CENTER_X/Y`,
   `P_WND_CENTER_X/Y`, `P_CRY_HOURS_DIAM`, `P_CRY_BALANCE_DIAM`, `P_WND_CROWN_DIAM`, `P_MOV_OFFSET_X/Y`.
3. `evidence/overlays/P2-002-*.png`.
4. Resposta a Q-BASE-001 (qual eixo é 41,45) e a Q-FST-001 (contagem e posição dos parafusos).
5. `agent-tasks/review/TASK-P2-002.md`.

## Restrições
- Distorção radial residual de grande angular é provável nas bordas de IMG-0004: estimar ou declarar
  inestimável, nunca ignorar em silêncio.
- A conferência com a segunda âncora (51 × 39) é obrigatória; divergência acima de 2% entre as duas
  escalas invalida a calibração e vira questão aberta.
- Nenhum valor entra em `master-parameters.yaml` sem `evidence_class: C`, `method`, `sources` e incerteza.
- Nenhuma medida do fundo é transportada para o plano da luneta sem correção — são planos diferentes.

## Questões abertas endereçadas
Q-BASE-001, Q-BASE-002, Q-CRY-002, Q-FST-001, Q-FST-002, Q-WND-005, Q-CASE-003.

## Testes
As duas âncoras independentes produzem escalas que concordam dentro de 2%; cada medida repetida em ao menos
duas imagens tem dispersão registrada; V-G02 passa com o contorno medido.

## Critério de aceitação
Ao menos seis parâmetros novos classe C no `master-parameters.yaml`, cada um com incerteza e overlay de
evidência, e Q-BASE-001 fechada com número.

## Arquivos que podem ser alterados
`evidence/**`, `engineering/master-parameters.yaml`, `research/claims.csv`, `docs/OPEN-QUESTIONS.md`,
`docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-002.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/PROJECT-CHARTER.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`,
`docs/CAD-RECONSTRUCTION-PLAN.md`, `research/source-manifest.csv`.
