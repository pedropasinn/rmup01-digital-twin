# CLAUDE.md — Projeto RM UP-01: Reconstrução Forense Digital

## 0. Mandato do projeto

Este repositório existe para um projeto de longo prazo: reconstruir digitalmente, com o máximo de fidelidade defensável por evidência pública, o Richard Mille RM UP-01 Ferrari e o calibre RMUP-01.

O objetivo NÃO é produzir uma aproximação visual rápida. O objetivo é construir uma reconstrução forense digital: forma externa, arquitetura do movimento, peças, interfaces, cinemática, empilhamento vertical, materiais, acabamento, lógica de corda/ajuste, trem de engrenagens, barrilete, escape, balanço, indicação e integração movimento-caixa.

O projeto é exclusivamente digital e educacional. Não haverá fabricação. Ainda assim, o CAD deve ser desenvolvido como se a fabricabilidade pudesse ser auditada no futuro: dimensões coerentes, interfaces explícitas, tolerâncias ou incertezas registradas, peças separáveis, montabilidade estudada e nenhuma geometria "mágica" apenas para fazer o render parecer certo.

A ambição final é chegar ao mais próximo possível de um gêmeo digital reconstruído a partir de fontes abertas, deixando absolutamente claro onde terminam os fatos e começam as inferências.

Depois da reconstrução, o mesmo corpus técnico sustentará um site de fã/estudo, não oficial, dedicado a explicar por que este relógio é extraordinário, como suas soluções funcionam e como a reconstrução foi feita.

Não temos pressa. Este projeto deve sobreviver por meses. Evidência e rastreabilidade valem mais que velocidade.

---

## 1. Princípio central

Nunca transformar ausência de informação em falsa certeza.

Cada afirmação, dimensão, relação mecânica ou peça deverá estar em uma destas classes:

- `A — PRIMÁRIA`: especificação publicada pelo fabricante, documento oficial, patente, desenho técnico primário ou declaração direta de um responsável técnico.
- `B — OBSERVADA`: característica diretamente visível em fotografia, vídeo, desmontagem ou material de primeira mão, sem necessidade de inferir dimensão.
- `C — MEDIDA`: dimensão ou posição obtida por metrologia de imagem calibrada.
- `D — INFERIDA`: resultado imposto ou fortemente restringido por geometria, cinemática, razão de engrenagens, física ou compatibilidade entre múltiplas fontes.
- `E — HIPÓTESE`: solução plausível ainda não determinada pelas evidências.
- `F — PLACEHOLDER`: valor temporário usado apenas para permitir progresso do modelo.

Nunca apresentar C, D, E ou F como A.

Qualquer número usado no CAD precisa de:
- `parameter_id`;
- valor nominal;
- unidade;
- classe de evidência;
- `source_id` ou conjunto de fontes;
- método de obtenção;
- incerteza ou faixa quando aplicável;
- data da última revisão;
- observações;
- dependências;
- estado: `confirmed`, `provisional`, `contested`, `placeholder`.

Se duas hipóteses forem compatíveis com as evidências, manter as duas até existir motivo para eliminar uma.

---

## 2. Âncoras públicas já conhecidas

Comece verificando novamente em fontes primárias, mas considere estes itens como âncoras iniciais a confirmar:

- relógio completo: espessura de 1,75 mm;
- calibre RMUP-01: 41,45 × 28,85 mm;
- espessura do calibre: 1,18 mm;
- corda manual;
- indicação de horas e minutos;
- seletor de função W/H;
- aproximadamente 45 h de reserva de marcha;
- 23 rubis;
- balanço em titânio grau 5, três braços e seis massas de regulagem;
- momento de inércia publicado de 3 mg·cm²;
- ângulo de levantamento publicado de 54°;
- 28.800 alternâncias/h, isto é, 4 Hz;
- espiral AK 3;
- proteção contra choque Kif;
- barrilete de rotação rápida: aproximadamente uma volta a cada 6 h;
- platina e pontes em titânio grau 5;
- escape ultraplano patenteado sem o conjunto convencional de dart/guard pin + safety roller;
- caixa e movimento trabalham conjuntamente para rigidez, mas o movimento continua sendo um movimento independente montado dentro da caixa;
- dois comandos frontais: seletor de função e operação de corda/ajuste;
- cristal da indicação de horas: 0,45 mm;
- cristal sobre a região do balanço: 0,20 mm no centro e 0,30 mm nas bordas;
- caixa montada com 13 parafusos spline de titânio grau 5;
- resistência à água publicada de 1 atm / 10 m;
- programa de desenvolvimento publicado superior a 6.000 horas e dezenas de protótipos;
- afirmação pública de tolerâncias de usinagem chegando a 1 μm em componentes;
- perfil involuta central, pressão de 20°, citado pelo fabricante para dentes do winding-barrel e o pinhão da terceira roda.

Patente prioritária para estudo do escape:
- EP3754433A1 / família CH716337A1 / US11550262B2;
- inventor: Giulio Papi;
- depositante/cessionário relacionado a Audemars Piguet;
- prioridade em 2019;
- usar a patente como fonte de topologia e princípio de funcionamento.
- REGRA: desenhos de patente NÃO são automaticamente desenhos em escala. Nunca extrair medidas deles sem evidência adicional.

Verificar cada item acima antes de promovê-lo ao registro `facts/`.

---

## 3. Fontes a pesquisar de forma sistemática

A pesquisa deve ser deliberadamente ampla, multilíngue e cumulativa.

### 3.1 Fontes primárias
Prioridade máxima:
- Richard Mille: página do RM UP-01, press kits, PDFs, páginas históricas, galerias, vistas 360°, vídeos, entrevistas e comunicados.
- Ferrari: lançamento, colaboração, material de imprensa e vídeos.
- Audemars Piguet Le Locle / antigo APRP / Renaud & Papi: entrevistas, patentes, apresentações e conteúdo institucional.
- Bases de patentes: EPO/Espacenet, WIPO, Google Patents, Swissreg e famílias nacionais.
- Registros de desenho industrial quando relevantes.
- Entrevistas com Giulio Papi, Richard Mille, Salvador Arbona e engenheiros envolvidos.
- Catálogos oficiais, manuais de uso e documentação de pós-venda pública.

### 3.2 Fontes técnicas de primeira mão
Pesquisar desmontagens, acesso físico ao relógio, hands-on, macrofotografia e entrevistas técnicas:
- Hodinkee e Hodinkee Japan;
- SJX;
- Monochrome;
- Revolution;
- WatchTime;
- Europa Star;
- Watches by SJX;
- Financial Times / How To Spend It;
- TimeZone e fóruns com material original identificável;
- publicações relojoeiras francesas, alemãs, italianas, japonesas e suíças.

### 3.3 Imagens e vídeo
Buscar:
- fotografia oficial em máxima resolução;
- vistas ortogonais;
- close-ups macro;
- fotos de montagem;
- movimento fora da caixa;
- movimento parcialmente desmontado;
- peças em pinça;
- vista do verso;
- sequência de operação dos seletores;
- exposições, feiras e vídeos de apresentação;
- frames de vídeo que revelem peças ocultas em fotos estáticas.

### 3.4 Pesquisa multilíngue
Executar consultas equivalentes em:
- inglês;
- francês;
- alemão;
- italiano;
- japonês;
- espanhol;
- português;
- quando útil, chinês.

Traduzir apenas para entendimento; preservar título original, língua e fonte.

### 3.5 Regras para fontes
Para toda fonte:
- armazenar URL original no manifesto local;
- título;
- autor;
- veículo;
- data;
- data de acesso;
- tipo de fonte;
- idioma;
- hash do arquivo local quando houver;
- direitos/licença quando conhecidos;
- quais claims ela suporta;
- qualidade visual;
- confiabilidade;
- observações.

Não usar material vazado, privado, obtido por invasão, paywall contornado ou acesso indevido.

Imagens protegidas podem ser mantidas no corpus privado de pesquisa quando obtidas legitimamente para análise, mas NÃO devem ser automaticamente republicadas no futuro site. O site deve preferir renders próprios, diagramas próprios, desenhos próprios e imagens com autorização/licença adequada.

---

## 4. Estrutura obrigatória do repositório

Criar e manter:

```text
rmup01-digital-twin/
├── CLAUDE.md
├── README.md
├── CHANGELOG.md
├── docs/
│   ├── PROJECT-CHARTER.md
│   ├── ARCHITECTURE.md
│   ├── FACTS.md
│   ├── OPEN-QUESTIONS.md
│   ├── HYPOTHESES.md
│   ├── DECISIONS.md
│   ├── FAILURE-LOG.md
│   ├── RESEARCH-LOG.md
│   ├── METROLOGY-METHOD.md
│   ├── VALIDATION-PLAN.md
│   └── site/
├── research/
│   ├── source-manifest.csv
│   ├── claims.csv
│   ├── patents/
│   ├── official/
│   ├── articles/
│   ├── interviews/
│   ├── images/
│   ├── videos/
│   └── translations/
├── evidence/
│   ├── evidence-ledger.csv
│   ├── image-landmarks/
│   ├── overlays/
│   ├── measurements/
│   └── alternatives/
├── engineering/
│   ├── master-parameters.yaml
│   ├── bom-reconstructed.csv
│   ├── interfaces.csv
│   ├── stack-height.csv
│   ├── materials.csv
│   ├── geartrain/
│   ├── barrel/
│   ├── escapement/
│   ├── balance/
│   ├── winding-setting/
│   ├── indications/
│   ├── jewels/
│   ├── case/
│   └── tolerances/
├── solvers/
│   ├── image_metrology/
│   ├── gear_search/
│   ├── kinematics/
│   ├── geometry_fit/
│   └── validation/
├── cad/
│   ├── fusion/
│   ├── scripts/
│   ├── exports/
│   ├── reference/
│   └── renders/
├── tests/
│   ├── geometry/
│   ├── collisions/
│   ├── ratios/
│   ├── stack_height/
│   ├── kinematics/
│   └── regression/
├── site/
│   ├── content/
│   ├── public/
│   ├── src/
│   └── data/
└── agent-tasks/
    ├── backlog/
    ├── active/
    ├── review/
    └── done/
```

Binários CAD grandes não devem destruir a legibilidade do Git. Usar Git LFS quando apropriado. Todo resultado importante deve ter também uma representação textual ou exportável que permita auditoria.

---

## 5. Documentos vivos obrigatórios

### `FACTS.md`
Somente fatos sustentados.

### `OPEN-QUESTIONS.md`
Toda lacuna importante deve permanecer visível. Cada questão recebe ID.

Exemplo:
`Q-ESC-014 — número exato de dentes da roda de escape ainda não confirmado.`

### `HYPOTHESES.md`
Cada hipótese deve ter:
- ID;
- problema;
- hipótese;
- evidências favoráveis;
- evidências contrárias;
- alternativas;
- teste que poderia discriminá-las;
- estado.

### `DECISIONS.md`
ADR simplificado: por que uma decisão de modelagem foi adotada.

### `FAILURE-LOG.md`
Guardar caminhos tentados e rejeitados. Não repetir meses depois o mesmo erro.

### `RESEARCH-LOG.md`
Diário cronológico de buscas, novas fontes e mudanças de entendimento.

---

## 6. Modelo de evidência

Criar `evidence/evidence-ledger.csv` com pelo menos:

```text
evidence_id
claim_id
parameter_id
part_id
source_id
evidence_class
method
nominal_value
unit
lower_bound
upper_bound
confidence_notes
status
created_at
updated_at
```

Não usar um "confidence score" mágico sem explicação. Preferir classes e justificativas.

Cada peça deve ter um `part_id` permanente, mesmo se o nome mudar.

Cada interface mecânica deve ter um `interface_id`.

Cada imagem útil deve ter `image_id`.

Cada landmark usado em fotogrametria deve ter `landmark_id`.

---

## 7. Política de metrologia por imagem

A reconstrução não deve ser feita "no olho".

Para toda medição extraída de imagem:

1. preservar a imagem original;
2. registrar resolução e origem;
3. identificar distorção, perspectiva e provável lente;
4. escolher âncoras conhecidas visíveis no mesmo plano;
5. corrigir perspectiva por homografia quando aplicável;
6. medir em pixels;
7. converter para unidade física;
8. repetir em imagens independentes;
9. registrar dispersão;
10. comparar com restrições cinemáticas e geométricas;
11. gerar overlay do CAD projetado sobre a fotografia;
12. guardar o overlay como evidência de validação.

Nunca calibrar um componente com uma dimensão que esteja em plano diferente sem corrigir perspectiva.

Não medir Z a partir de fotografia oblíqua sem um modelo de câmera defensável.

Quando houver três ou mais imagens independentes, preferir ajuste conjunto.

Para contornos importantes, desenvolver uma métrica de erro de projeção CAD→imagem.

Para contagem de dentes:
- usar periodicidade angular da borda;
- contagem manual independente;
- detecção computacional;
- restrições inteiras por razão;
- testar candidatos vizinhos;
- registrar alternativas até confirmação.

---

## 8. Estratégia de engenharia reversa

Não começar detalhando parafusos.

A ordem é do macro para o micro.

### Fase 0 — Fundação e governança
Entregáveis:
- estrutura do repositório;
- charter;
- esquema de evidência;
- convenções de IDs;
- testes vazios;
- backlog inicial.

Gate:
Nenhum CAD detalhado antes do sistema de evidência funcionar.

### Fase 1 — Corpus de pesquisa
Objetivo: reunir a maior base pública possível.

Entregáveis:
- manifesto de fontes;
- arquivo de patentes;
- catálogo de imagens;
- catálogo de vídeos;
- lista de entrevistas;
- fontes em múltiplos idiomas;
- deduplicação;
- ranking de utilidade por subsistema.

Gate:
As principais vistas do relógio, movimento e conjuntos internos devem estar catalogadas antes da reconstrução geométrica séria.

### Fase 2 — Mapa de fatos e arquitetura
Reconstruir a decomposição funcional:

```text
watch
├── case
├── crystals
├── movement
│   ├── baseplate
│   ├── bridges
│   ├── barrel
│   ├── winding
│   ├── function selector
│   ├── going train
│   ├── escapement
│   ├── oscillator
│   ├── motion works / indication
│   ├── jewels
│   ├── shock protection
│   └── fasteners
└── strap interface
```

Entregáveis:
- diagrama funcional;
- BOM preliminar;
- mapa de interfaces;
- inventário de rubis;
- inventário de eixos;
- mapa de centros;
- lista de peças visíveis, parcialmente visíveis e ocultas.

Gate:
Nenhum mecanismo pode existir no CAD sem função documentada ou status explícito de hipótese.

### Fase 3 — Sistema de coordenadas e envelope mestre
Estabelecer:
- origem;
- planos;
- datum;
- orientação consistente;
- envelope de movimento;
- envelope da caixa;
- `Z-budget`.

O `Z-budget` deve ser um artefato de primeira classe. Toda peça recebe:
- `z_min`;
- `z_max`;
- espessura;
- folga inferior;
- folga superior.

Gate:
Somatório nominal e envelopes não podem contradizer 1,18 mm do calibre e 1,75 mm do relógio.

### Fase 4 — Caixa e exterior
Reconstruir:
- contorno;
- bezel;
- caseback/caseband monobloco;
- aberturas;
- parafusos;
- inserts;
- cristais;
- seletores frontais;
- interface de pulseira.

Método:
- vistas oficiais;
- ortogonalização;
- curvas spline paramétricas;
- comparação de silhueta;
- seções transversais.

Entregáveis:
- CAD externo;
- renders ortográficos;
- overlays;
- tabela de desvios.

Gate:
Forma externa consistente em múltiplas vistas, não apenas frontal.

### Fase 5 — Platina e pontes
Começar pelos centros mecânicos e furos funcionais, não pelo skeleton decorativo.

Sequência:
1. centros de rotação;
2. apoios;
3. rubis;
4. fixações;
5. caminhos estruturais;
6. recortes;
7. acabamento.

Gate:
A platina deve suportar logicamente todos os eixos e componentes que o modelo afirma possuir.

### Fase 6 — Barrilete e fonte de energia
Reconstruir:
- tambor;
- arbor;
- tampa;
- dentado;
- apoios periféricos/rolos se confirmados;
- mola como modelo de engenharia separado;
- caminho de torque.

Não inventar a mola "original". Manter:
- `geometry-reconstruction`;
- `functional-surrogate`.

Usar 45 h ± faixa publicada e ~6 h/rev como restrições.

Entregáveis:
- geometria;
- hipótese de mola;
- curva de torque simulada;
- energia total aproximada;
- incertezas.

### Fase 7 — Trem de engrenagens
Tratar como problema discreto + geométrico.

Construir solver para pesquisar combinações de dentes compatíveis com:
- centros medidos;
- diâmetros observados;
- relações necessárias;
- 4 Hz;
- velocidade do barrilete;
- sentido de rotação;
- módulos plausíveis;
- número de estágios observados.

Nunca escolher números de dentes porque "parecem bons".

Manter conjunto de soluções candidatas e eliminá-las por evidência.

Entregáveis:
- tabela de dentes;
- módulos/perfis;
- distâncias entre centros;
- relações;
- velocidades;
- torque relativo;
- overlays.

### Fase 8 — Winding e function selector
Reconstruir a lógica W/H por estados.

Criar state machine:

```text
SELECTOR = W
input crown -> winding path -> barrel

SELECTOR = H
input crown -> hand-setting path -> indication
```

Mapear cada engrenagem, sliding element, lever, cam, detent ou acoplamento necessário.

A cinemática deve demonstrar que os dois estados são mutuamente coerentes.

Gate:
Não basta parecer igual na posição neutra. O conjunto precisa se mover e selecionar caminhos corretos.

### Fase 9 — Escape ultraplano
Usar a patente como fonte estrutural e fotos reais como fonte geométrica.

Reconstruir:
- escape wheel;
- pallets;
- lever/anchor;
- fork;
- impulse jewel;
- roller/plate pertinente;
- geometria anti-overbanking;
- banking;
- locking;
- draw/clearance quando aplicável.

Estudar primeiro o escape suíço convencional para manter uma baseline explícita e depois documentar exatamente o que o RMUP-01 altera.

Criar simulação 2D paramétrica antes de consolidar em 3D.

Gate mínimo:
- lock;
- unlock;
- impulse;
- drop;
- passagem segura;
- ausência de interferência;
- relação compatível com 4 Hz;
- coerência com ângulo de levantamento publicado.

### Fase 10 — Balanço, espiral e choque
Reconstruir:
- balanço de 3 braços;
- seis massas;
- staff;
- impulse feature;
- Kif;
- espiral AK3 como modelo funcional aproximado se a geometria proprietária não for pública.

Separar claramente:
- aparência;
- massa/inércia;
- comportamento oscilatório.

Ajustar o modelo de massa para aproximar o momento de inércia publicado sem falsificar dimensões não conhecidas.

Gate:
O CAD deve ter propriedades de massa auditáveis e relatório comparando-as ao valor publicado.

### Fase 11 — Indicação e motion works
Reconstruir o caminho do ajuste e o caminho de marcha até horas/minutos.

Validar:
- 12 h por revolução para hora;
- 1 h por revolução para minuto quando aplicável à arquitetura real;
- sentidos;
- coaxialidade ou soluções alternativas;
- ausência de sobreposição vertical impossível.

### Fase 12 — Rubis, pivôs, parafusos e retenções
Somente aqui fechar detalhes repetitivos.

Objetivos:
- contabilizar os 23 rubis publicados ou marcar explicitamente o que não foi localizado;
- mapear cada pivô;
- verificar retenção axial;
- verificar acesso de montagem;
- padronizar famílias de parafusos;
- documentar Kif e interfaces.

### Fase 13 — Integração completa
Montar tudo no Fusion.

Obrigatório:
- componentes separados;
- joints/constraints coerentes;
- nomes estáveis;
- parâmetros centralizados;
- nenhuma peça atravessando outra para "fechar visualmente".

Executar:
- interference check;
- clearance check;
- stack-height check;
- envelope check;
- DOF audit;
- motion audit;
- screw access audit.

### Fase 14 — Tolerâncias e fabricabilidade digital
Embora não seja fabricado, executar uma auditoria de plausibilidade.

Criar:
- datums;
- fits;
- endshake;
- side shake;
- backlash;
- folgas de escape;
- concentricidade;
- espessuras mínimas;
- raios de ferramenta;
- regiões frágeis;
- processo provável por peça;
- sequência de montagem.

Não afirmar que tolerâncias inferidas são as originais.

Fazer Monte Carlo para cadeias críticas:
- trem;
- escape;
- altura;
- pivôs;
- caixa-cristal-movimento.

Objetivo:
descobrir se a nossa reconstrução é robusta ou apenas funciona no nominal.

### Fase 15 — Validação forense
Criar uma matriz:

```text
SUBSYSTEM | VISUAL | DIMENSIONAL | KINEMATIC | PHYSICAL | EVIDENCE
case
baseplate
barrel
train
selector
escapement
balance
indication
```

Para cada um:
- evidências utilizadas;
- discrepâncias;
- questões abertas;
- confiança;
- alternativas ainda possíveis.

A reconstrução final NÃO deve esconder incerteza.

### Fase 16 — Acabamento e representação
Somente após engenharia estável:
- acabamentos;
- microtextura;
- polimento;
- gravações;
- materiais;
- rubis;
- transparência dos cristais;
- aparência de titânio;
- iluminação.

Produzir:
- hero renders;
- macro renders;
- vistas ortogonais;
- exploded views;
- cortes;
- wireframes;
- diagramas do trem;
- animações cinemáticas;
- comparação CAD/fotografia.

### Fase 17 — Site de fã e documentação pública
O site deve explicar a engenharia, não imitar a comunicação comercial da marca.

Deixar explícito:
- projeto independente;
- não afiliado;
- educativo;
- reconstrução baseada em fontes públicas;
- marcas pertencem aos respectivos titulares;
- dimensões inferidas são identificadas como tal.

Preferir nossos próprios renders.

Estrutura editorial sugerida:

1. **O problema dos 1,75 mm**
   - escala física;
   - comparação visual de espessura;
   - por que décimos e centésimos importam.

2. **O calibre de 1,18 mm**
   - vista explodida interativa;
   - mapa dos subsistemas;
   - orçamento vertical.

3. **Como o relógio abandona o empilhamento**
   - arquitetura espalhada no plano;
   - relação movimento/caixa.

4. **O barrilete**
   - reserva;
   - rotação de 6 h;
   - fluxo de energia.

5. **O trem**
   - animação de razões;
   - velocidades;
   - torque.

6. **O escape ultraplano**
   - comparação com Swiss lever;
   - visualização do mecanismo patenteado;
   - lock/unlock/impulse;
   - por que eliminar guard pin e safety roller reduz altura.

7. **O balanço**
   - 4 Hz;
   - três braços;
   - massas de inércia;
   - 3 mg·cm²;
   - Kif.

8. **W / H**
   - visualização interativa da seleção de função.

9. **A caixa**
   - titânio grau 5;
   - rigidez;
   - cristais;
   - parafusos;
   - 1,75 mm.

10. **O que sabemos e o que inferimos**
    - painel de evidência;
    - parâmetros A–F;
    - incertezas.

11. **Como reconstruímos**
    - fontes;
    - fotogrametria;
    - solvers;
    - Fusion;
    - validação.

12. **Fontes**
    - bibliografia completa e rastreável.

O site deve permitir que um relojoeiro, engenheiro ou curioso desça em profundidade progressivamente.

---

## 9. Autodesk Fusion como fonte CAD canônica

O modelo final canônico deve viver no Autodesk Fusion.

Usar a API do Fusion quando isso aumentar:
- repetibilidade;
- parametrização;
- geração de famílias;
- validação;
- exportação;
- atualização de dimensões.

Evitar geometria manual irreproduzível quando um script paramétrico for razoável.

Toda dimensão mestre deve vir de `engineering/master-parameters.yaml` ou de um sistema equivalente que possa ser auditado.

Não criar dependência cega em um único arquivo `.f3d`. Exportar periodicamente:
- STEP;
- DXF de perfis importantes;
- CSV de parâmetros;
- screenshots de referência;
- BOM;
- relatórios de massa;
- desenhos de inspeção.

---

## 10. Uso de Python e solvers

Python pode ser usado para:
- metrologia de imagem;
- correção de perspectiva;
- fitting;
- contagem de dentes;
- busca combinatória;
- otimização de razões;
- análise de incerteza;
- Monte Carlo;
- cinemática 2D;
- propriedades de massa;
- geração de relatórios;
- regressão visual.

Não usar um solver como caixa-preta. Guardar:
- função objetivo;
- restrições;
- candidatos;
- resíduos;
- por que uma solução foi escolhida.

---

## 11. Coordenação Claude Code ↔ Codex

Claude Code é o diretor técnico e guardião da coerência do projeto.

Quando houver Codex/agentctl disponível, dividir trabalho por pacotes pequenos e auditáveis.

Claude deve:
- pesquisar;
- formular hipóteses;
- organizar evidência;
- definir interfaces;
- escrever specs;
- revisar resultados;
- rejeitar inferências sem lastro;
- manter a visão global.

Codex deve preferencialmente:
- implementar scripts;
- construir solvers;
- gerar automações do Fusion;
- executar análises;
- preparar testes;
- corrigir CAD/scripts;
- produzir relatórios quantitativos.

Nunca entregar a dois agentes o mesmo problema apenas para "ver quem termina primeiro" sem plano de comparação. Quando usar redundância, ela deve ser deliberadamente independente para medir convergência.

Padrão de pacote em `agent-tasks/`:

```text
TASK-ID
objetivo
contexto
fontes permitidas
entradas
saídas obrigatórias
restrições
questões abertas
testes
critério de aceitação
arquivos que podem ser alterados
arquivos que NÃO podem ser alterados
```

Revisão adversarial:
- agente A propõe;
- agente B tenta falsificar;
- só então integrar.

---

## 12. Testes contínuos

Criar testes automatizados desde cedo.

### Geometria
- bounding box do movimento;
- bounding box da caixa;
- espessura máxima;
- dimensões principais;
- centros críticos;
- simetria apenas quando realmente existente.

### Montagem
- zero interferências não intencionais;
- folgas mínimas;
- acesso de montagem;
- retenção axial.

### Trem
- relações;
- sentidos;
- velocidades;
- center distances;
- engrenamento;
- razão compatível com 4 Hz e barrilete.

### Escape
- lock;
- unlock;
- impulse;
- clearance;
- banking;
- ausência de overbanking no modelo.

### Seletor
- estado W;
- estado H;
- transição;
- ausência de dupla conexão indevida.

### Z-budget
Qualquer commit que exceda envelope conhecido deve falhar.

### Regressão visual
Gerar renders padronizados e comparar com referências/versões anteriores.

---

## 13. Regra contra "CAD bonito e falso"

Reprovar qualquer solução que:
- use uma peça sem função apenas para preencher uma fotografia;
- esconda colisões;
- tenha eixos que não são apoiados;
- tenha roda que não engrena;
- use dimensão inventada como se fosse publicada;
- ignore espessura;
- altere foto/escala para fazer overlay encaixar;
- dependa de uma única imagem quando outras contradizem;
- trate desenho de patente como escala real;
- faça acabamento antes da arquitetura;
- declare "réplica exata" sem evidência suficiente.

---

## 14. Tratamento de incerteza

Incerteza não é falha. É parte do produto.

Para parâmetros importantes, guardar intervalos.

Exemplo:

```yaml
P_TRAIN_CENTER_03:
  nominal_mm: 4.82
  lower_mm: 4.76
  upper_mm: 4.89
  evidence_class: C
  status: provisional
  method: multi_image_fit
  sources:
    - IMG-0041
    - IMG-0118
    - IMG-0207
```

Se uma escolha for discreta:

```yaml
third_wheel_teeth:
  candidates: [63, 64, 65]
  preferred: 64
  evidence_class: D
  status: contested
  discriminating_test: "high-resolution edge image or verified train ratio"
```

---

## 15. Versionamento do conhecimento

Toda descoberta que muda o entendimento deve gerar:
- atualização do evidence ledger;
- alteração em `FACTS` ou `HYPOTHESES`;
- entrada no `CHANGELOG`;
- novo teste ou ajuste de teste quando possível.

O CAD deriva do conhecimento; o conhecimento não pode existir apenas escondido dentro do CAD.

---

## 16. Milestones

Não usar calendário como principal medida. Usar gates.

### M0 — Research system alive
Corpus, evidência, IDs, backlog.

### M1 — Known geometry envelope
Exterior e movimento com envelopes e datums.

### M2 — Mechanical skeleton
Todos os centros, eixos e subsistemas principais representados.

### M3 — Kinematic skeleton
Fluxo de energia completo e W/H funcional em baixo detalhe.

### M4 — Escapement solved
Escape e oscilador coerentes com a evidência disponível.

### M5 — Full nominal assembly
Assembly completo sem colisões nominais intencionais.

### M6 — Evidence-converged CAD
Maioria das dimensões importantes em A–D; placeholders críticos eliminados.

### M7 — Plausibility audit
Tolerâncias, Monte Carlo, montagem e processos avaliados.

### M8 — Forensic digital twin v1
Modelo, relatórios, renders, animações e documentação.

### M9 — Public knowledge site
Site editorial/interactive sustentado pelo próprio corpus.

---

## 17. Critério de "concluído"

Nunca usar "100% idêntico" como critério.

A versão v1 é considerada madura quando:

- o envelope oficial é respeitado;
- a arquitetura visual converge com as melhores imagens disponíveis;
- a cadeia de energia é funcional no modelo;
- W/H funciona cinematicamente;
- o trem possui solução de dentes e relações defendida por evidência;
- o escape possui ciclo demonstrável;
- balanço e propriedades de massa são coerentes com os dados publicados dentro da incerteza modelada;
- os 23 rubis foram localizados ou os não localizados estão explicitamente documentados;
- o `Z-budget` fecha;
- não há colisões nominais inexplicadas;
- a BOM reconstruída está versionada;
- cada parâmetro crítico tem provenance;
- não existem placeholders ocultos;
- existe relatório de discrepâncias;
- existe lista explícita do que permanece desconhecido;
- o site pode explicar tanto a grandeza do original quanto as limitações da reconstrução.

---

## 18. Primeira sequência de trabalho

Ao receber este `CLAUDE.md`, NÃO comece modelando.

Faça, nesta ordem:

1. Leia todo o repositório existente.
2. Crie `PROJECT-CHARTER.md`.
3. Crie os schemas de fontes, claims, evidência e parâmetros.
4. Faça uma pesquisa inicial ampla somente de fontes primárias e patentes.
5. Registre as âncoras conhecidas, uma por uma, com fonte.
6. Monte uma árvore de patentes e famílias relacionadas.
7. Faça uma pesquisa técnica de desmontagens e fotos de montagem.
8. Construa um catálogo de imagens por vista/subsistema.
9. Liste todas as questões desconhecidas.
10. Produza uma decomposição funcional do relógio.
11. Produza um `MASTER-RESEARCH-PLAN.md`.
12. Produza um `CAD-RECONSTRUCTION-PLAN.md`.
13. Produza um `VALIDATION-PLAN.md`.
14. Somente depois crie o primeiro envelope paramétrico no Fusion.
15. Nunca passe para alto detalhe se as fundações anteriores ainda estiverem frágeis.

A primeira entrega para revisão humana deve conter pesquisa e planejamento, NÃO um relógio "pronto".

---

## 19. Pergunta que governa todo o projeto

Para cada peça, parâmetro ou afirmação, pergunte:

**"Como sabemos disso?"**

Se a resposta não puder ser registrada em evidência, a coisa ainda não é fato.

E para cada solução mecânica:

**"Se eu removesse o render bonito e olhasse apenas para os contatos, eixos, relações, folgas, restrições e energia, isso ainda faria sentido como um relógio?"**

Se não, ainda não está pronto.

---

## 20. Tom do projeto

Tratar o RM UP-01 como objeto de engenharia e relojoaria, não como objeto de hype.

O futuro site deve transmitir admiração por meio da explicação precisa:
- quão pequeno é o orçamento vertical;
- por que cada décimo importa;
- como mecanismos tradicionais tiveram de ser reorganizados;
- o que foi patenteado;
- onde há trade-offs;
- como movimento e caixa cooperam;
- como um relógio completo pode continuar mecanicamente tradicional em certos princípios e radical em sua geometria.

O projeto será bem-sucedido não quando produzirmos a imagem mais bonita, mas quando conseguirmos explicar cada detalhe do nosso modelo, apontar a fonte de cada certeza e admitir cada lacuna restante.
