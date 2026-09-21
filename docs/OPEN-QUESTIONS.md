# OPEN-QUESTIONS

Toda lacuna importante fica visível aqui. Abertas pelo TASK-P1-001 (fontes primárias e âncoras) em 2026-09-20/21.
As questões abaixo são o que a Richard Mille, a Ferrari e a Audemars Piguet Le Locle **não publicam** —
ou publicam de forma contraditória. Ausência de resposta não vira certeza em lugar nenhum do repositório.

## Contradições dentro das próprias fontes primárias

- **Q-CRY-001** — Espessura do cristal das horas: a ficha técnica (cinco idiomas, SRC-0001..0005) diz 0,45 mm, mas a
  narrativa do mesmo comunicado (SRC-0006, SRC-0008) diz que **os dois** cristais foram afinados a 2/10 de milímetro
  ("affinés à une épaisseur de 2/10e"). Adotamos 0,45 mm por ser o dado mais específico e mais repetido; `P_CRY_HOURS_THICKNESS`
  fica `contested`. Teste discriminante: metrologia de imagem no perfil da caixa, ou um press kit/manual oficial em PDF.
- **Q-DOC-001** — Horas de desenvolvimento: "mais de 6 000 h" na comunicação geral contra 3 600 + 2 400 + 2 000 = 8 000 h
  no detalhamento do mesmo comunicado. Sem consequência para o CAD; registrado para não citarmos números incompatíveis.
- **Q-WND-003** — A ficha técnica reproduzida em SRC-0006 traz um bloco em francês, "Couronne dynamométrique", que fala em
  evitar "le bris de la tige de remontoir" — peça que este relógio explicitamente **não tem** (CLM-0036). Quase certamente
  boilerplate herdado de outro modelo Richard Mille. Não usar como evidência de nada até confirmação.
- **Q-TRN-001** — Nomenclatura da roda cujo pinhão tem involuta de 20°: en "third-wheel pinion", fr "pignon de moyenne",
  ja 三番車カナ (terceira roda), zh 过轮小齿轮 (roda intermediária). Em nomenclatura suíça "moyenne" costuma ser a terceira roda,
  mas a arquitetura aqui não é a clássica. Qual roda real recebe o perfil declarado é uma questão aberta.

## Geometria e arquitetura não publicadas

- **Q-BASE-001** — Qual eixo do relógio corresponde aos 41,45 mm do calibre? A marca publica as duas medidas, mas não a
  orientação. A hipótese natural (41,45 no eixo 3h–9h, alinhado com o tonneau alongado) precisa de verificação por imagem.
- **Q-BASE-002** — Posição do movimento dentro da caixa: sobram 9,55 mm no comprimento e 10,15 mm na largura. A repartição
  dessa folga entre os dois lados (e portanto a origem do sistema de coordenadas) não é publicada.
- **Q-BASE-003** — Espessura da platina, das pontes e de cada camada do empilhamento vertical. Nada disso é publicado:
  só o total de 1,18 mm. É o problema central da Fase 3.
- **Q-TRN-002** — Número de dentes, módulos, diâmetros e distâncias entre centros de **todas** as rodas e pinhões. Nenhum
  número de dentes é publicado em nenhum idioma.
- **Q-TRN-003** — Quantos estágios tem o trem de marcha, e se a indicação de horas/minutos vem de um trem separado.
  Nenhuma fonte primária descreve a topologia do trem.
- **Q-BAR-001** — Geometria do barrilete: diâmetro, número de dentes, espessura real (só sabemos "< 1,18 mm"), dimensões
  da mola, espessura da lâmina, comprimento, momento de torque, curva de torque. Nada publicado.
- **Q-BAR-002** — A comunicação menciona um **barrilete patenteado** (SRC-0008: "barillet extraplat breveté"), distinto da
  patente do escape. Essa segunda família de patentes precisa ser localizada — insumo direto para o TASK-P1-002.
- **Q-BAR-003** — As fotos de imprensa sugerem apoios periféricos (rolos) no barrilete, mas **nenhuma fonte primária**
  menciona isso. Não tratar como fato antes do TASK-P1-003/004.
- **Q-ESC-001** — Número de dentes da roda de escape, geometria dos pallets, ângulos de locking/draw, drop e clearance.
  Não publicados. Só a topologia (ausência de dard e de plateau) é primária.
- **Q-ESC-002** — Qual é exatamente a "parede anti-overbanking" que substitui o plateau: as fontes primárias dizem apenas
  que a função foi transferida para a forquilha alongada e as cornes modificadas, sem descrever a superfície de contato.
- **Q-OSC-001** — Diâmetro do balanço, seção dos braços, massa do balanço, geometria e massa das 6 massas de regulagem.
  Só o momento de inércia total (3 mg·cm²) é publicado — uma equação com muitas incógnitas.
- **Q-OSC-002** — Geometria da espiral AK 3: número de voltas, seção, diâmetro externo, curva terminal, ponto de fixação.
  "AK 3" identifica o produto, não a geometria.
- **Q-SHK-001** — Qual modelo/calibre de para-choque Kif é usado, e se protege só o balanço ou também o escape.
- **Q-JWL-001** — Distribuição dos 23 rubis por mancal. Só a contagem é publicada.
- **Q-IND-001** — Como se obtém a relação 12:1 entre hora e minuto se os ponteiros são decalcados diretamente sobre rodas
  do trem (CLM-0037): a cinemática do conjunto de indicação não é descrita em nenhuma fonte primária.
- **Q-IND-002** — Os dois ponteiros são coaxiais? A comunicação não diz, e a arquitetura "espalhada no plano" permite que
  não sejam.
- **Q-SEL-001** — Mecanismo interno do seletor W/H: came, excêntrico, embreagem deslizante, mola de posicionamento.
  Nenhuma fonte primária descreve as peças; só o efeito.
- **Q-WND-001** — Como a coroa-roda engrena no calibre atravessando a caixa e mantendo 1 atm de estanqueidade:
  geometria do acoplamento, vedação, diâmetro e número de dentes das coroas.
- **Q-WND-002** — A ficha técnica lista "Crown: In DLC treated 316L stainless steel" (SRC-0006), mas as coroas são
  descritas como rodas do calibre em titânio/aço. A qual peça exatamente se refere o DLC?
- **Q-CASE-001** — Perfil de espessura da caixa ao longo do contorno: sabemos que há pontos com 0,18 mm, não onde.
- **Q-CASE-002** — Geometria dos 13 parafusos spline (diâmetro, passo, tipo de spline) e quantos são de caixa e
  quantos são da interface da pulseira (ver Q-FST-001).
- **Q-FST-001** — Repartição dos 13 parafusos entre caixa e pulseira, conforme a declaração de Boillat (CLM-0053).
- **Q-STR-001** — Nenhuma fonte primária localizada descreve a interface da pulseira nem o material do bracelete.
- **Q-CRY-002** — Os cristais são circulares? O comunicado fala em "diâmetro calculado", o que sugere que sim, mas
  não há desenho técnico público.

## Fontes que não conseguimos alcançar

- **Q-DOC-002** — Não foi localizado um **press kit oficial em PDF** nem um manual de uso/pós-venda público do RM UP-01
  no domínio richardmille.com. O comunicado íntegro só foi obtido por reprodução em veículos de imprensa (SRC-0006, SRC-0008).
- **Q-DOC-003** — Não foi localizada **nenhuma** declaração pública da Audemars Piguet Le Locle, nem entrevista de
  Giulio Papi, tratando especificamente do RM UP-01 ou do escape do RMUP-01. Toda a atribuição à AP Le Locle vem do lado
  Richard Mille. Reabrir com a árvore de patentes (TASK-P1-002).
- **Q-DOC-004** — Nenhuma declaração pública do próprio Richard Mille (a pessoa) sobre este modelo foi localizada nas
  fontes primárias; as citações oficiais são de Salvador Arbona, Julien Boillat e Yves Mathys.
- **Q-DOC-005** — Preço: não publicado por Richard Mille nem pela Ferrari. A imprensa cita CHF 1 700 000 (fora impostos);
  registro e verificação ficam com o TASK-P1-003.

## TASK-P1-002 — árvore de patentes (21/09/2026)

Numeração a partir de 010 em cada subsistema para não colidir com os pacotes que corriam em paralelo.

### Respostas parciais que este pacote traz a questões já abertas
- **Q-ESC-002** (qual é a parede anti-overbanking): a patente da família responde pela *invenção* — a parede é a
  **periferia cilíndrica do plateau**, com um entalhe junto à cheville, e quem encosta nela é a **parede externa
  das cornas**, com uma primeira porção tangente (CLM-0202, CLM-0206). Falta confirmar que o RMUP-01 executa
  essa mesma solução (CLM-0214 é classe D).
- **Q-BAR-002** (localizar a patente do barrilete): **não localizada** neste pacote. Vira Q-BAR-010.
- **Q-CASE-001/002** (perfil de espessura, parafusos): as vistas ortogonais do US D991,795 S (SRC-0210) ajudam na
  *proporção*, mas não medem nada — desenho de registro não é desenho em escala.

### Questões novas
- **Q-ESC-010** — O RMUP-01 respeita os modos preferidos das reivindicações 7 e 8 do EP3754433B1 (distância
  âncora–plateau ≥ 2 × distância âncora–roda de escape; três centros coplanares)? A patente permite explicitamente
  não respeitar. Discriminante: metrologia dos três centros em foto macro calibrada.
- **Q-ESC-011** — A cheville do RMUP-01 é carregada por um suporte de uma peça com o plateau ou diretamente pelo
  balanço (reiv. 4 × reiv. 5)? Muda um nível inteiro do orçamento vertical do oscilador.
- **Q-ESC-012** — O RMUP-01 tem goupilles de limitação (banking pins) separadas, como prevê a reiv. 10, ou o
  banking foi integrado de outra forma? A comunicação da marca fala em "função de banking levada à forquilha",
  o que a patente não diz. Divergência de vocabulário ou de execução?
- **Q-ESC-013** — Quantos dentes tem a roda de escape do RMUP-01? A patente não desenha a roda nas figuras do
  ciclo e não dá número algum.
- **Q-ESC-014** — Existe um pedido de patente posterior, específico do escape ultraplano *do RMUP-01* (por exemplo
  com prioridade 2020–2022), distinto da família de 2019? Não foi encontrado, mas a busca por titular ficou
  incompleta pelo bloqueio das bases.
- **Q-ESC-015** — Situação legal dos membros JP7537920B2 e CN112114508B, e existência de uma patente suíça
  concedida (CH716337B1) — nada disso foi conferido em base nacional.
- **Q-SEL-010** — Qual patente, se alguma, cobre o seletor de função W/H do RM UP-01? A EP4295198B1 é parente
  conceitual, não prova (CLM-0218).
- **Q-SEL-011** — CH718513A1 ("Device for selecting and actuating several functions of a watch movement") é da
  mesma família da EP4295198B1, é um segundo depósito suíço distinto, ou é de outro titular? Documento não lido.
- **Q-BAR-010** — Patente do barrilete extraplano: nenhum número localizado. Hipóteses: depósito suíço ainda mal
  indexado nas bases acessíveis, titularidade fora de Audemars Piguet/Turlen, ou uso comercial amplo da palavra
  "patenteado". Refazer a busca por CPC G04B1/10–1/22 com acesso à Espacenet.
- **Q-OSC-010** — Patente do balanço de inércia variável ultraplano: idem, nenhum número localizado. Buscar por
  CPC G04B17/06 e G04B18/00 com prioridade 2019–2022.
- **Q-CASE-010** — Ler o registro internacional de Haia **DM/218823** na base Hague Express da OMPI para elevar a
  identificação do desenho do UP-01 de B (observada) para A (primária) e obter a lista completa de países.
- **Q-CASE-011** — Quais dos registros irmãos depositados em 28/10/2021 pela Turlen Holding (TWD222805S,
  TWD222806S, TWD222807S, CA208187S, CA210542S, ZAA202200456S) correspondem ao UP-01? Pelo menos um depósito
  da mesma data (USD989636S1) é de outro modelo, então a data não basta.
- **Q-CASE-012** — Existe registro de desenho específico do **movimento** RMUP-01 (as categorias "Watch movement"
  da Turlen Holding de 2022–2023: USD1015914S1 já foi aberto e não é; faltam USD1088933S1 e USD1102294S1)?
  Um registro do movimento traria vistas ortogonais da platina.
- **Q-PAT-010** — Refazer toda a varredura por titular (Audemars Piguet, Turlen Holding, Richard Mille) em
  Espacenet e WIPO Patentscope, que bloquearam acesso automatizado neste pacote. Sem isso, qualquer afirmação
  de "não existe patente sobre X" continua sendo afirmação sobre a nossa busca, não sobre o mundo.

---

# Abertas pelo TASK-P1-003 (imprensa técnica, hands-on e desmontagens), 2026-09-21

Numeração a partir de `-101` em cada subsistema, para não colidir com os pacotes que rodam em paralelo.

## Barrilete

- **Q-BAR-101** — Natureza e número dos apoios periféricos do barrilete. A Chronos Japan (SRC-0403) descreve
  **quatro buchas de berílio-cobre**; a Hodinkee (SRC-0400) descreve **roletes** e fotografa um deles. São a mesma
  peça com nomes diferentes, ou há bucha fixa *e* rolete? São quatro em ambas as leituras? Ver H-BAR-101.
  Teste discriminante: contagem direta em foto de montagem de alta resolução do barrilete instalado.
- **Q-BAR-102** — Espessura real do barrilete. O fabricante só diz "menos de 1,18 mm" (CLM-0403), que é o teto do
  calibre inteiro. Sem esse número o Z-budget do andar do barrilete fica aberto.
- **Q-BAR-103** — Diâmetro do tambor, número de dentes e módulo do dentado do barrilete.
- **Q-BAR-104** — Como o arbor do barrilete é retido axialmente, já que não há receptáculo acima nem abaixo
  (CLM-0401). Há pivô em rubi? Apoio na platina e na caixa? Esta é uma questão de montabilidade, não de estética.

## Trem

- **Q-TRN-101** — A relação entre segunda roda e roda intermediária de transmissão é mesmo 1:1? A única fonte
  (SRC-0403) usa formulação de conjetura. Discriminante: contagem de dentes por periodicidade angular nas duas rodas.
- **Q-TRN-102** — Número de estágios entre barrilete e roda de escape, contando a intermediária de CLM-0406.
- **Q-TRN-103** — A "terceira roda" citada na ficha técnica (perfil involuta 20°) é a terceira do trem de marcha ou
  a terceira contada a partir do barrilete incluindo a intermediária? A nomenclatura do press kit é ambígua e isso
  muda o alvo do solver.

## Escape

- **Q-ESC-101** — Número de dentes da roda de escape. Nenhuma fonte de imprensa dá o número.
- **Q-ESC-102** — Geometria e posição do entalhe de banking na platina (CLM-0412): é um entalhe único que limita os
  dois sentidos, ou dois apoios? O ângulo total da âncora depende disso.
- **Q-ESC-103** — Se o plateau de segurança foi eliminado, o que resta no eixo do balanço além da pedra de impulso?
  Há uma parede anti-overbanking no plateau, como na patente, e ela é visível em alguma foto?
- **Q-ESC-104** — "Side lever" (SRC-0400) descreve a posição da âncora em relação ao balanço ou ao trem? Confirmar
  com os três centros visíveis numa mesma imagem.
- **Q-ESC-105** — A descrição japonesa de âncora "quase linear, com extremidade em crescente" (SRC-0405) é
  compatível com a fourchette alongada de cornes novas do press kit? Podem ser a mesma peça descrita duas vezes,
  ou duas leituras incompatíveis.

## Oscilador

- **Q-OSC-101** — Três braços: do balanço, da ponte, ou de ambos? A RM publica balanço de três braços; a Hodinkee
  fala em **ponte** superior de três braços (CLM-0418). Discriminante: foto frontal do balanço em repouso.
- **Q-OSC-102** — Geometria do degrau nos braços do balanço (CLM-0417): que altura ele recupera, e o plano da
  espiral fica dentro ou acima do aro?
- **Q-OSC-103** — Diâmetro do balanço e distribuição das seis massas — necessários para bater nos 3 mg·cm².

## Indicação

- **Q-IND-101** — Existe mesmo um trem de indicação independente, à esquerda, acionado pelo barrilete (CLM-0421)?
  É hipótese explícita de um jornalista, não observação. Ver H-IND-101.
- **Q-IND-102** — Se existe, como se obtém a relação 12:1 entre hora e minuto dentro de 1,18 mm?
- **Q-IND-103** — O eixo da indicação se apoia mesmo **contra o cristal** (CLM-0420)? Se sim, qual peça faz contato,
  qual a folga nominal e o que impede desgaste da safira. Nenhuma fonte ocidental menciona isso.

## Seletor e corda

- **Q-SEL-101** — Geometria do braço deslizante (CLM-0422): o que o desloca (came, excêntrico, alavanca), o que o
  mantém em posição (mola, detent) e qual é o curso.
- **Q-SEL-102** — Há posição neutra entre W e H, ou o braço só tem dois estados?
- **Q-SEL-103** — Em que sentido cada coroa gira para cada função no relógio **montado**. O sentido observado na
  Hodinkee vem de uma imagem em que o movimento está girado 180°.
- **Q-WND-101** — Princípio do limitador de torque (CLM-0425): embreagem por fricção, mola de deslizamento, catraca?
  Nenhuma imagem pública localiza a peça.

## Caixa e fixações

- **Q-CASE-101** — Profundidade real do rebaixo interno que recebe barrilete e trem (CLM-0428). O "talvez 0,05 mm"
  da Hodinkee é chute declarado e não pode entrar no Z-budget.
- **Q-CASE-102** — Posição exata e diâmetro do cilindro roscado central que trava caixa e movimento (CLM-0429), e
  como a platina é recortada em torno dele.
- **Q-CASE-103** — 13 parafusos (RM, SRC-0412) ou 12 (SRC-0405)? Provavelmente contagem visível contra total real,
  mas precisa ser resolvido por contagem em foto do verso.
- **Q-CASE-104** — Massa: 28,5 g com pulseira e 11,2 g de cabeça (SRC-0403/0404) contra "cerca de 30 g" (SRC-0402).
  Qual é a massa da cabeça a ser batida pelo CAD?
- **Q-CASE-105** — O cristal é elemento estrutural (CLM-0432)? Se for, a interface cristal-caixa tem pré-carga e
  precisa ser modelada como tal, não como peça apoiada.

## Rubis, choque, lacunas do corpus

- **Q-JWL-101** — Nenhuma fonte de imprensa localiza um único dos 23 rubis. A contabilidade terá de ser feita por
  imagem, pivô a pivô.
- **Q-SHK-101** — Quantos conjuntos Kif existem (só o balanço? também a roda de escape?) e onde ficam.
- **Q-DOC-101** — Não foi localizada matéria específica sobre o RM UP-01 em **Europa Star**, **WatchTime** e
  **Financial Times / HTSI**, apesar de os três serem alvos do `CLAUDE.md` §3.2. Pode ser limitação da busca
  (conteúdo em PDF de edição impressa, arquivo fechado). Reabrir com busca nos arquivos dos próprios veículos.
- **Q-DOC-102** — Quill & Pad (duas matérias) e Forbes recusaram acesso automatizado (HTTP 403). Precisam de
  leitura humana em navegador para saber se acrescentam algo.
- **Q-DOC-103** — **Não existe desmontagem pública** do RM UP-01 por terceiro. Todo material de movimento fora da
  caixa é da própria marca. Consequência: **não há nenhuma imagem pública do verso do movimento**. Enquanto isso
  valer, tudo que estiver do lado oculto será classe D ou E.

## Imagens e vídeo (abertas pelo TASK-P1-004 em 2026-09-21)

- **Q-IMG-001** — Não foi possível confirmar por acesso legítimo a URL exata do produto de onde saíram os 12
  arquivos `Richard_Mille_RM_UP_01_Ferrari_1000_*.jpg`. `hum3d.com` responde 301 para `3dmodels.org`, e
  este devolve 403 tanto a `curl` quanto a WebFetch (anti-bot). A atribuição a Hum3D/3DModels.org se apoia
  na marca d'água queimada nas próprias imagens e no padrão de nome (`_1000_` = preview de 1000 px).
  Suficiente para **descartar** o material como evidência (CLM-0700); insuficiente para citar a fonte com
  precisão bibliográfica.
- **Q-IMG-002** — Quais imagens oficiais são fotografia e quais são renderização? O critério usado aqui é
  indiciário (nome do arquivo, data de render anterior ao lançamento, ausência total de poeira/risco,
  sombreamento uniforme). Não existe declaração da marca. Enquanto isso, `IMG-0001`, `IMG-0006`, `IMG-0007`,
  `IMG-0009`…`IMG-0013` estão classificadas como `render_CG_oficial` por inferência, e medidas tiradas delas
  nascem classe E. Teste discriminante: metadados EXIF nos originais, ou uma imagem da mesma vista publicada
  por veículo independente com equipamento identificável.
- **Q-IMG-003** — O render oficial (`IMG-0001`, `IMG-0035`, `IMG-VID0001-K012_48`) reproduz fielmente a
  geometria do movimento real, ou foi simplificado para comunicação? Comparar os centros medidos em
  `IMG-0001` com os centros medidos na platina nua (`IMG-0026`) é o teste: se convergirem dentro da
  incerteza, o render vira utilizável como guia topológico; se divergirem, cai para ilustrativo.
- **Q-IMG-004** — A caixa é curva no eixo longo, então a silhueta de `IMG-0007` e `IMG-0011` é a envoltória
  do sólido, não uma seção. Medir 1,75 mm ali exige decidir em que ponto do contorno a espessura publicada
  se aplica (ponto mais espesso? centro?). Não há fonte que diga.
- **Q-IMG-005** — A roda grande esqueletada de `IMG-0005` está em vista rasante e parcialmente fora de foco:
  a contagem de dentes por periodicidade de borda só é possível em um arco do perímetro. Quantos dentes tem,
  e de que roda se trata (barrilete? primeira do trem?), fica aberto.
- **Q-IMG-006** — Entre 46 e 48 s o filme associa a legenda "we have patented an ultra-flat escapement" a um
  plano de uma peça em vista de topo. Não está estabelecido que a peça mostrada **seja** a do escape: em
  filme institucional a imagem e a legenda são montadas, não sincronizadas tecnicamente. Não usar essa
  associação como evidência sem confirmação independente.
- **Q-IMG-007** — As duas rodas montadas no prolongamento esquerdo da platina (`IMG-0026`, CLM-0705) foram
  lidas como roda de coroa e roda de cliquet por função. Nenhuma fonte primária nomeia essas peças no
  RMUP-01, e a arquitetura sem tige de remontoir pode ter outra topologia de corda. Fica `provisional`.
- **Q-IMG-008** — Não existe no corpus público nenhuma imagem do movimento pelo lado da platina com as rodas
  montadas, nenhuma vista do escape isolado, nenhuma seção, nenhum corte e nenhuma desmontagem de terceiro
  independente. Toda a evidência visual do RM UP-01 é controlada pela marca. Isso limita estruturalmente o
  que a Fase 5 e a Fase 9 podem afirmar — e precisa ser dito assim no site (§17 do `CLAUDE.md`).
- **Q-IMG-009** — O sprite 360° cobre apenas a rotação em torno do eixo vertical. Não há sequência
  equivalente em torno do eixo horizontal, o que deixa a vista de topo/base do **perfil** sem série
  multivista. Verificar se a página oficial expõe um segundo sprite não localizado neste pacote.
