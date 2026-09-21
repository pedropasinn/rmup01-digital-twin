# Programa público — blog, vídeos e notificações semanais

Escrito por Claude em 21/09/2026 a pedido de Pedro. Objetivo: transformar o hobby de projetar relógios (PW-50, RM UP-01 e o que vier) numa publicação semanal para pessoas, com voz e cara próprias, e manter o repositório público informando os avanços toda semana.

## 1. Nome

**Escapamento** — "um diário sobre projetar relógios". O escapamento é a peça que deixa o tempo escapar do mecanismo em porções iguais; é também o que faz um relógio ser um relógio, e não uma mola desenrolando. Serve de metáfora para o blog: soltar o que aprendemos em porções regulares. Curto, pronunciável, disponível como `escapamento.dev` / `escapamento.blog` (conferir) e como identidade: uma âncora (a alavanca do escape) como marca.

Alternativas, se Pedro preferir: **Um Décimo** (um décimo de milímetro, a escala onde o PW-50 e o RM UP-01 se decidem); **Platina** (a base sobre a qual tudo se monta); **Batidas** (18 000 e 28 800 por hora).

## 2. Séries (cada post é para uma pessoa ler no café, 900–1 500 palavras, uma imagem própria por dobra, sem jargão sem explicação)

| Série | Ritmo | Sobre | Fonte |
|---|---|---|---|
| **Diário do RM UP-01** | semanal (segunda) | o que descobrimos, o que mudou de ideia, o que continua desconhecido; cada post fecha com "como sabemos disso" | `docs/RESEARCH-LOG.md`, ledger de evidência |
| **Lendo Daniels** | quinzenal (quinta) | comentário capítulo a capítulo de *Watchmaking* (George Daniels, 1981/1999, 13 capítulos): o que ele ensina, o que mudou em 45 anos, o que aplicamos no PW-50 e no RM UP-01 | o livro (comentário próprio; sem reprodução de texto ou figuras) |
| **O relógio de bolso** | mensal | a saga do PW-50: reconciliação, turbilhão, escape, ornamento, o que passou e o que reprovou | repo relogio-bolso |
| **Histórias do tempo** | mensal | história dos relógios: do verge ao co-axial, Harrison, Breguet, Daniels, os ultraplanos | fontes públicas com bibliografia |
| **A casa do Richard** | mensal | Richard Mille (a pessoa, a marca, Renaud & Papi, a parceria Ferrari) e o RM UP-01 em particular | fontes públicas; tom de estudo, não de hype |
| **Bastidores** | quando houver | como um hobby vira operação: agentes, Balcão, evidência, honestidade | esta operação |

Regras editoriais: primeira pessoa (Pedro), frases curtas, uma ideia por parágrafo, número só quando muda a leitura, sempre "o que não sabemos" no fim, nunca "réplica exata" nem promessa de relógio funcionando. Imagens: renders e diagramas nossos; nada de foto de marca sem licença. Cada post tem versão em inglês (a partir do segundo mês).

## 3. Calendário das 12 primeiras semanas (a partir de 29/09/2026)

| Semana | Segunda (Diário) | Quinta (série paralela) |
|---|---|---|
| 1 | Por que 1,75 mm: o problema que o RM UP-01 resolve | Lendo Daniels 0: quem foi George Daniels e por que este livro |
| 2 | O que a marca diz e o que não diz: as 16 âncoras | O relógio de bolso 1: três projetos, um relógio |
| 3 | Uma patente, um escape sem guard pin | Lendo Daniels 1: a oficina (cap. 1–2) |
| 4 | Como medir um relógio numa fotografia | Histórias do tempo 1: o escapamento, de verge a alavanca |
| 5 | O barrilete que dá uma volta a cada seis horas | Lendo Daniels 2: aço, latão e acabamento (cap. 3) |
| 6 | O trem: dentes que não conhecemos | A casa do Richard 1: quem é Richard Mille |
| 7 | W ou H: um seletor em vez de uma coroa que puxa | Lendo Daniels 3: tornear um eixo de balanço (cap. 4) |
| 8 | O balanço de três braços e 3 mg·cm² | O relógio de bolso 2: o turbilhão que coube |
| 9 | Z-budget: 1,18 mm repartidos | Lendo Daniels 4: rodas e pinhões (cap. 5) |
| 10 | Caixa e movimento trabalhando juntos | Histórias do tempo 2: os ultraplanos, de 1946 ao Octo Finissimo Ultra |
| 11 | Primeira montagem digital: o que colide | Lendo Daniels 5: peças pequenas (cap. 6) |
| 12 | O que sabemos, o que inferimos, o que inventamos | Bastidores 1: como uma pessoa e alguns agentes fazem isso |

Os posts do Diário dependem do avanço real; se a semana não render descoberta, o post diz isso e explica o porquê (isso também é conteúdo).

## 4. Vídeos com a voz de Pedro

Pedro vai gravar um áudio de referência. Com ele: registrar a voz `pedro` no auto-colab (`voices/pedro.yaml` com `consent.status: verified` e a evidência "pedido do próprio Pedro em 21/09/2026"), receita `omnivoice-islp-pedro`, e gerar: (a) um vídeo curto por post do Diário (60–120 s, quadros do viewer/diagramas + narração), (b) um vídeo mensal de 5–8 min de balanço, (c) versão em inglês com a mesma voz quando o modelo suportar. Pipeline: o do PW-50 (`video/scripts/`), com cartelas e legendas. Só depois do áudio.

## 5. Repositório público e notificações semanais

- `github.com/pedropasinn/rmup01-digital-twin` (público desde 21/09): código, evidência, planos; acervo de terceiros fora (só manifestos).
- Toda segunda: `git tag semana-NN`, uma Release com o resumo da semana (o mesmo texto do Diário, sem as imagens de terceiros), e o post no blog. Quem quiser acompanhar assina o RSS do blog ou "Watch → Releases" no GitHub. Sem newsletter no início; e-mail para Pedro com o rascunho na sexta para revisão.
- Automação: um script `scripts/semana.py` no repo do blog gera o rascunho a partir do RESEARCH-LOG e do CHANGELOG; Pedro revisa; publica-se por data (o site publica posts cujo `date` já passou; um timer semanal na Dell reconstrói e faz o deploy).

## 6. O site do blog

Repositório público próprio (`pedropasinn/escapamento`), Astro + Markdown (posts em `content/posts/*.md` com `date`, `series`, `lang`), RSS, página por série, busca simples, tema claro editorial na mesma família visual do PW-50 (papel, taupe, serifa para prosa), deploy estático na Vercel. Posts com data futura ficam invisíveis até a data; o timer semanal reconstrói. Primeira leva: os 12 posts da tabela, escritos como rascunhos para Pedro editar (a voz é dele; o texto sai em primeira pessoa e ele corta o que não é dele).

## 7. Balcão (ChatGPT web) como motor de pesquisa

Vinte pedidos U01–U20 (seção "U · RM UP-01") cobrem fontes primárias, patentes, imprensa em oito idiomas, entrevistas, anatomia comparada com outros ultraplanos, baseline do escape suíço, cálculo inverso do balanço, barrilete e trem, cristais e caixa, seletor W/H, glossário, histórias (Mille, ultraplanos), metrologia por imagem e licenças. Cada entrega volta como `<ID>-entrega.zip` em `_entrada/Balcao/` do repositório e é verificada antes de virar claim.
