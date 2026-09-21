# Changelog

## 0.1.0 — 2026-09-21 · Fase 1 fechada

Primeira entrega para revisão humana: **pesquisa e planejamento**, não um relógio. Fecha a Fase 1
(corpus de pesquisa) e a Fase 2 documental (decomposição funcional), e deixa a Fase 3 especificada.

### Corpus (pacotes TASK-P1-001…004)
- **50 fontes** registradas em `research/source-manifest.csv`: 12 primárias (página oficial em cinco
  idiomas, comunicado de 05/07/2022 na íntegra, ferrari.com, três vídeos oficiais, visualizador 360°),
  11 de patente, 22 de imprensa técnica em sete idiomas, 16 de imagem.
- **As 26 âncoras do `CLAUDE.md` §2 confirmadas em fonte primária**, uma a uma, com trecho literal.
- **7 PDFs de patente** arquivados; família do escape sem dardo fechada (CH 832/2019 → EP3754433B1
  concedida em 27/05/2026, US11550262B2, CH716337A1, HK40033669A, JP7537920B2, CN112114508B), lida
  integralmente e resumida em `docs/PATENT-TREE.md`.
- **US D991,795 S / Haia DM/218823** localizado: o registro de desenho do próprio RM UP-01, com seis
  vistas ortogonais — a melhor fonte ortográfica pública do projeto.
- **36 imagens catalogadas** com `natureza` declarada, 26 candidatos a landmark, 17 quadros-chave de vídeo
  escolhidos por nitidez, e o sprite 360° decodificado (81 quadros de 800 × 800, passo de 4,44°, duas
  iluminações).
- **~130 claims** classificados A–F com fonte; 22 linhas no `evidence-ledger.csv`.

### Achados que mudam o objeto a modelar
- **Não existe tige de remontoir:** as duas coroas são rodas do próprio calibre integradas à caixa.
- **Os ponteiros são decalcados sobre as rodas, sem canhão:** não há motion works clássico.
- **O barrilete é periférico e patenteado:** sem receptáculo acima nem abaixo, retido por quatro apoios.
- **Existe uma roda intermediária** entre barrilete e segunda roda.
- **O banking do escape é sólido, contra entalhe na platina**, com o pivô da âncora entre as duas pedras.
- **12 dos 19 arquivos de entrada eram render de terceiro** (marca d'água Hum3D) e foram descartados; boa
  parte do material oficial também é CG, e medida tirada de render oficial passa a nascer classe E
  (DEC-003).

### Síntese (este release)
- `docs/OPEN-QUESTIONS.md` consolidado: 87 → **81 questões**, deduplicadas, renumeradas em sequência única
  por subsistema, com prioridade por marco, teste discriminante, melhor fonte candidata e tabela de
  equivalência completa (DEC-004).
- `docs/ARCHITECTURE.md` **novo**: decomposição funcional nó a nó, com o que a Fase 1 mudou.
- `engineering/bom-reconstructed.csv`: 0 → **60 peças** com `part_id` permanente, visibilidade, classe e
  status — inclusive três peças registradas como inexistentes.
- `engineering/interfaces.csv`: 0 → **52 interfaces**, 22 ainda hipotéticas e marcadas como tal.
- `docs/MASTER-RESEARCH-PLAN.md`, `docs/CAD-RECONSTRUCTION-PLAN.md`, `docs/VALIDATION-PLAN.md` **novos**.
- `engineering/master-parameters.yaml`: +7 parâmetros — quatro deduções classe D (7,5 voltas úteis,
  14 400 dentes/h, folgas totais de 9,55 e 10,15 mm) e **três placeholders declarados** do sistema de
  coordenadas, para que o CAD não os invente em silêncio.
- `agent-tasks/backlog/`: **12 pacotes TASK-P2-001…012**.
- **DEC-004** (renumeração) e **DEC-005** (Z-budget por coluna; as duas hipóteses de cristal convivem).

### Decisões que aguardam Pedro
Cristal de 0,45 × 0,20 mm · imagens oficiais dentro ou fora do repositório · margem do Z-budget.
Resumo executivo em `agent-tasks/review/SINTESE-FASE-1.md`.

## 0.0.1 — 2026-09-20
Fase 0: estrutura, charter, esquemas, convenções, backlog.
