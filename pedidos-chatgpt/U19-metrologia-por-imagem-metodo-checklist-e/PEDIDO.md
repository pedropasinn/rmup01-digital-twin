# U19 — Metrologia por imagem: método, checklist e script para calibrar fotos oficiais

1. No Balcão, abra o pedido U19 e marque Rodei.
2. Cole o prompt no ChatGPT (GPT-6 Pro).
3. Salve a resposta como U19-entrega.zip em ~/repo/rmup01-digital-twin/_entrada/Balcao/.

---

PEDIDO U19 — Metrologia por imagem: método, checklist e script para calibrar fotos oficiais

CONTEXTO
Projeto independente, educacional e não afiliado: reconstrução forense digital do Richard Mille RM UP-01 Ferrari e do calibre RMUP-01 a partir de fontes públicas (repositório aberto github.com/pedropasinn/rmup01-digital-twin). Regra central: toda afirmação carrega classe de evidência — A primária (fabricante, patente, documento oficial), B observada (visível em foto/vídeo), C medida (metrologia de imagem), D inferida (imposta por geometria/cinemática), E hipótese, F placeholder — e fonte com URL real. Nunca apresentar C, D, E ou F como A. Âncoras já conhecidas a confirmar: relógio 1,75 mm; calibre 41,45 × 28,85 × 1,18 mm; corda manual; seletor W/H; ~45 h; 23 rubis; balanço titânio grau 5 de três braços e seis massas; 3 mg·cm²; ângulo de levantamento 54°; 28 800 A/h; espiral AK 3; Kif; barrilete ~6 h/volta; platina e pontes em titânio grau 5; escape ultraplano patenteado sem dart/guard pin e safety roller (EP3754433A1 / CH716337A1 / US11550262B2, Giulio Papi, prioridade 2019); cristais 0,45 mm (horas) e 0,20/0,30 mm (balanço); 13 parafusos spline; 1 atm; > 6 000 h de desenvolvimento; tolerâncias de 1 μm citadas; involuta 20° citada para winding-barrel e pinhão da terceira.
REGRAS
1. Só fontes públicas obtidas legitimamente; paywall se registra (título, veículo, URL), não se contorna; nada vazado.
2. Toda fonte com: título original, autor, veículo, data, URL (que exista), idioma, tipo; toda afirmação com classe A–F e fonte. Nunca inventar URL, número, autor ou citação. Marcar hipótese como hipótese.
3. Desenhos de patente não são escala: nunca extrair medidas deles.
4. Português brasileiro; tabelas; resumos próprios (não copie textos longos); traduções só para entendimento, preservando o original.
5. Entrega: um único zip <ID>-entrega.zip com a estrutura pedida, um LEIA-ME.md de meia página e um fontes.csv (source_id local, title, author, outlet, date, url, language, type, rights, claims_supported, notes) e um claims.csv (claim_id local, subsystem, statement, evidence_class, sources, parameter, notes).

TAREFA — Especificar e implementar (Python 3, só biblioteca padrão + opcionalmente numpy) o método de metrologia por imagem do projeto: escolha de âncoras no mesmo plano (ex.: largura do calibre 41,45 mm, diâmetros de cristal, cabeças dos 13 parafusos), correção de perspectiva por homografia a partir de 4+ pontos, conversão pixel → mm com propagação de incerteza, repetição em imagens independentes e cálculo de dispersão, métrica de erro de projeção para overlay CAD→foto, e contagem de dentes por periodicidade angular de borda. Entregar `metrologia/METODO.md` (passo a passo, armadilhas: lente, oblíqua, Z), `metrologia/homografia.py` (funções + exemplo com pontos sintéticos e teste), `metrologia/dentes.py` (contagem por periodicidade em um perfil de intensidade de exemplo), `metrologia/checklist.md`, fontes (bibliografia de visão computacional e fotogrametria com referências completas).

Devolva um único arquivo zip chamado U19-entrega.zip.

Onde estão os materiais de apoio (texto, pelo conector agenthub-tunnel): list_artifacts(run_id="run_20260921T030240_b853b8") e get_artifact(artifact_id=..., max_chars=60000). CHARTER.md (convenções de IDs) e ESQUEMAS.md (colunas dos CSV). Se o conector não responder, diga isso em vez de improvisar.
