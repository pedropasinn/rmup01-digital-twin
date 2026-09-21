# ARCHITECTURE — decomposição funcional do RM UP-01 e do calibre RMUP-01

Produzido pela SÍNTESE DA FASE 1 em 2026-09-21, a partir dos quatro pacotes `TASK-P1-001`…`TASK-P1-004`.
Corresponde ao entregável "decomposição funcional" da **Fase 2** do `CLAUDE.md` §8.

> **Gate da Fase 2:** nenhum mecanismo pode existir no CAD sem função documentada ou status explícito de
> hipótese. Este documento é o registro desse status. Toda peça listada aqui tem `part_id` permanente em
> `engineering/bom-reconstructed.csv`; toda interface tem `interface_id` em `engineering/interfaces.csv`.
> Peça sem evidência entra com `status: hypothetical` e classe E — nunca some da lista e nunca vira fato
> por repetição.

---

## 1. O que a Fase 1 mudou na arquitetura a modelar

Cinco achados obrigam a desenhar um relógio diferente do que o `CLAUDE.md` §2 descrevia. Três vieram das
fontes primárias, um da imprensa japonesa e inglesa, um do próprio corpus de imagens.

**(a) Não existe haste de corda.** O diâmetro mínimo de 1,5 mm de uma tige de remontoir não cabe num relógio
de 1,75 mm, então as duas coroas frontais foram integradas à caixa **como rodas do próprio calibre**
(CLM-0036, Boillat: "the crowns … are neither more nor less than the wheels of the calibre itself").
Consequência: toda a Fase 8 se desenha a partir de dois eixos verticais curtos atravessando a luneta, não a
partir de um remontoir clássico com pignon coulant, bascule e tirette. As peças canônicas do remontoir
(tige, pignon coulant, renvoi, tirette, sautoir) **não devem ser criadas por analogia**.

**(b) Os ponteiros são decalcados diretamente sobre as rodas, sem canhão.** CLM-0037, confirmado
visualmente em IMG-0030 (ponteiro de perfil sobre a pinça) e IMG-0031 (acoplamento ponteiro–roda). O motion
works tradicional — canhão de minutos com roda das horas empilhada — **não existe**. A relação 12:1 tem de
estar em outro lugar, no plano (Q-IND-001), e os dois ponteiros podem não ser coaxiais (Q-IND-002).

**(c) O barrilete é periférico e também é patenteado.** Não há receptáculo acima nem abaixo: o tambor é
retido só pela periferia, por quatro apoios (buchas de berílio-cobre segundo a Chronos, roletes segundo a
Hodinkee — Q-BAR-002). A marca chama o barrilete de "patenteado", mas a família de patentes correspondente
não foi localizada (Q-BAR-004). Arquitetonicamente isto libera toda a altura do andar do barrilete para a
largura da mola, que é o que compra as 45 h.

**(d) Existe uma roda intermediária de transmissão entre barrilete e segunda roda** (CLM-0406). O solver do
trem precisa admitir esse estágio extra desde o início; aritmeticamente ele se comporta como *idler*
(razão aparentemente 1:1, Q-TRN-004), o que é compatível com a razão total exigida — ver
`CAD-RECONSTRUCTION-PLAN.md` §7.

**(e) O banking do escape é sólido, contra um entalhe usinado na platina** (CLM-0412), e o pivô da âncora
fica **entre as duas pedras** (CLM-0413). Nenhuma das duas coisas está na patente, que prevê goupilles de
limitação (reiv. 10). As três descrições — entalhe na platina, goupilles da patente, "função de banking
levada à forquilha" do press kit — precisam ser conciliadas antes de qualquer simulação (Q-ESC-004).

**(f) E uma sexta, de método:** o cristal das horas está contestado entre 0,45 mm e 0,20 mm (Q-CRY-001), e
boa parte do material visual oficial é render, não fotografia (DEC-003). A arquitetura abaixo distingue,
em cada nó, o que se vê numa fotografia ou num quadro de filme do que se vê apenas num render.

---

## 2. A árvore

Notação por nó: **função** · **peças** (com `part_id`) · **visibilidade** (visível / parcial / oculta, com
a imagem que mostra) · **classe de evidência** do que se sabe · **âncoras** que restringem o nó.

```text
watch
├── case ........................... caixa monobloco + luneta + insertos + fixações
├── crystals ....................... cristal das horas + cristal do balanço
├── movement (calibre RMUP-01)
│   ├── baseplate .................. platina esqueletada Ti Gr5, 41,45 × 28,85 mm
│   ├── bridges .................... ponte do trem (3 braços, 3 rubis) + ponte do balanço + ?
│   ├── barrel ..................... tambor periférico, arbor, mola, 4 apoios
│   ├── winding .................... 2 coroas-roda + roda de coroa + cliquet + limitador de torque
│   ├── function selector .......... braço deslizante W/H + came + mola de posição
│   ├── going train ................ intermediária → 2ª → 3ª → (4ª?) → roda de escape
│   ├── escapement ................. roda de escape + âncora sem dardo + 2 pedras + plateau + cheville
│   ├── oscillator ................. balanço Ti Gr5 3 braços + 6 massas + eixo + espiral AK 3
│   ├── motion works / indication .. rodas porta-ponteiro + razão 12:1 + 2 ponteiros lâmina
│   ├── jewels ..................... 23 rubis (distribuição desconhecida)
│   ├── shock protection ........... Kif (quantidade e posição desconhecidas)
│   └── fasteners .................. parafusos de ponte + pinos de centragem
└── strap interface ................ orelhas integradas + pulseira, presas pelos mesmos 13 parafusos
```

---

## 3. Nó a nó

### 3.1 `case` — caixa

**Função.** Alojar o movimento como porta-movimento, formar com ele um corpo rígido único, garantir 1 atm,
carregar os dois comandos frontais e ancorar a pulseira. A caixa **não** faz as vezes de platina: a marca é
explícita e contrasta o próprio projeto com as soluções em que o fundo vira platina (CLM-0031).

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Carrura + fundo monobloco Ti Gr5 | PRT-CASE-001 | visível | IMG-0004, IMG-0010, IMG-0034 | A (existência, material) / C a medir |
| Luneta com quatro aberturas | PRT-CASE-002 | visível | IMG-0004, IMG-0006, IMG-0009 | A/B |
| Junta perimetral | PRT-CASE-003 | parcial | IMG-0004 (explodida) | B |
| Insertos de cerâmica preta (×2) | PRT-CASE-004 | visível | IMG-0006, IMG-0032 | A |
| Nervura periférica de espessura integral | PRT-CASE-005 | oculta | — (SRC-0403, texto) | D |
| Cilindro roscado central caixa↔movimento | PRT-CASE-006 | oculta | procurar em IMG-0026 | B (existência) / E (posição) |
| Rebaixo interno que recebe barrilete e trem | PRT-CASE-007 (feature) | oculta | IMG-0027 (degrau) | B (existência) / F (profundidade) |

**Âncoras que restringem.** Caixa 51,00 × 39,00 × 1,75 mm (A). Parede mínima 0,18 mm em pontos não
especificados (A). 13 parafusos spline Ti Gr5 com arruelas 316L, que prendem caixa **e** pulseira (A).
1 atm / 10 m (A). Não deforma sob ~12 kg na periferia (A, via entrevista japonesa). Ponto de partida formal
declarado: o tonneau do RM 67-01, alongado no segmento 3h–9h, com espessura inicialmente fixada em 3 mm (A).

**O que não se sabe.** Onde estão os 0,18 mm (Q-CASE-001); em que ponto do contorno curvo valem os 1,75 mm
(Q-CASE-002); a profundidade do rebaixo (Q-CASE-003); a posição do cilindro roscado (Q-CASE-004); onde fica
a linha de junção corpo/tampa (Q-CASE-005).

### 3.2 `crystals` — cristais

**Função.** Fechar as duas aberturas superiores; possivelmente participar da rigidez da caixa (H-CASE-101);
possivelmente servir de apoio ao eixo da indicação (CLM-0420).

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Cristal das horas, safira 1 800 Vickers | PRT-CRY-001 | visível | IMG-0009, IMG-0036 | A (material, AR nos dois lados) / **contested** na espessura |
| Cristal do balanço, 0,20 mm centro / 0,30 mm borda | PRT-CRY-002 | visível | IMG-0009, IMG-0036 | A |

**Âncoras.** 0,45 mm (ficha técnica, contestada por "2/10 mm" na narrativa — Q-CRY-001); 0,20/0,30 mm
(superfície **não plana**: o cristal do balanço é mais espesso na borda que no centro); antes deste modelo o
cristal mais fino da marca tinha 0,8 mm.

**Consequência de projeto.** Os dois cristais têm espessuras diferentes e provavelmente **alturas de
assentamento diferentes**; isso é uma previsão testável, ver `CAD-RECONSTRUCTION-PLAN.md` §4.

### 3.3 `baseplate` — platina

**Função.** Suportar todos os centros de rotação, os recortes que alojam as duas coroas, o entalhe de
banking da âncora, a abertura do barrilete e o furo do parafuso central de caixa.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Platina esqueletada Ti Gr5 (90/6/4) | PRT-BASE-001 | **visível nua** | **IMG-0026** (t = 25,42 s do filme) | A (material, acabamento) / B (topologia) |

**Âncoras.** 41,45 × 28,85 mm; 1,18 mm de espessura **do calibre inteiro**, não da platina; liga 90% Ti,
6% Al, 4% V; platina retificada à mão e jateada a úmido; validada em ensaios separados; pivôs brunidos e
escareados polidos a diamante **do lado das pontes**.

**IMG-0026 é a peça central de todo o projeto.** É a única imagem pública em que os furos de pivô do lado do
trem não estão cobertos por pontes, e o suporte de montagem — hastes retas e paralelas de fábrica — dá o
plano de referência para a homografia. Toda a Fase 5 se apoia nela.

**O que não se sabe.** A espessura da platina (Q-BASE-003); o contorno exato com o prolongamento esquerdo
(Q-BASE-004); **o que existe na face voltada para o mostrador** (Q-BASE-005) — não há uma única imagem
pública desse lado com as rodas montadas.

### 3.4 `bridges` — pontes

**Função.** Fechar os mancais superiores do trem e do oscilador. O barrilete, notavelmente, **não tem
ponte** — é retido pela periferia (CLM-0401), e essa ausência é decisão de arquitetura, não lacuna.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Ponte esqueletada de 3 braços, 3 mancais rubinados, 2 parafusos + 1 pino | PRT-BRG-001 | **isolada** | IMG-0003 (foto) + IMG-0028 (filme, 2º ângulo) | B |
| Ponte do balanço (superior, 3 braços segundo SRC-0400) | PRT-BRG-002 | parcial | IMG-0001 (render), IMG-0029 | E na geometria; B na existência |
| Ponte/cobertura do caminho de corda | PRT-BRG-003 | oculta | — | E |
| Ponte do barrilete | — | **não existe** | CLM-0401 | D (ausência declarada por observação) |

**Par de vistas.** IMG-0003 + IMG-0028 mostram **a mesma peça rígida em dois ângulos**: os três centros
rubinados têm distância invariante e são recuperáveis por reconstrução de duas vistas. É o primeiro
subconjunto do projeto que pode ser resolvido metrologicamente de ponta a ponta.

### 3.5 `barrel` — barrilete e fonte de energia

**Função.** Armazenar a energia de 45 h ± 10%, girando uma volta a cada 6 h — 7,5 voltas úteis.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Tambor dentado esqueletado | PRT-BAR-001 | parcial | IMG-0029 (dentado), IMG-0001 (render) | B |
| Arbor | PRT-BAR-002 | oculta | — | E |
| Tampa do barrilete | PRT-BAR-003 | oculta | — | E — **pode não existir** na forma clássica |
| Mola principal, lâmina extremamente fina | PRT-BAR-004 | oculta | — | A (existência) / E (geometria) |
| Apoios periféricos (×4?), BeCu | PRT-BAR-005 | parcial | foto dedicada da Hodinkee | B / **contested** (rolete × bucha) |

**Âncoras.** 6 h por volta, valor **exato** e não aproximado ("6 hours per revolution instead of 7.5 hours");
45 h ± 10% (40,5–49,5 h); espessura < 1,18 mm (limite trivial); dentado com involuta central e ângulo de
pressão de 20°; barrilete declarado patenteado.

**Consequência.** Suprimir receptáculo acima e abaixo converte altura em largura de mola. A retenção axial
do arbor passa a ser um problema de montabilidade em aberto (Q-BAR-003) e não pode ser resolvida no CAD por
um pivô inventado sem status.

### 3.6 `winding` — corda

**Função.** Levar torque da coroa inferior (7h–8h) até o barrilete quando o seletor está em W, com
limitador de torque contra corda forçada.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Coroa-roda de execução (7h–8h) | PRT-WND-001 | visível | IMG-0004 (isolada), IMG-0006, IMG-0032 | A/B |
| Coroa-roda de seleção (10h–11h) | PRT-WND-002 | visível | idem — **mesmo desenho** (CLM-0709) | A/B |
| Roda de coroa | PRT-WND-003 | **visível montada** | IMG-0026 (prolongamento esquerdo) | B, identificação funcional `provisional` (Q-IMG-005) |
| Roda de cliquet | PRT-WND-004 | **visível montada** | IMG-0026 | B, idem |
| Cliquet + mola de retenção | PRT-WND-005 | oculta | — | E |
| Limitador de torque | PRT-WND-006 | oculta | — | A (existência) / E (princípio) |
| Ferramenta spline dedicada | PRT-WND-007 | externa | SRC-0409 | A |
| Aro de cerâmica de vedação | PRT-WND-008 | parcial | IMG-0006 | B |

**Âncoras.** Não há tige (o mínimo de 1,5 mm não cabia); os dois comandos têm o mesmo desenho estriado com
encaixe spline central; insertos de cerâmica preta asseguram a estanqueidade; a coroa listada na ficha
técnica é "316L com DLC", o que ainda não se sabe a que peça se refere (Q-WND-002).

### 3.7 `function selector` — seletor W/H

**Função.** Escolher, girando a coroa superior, se a coroa inferior dá corda (W) ou acerta a hora (H);
em H, **desacoplar o barrilete** para que acertar não torça a mola.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Braço deslizante | PRT-SEL-001 | parcial | stills do filme (SRC-0400/0401) | B |
| Came ou excêntrico do seletor | PRT-SEL-002 | oculta | — | E |
| Mola de posicionamento / detent | PRT-SEL-003 | oculta | — | E |

**Âncoras.** O seletor fica na luneta entre 10h e 11h; a execução fica entre 7h e 8h; girar o seletor
desloca o braço — para um lado engata a corda, para o outro o acerto (CLM-0422). O gate da Fase 8 é duro:
não basta parecer igual na posição neutra, os dois estados têm de ser cinematicamente coerentes.

**Nota de patente.** A EP4295198B1 (Papi + Fernandez, prioridade 16/02/2021) protege um órgão único de
comando com duas ou três posições angulares estáveis de seleção. O modo de realização descrito é de
cronógrafo, com coroa de saia e tige. **É parente conceitual, não prova** (H-SEL-010, Q-SEL-004).

### 3.8 `going train` — trem de marcha

**Função.** Transmitir o torque do barrilete até a roda de escape com a razão que sustenta 4 Hz.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Roda intermediária de transmissão | PRT-TRN-001 | parcial | SRC-0403 (texto), centros em IMG-0026 | B |
| Segunda roda + pinhão | PRT-TRN-002 | parcial | foto da Chronos (na pinça) | B |
| Terceira roda + pinhão | PRT-TRN-003 | oculta | — | D |
| Roda de escape + pinhão | PRT-TRN-004 / PRT-ESC-001 | parcial | still alavanca+roda (SRC-0400) | B |

**Âncoras.** 28 800 A/h = 4 Hz; barrilete a 1 volta/6 h; involuta central com 20° de pressão declarada para
o dentado do barrilete e o pinhão da "terceira" roda — com a nomenclatura divergindo entre idiomas
(Q-TRN-001); rodas com chanfro côncavo a diamante, ródio aplicado **antes** de cortar os dentes e correções
mínimas para preservar a geometria; o trem inteiro fica à direita do barrilete e é **completamente coberto
pela caixa superior**, o que significa que no relógio montado ele é invisível.

**Restrição aritmética.** Razão total barrilete→escape = 5 760 se a roda de escape tiver 15 dentes, 4 800
com 18, 4 320 com 20 (dedução em `CAD-RECONSTRUCTION-PLAN.md` §7). Nenhum número de dentes é publicado em
nenhum idioma: tudo virá do `gear_search` sob restrição de centros medidos.

### 3.9 `escapement` — escape ultraplano patenteado

**Função.** Travar, destravar e dar impulso ao oscilador 4 vezes por segundo, com 54° de levantamento e sem
as duas peças que mais somam altura num escape suíço.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Roda de escape, dentes em clave | PRT-ESC-001 | parcial | still da Hodinkee | B |
| Âncora sem dardo, fourchette alongada, cornes modificadas | PRT-ESC-002 | parcial | still da Hodinkee; IMG-0026 (entalhe) | A (topologia) / E (silhueta) |
| Pedra de entrada | PRT-ESC-003 | oculta | — | A (existência) / E (geometria) |
| Pedra de saída | PRT-ESC-004 | oculta | — | idem |
| Plateau único com parede anti-renversement e entalhe | PRT-ESC-005 | oculta | — | D (via patente) |
| Cheville (pedra de impulso) | PRT-ESC-006 | oculta | — | D |
| Entalhe de banking na platina | PRT-ESC-007 (feature) | parcial | IMG-0026 | B |
| Dardo / guard pin | — | **não existe** | CLM-0410 | A |
| Pequeno plateau / safety roller | — | **não existe** | CLM-0410 | A |

**Âncoras e fonte de topologia.** A família CH 832/2019 (EP3754433B1 concedida em 27/05/2026, US11550262B2,
CH716337A1, HK40033669A, JP7537920B2, CN112114508B), inventor Giulio Papi, titular Audemars Piguet. A
reivindicação 1 dá a topologia: plateau único no mesmo nível da cheville; periferia cilíndrica do plateau
como parede anti-renversement com um entalhe; as duas cornas batendo nessa parede; e a condição
caracterizante de que cada corna só entra no entalhe quando a cheville já está dentro da forquilha.
A reiv. 2 dá a desigualdade geométrica que evita o travamento em rebat — a falha do CH44855 de 1909.
A reiv. 3 dá o perfil da parede externa da corna (porção tangente + porção a 0–45°). As reivs. 4 e 5 dão as
duas variantes de fixação da cheville (plateau × **balanço**). As reivs. 7 e 8 dão os modos preferidos de
arquitetura (razão ≥ 2 entre distâncias de centros; três centros coplanares), explicitamente não obrigatórios.

> **Regra dura, repetida aqui de propósito:** desenho de patente não é desenho em escala. Nenhuma dimensão
> sai das figuras. A figura 5 mostra várias formas alternativas de âncora dentro da mesma invenção — a
> silhueta da âncora do RMUP-01 **tem de vir de fotografia**, não da figura.

**A identificação do escape do RMUP-01 com esta família é classe D**, não A: nenhum documento liga os dois
(H-ESC-010).

### 3.10 `oscillator` — balanço, espiral e choque

**Função.** Oscilar a 4 Hz com 3 mg·cm² de inércia e permitir regulagem sem raquete.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Balanço Ti Gr5, 3 braços, com degrau | PRT-OSC-001 | parcial | IMG-0029, IMG-0036 | A (material/3 braços) / B (degrau) |
| Massas de regulagem (×6) | PRT-OSC-002 | parcial | IMG-0036 | A |
| Eixo do balanço | PRT-OSC-003 | oculta | — | E |
| Espiral AK 3, plana (sem overcoil) | PRT-OSC-004 | oculta | — | A (produto) / B (plana) / E (geometria) |
| Virola / ponto de fixação | PRT-OSC-005 | oculta | — | E |
| Piton / porta-espiral | PRT-OSC-006 | oculta | — | E |
| Kif | PRT-SHK-001 | oculta | — | A (existência) / E (modelo, quantidade, posição) |

**Âncoras.** 3 mg·cm²; 54° de levantamento; 4 Hz; três braços; seis massas; sem índice de raquete; espiral
AK 3; Kif; titânio grau 5 — primeiro balanço em titânio da marca. A espiral é **plana**, não overcoil, por
imposição de altura (CLM-0416); os braços têm **um degrau** que aproxima a espiral do plano do balanço
(CLM-0417), e esse degrau é ganho de altura que tem de aparecer no Z-budget.

**Equação com muitas incógnitas.** 3 mg·cm² e 4 Hz restringem o produto inércia × rigidez, não o diâmetro,
nem a seção dos braços, nem a massa individual dos seis pesos. Manter conjunto de soluções (Q-OSC-001).

### 3.11 `motion works / indication` — indicação

**Função.** Levar a energia até dois ponteiros, com 1 volta/h no minuto e 1 volta/12 h na hora, **sem
canhão e sem empilhamento**.

| Peça | `part_id` | Visibilidade | Onde se vê | Classe |
|---|---|---|---|---|
| Roda porta-ponteiro dos minutos | PRT-IND-001 | parcial | IMG-0031 | B |
| Roda porta-ponteiro das horas | PRT-IND-002 | parcial | IMG-0031 | B |
| Ponteiro das horas (lâmina plana) | PRT-IND-003 | visível | IMG-0030, IMG-0036 | A/B |
| Ponteiro dos minutos (lâmina plana) | PRT-IND-004 | visível | IMG-0030, IMG-0036 | A/B |
| Roda(s) da razão 12:1 | PRT-IND-005 | oculta | — | E |
| Marcação das horas 12/3/6/9 | PRT-IND-006 | visível | IMG-0036, IMG-0009 | B |

**Âncoras.** Ponteiros decalcados diretamente sobre as rodas, para eliminar os canhões e ganhar espessura
(A, com confirmação visual). "Gears e ponteiros sobrepostos eram impossíveis" (A, Arbona).

**Três questões encadeadas.** Os ponteiros são coaxiais (Q-IND-002)? Onde está o 12:1 (Q-IND-001)? Existe um
trem de indicação independente acionado pelo barrilete (Q-IND-003, H-IND-101)? A primeira é resolvível por
**uma única fotografia frontal** e deve ser feita primeiro, porque restringe as outras duas. A terceira é a
suposição mais sedutora do corpus e a mais fácil de virar "fato" por repetição: é de um jornalista
competente que diz explicitamente que está supondo. Classe E em todas as fases.

### 3.12 `jewels`, `shock protection`, `fasteners`

- **23 rubis** publicados (A). Distribuição não publicada, e nenhuma imagem os mostra simultaneamente
  (Q-JWL-001). Rubis soltos aparecem em IMG-0005; três rubis embutidos na ponte de 3 braços em IMG-0003.
  O §17 admite duas saídas: localizar os 23, ou **documentar explicitamente** quais não foram localizados.
- **Kif** (A). Modelo, quantidade e posição desconhecidos (Q-SHK-001).
- **Fixações internas**: parafusos de ponte e pinos de centragem — a ponte de 3 braços tem dois furos de
  parafuso e um furo liso (CLM-0706). Nada publicado (Q-FST-003).

### 3.13 `strap interface`

**Função.** Ancorar a pulseira à caixa. Os mesmos 13 parafusos spline prendem componentes da caixa **e** a
pulseira (A, Boillat) — ou seja, a interface de pulseira não é um subsistema separável do fecho da caixa.
Nenhuma fonte primária localizada descreve a geometria (Q-STR-001).

---

## 4. Mapa de centros — o que a Fase 2 entrega à Fase 5

Os centros de rotação conhecidos ou localizáveis hoje, em ordem de confiança:

| Centro | Onde é medível | Confiança |
|---|---|---|
| Barrilete | IMG-0026 (abertura na platina nua), confirmável em IMG-0001 | **máxima** |
| Roda de coroa e roda de cliquet | IMG-0026, com as rodas montadas | máxima |
| Furos de pivô do lado do trem/escape | IMG-0026 — os únicos não cobertos por pontes em todo o corpus | máxima |
| Balanço | IMG-0001 (render — precisa do teste de fidelidade antes), IMG-0029, IMG-0036 | alta, condicionada a Q-IMG-003 |
| Dois comandos frontais | IMG-0004, IMG-0006 (macro) | alta |
| Três mancais da ponte de 3 braços | IMG-0003 + IMG-0028, por duas vistas | alta |
| Rodas porta-ponteiro | IMG-0031, IMG-0036 | média |
| Âncora e roda de escape | still da Hodinkee; nenhuma imagem dedicada | baixa |

**Nenhum centro é conhecido hoje em milímetros.** Tudo acima é "medível", não "medido": a Fase 1 não fez
metrologia. Essa é a primeira coisa que a Fase 2 executável (TASK-P2-001, -002, -005) tem de mudar.

---

## 5. O que este documento deliberadamente não afirma

1. **Que o render oficial é fiel.** IMG-0001 é a vista mais informativa do calibre e é um render. Tudo que
   depende só dele está marcado E. O teste que decide está em TASK-P2-001.
2. **Que existe um trem de indicação independente.** É hipótese de terceiro (H-IND-101), não observação.
3. **Que o escape do RMUP-01 é a família de 2019.** É inferência forte (D), não fato.
4. **Que os apoios do barrilete giram.** "Rolete" e "bucha" são duas leituras; H-BAR-101 propõe que sejam a
   mesma peça, e a diferença muda contagem de peças, de rubis e de montagem.
5. **Qualquer dimensão interna.** Nenhum número de dentes, módulo, diâmetro de roda, distância entre
   centros ou espessura de peça interna existe em fonte pública, em nenhum idioma. Todos virão de
   metrologia de imagem e dos solvers, e nascerão classe C ou D com incerteza registrada.
