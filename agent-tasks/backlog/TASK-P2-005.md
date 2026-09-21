# TASK-P2-005 — Mapa de centros da platina nua (IMG-0026)

**Fase:** 5 · **Prioridade:** máxima depois de TASK-P2-001 · **Bloco de IDs:** `CLM-1200…1249`, `EVD-1200…1249`
**Gate que libera:** G-R5 (→ M2) · **Testes:** V-G05, V-M05

## Objetivo
Produzir o mapa de centros do calibre: todos os furos de pivô, o centro do barrilete, os centros das duas
rodas do caminho de corda, o entalhe de banking e o furo do parafuso central de caixa, medidos em
milímetros no sistema de coordenadas do movimento, com incerteza.

## Contexto
IMG-0026 é a imagem mais valiosa do corpus: a única em que os furos de pivô do lado do trem não estão
cobertos por pontes. As hastes retas e paralelas do suporte de montagem dão o par de linhas para estimar
pontos de fuga e calibrar a homografia sem depender do próprio relógio. Este pacote é o que transforma a
arquitetura da Fase 2, hoje toda qualitativa, em geometria.

## Fontes permitidas
IMG-0026; IMG-0027 e IMG-0001 como segunda projeção (esta última com a ressalva de Q-IMG-003);
IMG-0003 + IMG-0028 para a ponte de 3 braços; IMG-0029 para a região barrilete/balanço.

## Entradas
Âncora: contorno da platina, 41,45 × 28,85 mm. Landmarks LMK-IMG0026-001…005.
`solvers/image_metrology/homografia.py`.

## Saídas obrigatórias
1. `evidence/measurements/P2-005-centros.csv` — um centro por linha, com `part_id` provável,
   x/y em mm, incerteza, imagens usadas, dispersão.
2. Parâmetros `P_<SUB>_CENTER_<NNN>_X/Y` em `master-parameters.yaml`, classe C, com incerteza.
3. Atualização de `engineering/bom-reconstructed.csv`: peças que saem de E para B/C/D à luz do que se vê.
4. `evidence/overlays/P2-005-*.png`.
5. Inventário parcial de rubis visíveis (entrada de Q-JWL-001).
6. `agent-tasks/review/TASK-P2-005.md`.

## Restrições
- Todo centro medido em pelo menos duas imagens independentes quando possível; dispersão registrada.
- Não nomear peça pela função sem marcar `provisional`: as "roda de coroa" e "roda de cliquet" de CLM-0705
  são leitura funcional, não declaração do fabricante (Q-IMG-005).
- Nenhum centro é inventado para completar um trem plausível. Centro que não se vê, não entra.
- Não usar IMG-0001 como fonte de posição se TASK-P2-001 tiver rebaixado o render a ilustrativo.

## Questões abertas endereçadas
Q-BASE-004, Q-BRG-001, Q-BRG-002, Q-TRN-003, Q-CASE-004, Q-ESC-004, Q-ESC-005, Q-ESC-009, Q-JWL-001,
Q-FST-003, Q-IMG-005.

## Testes
V-G05 sobre os centros medidos; o contorno recuperado reproduz 41,45 × 28,85 mm dentro de 1%; cada centro
tem incerteza declarada.

## Critério de aceitação
Um mapa de centros que a Fase 7 possa consumir como entrada do `gear_search`, com incerteza por centro — e
uma lista explícita dos centros que **não** foi possível medir e por quê.

## Arquivos que podem ser alterados
`evidence/**`, `engineering/master-parameters.yaml`, `engineering/bom-reconstructed.csv`,
`research/claims.csv`, `docs/OPEN-QUESTIONS.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-005.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/PROJECT-CHARTER.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md` (a arquitetura só é
reescrita pelo diretor técnico, com base neste relatório), `engineering/interfaces.csv`.
