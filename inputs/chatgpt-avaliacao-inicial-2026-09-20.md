Assumindo que você está falando de **Autodesk Fusion**, eu tentaria. Mas colocaria o RM UP-01 numa categoria bem acima do PW-50: ele é um projeto de engenharia reversa extremamente difícil, porém justamente do tipo em que Codex + Claude trabalhando como agentes podem produzir algo muito interessante.

A distinção essencial é esta:

| Meta                                                                    | Dificuldade | Minha expectativa                                 |
| ----------------------------------------------------------------------- | ----------: | ------------------------------------------------- |
| Replica visual externa                                                  |        4/10 | Muito viável                                     |
| CAD detalhado do movimento                                              |        7/10 | Viável                                           |
| Movimento cinematicamente correto                                       |      8,5/10 | Viável com bastante investigação               |
| Reconstrução funcional a 1,18 mm                                      |      9,5/10 | Possível como projeto experimental, sem garantia |
| Clone fabricável 1:1 do RMUP-01                                        |       10/10 | Dados públicos insuficientes                     |
| Clone que realmente entregue 45 h, 4 Hz, 1,18 mm e resistência extrema |      >10/10 | Exigiria prototipagem e metrologia reais          |

O motivo de eu achar o projeto mais factível do que parece é que existe **muito mais informação pública do RM UP-01 do que normalmente existe de um calibre proprietário**.

![Image](https://uncrate.com/p/2022/07/richard-mille-ferrari-rm-up-01-3.jpg)

![Image](https://www.ft.com/__origami/service/image/v2/images/raw/https%3A//d1e00ek4ebabms.cloudfront.net/production/57787a2b-eb54-4eec-b9e2-d2ccc922ab03.png?dpr=2\&fit=scale-down\&quality=medium\&source=next\&width=700)

![Image](https://people.timezone.com/jmerino/22RMferrari8.jpg)

A própria Richard Mille nos dá uma série de âncoras dimensionais bastante valiosas. O calibre RMUP-01 mede **41,45 × 28,85 mm e somente 1,18 mm de espessura**, possui 23 rubis, balanço de titânio de três braços com seis massas de regulagem, momento de inércia de 3 mg·cm², ângulo de levantamento de 54°, frequência de 28.800 alternâncias/h — 4 Hz — e aproximadamente 45 horas de reserva de marcha. O relógio completo tem apenas 1,75 mm de espessura. ([Richard Mille][1])

Isso é excelente para engenharia reversa porque nos dá uma escala absoluta para calibrar fotografias.

Mais importante ainda: sabemos bastante da arquitetura. O barrilete fica aproximadamente no centro; o trem principal fica à direita; escape e balanço também ficam desse lado. À esquerda existe o sistema de corda/ajuste e aparentemente um trem separado para a indicação de horas e minutos. Fotografias de montagem mostram rodas individualmente e até o sistema deslizante que seleciona `W` para winding e `H` para hand-setting. ([Hodinkee][2])

E aí vem a parte particularmente interessante: **o escape não precisa ser inventado do zero**.

O escape ultraplano tem patente pública.

A patente europeia **EP3754433A1**, inventor Giulio Papi, prioridade de 19 de junho de 2019, descreve justamente um conjunto de escape de âncora no qual a âncora não tem o guard pin convencional. A geometria das pontas da forquilha interage diretamente com uma parede anti-overbanking do plateau. ([Patentes Google][3])

A correspondente americana virou a patente US 11,550,262. ([Justia Patents][4])

Esse mecanismo coincide com a descrição oficial da Richard Mille: foram eliminados o dart/guard pin e o safety roller convencional, que normalmente acrescentam altura ao escape; a função de segurança foi incorporada à geometria da forquilha e do roller. ([Richard Mille][1])

Portanto, uma das partes mais secretas do relógio está parcialmente documentada em desenhos de patente.

E isso muda tudo.

A dificuldade real não seria "conseguir desenhar o relógio". Seria **determinar as dimensões que não foram publicadas**.

Entre as coisas que provavelmente teremos de reconstruir por inferência estão: número exato de dentes de várias rodas; módulos; diâmetros de pivôs; alturas individuais de rodas e pinhões; posições exatas dos rubis; profundidades dos rebaixos; dimensões da mola principal; curva de torque; espessuras de bridges; folgas axiais; endshake; backlash; perfis de algumas rodas; geometria completa do seletor W/H; detalhes do KIF; tolerâncias de montagem e várias interfaces entre caixa e movimento.

E no RM UP-01 isso é especialmente brutal porque estamos brigando por **centésimos de milímetro**.

A Richard Mille afirma que componentes do relógio foram usinados com tolerâncias chegando a **um mícron**. O próprio movimento foi desenvolvido em conjunto com Audemars Piguet Le Locle e passou por mais de 6.000 horas de desenvolvimento/testes; a marca afirma resistência a acelerações acima de 5.000 g. ([Richard Mille][1])

Ou seja, fazer uma peça "parecida" é fácil. Fazer duas peças que ainda funcionem quando há apenas 1,18 mm verticalmente disponível é outra história.

### Mas Codex + Claude mudam bastante o jogo

Eu não faria os agentes "modelarem o relógio olhando fotos".

Isso daria errado.

Eu construiria uma pequena operação de engenharia reversa.

O Claude/Fable funcionaria muito bem como **engenheiro de documentação/reverse engineering**: ler artigos, patentes, entrevistas e descrições; catalogar imagens; comparar fotografias de diferentes ângulos; extrair relações geométricas; produzir hipóteses; detectar inconsistências; e manter uma `evidence matrix`.

O Codex ficaria responsável principalmente pelo **CAD paramétrico, cálculos e validações automáticas**.

O Fusion é particularmente adequado porque tem uma API real para automação em Python, C++ e TypeScript, e os próprios parâmetros do modelo podem dirigir dimensões e relações geométricas. A Autodesk também fornece API para CAM. ([Ajuda Autodesk][5])

Então poderíamos fazer algo muito melhor que CAD manual:

```text
RMUP01/
│
├── evidence/
│   ├── patents/
│   ├── official/
│   ├── articles/
│   ├── photos/
│   └── videos/
│
├── measurements/
│   ├── image-calibration/
│   ├── known-dimensions.yaml
│   ├── inferred-dimensions.yaml
│   └── uncertainty.yaml
│
├── calculations/
│   ├── geartrain.py
│   ├── escapement.py
│   ├── barrel.py
│   ├── motion_works.py
│   └── tolerances.py
│
├── fusion/
│   ├── case/
│   ├── baseplate/
│   ├── barrel/
│   ├── train/
│   ├── escapement/
│   ├── balance/
│   ├── winding/
│   └── assembly/
│
├── tests/
│   ├── collisions.py
│   ├── gear_mesh.py
│   ├── clearances.py
│   ├── stack_height.py
│   └── kinematics.py
│
└── RMUP01.f3d
```

Cada dimensão teria algo como:

```yaml
balance_frequency:
  value: 4
  unit: Hz
  confidence: A
  source: Richard Mille

movement_thickness:
  value: 1.18
  unit: mm
  confidence: A

escape_wheel_diameter:
  value: 3.14
  unit: mm
  confidence: C
  method: photogrammetry
  uncertainty: 0.08
```

A = publicada.

B = mensurada de imagem calibrada.

C = inferida cinematicamente.

D = hipótese temporária.

Isso seria fundamental para impedir que os agentes transformassem hipóteses em "fatos".

### Eu começaria pelo exterior

A reconstrução externa seria relativamente simples porque temos uma quantidade grande de vistas e sabemos a espessura total.

Há também patentes de design da Richard Mille contendo vistas ortogonais dos relógios, que podem servir como fonte geométrica adicional para contorno e proporções. ([Justia Patents][6])

No Fusion:

```text
MASTER_PARAMETERS

watch_Z = 1.750 mm
movement_Z = 1.180 mm

movement_X = 41.450 mm
movement_Y = 28.850 mm

hour_crystal_Z = 0.450 mm
balance_crystal_center_Z = 0.200 mm
balance_crystal_edge_Z = 0.300 mm
```

Essas espessuras de safira são inclusive publicadas oficialmente. ([Richard Mille][1])

Depois calibramos fotografias frontais usando `movement_X` e `movement_Y`.

Daí o agente consegue estimar coordenadas:

```text
BARREL_CENTER = (x1,y1)
BALANCE_CENTER = (x2,y2)
ESCAPE_CENTER = (x3,y3)
SELECTOR_CENTER = (...)
SETTING_CENTER = (...)
```

Um script pode fazer isso quantitativamente em vez de alguém simplesmente eyeballar as posições.

### O segundo grande passo seria reconstruir a platina

Aqui aparece uma vantagem enorme do RM.

A platina é extremamente aberta e existem fotografias dela desmontada.

A imagem explodida disponível publicamente mostra caixa, movimento, seletor, barrilete e outros conjuntos separados. As fotos de montagem mostram ainda a posição de várias rodas. ([Hodinkee][2])

O Codex poderia gerar inicialmente uma platina aproximada e depois iterar:

```text
foto
 ↓
contorno
 ↓
pontos de referência
 ↓
restrições geométricas
 ↓
Fusion sketch
 ↓
comparação render ↔ foto
 ↓
erro
 ↓
nova iteração
```

Isso é exatamente o tipo de trabalho repetitivo em que agentes podem tentar 30 ou 100 variantes sem cansar.

### Depois viria o barrilete

E aqui a dificuldade sobe bastante.

Sabemos que ele dá uma volta em aproximadamente **seis horas**, mais rapidamente que um barrilete tradicional, e sabemos que a reserva de marcha é aproximadamente 45 horas. ([Richard Mille][1])

Também vemos uma característica muito estranha nas fotos: o barrilete ultraplano é estabilizado por **rolos em sua periferia**, em vez de usar simplesmente a arquitetura vertical tradicional. ([Hodinkee][2])

Isso é excelente para reconstruir o conceito.

Mas não sabemos publicamente todas as propriedades da mola.

Portanto, eu faria duas coisas separadas:

**RMUP-CAD**, tentando reproduzir geometricamente o original.

E:

**RMUP-FUNCTIONAL**, usando uma mola calculada por nós capaz de entregar aproximadamente o comportamento requerido.

Nunca fingiria que a segunda é exatamente a mola da Richard Mille.

### O trem de engrenagens seria um dos desafios mais interessantes para os agentes

Temos uma restrição muito poderosa:

```text
barrel ≈ 1 rev / 6 h
balance = 4 Hz
```

O escape precisa converter uma rotação extremamente lenta do barrilete em eventos de escape a 8 alternâncias por segundo.

Então podemos buscar combinações discretas de:

```text
Z1/z2 × Z3/z4 × Z5/z6 ...
```

que satisfaçam a razão total.

Depois comparamos os conjuntos candidatos às fotos.

Esse problema é quase perfeito para solver computacional.

Imagine:

```python
for train in possible_trains:
    ratio_error = ...
    diameter_error = ...
    photo_error = ...
    center_distance_error = ...
    tooth_geometry_error = ...

    score(train)
```

Depois os agentes examinam, por exemplo, 20 candidatos em vez de simplesmente inventarem um número de dentes.

Eu inclusive tentaria reconstruir os dentes a partir das fotografias com análise angular/periodicidade da borda da roda.

### O escape é difícil, mas surpreendentemente reconstruível

A patente é ouro.

Ela descreve a interação entre:

* escape wheel;
* pallet fork;
* dois pallets;
* impulse pin;
* roller;
* anti-overbanking wall;
* notch;
* horns da forquilha.

([Patentes Google][3])

E fotografias do próprio RM mostram o conjunto desmontado. Hodinkee inclusive mostra separadamente lever, escape wheel e lever bridge e descreve a forma como a alavanca banca diretamente contra a platina. ([Hodinkee][2])

Então eu acho que conseguimos uma **reconstrução funcional bastante convincente do escape**.

Isso seria provavelmente uma das melhores partes do projeto.

### Já o seletor W/H é outro quebra-cabeças excelente

Existem imagens públicas em que o sistema está efetivamente desmontado e sendo operado.

O seletor superior desloca um braço lateral; numa posição ele acopla a roda de corda, e na outra desacopla o barrilete e conecta o ajuste das horas. ([Hodinkee][2])

Ou seja: novamente não estamos no escuro.

Isso permitiria modelar:

```text
Selector
   ↓
cam / eccentric
   ↓
sliding clutch
 ┌───────────┐
 W           H
 ↓           ↓
barrel      hands
```

E colocar joints no Fusion para demonstrar o mecanismo.

### O verdadeiro inferno é Z

O relógio é basicamente um exercício de `Z-budget`.

Eu faria o agente manter permanentemente algo parecido com:

```text
TOTAL MOVEMENT
===========================

baseplate             0.xxx
wheel layer           0.xxx
pivot clearance       0.xxx
bridge                 0.xxx
---------------------------
TOTAL                  ≤ 1.180 mm
```

e:

```text
TOTAL WATCH
===========================

caseback
movement
top clearances
bezel
sapphire
---------------------------
TOTAL                  ≤ 1.750 mm
```

Qualquer alteração que estourasse o orçamento vertical faria o CI reprovar o CAD.

Esse seria um projeto muito adequado ao método que vocês estão usando no PW-50: transformar o CAD em **engenharia verificável**, não em um modelo bonito.

Só que aqui eu iria ainda mais longe.

Cada commit do agente deveria gerar automaticamente:

```text
✓ movement envelope
✓ interference test
✓ gear center distances
✓ gear ratio
✓ escape geometry
✓ jewel count
✓ stack-height
✓ screw clearances
✓ minimum wall
✓ motion range
✓ winding selector states
```

### Eu usaria os dois agentes de maneira adversarial

Não deixaria Claude e Codex trabalharem juntos fazendo a mesma coisa.

Faria algo assim:

```text
CLAUDE — Reverse Engineering Lead
        ↓
extrai evidência
propõe arquitetura
estima medidas
documenta incerteza

        ↓ spec

CODEX — CAD Engineer
        ↓
implementa Fusion API
faz cálculos
gera componentes
executa validações

        ↓ report

CLAUDE — Auditor
        ↓
compara CAD ↔ fontes
acha inconsistências
questiona hipóteses

        ↓ corrections

CODEX
```

E ocasionalmente inverteria:

```text
Codex propõe solução
Claude tenta destruí-la.
```

Isso reduz bastante alucinação geométrica.

### Eu também faria uma regra importante

Os agentes não podem dizer:

> "a roda tem 67 dentes".

Teriam de dizer:

> `67 dentes — hipótese C17 — estimada a partir das imagens IMG-042/043 e da razão cinemática R12; alternativas 66/68 ainda abertas.`

Esse detalhe sozinho provavelmente faria a diferença entre um projeto de IA impressionante e um CAD cheio de números inventados.

### Quanto conseguiríamos reproduzir?

Minha estimativa, depois de olhar o material disponível, seria aproximadamente:

**Exterior:** 95–99% visualmente.

**Layout do movimento:** 90–95%.

**Peças visíveis principais:** 85–95%.

**Arquitetura mecânica:** talvez 85–90%.

**Cinemática:** provavelmente >90% do comportamento observável.

**Dimensões internas exatas:** talvez 60–80%.

**Tolerâncias reais:** muito menos.

**Performance física real:** desconhecida até fabricação.

Isso significa que eu acredito ser plausível chegarmos a um ponto em que alguém da relojoaria olhe o assembly no Autodesk e diga:

> "Isso é claramente uma reconstrução técnica séria do RMUP-01."

Não acredito que apenas a internet permita afirmar:

> "Este é um clone dimensional perfeito do calibre RMUP-01."

Essa distinção é importante.

### E há uma coisa que torna esse projeto excepcional como teste de Codex/Claude

O original levou **mais de 6.000 horas de desenvolvimento e testes**, segundo a Richard Mille. ([Richard Mille][1])

Não vamos substituir essas 6.000 horas com prompts.

Mas o objetivo pode ser diferente.

Podemos perguntar:

> **Até onde uma equipe de agentes consegue reconstruir, a partir apenas de informação pública, um dos movimentos mecânicos mais extremos já construídos?**

Isso é uma experiência muito mais interessante.

E comparado ao PW-50, eu acho que seria um excelente **"boss final"**.

O PW-50 testa se os agentes conseguem **projetar** um relógio.

O RMUP-01 testaria se conseguem:

**pesquisar → interpretar patentes → fazer fotogrametria → inferir dimensões → resolver trem → reconstruir mecanismos → escrever CAD paramétrico → auditar incerteza → validar cinemática.**

Minha estimativa de trabalho seria algo como **4–8 semanas de execução intensiva dos agentes** para chegar a um CAD digital muito bom, desde que tratemos isso como um projeto com centenas de tarefas pequenas e testes, não como "faça o RM UP-01". Uma primeira versão externa poderia aparecer em dias; um movimento convincente em 1–2 semanas; e a fase realmente difícil começaria quando tentássemos fechar tudo dentro dos **1,18 mm**.

Eu faria esse projeto.

E faria com uma ambição específica: **não uma cópia estética do RM UP-01, mas uma reconstrução forense completa do RMUP-01 a partir de fontes abertas**, com cada dimensão marcada como publicada, medida, inferida ou hipotética. Se no final conseguirmos fechar uma cinemática funcional dentro do envelope de 41,45 × 28,85 × 1,18 mm, isso já seria um resultado bastante extraordinário.

Para uso de estudo e engenharia reversa isso é uma coisa; caso a intenção chegue a fabricar/comercializar uma réplica, valeria tratar separadamente as patentes e os direitos de design ainda relevantes.

Sim. Para esse projeto eu mudaria completamente a escala da operação. O PW-50 é essencialmente um projeto de engenharia; o RM UP-01 pode virar uma **reconstrução forense digital de longo prazo**, na qual pesquisa histórica, patentes, metrologia por imagem, engenharia reversa, CAD paramétrico, simulação e documentação pública formam um único sistema.

Preparei a instrução-mestra completa para o Claude Code. Ela tem mais de 1.100 linhas e foi escrita para ficar na raiz do repositório como `CLAUDE.md`:

[Baixar CLAUDE-RM-UP-01.md](sandbox:/mnt/data/CLAUDE-RM-UP-01.md)

A ideia central do arquivo é importante: **não queremos um relógio que apenas pareça um RM UP-01. Queremos a reconstrução mais próxima do original que seja defensável por informação pública.**

Isso é especialmente promissor porque temos âncoras extraordinariamente boas. A Richard Mille publica diretamente que o movimento mede 41,45 × 28,85 × 1,18 mm, trabalha a 4 Hz, possui 23 rubis, balanço de titânio de três braços e seis massas, momento de inércia de 3 mg·cm², lift angle de 54°, cerca de 45 h de reserva e barrilete que completa uma volta aproximadamente a cada seis horas. A empresa publica inclusive espessuras dos cristais, construção da caixa, materiais e vários detalhes de acabamento e dentado. ([Richard Mille][1])

Também não estamos tentando deduzir o escape apenas olhando uma fotografia. Existe uma família de patentes de Giulio Papi, incluindo EP3754433A1, que descreve a arquitetura do escape com a âncora sem o guard pin convencional e a geometria anti-overbanking incorporada à interação entre forquilha e plateau. ([Patentes Google][2])

E existe documentação fotográfica particularmente boa de desmontagem e montagem. A análise técnica da Hodinkee mostra o movimento fora da caixa, going train, barrilete, escape e vários passos de montagem, o que é muito valioso para estabelecer topologia e relações espaciais. ([Hodinkee][3])

A própria Richard Mille diz que o desenvolvimento real envolveu dezenas de protótipos e mais de 6.000 horas de desenvolvimento e testes. Isso ajuda a definir a filosofia correta para nosso trabalho: não tentar terminar em dez prompts. ([Richard Mille][1])

No `CLAUDE.md`, organizei o projeto assim:

1. **Fundação antes do CAD.** Primeiro surgem o sistema de evidências, catálogo de fontes, IDs permanentes, banco de hipóteses, perguntas abertas e parâmetros. Nenhum agente pode simplesmente escrever “essa roda tem 64 dentes”. Ele terá de dizer de onde saiu o 64, qual a incerteza e quais alternativas ainda existem.
2. **Pesquisa brutal e multilíngue.** Richard Mille, Ferrari, Audemars Piguet Le Locle/APRP, famílias de patentes, entrevistas com Giulio Papi e outros responsáveis, press kits, páginas antigas, fotografias oficiais, desmontagens, vídeos, feiras, revistas técnicas e material em inglês, francês, alemão, italiano, japonês etc. Cada fonte entra em um manifesto e cada claim é ligado às fontes que o sustentam.
3. **Metrologia de imagem.** As fotografias deixam de ser apenas referências visuais. Vamos calibrá-las usando dimensões conhecidas, corrigir perspectiva, marcar landmarks, comparar várias imagens do mesmo componente e projetar o CAD de volta sobre as fotografias. Assim conseguimos transformar pixels em intervalos dimensionais defensáveis.
4. **Reconstrução da arquitetura.** Antes de decorar qualquer peça, mapeamos centros, eixos, rubis, interfaces, cadeia de energia e orçamento vertical. O `Z-budget` será quase tão importante quanto o CAD: tudo precisa caber de verdade nos 1,18 mm do movimento e nos 1,75 mm do relógio.
5. **Reconstrução por subsistemas.** Caixa → platina e pontes → barrilete → trem → seletor W/H → escape → balanço/espiral/Kif → indicação → pivôs/rubis/parafusos → assembly. Cada subsistema tem seu próprio gate de aceitação.
6. **Problemas difíceis tratados computacionalmente.** O número de dentes, por exemplo, não será adivinhado. Um solver combinará diâmetros aparentes, distâncias entre centros, relações de transmissão, barrilete de ~6 h/rev, 4 Hz, sentidos de rotação e possíveis módulos. O mesmo vale para fitting de formas, incertezas, propriedades de massa e posteriormente Monte Carlo.
7. **Autodesk Fusion como CAD canônico.** Componentes de verdade, joints, parâmetros centralizados, scripts pela API quando fizer sentido, STEP/DXF/CSV de apoio e testes de interferência. Não quero que todo o conhecimento fique enterrado num `.f3d` impossível de auditar.
8. **Claude e Codex com papéis diferentes.** Claude funciona principalmente como diretor técnico, pesquisador, arquiteto de evidências e revisor. Codex recebe pacotes delimitados para scripts, solvers, automação do Fusion, testes e análises quantitativas. Há também uma etapa adversarial: um agente propõe; outro tenta falsificar a solução antes de integrarmos.
9. **Fabricabilidade digital como auditoria.** Não vamos fabricar o relógio, mas vamos perguntar se ele poderia ser levado a sério como mecanismo: endshake, backlash, folgas, pivôs, retenção axial, acessibilidade de montagem, processos prováveis, espessuras mínimas, tolerâncias e Monte Carlo. Não para afirmar que conhecemos as tolerâncias originais, mas para impedir um CAD que só funcione visualmente.
10. **O site vem no final e nasce da própria engenharia.** Em vez de um site “luxuoso sobre um relógio caro”, teremos uma espécie de museu técnico digital: por que 1,75 mm é absurdo, o movimento de 1,18 mm, exploded view interativo, barrilete, fluxo de energia, trem, escape ultraplano, balanço, seletor W/H, orçamento vertical, materiais, acabamento e uma seção particularmente importante chamada algo como **“O que sabemos / o que inferimos”**.

O detalhe que considero mais importante no plano é o sistema de classificação que coloquei para cada informação:

`A — primária`
`B — observada`
`C — medida`
`D — inferida`
`E — hipótese`
`F — placeholder`

Isso pode acabar sendo a característica mais interessante do projeto inteiro.

Imagine clicar em uma roda no futuro site e ver:

> Diâmetro: 4,82 mm
> Evidência: C
> Obtido de três fotografias calibradas
> intervalo estimado: 4,76–4,89 mm
> número de dentes: 64
> Evidência: D
> candidatos descartados: 63, 65
> motivo: incompatibilidade com relação cinemática / diâmetro observado.

Isso transforma o projeto de “um cara recriou um Richard Mille em CAD” para algo muito mais sério: **uma anatomia pública de como se reconstrói uma máquina extraordinária quando não se possui seus desenhos industriais.**

Há também algumas regras severas no documento. Desenhos de patente nunca são considerados automaticamente em escala. Uma peça que só existe para preencher uma fotografia é recusada. Um eixo sem apoio é recusado. Uma roda que não engrena é recusada. Uma colisão escondida para melhorar o render é recusada. Uma dimensão inventada jamais pode virar “fato”. E desconhecidos podem permanecer desconhecidos durante meses.

Eu não trabalharia por “semana 1, semana 2, semana 3”. Coloquei milestones por maturidade:

`M0` sistema de pesquisa funcionando → `M1` envelopes conhecidos → `M2` esqueleto mecânico → `M3` cadeia cinemática → `M4` escape resolvido → `M5` assembly nominal completo → `M6` CAD convergido às evidências → `M7` auditoria de plausibilidade → `M8` forensic digital twin v1 → `M9` site público.

Assim podemos ficar três meses presos no escape se for necessário sem artificialmente declarar que uma “fase de duas semanas terminou”.

E a primeira ordem para o Claude é deliberadamente: **não abra o Fusion ainda**.

Ele deverá primeiro construir o sistema de pesquisa, levantar fontes primárias, formar a árvore de patentes, catalogar imagens, listar incógnitas, decompor todos os mecanismos e escrever três documentos: `MASTER-RESEARCH-PLAN.md`, `CAD-RECONSTRUCTION-PLAN.md` e `VALIDATION-PLAN.md`. Só então aparece o primeiro sólido no Autodesk.

Esse é o tipo de projeto que eu acho que pode se tornar bastante especial. Não apenas porque no final teremos um RM UP-01 digital, mas porque teremos registrado todo o caminho entre **“há uma fotografia deste mecanismo”** e **“esta é a geometria que acreditamos que ele possui, por estas razões”**.

Para iniciar o Claude Code, eu colocaria o arquivo como `CLAUDE.md` na raiz de um repositório vazio e daria somente esta ordem inicial:

> Leia integralmente o CLAUDE.md. Este será um projeto de longo prazo e não há urgência para produzir CAD. Execute somente a fundação e a primeira fase de pesquisa. Quero que sua primeira grande entrega seja o corpus inicial, a árvore de evidências, as perguntas abertas e os três planos mestres descritos no documento. Não modele o relógio ainda. Pesquise profundamente, preserve provenance e trate qualquer incerteza como uma informação a ser registrada, não como um espaço a preencher por suposição.

Eu começaria exatamente daí.

[www.youtube.com/playlist?list=PLoaRvbL3QWqluu3PGRpIa-QmCWQ1bLGCH](https://www.youtube.com/playlist?list=PLoaRvbL3QWqluu3PGRpIa-QmCWQ1bLGCH)

[1]: https://www.richardmille.com/collections/rm-up-01-manual-winding-ultraflat-ferrari?utm_source=chatgpt.com
[2]: https://www.hodinkee.com/articles/the-richard-mille-rm-up-01-a-very-deep-dive-on-a-very-thin-watch
[3]: https://patents.google.com/patent/EP3754433A1/en?utm_source=chatgpt.com
[4]: https://patents.justia.com/patents-by-us-classification/70/463?utm_source=chatgpt.com
[5]: https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/PythonSpecific_UM.htm?utm_source=chatgpt.com
[6]: https://patents.justia.com/patent/D991795?utm_source=chatgpt.com
[1]: https://www.richardmille.com/collections/rm-up-01-manual-winding-ultraflat-ferrari
[2]: https://patents.google.com/patent/EP3754433A1/en?utm_source=chatgpt.com
[3]: https://www.hodinkee.com/articles/the-richard-mille-rm-up-01-a-very-deep-dive-on-a-very-thin-watch?utm_source=chatgpt.com
