# HYPOTHESES

Esquema do `CLAUDE.md` §5: ID · problema · hipótese · evidências favoráveis · evidências contrárias · alternativas ·
teste discriminante · estado. Abertas pelo TASK-P1-001 a partir de fontes primárias apenas.

---

## H-CRY-001 — o "2/10 mm" se refere só ao cristal do balanço

- **Problema:** o comunicado diz que os dois cristais de safira foram afinados a 2/10 de milímetro, mas a ficha técnica
  do mesmo comunicado e do site atribui 0,45 mm ao cristal das horas e 0,20/0,30 mm ao do balanço.
- **Hipótese:** o texto narrativo generalizou para ambos um número que só vale para o cristal do balanço; a ficha técnica
  está correta.
- **Favoráveis:** 0,20 mm no centro do cristal do balanço é exatamente "2/10"; a ficha técnica é mais específica, tem três
  valores distintos e se repete idêntica em en/fr/ja/es/zh; um cristal de 0,20 mm sobre a indicação horária deixaria muito
  pouca margem estrutural num relógio de 1,75 mm que ainda assim é dado como usável no dia a dia.
- **Contrárias:** o parágrafo narrativo é explícito quanto a "les deux verres saphir"; e a comparação seguinte ("antes
  nossos cristais mais finos eram 8/10") faz mais sentido retórica se aplicada aos dois.
- **Alternativas:** (a) a ficha técnica é que está desatualizada e ambos são 0,20 mm; (b) 0,45 mm é a espessura da peça
  bruta e 0,20 mm a da região central depois da usinagem.
- **Teste discriminante:** metrologia de imagem numa vista de perfil calibrada pela espessura total de 1,75 mm; ou um press
  kit/manual oficial em PDF (Q-DOC-002).
- **Estado:** aberta. `P_CRY_HOURS_THICKNESS` marcado `contested`, valor preferido 0,45 mm.

## H-BASE-001 — o eixo de 41,45 mm é o 3h–9h

- **Problema:** a marca publica 41,45 × 28,85 mm sem dizer qual medida corresponde a qual eixo.
- **Hipótese:** 41,45 mm é o eixo 3h–9h e 28,85 mm o eixo 12h–6h.
- **Favoráveis:** a caixa é 51,00 × 39,00 mm (CLM-0035) e Boillat declara que o tonneau foi **alongado no segmento
  3h–9h** (CLM-0050); 51,00 > 39,00 na mesma proporção qualitativa que 41,45 > 28,85; as folgas resultantes ficam
  parecidas nos dois eixos (9,55 e 10,15 mm), o que é o esperado numa caixa de parede quase uniforme.
- **Contrárias:** nenhuma fonte primária afirma isso literalmente.
- **Alternativas:** a orientação invertida (implicaria folga de 51,00−28,85 = 22,15 mm num eixo e 39,00−41,45 < 0 no
  outro, ou seja, é geometricamente impossível).
- **Teste discriminante:** já é praticamente decidida pela aritmética da caixa; confirmar por metrologia de imagem numa
  vista frontal ortogonalizada.
- **Estado:** fortemente favorecida (classe D). A alternativa é eliminada por contradição geométrica; mantida como
  hipótese formal até haver medida de imagem.

## H-WND-001 — cada coroa é uma roda dentada montada em furo da carrura

- **Problema:** as fontes dizem que as coroas "são as rodas do próprio calibre" e que não há tige de remontoir, mas não
  descrevem o acoplamento nem como se mantém a estanqueidade.
- **Hipótese:** cada comando é um disco/roda com eixo vertical alojado num furo passante da luneta/carrura, engrenando
  radialmente com uma roda do movimento no mesmo plano, com o inserto de cerâmica preta funcionando como pista de atrito
  e assento da vedação.
- **Favoráveis:** ausência de haste (CLM-0036); os insertos de cerâmica "asseguram a estanqueidade" ao redor das coroas
  (CLM-0020); a arquitetura é explicitamente plana, não empilhada (CLM-0032); há ferramenta dedicada para operar os
  comandos (CLM-0051), o que sugere uma peça de perfil muito baixo e de difícil pega.
- **Contrárias:** nenhuma fonte primária descreve o mecanismo; a menção a coroa em 316L com DLC (CLM-0043) sugere uma
  peça de comando distinta da roda do calibre.
- **Alternativas:** (a) a coroa é uma peça de comando separada que aciona uma roda interna por dentado cônico ou por
  atrito; (b) há um eixo curto, de diâmetro muito menor que os 1,5 mm da haste padrão.
- **Teste discriminante:** macrofotografia da luneta na região das coroas e frames dos vídeos oficiais (SRC-0009,
  SRC-0011) mostrando a operação; secção transversal em qualquer material de imprensa técnica.
- **Estado:** aberta (classe E).

## H-IND-001 — a relação 12:1 é obtida por um trem de indicação dedicado, não por motion works empilhado

- **Problema:** os ponteiros são decalcados diretamente sobre rodas (CLM-0037), o que elimina o canhão de minutos e a
  roda das horas empilhados; mas a relação 12:1 entre hora e minuto tem de existir em algum lugar.
- **Hipótese:** existe um trem de indicação distribuído no plano, com hora e minuto em centros **separados**, cada
  ponteiro solidário a uma roda diferente, e a razão 12:1 realizada por engrenagens no mesmo plano em vez de
  coaxialmente.
- **Favoráveis:** a diretriz declarada é distribuir no plano o que não podia ser empilhado (CLM-0032); os canhões dos
  ponteiros foram eliminados por razão de altura (CLM-0037); a eliminação do empilhamento é apresentada como condição
  do projeto ("precluded a traditional movement with superimposed gears and hands").
- **Contrárias:** nenhuma fonte primária descreve a topologia da indicação; ponteiros coaxiais com canhão muito baixo
  continuam possíveis em princípio.
- **Alternativas:** (a) hora e minuto coaxiais, com a roda das horas rebaixada na platina em vez de empilhada;
  (b) indicação por discos em vez de ponteiros (descartável: as fontes falam em *aiguilles*/*hands*).
- **Teste discriminante:** qualquer fotografia frontal com os dois ponteiros visíveis — se os eixos forem distintos, a
  hipótese está confirmada por observação simples (classe B). Fica para o TASK-P1-004.
- **Estado:** aberta (classe E), provavelmente resolúvel de imediato com uma imagem.

## H-BAR-001 — há uma segunda família de patentes, do barrilete

- **Problema:** o `CLAUDE.md` §2 só aponta a patente do escape, mas o comunicado fala em barrilete **patenteado**.
- **Hipótese:** existe uma família de patentes distinta, sobre o barrilete extraplano (e possivelmente sobre seus apoios),
  provavelmente com prioridade próxima a 2019–2021 e cessionário ligado à Audemars Piguet Le Locle ou à Richard Mille.
- **Favoráveis:** SRC-0008, "Le barillet extraplat **breveté**"; SRC-0006, "The patented extra flat barrel".
- **Contrárias:** nenhuma; apenas ainda não procuramos.
- **Alternativas:** o adjetivo "breveté" pode se referir por extensão à mesma família do escape ou a uma patente de
  conjunto do calibre.
- **Teste discriminante:** busca na Espacenet/Google Patents por cessionário e prioridade — trabalho do TASK-P1-002.
- **Estado:** aberta (classe E). Registrada como `Q-BAR-002`.

## H-ESC-010 — o escape do RMUP-01 é uma execução da família CH 832/2019

- **Problema:** a patente prioritária do `CLAUDE.md` §2 não cita Richard Mille nem o calibre RMUP-01.
- **Hipótese:** o escape do RMUP-01 executa o ensinamento de EP3754433B1 / US11550262B2 (âncora sem dardo,
  plateau único com parede anti-renversement entalhada, segurança pelas cornas).
- **Favoráveis:** coincidência ponto a ponto com a descrição pública da marca (dard e plateau de segurança
  eliminados, segurança levada à forquilha alongada com cornas modificadas); inventor Giulio Papi é o diretor
  técnico da Audemars Piguet Le Locle (ex-APRP), parceira declarada do desenvolvimento; prioridade 06/2019,
  compatível com o lançamento em 07/2022.
- **Contrárias:** nenhuma evidência direta; nenhum documento liga os dois.
- **Alternativas:** (a) o RMUP-01 usa uma variante posterior não publicada da mesma família; (b) usa outra
  solução, e a patente de 2019 é apenas do mesmo laboratório.
- **Teste discriminante:** macrofotografia do escape mostrando plateau único com entalhe largo e cornas de
  parede externa em duas porções — TASK-P1-004 e Fase 9.
- **Estado:** aberta, classe D (CLM-0214).

## H-ESC-011 — a cheville é carregada diretamente pelo balanço

- **Problema:** fechar 1,18 mm exige suprimir níveis verticais no oscilador.
- **Hipótese:** o RMUP-01 usa a variante da reivindicação 5 do EP3754433B1, em que o suporte da cheville é o
  próprio balanço, dispensando um plateau independente.
- **Favoráveis:** a patente prevê a variante exatamente para esse fim; a arquitetura do calibre é toda de
  supressão de níveis.
- **Contrárias:** a reivindicação 4 (suporte de uma peça com o plateau) é a variante descrita em detalhe e
  desenhada nas figuras.
- **Alternativas:** plateau independente finíssimo com saliência radial integrada.
- **Teste discriminante:** macro do balanço visto de lado ou desmontado: existe ou não um disco separado abaixo
  dos braços?
- **Estado:** aberta, classe E (CLM-0215).

## H-SEL-010 — o seletor W/H segue a gramática da EP4295198B1

- **Problema:** nenhuma patente do seletor de função do RM UP-01 foi localizada.
- **Hipótese:** o seletor W/H usa a mesma ideia protegida em EP4295198B1 (um único órgão de comando com
  posições angulares estáveis de seleção e segurança por encoche/goupille), adaptada a um comando frontal chato.
- **Favoráveis:** mesmo inventor (Papi), prioridade fev/2021, e as reivindicações 8 e 9 descrevem justamente
  "função de seleção" com duas ou três posições angulares estáveis.
- **Contrárias:** o único modo de realização descrito é de cronógrafo, com coroa de saia e tige, geometria que
  não cabe em 1,75 mm; a patente insiste na translação axial da coroa, que o UP-01 aparentemente não usa.
- **Alternativas:** (a) o seletor é coberto por outra patente ainda não localizada (CH718513A1?); (b) não é
  patenteado e é execução clássica de tirette/came.
- **Teste discriminante:** ler CH718513A1 e refazer a busca por titular na Espacenet; depois, vídeo do
  savoir-faire mostrando a came do seletor.
- **Estado:** aberta, classe E (CLM-0218). Ver Q-SEL-010 e Q-SEL-011.

## Nota sobre H-BAR-001 (barrilete patenteado)

O TASK-P1-002 procurou e **não encontrou** a família do barrilete extraplano nem a do balanço de inércia
variável. As buscas por titular só alcançaram o Google Patents (Espacenet, WIPO Patentscope, Swissreg e Justia
recusaram acesso automatizado) e foram interrompidas por bloqueio do próprio Google. A hipótese continua
aberta e passa a ter as questões Q-BAR-010 e Q-OSC-010 como endereço.

---

# Abertas pelo TASK-P1-003, 2026-09-21 (numeração a partir de -101)

## H-BAR-101 — os "roletes" da Hodinkee e as "buchas" da Chronos são a mesma peça

- **Problema:** o barrilete não tem receptáculo acima nem abaixo (CLM-0401) e é retido pela periferia, mas as duas
  melhores fontes nomeiam o apoio de formas diferentes: roletes (SRC-0400) e quatro buchas de berílio-cobre (SRC-0403).
- **Hipótese:** há **um único** conjunto de quatro apoios periféricos, cilíndricos, em liga de berílio-cobre,
  montados fixos na platina e servindo de superfície de deslizamento para o flanco do tambor. "Rolete" seria
  descrição de forma, não de função rotativa.
- **Favoráveis:** as duas fontes descrevem apoios na periferia da mesma peça, na mesma região; a Hodinkee fotografa
  um apoio isolado e não afirma que ele gira; berílio-cobre é escolha clássica para mancal de deslizamento não
  magnético.
- **Contrárias:** a palavra "roller" sugere rotação; se os apoios girassem sobre pivôs, cada um seria um subconjunto
  e não uma bucha, o que muda contagem de peças, rubis e montagem.
- **Alternativas:** (a) quatro roletes livres sobre eixos fixos; (b) buchas fixas em número diferente de quatro;
  (c) combinação — apoios fixos mais um rolete de pressão.
- **Teste discriminante:** imagem macro do barrilete instalado com os apoios visíveis em torno do tambor; contagem e
  verificação de pivô central em cada apoio. Alternativamente, o vídeo oficial (SRC-0401) em quadro a quadro.
- **Estado:** aberta (classe D). Registrada como Q-BAR-101.

## H-IND-101 — a indicação tem trem próprio acionado pelo barrilete

- **Problema:** a primeira roda do trem de marcha fica à direita e não carrega ponteiro; os ponteiros estão à
  esquerda/centro, decalcados sobre rodas (CLM-0419). Como a energia chega à indicação?
- **Hipótese:** existe um trem de indicação separado, à esquerda, **acionado pela rotação do próprio barrilete** e
  fora do fluxo de potência do trem de marcha, como proposto por Jack Forster (CLM-0421). Como a velocidade do
  barrilete é regulada pelo trem de marcha, a indicação fica correta mesmo sem estar no caminho do escape.
- **Favoráveis:** é a leitura de um observador competente sobre as fotos de montagem; é geometricamente coerente
  com o barrilete de 6 h/volta (relação inteira simples até 1 volta/h é plausível); explica por que o seletor em H
  precisa desacoplar o barrilete para acertar as horas sem torcer a mola (CLM-0422).
- **Contrárias:** nenhuma fonte primária confirma; o próprio autor marca como suposição.
- **Alternativas:** (a) a indicação sai de uma roda do trem de marcha por um caminho longo que atravessa o
  movimento por baixo do barrilete; (b) há uma roda intermediária dedicada saindo da segunda roda —
  compatível com a roda intermediária de CLM-0406, que pode servir aos dois propósitos.
- **Teste discriminante:** foto de montagem em que se veja o que engrena com a roda do ponteiro dos minutos; ou
  consistência de razões: se o barrilete gira 1 volta/6 h, o caminho até 1 volta/h exige razão 6:1 exata, o que o
  solver do trem pode testar contra os diâmetros observados.
- **Estado:** aberta (classe E). Registrada como Q-IND-101. **Não usar como fato em nenhuma fase.**

## H-CASE-101 — o cristal das horas é elemento estrutural da caixa

- **Problema:** por que manter 0,45 mm de safira, quase um quarto da altura total do relógio, quando a própria
  janela do balanço desce a 0,20 mm?
- **Hipótese:** o cristal das horas participa da rigidez da caixa (SRC-0404) e, junto com o apoio do eixo da
  indicação contra ele (CLM-0420), forma um conjunto pré-carregado caixa-cristal-movimento.
- **Favoráveis:** Hirota afirma as duas coisas depois de manusear o relógio; explica a assimetria entre os dois
  cristais; é coerente com a caixa resistir a ~12 kg na periferia (CLM-0433).
- **Contrárias:** nenhuma fonte ocidental menciona; pode ser interpretação do jornalista e não declaração técnica.
- **Alternativas:** os 0,45 mm existem só por resistência do próprio cristal a impacto, sem função estrutural na caixa.
- **Teste discriminante:** declaração primária da RM; ou, no modelo, comparar a rigidez da caixa com e sem o cristal
  colado — se a diferença for grande, a hipótese ganha plausibilidade, sem virar fato.
- **Estado:** aberta (classe E). Registrada como Q-CASE-105.
