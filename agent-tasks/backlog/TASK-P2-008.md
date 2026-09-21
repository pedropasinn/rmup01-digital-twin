# TASK-P2-008 — Escape: baseline suíço e máquina de estados 2D

**Fase:** 9 (preparação) · **Prioridade:** alta · **Bloco de IDs:** `CLM-1350…1399`
**Gate que libera:** G-R8 (→ M4) · **Testes:** V-E01…V-E08

## Objetivo
Construir a simulação 2D paramétrica do escape sem dardo, com o escape de alavanca suíça ao lado como
baseline explícito, e conciliar as três descrições divergentes do banking antes de qualquer 3D.

## Contexto
Não existe uma única fotografia pública do escape do RMUP-01 isolado (Q-IMG-007): a patente carrega sozinha
a topologia. A família CH 832/2019 dá a reivindicação 1 (plateau único no nível da cheville; periferia
cilíndrica como parede anti-renversement com um entalhe; cornas como batente; cada corna só entra no
entalhe com a cheville já na forquilha), a reiv. 2 (desigualdade que evita o travamento em rebat), a
reiv. 3 (perfil da parede externa da corna: porção tangente + porção a 0–45°), as reivs. 4 e 5 (cheville no
plateau **ou** no próprio balanço) e as reivs. 7 e 8 (modos preferidos de arquitetura, não obrigatórios).
Contra isso há três descrições de banking que precisam ser conciliadas: entalhe usinado na platina
(CLM-0412, observação da Hodinkee), goupilles de limitação (reiv. 10 da patente) e "função de banking
levada à forquilha" (press kit).

## Fontes permitidas
`research/patents/EP3754433B1.pdf`, `US11550262.pdf`, `CH716337A1.pdf`;
`research/translations/EP3754433B1-reivindicacoes-pt.md`; `docs/PATENT-TREE.md`;
literatura aberta sobre escape de alavanca suíça; entregas **U03** e **U11** se já integradas.

## Entradas
54° de levantamento, 4 Hz, 3 mg·cm²; candidatos de dentes da roda de escape; restrição de que o pivô da
âncora fica **entre as duas pedras** (CLM-0413).

## Saídas obrigatórias
1. `solvers/kinematics/escape_2d.py` — simulação paramétrica com lock, unlock, impulse, drop, passagem
   segura e rebat, **nos dois casos**: baseline suíço e invenção sem dardo.
2. `engineering/escapement/BASELINE-SUICO.md` — o que é normal, para que o que muda fique visível.
3. `engineering/escapement/CONCILIACAO-BANKING.md` — as três descrições de banking, o que cada uma implica
   geometricamente, e se são compatíveis. Resposta a Q-ESC-004.
4. Conjunto de geometrias candidatas que fecham o ciclo a 4 Hz com 54°, com as duas variantes de cheville
   (reiv. 4 × reiv. 5) carregadas em paralelo.
5. `agent-tasks/review/TASK-P2-008.md`.

## Restrições
- **Nenhuma dimensão sai das figuras da patente.** A figura 5 é um catálogo de formas alternativas: copiar
  a silhueta de qualquer uma delas está proibido.
- Os números que atravessam do texto (0–45° da parede externa, razão ≥ 2 das distâncias de centros,
  alongamento de 360°+β) pertencem **à invenção**, não ao RMUP-01, e têm de ser marcados assim.
- A identificação do escape do RMUP-01 com esta família é classe **D** (H-ESC-010) e continua sendo depois
  deste pacote.
- Não escolher entre reiv. 4 e reiv. 5 por conveniência: a diferença é um nível inteiro de Z (Q-ESC-006).
- 2D antes de 3D, sem exceção (`CLAUDE.md` §8 Fase 9).

## Questões abertas endereçadas
Q-ESC-002, Q-ESC-003, Q-ESC-004, Q-ESC-005, Q-ESC-006, Q-ESC-010, Q-IMG-004.

## Testes
V-E01…V-E08 sobre a simulação. O baseline suíço tem de reproduzir números conhecidos de um escape
documentado — se não reproduzir, o simulador está errado e não o RMUP-01.

## Critério de aceitação
Um ciclo fechado e conferível nas duas topologias, com o conjunto de geometrias compatíveis, e um documento
que diga explicitamente o que o RMUP-01 elimina, o que ele paga por isso (cornas mais largas → entalhe
maior → plateau maior → baguette mais longa) e o que continua desconhecido.

## Arquivos que podem ser alterados
`solvers/kinematics/**`, `engineering/escapement/**`, `research/claims.csv`, `docs/OPEN-QUESTIONS.md`,
`docs/HYPOTHESES.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-008.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/PATENT-TREE.md`, `research/patents/**`,
`engineering/master-parameters.yaml`.
