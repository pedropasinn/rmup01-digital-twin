# Revisão — TASK-P1-002 · Árvore de patentes

Executado em 20–21/09/2026. Bloco de IDs usado: **SRC-0200…0210**, **CLM-0200…0222**, **EVD-0200…0205**.
Sem commit. Sem Codex.

## 1. O que ficou feito

**Família do escape fechada e arquivada.** A âncora do `CLAUDE.md` §2 foi verificada em documento oficial e
corrigida num ponto: o documento vivo hoje não é o pedido EP3754433A1, e sim a **patente concedida
EP3754433B1**, com menção de concessão em **27/05/2026** (Bulletin 2026/22) — ou seja, a concessão europeia
saiu há quatro meses e o prazo de oposição de nove meses ainda corre. A família da prioridade **CH 832/2019
(19/06/2019)**, titular **Manufacture d'Horlogerie Audemars Piguet SA**, inventor **Giulio Papi**, tem os
membros: CH716337A1, EP3754433A1/B1, US11550262B2, HK40033669A, JP7537920B2, CN112114508B.

**Leitura integral do ensinamento**, a partir do US11550262B2 (texto em inglês, com descrição completa) e do
EP3754433B1 (reivindicações concedidas): topologia do escape sem dardo, ciclo completo (figs. 3a–3n),
situação de rebat (figs. 4a–4c), a condição geométrica que resolve a falha do CH44855 de 1909, as duas
variantes de fixação da cheville e as duas relações de arquitetura das reivindicações 7 e 8.

**Dois achados laterais que valem o pacote inteiro:**

1. **US D991,795 S — registro de desenho do próprio RM UP-01** (Haia **DM/218823**, depositado 28/10/2021 por
   **Turlen Holding SA**, o veículo de PI da Richard Mille, com Richard Mille como autor; concedido 11/07/2023).
   Dez pranchas com **seis vistas ortogonais** (frente, verso, direita, esquerda, inferior, superior) e quatro
   perspectivas. É a melhor fonte ortográfica pública encontrada até agora para a Fase 4 — com a ressalva, dita
   em todos os documentos que escrevi, de que **desenho de registro também não é desenho em escala**.
2. **EP4295198B1** (Papi + Fernandez, prioridade CH 150/2021 de 16/02/2021, concedida 18/02/2026): órgão único
   de comando em que a rotação aciona uma função — podendo ser **função de seleção com duas ou três posições
   angulares estáveis** — e a pressão axial aciona outra. O modo de realização descrito é de cronógrafo, então
   a ligação com o seletor W/H do UP-01 ficou como **hipótese**, não como fato.

**Arquivos entregues**

| Arquivo | Conteúdo |
|---|---|
| `research/patents/` | 7 PDFs oficiais (CH716337A1, EP3754433A1, EP3754433B1, US11550262, HK40033669A, EP4295198B1, USD991795) |
| `research/patents/patents.csv` | 10 linhas: número, família, prioridade, titular, inventores, situação legal, CPC, resumo em pt, o que ensina sobre topologia, `sha256` e caminho local |
| `docs/PATENT-TREE.md` | árvore das três famílias + reivindicações-chave em linguagem própria + tabela figura a figura (uso legítimo × uso proibido) + o que não se pode extrair + buracos conhecidos |
| `research/translations/EP3754433B1-reivindicacoes-pt.md` | as 11 reivindicações concedidas em tradução de trabalho, com o vocabulário francês preservado |
| `research/source-manifest.csv` | +11 linhas (SRC-0200…0210) |
| `research/claims.csv` | +23 linhas (CLM-0200…0222) |
| `evidence/evidence-ledger.csv` | +6 linhas (EVD-0200…0205) |
| `docs/OPEN-QUESTIONS.md`, `docs/HYPOTHESES.md`, `docs/RESEARCH-LOG.md` | seções novas do pacote |

## 2. Fontes registradas

11 linhas novas no manifesto. Por tipo: **5 patentes** com PDF local (CH, EP A1, EP B1, US, HK), **1 patente**
com PDF local da segunda família (EP4295198B1), **1 registro de desenho** com PDF local (USD991795),
**3 páginas/buscas de base de patentes** sem arquivo (listagem de família e duas varreduras por
inventor/titular) e **1 documento localizado mas NÃO verificado** (CH718513A1, marcado com confiabilidade baixa
e proibido de uso até leitura). Por idioma: francês 3, inglês 3, multilíngue fr/de/en 2 (fascículos EP),
metadados em inglês 3. Todas as sete URLs de arquivo conferidas com `curl -sIL --max-time 20`: HTTP 200.
`sha256` calculado para os sete arquivos locais.

Claims: 23, sendo **16 de classe A** (leitura direta de reivindicação ou descrição), **2 de classe B**
(identificação do desenho pelas pranchas), **1 de classe D** (o escape do RMUP-01 é execução desta família) e
**4 de classe E**. Nenhuma dimensão foi extraída de nenhum desenho.

## 3. O que NÃO foi possível, e por quê

- **Espacenet, WIPO Patentscope, Swissreg e Justia recusaram acesso automatizado** (HTTP 403, Cloudflare em
  alguns casos). Não houve tentativa de contornar: registrei e segui.
- **O Google Patents passou a responder 503 a este IP** depois de cerca de uma dezena de consultas, e não
  voltou até o fim do pacote. Isso interrompeu a varredura por titular e por CPC pela metade. Os fascículos
  europeus foram salvos pelo **servidor de publicação oficial do EPO** (`data.epo.org/publication-server`),
  que atende bem; foi por ele que apareceu a concessão EP3754433B1, invisível nas fontes anteriores.
- **Patentes do barrilete extraplano e do balanço de inércia variável: não localizadas.** A marca e a imprensa
  dizem "patenteado" para ambos (H-BAR-001 do TASK-P1-001), mas nenhuma família corresponde nas buscas que
  consegui rodar. Isso é resultado de busca, não conclusão sobre o mundo — está dito assim em CLM-0222 e nas
  questões Q-BAR-010 e Q-OSC-010.
- **Nenhuma patente de utilidade em nome de Richard Mille / Turlen Holding** apareceu: só registros de desenho.
  Compatível com o modelo de desenvolvimento por parceiros, mas com uma base só, não é prova.
- **JP7537920B2 e CN112114508B** ficaram registrados pela listagem de família do Google Patents, sem conferência
  em J-PlatPat/CNIPA e sem PDF. **CH716337A1** não teve a eventual concessão suíça (B1) verificada.
- **CH718513A1** ficou como pista, não como fonte: a página nunca abriu.

## 4. Questões abertas criadas

14 questões novas: `Q-ESC-010` a `Q-ESC-015`, `Q-SEL-010`, `Q-SEL-011`, `Q-BAR-010`, `Q-OSC-010`,
`Q-CASE-010` a `Q-CASE-012`, `Q-PAT-010`. Três hipóteses: `H-ESC-010` (o escape do RMUP-01 executa a família de
2019), `H-ESC-011` (cheville carregada pelo próprio balanço) e `H-SEL-010` (o seletor W/H segue a gramática da
EP4295198B1), cada uma com teste discriminante.

Como os pacotes P1-001 e P1-003 estavam escrevendo nos mesmos arquivos ao mesmo tempo, numerei minhas questões
a partir de **010** em cada subsistema para não colidir; o diretor técnico pode renumerar na consolidação.
Registrei também, na seção nova de `OPEN-QUESTIONS.md`, as **respostas parciais** que este pacote dá a
`Q-ESC-002` (o que é a parede anti-overbanking) e a `Q-BAR-002` (não localizada).

## 5. Pendente / recomendação para o próximo pacote

1. **Refazer a varredura com acesso humano ou por outra rota** (Espacenet ou OPS com chave): busca por titular
   Audemars Piguet e Turlen Holding, CPC G04B1/* (barrilete), G04B17/*–18/* (balanço/espiral), G04B3/* e
   G04B27/* (corda e seletor), prioridades 2018–2022. É o maior buraco que deixo.
2. **Ler o registro Haia DM/218823** na base Hague Express: eleva a identificação do desenho do UP-01 de B para
   A e dá a lista de países.
3. **Abrir USD1088933S1 e USD1102294S1** ("Watch movement", Turlen Holding, prioridades 09/2022 e 02/2023):
   se um deles for o RMUP-01, teremos vistas ortogonais da platina. (USD1015914S1 foi aberto e **não** é.)
4. **Usar as seis vistas do USD991795** na Fase 4 apenas por proporção relativa, calibrada contra dimensões
   publicadas, e registrar a calibração — nunca medindo direto na prancha.
5. Nenhum parâmetro de `engineering/master-parameters.yaml` foi alterado: este pacote não confirmou nenhuma
   **dimensão** de âncora do §2 em fonte primária. O que ele confirmou foi a existência, a autoria, a
   titularidade e o conteúdo da patente do escape — e isso ficou nos claims e no evidence ledger.

## 6. Critério de aceitação

"Nenhuma dimensão extraída de desenho de patente sem marcação explícita como não-escala": cumprido — **nenhuma
dimensão foi extraída de desenho algum**. Os três únicos números que atravessaram para os claims (0–45° da
parede externa da corna, razão ≥ 2 entre distâncias de centros, alongamento de 360°+β) são **literais do texto**
e estão marcados como pertencentes à invenção, não ao RMUP-01. A regra "desenho de patente não é escala" está
repetida no cabeçalho do `PATENT-TREE.md`, na tabela de figuras, no `patents.csv` (linha do registro de desenho)
e nas notas dos claims de classe B.
