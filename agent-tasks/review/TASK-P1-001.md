# Revisão — TASK-P1-001 · Fontes primárias e âncoras

Executado em 2026-09-20/21 (BRT). Bloco de IDs usado: SRC-0001…0012, CLM-0001…0059, EVD-0001…0022.
Sem commit. Sem Codex.

---

## 1. Resultado em uma frase

**As 26 âncoras do `CLAUDE.md` §2 foram todas confirmadas em fonte primária**, com trecho literal e URL conferida —
nenhuma ficou como "não confirmada em fonte primária". Além disso, a pesquisa trouxe seis parâmetros novos de classe A
e três fatos que mudam a arquitetura que vamos modelar.

## 2. O que foi feito

- 12 fontes primárias localizadas, conferidas (`curl -sIL` e/ou WebFetch) e registradas em `research/source-manifest.csv`.
- 59 claims em `research/claims.csv` (57 classe A, 2 classe B; 55 `confirmed`, 2 `provisional`, 2 `contested`).
- 22 linhas em `evidence/evidence-ledger.csv`, uma por parâmetro mestre com valor numérico.
- `engineering/master-parameters.yaml`: os 16 parâmetros existentes saíram de `provisional` para `confirmed` com
  `sources`, `method` e `claims`; 6 parâmetros novos acrescentados.
- `docs/FACTS.md` preenchido (só classe A, formato fato · classe · SRC · trecho literal), organizado por subsistema.
- `docs/OPEN-QUESTIONS.md`: 32 questões abertas.
- `docs/HYPOTHESES.md`: 5 hipóteses no esquema do §5.
- `research/official/`: 8 fontes salvas (HTML + texto extraído), com sha256 no manifesto.
- `research/translations/TASK-P1-001_trechos-nao-ingleses.md`: traduções de apoio do fr/ja/es/zh.
- `docs/RESEARCH-LOG.md`: entrada do dia.

## 3. Fontes registradas

Por tipo: 6 páginas oficiais (5 da Richard Mille + 1 da Ferrari), 2 reproduções íntegras do comunicado oficial,
3 vídeos oficiais, 1 galeria/visualizador 360° oficial.
Por idioma: **en** 5 (SRC-0001, 0006, 0007, 0009/0010/0011 em inglês), **fr** 2, **ja** 1, **es** 1, **zh** 1.

| ID | O que é | Idioma |
|---|---|---|
| SRC-0001…0005 | richardmille.com, página do RM UP-01 Ferrari | en, fr, ja, es, zh |
| SRC-0006 | Comunicado Richard Mille de 05/07/2022, íntegro (ficha técnica + entrevista com Arbona, Boillat e Mathys), reproduzido pela La Cote des Montres | en |
| SRC-0007 | ferrari.com, "Ultra-flat Precision" | en |
| SRC-0008 | Reprodução francesa do mesmo comunicado (my-watchsite.fr) | fr |
| SRC-0009, SRC-0010 | Vídeos oficiais `RMUP-01_SF_EN.mp4` e `caliber.mp4` em media.richardmille.com | en |
| SRC-0011 | "Savoir-faire RM UP-01 Ferrari" no canal oficial @RichardMilleOfficial (autoria confirmada por oEmbed) | en |
| SRC-0012 | Visualizador 360° e as quatro vistas nomeadas na página oficial | en |

**Achado lateral útil ao TASK-P1-004:** os dois vídeos que Pedro deixou em `research/videos/` têm procedência
confirmada — `RMUP-01_SF_EN.mp4` e `caliber.mp4` são exatamente os arquivos servidos pela página oficial do produto
(mesmo nome, host `media.richardmille.com`, HTTP 200, `video/mp4`). Isso resolve o DEC-002 para esses dois arquivos.

## 4. As 26 âncoras do §2, uma a uma

Todas classe **A**. Fontes abreviadas: RM = página oficial (SRC-0001…0005), CP = comunicado (SRC-0006/0008),
FE = ferrari.com (SRC-0007).

| # | Âncora | Situação | Fonte | Observação |
|---|---|---|---|---|
| 1 | 1,75 mm (relógio) | confirmada | RM, CP, FE | |
| 2 | 41,45 × 28,85 mm | confirmada | RM (5 idiomas), CP | qual eixo é qual não é publicado (Q-BASE-001) |
| 3 | 1,18 mm (calibre) | confirmada | RM, CP | |
| 4 | corda manual | confirmada | RM, CP | |
| 5 | horas e minutos | confirmada | RM, CP | sem segundos |
| 6 | seletor W/H | confirmada | RM, CP | na luneta, entre 10h e 11h |
| 7 | ~45 h de reserva | confirmada | RM, CP, FE | **a tolerância ±10% é publicada**: 40,5–49,5 h |
| 8 | 23 rubis | confirmada | RM, CP | distribuição não publicada |
| 9 | balanço Ti Gr5, 3 braços, 6 massas | confirmada | RM, CP | |
| 10 | 3 mg·cm² | confirmada | RM, CP | |
| 11 | 54° de levantamento | confirmada | RM, CP | |
| 12 | 28 800 A/h = 4 Hz | confirmada | RM, CP | |
| 13 | espiral AK 3 | confirmada | RM, CP | |
| 14 | antichoque Kif | confirmada | RM, CP | modelo exato não publicado |
| 15 | barrilete ~1 volta/6 h | confirmada | RM, CP | **é exato, não aproximado**: "6 hours per revolution instead of 7.5 hours" |
| 16 | platina e pontes Ti Gr5 | confirmada | RM, CP | liga 90/6/4 também publicada |
| 17 | escape ultraplano sem dart + safety roller | confirmada | RM (5 idiomas), CP | banking transferido para a forquilha alongada, cornes modificadas |
| 18 | caixa+movimento rígidos juntos, movimento independente | confirmada | RM, CP, FE | as duas metades da frase são literais e explícitas |
| 19 | dois comandos frontais | confirmada | RM, CP | seletor 10h–11h, coroa de execução 7h–8h |
| 20 | cristal das horas 0,45 mm | confirmada, **contestada** | RM, CP | a narrativa do mesmo comunicado diz 2/10 mm para os dois cristais (Q-CRY-001) |
| 21 | cristal do balanço 0,20 centro / 0,30 borda | confirmada | RM, CP | superfície não plana |
| 22 | 13 parafusos spline Ti Gr5 | confirmada | RM, CP | prendem caixa **e** pulseira (Q-FST-001) |
| 23 | 1 atm / 10 m | confirmada | RM, CP | |
| 24 | >6 000 h e dezenas de protótipos | confirmada | RM, CP, FE | o próprio comunicado detalha 3 600+2 400+2 000 = 8 000 h (Q-DOC-001) |
| 25 | tolerância de 1 μm | confirmada | RM (5 idiomas) | é capacidade de processo declarada, não tolerância de peça |
| 26 | involuta central 20°, barrilete + pinhão da 3ª roda | confirmada | RM (5 idiomas), CP | nomenclatura diverge entre idiomas (Q-TRN-001) |

## 5. Parâmetros novos entrando em `master-parameters.yaml`

| Parâmetro | Valor | Classe | Por que importa |
|---|---|---|---|
| `P_CASE_LENGTH` / `P_CASE_WIDTH` | 51,00 / 39,00 mm | A | fecha o envelope externo da Fase 4; não está na página do produto, só no comunicado |
| `P_MOV_MASS` | 2,82 g | A | restrição de massa para auditar o CAD inteiro do movimento (Fases 10 e 13) |
| `P_CASE_MIN_WALL` | 0,18 mm | A | piso de espessura de parede da carrura/fundo, declarado por Julien Boillat |
| `P_BAR_THICKNESS_MAX` | < 1,18 mm | A | limite superior declarado por Arbona (fraco, mas registrado) |
| `P_ACCEL_RESISTANCE` | > 5 000 g | A | piso de resistência verificado por pêndulo de Charpy |

## 6. Três achados que mudam a arquitetura a modelar

1. **Não existe tige de remontoir.** O diâmetro mínimo de 1,5 mm de uma haste de corda não cabia no relógio, então as
   duas coroas foram integradas à caixa **como rodas do próprio calibre** (Boillat: "the crowns designed without winding
   stems, which are neither more nor less than the wheels of the calibre itself"). Toda a Fase 8 tem de ser desenhada a
   partir disso, não a partir de um remontoir clássico.
2. **Os ponteiros são decalcados diretamente sobre as rodas**, sem canhões ("eliminating the hands' barrels to gain in
   thickness"; fr: "aiguilles directement décalquées sur les roues"). O motion works tradicional — canhão de minutos
   empilhado com roda das horas — **não existe**. A Fase 11 precisa explicar onde fica a relação 12:1 (Q-IND-001).
3. **O barrilete também é patenteado** ("Le barillet extraplat breveté", "The patented extra flat barrel"). Há uma
   segunda família de patentes além da do escape — entrada direta para o TASK-P1-002 (Q-BAR-002, H-BAR-001).

Bônus de método: a comparação entre idiomas desfez um erro do release inglês. Na entrevista, Arbona aparece dizendo que
o barrilete tem "an extremely thin **hairspring**"; o original francês diz "un **ressort** extrêmement fin", isto é, a
mola de barrilete. Traduzir de volta do inglês teria colocado uma espiral dentro do barrilete no nosso modelo.

## 7. Contradições dentro das próprias fontes primárias

- **Cristais** (Q-CRY-001): ficha técnica 0,45 / 0,20 / 0,30 mm contra narrativa "os dois cristais a 2/10 mm".
  Adotada a ficha técnica; `P_CRY_HOURS_THICKNESS` fica `contested`; hipótese H-CRY-001 registrada.
- **Horas de desenvolvimento** (Q-DOC-001): ">6 000" contra 3 600+2 400+2 000 = 8 000.
- **"Couronne dynamométrique"** (Q-WND-003): a ficha técnica reproduzida traz um parágrafo em francês falando em evitar
  a quebra da *tige de remontoir* — peça que este relógio explicitamente não tem. Boilerplate de outro modelo; marcado
  para não ser usado como evidência.
- **Nomenclatura do pinhão** (Q-TRN-001): "third-wheel pinion" (en) / "pignon de moyenne" (fr) / 三番車カナ (ja) /
  过轮小齿轮 (zh).

## 8. O que NÃO foi possível e por quê

- **Press kit oficial em PDF e manual de uso/pós-venda** (Q-DOC-002): não existe link público no domínio
  richardmille.com que eu tenha conseguido localizar. O comunicado íntegro só foi obtido por reprodução em veículos de
  imprensa (SRC-0006 e SRC-0008), que conferem entre si e com a página oficial em tudo que se sobrepõe. Onde há
  informação só nessas reproduções (caixa 51×39, massa 2,82 g, entrevistas), a classe continua A por ser texto do
  fabricante, mas o manifesto anota o vetor.
- **Audemars Piguet Le Locle e Giulio Papi** (Q-DOC-003): **nenhuma** declaração pública deles sobre o RM UP-01 ou sobre
  o escape do RMUP-01 foi localizada. Toda a atribuição à AP Le Locle vem do lado Richard Mille. As entrevistas de Papi
  que aparecem em busca (Monochrome, Europa Star, Haute Time, A Timely Perspective, Worldtempus) são sobre outros
  assuntos e anos. O caminho real para o lado AP é a árvore de patentes — TASK-P1-002.
- **Declaração do próprio Richard Mille (a pessoa)** sobre este modelo (Q-DOC-004): não localizada. As citações oficiais
  são de Arbona, Boillat e Mathys.
- **ferrari.com**: responde 403 a requisição `HEAD` por curl (anti-bot); o `GET` com user-agent de navegador devolve 200
  e o corpo do artigo. Registrado no manifesto para ninguém concluir que a página caiu.
- **Preço** (Q-DOC-005): não publicado por nenhuma das duas marcas. A imprensa cita CHF 1 700 000 fora impostos; deixei
  para o TASK-P1-003 registrar com fonte, porque é matéria de imprensa e o bloco de IDs é dele.
- **Vídeos oficiais**: registrados (SRC-0009…0011) mas **não analisados** — extração de quadros e leitura de conteúdo
  são do TASK-P1-004, com o bloco IMG-/VID-.
- **Imagens oficiais**: a página tem visualizador 360° e quatro vistas nomeadas (SRC-0012). Não baixei nada: o catálogo
  de imagens é do TASK-P1-004 e a regra do preâmbulo é não baixar em massa.

## 9. Questões abertas criadas (32)

Contradições: Q-CRY-001, Q-DOC-001, Q-WND-003, Q-TRN-001.
Geometria não publicada: Q-BASE-001/002/003, Q-TRN-002/003, Q-BAR-001/002/003, Q-ESC-001/002, Q-OSC-001/002,
Q-SHK-001, Q-JWL-001, Q-IND-001/002, Q-SEL-001, Q-WND-001/002, Q-CASE-001/002, Q-FST-001, Q-STR-001, Q-CRY-002.
Fontes inalcançadas: Q-DOC-002/003/004/005.

Hipóteses formais: H-CRY-001 (o "2/10" é só o cristal do balanço), H-BASE-001 (41,45 mm é o eixo 3h–9h — praticamente
decidida pela aritmética da caixa, a alternativa é geometricamente impossível), H-WND-001 (cada coroa é uma roda em furo
da carrura), H-IND-001 (trem de indicação distribuído no plano, ponteiros possivelmente não coaxiais — resolúvel com uma
única fotografia frontal), H-BAR-001 (segunda família de patentes, do barrilete).

## 10. Pendente / recomendações ao diretor técnico

1. **TASK-P1-002 ganha um alvo novo:** procurar a família de patentes do **barrilete extraplano**, não só a do escape.
2. **TASK-P1-004 tem uma pergunta barata e de alto valor:** uma vista frontal já decide H-IND-001 (ponteiros coaxiais ou
   não) e H-BASE-001. Vale priorizar.
3. **Q-CRY-001 precisa de decisão do diretor técnico** antes da Fase 3: 0,45 mm ou 0,20 mm no cristal das horas muda o
   Z-budget em 0,25 mm, que é 14% do relógio inteiro.
4. O `Z-budget` já pode começar com números reais: 1,75 mm de relógio, 1,18 mm de movimento, 0,45 + 0,20/0,30 mm de
   cristais, 0,18 mm de parede mínima — sobram, no eixo Z, 1,75 − 1,18 = 0,57 mm para fundo, folgas e cristais somados.
   Com 0,45 mm só do cristal das horas, a conta fica muito apertada: **isso por si só é um argumento a favor de
   H-CRY-001** e merece ser verificado com aritmética explícita na Fase 3.
5. Nada foi comitado, conforme o preâmbulo.

## 11. Nota de governança

O `.gitignore` já mantinha `research/official/*.html` e `*.pdf` fora do repositório (acervo com direitos de terceiros).
As extrações em texto puro que salvei são cópias integrais das mesmas páginas, então acrescentei duas linhas —
`research/official/*.txt` e `research/articles/*.txt` — para que a regra fique coerente. Os arquivos continuam no
disco e no manifesto (com sha256); só não entram no repositório. Os trechos literais citados em `docs/FACTS.md` são
curtos e identificados por fonte, o que é uso legítimo de citação.
