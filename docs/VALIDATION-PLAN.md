# VALIDATION-PLAN — como saberemos que a reconstrução está certa (e onde ela não está)

Escrito pela SÍNTESE DA FASE 1 em 2026-09-21. Corresponde ao item 13 do `CLAUDE.md` §18 e cobre o §12
(testes contínuos), o §15 (matriz forense) e o §17 (critério de "concluído").

**Princípio.** Validar aqui não é demonstrar semelhança com uma fotografia. É demonstrar que o modelo
respeita as restrições publicadas, que se move, que não se atravessa, e que **sabe dizer de onde veio cada
número**. Um modelo que parece idêntico e não fecha o Z-budget está reprovado; um modelo feio que fecha
tudo e declara suas incertezas está aprovado.

---

## 1. Primeiro item: o teste barato de alto retorno

> **V-000 — O render oficial é geometricamente fiel? (Q-IMG-003)**
> Cruzar os centros medidos em **IMG-0001** (render CG oficial do calibre) com os centros medidos em
> **IMG-0026** (quadro do filme com a **platina nua** no suporte de montagem).

**Por que este primeiro.** IMG-0001 é a imagem mais informativa do corpus inteiro sobre a arquitetura do
movimento — e é um render, isto é, a interpretação do departamento de comunicação. IMG-0026 é a única
imagem pública em que os furos de pivô do lado do trem não estão cobertos por pontes — mas mostra a platina
sem as rodas. As duas são complementares e uma valida a outra. O teste custa uma tarde e decide o regime de
trabalho de duas fases inteiras.

**Procedimento.**
1. Homografia em IMG-0026 usando o contorno da platina (41,45 × 28,85 mm) como âncora, com as hastes retas
   e paralelas do suporte de montagem estimando os pontos de fuga.
2. Homografia em IMG-0001 usando o mesmo contorno, com a ressalva de que o objeto está inclinado ~10–15°
   em torno do eixo vertical e ~5° em torno do horizontal.
3. Medir em ambas: centro do barrilete, centros das duas rodas do prolongamento esquerdo, centros dos furos
   de pivô do lado direito, centro do balanço (só em IMG-0001), e as gravações `23 JEWELS / RMUP-01 / N001`
   como pontos de correspondência de superfície.
4. Registrar as duas nuvens de centros no mesmo sistema e calcular o resíduo ponto a ponto.

**Critério de decisão.**

| Resultado | Consequência |
|---|---|
| Resíduo dentro da incerteza combinada das duas homografias | O render vira **guia topológico legítimo** (classe D para posições, nunca A). Q-IMG-003 fecha. As Fases 5 e 7 ganham a vista mais completa do calibre. |
| Resíduo fora da incerteza, mas com topologia preservada | O render fica **ilustrativo**: serve para saber *o que* existe e *onde procurar*, nunca para medir. Toda posição volta a depender de IMG-0026. |
| Topologia divergente (peça que existe num e não no outro) | O render é **descartado** como fonte de qualquer coisa, e isso vira achado publicável: a marca divulgou um calibre que não é o calibre. |

**Saídas obrigatórias:** overlay das duas nuvens guardado em `evidence/overlays/`; tabela de resíduos em
`evidence/measurements/`; linhas no `evidence-ledger.csv`; atualização de Q-IMG-003 com o veredito.
Pacote: **TASK-P2-001**.

---

## 2. Testes por família (§12)

Todos automatizados em `tests/`, rodando sobre os CSV do repositório e sobre os STEP exportados do Fusion —
sem depender do Fusion estar aberto. Um teste que só pode ser conferido a olho não é teste.

### 2.1 Geometria — `tests/geometry/`

| ID | Teste | Critério | Depende de |
|---|---|---|---|
| V-G01 | Bounding box do movimento | ≤ 41,45 × 28,85 × 1,18 mm, com tolerância de modelagem declarada | Fase 3 |
| V-G02 | Bounding box da caixa | ≤ 51,00 × 39,00 mm | Fase 4 |
| V-G03 | Espessura máxima do relógio | = 1,75 mm no ponto definido por Q-CASE-002 | Fase 4 |
| V-G04 | Parede mínima da caixa | nenhum ponto abaixo de 0,18 mm | Fase 4 |
| V-G05 | Centros críticos | cada centro do CAD bate com o centro medido, dentro da incerteza registrada | Fase 5 |
| V-G06 | Simetria | **só** onde realmente observada; o teste reprova simetria imposta sem evidência | Fase 4 |

### 2.2 Montagem — `tests/collisions/`

| ID | Teste | Critério |
|---|---|---|
| V-M01 | Interferências | zero interferências não intencionais; toda interferência intencional tem `interface_id` do tipo `press` ou `contact` |
| V-M02 | Folgas mínimas | nenhuma folga menor que o mínimo declarado por família, e **nenhuma folga zero sem interface declarada** |
| V-M03 | Acesso de montagem | cada peça tem trajetória de inserção sem atravessar outra; cada parafuso tem acesso de ferramenta |
| V-M04 | Retenção axial | todo eixo tem retenção declarada nos dois sentidos — inclusive o arbor do barrilete (Q-BAR-003), que é o caso difícil |
| V-M05 | Eixos apoiados | todo eixo tem os dois mancais existentes na platina ou numa ponte; eixo flutuante reprova |

### 2.3 Trem — `tests/ratios/`

| ID | Teste | Critério |
|---|---|---|
| V-T01 | Razão total | barrilete → roda de escape compatível com 4 Hz e 6 h/volta, para o número de dentes adotado (5 760 com 15 dentes; 4 800 com 18; 4 320 com 20) |
| V-T02 | Voltas úteis | 45 h ÷ 6 h = 7,5 voltas, dentro de 6,75–8,25 pela tolerância publicada |
| V-T03 | Sentidos | sentido de rotação alternando corretamente ao longo do trem, e coerente com o sentido de corda observado |
| V-T04 | Distância entre centros | igual a m·(z₁+z₂)/2 para cada par, dentro da incerteza dos centros medidos |
| V-T05 | Engrenamento real | todo par tem engrenamento geométrico verificado, com backlash positivo; **roda que não engrena reprova** |
| V-T06 | Indicação | minuto a 1 volta/h e hora a 1 volta/12 h, verificados por propagação de razões a partir do barrilete |

### 2.4 Escape — `tests/kinematics/`

| ID | Teste | Critério |
|---|---|---|
| V-E01 | Lock | travamento em ambas as pedras, com repouso estável |
| V-E02 | Unlock | desengate ocorre com a cheville dentro da forquilha, conforme a condição caracterizante da reiv. 1 |
| V-E03 | Impulse | impulso transmitido pela parede **interna** da corna |
| V-E04 | Drop | drop positivo nas duas pedras, sem contato prematuro |
| V-E05 | Banking | debate limitado pela solução adotada (entalhe na platina, goupilles, ou forquilha) — e o **ângulo total resultante** é coerente com o ciclo |
| V-E06 | Anti-renversement | a parede externa da corna encosta na periferia do plateau e **não entra no entalhe** fora da janela permitida (condição da reiv. 2) |
| V-E07 | Ângulo de levantamento | o levantamento simulado bate com os 54° publicados, dentro da incerteza do modelo |
| V-E08 | Sem overbanking no modelo | simulação de rebat não produz travamento |

### 2.5 Seletor — `tests/kinematics/`

| ID | Teste | Critério |
|---|---|---|
| V-S01 | Estado W | o caminho coroa → barrilete está fechado e o caminho de acerto está aberto |
| V-S02 | Estado H | o caminho coroa → indicação está fechado **e o barrilete está desacoplado** |
| V-S03 | Transição | o braço percorre o curso sem colidir e sem passar por um estado de dupla conexão |
| V-S04 | Ausência de dupla conexão | em nenhuma posição intermediária os dois caminhos estão simultaneamente acoplados |
| V-S05 | Limitador de torque | o modelo declara onde está e como funciona, ou declara que é hipótese |

### 2.6 Z-budget — `tests/stack_height/`

| ID | Teste | Critério |
|---|---|---|
| V-Z01 | Coluna do balanço | piso + movimento local + cristal 0,20 + folgas ≤ 1,75 mm |
| V-Z02 | Coluna da indicação | roda **duas vezes**, Hipótese A (0,45) e Hipótese B (0,20), e registra em qual fecha |
| V-Z03 | Teto do calibre | nenhuma coluna do movimento acima de 1,18 mm |
| V-Z04 | Continuidade | `z_max` de uma peça + folga = `z_min` da seguinte, sem buracos nem sobreposições não declaradas |
| V-Z05 | Placeholders | nenhuma camada `F` entra numa soma apresentada como resultado |

**Qualquer commit que exceda envelope conhecido falha.** Isso é o §12 literal e não tem exceção.

### 2.7 Massa e física — `tests/regression/`

| ID | Teste | Critério |
|---|---|---|
| V-P01 | Massa do movimento | soma das massas = 2,82 g dentro da incerteza dos materiais; densidade aparente ≈ 2,0 g/cm³, ou seja, o calibre é ~55% vazio — modelo maciço reprova |
| V-P02 | Inércia do balanço | momento de inércia do conjunto = 3 mg·cm², com relatório de como se chegou lá |
| V-P03 | Energia do barrilete | energia armazenada compatível com 45 h ± 10% na curva de torque simulada |
| V-P04 | Massa da cabeça | comparada com 11,2 g, com a divergência de Q-CASE-006 explicitada |

### 2.8 Regressão visual — `tests/regression/`

Renders padronizados (mesma câmera, mesma luz, mesmo enquadramento) comparados entre versões e contra as
referências fotográficas. **Nunca contra IMG-0014…IMG-0025** (render de terceiro) e, enquanto Q-IMG-003
estiver aberta, nunca contra IMG-0001 como se fosse o objeto.

---

## 3. Matriz forense (§15)

Preenchida a cada marco. `—` = ainda não avaliado. Estado em 2026-09-21, fim da Fase 1: **nada foi medido
ainda**, e a matriz registra isso honestamente.

| Subsistema | VISUAL | DIMENSIONAL | CINEMÁTICO | FÍSICO | EVIDÊNCIA DISPONÍVEL | Alternativas ainda possíveis |
|---|---|---|---|---|---|---|
| **case** | — | — | n/a | — | A para 51×39×1,75, 0,18 mm, 13 parafusos, 1 atm; sprite 360° com 81 vistas; 6 vistas ortogonais do USD991795 | onde valem os 1,75 mm; onde estão os 0,18 mm; corpo+tampa × monobloco puro |
| **crystals** | — | — | n/a | — | A para 0,20/0,30; **contestada** para 0,45 | 0,45 × 0,20; cristal estrutural × cristal apoiado |
| **baseplate** | — | — | n/a | — | **IMG-0026, platina nua** — melhor ativo do projeto; A para material e acabamento | espessura da platina; tudo do lado do mostrador |
| **bridges** | — | — | n/a | — | IMG-0003 + IMG-0028 (par de vistas da mesma peça) | quantas pontes; que eixos a ponte de 3 braços fecha |
| **barrel** | — | — | — | — | A para 6 h/volta e 45 h; B para ausência de receptáculo | rolete × bucha; 4 × outro número; geometria da mola |
| **winding** | — | — | — | n/a | A para ausência de haste; B para as duas rodas em IMG-0026 | topologia do acoplamento; princípio do limitador de torque |
| **selector** | — | — | — | n/a | B para o braço deslizante (stills do filme) | came × alavanca; com × sem posição neutra |
| **going train** | — | — | — | — | B para a roda intermediária; A para involuta 20° | número de estágios; dentes; idler × estágio de multiplicação |
| **escapement** | — | — | — | — | A para a topologia (sem dardo, sem plateau duplo); D para a identificação com a família de 2019 | reiv. 4 × reiv. 5 (cheville); entalhe × goupilles; 15/18/20 dentes |
| **oscillator** | — | — | — | — | A para 3 mg·cm², 54°, 3 braços, 6 massas, AK 3, Kif | diâmetro e massas que produzem 3 mg·cm²; 3 braços do balanço × da ponte |
| **indication** | — | — | — | n/a | A para ponteiros sem canhão, confirmado em IMG-0030/0031 | coaxial × não coaxial; trem próprio × derivação do trem de marcha |
| **jewels** | — | — | n/a | n/a | A só para a contagem (23) | distribuição inteira |
| **shock** | — | — | — | — | A só para a existência do Kif | modelo, quantidade, posição |

**Como preencher.** Cada célula recebe, quando avaliada: classe de evidência atingida, discrepância medida,
questões abertas restantes e alternativas ainda vivas. **A matriz nunca esconde incerteza** — uma célula
vazia é informação, e uma célula que diz "alternativas: nenhuma" precisa provar por que as outras morreram.

---

## 4. Critério de "concluído" (§17) mapeado a testes

Cada linha do §17 vira uma condição verificável. A v1 é madura quando **todas** passam.

| Critério do §17 | Teste que o demonstra | Estado hoje |
|---|---|---|
| O envelope oficial é respeitado | V-G01, V-G02, V-G03, V-G04 | não avaliado |
| A arquitetura visual converge com as melhores imagens | V-000 + regressão visual + tabela de desvios da Fase 4 | não avaliado |
| A cadeia de energia é funcional no modelo | V-T01…V-T05, V-P03 | não avaliado |
| W/H funciona cinematicamente | V-S01…V-S04 | não avaliado |
| O trem tem solução de dentes defendida por evidência | V-T01, V-T04, V-T05 + conjunto de candidatos do `gear_search` com resíduos | não avaliado |
| O escape tem ciclo demonstrável | V-E01…V-E08 | não avaliado |
| Balanço e massa coerentes com o publicado | V-P01, V-P02 | não avaliado |
| Os 23 rubis localizados, ou os não localizados documentados | inventário de `bom-reconstructed.csv` × 23, com lista explícita de faltantes | **0 de 23 localizados** |
| O `Z-budget` fecha | V-Z01…V-Z05, nas duas hipóteses de cristal | não avaliado |
| Sem colisões nominais inexplicadas | V-M01, V-M02 | não avaliado |
| BOM reconstruída versionada | `engineering/bom-reconstructed.csv` sob git, com `part_id` permanente | **feito** (60 peças) |
| Cada parâmetro crítico tem provenance | auditoria automática de `master-parameters.yaml`: todo parâmetro com `evidence_class`, `sources`, `method`, `status` | 22 parâmetros com provenance completa |
| Sem placeholders ocultos | V-Z05 + relatório de placeholders; nenhum `F` usado como se fosse medido | 3 placeholders **declarados** (`P_MOV_OFFSET_X/Y/Z`) |
| Relatório de discrepâncias | matriz forense do §3 preenchida | estrutura pronta, células vazias |
| Lista explícita do que permanece desconhecido | `docs/OPEN-QUESTIONS.md` consolidado | **feito** (81 questões, priorizadas) |
| O site explica a grandeza do original e os limites da reconstrução | Fase 17, com Q-IMG-007 dita na cara | não iniciado |

**Um critério que este projeto acrescenta ao §17:** *nenhuma peça no CAD sem `part_id`, função e status*.
Uma peça anônima é uma peça inventada, e a BOM existe exatamente para tornar isso impossível.

---

## 5. Revisão adversarial

O `CLAUDE.md` §11 manda: agente A propõe, agente B tenta falsificar, só então integra. Aqui isso se aplica
aos três lugares onde o erro é mais provável e menos visível:

1. **Toda medida de imagem** é refeita por um segundo pacote em imagem independente, e a dispersão entra no
   ledger. Uma medida com fonte única fica `provisional`, nunca `confirmed`.
2. **Toda solução do `gear_search`** é atacada com o conjunto de candidatos vizinhos: se o segundo melhor
   candidato estiver dentro da incerteza dos centros, os dois sobrevivem.
3. **Toda hipótese que vira fato** passa por uma tentativa explícita de falsificação registrada em
   `docs/FAILURE-LOG.md`. H-IND-101 é o caso a vigiar: é a suposição mais sedutora do corpus e a mais fácil
   de virar "fato" por repetição.

E uma regra de higiene que a Fase 1 comprou caro: **uma entrega que afirma um número sem fonte verificável
é rejeitada inteira**, não corrigida parcialmente. Corrigir parcialmente é como uma reconstrução forense
morre — um número bom carrega dez ruins.
