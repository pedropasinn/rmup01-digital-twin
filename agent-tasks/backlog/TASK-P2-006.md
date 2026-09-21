# TASK-P2-006 — `gear_search` v0: o espaço de soluções do trem

**Fase:** 7 · **Prioridade:** alta, depois de TASK-P2-005 · **Bloco de IDs:** `CLM-1250…1299`
**Gate que libera:** G-R7 (→ M3) · **Testes:** V-T01…V-T06

## Objetivo
Construir o solver combinatório que devolve **todos** os conjuntos de dentes compatíveis com os centros
medidos, com a razão total exigida e com os módulos plausíveis — e nenhum deles escolhido por aparência.

## Contexto
Nenhum número de dentes é publicado em nenhum idioma. A aritmética disponível é: barrilete a 1 volta/6 h;
28 800 A/h ÷ 2 = 14 400 dentes/h na roda de escape, logo razão total de **5 760** (15 dentes), **4 800**
(18) ou **4 320** (20); 7,5 voltas úteis de mola; minuto a 1 volta/h; hora a 1 volta/12 h. Há uma roda
intermediária de transmissão observada entre barrilete e segunda roda (CLM-0406), com razão conjecturada
1:1 — que, aritmeticamente, se comporta como *idler* e é **consistente** com a razão total, já que um trem
suíço clássico faz ~4 500 em quatro engrenamentos (média 8,2 por estágio).

## Fontes permitidas
`evidence/measurements/P2-005-centros.csv`; `engineering/master-parameters.yaml`; contagens parciais de
TASK-P2-007; a entrega **U13** do Balcão, se já integrada (como material de terceiro, reavaliado por nós).

## Entradas
Centros medidos com incerteza; diâmetros observados; faixa de módulos plausível para um calibre de 1,18 mm;
candidatos de dentes da roda de escape (15, 18, 20, 21, 24); topologias admitidas (intermediária como idler
**e** como estágio de multiplicação); sentidos de rotação.

## Saídas obrigatórias
1. `solvers/gear_search/gear_search.py` — busca combinatória com função objetivo e restrições explícitas.
2. `engineering/geartrain/candidatos.csv` — **todos** os candidatos, com dentes por estágio, módulo,
   distância entre centros teórica, resíduo contra os centros medidos e razão total resultante.
3. `engineering/geartrain/RESTRICOES.md` — a aritmética acima, escrita, com as contas refeitas.
4. Cadeia de indicação resolvida no mesmo solver: 6:1 do barrilete ao minuto (se H-IND-101), 12:1 entre as
   duas rodas porta-ponteiro.
5. `agent-tasks/review/TASK-P2-006.md`.

## Restrições
- **Nunca escolher números de dentes porque "parecem bons"** (`CLAUDE.md` §7). O solver devolve conjunto;
  a eliminação é por evidência ou por resíduo, e fica registrada.
- Manter os candidatos vizinhos vivos: se o segundo melhor estiver dentro da incerteza dos centros, os dois
  sobrevivem como `contested`.
- Não tratar H-IND-101 (trem de indicação acionado pelo barrilete) como fato: rodar as duas topologias.
- Não usar solver como caixa-preta: guardar função objetivo, restrições, candidatos e resíduos (§10).

## Questões abertas endereçadas
Q-TRN-002, Q-TRN-003, Q-TRN-004, Q-TRN-001, Q-ESC-001, Q-IND-001, Q-IND-003, Q-BAR-001.

## Testes
V-T01 (razão total), V-T02 (voltas úteis), V-T04 (distância entre centros), V-T06 (indicação). O solver é
validado contra um trem suíço clássico conhecido: alimentado com os dados de um calibre documentado, tem de
recuperar os dentes reais.

## Critério de aceitação
Um conjunto de candidatos com resíduos, e a demonstração de que nenhum candidato foi eliminado sem motivo
registrado. Se o espaço de soluções for grande, isso é o resultado — não um defeito a esconder.

## Arquivos que podem ser alterados
`solvers/gear_search/**`, `engineering/geartrain/**`, `research/claims.csv`, `docs/OPEN-QUESTIONS.md`,
`docs/HYPOTHESES.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-006.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`, `evidence/measurements/**` (este pacote consome
medidas, não as produz), `engineering/master-parameters.yaml`.
