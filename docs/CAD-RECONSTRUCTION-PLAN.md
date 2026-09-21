# CAD-RECONSTRUCTION-PLAN — coordenadas, envelope, Z-budget e ordem das fases

Escrito pela SÍNTESE DA FASE 1 em 2026-09-21. Corresponde ao item 12 do `CLAUDE.md` §18.
Nada aqui é CAD: é a especificação de como o CAD será feito, e as restrições que ele terá de respeitar.

---

## 1. Sistema de coordenadas

**Unidade:** milímetro. **Ângulos:** grau. **Regra da mão direita.**

### 1.1 Datums do movimento (sistema mestre)

O sistema mestre é o **do movimento**, não o da caixa, por uma razão de evidência: 41,45 × 28,85 mm é a
âncora de calibração fotográfica mais forte do projeto (classe A, repetida em cinco idiomas, e visível
isolada em IMG-0004 e IMG-0026). Amarrar a origem a ela é amarrá-la ao número mais bem sustentado que
temos.

| Datum | Definição | Classe |
|---|---|---|
| **A** (primário) | Plano da **face inferior da platina** — a face que encosta no fundo da caixa. `z = 0`. | D — a planicidade dessa face é hipótese razoável, a confirmar contra o rebaixo IFC-006 |
| **B** (secundário) | Eixo longo do movimento, 3h→9h, no plano A. Define **+X para 3h**. | D via H-BASE-001 (41,45 mm é este eixo) |
| **C** (terciário) | Eixo curto, 6h→12h, ortogonal a B no plano A. Define **+Y para 12h**. | D |
| Origem | Centro do retângulo envolvente 41,45 × 28,85 mm, sobre o plano A. | D |
| +Z | Do fundo para o cristal (*dial-up*). | por construção |

Convenção horária derivada: 12h em +Y, 3h em +X, 6h em −Y, 9h em −X. O ângulo horário θ de um ponto é
medido a partir de +Y no sentido horário visto de +Z, de modo que "entre 10h e 11h" é o quadrante
−X/+Y (canto superior esquerdo) e "entre 7h e 8h" é −X/−Y (canto inferior esquerdo) — coerente com o
prolongamento esquerdo da platina (IMG-0026) e com as gravações de IMG-0006.

### 1.2 Datums da caixa

| Datum | Definição |
|---|---|
| **A'** | Plano da face externa do fundo. `z' = 0`. |
| **B'/C'** | Eixos longo (51,00 mm) e curto (39,00 mm) da caixa. |
| Origem da caixa | Centro do retângulo envolvente 51,00 × 39,00 mm sobre A'. |

**Transformação caixa→movimento** — três parâmetros, hoje todos desconhecidos:

```yaml
P_MOV_OFFSET_X: {nominal: 0.00, unit: mm, evidence_class: F, status: placeholder,
                 notes: "deslocamento do centro do movimento em relação ao centro da caixa, eixo 3h-9h;
                         a folga total é 51,00 - 41,45 = 9,55 mm e a repartição não é publicada (Q-BASE-002)"}
P_MOV_OFFSET_Y: {nominal: 0.00, unit: mm, evidence_class: F, status: placeholder,
                 notes: "folga total 39,00 - 28,85 = 10,15 mm (Q-BASE-002)"}
P_MOV_OFFSET_Z: {nominal: null, unit: mm, evidence_class: F, status: placeholder,
                 notes: "altura da face inferior da platina acima da face interna do fundo; negativa se o
                         movimento afundar no rebaixo IFC-006 (Q-CASE-003)"}
```

Os três nascem `F — PLACEHOLDER` com valor zero **declarado como placeholder**, e o teste automático
`test_no_hidden_placeholders` reprova qualquer commit que os use como se fossem medidos. TASK-P2-002 mede
os dois primeiros em IMG-0027.

### 1.3 Regra de nomeação de centros

Todo centro de rotação recebe `P_<SUB>_CENTER_<NNN>_X` / `_Y`, com incerteza e lista de imagens de origem,
no formato do `CLAUDE.md` §14. Nenhum centro entra no CAD sem `evidence_class` e sem dispersão medida em
pelo menos duas imagens independentes (§7, item 8).

---

## 2. Envelope mestre

| Envelope | Valor | Classe | Observação |
|---|---|---|---|
| Caixa, X | 51,00 mm | A | eixo 3h–9h |
| Caixa, Y | 39,00 mm | A | |
| Caixa, Z | 1,75 mm | A | **onde** no contorno curvo este valor se aplica é Q-CASE-002 |
| Movimento, X | 41,45 mm | A | H-BASE-001 |
| Movimento, Y | 28,85 mm | A | |
| Movimento, Z | 1,18 mm | A | valor **máximo** do calibre, não uniforme |
| Folga lateral total, X | 9,55 mm | D | repartição desconhecida |
| Folga lateral total, Y | 10,15 mm | D | idem |
| Massa do movimento | 2,82 g | A | restrição global de massa do CAD |
| Massa da cabeça | 11,2 g | A, contestada | Q-CASE-006 |

**Regra de envelope:** nenhum sólido pode ultrapassar o envelope da caixa; nenhum sólido do movimento pode
ultrapassar o envelope do movimento. Violação reprova o commit (§12).

---

## 3. A superfície não é um prisma

O relógio é curvo no eixo longo: IMG-0007 e IMG-0011 mostram a silhueta como **envoltória do sólido**, não
como seção. Consequências para o CAD:

1. O envelope de 1,75 mm é um **envelope local**, não uma altura constante. O modelo paramétrico da caixa
   precisa de uma curva de perfil, não de uma extrusão.
2. Medir Z em qualquer foto de perfil sem tratar a curvatura produz um número errado — é exatamente o erro
   que o §13 proíbe ("altere foto/escala para fazer overlay encaixar").
3. O sprite 360° (81 quadros de 800 × 800, passo de 4,44°, duas iluminações) é o insumo certo: 81 vistas
   auto-consistentes do mesmo objeto, com rotação de eixo único e passo constante. O ajuste conjunto
   multivista sobre elas é o caminho defensável para o contorno (TASK-P2-003).

---

## 4. Z-budget inicial

> **Este é o artefato de primeira classe do `CLAUDE.md` §8 Fase 3.** Vive em
> `engineering/stack-height.csv`; o que segue é a especificação dele e a aritmética que ele tem de honrar.

### 4.1 A descoberta desta síntese: o orçamento é por coluna, não global

O TASK-P1-001 observou que sobram 1,75 − 1,18 = **0,57 mm** fora do movimento e concluiu que 0,45 mm de
cristal deixaria a conta "muito apertada", tratando isso como argumento a favor de H-CRY-001 (os dois
cristais a 0,20 mm).

**O argumento não se sustenta quando a conta é feita corretamente.** O relógio não tem uma pilha vertical:
tem várias, e cada abertura do cristal fica sobre uma região diferente do movimento. Os 1,18 mm são a
espessura **máxima** do calibre, atingida onde estão o barrilete e o oscilador — não sob a indicação, onde
há apenas rodas-lâmina com ponteiros decalcados e nenhum canhão (CLM-0037).

Fazendo o orçamento coluna a coluna:

**Coluna do balanço** (onde o movimento é mais alto e o cristal é o mais fino):

| Camada | Espessura | Classe |
|---|---|---|
| Piso do fundo da caixa | ≥ 0,18 | A (é o mínimo declarado; o piso real pode ser maior) |
| Folga fundo ↔ movimento | ? | F |
| Movimento (altura local ≈ máxima) | ≤ 1,18 | A |
| Folga movimento ↔ cristal | ? | F |
| Cristal do balanço | 0,20 centro / 0,30 borda | A |
| **Soma mínima** | **1,56** | |
| **Resta para as duas folgas + ressalto da luneta** | **0,19** | |

A coluna fecha, e fecha apertada: 0,19 mm para tudo que não é material declarado. É uma restrição forte e
utilizável — por exemplo, ela sozinha torna improvável qualquer folga superior maior que ~0,08 mm.

**Coluna da indicação** (onde o cristal é o espesso):

| | Hipótese A — cristal 0,45 | Hipótese B — cristal 0,20 |
|---|---|---|
| Piso do fundo | ≥ 0,18 | ≥ 0,18 |
| Altura local do movimento sob a indicação | **≤ 1,12** | ≤ 1,37 (sem restrição útil: o teto já é 1,18) |
| Cristal | 0,45 | 0,20 |
| Soma | 1,75 com folga zero | 1,56, sobrando 0,19 |
| Consequência | a região da indicação tem de ser **pelo menos 0,06 mm mais baixa** que o ponto mais alto do calibre, e a folga acima dela é praticamente nula | nenhuma consequência geométrica |

A Hipótese A não é impossível: ela é **uma previsão específica e testável**. E ela tem duas confirmações
independentes esperando:

- **CLM-0420** (fonte japonesa): o eixo da indicação se apoia **contra o cristal**. Folga superior nula na
  coluna da indicação é exatamente o que a Hipótese A exige.
- **A assimetria dos dois cristais** deixa de ser estranha: o cristal grosso está sobre a região baixa do
  movimento, e o fino sobre a região alta. É a solução de um engenheiro, não uma inconsistência.

**Conclusão de método:** o Z-budget **não decide Q-CRY-001** — nem a favor nem contra. Ele transforma a
questão num teste geométrico: *a região da indicação é mais baixa que a do balanço, e por quanto?* Se for
por ≥ 0,06 mm, a ficha técnica (0,45 mm) fica coerente; se o movimento for sensivelmente plano por cima,
a narrativa (0,20 mm) ganha força. **A decisão de Pedro sobre Q-CRY-001 pode, portanto, ser adiada sem
travar a Fase 3**, desde que o modelo carregue as duas colunas em paralelo. Ver DEC-005.

### 4.2 Regras do `stack-height.csv`

1. Toda peça tem `z_min`, `z_max`, `thickness`, `clearance_below`, `clearance_above`, classe e status.
2. **Duas colunas de cristal** convivem: o arquivo carrega os campos `z_*` para a Hipótese A e a Hipótese B
   enquanto Q-CRY-001 estiver aberta. O teste de Z-budget roda duas vezes; uma configuração que só fecha
   numa das duas é aceitável **e a informação de qual delas é registrada**.
3. Folga nunca é zero por conveniência. Folga zero é uma afirmação mecânica (contato) e precisa de
   interface em `interfaces.csv` — é o caso de IFC-008.
4. Toda camada cuja espessura seja placeholder é marcada `F` e aparece num relatório de placeholders que o
   §17 exige zerar antes da v1.
5. O somatório nominal não pode contradizer 1,18 mm nem 1,75 mm. Isso é teste automático, não revisão.

### 4.3 Restrições verticais conhecidas, uma a uma

| Restrição | Valor | Origem | Efeito |
|---|---|---|---|
| Relógio | 1,75 mm | A | teto absoluto |
| Calibre | 1,18 mm | A | teto do movimento |
| Parede mínima da caixa | 0,18 mm | A | piso do fundo e da luneta |
| Cristal das horas | 0,45 **ou** 0,20 mm | A, contestada | duas colunas |
| Cristal do balanço | 0,20 / 0,30 mm | A | superfície não plana: modelar como lente, não como disco |
| Rebaixo interno da caixa | existe, profundidade desconhecida | B / F | pode dar folga negativa (o movimento afunda) |
| Degrau nos braços do balanço | existe | B | recupera altura no oscilador; quanto é Q-OSC-004 |
| Espiral plana, sem overcoil | — | B | a espiral não pode ocupar um nível próprio acima do aro |
| Sem canhão de ponteiro | — | A | elimina um nível inteiro na indicação |
| Sem plateau duplo no escape | — | A | elimina um nível no oscilador |
| Cheville no plateau ou no balanço | duas variantes | D | **um nível inteiro de diferença** (Q-ESC-006) |
| Barrilete sem receptáculo | — | B | toda a altura do andar vira largura de mola |

---

## 5. O que vai para o Fusion e o que fica aqui

A Dell não tem Fusion (o Fusion está na máquina de Pedro). Isso não é limitação temporária a contornar: é
divisão de trabalho, e define o que cada lado produz.

**Aqui (Dell, Python 3.12 + CadQuery + numpy/PIL/opencv):**
- toda a metrologia de imagem, homografias, overlays e relatórios de dispersão;
- os solvers (busca de dentes, cinemática 2D, ajuste de geometria);
- geometria auxiliar e protótipos 2D/3D em CadQuery, exportados em STEP — **modelos de estudo**, não o
  modelo canônico;
- todos os testes automáticos (`tests/`), inclusive os de Z-budget e de envelope, que rodam sobre os CSV e
  os STEP exportados, sem precisar do Fusion;
- **os scripts da API do Fusion**, escritos e revisados aqui, executados lá.

**Lá (Fusion, máquina de Pedro):**
- o modelo canônico paramétrico, com componentes separados, joints coerentes e nomes estáveis;
- todos os parâmetros vindos de `engineering/master-parameters.yaml` — nenhuma dimensão digitada à mão;
- interference check, clearance check, DOF audit, motion audit e relatórios de massa;
- os renders da Fase 16.

**Contrato entre os dois lados.** O Fusion nunca é a fonte da verdade: `master-parameters.yaml` é. Cada
sessão no Fusion termina exportando STEP, CSV de parâmetros, BOM e relatório de massa de volta para o
repositório, e é sobre esses arquivos que os testes rodam. Se o CAD e o YAML divergirem, o YAML vence e o
CAD é regerado.

---

## 6. Ordem das fases 3 → 13, com gates

| Fase | Entrega | Gate para sair |
|---|---|---|
| **3** Coordenadas e envelope | Datums acima implementados; `stack-height.csv` com as duas colunas; `P_MOV_OFFSET_*` medidos | Somatório nominal e envelopes não contradizem 1,18 nem 1,75 mm, nas duas hipóteses de cristal; nenhum placeholder sem marca |
| **4** Caixa e exterior | Contorno por ajuste multivista do sprite 360°; perfil curvo; aberturas; cristais; comandos; interface de pulseira | Silhueta consistente em ≥ 3 vistas independentes, com tabela de desvios; o perfil reproduz 1,75 mm no ponto decidido em Q-CASE-002 |
| **5** Platina e pontes | Centros medidos em IMG-0026; rubis; fixações; recortes; só então acabamento | A platina suporta **todos** os eixos que o modelo afirma ter; nenhum eixo flutuando |
| **6** Barrilete | Tambor, arbor, apoios periféricos, mola como modelo separado, curva de torque | Energia total compatível com 45 h ± 10% e 7,5 voltas; as duas leituras dos apoios (bucha × rolete) modeladas como variantes |
| **7** Trem | `gear_search` sobre centros medidos; tabela de dentes candidatos com resíduos | Razão total compatível com 4 Hz e 6 h/volta; engrenamento real em todos os pares; nenhuma escolha de dentes "porque parece boa" |
| **8** Corda e seletor | Máquina de estados W/H; coroas-roda; limitador de torque | Os dois estados se movem e selecionam caminhos corretos; **nenhuma dupla conexão** em nenhum estado |
| **9** Escape | Simulação 2D paramétrica antes do 3D; baseline suíço explícito ao lado | Ciclo lock/unlock/impulse/drop fechado, sem interferência, coerente com 54° e 4 Hz |
| **10** Oscilador | Balanço, 6 massas, espiral funcional, Kif | Propriedades de massa auditáveis e relatório comparando com 3 mg·cm² |
| **11** Indicação | Caminho de marcha e caminho de acerto até hora e minuto | 12 h e 1 h por revolução verificados; sentidos corretos; sem sobreposição vertical impossível |
| **12** Rubis, pivôs, parafusos | Os 23 rubis localizados **ou** explicitamente listados como não localizados | Cada pivô mapeado; retenção axial verificada; acesso de montagem verificado |
| **13** Integração | Assembly completo no Fusion | Interference, clearance, stack-height, envelope, DOF, motion e screw access — todos passando |

**A ordem não é negociável em dois pontos.** A Fase 5 não começa antes da Fase 3 (sem datum, centro medido
não tem onde morar), e a Fase 7 não começa antes da Fase 5 (o `gear_search` sem centros medidos degenera em
busca de números bonitos, que é precisamente o que o §7 proíbe).

---

## 7. Aritmética que o CAD tem de honrar

Deduções de classe **D**, obtidas só de valores publicados. Elas são restrição, não resultado.

**Voltas úteis da mola.** 45 h ÷ 6 h/volta = **7,5 voltas**. Com a tolerância publicada: 6,75 a 8,25 voltas.
É um número alto para um barrilete de relógio de pulso e é coerente com a decisão de converter altura em
largura de mola.

**Velocidade da roda de escape.** 28 800 A/h ÷ 2 = 14 400 oscilações completas por hora; um dente por
oscilação → 14 400 dentes/h. Logo:

| Dentes da roda de escape | Rotações/h | Razão total barrilete → escape |
|---|---|---|
| 15 | 960 | **5 760** |
| 18 | 800 | 4 800 |
| 20 | 720 | 4 320 |
| 21 | ≈ 685,7 | ≈ 4 114 |
| 24 | 600 | 3 600 |

**Número de estágios.** Um trem suíço clássico faz ~4 500 em quatro engrenamentos, média 8,2 por estágio.
Aqui, 5 760 em quatro engrenamentos dá média **8,71** — alto, mas dentro do normal. Em cinco engrenamentos
daria 5,66, que seria anormalmente baixo. **Conclusão:** a roda intermediária observada (CLM-0406) se
comporta aritmeticamente como *idler*, e a razão 1:1 conjecturada por SRC-0403 é **consistente**, não
suspeita. O `gear_search` deve testar as duas topologias — intermediária como idler e como estágio de
multiplicação — e deixar que os centros medidos decidam.

**Indicação.** Minuto a 1 volta/h. Se a indicação for acionada pelo barrilete (H-IND-101), a razão exigida
é **6:1 exata** — um número inteiro limpo, o que é um ponto a favor da hipótese sem chegar perto de
prová-la. Hora a 1 volta/12 h: razão **12:1** entre as duas rodas porta-ponteiro, realizada no plano
(Q-IND-001). O `gear_search` tem de fechar as duas cadeias com os mesmos centros.

**Massa.** O somatório de massas do CAD do movimento tem de dar 2,82 g em titânio grau 5 (ρ ≈ 4,43 g/cm³)
mais rubis e aço. Isso é uma restrição global forte: 2,82 g em 41,45 × 28,85 × 1,18 mm significa densidade
aparente de ≈ 2,0 g/cm³ — ou seja, **o calibre é mais de metade vazio**. Qualquer modelo que feche em massa
sem esqueletar pesadamente está errado.

---

## 8. Solvers

Cinco famílias, em `solvers/`. Nenhum solver é caixa-preta: cada execução guarda função objetivo,
restrições, candidatos, resíduos e a justificativa da escolha (`CLAUDE.md` §10).

### `image_metrology`
- **Entradas:** imagem + `image_id` + `natureza`; pontos de landmark (`evidence/image-landmarks/`);
  dimensões de âncora **no mesmo plano** dos pontos medidos; modelo de distorção quando estimável.
- **Saídas:** homografia; escala mm/px com incerteza; coordenadas medidas com elipse de erro; dispersão
  entre imagens independentes; overlay CAD→foto guardado como evidência; linhas em `evidence-ledger.csv`.
- **Regras:** classe C só sai de `fotografia_oficial` ou `quadro_de_video`; de `render_CG_oficial` sai
  classe **E**; de `render_CG_terceiro` não sai nada (DEC-003).
- **Já existe:** `extrair_quadros_chave.py` (seleção por variância do laplaciano) e
  `fatiar_sprite_360.py` (detecção do número de quadros por FFT). Falta a homografia — vem de U19.

### `gear_search`
- **Entradas:** centros medidos com incerteza; diâmetros observados; razão total alvo por candidato de
  dentes da roda de escape; faixa de módulos plausível para 1,18 mm; sentidos de rotação; número de
  estágios admitido; contagens parciais obtidas por periodicidade.
- **Saídas:** conjunto de candidatos (dentes por estágio, módulo, distância entre centros teórica) com
  resíduo contra os centros medidos; ranking por resíduo; **todos** os candidatos preservados, nunca só o
  melhor; tabela em `engineering/geartrain/`.
- **Regra:** nenhum número de dentes é escolhido por aparência. A eliminação é por evidência ou por
  resíduo, e fica registrada.

### `kinematics`
- **Entradas:** topologia (`interfaces.csv`), dentes, geometria do escape, estados do seletor.
- **Saídas:** velocidades angulares por eixo; traço da máquina de estados W/H com verificação de ausência
  de dupla conexão; ciclo do escape com lock, unlock, impulse, drop e passagem segura; verificação de
  ausência de overbanking no modelo; comparação do ângulo de levantamento simulado com os 54° publicados.

### `geometry_fit`
- **Entradas:** silhuetas extraídas dos 81 quadros do sprite 360° (duas iluminações), par ortogonal
  IMG-0009/IMG-0011, perfil IMG-0007; superfície paramétrica candidata da caixa.
- **Saídas:** parâmetros de forma ajustados; **métrica de erro de projeção CAD→imagem** por vista; mapa de
  resíduo ao longo do contorno; resposta a Q-CASE-002 (onde valem os 1,75 mm).

### `validation`
- **Entradas:** exports do Fusion (STEP, CSV de parâmetros, BOM, massa) e os CSV do repositório.
- **Saídas:** relatório por família de teste do §12, com PASS/FAIL; qualquer excesso de envelope ou de
  Z-budget reprova o commit. Detalhado em `VALIDATION-PLAN.md`.

---

## 9. O que este plano proíbe

Releitura operacional do `CLAUDE.md` §13, com os nomes deste projeto:

- Criar tige, pignon coulant, bascule ou tirette por analogia com um remontoir clássico — **este relógio
  não tem haste** (CLM-0036).
- Criar canhão de minutos ou roda das horas empilhada — **não existem** (CLM-0037).
- Criar ponte do barrilete — o barrilete é retido pela periferia (CLM-0401).
- Tirar qualquer dimensão das figuras da EP3754433B1, do US11550262B2 ou das pranchas do USD991795.
- Copiar a silhueta da âncora da figura 5 da patente, que é explicitamente um catálogo de formas
  alternativas.
- Usar IMG-0014…IMG-0025 (render de terceiro) para qualquer coisa.
- Usar IMG-0001 como fonte de medida antes de Q-IMG-003 ser respondida.
- Fechar uma folga em zero para o modelo caber, sem declarar contato em `interfaces.csv`.
- Escolher uma das duas hipóteses de cristal por conveniência de modelagem, em vez de carregar as duas.
