# Charter — RM UP-01 · reconstrução forense digital

Aberto em 20/09/2026 por Pedro Pasin; direção técnica de Claude (Fable 5.1); execução por agentes Claude Opus (o uso do Codex está reduzido por decisão de Pedro em 20/09; ver DEC-001).

## Objeto
Reconstruir digitalmente o Richard Mille RM UP-01 Ferrari e o calibre RMUP-01: forma externa, arquitetura do movimento, peças, interfaces, cinemática, empilhamento vertical (Z-budget), materiais, lógica de corda/ajuste (seletor W/H), trem, barrilete, escape ultraplano patenteado, oscilador, indicação e integração movimento–caixa. Exclusivamente digital e educacional; sem fabricação; CAD desenvolvido como se pudesse ser auditado para fabricabilidade.

## Princípio
"Como sabemos disso?" Toda afirmação, dimensão e peça carrega classe de evidência A–F, fonte, método, incerteza e estado (`confirmed`, `provisional`, `contested`, `placeholder`). Nunca apresentar C, D, E ou F como A. Hipóteses concorrentes convivem até um teste discriminar.

## Fora de escopo
Fabricar; obter material vazado, privado ou por acesso indevido; republicar imagens protegidas no site; declarar "réplica exata".

## Entregáveis por marco (gates, não calendário)
M0 sistema de pesquisa vivo · M1 envelope geométrico conhecido · M2 esqueleto mecânico · M3 esqueleto cinemático (energia + W/H) · M4 escape resolvido · M5 montagem nominal completa · M6 CAD convergido com evidência · M7 auditoria de plausibilidade · M8 gêmeo digital forense v1 · M9 site público de conhecimento.

## Fontes de verdade
`engineering/master-parameters.yaml` (toda dimensão mestre), `evidence/evidence-ledger.csv` (toda evidência), `research/source-manifest.csv` (toda fonte), `research/claims.csv` (toda afirmação). O CAD deriva do conhecimento; o conhecimento nunca vive só no CAD.

## Convenções de identificadores
- Fontes `SRC-0001`; imagens `IMG-0001`; vídeos `VID-0001`; quadros de vídeo `IMG-VID0001-F000123`; patentes `PAT-EP3754433A1`.
- Claims `CLM-0001`; evidências `EVD-0001`; parâmetros `P_<SUBSISTEMA>_<NOME>` (ex.: `P_MOV_LENGTH`, `P_TRAIN_CENTER_03`); peças `PRT-<SUB>-<NNN>` (ex.: `PRT-ESC-001`); interfaces `IFC-<NNN>`; landmarks `LMK-<IMG>-<NNN>`; questões `Q-<SUB>-<NNN>`; hipóteses `H-<SUB>-<NNN>`; decisões `DEC-NNN`; tarefas `TASK-<FASE>-<NNN>`.
- Subsistemas: CASE, CRY (cristais), BASE (platina), BRG (pontes), BAR (barrilete), WND (corda), SEL (seletor W/H), TRN (trem), ESC (escape), OSC (oscilador), IND (indicação/motion works), JWL (rubis), SHK (choque), FST (fixações), STR (pulseira).

## Ferramentas
Python 3.12 (venv própria; numpy, opencv, shapely, cadquery para geometria auxiliar), Autodesk Fusion como CAD canônico (na máquina de Pedro; a Dell não tem Fusion — scripts preparados e executados quando disponível), Playwright para captura, agentes Claude Opus em pacotes `agent-tasks/`.
