# SÍNTESE DA FASE 1 — resumo executivo para Pedro

21/09/2026 · sem commit · sem Codex · versão 0.1.0 do repositório

---

## Em uma página

A Fase 1 acabou e entregou mais do que se esperava dela. As 26 âncoras que você deixou no `CLAUDE.md`
estão todas confirmadas em fonte primária, com o trecho literal ao lado. A patente do escape foi
encontrada, lida inteira e resumida — e descobrimos que a concessão europeia saiu em maio deste ano, quatro
meses atrás, com o prazo de oposição ainda correndo. Apareceu também o registro de desenho do próprio
relógio, com seis vistas ortogonais, que nenhum de nós sabia que existia.

Mas o resultado mais importante da fase é outro, e é desconfortável: **o relógio que o `CLAUDE.md`
descrevia não é exatamente o relógio que vamos modelar.** Cinco coisas mudaram.

1. **Não existe haste de corda.** O diâmetro mínimo de 1,5 mm de uma tige não cabia, então as duas coroas
   frontais foram integradas à caixa como rodas do próprio calibre. Quem disse isso foi o diretor técnico
   de caixas da marca, com todas as letras. Toda a lógica de corda e acerto tem de ser desenhada a partir
   do zero — as peças clássicas do remontoir não existem aqui.
2. **Os ponteiros são decalcados diretamente sobre as rodas, sem canhão.** Está no comunicado, e o filme
   oficial mostra um ponteiro de perfil sobre a pinça: é uma lâmina plana. O motion works tradicional não
   existe, e a relação 12:1 entre hora e minuto está em algum lugar que ainda não sabemos qual.
3. **O barrilete não tem ponte nem receptáculo**, nem acima nem abaixo: é retido só pela periferia, por
   quatro apoios. Isso converte altura em largura de mola, que é o que compra as 45 horas.
4. **Há uma roda intermediária** entre o barrilete e a segunda roda que ninguém tinha previsto.
5. **O banking do escape é sólido, contra um entalhe usinado na platina**, com o pivô da âncora entre as
   duas pedras — coisas que a patente não diz e que só aparecem na análise da Hodinkee.

E um sexto achado, de higiene: **doze dos dezenove arquivos que você me deu não eram fotografias**. Eram
previews de um modelo 3D comercial de terceiro, com marca d'água, e dois deles mostram a malha poligonal em
wireframe. Estavam a um passo de entrar no projeto como se fossem o objeto — e o perfil renderizado por
aquele modelo é visivelmente mais grosso que 1,75 mm. Pior: boa parte do material **oficial** da própria
Richard Mille também é render, não fotografia. Os nomes dos arquivos entregam o pipeline e trazem data de
render sete meses anterior ao lançamento. Isso virou regra de método (DEC-003): medida tirada de render
oficial nasce classe E, nunca C.

---

## O que sabemos (classe A — fonte primária)

Tudo que a marca publica e todas as declarações nomeadas de Arbona, Boillat e Mathys, em cinco idiomas,
está em `docs/FACTS.md` com o trecho literal. O núcleo:

- Relógio 51,00 × 39,00 × 1,75 mm; calibre 41,45 × 28,85 × 1,18 mm; movimento de 2,82 g.
- 45 h ± 10% (a tolerância é publicada), barrilete a **exatamente** 6 h por volta, 4 Hz, 54° de
  levantamento, 3 mg·cm², 23 rubis, espiral AK 3, Kif, balanço de titânio grau 5 com três braços e seis
  massas, sem raquete.
- Cristais: 0,20 mm no centro e 0,30 mm na borda sobre o balanço; **0,45 mm** sobre as horas — contestado
  pelo próprio comunicado, que num trecho narrativo diz que os dois foram afinados a 2/10 de milímetro.
- Caixa monobloco em titânio grau 5, com pontos de **0,18 mm** de material onde a norma relojoeira pede
  0,35 mm; 13 parafusos spline que prendem caixa **e** pulseira; 1 atm; mais de 5 000 g de resistência,
  verificados em pêndulo de Charpy.
- Escape patenteado sem dardo e sem plateau de segurança, com a função de banking transferida para uma
  forquilha alongada de cornes modificadas.

Duas contradições vivem dentro das próprias fontes primárias e ficaram registradas em vez de resolvidas: a
espessura do cristal das horas, e as horas de desenvolvimento (mais de 6 000, contra 3 600 + 2 400 + 2 000
= 8 000 no detalhamento do mesmo texto).

---

## O que inferimos (classes C e D — nosso trabalho, não deles)

Nenhuma medida foi feita ainda: a Fase 1 foi pesquisa. O que temos de inferência é aritmética sobre números
publicados, e ela é mais útil do que parece.

- **7,5 voltas úteis de mola** (45 h ÷ 6 h). É bastante para um relógio de pulso, e é coerente com a
  decisão de converter altura em largura de mola.
- **A razão total do trem** fica determinada assim que soubermos quantos dentes tem a roda de escape:
  5 760 com 15 dentes, 4 800 com 18, 4 320 com 20. Um trem suíço clássico faz cerca de 4 500 em quatro
  engrenamentos, média de 8,2 por estágio — o que significa que a roda intermediária recém-descoberta se
  comporta como *idler* puro, e que a razão 1:1 que a revista japonesa conjeturou é **consistente**, não
  suspeita. Foi a primeira coisa que a síntese conseguiu decidir sem precisar de imagem.
- **O calibre é mais de metade vazio.** 2,82 g num envelope de 1,41 cm³ dá densidade aparente de 2,0 g/cm³
  contra 4,43 do titânio grau 5. Qualquer modelo nosso que feche em massa sem esqueletar pesadamente está
  errado, e agora isso é um teste automático.
- **O eixo de 41,45 mm é o 3h–9h.** A alternativa é geometricamente impossível (daria folga negativa no
  outro eixo). Falta só confirmar por imagem, o que é trivial.

---

## O que não sabemos — e agora está organizado

As 87 questões abertas pelos quatro pacotes foram deduplicadas e renumeradas em **81**, cada uma com o
marco que bloqueia, o teste que a decide e onde procurar. Três delas não são fecháveis por trabalho nosso e
definem o teto do projeto:

- **Não existe desmontagem pública do RM UP-01 feita por terceiro, em nenhum idioma.** Todo material de
  movimento fora da caixa vem da própria Richard Mille. **Não há uma única imagem pública do verso do
  movimento**, nem do escape isolado, nem uma seção, nem um desenho cotado. Toda a evidência visual deste
  relógio é controlada pela marca. Isso põe um teto permanente na classe de evidência de tudo que fica do
  lado oculto, e precisa ser dito no site, não escondido.
- **Não há press kit em PDF nem manual público.** O comunicado íntegro só existe por reprodução em
  imprensa.
- **A Audemars Piguet Le Locle e Giulio Papi nunca falaram publicamente deste relógio.** Toda a atribuição
  a eles vem do lado Richard Mille. O caminho para o lado AP é a árvore de patentes.

E um buraco que **é** fechável e continua aberto: Espacenet, WIPO, Swissreg e Justia recusaram acesso
automatizado, e o Google Patents começou a devolver 503 no meio do trabalho. A varredura por titular e por
CPC ficou pela metade. Por causa disso, três famílias de patentes que a marca diz existir — barrilete
extraplano, balanço de inércia variável e seletor W/H — continuam sem número. É o maior buraco de pesquisa
que a fase deixa, e depende de acesso seu ou dos pedidos U04/U05.

---

## O que foi entregue nesta síntese

| Arquivo | O que é |
|---|---|
| `docs/OPEN-QUESTIONS.md` | 81 questões consolidadas, priorizadas por marco, com teste discriminante e tabela de equivalência dos IDs antigos |
| `docs/ARCHITECTURE.md` | decomposição funcional nó a nó: função, peças, visibilidade, imagem que mostra cada uma, classe de evidência, âncoras |
| `engineering/bom-reconstructed.csv` | 60 peças com `part_id` permanente — inclusive **três registradas como inexistentes** (dardo, plateau de segurança, ponte do barrilete) |
| `engineering/interfaces.csv` | 52 interfaces, 22 ainda hipotéticas e marcadas como tal |
| `docs/MASTER-RESEARCH-PLAN.md` | seis alvos que ainda valem busca, o que cada um dos 20 pedidos do Balcão deve fechar, critérios de parada, nove gates |
| `docs/CAD-RECONSTRUCTION-PLAN.md` | datums, envelope, Z-budget com duas colunas, fases 3→13, divisão Fusion × Python, cinco solvers |
| `docs/VALIDATION-PLAN.md` | testes por família, matriz forense, os 16 critérios de "concluído" mapeados a testes |
| `agent-tasks/backlog/` | 12 pacotes TASK-P2-001…012 prontos para as próximas ondas |

---

## Três decisões que dependem de você

### 1. Cristal das horas: 0,45 mm ou 0,20 mm?

**A boa notícia é que você pode não decidir agora.** O relatório da primeira onda sugeria que 0,45 mm
apertaria demais a conta vertical e que isso favorecia a hipótese dos dois cristais a 0,20 mm. Refazendo a
conta coluna a coluna, o argumento se desfaz: o relógio não tem uma pilha vertical, tem várias. Os 1,18 mm
são a altura **máxima** do calibre, onde estão o barrilete e o balanço — e ali o cristal é o fino, de
0,20 mm. Sob a indicação, onde o cristal é o grosso, só há rodas-lâmina com ponteiros decalcados e nenhum
canhão.

- Coluna do balanço: 0,18 (piso da caixa) + 1,18 (movimento) + 0,20 (cristal) = **1,56 mm**, sobrando
  0,19 mm para todas as folgas. Fecha, apertado.
- Coluna da indicação com cristal de 0,45 mm: exige que a região da indicação seja pelo menos **0,06 mm
  mais baixa** que o ponto mais alto do calibre. Plausível — e há uma observação japonesa dizendo que o
  eixo da indicação se apoia **contra o cristal**, que é exatamente a folga zero que essa hipótese pede.

Ou seja: a assimetria entre os dois cristais deixa de ser estranha e passa a parecer solução de engenheiro
— o vidro grosso está sobre a região baixa, o fino sobre a alta.

**O que proponho:** carregar as duas hipóteses em paralelo no Z-budget, com o teste automático rodando duas
vezes e registrando em qual delas cada coluna fecha (já registrado como DEC-005). A questão vira um teste
geométrico, não uma aposta. **Decida só se discordar disso.**

### 2. As imagens oficiais ficam dentro ou fora do repositório?

Hoje estão **fora**: `research/images/rm-oficial/` (13 arquivos, 4,7 MB) está no `.gitignore`, junto com os
quadros de vídeo e as fatias do sprite 360°. O manifesto guarda URL e `sha256` de cada arquivo, e os dois
scripts em `solvers/image_metrology/` reproduzem os quadros a partir do mp4 e dos timestamps — então nada
se perde, só não viaja no Git.

- **A favor de manter fora:** o repositório é público, o material tem direitos de terceiro, e o §3.5 do
  `CLAUDE.md` já diz que imagens protegidas não devem ser republicadas. Repositório leve.
- **A favor de trazer para dentro:** reprodutibilidade imediata. Se a Richard Mille trocar ou remover um
  arquivo do `media.richardmille.com`, o `sha256` deixa de ser verificável e perdemos a base de metrologia
  — e é sobre essas imagens que toda a Fase 5 vai ser construída.

**O que proponho:** manter fora do Git, e fazer um espelho local versionado por você em disco (fora do
repositório), com o `sha256` do manifesto servindo de conferência. Assim temos reprodutibilidade sem
redistribuir material de terceiro num repositório público. **Precisa da sua palavra** porque é decisão de
risco jurídico, não técnica.

### 3. Margem do Z-budget: quanta folga assumir enquanto não medimos?

Este é o número que vai limitar tudo. Sabemos o teto (1,75 mm), o teto do movimento (1,18 mm), o piso de
parede (0,18 mm) e as espessuras dos cristais. **Não sabemos nenhuma folga**, e a soma dos materiais
declarados já consome 1,56 dos 1,75 mm na coluna crítica. Sobram 0,19 mm para: folga fundo↔movimento,
folga movimento↔cristal, e o quanto a luneta sobe acima do cristal.

Três posturas possíveis:

| Postura | Como fica | Risco |
|---|---|---|
| **Conservadora** — folgas mínimas relojoeiras usuais (~0,03–0,05 mm por lado) | consome 0,06–0,10 dos 0,19 mm; sobra pouco para a luneta | pode não fechar, e aí descobrimos que nossa hipótese de piso está errada |
| **Justa** — folgas no mínimo físico (~0,01–0,02 mm) | fecha com folga para a luneta | assume precisão que só se justifica pela tolerância de 1 μm declarada |
| **Explícita** — toda folga entra como placeholder classe F, declarada, e o teste roda com faixas em vez de valores | não fecha nem deixa de fechar: **informa** | exige disciplina para não virar "provisório permanente" |

**O que proponho:** a terceira, com um relatório de placeholders que o §17 obriga a zerar antes da v1. Já
deixei três placeholders declarados no `master-parameters.yaml` (a posição do movimento dentro da caixa nos
três eixos) exatamente para que o CAD não os invente em silêncio. Mas se você preferir um número de
trabalho para destravar a modelagem, diga qual postura, e ele entra como F com a sua assinatura.

---

## O que eu faria a seguir, se fosse decidir sozinho

Nesta ordem, e por uma razão em cada caso:

1. **TASK-P2-001** — cruzar o render oficial do calibre com o quadro da platina nua. Custa uma tarde e
   decide se a imagem mais informativa do corpus serve para alguma coisa. Uma resposta negativa muda o
   regime de trabalho de duas fases inteiras, e é melhor descobrir agora do que na Fase 7.
2. **TASK-P2-010** — olhar uma foto frontal e responder se os dois ponteiros são coaxiais. É a pergunta
   mais barata que temos em aberto e ainda não foi feita; ela restringe de imediato duas outras.
3. **TASK-P2-002 e TASK-P2-005** — as duas calibrações que transformam a arquitetura, hoje toda
   qualitativa, em milímetros.
4. Em paralelo, **fora do nosso tempo de máquina**: a varredura de patentes com acesso desbloqueado
   (TASK-P2-011) e a chegada das entregas U01–U20 do Balcão (TASK-P2-012).

E uma recomendação de disciplina: **a pesquisa deixa de ser a atividade principal do projeto.** O corpus já
é suficiente para começar a medir. O risco dominante daqui para frente não é a falta de informação — é
continuar lendo em vez de medir.

---

## Nota de governança

Nada foi comitado, conforme o preâmbulo dos pacotes. Nenhum Codex foi usado. Nenhuma imagem nova foi
baixada e nenhum bloqueio de acesso foi contornado. Os arquivos alterados nesta síntese são
`docs/OPEN-QUESTIONS.md`, `docs/ARCHITECTURE.md` (novo), `docs/MASTER-RESEARCH-PLAN.md` (novo),
`docs/CAD-RECONSTRUCTION-PLAN.md` (novo), `docs/VALIDATION-PLAN.md` (novo), `docs/DECISIONS.md`
(DEC-004 e DEC-005), `docs/RESEARCH-LOG.md`, `CHANGELOG.md`, `engineering/bom-reconstructed.csv`,
`engineering/interfaces.csv`, `engineering/master-parameters.yaml` e os doze pacotes em
`agent-tasks/backlog/`.
