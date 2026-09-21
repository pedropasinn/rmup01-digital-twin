# Árvore de patentes — RM UP-01 / calibre RMUP-01

Pacote TASK-P1-002, levantado em 20–21/09/2026. Bloco de IDs: SRC-0200…, CLM-0200…, EVD-0200….
Arquivos locais em `research/patents/`; metadados linha a linha em `research/patents/patents.csv`;
fontes em `research/source-manifest.csv`.

> **Regra que vale para todo este documento.** Desenho de patente — e também desenho de registro de
> desenho industrial — **não é desenho em escala**. Nada aqui autoriza extrair milímetros. O que as
> patentes dão é **topologia, função, sequência de contatos e relações qualitativas ou relativas**.
> Onde um número aparece abaixo, ele é literal do texto da patente (ângulo declarado, razão declarada),
> nunca medido de figura, e vale para a invenção, não necessariamente para o calibre RMUP-01.

---

## 1. Visão geral

```text
FAM-ESC-PAPI-2019 — escape a âncora sem dardo (prioridade CH 832/2019, 19/06/2019)
│  titular: Manufacture d'Horlogerie Audemars Piguet SA (Le Brassus)
│  inventor: Giulio Papi (La Chaux-de-Fonds)
│  mandatário: e-Patent SA, Neuchâtel
├── CH716337A1  depósito de prioridade, publicado 30/12/2020            [PDF local]
├── EP3754433A1 pedido EP, publicado 23/12/2020                          [PDF local]
│    └── EP3754433B1 concedida, menção 27/05/2026 (Bulletin 2026/22)     [PDF local]
├── US11550262B2 concedida 10/01/2023 (texto de trabalho, em inglês)     [PDF local]
├── HK40033669A publicado 16/04/2021                                     [PDF local]
├── JP7537920B2 concedida 21/08/2024        (listagem de família; não conferida no J-PlatPat)
└── CN112114508B concedida 25/07/2023       (listagem de família; não conferida no CNIPA)

FAM-CMD-PAPI-2021 — órgão único de comando de várias funções (prioridade CH 150/2021, 16/02/2021)
│  titular: Audemars Piguet; inventores: Giulio Papi e José-Manuel Fernandez
├── PCT/EP2022/051007 → WO 2022/175002 (25/08/2022)
├── EP4295198A1 publicado 27/12/2023
│    └── EP4295198B1 concedida, menção 18/02/2026 (Bulletin 2026/08)     [PDF local]
└── CH718513A1 "Device for selecting and actuating several functions of a watch movement"
     — localizado por busca, dados bibliográficos NÃO conferidos (Q-SEL-003)

FAM-DES-UP01-2021 — registro de desenho do relógio ultraplano (Haia DM/218823, 28/10/2021)
│  titular: Turlen Holding SA (veículo de PI da Richard Mille); autor: Richard Mille
├── USD991795S1 concedido 11/07/2023, 10 pranchas, 6 vistas ortogonais    [PDF local]
└── candidatos irmãos na mesma data de depósito, ainda não conferidos visualmente:
     TWD222805S, TWD222806S, TWD222807S, CA208187S, CA210542S, ZAA202200456S (Q-CASE-002)

NÃO LOCALIZADOS (a imprensa afirma existirem; nenhum número encontrado)
├── barrilete ultraplano "patenteado"                                    → Q-BAR-001
├── balanço de inércia variável ultraplano "patenteado"                  → Q-OSC-001
└── qualquer patente de utilidade em nome de Richard Mille / Turlen sobre caixa-movimento → Q-CASE-003
```

---

## 2. FAM-ESC-PAPI-2019 — o escape sem dardo

### 2.1 O que o documento é

Família de um só inventor (Giulio Papi) e um só titular (Audemars Piguet), nascida do depósito suíço
CH 832/2019 de 19/06/2019, com relatório de busca suíço de 15/10/2019. Classificação CPC G04B15/08
(escapes de âncora) e G04B15/14 (peças de escape). O texto de trabalho do projeto é o US11550262B2,
por estar em inglês e trazer descrição e figuras completas; o EP3754433B1 é a versão concedida na
Europa e é a referência para o **escopo** reivindicado.

Arte citada contra a família: CH2209 (1890), CH44855 (1909), CH567293, CH699273, DE867671,
GB679416, JP2002-228767, US2010/0208555, US2015/0103637, US2015/0268631, EP2924517.
O próprio texto trata CH44855 (1909) como o ancestral direto: um escape sem dardo, mais fino, que
nunca se firmou no mercado por risco de travar em situação de rebat (*knocking*).

### 2.2 Reivindicação 1, em linguagem própria

Um conjunto de escape a âncora formado por **âncora sem dardo** (palheta de entrada, palheta de saída
e forquilha com duas cornas), **um plateau** e **uma cheville presa ao plateau**, em que:

- o plateau fica, ao menos em parte, **no mesmo nível da cheville** na direção da espessura — ou seja,
  plateau único, e não o par plateau grande + plateau pequeno do escape suíço clássico;
- a periferia cilíndrica do plateau é uma **parede anti-renversement** com **um entalhe** junto à cheville;
- em serviço, essa parede serve de **batente para as duas cornas** (é ela que impede o renversement,
  papel que no escape suíço cabe ao dardo);
- e — aqui está o caracterizante — **cada corna só consegue entrar no entalhe quando a cheville já está,
  pelo menos em parte, dentro da entrada da forquilha**.

### 2.3 Reivindicações dependentes que interessam à reconstrução

- **Condição geométrica anti-travamento (reiv. 2):** em situação de rebat, a distância entre o ponto de
  contato da cheville na parede externa da corna e a extremidade dessa parede mais próxima da parede
  interna é **maior** que a distância entre a cheville e a junção parede/entalhe mais próxima daquela
  corna. É essa desigualdade que impede a corna de cair dentro do entalhe quando o balanço inverte o
  sentido — a falha do CH44855.
- **Perfil da parede externa da corna (reiv. 3):** a partir da extremidade vizinha da parede interna,
  primeiro uma **porção de segurança sensivelmente tangente** à parede anti-renversement; depois uma
  segunda porção a **0°–45° em relação à baguette** da âncora (a descrição fala em "da ordem de 0 a 60°,
  de preferência menos de 45°, por exemplo 30°"), estendendo-se ao menos até o ponto de contato da
  cheville em rebat. Efeito declarado: atrito baixo no apoio e cornas mais largas, logo menos frágeis.
- **Fixação da cheville (reiv. 4 e 5):** por um **suporte feito de uma peça com o plateau** (na descrição,
  a pequena saliência radial 28), **ou** por um suporte que é **o próprio balanço** — isto é, a cheville
  pode ser carregada diretamente pelo balanço, o que suprime mais uma peça na pilha vertical.
- **Arquitetura (reiv. 7):** distância entre eixos **âncora↔plateau ≥ 2 ×** distância entre eixos
  **âncora↔roda de escape**.
- **Arquitetura (reiv. 8):** eixos da **roda de escape, da âncora e do plateau coplanares**.
  A descrição diz expressamente que podem ser coplanares **ou não** sem sair da invenção: logo, 7 e 8
  são modos preferidos, não obrigações.
- **Reiv. 10:** o movimento pode ter **goupilles de limitação** (banking pins) de um lado e de outro da
  âncora para definir o debate máximo. Importante: na patente os **banking pins continuam existindo**;
  o que foi eliminado é o dardo e o plateau duplo.

### 2.4 O que a patente ensina sobre topologia (e o preço que ela cobra)

1. O escape perde **dardo** e **plateau pequeno/duplo**; a segurança contra renversement migra para as
   **cornas** (parede externa) contra a **periferia do plateau**.
2. Consequência dimensional declarada, sem números: como as cornas são **mais largas** que um dardo,
   o **entalhe precisa ser maior** e o **plateau precisa crescer**; para manter o ângulo de debate da
   âncora com a mesma roda de escape, a **baguette (haste) da âncora precisa alongar**. Isto é: o escape
   fica mais fino às custas de ficar **mais comprido no plano** — exatamente a troca que um calibre de
   1,18 mm espalhado em 41,45 × 28,85 mm pode pagar.
3. Desengate, impulso e segurança passam a acontecer **no mesmo nível vertical** (parede interna e
   parede externa da mesma corna), enquanto no escape suíço o dardo trabalha num nível diferente das
   cornas. É esta a explicação mecânica da redução de altura.
4. Ganho funcional declarado: no rebat, o alongamento do balanço pode passar de **360° + β** (β de
   alguns graus), contra 330–340° do escape suíço — argumento de isocronismo, não de altura.
5. A figura 5 mostra **várias formas alternativas de âncora** dentro da mesma invenção: a patente
   assume explicitamente que a forma exata da forquilha é livre. Portanto a silhueta da âncora do
   RMUP-01 **não pode ser copiada da figura**; tem de vir de fotografia.

### 2.5 Figuras e para que servem

| Figura | Conteúdo | Uso legítimo | Uso proibido |
|---|---|---|---|
| 1a / 1b | vista de cima, escape suíço (1a) × invenção (1b) | comparar topologia e o alongamento da baguette | medir centros, módulo, raio do plateau |
| 2a / 2b | vista lateral parcial dos mesmos conjuntos | entender **quais** níveis somem na pilha vertical | ler espessuras |
| 3a–3n | ciclo completo: repouso, entrada da cheville, desengate, impulso, ponto morto, locking, saída | construir a máquina de estados do escape e o teste lock/unlock/impulse/drop | ângulos de levantamento, de repouso, de drop |
| 4a / 4b / 4c | rebat no CH44855, no escape suíço e na invenção | entender a condição da reiv. 2 e por que a corna não entra no entalhe | o "330–340°" e o "360°+β" são do texto, não das figuras |
| 5 | catálogo de âncoras alternativas | lembrar que a forma é livre | tratar qualquer delas como a âncora do RMUP-01 |

### 2.6 O que NÃO se pode extrair

- Nenhuma dimensão: nem diâmetro de plateau, nem raio de cheville, nem comprimento de baguette, nem
  espessura de nada. As figuras são esquemáticas e a própria descrição as chama de simplificadas.
- Número de dentes da roda de escape: a roda aparece só como contorno e nem é desenhada nas figs. 3.
- Ângulo de levantamento: os 54° publicados pela Richard Mille são dado de marca (a confirmar em
  P1-001), não da patente.
- Que este escape **seja** o escape do RMUP-01. A patente não cita Richard Mille nem o calibre.
  A ligação vem da descrição pública da marca (dardo e plateau de segurança eliminados, função de
  segurança levada à forquilha) e é, por enquanto, **inferência forte (D)**, não fato primário.

---

## 3. FAM-CMD-PAPI-2021 — comando/seleção de várias funções

EP4295198B1 (prioridade CH 150/2021, de 16/02/2021; PCT/EP2022/051007; WO 2022/175002) protege um
**órgão de comando único** — coroa + tige solidárias em rotação e em translação — em que:

- **rodar** a coroa aciona uma primeira função via a tige (reiv. 1);
- **premer** a coroa aciona uma segunda função distinta, por um segundo dispositivo de acionamento,
  e a mola devolve a coroa ao repouso;
- um **dispositivo de segurança** (encoche axial na saia da coroa + goupille fixa) impede premer fora
  da posição angular estável e impede rodar quando premida (reiv. 2 e 3);
- na variante das reivindicações 8 e 9 a primeira função é **função de seleção**, com **duas ou três
  posições angulares estáveis**, cada uma correspondendo a uma função selecionada.

O exemplo desenvolvido no texto é de **cronógrafo** (rotação = start/stop; pressão = remise à zéro /
flyback) — não é o seletor W/H do RM UP-01. O que torna a família interessante para nós é a data de
prioridade (fev/2021), o inventor comum e, sobretudo, a **gramática de projeto**: um só órgão frontal
com posições angulares estáveis de seleção, que é conceitualmente o que o RM UP-01 faz com o seletor
W/H. Tratar como **hipótese (E)**, registrada em H-SEL-001, e verificar CH718513A1 (Q-SEL-003).

---

## 4. FAM-DES-UP01-2021 — o registro de desenho do relógio

**USD991795S1** — "Watch", requerente **Turlen Holding SA** (Les Breuleux, CH), autor **Richard Mille**,
depósito 28/10/2021 pelo **registro internacional de Haia DM/218823** (publicado 29/04/2022),
concedido em 11/07/2023, 15 anos, 1 reivindicação e **10 pranchas**.

Identificação: as vistas mostram uma caixa oblonga achatada, sem coroa lateral, com **dois discos
moleteados** num dos lados, **indicação central de horas/minutos** com ponteiros e uma **abertura
circular com balanço de braços** do outro lado — a assinatura do RM UP-01. O próprio examinador citou,
como publicação relacionada, o artigo do Hodinkee "In-Depth The Richard Mille RM UP-01, A Very Deep
Dive On A Very Thin Watch" (13/07/2022). Identificação classificada **B (observada)**; virará A se o
registro de Haia DM/218823 for lido na base da OMPI (Q-CASE-001).

Vistas disponíveis: **1.1 frente, 1.2 verso, 1.3 direita, 1.4 esquerda, 1.5 inferior, 1.6 superior,
1.7–1.10 perspectivas**. É o conjunto ortográfico público mais completo encontrado até agora e será a
base de silhueta da Fase 4 — **por proporção relativa e por calibração contra dimensões publicadas**,
nunca por medida direta: desenho de registro também não é desenho em escala, e as pranchas ainda
passaram por digitalização e reimpressão.

Observação útil já visível nas vistas 1.4/1.5: a caixa aparece como uma **lâmina de espessura
praticamente constante**, com ressaltos discretos apenas nas regiões dos comandos — coerente com o
1,75 mm publicado, mas isso é coerência qualitativa, não medição.

Irmãos prováveis do mesmo depósito (28/10/2021, mesmo titular): TWD222805S, TWD222806S, TWD222807S,
CA208187S, CA210542S, ZAA202200456S. Não foram abertos um a um; USD989636S1, também de 28/10/2021,
foi aberto e **não** é o UP-01 (caixa tonneau clássica) — prova de que a data de depósito sozinha não
identifica o desenho.

---

## 5. Buracos conhecidos desta árvore

- **Barrilete ultraplano e balanço de inércia variável**: a comunicação da marca e a imprensa dizem
  "patenteado" para ambos; nenhuma patente correspondente foi localizada neste pacote. Pode ser (a)
  depósito suíço ainda não indexado nas bases consultadas, (b) titularidade em nome que não testamos,
  (c) uso comercial amplo da palavra "patenteado". Q-BAR-001 e Q-OSC-001.
- **Seletor W/H**: nenhuma patente específica identificada; EP4295198B1 é parente conceitual, não prova.
- **Cristais e montagem da caixa (13 parafusos spline)**: nada encontrado.
- **Busca por titular Richard Mille / Turlen Holding** só devolveu **desenhos industriais** — nenhuma
  patente de utilidade. Isso é consistente com o que se sabe da marca (desenvolvimento por parceiros
  como a Audemars Piguet Le Locle, que fica com as patentes), mas precisa de verificação independente.
- Bases que **não** puderam ser consultadas neste pacote: Espacenet, WIPO Patentscope, Swissreg e
  Justia bloquearam o acesso automatizado (403); o Google Patents passou a responder 503 no meio do
  trabalho. Ver o relatório do pacote.
