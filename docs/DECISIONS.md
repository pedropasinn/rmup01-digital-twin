# Decisões (ADR simplificado)

## DEC-001 — Executor: agentes Claude Opus; Codex em pausa (20/09/2026)
Contexto: `CLAUDE.md` §11 prevê Codex para solvers e automações. Pedro reduziu o uso do Codex em 20/09 por custo. Decisão: enquanto durar, os pacotes de implementação vão para agentes Opus, mantendo o padrão de pacote e a revisão adversarial (A propõe, B falsifica). Reversível quando Pedro liberar o Codex.

## DEC-002 — Material de entrada de Pedro é corpus de pesquisa, não fonte primária automática (20/09/2026)
As 19 imagens e 2 vídeos em `research/images` e `research/videos` vieram da pasta de Pedro sem URL de origem. Entram no manifesto como `origem: acervo Pedro, procedência a confirmar`, classe de uso "pesquisa interna", direitos "desconhecidos, presumidos do fabricante/imprensa"; não vão para o site. Cada um deve ser reencontrado na fonte pública original para ganhar `source_id` completo.
