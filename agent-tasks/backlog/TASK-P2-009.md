# TASK-P2-009 — W/H: máquina de estados e mapa de peças do seletor

**Fase:** 8 (preparação) · **Prioridade:** alta · **Bloco de IDs:** `CLM-1400…1449`, `IMG-0037…`
**Testes:** V-S01…V-S05

## Objetivo
Extrair do filme oficial, quadro a quadro, tudo que se pode saber sobre o seletor e a corda, e montar a
máquina de estados W/H com as peças nomeadas e o que falta declarado.

## Contexto
Este relógio **não tem haste de corda**: as duas coroas são rodas do próprio calibre integradas à caixa,
porque o diâmetro mínimo de 1,5 mm de uma tige não cabia. Toda a Fase 8 tem de ser desenhada a partir disso,
e as peças canônicas do remontoir (tige, pignon coulant, bascule, tirette, sautoir) **não podem ser criadas
por analogia**. O que se sabe: girar o seletor de cima desloca um braço deslizante; para um lado engata a
corda, para o outro o acerto e **desacopla o barrilete**; há limitador de torque; a vedação é por aro de
cerâmica; as duas coroas têm o mesmo desenho e o mesmo encaixe spline; as coroas são montadas **antes** do
encaixotamento.

## Fontes permitidas
`research/videos/RMUP-01_SF_EN.mp4` (SRC-0009) e `caliber.mp4`; os 17 quadros-chave já catalogados;
IMG-0026 (recortes da platina), IMG-0004, IMG-0006, IMG-0032. Reextração de janelas a 25 fps com o script
existente é permitida e esperada.

## Entradas
`research/videos/VID-0001-quadros.csv`; `solvers/image_metrology/extrair_quadros_chave.py`.

## Saídas obrigatórias
1. Novos quadros-chave catalogados (`IMG-0037…`) nas janelas do braço deslizante, da montagem das coroas e
   da sequência de corda, com timestamp e critério de nitidez.
2. `engineering/winding-setting/ESTADOS.md` — máquina de estados W ↔ H, com o que engata e o que desengata
   em cada estado, e a verificação de ausência de dupla conexão em toda a transição.
3. Atualização de `engineering/interfaces.csv`: IFC-013…IFC-021 saem de `hypothetical` onde a imagem
   permitir, ou ganham nota explicando por que continuam hipotéticas.
4. Veredito sobre Q-IMG-005 (as duas rodas do prolongamento esquerdo são coroa e cliquet?).
5. `agent-tasks/review/TASK-P2-009.md`.

## Restrições
- O filme institucional **alterna render e filmagem real sem avisar** (CLM-0710): cada quadro novo entra no
  catálogo com `natureza` declarada, e quadro de render não vira evidência do objeto.
- **Armadilha conhecida:** na foto de encaixotamento da Hodinkee o movimento está girado 180° em relação à
  posição final. Qualquer comparação de posição ou de sentido tem de corrigir isso (Q-SEL-003).
- Não inventar came, mola ou detent para fechar a máquina de estados: peça não observada entra como
  `hypothetical` com classe E e continua na lista.
- Não usar a associação legenda↔imagem do filme como evidência técnica (Q-IMG-004): em filme institucional
  elas são montadas, não sincronizadas.

## Questões abertas endereçadas
Q-SEL-001, Q-SEL-002, Q-SEL-003, Q-WND-001, Q-WND-004, Q-WND-005, Q-IMG-005.

## Testes
V-S01…V-S04 sobre a máquina de estados descrita (ainda sem geometria 3D): os dois estados são mutuamente
coerentes e não há posição intermediária com dupla conexão.

## Critério de aceitação
Uma máquina de estados que um relojoeiro consiga criticar: cada transição com a peça que a realiza nomeada,
ou explicitamente marcada como desconhecida.

## Arquivos que podem ser alterados
`research/images/catalogo.csv`, `research/videos/VID-0001-quadros.csv`,
`engineering/winding-setting/**`, `engineering/interfaces.csv`, `research/claims.csv`,
`docs/OPEN-QUESTIONS.md`, `docs/HYPOTHESES.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-009.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`, `engineering/bom-reconstructed.csv`
(as peças novas vão no relatório; o diretor técnico integra), `engineering/master-parameters.yaml`.
