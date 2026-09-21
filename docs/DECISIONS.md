# Decisões (ADR simplificado)

## DEC-001 — Executor: agentes Claude Opus; Codex em pausa (20/09/2026)
Contexto: `CLAUDE.md` §11 prevê Codex para solvers e automações. Pedro reduziu o uso do Codex em 20/09 por custo. Decisão: enquanto durar, os pacotes de implementação vão para agentes Opus, mantendo o padrão de pacote e a revisão adversarial (A propõe, B falsifica). Reversível quando Pedro liberar o Codex.

## DEC-002 — Material de entrada de Pedro é corpus de pesquisa, não fonte primária automática (20/09/2026)
As 19 imagens e 2 vídeos em `research/images` e `research/videos` vieram da pasta de Pedro sem URL de origem. Entram no manifesto como `origem: acervo Pedro, procedência a confirmar`, classe de uso "pesquisa interna", direitos "desconhecidos, presumidos do fabricante/imprensa"; não vão para o site. Cada um deve ser reencontrado na fonte pública original para ganhar `source_id` completo.

## DEC-003 — Classe de evidência depende da natureza da imagem (21/09/2026)
Achado do TASK-P1-004: 12 dos 19 arquivos do acervo inicial são previews de um modelo 3D comercial (Hum3D) e parte do material oficial é render (nomes de arquivo com pipeline CG e data anterior ao lançamento). Decisão: todo item do catálogo de imagens leva `natureza` (fotografia | render oficial | render de terceiro | quadro de vídeo | desenho de registro); medida tirada de render oficial nasce classe **E** (hipótese), nunca C; render de terceiro é proibido como evidência (só registro do descarte); fotografia e quadro de vídeo podem gerar C após homografia e âncoras no mesmo plano (§7). Imagens oficiais guardadas localmente ficam fora do repositório público (`research/images/rm-oficial/` no .gitignore); entram só manifesto, URL e sha256.
