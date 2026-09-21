# Índice da imprensa técnica, hands-on e desmontagens — RM UP-01 / calibre RMUP-01

Pacote `TASK-P1-003`, 2026-09-20/21. Bloco de IDs: `SRC-0400…0699`, `CLM-0400…0699`.
Questões abertas deste pacote: faixa `-101` em diante (o TASK-P1-001 já ocupara `-001…-003`).

Este índice cobre **imprensa e material de primeira mão** — não fontes primárias da marca
(essas estão no TASK-P1-001) nem patentes (TASK-P1-002) nem o catálogo de imagens/vídeos (TASK-P1-004).
Nenhum texto foi copiado: todos os resumos abaixo são próprios. Nenhum arquivo de artigo foi salvo
localmente, porque nenhum dos veículos publica licença que permita guardar cópia; por isso
`local_path` e `sha256` estão vazios no manifesto.

## Como ler as duas notas do manifesto

`visual_quality` — o que as **imagens** daquela matéria valem para reconstrução geométrica:
- **alta** — mostra o movimento fora da caixa, peças soltas, passos de montagem ou macro de subconjunto;
- **média** — imagens oficiais de imprensa do relógio montado, comparações de escala, macro do mostrador;
- **baixa** — só fotos de catálogo já disponíveis em outras fontes;
- **desconhecida** — página não acessível.

`reliability` — quanto a matéria merece crédito como **afirmação técnica**:
- **alta** — autor com competência relojoeira demonstrada e contato com o objeto ou com material de montagem,
  e que separa o que viu do que supõe;
- **média** — jornalismo correto, mas derivado do dossiê de imprensa, sem verificação própria;
- **baixa** — reprodução com erros técnicos detectados;
- **desconhecida** — não lida.

---

## Ranking de utilidade por subsistema

Ordem decrescente de valor real para a reconstrução. Entre parênteses, o que aquela fonte entrega.

| Subsistema | 1º | 2º | 3º |
|---|---|---|---|
| **BAR** barrilete | SRC-0403 Chronos JP (sem mancal acima/abaixo; 4 buchas BeCu na periferia) | SRC-0400 Hodinkee (barrilete esqueletado central com roletes periféricos; foto dedicada a um roller) | SRC-0412/0413 press kit (6 h/volta contra 7,5 h; barrilete < 1,18 mm) |
| **ESC** escape | SRC-0400 Hodinkee (side lever, banking contra entalhe na platina, pivô entre as pedras, foto alavanca+roda+ponte) | SRC-0401 vídeo oficial (ação da alavanca ~0:52) | SRC-0405 Hodinkee JP (âncora quase linear, extremidade em crescente) |
| **SEL** seletor W/H | SRC-0400 Hodinkee (braço deslizante, sentido de engate, still do vídeo) | SRC-0401 vídeo oficial | SRC-0409 Watchonista (operação real com a chave) |
| **TRN** trem | SRC-0403 Chronos JP (roda intermediária barrilete↔2ª roda; offset deliberado) | SRC-0400 Hodinkee (trem à direita, oculto sob a caixa) | SRC-0412 press kit (involuta 20°) |
| **CASE** caixa | SRC-0400 Hodinkee (rebaixo interno, parafuso central travando caixa+movimento) | SRC-0404 Chronos JP (caixa+tampa, 12 kg, cristal como elemento de rigidez) | SRC-0403 Chronos JP (nervura periférica, interior da tampa jateado) |
| **WND** corda | SRC-0413 press kit (sem haste: 1,5 mm não cabia; limitador de torque) | SRC-0403/0404 Chronos JP (coroas SS + aro de cerâmica como vedação) | SRC-0409 Watchonista (ergonomia da chave) |
| **OSC** oscilador | SRC-0400 Hodinkee (freesprung, espiral plana, degrau nos braços, ponte de 3 braços) | SRC-0420 Worldtempus (23 rubis, Kif, AK 3, seis massas) | SRC-0404 Chronos JP (inércia ~3 mg·cm²) |
| **IND** indicação | SRC-0404 Chronos JP (eixo apoiado contra o cristal) | SRC-0412 press kit (ponteiros sobre as rodas) | SRC-0400 Hodinkee (hipótese do trem próprio à esquerda) |
| **BASE/BRG** platina e pontes | SRC-0400 Hodinkee (fotos de montagem com a platina nua) | SRC-0403 Chronos JP (grande área, offset) | SRC-0412 press kit (acabamentos) |
| **FST** fixações | SRC-0412 press kit (13 spline Ti5 + arruelas 316L) | SRC-0400 Hodinkee (cilindro roscado central) | SRC-0405 Hodinkee JP (conta 12 — divergência) |
| **JWL / SHK** | — | — | nenhuma fonte de imprensa localiza os 23 rubis nem os Kif; ver Q-JWL-101 e Q-SHK-101 |

Conclusão do ranking: **duas fontes carregam quase tudo** — a análise da Hodinkee (SRC-0400) e as duas
matérias da Chronos Japan (SRC-0403, SRC-0404). Elas são complementares: a Hodinkee descreve topologia
(escape, seletor, interface caixa-movimento), a Chronos descreve construção (apoios do barrilete, roda
intermediária, vedação, rigidez da caixa). O resto da imprensa é, tecnicamente, reprodução do dossiê.

---

## Fichas por artigo

### SRC-0400 — Hodinkee, "An In Depth Technical Analysis Of The Richard Mille RM UP-01" (Jack Forster, 13/07/2022, en)

A matéria técnica mais rica do corpus aberto. O autor não desmontou o relógio, mas trabalha sobre
fotografias de montagem e sobre o vídeo de savoir-faire, e é disciplinado em dizer quando está supondo.

- **CASE** — movimento independente dentro de caixa de titânio grau 5 (contraste explícito com Piaget AUC e
  Bulgari Octo Finissimo Ultra, que usam a tampa como platina); a caixa funciona como porta-movimento;
  há um **rebaixo raso usinado na face interna da caixa inferior** que recebe barrilete e trem (profundidade
  não medida — o autor arrisca "talvez 0,05 mm", o que é chute e está marcado como classe E);
  **um cilindro roscado no meio do movimento**, perto do canto superior direito do barrilete, recebe um dos
  parafusos de caixa e trava caixa + movimento como corpo único, impedindo flexão central. Quatro aberturas
  na parte superior da caixa: seletor, corda/acerto, indicação, balanço. Cristais 0,45 mm (horas) e
  0,20/0,30 mm (balanço). Cabeças de parafuso de cinco entalhes. 10 m.
- **BAR** — barrilete esqueletado no centro, **estabilizado por roletes na periferia**.
- **TRN** — trem à direita do barrilete, completamente coberto pela caixa superior (sob o logo Ferrari).
- **ESC** — âncora com roda de escape de dentes em clave quase convencional; **sem guard pin e sem safety
  roller**; configuração **side lever**; geometria das pedras de pallet alterada para travamento seguro;
  **a âncora bate diretamente contra um entalhe usinado na platina** (banking sólido, sem pinos); o pivô da
  âncora fica **entre as duas pedras**.
- **OSC** — balanço freesprung com massas ajustáveis, **espiral plana** (overcoil sairia do orçamento vertical),
  **braços do balanço com um degrau** para aproximar a espiral do plano do balanço, ponte superior de três braços.
- **SEL** — duas grandes aberturas do lado esquerdo do movimento; girar o seletor de cima desloca **um braço
  deslizante**: para a direita engata as rodas que dão corda ao barrilete; para a esquerda engata o acerto e
  desacopla o barrilete.
- **IND** — o autor **supõe** (e diz que supõe) existir um trem próprio da indicação, à esquerda, movido pela
  rotação do barrilete, já que a primeira roda do trem de marcha está à direita e não tem ponteiro.
- **Fotos únicas** (arquivos `RM-UP-01-SF-xx` da própria Hodinkee): encaixotamento do movimento, com aviso de que
  **o movimento está girado 180° em relação à posição final** (armadilha de metrologia); detalhe de **um roller do
  barrilete**; instalação das rodas do trem à direita da abertura do barrilete; **alavanca, roda de escape e ponte
  da alavanca** juntas; stills do vídeo mostrando o travamento da alavanca contra a platina e o braço deslizante do
  seletor sendo manipulado com pinça. Vídeo embutido (cópia Brightcove do vídeo oficial), com a ação da alavanca
  por volta de 0:52.
- Não confundir: os comparativos com JLC 849, Piaget AUC, Bulgari Octo Finissimo Ultra e Rolex Chronergy são
  material de referência de outras marcas, úteis como baseline para a Fase 9 mas irrelevantes como evidência do RMUP-01.

### SRC-0401 — Richard Mille, vídeo "Savoir-faire RM UP-01 Ferrari" (canal oficial, 06/07/2022)
Origem dos stills usados pela Hodinkee. É o registro em movimento do escape e do braço deslizante do seletor.
A extração quadro a quadro e o catálogo cabem ao TASK-P1-004; aqui fica só o registro e a ligação com SRC-0400.

### SRC-0402 — SJX Watches, "Richard Mille Unveils the Thinnest Mechanical Watch Ever" (JX Su, 06/07/2022, en)
Introducing técnico, sem hands-on. Boa formulação da supressão do dard e do plateau e da fourchette alongada;
traz um diagrama de escape. Útil como confirmação redundante; não trouxe nada que as duas fontes de topo já não tivessem.

### SRC-0403 — Chronos Japan / webChronos, "1/100mmを削ぎ落とす技術" (鈴木裕之, 05/08/2022, ja)
A melhor fonte sobre **construção**. Texto conferido no HTML original, não só por resumo.
- **BAR** — **não há receptáculo acima nem abaixo do barrilete**; a periferia é retida por **4 buchas de
  berílio-cobre**. O autor lê isso como decisão para maximizar a altura do barrilete, ou seja, a largura da mola.
- **TRN** — offset do trem levado ao limite aproveitando a grande área da platina; **há uma roda intermediária de
  transmissão entre o barrilete e a segunda roda**, e a relação 2ª roda : intermediária **parece** 1:1 (o autor
  usa formulação de conjetura — não é razão confirmada).
- **WND/SEL** — as duas coroas ficam **alojadas em vazios do próprio movimento**; são de aço inoxidável com
  **inserto de cerâmica preta** na periferia, responsável pela estanqueidade; coroas e vedação são montadas
  **antes** do encaixotamento.
- **CASE** — interior da tampa em jateado úmido; o aro externo equivalente ao bezel é **uma nervura que ocupa
  toda a espessura da caixa**, o que dá a rigidez.
- **Massas** — relógio com pulseira 28,5 g; **cabeça 11,2 g**.
- **Fotos únicas** — sequência com **pinça segurando a segunda roda**, detalhe das duas coroas em corte,
  interior da tampa. Sete imagens legendadas.

### SRC-0404 — Chronos Japan / webChronos, "The RM UP-01 Ferrari: An unprecedented watch…" (広田雅将, 25/03/2023, ja; versão en no site)
Autor manuseou o relógio. Três informações estruturais que **não aparecem na imprensa ocidental**:
- **CASE** — estrutura **caixa e tampa**, com a tampa fixada sobre o corpo para impedir distorção e **abertura do
  corpo reduzida** para ganhar robustez; a caixa **não deforma sob ~12 kg** aplicados na periferia; o cristal de
  0,45 mm foi deixado deliberadamente espesso e **contribui para a rigidez da caixa**.
- **IND** — as duas rodas que fazem de ponteiro têm o **eixo apoiado contra o cristal**, o que suprime deformação
  do cristal. Se confirmado, é uma interface cristal↔movimento com consequência direta no Z-budget.
- **WND** — a vedação das coroas usa **aro fino de cerâmica** no lugar da borracha, e os 10 m vêm do encaixe de
  peças usinadas ao mícron.
- Erro tipográfico a ignorar: o corpo do texto diz "8800 A/h"; a ficha do mesmo artigo diz 28.800.

### SRC-0405 — Hodinkee Japan, "Beyond the Limits 極限の挑戦の先に見た、極薄の美学" (高木教雄, 11/12/2023, ja, patrocinado)
Artigo japonês original. Descreve a âncora como **forma quase linear com duas pedras e extremidade em crescente**
e insiste na montagem coplanar (peças que se apoiam mutuamente) como origem dos 5.000 g. **Conta 12 parafusos
na caixa**, contra os 13 publicados — divergência registrada. Por ser patrocinado, a avaliação não é independente.

### SRC-0406 / SRC-0407 — Hodinkee Japan (tradução do deep dive; relato de uso no pulso)
SRC-0406 é tradução de SRC-0400 — registrada para deduplicação, sem claim próprio. SRC-0407 é relato de uso,
útil só para CASE/STR (ergonomia, comportamento da pulseira).

### SRC-0408 — Monochrome (Rebecca Doulton, 06/07/2022, en)
Introducing sobre o dossiê. Confirma 13 parafusos spline e os acabamentos. Sem contato físico.

### SRC-0409 — Watchonista, "Hands (and Mind) On…" (Mike Espindle, 30/09/2022, en)
Hands-on real, de uso. Valor para **SEL/WND**: descreve a chave dedicada como objeto acabado, a operação das duas
coroas (a de cima escolhe o modo, a de baixo executa, com sentidos opostos para corda e acerto) e diz que dá para
operar com o polegar, com menos precisão. Nenhuma imagem de movimento.

### SRC-0410 — Swisswatches Magazine, "A Closer Look…" (Philipp Riehr, 25/10/2022, en)
Visto ao vivo em boutique. Interesse: **comparação de espessura com uma moeda de 2 euros** (calibração grosseira
possível) e reprodução de imagens oficiais de savoir-faire. Vários pontos do texto são tecnicamente imprecisos e
não foram aproveitados.

### SRC-0411 — aBlogtoWatch (Ripley Sellers, 06/07/2022, en)
Sem contato físico; **galeria ampla** de imagens de imprensa, incluindo macro do movimento — o valor está nas
imagens, não no texto, que é sobretudo crítica estética e à associação com a Ferrari.

### SRC-0412 / SRC-0413 — La Cote des Montres, fr e en (05/07/2022)
Reprodução íntegra do dossiê de imprensa **com a entrevista** a Yves Mathys, Salvador Arbona e Julien Boillat.
É a via pela qual as declarações do fabricante chegam a este pacote:
- **Arbona** — o briefing era 45 h, 4 Hz e seletor de função no pacote mais fino imaginável; gears e ponteiros
  sobrepostos eram impossíveis; **barrilete extraplano de menos de 1,18 mm** com mola extremamente fina;
  barrilete de rotação rápida (**6 h contra 7,5 h**) para reduzir aderência da mola; escape patenteado com
  **âncora sem dard**, **fourchette alongada com cornes novas** e função de banking transferida para a âncora;
  balanço de inércia variável em titânio com **seis massas**, espiral **AK 3**.
- **Boillat** — o alvo inicial de caixa era 3 mm e se revelou grosso demais; **a haste tradicional foi descartada
  porque seu diâmetro mínimo é ~1,5 mm**; as duas coroas são rodas do movimento; há **limitador de torque** contra
  corda forçada; **certos segmentos da caixa foram reduzidos a 0,18 mm**; cerca de **dez impressões 3D** e
  **uns vinte protótipos** em materiais metálicos antes do titânio.
- **Mathys** — operações verificadas em quase todas as etapas, tolerância de **um mícron**.
- Ficha técnica reproduzida: 41,45 × 28,85 × 1,18 mm; 2,82 g; 45 h ±10%; 23 rubis; **13 parafusos spline Ti grau 5
  com arruelas 316L**; involuta central 20° no winding-barrel e no pinhão da terceira roda; ponteiros decalcados
  diretamente sobre as rodas.

### SRC-0414 — 腕表之家 xbiao.com (林北的表, 07/07/2022, zh)
Cobertura chinesa derivada do dossiê. Explica bem a supressão dos elementos de segurança, mas **afirma que a
platina serve de tampa da caixa**, o que é falso e contradiz RM, Hodinkee e Chronos. Confiabilidade baixa;
usar só como reforço terminológico.

### SRC-0415 — Maxim (Jared Paul Stern, 21/11/2022, en) · SRC-0419 — Revolution (Wei Koh, 20/12/2022, en) · SRC-0420 — Worldtempus · SRC-0421 — Time and Watches
Editorial e ficha sobre o dossiê, sem verificação própria. SRC-0420 é útil por listar os componentes especiais
(23 rubis, Kif, balanço Ti grau 5 de três braços com seis massas, AK 3) de forma explícita.

### SRC-0416 / SRC-0417 — Quill & Pad (2022 e reprise 2023) · SRC-0418 — Forbes (Carol Besler, 08/07/2022)
**Não lidas.** O servidor devolveu HTTP 403 ao acesso automatizado (desafio anti-robô no caso do Quill & Pad).
Registradas no manifesto com `rights` explícito, sem conteúdo, sem autoria verificada e sem claim.
Nada foi contornado. Reavaliar por leitura humana em navegador.

---

## O que a imprensa NÃO entrega

- Nenhuma **desmontagem real** (teardown de relojoeiro) do RM UP-01 foi localizada em nenhum idioma. Todo o material
  de "movimento fora da caixa" vem de **fotografias e vídeo de montagem produzidos pela própria Richard Mille** e
  reproduzidos pela imprensa. Isso limita os ângulos disponíveis e significa que não existe registro público do
  **verso do movimento** nem das peças do lado oculto.
- Nenhuma matéria localiza os 23 rubis nem os Kif.
- Nenhuma matéria dá número de dentes, módulo, diâmetro de roda, distância entre centros ou espessura de peça
  interna. Todo número desse tipo terá de vir de metrologia de imagem (Fase 1→3) e dos solvers.
- Em **espanhol e português** não foi encontrada uma única matéria com conteúdo técnico de primeira mão: a cobertura
  é integralmente derivada de agências e do dossiê. Em **alemão**, a cobertura passa pela Swisswatches (bilíngue).
  Em **italiano**, idem. O material técnico independente está em **inglês (Hodinkee, SJX)** e sobretudo em
  **japonês (Chronos Japan)**.
- **Europa Star**, **WatchTime** e **Financial Times / HTSI** não tiveram matéria específica sobre o RM UP-01
  localizada por busca; ver Q-DOC-101.
