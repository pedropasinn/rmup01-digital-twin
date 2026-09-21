# OPEN-QUESTIONS — consolidado da Fase 1

Consolidado em 2026-09-21 pela SÍNTESE DA FASE 1, a partir das 87 questões abertas pelos quatro pacotes
`TASK-P1-001` … `TASK-P1-004`. Estas 81 questões substituem integralmente as listas anteriores.

**O que mudou.** Os quatro pacotes rodaram em paralelo e numeraram suas questões em faixas separadas
(`-001`, `-010`, `-101`, `Q-IMG-*`) para não colidir. O preço disso foi um conjunto com repetições — a mesma
pergunta aberta três vezes com três IDs — e, em dois lugares, o **mesmo ID com dois significados**
(o `PATENT-TREE.md` usa `Q-BAR-001`, `Q-OSC-001` e `Q-CASE-001/002/003` com o sentido que o
`OPEN-QUESTIONS.md` do P1-002 registrou como `Q-BAR-010`, `Q-OSC-010` e `Q-CASE-010/011/012`). Aqui as
questões foram deduplicadas e renumeradas em **sequência única por subsistema**, e a **tabela de
equivalência do fim** traduz todo ID antigo para o novo. A partir desta consolidação, **citar sempre o ID
novo**; os antigos ficam só como histórico (ver DEC-004).

**Colunas.**
- *Bloqueia* — o primeiro marco do `CLAUDE.md` §16 que não fecha enquanto a questão estiver aberta.
  `—` significa que a questão é de higiene documental ou editorial e não trava nenhum marco.
- *Teste discriminante* — o experimento, a medição ou o documento que efetivamente decide. Onde o teste é
  "declaração primária", está dito: é uma questão que nenhuma medida nossa resolve.
- *Melhor fonte candidata* — onde procurar primeiro. `U01`…`U20` são os pedidos já no Balcão
  (`pedidos-chatgpt/PEDIDOS.json`); `IMG-*` são imagens do catálogo; `TASK-P2-*` são pacotes do backlog.

**Regra que não muda:** ausência de resposta não vira certeza em lugar nenhum do repositório.

---

## Resumo por prioridade

| Bloqueia | Quantas | As mais caras |
|---|---|---|
| **M1** envelope geométrico | 17 | Q-CRY-001 (0,45 × 0,20), Q-BASE-003 (espessuras internas), Q-CASE-002 (onde valem os 1,75 mm) |
| **M2** esqueleto mecânico | 12 | Q-IMG-003 (o render é fiel?), Q-BASE-004, Q-BRG-001, Q-CASE-010 (registro do movimento) |
| **M3** esqueleto cinemático | 17 | Q-TRN-002 (dentes), Q-IND-001 (onde está o 12:1), Q-SEL-001 (braço deslizante) |
| **M4** escape | 16 | Q-ESC-001 (dentes da roda), Q-ESC-004 (banking), Q-ESC-006 (cheville no plateau ou no balanço), Q-OSC-001 (o que produz 3 mg·cm²) |
| **M5** montagem nominal | 6 | Q-BAR-003 (retenção axial do arbor), Q-FST-002 |
| **M6** CAD convergido | 2 | Q-JWL-001 (os 23 rubis), Q-WND-002 |
| **M7** auditoria de plausibilidade | 1 | Q-CASE-006 (qual massa o CAD tem de bater) |
| duas em dois marcos | 2 | Q-PAT-001 (M2/M4), Q-IMG-007 (M4/M6) |
| — não bloqueia | 8 | Q-DOC-007, Q-IMG-001, Q-WND-003, Q-ESC-008, Q-DOC-003…006 |

Três questões não são fecháveis por trabalho nosso e definem o teto do projeto: **Q-IMG-007** (não existe
desmontagem pública nem vista do verso do movimento), **Q-DOC-001** (não há press kit em PDF nem manual
público) e **Q-DOC-002** (a Audemars Piguet Le Locle nunca falou publicamente deste relógio).

---

## CASE — caixa

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-CASE-001** | Perfil de espessura da caixa ao longo do contorno. Sabemos que há pontos com 0,18 mm (CLM-0430), não **onde**. | M1 | Seções extraídas do ajuste multivista do sprite 360° (IMG-0012) confrontadas com o par ortogonal IMG-0009/IMG-0011; um corte publicado encerraria a questão. | U14; TASK-P2-003 |
| **Q-CASE-002** | Em que ponto do contorno curvo se aplicam os 1,75 mm publicados — espessura máxima, centro, ou envoltória? A caixa é curva no eixo longo, então a silhueta de perfil é envoltória, não seção (antigo Q-IMG-004). | M1 | Reconstruir a superfície pelo sprite 360° e comparar a espessura em cada seção com 1,75 mm: só uma das leituras fecha. | TASK-P2-003; U14 |
| **Q-CASE-003** | Profundidade real do rebaixo interno da caixa que recebe barrilete e trem (CLM-0428). O "talvez 0,05 mm" da Hodinkee é chute declarado e **não entra no Z-budget**. | M1 | Metrologia em IMG-0027 (movimento dentro da caixa, vista nadir) medindo o degrau visível; ou declaração primária. | TASK-P2-002; U14 |
| **Q-CASE-004** | Posição e diâmetro do cilindro roscado central que trava caixa e movimento (CLM-0429), e como a platina é recortada em torno dele. | M2 | O furo/recorte tem de aparecer na platina nua: procurar em IMG-0026 na região do canto superior direito do barrilete. | TASK-P2-005 |
| **Q-CASE-005** | A caixa é "corpo + tampa" (SRC-0404) com nervura periférica de espessura integral (SRC-0403): onde fica a linha de junção e qual é a seção da borda? | M1 | Perfil calibrado + vistas 1.3/1.4/1.5 do USD991795 (proporção relativa apenas). | U14; TASK-P2-003 |
| **Q-CASE-006** | Massa da cabeça do relógio: 11,2 g (SRC-0403/0404) contra "cerca de 30 g" com pulseira (SRC-0402) e 28,5 g com pulseira. Qual número o CAD tem de bater? | M7 | Reconciliar as três fontes; a massa do movimento (2,82 g) é a única classe A sem disputa. | U08; U14 |
| **Q-CASE-007** | O cristal das horas é elemento estrutural da caixa, com pré-carga (H-CASE-101)? | M5 | Declaração primária; subsidiariamente, comparar a rigidez do modelo com e sem o cristal colado — o que dá plausibilidade, não fato. | U14; U01 |
| **Q-CASE-008** | Ler o registro internacional de Haia **DM/218823** na base Hague Express: eleva a identificação do desenho do UP-01 de B para A e dá a lista de países. | M1 | Leitura direta do registro. | U05 |
| **Q-CASE-009** | Quais dos registros irmãos depositados em 28/10/2021 pela Turlen Holding (TWD222805S/06S/07S, CA208187S, CA210542S, ZAA202200456S) são o UP-01? USD989636S1, da mesma data, **não** é. | M1 | Abrir cada prancha. | U05 |
| **Q-CASE-010** | Existe registro de desenho do **movimento** RMUP-01? USD1015914S1 foi aberto e não é; faltam USD1088933S1 e USD1102294S1. Um registro do movimento traria vistas ortogonais da platina. | M2 | Abrir os dois documentos. | U05 |

## CRY — cristais

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-CRY-001** | Espessura do cristal das horas: **0,45 mm** (ficha técnica em cinco idiomas) ou **0,20 mm** ("os dois cristais afinados a 2/10" na narrativa do mesmo comunicado)? `P_CRY_HOURS_THICKNESS` está `contested`. | M1 | Metrologia de perfil calibrada pela espessura total de 1,75 mm; ou press kit/manual oficial em PDF. **Ver a nota do CAD-RECONSTRUCTION-PLAN §4: o argumento de Z-budget que parecia decidir a favor de 0,20 mm não se sustenta quando o orçamento é feito por coluna.** | U01; U14; TASK-P2-004 |
| **Q-CRY-002** | Os dois cristais são circulares? Que diâmetro e que posição têm? O comunicado fala em "diâmetro calculado", o que sugere círculo, mas não há desenho público. | M1 | Homografia em IMG-0004 (luneta e movimento no mesmo plano e na mesma escala). | TASK-P2-002 |
| **Q-CRY-003** | Como cada cristal é assentado e vedado na luneta (rebaixo, colagem, junta), e quanto da sua espessura fica acima da superfície externa. | M5 | Macro do perfil na borda do cristal; ou declaração primária. | U14 |

## BASE — platina

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-BASE-001** | Qual eixo do relógio corresponde aos 41,45 mm do calibre? A marca publica as duas medidas, não a orientação. H-BASE-001 já a trata como praticamente decidida pela aritmética da caixa (a alternativa é geometricamente impossível). | M1 | Qualquer vista frontal ortogonalizada com o movimento visível — IMG-0004 fecha sozinha. | TASK-P2-002 |
| **Q-BASE-002** | Repartição da folga movimento–caixa (9,55 mm no comprimento, 10,15 mm na largura): é ela que fixa a origem do sistema de coordenadas. | M1 | Medir a folga nos quatro lados em IMG-0027. | TASK-P2-002 |
| **Q-BASE-003** | Espessura da platina, das pontes e de **cada camada** do empilhamento vertical. Só o total de 1,18 mm é publicado. É o problema central da Fase 3. | M1 | Nenhuma imagem pública resolve (não há seção nem vista de perfil do calibre). Só fecha por inferência de soma sob restrição, ou por documento primário. | U01; TASK-P2-004 |
| **Q-BASE-004** | Contorno completo da platina, incluindo o prolongamento esquerdo que aloja os comandos e os recortes que recebem as duas coroas (CLM-0439). | M2 | Homografia em IMG-0026 (platina nua), com o suporte de montagem dando o plano de referência. | TASK-P2-005 |
| **Q-BASE-005** | O que existe na face da platina voltada para o mostrador? Nenhuma imagem pública mostra o movimento por esse lado com as rodas montadas. Todo o caminho de acerto de hora é invisível. | M2 | Não há teste disponível no corpus atual; depende de material novo (Q-IMG-007). | — |

## BRG — pontes

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-BRG-001** | Quantas pontes existem e qual é a topologia de cada uma? O render IMG-0001 sugere ao menos duas (balanço em cima à direita, trem embaixo à direita), mas render não é evidência do objeto. | M2 | Contagem em IMG-0026 pelos furos de fixação e pinos de centragem, cruzada com IMG-0001 (o teste de fidelidade do render, Q-IMG-003, precisa vir antes). | TASK-P2-001; TASK-P2-005 |
| **Q-BRG-002** | A ponte esqueletada de três braços com três mancais rubinados (CLM-0706, IMG-0003 + IMG-0028) é a ponte do trem? De que eixos ela cuida? | M2 | Casar os três centros da peça isolada com três centros medidos na platina nua (a distância entre eles é invariante e recuperável por duas vistas). | TASK-P2-005 |

## BAR — barrilete

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-BAR-001** | Geometria do barrilete: diâmetro do tambor, número de dentes, módulo e **espessura real**. O fabricante só diz "menos de 1,18 mm", que é o teto do calibre inteiro. | M2 | Diâmetro e dentes por metrologia + periodicidade angular em IMG-0029 e IMG-0026 (abertura na platina); a espessura não tem imagem e depende do Z-budget. | TASK-P2-007; U13 |
| **Q-BAR-002** | Natureza e número dos apoios periféricos: **quatro buchas de berílio-cobre** (Chronos) ou **roletes** (Hodinkee)? São a mesma peça com dois nomes (H-BAR-101), ou há bucha fixa *e* rolete? | M2 | Contagem direta em macro do barrilete instalado; verificar se cada apoio tem pivô central. O vídeo oficial quadro a quadro é a melhor chance. | TASK-P2-007 |
| **Q-BAR-003** | Como o arbor é retido axialmente, já que não há receptáculo acima nem abaixo (CLM-0401)? Pivô em rubi? Apoio contra a caixa? É questão de montabilidade, não de estética. | M5 | Nenhuma imagem pública mostra; decide-se por coerência de montagem no CAD e por qualquer macro nova do barrilete. | U13 |
| **Q-BAR-004** | Localizar a família de patentes do **barrilete extraplano**, dito "patenteado" pela marca (H-BAR-001). O TASK-P1-002 procurou e não achou — resultado sobre a nossa busca, não sobre o mundo. | M2 | Varredura por CPC G04B1/10–1/22 e por titular com acesso à Espacenet/WIPO (bloqueadas ao acesso automatizado). | U04; U05; TASK-P2-011 |
| **Q-BAR-005** | Mola principal: espessura de lâmina, comprimento, altura útil e curva de torque que produza 45 h ± 10% com 7,5 voltas úteis. | M3 | Modelo de engenharia separado (`geometry-reconstruction` × `functional-surrogate`, §8 Fase 6) validado contra a reserva publicada. | U13 |

## WND — corda

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-WND-001** | Como a coroa-roda engrena no calibre atravessando a caixa e mantendo 1 atm: geometria do acoplamento, eixo, vedação. Não há tige de remontoir (CLM-0036). | M3 | Macro da luneta na região das coroas + quadros do filme mostrando a montagem das coroas **antes** do encaixotamento (SRC-0403 afirma essa ordem). | TASK-P2-009; U15 |
| **Q-WND-002** | A ficha técnica lista "Crown: DLC treated 316L stainless steel", mas as coroas são descritas como rodas do calibre; as matérias japonesas dizem aço inoxidável com aro de cerâmica. A qual peça exatamente se refere o DLC? | M6 | Reconciliação de fontes; macro colorimétrica não decide. | U01; U08 |
| **Q-WND-003** | O bloco "Couronne dynamométrique" reproduzido em SRC-0006 fala em evitar a quebra da *tige de remontoir* — peça que este relógio não tem. Boilerplate de outro modelo? **Não usar como evidência até confirmação.** | — | Comparar o mesmo parágrafo em fichas técnicas de outros modelos Richard Mille. | U01 |
| **Q-WND-004** | Princípio do limitador de torque (CLM-0425): embreagem por fricção, mola deslizante, catraca? Nenhuma imagem pública localiza a peça. | M3 | Vídeo quadro a quadro na sequência de corda; ou patente ainda não localizada. | TASK-P2-009; U15 |
| **Q-WND-005** | Diâmetro e número de dentes das duas rodas de comando, e se as duas são realmente idênticas (CLM-0709). | M3 | As duas aparecem isoladas e no mesmo plano de escala em IMG-0004; macro de alta resolução em IMG-0006. | TASK-P2-002 |

## SEL — seletor de função W/H

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-SEL-001** | Mecanismo interno do seletor: o que desloca o braço deslizante (came, excêntrico, alavanca), o que o mantém em posição (mola, detent) e qual é o curso. Só o efeito é público. | M3 | Vídeo oficial quadro a quadro na janela em que o braço é manipulado com pinça; a platina nua mostra os recortes que limitam o curso. | TASK-P2-009; U15 |
| **Q-SEL-002** | Há posição neutra entre W e H, ou o braço só tem dois estados? | M3 | Observação do curso no vídeo; a EP4295198B1 prevê duas **ou três** posições angulares estáveis — o que só sugere. | TASK-P2-009 |
| **Q-SEL-003** | Em que sentido cada coroa gira para cada função no relógio **montado**. O sentido observado na Hodinkee vem de uma foto com o movimento girado 180°. | M3 | Vídeo de operação com o relógio montado (SRC-0409 descreve sentidos opostos para corda e acerto). | TASK-P2-009 |
| **Q-SEL-004** | Qual patente, se alguma, cobre o seletor W/H? A EP4295198B1 é parente conceitual (mesmo inventor, fev/2021), não prova. | M3 | Varredura por titular com acesso à Espacenet; CPC G04B3/* e G04B27/*. | U04; U15; TASK-P2-011 |
| **Q-SEL-005** | CH718513A1 ("Device for selecting and actuating several functions of a watch movement") é da mesma família da EP4295198B1, é um segundo depósito suíço, ou é de outro titular? Documento nunca aberto. | M3 | Leitura do documento. | U04 |

## TRN — trem

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-TRN-001** | Qual roda real recebe o perfil involuta de 20°: en "third-wheel pinion", fr "pignon de moyenne", ja 三番車カナ, zh 过轮小齿轮. A nomenclatura diverge entre idiomas e a arquitetura não é a clássica. | M3 | Identificar a roda por posição depois que os centros estiverem medidos; a ambiguidade é de vocabulário e só some com a topologia resolvida. | U16; TASK-P2-005 |
| **Q-TRN-002** | Número de dentes, módulos, diâmetros e distâncias entre centros de **todas** as rodas e pinhões. Nenhum número é publicado em nenhum idioma. | M3 | `gear_search` sobre centros medidos + contagem por periodicidade angular onde a borda estiver resolvida. | TASK-P2-006; TASK-P2-007; U13 |
| **Q-TRN-003** | Quantos estágios existem entre barrilete e roda de escape, contando a roda intermediária de CLM-0406? | M3 | Contagem de centros na platina nua + coerência com a razão total exigida (ver VALIDATION-PLAN §3). | TASK-P2-005; TASK-P2-006 |
| **Q-TRN-004** | A relação entre segunda roda e roda intermediária é mesmo 1:1? A única fonte usa formulação de conjetura (ようなので). | M3 | Contagem de dentes nas duas rodas; aritmeticamente um estágio 1:1 é um *idler* e é compatível com a razão total (ver CAD-RECONSTRUCTION-PLAN §7). | TASK-P2-006 |
| **Q-TRN-005** | Quantos dentes tem a roda grande esqueletada de IMG-0005, e de que roda se trata (barrilete? primeira do trem?)? A vista é rasante e só um arco do perímetro é utilizável. | M3 | Correção de perspectiva e contagem por periodicidade no arco em foco, confirmada por diâmetro relativo. | TASK-P2-007 |

## ESC — escape

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-ESC-001** | Número de dentes da roda de escape. Nem a marca, nem a imprensa, nem a patente dão o número — a patente sequer desenha a roda no ciclo. | M4 | Contagem por periodicidade em macro; ou fechamento do trem pelo `gear_search` com a razão total. | TASK-P2-006; TASK-P2-008 |
| **Q-ESC-002** | Geometria das pedras de pallet, ângulos de locking e de draw, drop e clearance. A marca diz apenas que a geometria foi "alterada para travamento seguro". | M4 | Simulação 2D paramétrica que produza ciclo válido a 4 Hz com 54° de levantamento; o conjunto de soluções é reduzido, não único. | TASK-P2-008; U11 |
| **Q-ESC-003** | Qual é, no RMUP-01, a superfície anti-renversement, e o que resta no eixo do balanço além da cheville? A patente responde pela **invenção** (periferia cilíndrica do plateau com entalhe, batida pela parede externa das cornas); falta confirmar a execução. | M4 | Macro do balanço de lado: existe ou não um disco separado abaixo dos braços? | TASK-P2-008; U11 |
| **Q-ESC-004** | Banking: a âncora bate contra **um entalhe usinado na platina** (CLM-0412), contra **goupilles** (reiv. 10 da patente), ou a função está "na própria forquilha" (press kit)? Um entalhe único limitando os dois sentidos, ou dois apoios? As três descrições precisam ser conciliadas antes de qualquer simulação. | M4 | Metrologia da região em macro; a geometria do entalhe define o ângulo total de debate da âncora, que por sua vez é testável contra os 54°. | TASK-P2-008 |
| **Q-ESC-005** | O RMUP-01 respeita os modos preferidos das reivindicações 7 e 8 (distância âncora–plateau ≥ 2 × distância âncora–roda de escape; três centros coplanares)? A patente permite explicitamente não respeitar. | M4 | Metrologia dos três centros numa macro calibrada. | TASK-P2-005; TASK-P2-008 |
| **Q-ESC-006** | A cheville é carregada por um suporte de uma peça com o plateau (reiv. 4) ou **pelo próprio balanço** (reiv. 5)? Muda um nível inteiro do orçamento vertical do oscilador (H-ESC-011). | M4 | Macro do balanço visto de lado ou desmontado. | TASK-P2-008; U12 |
| **Q-ESC-007** | Existe pedido de patente posterior, específico do escape **do RMUP-01** (prioridade 2020–2022), distinto da família de 2019? | M4 | Varredura por titular e CPC G04B15/* com acesso desbloqueado. | U04; TASK-P2-011 |
| **Q-ESC-008** | Situação legal de JP7537920B2 e CN112114508B e existência de uma concessão suíça CH716337B1 — nada conferido em base nacional. | — | Consulta a J-PlatPat, CNIPA e Swissreg. | U04 |
| **Q-ESC-009** | "Side lever" (SRC-0400) descreve a posição da âncora em relação ao balanço ou ao trem? | M4 | Uma única imagem com os três centros (roda de escape, âncora, balanço) visíveis resolve. | TASK-P2-005 |
| **Q-ESC-010** | A âncora "quase linear, com extremidade em crescente" (SRC-0405, ja) é a mesma peça que a "fourchette alongada com cornes modificadas" do press kit, ou são duas leituras incompatíveis? | M4 | Silhueta da âncora em macro; a figura 5 da patente mostra que a forma é livre dentro da invenção e **não pode ser copiada**. | TASK-P2-008 |

## OSC — oscilador

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-OSC-001** | Diâmetro do balanço, seção dos braços, massa do aro e geometria/massa das seis massas de regulagem. Só o momento de inércia total (3 mg·cm²) é publicado — uma equação com muitas incógnitas. | M4 | Metrologia do diâmetro em macro + espaço de soluções de massa que produza 3 mg·cm² em titânio grau 5; manter o conjunto de candidatos, não escolher um. | U12; TASK-P2-005 |
| **Q-OSC-002** | Geometria da espiral AK 3: número de voltas, seção, diâmetro externo, curva terminal, ponto de fixação. "AK 3" identifica o produto, não a geometria. | M4 | Cálculo inverso a partir de 4 Hz e 3 mg·cm² (rigidez exigida), mais macro do plano da espiral. | U12 |
| **Q-OSC-003** | Três braços: do **balanço**, da **ponte**, ou de ambos? A RM publica balanço de três braços; a Hodinkee fala em ponte superior de três braços. | M2 | Foto frontal do balanço em repouso — resolve por observação simples. | TASK-P2-010 |
| **Q-OSC-004** | Geometria do degrau nos braços do balanço (CLM-0417): que altura ele recupera, e o plano da espiral fica dentro ou acima do aro? | M4 | Macro de perfil do balanço; entra direto no Z-budget do oscilador. | U12; TASK-P2-004 |
| **Q-OSC-005** | Localizar a patente do **balanço de inércia variável ultraplano**, dito patenteado. Não encontrada no TASK-P1-002. | M4 | Varredura por CPC G04B17/06 e G04B18/* com prioridade 2019–2022. | U04; TASK-P2-011 |

## IND — indicação

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-IND-001** | Onde está a relação 12:1 entre hora e minuto, se os ponteiros são decalcados diretamente sobre rodas e não há canhão nem roda das horas empilhada? | M3 | Identificar o que engrena com cada roda porta-ponteiro; a razão tem de aparecer como dois pares de dentes no plano. | TASK-P2-010; U13 |
| **Q-IND-002** | Os dois ponteiros são coaxiais? A arquitetura "espalhada no plano" permite que não sejam (H-IND-001). | M2 | **Qualquer fotografia frontal com os dois ponteiros visíveis.** Se os eixos forem distintos, fica resolvido por observação (classe B). É a questão mais barata do conjunto. | IMG-0009, IMG-0036; TASK-P2-010 |
| **Q-IND-003** | Existe um trem de indicação independente, à esquerda, acionado pela rotação do barrilete (H-IND-101)? É hipótese explícita de um jornalista, não observação. **Não usar como fato em nenhuma fase.** | M3 | Foto de montagem em que se veja o que engrena com a roda do ponteiro dos minutos; ou coerência de razões — do barrilete a 1 volta/6 h até 1 volta/h exige razão 6:1 exata, testável pelo solver contra os diâmetros observados. | TASK-P2-006; TASK-P2-010 |
| **Q-IND-004** | O eixo da indicação se apoia mesmo **contra o cristal** (CLM-0420, só em fonte japonesa)? Se sim, qual peça faz contato, qual a folga nominal e o que impede desgaste da safira. | M1 | Declaração primária ou macro de perfil; se confirmada, é interface cristal↔movimento com efeito direto no Z-budget. | U14; U08 |
| **Q-IND-005** | Como o ponteiro é fixado sobre a roda (assento, aperto, colagem) e que diâmetro tem esse assento? | M5 | LMK-IMG0031-001: a interface ponteiro–roda em IMG-0031 é a única evidência visual do acoplamento. | TASK-P2-010 |

## JWL, SHK, FST, STR

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-JWL-001** | Distribuição dos 23 rubis por mancal. Só a contagem é publicada, e nenhuma imagem mostra os 23 simultaneamente. A contabilidade terá de ser feita pivô a pivô. | M6 | Inventário por imagem: rubis visíveis em IMG-0026 (platina nua), IMG-0003 (ponte de 3 braços), IMG-0005 (rubis soltos), IMG-0001 (render, só como guia). Fechar ou declarar explicitamente o que não foi localizado (§17). | TASK-P2-005 |
| **Q-SHK-001** | Qual modelo/calibre de Kif é usado, quantos conjuntos existem e onde (só o balanço? também a roda de escape?). | M4 | Macro do balanço; catálogo público de modelos Kif confrontado com o diâmetro medido. | U12 |
| **Q-FST-001** | Repartição dos 13 parafusos entre caixa e pulseira (Boillat diz que os 13 prendem caixa **e** pulseira), e a divergência 13 (RM) × 12 (SRC-0405). | M1 | Contagem em foto do verso e da frente, com as cabeças identificadas uma a uma. | TASK-P2-002 |
| **Q-FST-002** | Geometria dos parafusos spline: diâmetro, passo, número de entalhes (cinco, segundo a Hodinkee), e as arruelas 316L. | M5 | Macro IMG-0006 calibrada; a chave dedicada dá o perfil do encaixe. | TASK-P2-002 |
| **Q-FST-003** | Fixações internas: quantos parafusos prendem cada ponte, e onde estão os pinos de centragem. A ponte de três braços tem dois furos de parafuso e um furo liso (CLM-0706). | M5 | Contagem em IMG-0026 e IMG-0003/IMG-0028. | TASK-P2-005 |
| **Q-STR-001** | Interface da pulseira: geometria das orelhas/encaixes e material do bracelete. Nenhuma fonte primária localizada descreve. | M1 | Sprite 360° e vistas do USD991795; IMG-0007 mostra recortes de interface na borda. | U14; TASK-P2-003 |

## PAT e DOC — o que não conseguimos alcançar

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-PAT-001** | Refazer **toda** a varredura por titular (Audemars Piguet, Turlen Holding, Richard Mille) e por CPC em Espacenet e WIPO Patentscope, que bloquearam acesso automatizado. Sem isso, "não existe patente sobre X" é afirmação sobre a nossa busca, não sobre o mundo. | M2/M4 | Acesso humano ou chave OPS do EPO. | U04; U05; TASK-P2-011 |
| **Q-DOC-001** | Press kit oficial em PDF e manual de uso/pós-venda público: não localizados no domínio richardmille.com. O comunicado íntegro só existe por reprodução em imprensa (SRC-0006, SRC-0008). | M1 | Busca no próprio domínio e em canais de revendedor autorizado. | U01 |
| **Q-DOC-002** | **Nenhuma** declaração pública da Audemars Piguet Le Locle ou de Giulio Papi sobre o RM UP-01 ou sobre o escape do RMUP-01 foi localizada. Toda a atribuição vem do lado Richard Mille. | M4 | Entrevistas em veículos suíços e franceses; anais de conferência; o caminho real é a árvore de patentes. | U09; U04 |
| **Q-DOC-003** | Nenhuma declaração do próprio Richard Mille (a pessoa) sobre este modelo. As citações oficiais são de Arbona, Boillat e Mathys. | — | Entrevistas de lançamento em vídeo. | U09; U17 |
| **Q-DOC-004** | Preço: não publicado por nenhuma das duas marcas. A imprensa cita CHF 1 700 000 fora impostos. | — | Registrar com fonte de imprensa e classe correta; não é dado técnico. | U06 |
| **Q-DOC-005** | Não foi localizada matéria específica sobre o RM UP-01 em **Europa Star**, **WatchTime** e **Financial Times / HTSI**, apesar de serem alvos do `CLAUDE.md` §3.2. Pode ser limitação da busca (edição impressa, arquivo próprio não indexado). | — | Busca nos arquivos próprios dos três veículos. | U06 |
| **Q-DOC-006** | Quill & Pad (duas matérias) e Forbes recusaram acesso automatizado (HTTP 403). Precisam de leitura humana em navegador para saber se acrescentam algo. Nada foi contornado. | — | Leitura humana. | Pedro; U06 |
| **Q-DOC-007** | Horas de desenvolvimento: "mais de 6 000" contra 3 600 + 2 400 + 2 000 = 8 000 no mesmo comunicado. Sem consequência para o CAD; registrado para não citarmos números incompatíveis. | — | Nenhum; é questão editorial. | U02 |

## IMG — o corpus visual

| ID | Questão | Bloqueia | Teste discriminante | Melhor fonte candidata |
|---|---|---|---|---|
| **Q-IMG-001** | Não foi possível confirmar por acesso legítimo a URL exata do produto Hum3D/3DModels.org de onde saíram os 12 arquivos descartados. A atribuição se apoia na marca d'água e no padrão de nome — suficiente para **descartar**, insuficiente para citar. | — | Acesso humano ao site (responde 403 a robô). Baixa prioridade: o material está descartado de qualquer modo. | Pedro |
| **Q-IMG-002** | Quais imagens oficiais são fotografia e quais são render? O critério hoje é indiciário (nome de arquivo, data de render anterior ao lançamento, ausência de poeira, sombreamento uniforme). **Medida tirada de render oficial nasce classe E** (DEC-003). | M1 | Metadados EXIF nos originais; ou a mesma vista publicada por veículo independente com equipamento identificável. | TASK-P2-001 |
| **Q-IMG-003** | O render oficial (IMG-0001, IMG-0035) reproduz fielmente a geometria do movimento real, ou foi simplificado para comunicação? | M2 | **Comparar os centros medidos em IMG-0001 com os centros medidos na platina nua IMG-0026.** Se convergirem dentro da incerteza, o render vira guia topológico legítimo; se divergirem, cai para ilustrativo. É o teste mais barato e de maior consequência de toda a Fase 2. | **TASK-P2-001** |
| **Q-IMG-004** | Entre 46 e 48 s o filme associa a legenda "we have patented an ultra-flat escapement" a um plano de uma peça em vista de topo. Não está estabelecido que a peça mostrada **seja** a do escape: em filme institucional imagem e legenda são montadas, não sincronizadas tecnicamente. | M4 | Identificar a peça por forma, cruzando com a topologia da patente. Não usar a associação como evidência sem confirmação. | TASK-P2-008 |
| **Q-IMG-005** | As duas rodas montadas no prolongamento esquerdo da platina (IMG-0026) foram lidas como roda de coroa e roda de cliquet **por função**. Nenhuma fonte primária nomeia essas peças, e a arquitetura sem tige pode ter outra topologia. | M3 | Vídeo quadro a quadro da sequência de corda; presença ou ausência de cliquet e mola. | TASK-P2-009 |
| **Q-IMG-006** | O sprite 360° cobre só a rotação em torno do eixo vertical. Não há sequência equivalente em torno do eixo horizontal, o que deixa o **perfil** sem série multivista. Existe um segundo sprite não localizado? | M1 | Inspeção do código da página oficial. | TASK-P2-003 |
| **Q-IMG-007** | **Limite estrutural do corpus.** Não existe em fonte pública: imagem do movimento pelo lado do mostrador com rodas montadas, vista do escape isolado, seção, corte, desenho cotado, vista do verso do movimento, nem desmontagem de terceiro. Toda a evidência visual do RM UP-01 é controlada pela marca. | M4/M6 | Não é fechável por trabalho nosso. Define o teto de classe de evidência de tudo que está do lado oculto (D ou E) e **precisa aparecer no site**. | — |

---

## Tabela de equivalência — ID antigo → ID novo

Toda questão aberta pelos pacotes P1-001…P1-004 está aqui. `=` significa que o ID não mudou de número nem
de sentido. "fundida em" significa que a pergunta foi absorvida por outra, mais concreta ou mais ampla.

| Antigo | Pacote | Novo | Observação |
|---|---|---|---|
| Q-CRY-001 | P1-001 | Q-CRY-001 | = |
| Q-CRY-002 | P1-001 | Q-CRY-002 | = |
| Q-DOC-001 | P1-001 | Q-DOC-007 | renumerada (horas de desenvolvimento) |
| Q-DOC-002 | P1-001 | Q-DOC-001 | press kit / manual |
| Q-DOC-003 | P1-001 | Q-DOC-002 | AP Le Locle / Papi |
| Q-DOC-004 | P1-001 | Q-DOC-003 | declaração de Richard Mille |
| Q-DOC-005 | P1-001 | Q-DOC-004 | preço |
| Q-WND-003 | P1-001 | Q-WND-003 | = |
| Q-TRN-001 | P1-001 | Q-TRN-001 | fundida com Q-TRN-103 |
| Q-BASE-001 | P1-001 | Q-BASE-001 | = |
| Q-BASE-002 | P1-001 | Q-BASE-002 | = |
| Q-BASE-003 | P1-001 | Q-BASE-003 | = (absorve a espessura das pontes) |
| Q-TRN-002 | P1-001 | Q-TRN-002 | = |
| Q-TRN-003 | P1-001 | Q-TRN-003 + Q-IND-003 | a parte "trem separado da indicação" foi para IND |
| Q-BAR-001 | P1-001 | Q-BAR-001 | fundida com Q-BAR-102 e Q-BAR-103 |
| Q-BAR-002 | P1-001 | Q-BAR-004 | patente do barrilete; duplicada por Q-BAR-010 |
| Q-BAR-003 | P1-001 | Q-BAR-002 | fundida com Q-BAR-101 |
| Q-ESC-001 | P1-001 | Q-ESC-001 + Q-ESC-002 | dentes separados da geometria de pallets |
| Q-ESC-002 | P1-001 | Q-ESC-003 | fundida com Q-ESC-103 |
| Q-OSC-001 | P1-001 | Q-OSC-001 | fundida com Q-OSC-103 |
| Q-OSC-002 | P1-001 | Q-OSC-002 | = |
| Q-SHK-001 | P1-001 | Q-SHK-001 | fundida com Q-SHK-101 |
| Q-JWL-001 | P1-001 | Q-JWL-001 | fundida com Q-JWL-101 |
| Q-IND-001 | P1-001 | Q-IND-001 | fundida com Q-IND-102 |
| Q-IND-002 | P1-001 | Q-IND-002 | = |
| Q-SEL-001 | P1-001 | Q-SEL-001 | fundida com Q-SEL-101 |
| Q-WND-001 | P1-001 | Q-WND-001 | = |
| Q-WND-002 | P1-001 | Q-WND-002 | = |
| Q-CASE-001 | P1-001 | Q-CASE-001 | = (atenção: o PATENT-TREE.md usa este ID para o registro de Haia) |
| Q-CASE-002 | P1-001 | Q-FST-001 + Q-FST-002 | repartição e geometria dos parafusos separadas |
| Q-FST-001 | P1-001 | Q-FST-001 | fundida com Q-CASE-103 |
| Q-STR-001 | P1-001 | Q-STR-001 | = |
| Q-ESC-010 | P1-002 | Q-ESC-005 | reivindicações 7 e 8 |
| Q-ESC-011 | P1-002 | Q-ESC-006 | cheville: reiv. 4 × reiv. 5 |
| Q-ESC-012 | P1-002 | Q-ESC-004 | fundida com Q-ESC-102 |
| Q-ESC-013 | P1-002 | Q-ESC-001 | fundida |
| Q-ESC-014 | P1-002 | Q-ESC-007 | |
| Q-ESC-015 | P1-002 | Q-ESC-008 | |
| Q-SEL-010 | P1-002 | Q-SEL-004 | |
| Q-SEL-011 | P1-002 | Q-SEL-005 | (o PATENT-TREE.md chama-a Q-SEL-003) |
| Q-BAR-010 | P1-002 | Q-BAR-004 | duplicata de Q-BAR-002 antigo |
| Q-OSC-010 | P1-002 | Q-OSC-005 | (o PATENT-TREE.md chama-a Q-OSC-001) |
| Q-CASE-010 | P1-002 | Q-CASE-008 | registro de Haia DM/218823 |
| Q-CASE-011 | P1-002 | Q-CASE-009 | registros irmãos |
| Q-CASE-012 | P1-002 | Q-CASE-010 | registro do movimento |
| Q-PAT-010 | P1-002 | Q-PAT-001 | |
| Q-BAR-101 | P1-003 | Q-BAR-002 | fundida |
| Q-BAR-102 | P1-003 | Q-BAR-001 | fundida |
| Q-BAR-103 | P1-003 | Q-BAR-001 | fundida |
| Q-BAR-104 | P1-003 | Q-BAR-003 | |
| Q-TRN-101 | P1-003 | Q-TRN-004 | |
| Q-TRN-102 | P1-003 | Q-TRN-003 | fundida |
| Q-TRN-103 | P1-003 | Q-TRN-001 | fundida |
| Q-ESC-101 | P1-003 | Q-ESC-001 | fundida |
| Q-ESC-102 | P1-003 | Q-ESC-004 | fundida |
| Q-ESC-103 | P1-003 | Q-ESC-003 | fundida |
| Q-ESC-104 | P1-003 | Q-ESC-009 | |
| Q-ESC-105 | P1-003 | Q-ESC-010 | |
| Q-OSC-101 | P1-003 | Q-OSC-003 | |
| Q-OSC-102 | P1-003 | Q-OSC-004 | |
| Q-OSC-103 | P1-003 | Q-OSC-001 | fundida |
| Q-IND-101 | P1-003 | Q-IND-003 | |
| Q-IND-102 | P1-003 | Q-IND-001 | fundida |
| Q-IND-103 | P1-003 | Q-IND-004 | |
| Q-SEL-101 | P1-003 | Q-SEL-001 | fundida |
| Q-SEL-102 | P1-003 | Q-SEL-002 | |
| Q-SEL-103 | P1-003 | Q-SEL-003 | |
| Q-WND-101 | P1-003 | Q-WND-004 | |
| Q-CASE-101 | P1-003 | Q-CASE-003 | |
| Q-CASE-102 | P1-003 | Q-CASE-004 | |
| Q-CASE-103 | P1-003 | Q-FST-001 | fundida |
| Q-CASE-104 | P1-003 | Q-CASE-006 | |
| Q-CASE-105 | P1-003 | Q-CASE-007 | |
| Q-JWL-101 | P1-003 | Q-JWL-001 | fundida |
| Q-SHK-101 | P1-003 | Q-SHK-001 | fundida |
| Q-DOC-101 | P1-003 | Q-DOC-005 | |
| Q-DOC-102 | P1-003 | Q-DOC-006 | |
| Q-DOC-103 | P1-003 | Q-IMG-007 + Q-BASE-005 | limite do corpus separado da consequência sobre a platina |
| Q-IMG-001 | P1-004 | Q-IMG-001 | = |
| Q-IMG-002 | P1-004 | Q-IMG-002 | = |
| Q-IMG-003 | P1-004 | Q-IMG-003 | = |
| Q-IMG-004 | P1-004 | Q-CASE-002 | é pergunta sobre a caixa, não sobre a imagem |
| Q-IMG-005 | P1-004 | Q-TRN-005 | idem, sobre o trem |
| Q-IMG-006 | P1-004 | Q-IMG-004 | |
| Q-IMG-007 | P1-004 | Q-IMG-005 | |
| Q-IMG-008 | P1-004 | Q-IMG-007 | fundida com Q-DOC-103 |
| Q-IMG-009 | P1-004 | Q-IMG-006 | |

### Questões novas, abertas por esta síntese

| Novo | Por quê |
|---|---|
| Q-CASE-005 | A estrutura "corpo + tampa" com nervura periférica (CLM-0431, CLM-0434) nunca tinha virado questão, e define a seção da borda que a Fase 4 precisa desenhar. |
| Q-CRY-003 | O assentamento e a vedação dos cristais são interface, não acabamento, e entram no Z-budget. |
| Q-BASE-004 | O contorno da platina com o prolongamento esquerdo é o primeiro alvo mensurável da Fase 5 e não tinha ID. |
| Q-BASE-005 | A consequência específica de não existir imagem do lado do mostrador. |
| Q-BRG-001, Q-BRG-002 | O subsistema BRG não tinha nenhuma questão aberta, apesar de a contagem e a identidade das pontes serem pré-requisito da Fase 5. |
| Q-BAR-005 | A mola do barrilete é o modelo de engenharia da Fase 6 e não tinha endereço. |
| Q-WND-005 | O diâmetro e os dentes das coroas-roda são medíveis já na Fase 2 e faltavam. |
| Q-IND-005 | A interface ponteiro–roda substitui o canhão e precisa ser desenhada. |
| Q-FST-003 | Fixações internas (parafusos de ponte, pinos de centragem) não tinham questão. |
