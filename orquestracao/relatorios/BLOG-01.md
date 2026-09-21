# BLOG-01 — Escapamento, o blog

Entregue em 21/09/2026. Repositório novo em `~/repo/escapamento`, branch `main`, sem
remoto, sem push, sem deploy — as duas últimas coisas ficam com o Pedro.

## Feito

**Site.** Astro 7 estático, Node 22, tema claro editorial na mesma família visual do
site do PW-50 (papel `#ffffff`/`#f4f3f1`, taupe `#8b7d66`, texto `#4a4a4a`, Cormorant
Garamond na prosa e Inter leve em caixa alta nos rótulos, tudo via `@fontsource`, nada
de CDN). Largura de leitura 68ch, tipografia de 1,25–1,44 rem na prosa, entrelinha 1,68.

Páginas: home (chamada do último post, lista dos demais, grade das seis séries),
`/serie/<slug>` para as seis, `/post/<slug>`, `/sobre`, `/en`, `/rss.xml`, sitemap,
`404`, OpenGraph e Twitter card em todas, canônica em todas.

**Coleção.** `content/posts/*.md` com o frontmatter pedido (`title`, `description`,
`pubDate`, `series`, `lang`, `draft`, `cover?`, `tags`), validado por Zod no build. O
slug é o nome do arquivo.

**As duas regras de publicação**, num lugar só (`src/lib/posts.ts`): `draft: true` não
aparece; `pubDate` no futuro não aparece. Avaliadas no build — é o que dá sentido ao
timer semanal. `ESCAPAMENTO_RASCUNHOS=1` derruba as duas para releitura local, e o
`publicar.sh` limpa a variável de propósito.

**Doze rascunhos**, 1 105 a 1 262 palavras cada, todos com `draft: true` e com as
seções "o que não sabemos" e "como sabemos disso". Lista abaixo.

**`scripts/semana.py`** (stdlib): lê `docs/RESEARCH-LOG.md` e `CHANGELOG.md` deste
repositório, recorta a janela de sete dias, quebra as entradas em marcadores e grava
`content/posts/diario-AAAA-MM-DD.md` com a data da próxima segunda às 08:00 −03:00 e o
esqueleto editorial. Janela vazia gera o post "a semana em que nada foi descoberto".

**`scripts/publicar.sh`**: `npm run build` + `vercel deploy --prod --yes --archive=tgz`
a partir de `dist/`. Não foi executado.

**`systemd/escapamento-semanal.{service,timer}`**: segunda 08:00 `America/Sao_Paulo`,
`Persistent=true`, chama o `publicar.sh`. Não instalado; instruções em
`systemd/LEIA-ME.md`.

**`scripts/verificar.mjs`**: Chromium do cache do `playwright-core`, como no site do
PW-50. Constrói com as fixtures, sobe um servidor estático sobre `dist/`, abre home,
série, post e `/sobre` em 1440×900 e 400×800, reprova com erro de console, com rolagem
horizontal (nomeando o elemento culpado) e com post futuro ou em rascunho em qualquer
arquivo do `dist`. Capturas e `resultado.json` em `verificacao/`.

**README.md**: como escrever um post (frontmatter, séries, regras editoriais), como
publicar, como funciona a agenda e a régua.

## Executado

- `npm run build` — verde, 10 páginas (nenhum post, porque os doze são rascunho).
- `ESCAPAMENTO_RASCUNHOS=1 npm run build` — verde, 22 páginas.
- `npm run verificar` — verde, 8 capturas, 8 s.
- Teste negativo: com a fixture futura trazida para o passado, a régua reprova em cinco
  pontos (home, rota, RSS, página da série e existência do arquivo). Fixture restaurada.
- `python3 scripts/semana.py --hoje 2026-09-22 --stdout` — recortou corretamente as
  quatro entradas de 20–21/09 do RESEARCH-LOG e a versão 0.0.1 do CHANGELOG.
- Inspeção visual das páginas em 1440×900 e 400×800; corrigido um erro de
  especificidade que zerava o espaçamento entre parágrafos da prosa.

## Os doze rascunhos

Todos `draft: true`, pt-BR, primeira pessoa.

| # | Data (08:00 BRT) | Série | Título | Arquivo |
|---|---|---|---|---|
| 1 | 29/09/2026 | Diário do RM UP-01 | Por que 1,75 mm | `por-que-1-75-mm.md` |
| 2 | 02/10/2026 | Lendo Daniels | Por que este livro | `quem-foi-george-daniels.md` |
| 3 | 06/10/2026 | Diário do RM UP-01 | O que a marca diz e o que não diz | `o-que-a-marca-diz-e-o-que-nao-diz.md` |
| 4 | 09/10/2026 | O relógio de bolso | Três projetos, um relógio | `tres-projetos-um-relogio.md` |
| 5 | 13/10/2026 | Diário do RM UP-01 | Um escapamento sem as duas peças de segurança | `uma-patente-um-escape-sem-guard-pin.md` |
| 6 | 16/10/2026 | Lendo Daniels | A oficina antes do relógio | `a-oficina-antes-do-relogio.md` |
| 7 | 20/10/2026 | Diário do RM UP-01 | Como medir um relógio numa fotografia | `como-medir-um-relogio-numa-fotografia.md` |
| 8 | 23/10/2026 | Histórias do tempo | De verge a alavanca | `o-escapamento-de-verge-a-alavanca.md` |
| 9 | 27/10/2026 | Diário do RM UP-01 | O barrilete que dá uma volta a cada seis horas | `o-barrilete-de-seis-horas.md` |
| 10 | 30/10/2026 | Lendo Daniels | Aço, latão e a razão do acabamento | `aco-latao-e-acabamento.md` |
| 11 | 03/11/2026 | Diário do RM UP-01 | O trem: dentes que não conhecemos | `o-trem-dentes-que-nao-conhecemos.md` |
| 12 | 06/11/2026 | A casa do Richard | Quem é Richard Mille, e por que eu ainda não posso contar | `quem-e-richard-mille.md` |

### Três decisões editoriais que o Pedro precisa julgar

1. **"Os 12 primeiros posts" foi lido como as seis primeiras semanas**, segunda e
   quinta de cada uma — porque o enunciado manda usar os dois horários. A tabela do
   PROGRAMA tem 24 posts em 12 semanas; as semanas 7 a 12 ficaram de fora.
2. **29/09/2026 não é segunda-feira** no calendário real (é terça; a segunda é 28/09).
   Segui a data explícita do plano e mantive o ritmo de sete em sete dias a partir
   dela; a série paralela cai três dias depois. Se o Pedro quiser segundas de verdade,
   basta recuar um dia em todos os doze `pubDate`. O `semana.py` calcula a próxima
   segunda pelo calendário, não por essa tabela.
3. **Três títulos foram trocados por causa de fato.** "As 16 âncoras" virou "O que a
   marca diz e o que não diz", porque as âncoras conferidas são 26. "Quem foi George
   Daniels" virou "Por que este livro", porque não há nos documentos lidos biografia
   que aguente citação. "Quem é Richard Mille" ficou com o título, mas o post é sobre
   a ausência de declarações dele — que é o fato que os documentos sustentam.

### De onde saiu cada fato

Só dos documentos lidos: `PROGRAMA-PUBLICO.md`, `CLAUDE.md` (§0–2, 8, 17, 20),
`docs/FACTS.md`, `docs/OPEN-QUESTIONS.md`, `docs/RESEARCH-LOG.md`, o
`RESUMO-EXECUTIVO.md` e a `CONSOLIDACAO-01.md` do relógio de bolso, e o sumário dos
treze capítulos do *Watchmaking*. Nenhum trecho nem figura do livro é reproduzido.

Onde faltou fato, o post escreve a pergunta. O de história (nº 8) foi escrito
deliberadamente sem uma única data, com a bibliografia declarada como dívida; o nº 12
é um post sobre o que não se conseguiu achar.

Nenhum post promete relógio funcionando, nenhum usa "réplica exata", nenhum cita nome
interno de job, agente ou ferramenta de orquestração.

## Pendente (é do Pedro)

- **Revisar os doze textos e tirar o `draft: true`.** A voz é dele; o que está lá é
  rascunho para ser cortado.
- **Domínio.** `astro.config.mjs` está com um endereço provisório
  (`escapamento.vercel.app`). RSS, sitemap e OpenGraph dependem dele. Conferir a
  disponibilidade de `escapamento.dev` / `escapamento.blog`, como o PROGRAMA pede.
- **Criar o repositório remoto** `pedropasinn/escapamento` e dar o push.
- **Primeiro deploy** (`./scripts/publicar.sh`), com a CLI da Vercel autenticada.
- **Instalar o timer** (`systemd/LEIA-ME.md`), depois que o deploy manual funcionar uma
  vez.
- **Imagens.** Nenhum post tem `cover`. O PROGRAMA pede uma imagem própria por dobra:
  renders e diagramas nossos, nada de foto de marca sem licença. O campo já existe e a
  página já trata a capa.
- **Versões em inglês.** A `/en` está pronta e vazia; o plano prevê começar no segundo
  mês.
- **Semanas 7 a 12** do calendário, se ele quiser a leva completa.
- Decidir se os posts do diário devem sair em segunda de calendário (ver decisão 2).

## Onde estão as coisas

```
~/repo/escapamento/
├── README.md                 como escrever, como publicar, como funciona a agenda
├── content/posts/            os doze rascunhos
├── content/fixtures/         as três fixtures da régua
├── src/lib/posts.ts          as seis séries e as duas regras de publicação
├── scripts/semana.py         rascunho automático da semana
├── scripts/publicar.sh       build + deploy (não executado)
├── scripts/verificar.mjs     régua do navegador
├── systemd/                  timer semanal (não instalado)
└── verificacao/              capturas da última verificação (fora do Git)
```
