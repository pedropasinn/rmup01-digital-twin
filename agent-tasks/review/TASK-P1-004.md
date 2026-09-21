# TASK-P1-004 — Catálogo de imagens e vídeo · relatório

Executado em 2026-09-20 23:50 → 2026-09-21 01:30 BRT. Sem commit, sem Codex.
Blocos de ID usados: `SRC-0700`…`SRC-0715`, `CLM-0700`…`CLM-0710`, `IMG-0001`…`IMG-0036`,
`VID-0001`/`VID-0002`, `LMK-*`, `Q-IMG-001`…`Q-IMG-009`.

---

## 1. Feito

**(a) Acervo de Pedro processado.** Os 19 arquivos de `research/images/` e os 2 de `research/videos/`
foram medidos (resolução, hash sha256), inspecionados visualmente um a um, classificados por vista,
subsistema, âncoras dimensionais visíveis, qualidade, distorção/perspectiva e natureza, e tiveram a
procedência pública reencontrada por busca descritiva — **sem upload a serviço de terceiro**, conforme
DEC-002 e a restrição do pacote.

**(b) Vídeos.** Extraídos 160 quadros a 1 fps de `RMUP-01_SF_EN.mp4` e os 18 quadros de `caliber.mp4`
para `research/images/frames/` (ignorado pelo Git). Além disso, 17 janelas de interesse foram
reextraídas a 25 fps e, dentro de cada uma, o quadro mais nítido foi escolhido por variância do
laplaciano — evitando o quadro borrado que uma amostragem cega a 1 fps entrega. Os 17 quadros-chave
estão catalogados com timestamp, legenda do filme e conteúdo em `research/videos/VID-0001-quadros.csv`.

**(c) Web.** Levantadas as imagens de maior resolução por vista/subsistema, com URL, dimensões e direitos
registrados. Não houve download em massa: 13 arquivos baixados, todos tecnicamente úteis, ~4,7 MB.

### Saídas

| Arquivo | Conteúdo |
|---|---|
| `research/images/catalogo.csv` | 36 imagens (IMG-0001…IMG-0036), 15 colunas incluindo `natureza` e `distorcao_perspectiva` |
| `docs/IMAGE-CATALOG.md` | Matriz vista × subsistema, ranking de utilidade, lacunas, regras de uso |
| `evidence/image-landmarks/candidatos.csv` | 26 candidatos a landmark com justificativa e prioridade |
| `research/videos/VID-0001-quadros.csv` | 17 quadros-chave com timestamp e timecode |
| `research/videos/VID-0002-quadros.csv` | 2 quadros (o clipe tem 0,72 s) |
| `research/images/rm-oficial/` | 13 originais oficiais em resolução máxima |
| `research/source-manifest.csv` | +16 fontes (SRC-0700…SRC-0715); sha256 de SRC-0009/0010 preenchido |
| `research/claims.csv` | +11 afirmações (CLM-0700…CLM-0710) |
| `docs/OPEN-QUESTIONS.md` | +9 questões Q-IMG-001…Q-IMG-009 |
| `solvers/image_metrology/extrair_quadros_chave.py` | Seleção de quadro por nitidez (reproduz os 17 quadros) |
| `solvers/image_metrology/fatiar_sprite_360.py` | Detecta o número de quadros do sprite por FFT e fatia |

## 2. Os dois achados que mudam o corpus

**12 dos 19 arquivos de Pedro não são fotografias.** São previews de um modelo 3D comercial de terceiro,
com a marca d'água `Hum3D TOOLS #1319` impressa na imagem; dois exibem a malha poligonal em wireframe e um
mostra um mostrador preto com ponteiro vermelho que nenhuma imagem oficial reproduz — invenção do
modelador. Catalogados como `IMG-0014`…`IMG-0025` com **uso proibido como evidência** (CLM-0700). Se
tivessem entrado no projeto como fotografia, teriam contaminado o contorno da caixa e a espessura: o
perfil renderizado por aquele modelo é visivelmente mais grosso que 1,75 mm.

**Parte do material oficial também é CG.** Os nomes dos arquivos entregam o pipeline (`3DUP3PH…`,
`…CSmoothing1`, data de render `2021-12-14`, sete meses antes do lançamento), e o filme institucional
alterna render e filmagem real sem avisar. Daí a regra nova (CLM-0710): o catálogo marca `natureza` em
toda imagem, e **medida tirada de render oficial nasce classe E, não C**. Um render é a interpretação do
departamento de comunicação, não o objeto.

## 3. O que o vídeo entregou e as fotos não tinham

- **A platina nua** (`IMG-0026`, t = 25,42 s), em vista quase perpendicular, presa a um suporte de
  montagem cujas hastes retas e paralelas servem de referência para a homografia. É a única imagem pública
  localizada em que os furos de pivô do lado do trem não estão cobertos por pontes. Passa a ser a imagem
  mais valiosa do corpus inteiro.
- **O movimento dentro da caixa** em vista quase nadir (`IMG-0027`, t = 68,46 s): a única chance de medir a
  folga movimento–caixa e fixar a origem do sistema de coordenadas (Q-BASE-002).
- **O ponteiro de perfil sobre a pinça** (`IMG-0030`, t = 58,88 s) e o acoplamento ponteiro–roda
  (`IMG-0031`): confirmação **visual** de CLM-0037, que até aqui só existia no texto do comunicado.
- **A mesma ponte de 3 braços em segundo ângulo** (`IMG-0028`), formando par com a foto oficial `IMG-0003`.

E o sprite do visualizador 360° da página oficial: uma tira de 64 800 × 800 px que, por análise de
periodicidade (FFT do desvio-padrão por coluna, pico limpo), são **81 quadros de 800 × 800 cobrindo 360°
em passos de 4,44°**, em duas iluminações — 162 vistas auto-consistentes do exterior. Isso fecha o
`SRC-0012` que o TASK-P1-001 tinha deixado em aberto e entrega exatamente o insumo que `CLAUDE.md` §7 pede
para ajuste conjunto multivista.

## 4. O que NÃO foi possível, e por quê

- **URL exata do produto Hum3D** (Q-IMG-001): `hum3d.com` responde 301 para `3dmodels.org`, que devolve
  403 a `curl` e a WebFetch (anti-bot). Não foi contornado — a regra 1 do preâmbulo proíbe. A atribuição
  ficou apoiada na marca d'água e no padrão de nome, o que basta para **descartar** o material, não para
  citá-lo com precisão bibliográfica.
- **Separar render de fotografia com certeza** (Q-IMG-002): o critério é indiciário. Não há declaração da
  marca, e os originais não foram examinados quanto a EXIF neste pacote.
- **Nenhuma imagem do escape isolado, nenhuma seção, nenhum corte, nenhum desenho cotado, nenhuma
  desmontagem de terceiro** existe em fonte pública (Q-IMG-008). Toda a evidência visual do RM UP-01 é
  controlada pela marca. Isso é um limite estrutural do projeto, não uma falha deste pacote, e precisa
  aparecer no site.
- **Galerias de imprensa não agregaram resolução**: SJX serve tudo a 1600 × 1067 e aBlogtoWatch a no
  máximo 2000 × 1333 / 1708 × 2560 — abaixo dos até 2800 × 1825 disponíveis no próprio domínio do
  fabricante. Registradas como SRC-0714/SRC-0715 e **não baixadas**, por não haver ganho.
- **opencv não foi instalado.** PIL + numpy bastaram (FFT para o sprite, variância do laplaciano para a
  nitidez). Nada foi alterado na venv.

## 5. Questões abertas criadas

`Q-IMG-001` procedência Hum3D não confirmável por acesso legítimo · `Q-IMG-002` quais imagens oficiais são
render · `Q-IMG-003` o render oficial é geometricamente fiel? · `Q-IMG-004` onde no contorno curvo se aplica
1,75 mm · `Q-IMG-005` dentes e identidade da roda de `IMG-0005` · `Q-IMG-006` a peça do plano do "escape
patenteado" é mesmo o escape? · `Q-IMG-007` as duas rodas do prolongamento esquerdo são coroa/cliquet? ·
`Q-IMG-008` lacunas estruturais do corpus visual · `Q-IMG-009` não há sprite 360 no eixo horizontal.

## 6. Pendente (para o diretor técnico decidir)

1. **Commit.** `research/images/rm-oficial/` tem 4,7 MB e **não** está no `.gitignore`. Se o diretor
   preferir manter o repositório leve, basta ignorá-lo: o manifesto guarda URL + sha256 de cada arquivo e
   o download é reproduzível. Os quadros de vídeo e as fatias do sprite já ficam fora do Git por
   `.gitignore`, e são reproduzíveis pelos dois scripts em `solvers/image_metrology/`.
2. **DEC-003 sugerida** — formalizar a regra de classe por natureza de imagem: `fotografia_oficial` → B/C;
   `render_CG_oficial` → E; `render_CG_terceiro` → proibido. Hoje isso vive em CLM-0710 e no
   `IMAGE-CATALOG.md`, mas é decisão de método e merece ADR.
3. **Próximo pacote de metrologia** (sugestão): calibrar `IMG-0004` por homografia usando 41,45 × 28,85 mm
   e extrair, nesta ordem, o contorno da caixa, os dois centros de comando e as aberturas dos cristais —
   é o caminho mais curto para fechar Q-BASE-001, Q-CASE-002, Q-CRY-002 e Q-FST-001 de uma vez.
4. **Cruzar `IMG-0001` (render) com `IMG-0026` (platina real)** para responder Q-IMG-003. Se os centros
   convergirem, o render vira guia topológico legítimo; se não, cai para ilustrativo. É um teste barato
   com consequência grande para as Fases 5 e 7.
5. **TASK-P1-002 (patentes)** herda um peso maior do que o previsto: sem nenhuma imagem pública do escape,
   a patente é a única fonte de topologia — e continua valendo que desenho de patente não é desenho em
   escala.
