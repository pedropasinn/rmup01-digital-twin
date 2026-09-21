# Catálogo de imagens e vídeo — RM UP-01 / calibre RMUP-01

Produzido pelo **TASK-P1-004** em 2026-09-21. Dados brutos em `research/images/catalogo.csv`,
`research/videos/VID-0001-quadros.csv` e `research/videos/VID-0002-quadros.csv`.
Candidatos a landmark em `evidence/image-landmarks/candidatos.csv`.

---

## 1. O achado que reorganiza o corpus

Dos 19 arquivos de imagem entregues por Pedro, **12 não são fotografias do relógio**. São previews de
renderização de um modelo 3D comercial de terceiro, com a marca d'água `Hum3D TOOLS #1319` impressa na
própria imagem; dois deles mostram a malha poligonal do modelador em wireframe, e um terceiro exibe um
mostrador preto com ponteiro vermelho que nenhuma imagem oficial reproduz. Ficaram catalogados como
`IMG-0014`…`IMG-0025` **com uso proibido como evidência** (CLM-0700).

O segundo achado é mais incômodo, porque afeta material oficial: **boa parte das imagens publicadas pela
própria Richard Mille também é CG**, não fotografia. Os nomes dos arquivos denunciam o pipeline
(`3DUP3PH…`, `…CSmoothing1`, data de render `2021-12-14` — sete meses antes do lançamento), e o filme
institucional alterna livremente entre render e filmagem real (CLM-0710). Por isso o catálogo ganhou uma
coluna `natureza` com quatro valores: `fotografia_oficial`, `render_CG_oficial`, `render_CG_terceiro`,
`quadro_de_video`. **Imagem oficial não é automaticamente evidência classe B do objeto físico.**

A consequência prática: o corpus de imagens realmente utilizável é bem menor do que 19 arquivos — mas
ficou maior do que era, porque o vídeo rendeu mais do que as fotos.

## 2. O que entrou de novo

| Origem | O que é | Ganho |
|---|---|---|
| `media.richardmille.com` (originais) | As 7 imagens legítimas do acervo, em resolução original (até 2800 × 1825 em vez de 1000 px) | 1,25× a 2,8× em escala linear |
| Sprite 360° oficial | `360_rmup-01_d01/n01.jpg`: 81 quadros de 800 × 800 cobrindo 360° em passos de 360/81 ≈ 4,44°, em duas iluminações | 162 vistas auto-consistentes do exterior |
| Par ortogonal CG oficial | `3DUP3PHWS` (frente) + `3DUP3PH3h` (perfil 3h) + `3DUP3PHbackWS` (fundo) | Envelope externo em projeção quase ortográfica |
| Filme `RMUP-01_SF_EN.mp4` | 160 quadros a 1 fps + 17 quadros-chave escolhidos por nitidez | **A platina nua** e o **ponteiro de perfil**, que não existem em nenhuma foto |
| `boite155.jpg` | Foto oficial nova, documental | escala humana |

## 3. Matriz vista × subsistema

Legenda: **★★★** melhor material disponível · **★★** utilizável · **★** só indicativo · **—** lacuna.
Entre parênteses, o `image_id` da melhor imagem.

| Subsistema | Plano (dial-up) | Plano (fundo) | Perfil / Z | Macro | Peça isolada | Desmontado |
|---|---|---|---|---|---|---|
| CASE (caixa) | ★★★ IMG-0009 / IMG-0012 | ★★★ IMG-0010, IMG-0034 | ★★ IMG-0011, IMG-0007 | ★★★ IMG-0006 | ★★ IMG-0004 | ★★ IMG-0004 |
| CRY (cristais) | ★★ IMG-0009 | — | ★ IMG-0007 | ★ IMG-0036 | — | ★★ IMG-0004 (aberturas) |
| BASE (platina) | ★★★ IMG-0001 (CG) | — | — | ★★ IMG-0027 | ★★★ **IMG-0026** | ★★★ IMG-0026 |
| BRG (pontes) | ★★★ IMG-0001 (CG) | — | ★ IMG-0033 | ★★ IMG-0029 | ★★★ IMG-0003 + IMG-0028 | ★★★ IMG-0003 |
| BAR (barrilete) | ★★ IMG-0001 (CG) | — | — | ★★ IMG-0029 | — | ★★ IMG-0026 (abertura) |
| TRN (trem) | ★★ IMG-0001 (CG) | — | — | ★★ IMG-0031 | ★★ IMG-0005 | ★★★ IMG-0026 |
| ESC (escape) | ★ IMG-0001 (CG) | — | — | ★ IMG-0029 | — | ★ IMG-0026 |
| OSC (oscilador) | ★★ IMG-0001 (CG) | — | — | ★★ IMG-0029 | — | — |
| IND (indicação) | ★★ IMG-0036 | — | ★★★ **IMG-0030** | ★★★ **IMG-0031** | ★★ IMG-0030 | ★★ IMG-0031 |
| SEL + WND | ★★★ IMG-0006 | ★★ IMG-0010 | — | ★★★ IMG-0006, IMG-0032 | ★★ IMG-0004 (rodas) | ★★★ IMG-0026 |
| JWL (rubis) | ★★ IMG-0001 (CG) | — | — | ★★ IMG-0003 | ★★ IMG-0005 (soltos) | ★★ IMG-0026 |
| SHK (choque) | ★ IMG-0001 (CG) | — | — | ★ IMG-0029 | — | — |
| FST (fixações) | ★★★ IMG-0006 | ★★★ IMG-0010 | — | ★★★ IMG-0006 | — | ★★★ IMG-0004 |
| STR (pulseira) | ★★ IMG-0009 | ★★ IMG-0010 | ★★ IMG-0011 | — | — | — |

### Ranking de utilidade (as sete que importam)

1. **IMG-0026** — platina nua no suporte, quadro do filme a 25,42 s. Os centros de rotação sem nada em
   cima. É a imagem mais valiosa de todo o corpus e não estava no acervo: veio do vídeo.
2. **IMG-0004** (`illup068`) — explodida em plano: luneta, junta, as duas rodas de comando, o fundo e o
   movimento, tudo no mesmo plano e na mesma escala. Candidata nº 1 a calibração por homografia usando
   41,45 × 28,85 mm.
3. **IMG-0012** (sprite 360°) — 81 vistas de um mesmo objeto com rotação de eixo único e passo constante:
   exatamente o insumo que `CLAUDE.md` §7 pede para o ajuste conjunto multivista.
4. **IMG-0027** — movimento dentro da caixa, vista quase nadir: única chance de medir a folga
   movimento–caixa e fixar a origem do sistema de coordenadas (Q-BASE-002).
5. **IMG-0001** — a vista completa do calibre, mas **é render**: serve para topologia e para decidir
   *onde* medir, nunca como fonte da medida.
6. **IMG-0003 + IMG-0028** — a mesma ponte de 3 braços em duas vistas independentes: reconstrução de peça
   por duas vistas.
7. **IMG-0030 / IMG-0031** — o ponteiro de perfil e o acoplamento ponteiro–roda: a evidência visual de que
   não há motion works clássico.

## 4. Lacunas (o que o corpus público NÃO tem)

Nenhuma dessas lacunas deve virar hipótese silenciosa no CAD.

- **Nenhuma imagem do movimento pelo lado da platina (dial-side) com as rodas montadas.** Só a platina nua
  (IMG-0026) ou o movimento já fechado. O caminho de acerto de hora fica invisível.
- **Nenhuma vista do escape isolado.** A peça mais importante do projeto (Fase 9) não tem uma única
  fotografia dedicada em fonte pública. A patente terá de carregar sozinha a topologia — e desenho de
  patente não é desenho em escala (`CLAUDE.md` §2).
- **Nenhuma seção transversal, nenhum corte, nenhum desenho técnico com cotas.** O Z-budget não tem
  nenhuma imagem de apoio: só os números publicados.
- **Nenhuma vista do barrilete aberto**, da mola, do arbor ou da tampa.
- **Nenhuma imagem do seletor W/H em operação** (estado W × estado H lado a lado).
- **Nenhuma macro do balanço com as 6 massas contáveis** nem da espiral.
- **Nenhuma desmontagem de terceiro** (relojoeiro independente, leilão, serviço). Todo o material visual
  público é controlado pela marca.
- **Nenhuma imagem em que os 23 rubis sejam simultaneamente visíveis e contáveis.**

## 5. Regras de uso que saem deste pacote

1. Toda medida extraída de imagem registra `image_id`, `natureza` e `landmark_id`. Medida tirada de
   `render_CG_oficial` nasce classe **E (hipótese)**, não C — um render é a interpretação do departamento
   de comunicação, não o objeto.
2. `render_CG_terceiro` (IMG-0014…IMG-0025) é **proibido** como fonte de qualquer número ou contorno.
3. Calibração só com âncora no **mesmo plano** do que se mede (`CLAUDE.md` §7). Na prática isso reduz o
   material calibrável a IMG-0004, IMG-0026 e IMG-0027.
4. Toda medida repetida em pelo menos duas imagens independentes, com dispersão registrada.
5. Os quadros de vídeo ficam fora do Git (`research/images/frames/` é ignorado); são **reprodutíveis** a
   partir do mp4 e dos timestamps em `VID-0001-quadros.csv`.
