# Diário de pesquisa

- 2026-09-20 23:50 BRT — Repositório criado a partir de `CLAUDE.md` (brief de Pedro). Fase 0: charter, esquemas (fontes, claims, evidência, parâmetros, Z-budget, BOM, interfaces), convenções de IDs, backlog. Entradas de Pedro (19 imagens, 2 vídeos, avaliação inicial do ChatGPT) guardadas em `research/` e `inputs/` com procedência a confirmar (DEC-002). Fase 1 lançada em quatro pacotes: fontes primárias e âncoras, patentes, imprensa técnica e desmontagens, catálogo de imagens e vídeo.

- 2026-09-21 00:40 BRT — **TASK-P1-001 (fontes primárias e âncoras) concluído.** Localizadas e conferidas 12 fontes
  primárias: a página oficial do produto em cinco idiomas (en/fr/ja/es/zh), o comunicado de imprensa Richard Mille de
  05/07/2022 reproduzido na íntegra (ficha técnica + entrevista com Salvador Arbona, Julien Boillat e Yves Mathys),
  a reprodução francesa do mesmo comunicado, o artigo "Ultra-flat Precision" da ferrari.com, os dois vídeos oficiais
  servidos por media.richardmille.com e o vídeo de savoir-faire no canal oficial da marca no YouTube.
  **As 26 âncoras do `CLAUDE.md` §2 foram todas confirmadas em fonte primária** — nenhuma ficou como "não confirmada".
  Seis parâmetros novos entraram no `master-parameters.yaml`: caixa 51,00 × 39,00 mm, massa do movimento 2,82 g,
  parede mínima da caixa 0,18 mm, teto de espessura do barrilete, resistência a 5 000 g.
  Três descobertas mudam a arquitetura que vamos modelar: (1) **não existe tige de remontoir** — as duas coroas são
  rodas do próprio calibre integradas à caixa, porque o diâmetro mínimo de 1,5 mm da haste não cabia; (2) **os ponteiros
  são decalcados diretamente sobre as rodas**, sem canhões, o que elimina o motion works clássico; (3) **o barrilete
  também é patenteado**, ou seja, há uma segunda família de patentes a procurar além da do escape.
  Duas contradições dentro das próprias fontes primárias ficaram registradas: a espessura do cristal das horas
  (0,45 mm na ficha técnica contra "2/10 mm" na narrativa) e as horas de desenvolvimento (>6 000 contra 8 000).
  Não foi localizado press kit em PDF, manual de uso público, nem qualquer declaração da Audemars Piguet Le Locle ou de
  Giulio Papi sobre este relógio. Ficaram 32 questões abertas e 5 hipóteses formais.
- 2026-09-21 01:20 BRT — TASK-P1-002 (árvore de patentes). Família do escape sem dardo fechada e arquivada:
  CH716337A1 (prioridade CH 832/2019, 19/06/2019), EP3754433A1, **EP3754433B1 concedida em 27/05/2026**,
  US11550262B2, HK40033669A, mais JP7537920B2 e CN112114508B por listagem de família. Texto integral lido:
  topologia, ciclo 3a-3n, condição anti-rebat, relações de arquitetura das reivindicações 7 e 8. Achados
  laterais: EP4295198B1 (órgão único de comando com posições angulares de seleção, Papi + Fernandez,
  prioridade 16/02/2021) e, sobretudo, **US D991,795 S / Haia DM/218823** — o registro de desenho do próprio
  RM UP-01, com seis vistas ortogonais, depositado pela Turlen Holding SA (Richard Mille) em 28/10/2021.
  Não localizadas: as patentes do barrilete extraplano e do balanço de inércia variável (Q-BAR-010, Q-OSC-010).
  Espacenet, WIPO Patentscope, Swissreg e Justia recusaram acesso automatizado (403) e o Google Patents passou
  a responder 503 no meio do trabalho; os PDFs do EPO vieram do servidor de publicação oficial.

## 2026-09-20/21 — TASK-P1-003 · imprensa técnica, hands-on e desmontagens

Varredura da imprensa relojoeira em sete idiomas (en, ja, fr, de, it, es, pt, zh) atrás de material de
**primeira mão**: hands-on, macrofotografia, movimento fora da caixa, passos de montagem e operação dos seletores.
22 fontes registradas (SRC-0400…0421), 40 claims (CLM-0400…0439), índice em `research/articles/INDICE.md`.

O achado que organiza o pacote: **não existe desmontagem pública do RM UP-01 feita por terceiro**. Todo o material
de "movimento fora da caixa" que circula na imprensa vem de fotografias e do vídeo de savoir-faire produzidos pela
própria Richard Mille. Não há nenhuma imagem pública do **verso** do movimento. Isso põe um teto na classe de
evidência de tudo que fica do lado oculto e será a restrição dominante das Fases 5 a 7.

Três fontes carregam quase todo o conteúdo técnico independente: a análise de Jack Forster na Hodinkee (topologia:
escape side-lever com banking contra entalhe na platina, braço deslizante do seletor, rebaixo interno da caixa,
parafuso central travando caixa e movimento) e as duas matérias da Chronos Japan (construção: barrilete sem
receptáculo acima nem abaixo, retido por quatro buchas de berílio-cobre na periferia; roda intermediária entre
barrilete e segunda roda; coroas de aço com aro de cerâmica fazendo a vedação; caixa em estrutura caixa+tampa que
suporta ~12 kg na periferia; eixo da indicação apoiado contra o cristal). Espanhol e português não produziram
uma única matéria com conteúdo próprio; o material técnico independente está em inglês e, sobretudo, em japonês.

Divergências registradas em vez de resolvidas: roletes × quatro buchas no barrilete (H-BAR-101); ponte de três
braços × balanço de três braços (Q-OSC-101); 13 × 12 parafusos (Q-CASE-103); 28,5 g × ~30 g (Q-CASE-104).
Uma matéria chinesa (SRC-0414) afirma que a platina serve de tampa da caixa — erro, contradito por RM, Hodinkee e
Chronos, anotado no manifesto para não voltar a circular.

Paywall/bloqueio: Quill & Pad (duas matérias) e Forbes devolveram HTTP 403 ao acesso automatizado. Registradas no
manifesto com o direito explicitado, **sem leitura e sem contorno**, e sem gerar claim (Q-DOC-102).
