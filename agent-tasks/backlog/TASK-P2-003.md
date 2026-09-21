# TASK-P2-003 — Envelope externo por ajuste multivista do sprite 360°

**Fase:** 4 · **Prioridade:** alta · **Bloco de IDs:** `CLM-1100…1149`, `EVD-1100…1149`
**Gate que libera:** G-R4 · **Testes:** V-G02, V-G03, V-G06

## Objetivo
Reconstruir o contorno externo e o perfil curvo da caixa por ajuste conjunto sobre as 81 vistas do
visualizador 360° oficial, e responder onde no contorno se aplicam os 1,75 mm publicados (Q-CASE-002).

## Contexto
IMG-0012/IMG-0013 são sprites de 64 800 × 800 px contendo 81 quadros de 800 × 800 que cobrem 360° em
passos de 4,44°, em duas iluminações — 162 vistas auto-consistentes do mesmo objeto, com rotação de eixo
único e passo constante. É exatamente o insumo que o `CLAUDE.md` §7 pede para ajuste conjunto multivista.
O script de fatiamento já existe (`fatiar_sprite_360.py`, detecção do número de quadros por FFT).
A caixa é curva no eixo longo: a silhueta de perfil é **envoltória**, não seção.

## Fontes permitidas
IMG-0012, IMG-0013 (sprites), IMG-0009, IMG-0011 (par ortogonal CG), IMG-0007 (perfil), IMG-0033.
As seis vistas ortogonais do USD991795 **apenas por proporção relativa**, nunca por medida.

## Entradas
Âncora de escala: 51,00 × 39,00 mm. Quadros fatiados em `research/images/frames/360-d01/` (fora do Git,
reprodutíveis). `solvers/geometry_fit/`.

## Saídas obrigatórias
1. `solvers/geometry_fit/silhueta.py` — extração de silhueta por quadro e ajuste conjunto de uma superfície
   paramétrica de caixa (perfil curvo + contorno tonneau).
2. `evidence/measurements/P2-003-envelope.csv` — contorno amostrado e curva de perfil, com resíduo por vista.
3. **Métrica de erro de projeção CAD→imagem** implementada e reportada por vista (`CLAUDE.md` §7, item 11).
4. Veredito sobre Q-CASE-002, com o ponto do contorno em que a espessura atinge 1,75 mm.
5. `cad/reference/` — perfil e contorno exportados em DXF/CSV para a Fase 4.
6. `agent-tasks/review/TASK-P2-003.md`.

## Restrições
- As 81 vistas são **render CG oficial**: o contorno delas nasce classe **E**, não C, até que a escala seja
  cruzada com uma fotografia (DEC-003). Dizer isso explicitamente no relatório é obrigatório.
- Nenhuma medida sai das pranchas do USD991795.
- Não forçar simetria no ajuste: V-G06 reprova simetria imposta sem evidência.
- Se o ajuste não convergir, entregar o resíduo e a razão — não entregar um contorno "suavizado à mão".

## Questões abertas endereçadas
Q-CASE-002 (principal), Q-CASE-001, Q-CASE-005, Q-STR-001, Q-IMG-006.

## Testes
Reprojeção do contorno ajustado em 10 quadros não usados no ajuste, com erro reportado; o eixo longo
recuperado bate com 51,00 mm dentro de 1%.

## Critério de aceitação
Uma superfície de caixa paramétrica que reprojeta sobre as 81 vistas com erro reportado, e uma resposta
numérica para Q-CASE-002 — ou a demonstração de que as 81 vistas não bastam para respondê-la.

## Arquivos que podem ser alterados
`solvers/geometry_fit/**`, `evidence/**`, `cad/reference/**`, `research/claims.csv`,
`docs/OPEN-QUESTIONS.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-003.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/PROJECT-CHARTER.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`,
`engineering/master-parameters.yaml` (sem fotografia que cruze a escala, nada de classe C sai daqui).
