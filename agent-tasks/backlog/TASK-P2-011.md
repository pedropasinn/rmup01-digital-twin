# TASK-P2-011 — Reabertura da varredura de patentes (depende de acesso humano)

**Fase:** 1 residual · **Prioridade:** alta, mas fora do nosso controle · **Bloco de IDs:** `SRC-0900…0999`, `CLM-1500…1549`
**Gate que libera:** G-R6

## Objetivo
Fechar o maior buraco de pesquisa que a Fase 1 deixou: a varredura por titular e por CPC que as bases
recusaram ao acesso automatizado. Três famílias ditas patenteadas continuam sem número.

## Contexto
No TASK-P1-002, **Espacenet, WIPO Patentscope, Swissreg e Justia recusaram acesso automatizado** (403,
Cloudflare em alguns casos) e o **Google Patents passou a responder 503** depois de cerca de uma dezena de
consultas, interrompendo a varredura pela metade. Nada foi contornado e nada será. Os fascículos europeus
foram salvos pelo servidor de publicação oficial do EPO, que atende bem — foi por ele que apareceu a
concessão EP3754433B1, invisível nas fontes anteriores.

## Fontes permitidas
Espacenet (interface humana ou OPS com chave), WIPO Patentscope, Swissreg, Hague Express (OMPI),
J-PlatPat, CNIPA, `data.epo.org/publication-server`. **Nada de contorno de anti-robô.**

## Entradas
- Titulares: Manufacture d'Horlogerie Audemars Piguet SA; Turlen Holding SA; Richard Mille SA.
- Inventores: Giulio Papi; José-Manuel Fernandez.
- CPC: **G04B1/10–1/22** (barrilete) · **G04B17/06**, **G04B18/\*** (balanço, espiral) · **G04B3/\***,
  **G04B27/\*** (corda, seletor) · **G04B15/\*** (escape).
- Prioridades 2018–2022.
- Documentos nomeados a abrir: **CH718513A1** (nunca aberto), **USD1088933S1** e **USD1102294S1**
  ("Watch movement", Turlen Holding), registro de Haia **DM/218823**, irmãos de 28/10/2021
  (TWD222805S/06S/07S, CA208187S, CA210542S, ZAA202200456S), eventual **CH716337B1**,
  **JP7537920B2** e **CN112114508B** em base nacional.

## Saídas obrigatórias
1. Linhas novas em `research/source-manifest.csv` e `research/patents/patents.csv`, com `sha256` de cada
   PDF salvo.
2. Atualização de `docs/PATENT-TREE.md`: famílias novas, ou a declaração explícita de que a varredura
   completa foi feita e **não** localizou as famílias do barrilete, do balanço e do seletor — o que é uma
   afirmação muito mais forte do que a atual.
3. Vereditos em Q-BAR-004, Q-OSC-005, Q-SEL-004, Q-SEL-005, Q-ESC-007, Q-ESC-008, Q-CASE-008, Q-CASE-009,
   Q-CASE-010, Q-PAT-001.
4. `agent-tasks/review/TASK-P2-011.md`.

## Restrições
- **Desenho de patente e desenho de registro não são desenhos em escala.** Nenhuma dimensão sai deles.
- Documento não lido não vira fonte: fica como pista, com confiabilidade baixa e uso proibido (foi o que se
  fez com CH718513A1).
- Se USD1088933S1 ou USD1102294S1 for o RMUP-01, **isso é o achado do pacote**: seriam as primeiras vistas
  ortogonais da platina — e ainda assim não seriam escala.

## Questões abertas endereçadas
Q-PAT-001, Q-BAR-004, Q-OSC-005, Q-SEL-004, Q-SEL-005, Q-ESC-007, Q-ESC-008, Q-CASE-008, Q-CASE-009,
Q-CASE-010.

## Testes
Cada URL conferida com `curl -sIL --max-time 20`; `sha256` de cada arquivo local; cada família com
prioridade, titular, inventor e situação legal conferidos no próprio documento, nunca supostos.

## Critério de aceitação
Ou as famílias aparecem, ou a frase "não existe patente localizada sobre X" passa a ser sustentada por uma
varredura descrita e reproduzível — deixando de ser afirmação sobre a nossa busca.

## Arquivos que podem ser alterados
`research/patents/**`, `research/source-manifest.csv`, `research/claims.csv`, `research/translations/**`,
`docs/PATENT-TREE.md`, `docs/OPEN-QUESTIONS.md`, `docs/HYPOTHESES.md`, `docs/RESEARCH-LOG.md`,
`evidence/evidence-ledger.csv`, `agent-tasks/review/TASK-P2-011.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`, `engineering/**`.
