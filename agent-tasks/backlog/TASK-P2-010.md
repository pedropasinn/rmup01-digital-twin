# TASK-P2-010 — Indicação: coaxialidade, razão 12:1 e a interface ponteiro–roda

**Fase:** 11 (preparação) · **Prioridade:** alta, e é o segundo teste mais barato do projeto
**Bloco de IDs:** `CLM-1450…1499` · **Testes:** V-T06

## Objetivo
Responder por observação direta se os ponteiros de hora e minuto são coaxiais (Q-IND-002), e reunir tudo
que o corpus permite dizer sobre onde está a relação 12:1 e como o ponteiro se prende à roda.

## Contexto
Os ponteiros são decalcados diretamente sobre as rodas, sem canhão — isso é classe A e está confirmado
visualmente em IMG-0030 (ponteiro de perfil sobre a pinça) e IMG-0031 (acoplamento ponteiro–roda). O motion
works clássico não existe. Mas **Q-IND-002 é resolvível por uma única fotografia frontal**: se os dois
ponteiros giram em torno de eixos distintos, a hipótese H-IND-001 se confirma por observação simples
(classe B), e isso restringe imediatamente Q-IND-001 e Q-IND-003. É a pergunta mais barata que o projeto
tem em aberto e ainda não foi feita.

## Fontes permitidas
IMG-0009, IMG-0036 (frontais), IMG-0030, IMG-0031 (macro da indicação), IMG-0012/0013 (quadros do sprite
em que o mostrador aparece de frente), quadros novos do filme na janela 71–88 s (montagem dos ponteiros).

## Entradas
`research/images/catalogo.csv`; `solvers/image_metrology/homografia.py`.

## Saídas obrigatórias
1. Veredito sobre **Q-IND-002**, com o método: posição dos dois eixos, medida ou observada, em pelo menos
   duas imagens independentes.
2. `evidence/measurements/P2-010-indicacao.csv` — centros das rodas porta-ponteiro, diâmetro do assento do
   ponteiro (LMK-IMG0031-001), diâmetro aparente do dentado das horas.
3. Atualização de H-IND-001 e H-IND-101 em `docs/HYPOTHESES.md` com o que a observação fez com cada uma.
4. Resposta ou estreitamento de Q-OSC-003 (três braços: do balanço, da ponte, ou de ambos?) — está no mesmo
   enquadramento frontal e sai de graça.
5. `agent-tasks/review/TASK-P2-010.md`.

## Restrições
- IMG-0009 e IMG-0036 são **render CG oficial**: observação de topologia ali é B fraca e precisa ser
  confirmada em quadro de filmagem real. Um render pode simplificar o mostrador.
- **H-IND-101 (trem de indicação próprio acionado pelo barrilete) não vira fato neste pacote.** É a
  suposição mais sedutora do corpus e a mais fácil de virar verdade por repetição; a instrução explícita é
  tratá-la como classe E em todas as fases.
- Não deduzir a razão 12:1 de diâmetro aparente: diâmetro não é contagem de dentes.

## Questões abertas endereçadas
Q-IND-002 (principal), Q-IND-001, Q-IND-003, Q-IND-005, Q-IND-004, Q-OSC-003.

## Testes
A posição dos dois eixos, medida em duas imagens, concorda dentro da incerteza. Se as duas imagens
discordarem, o resultado é "indeterminado", não a média.

## Critério de aceitação
Q-IND-002 fechada com evidência, ou a demonstração de que nenhuma imagem do corpus a resolve — o que seria
um achado forte por si só, dado que a resposta deveria estar visível a olho nu.

## Arquivos que podem ser alterados
`evidence/**`, `research/claims.csv`, `docs/OPEN-QUESTIONS.md`, `docs/HYPOTHESES.md`,
`docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-010.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`, `engineering/master-parameters.yaml`,
`engineering/bom-reconstructed.csv`.
