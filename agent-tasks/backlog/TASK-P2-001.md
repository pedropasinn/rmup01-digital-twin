# TASK-P2-001 — O render oficial é fiel? (IMG-0001 × IMG-0026)

**Fase:** 2 · **Prioridade:** máxima, primeiro da onda · **Bloco de IDs:** `CLM-1000…1049`, `EVD-1000…1049`, `LMK-*` novos
**Gate que libera:** G-R2 · **Teste de validação:** V-000

## Objetivo
Decidir Q-IMG-003: os centros medidos no render oficial do calibre (IMG-0001) convergem, dentro da
incerteza, com os centros medidos na platina nua real (IMG-0026)? O veredito define se a imagem mais
informativa do corpus pode ser usada como guia topológico ou se cai para ilustrativa.

## Contexto
IMG-0001 (`EV05_2206_RM_UP_FRONT_UNDER_V02_FONDcalibre.jpg`, 2188 × 2500) é a vista mais completa do
calibre — e é um render CG oficial (DEC-003), o que faz de qualquer medida tirada dela classe E.
IMG-0026 (quadro do filme de savoir-faire em t = 25,42 s, 1920 × 1080) é a única imagem pública em que os
furos de pivô do lado do trem não estão cobertos por pontes, com o suporte de montagem — hastes retas e
paralelas de fábrica — servindo de referência de plano. As duas nunca foram comparadas.

## Fontes permitidas
`research/images/rm-oficial/EV05_2206_RM_UP_FRONT_UNDER_V02_FONDcalibre.jpg`;
`research/images/frames/VID-0001-key/IMG-VID0001-K025_42.png` (reproduzível pelo script existente a partir
do mp4 e do timestamp); `research/images/catalogo.csv`; `evidence/image-landmarks/candidatos.csv`.
Nenhuma imagem nova. Nenhum upload a serviço de terceiro.

## Entradas
- Âncora de escala: 41,45 × 28,85 mm (CLM-0001/0002), aplicada ao contorno do movimento/platina.
- Landmarks já propostos: LMK-IMG0026-001…005 e LMK-IMG0001-001…004.
- Python 3.12 da venv do projeto; PIL, numpy; opencv se necessário (registrar a instalação).

## Saídas obrigatórias
1. `solvers/image_metrology/homografia.py` — funções de homografia de 4+ pontos, conversão px→mm com
   propagação de incerteza, e teste com pontos sintéticos.
2. `evidence/measurements/P2-001-centros.csv` — para cada centro: `landmark_id`, `image_id`, x/y em mm no
   sistema do movimento, incerteza, método.
3. `evidence/overlays/P2-001-*.png` — sobreposição das duas nuvens de centros, com barras de erro.
4. Linhas em `evidence/evidence-ledger.csv` (bloco EVD-1000…) e em `research/claims.csv` (CLM-1000…).
5. Veredito escrito em `docs/OPEN-QUESTIONS.md` na linha Q-IMG-003, com uma das três consequências do
   `VALIDATION-PLAN.md` §1.
6. `agent-tasks/review/TASK-P2-001.md`.

## Restrições
- Calibração só com âncora **no mesmo plano** do que se mede (`CLAUDE.md` §7).
- IMG-0001 tem inclinação de ~10–15° em torno do eixo vertical e ~5° em torno do horizontal: a homografia
  tem de tratar isso, não ignorar.
- Nenhuma medida sai de IMG-0014…IMG-0025 (render de terceiro), nem entra no relatório.
- Medida tirada de IMG-0001 nasce classe **E**; de IMG-0026 pode chegar a **C** (DEC-003).
- Não ajustar escala de nenhuma imagem para fazer as nuvens coincidirem — isso é o erro nomeado no §13.

## Questões abertas endereçadas
Q-IMG-003 (principal), Q-IMG-002, Q-BASE-001, Q-BASE-004, Q-CASE-004, Q-IMG-005.

## Testes
- O `homografia.py` reproduz, sobre pontos sintéticos com homografia conhecida, a transformação inversa com
  erro < 0,1 px.
- A escala recuperada em cada imagem, aplicada ao eixo curto, reproduz 28,85 mm dentro de 1%.
- Cada centro medido em pelo menos duas imagens tem dispersão registrada.

## Critério de aceitação
Q-IMG-003 sai de "aberta" para uma das três consequências, com número: resíduo médio e máximo em mm, e a
incerteza combinada contra a qual ele foi comparado. Um relatório que diga "parece coincidir" sem número
é rejeitado.

## Arquivos que podem ser alterados
`solvers/image_metrology/**`, `evidence/measurements/**`, `evidence/overlays/**`,
`evidence/evidence-ledger.csv`, `research/claims.csv`, `docs/OPEN-QUESTIONS.md` (só a linha Q-IMG-003),
`docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-001.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/PROJECT-CHARTER.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`,
`engineering/master-parameters.yaml` (este pacote não confirma âncora de fabricante),
`research/images/catalogo.csv`, `research/source-manifest.csv`.
