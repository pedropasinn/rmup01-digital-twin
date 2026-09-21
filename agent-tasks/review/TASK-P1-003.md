# Revisão — TASK-P1-003 · Imprensa técnica, hands-on e desmontagens

Executado em 2026-09-20/21. Bloco de IDs usado: `SRC-0400…0421`, `CLM-0400…0439`.
Sem commit (fica com o diretor técnico). Sem Codex.

## Feito

- **22 fontes** registradas em `research/source-manifest.csv`, cada uma com `visual_quality` e `reliability`
  justificadas em `notes` e com a régua das duas notas escrita no topo de `research/articles/INDICE.md`.
- **40 claims** em `research/claims.csv` (`CLM-0400…0439`), com classe A–F, fontes e estado. Nenhum claim de
  classe C (não houve metrologia neste pacote).
- **`research/articles/INDICE.md`** criado: régua das notas, **ranking de utilidade por subsistema** (BAR, ESC,
  SEL, TRN, CASE, WND, OSC, IND, BASE/BRG, FST, JWL/SHK), ficha por artigo com o que cada um revela por
  subsistema e quais fotos únicas contém, e uma seção final sobre o que a imprensa **não** entrega.
- **`docs/OPEN-QUESTIONS.md`**: 32 questões novas (faixa `-101` em diante, para não colidir com pacotes
  concorrentes) em BAR, TRN, ESC, OSC, IND, SEL, WND, CASE, JWL, SHK e DOC.
- **`docs/HYPOTHESES.md`**: 3 hipóteses formais no esquema do §5 — H-BAR-101 (roletes × buchas),
  H-IND-101 (trem de indicação próprio acionado pelo barrilete), H-CASE-101 (cristal como elemento estrutural).
- **`docs/RESEARCH-LOG.md`**: entrada cronológica do pacote.
- Nenhum texto copiado: todos os resumos são próprios. Nenhum arquivo salvo em `research/articles/` — nenhum dos
  veículos publica licença que permita guardar cópia, então `local_path` e `sha256` ficaram vazios no manifesto,
  conforme a regra 5 do preâmbulo.

### Contagem por tipo e idioma

| | |
|---|---|
| artigos | 21 |
| vídeo | 1 (SRC-0401, canal oficial RM, registrado aqui por ser a origem dos stills da Hodinkee; catálogo de vídeo é do TASK-P1-004) |
| inglês | 14 |
| japonês | 5 |
| francês | 1 |
| chinês | 1 |
| alemão / italiano / espanhol / português | 0 com conteúdo próprio (ver abaixo) |

Todas as URLs foram conferidas com `curl -sIL` (status na tabela do índice implícito: 200, exceto os três 403
explicitados). Título, autor e data de cada fonte lida foram tirados da própria página, nunca supostos; onde não
foi possível ler, a autoria está marcada como não verificada.

## Achados que mudam o trabalho seguinte

1. **Não existe desmontagem pública feita por terceiro.** Todo material de "movimento fora da caixa" vem de fotos e
   do vídeo de montagem da própria Richard Mille. **Não há nenhuma imagem pública do verso do movimento.** Isso põe
   um teto na classe de evidência de tudo que fica do lado oculto (Q-DOC-103) e deve ser dito na cara do plano das
   Fases 5–7, em vez de descoberto no meio do CAD.
2. **Barrilete sem receptáculo acima nem abaixo**, retido só pela periferia (CLM-0401) — decisão de arquitetura, não
   detalhe. A Chronos conta quatro buchas de berílio-cobre; a Hodinkee fala em roletes (H-BAR-101).
3. **Roda intermediária de transmissão entre barrilete e segunda roda** (CLM-0406), com razão que "parece" 1:1
   (classe D, CLM-0407). Estágio extra que o solver do trem precisa admitir desde o início.
4. **Banking sólido contra um entalhe usinado na platina** e **pivô da âncora entre as duas pedras** (CLM-0412/0413):
   duas restrições geométricas fortes para a Fase 9 que não estão na patente.
5. **Braços do balanço com degrau** para baixar o plano da espiral (CLM-0417) — ganho de altura que precisa aparecer
   no Z-budget do oscilador.
6. **Parafuso de caixa no meio do movimento**, num cilindro roscado junto ao canto superior direito do barrilete
   (CLM-0429): exige furo passante na platina em posição determinável por foto, e é a peça que faz caixa e movimento
   virarem um corpo rígido único.
7. **Eixo da indicação apoiado contra o cristal** (CLM-0420, só em fonte japonesa): se confirmado, é interface
   cristal↔movimento com efeito direto no Z-budget, e não uma curiosidade.
8. **Sem haste de corda** porque 1,5 mm não cabia, **com limitador de torque** no comando (CLM-0424/0425), e vedação
   das coroas por **aro de cerâmica** em vez de borracha (CLM-0426).
9. **Certos segmentos da caixa a 0,18 mm** (CLM-0430) — provável piso de parede para a Fase 4, mas o fabricante não
   diz onde (Q-CASE-102 do pacote P1-001 e Q-CASE-101/105 deste).

## O que NÃO foi possível, e por quê

- **Quill & Pad (2 matérias) e Forbes**: HTTP 403 ao acesso automatizado (desafio anti-robô no Quill & Pad).
  Registradas no manifesto com `rights` explícito, **sem leitura e sem contorno**, autoria não verificada, sem claim.
  Precisam de leitura humana em navegador (Q-DOC-102).
- **Europa Star, WatchTime e Financial Times / HTSI**: não foi localizada matéria específica sobre o RM UP-01 em
  nenhum dos três, apesar de serem alvos do `CLAUDE.md` §3.2. Pode ser limitação da busca (edição impressa, arquivo
  próprio não indexado). Registrado como Q-DOC-101, não como "não existe".
- **TimeZone / fóruns**: a avaliação inicial cita uma imagem hospedada em `people.timezone.com`. Não foi localizado
  o tópico de origem com autoria identificável, e sem isso a imagem não pode ser atribuída nem registrada como fonte.
  Fica para o TASK-P1-004, que trata de imagens.
- **es / pt / de / it**: nenhuma matéria com conteúdo técnico próprio. A cobertura nesses idiomas é integralmente
  derivada do dossiê de imprensa e de agências, e algumas reproduzem erros (ex.: peso de 2,82 g atribuído ao relógio
  inteiro). Não foram registradas fontes só para engordar o manifesto; a ausência está documentada no índice.
- **Nenhum número interno** (dentes, módulo, diâmetro de roda, distância entre centros, espessura de peça) foi obtido:
  a imprensa não publica nada disso. Todo número desse tipo terá de vir de metrologia de imagem e dos solvers.
- **`engineering/master-parameters.yaml` e `evidence/evidence-ledger.csv` não foram tocados.** A regra 3 do preâmbulo
  manda atualizá-los quando uma âncora do §2 for confirmada **em fonte primária**; as âncoras que este pacote encontra
  (6 h/volta, involuta 20°, 13 parafusos, 23 rubis/Kif/AK 3, cristais) chegam por **reprodução de press kit em
  veículo secundário**. O TASK-P1-001 já as confirmou em fonte primária e já mexeu nesses arquivos; duplicar aqui
  criaria proveniência falsa. As claims correspondentes apontam para os `parameter_id` certos e ficam disponíveis
  como confirmação redundante.

## Pendente / recomendações

1. Leitura humana das três páginas bloqueadas (Q-DOC-102) e busca nos arquivos próprios de Europa Star, WatchTime e
   FT (Q-DOC-101).
2. Passar o vídeo oficial (SRC-0401) a quadro a quadro no TASK-P1-004, com atenção a: ação da alavanca (~0:52),
   braço deslizante do seletor, apoios do barrilete e montagem das rodas do trem. É o registro em movimento mais
   informativo do corpus.
3. **Armadilha de metrologia a propagar**: na foto de encaixotamento da Hodinkee o movimento está **girado 180°** em
   relação à posição final na caixa. Qualquer homografia feita sobre aquela imagem precisa corrigir isso antes de
   comparar posições com o relógio montado.
4. Tratar CLM-0421 (trem de indicação próprio) como classe E em todas as fases. É a suposição mais sedutora do
   corpus e a mais fácil de virar "fato" por repetição.
5. Confrontar CLM-0412/0413/0415 (banking na platina, pivô entre as pedras, banking na fourchette) com a família
   EP3754433A1 no TASK-P1-002: as descrições podem ser compatíveis, mas precisam ser conciliadas explicitamente
   antes de qualquer simulação 2D do escape.
