# TASK-P2-007 — Contagem de dentes por periodicidade angular

**Fase:** 7 · **Prioridade:** média-alta, paralelo a TASK-P2-006 · **Bloco de IDs:** `CLM-1300…1349`, `EVD-1300…1349`
**Testes:** V-T01, V-T04

## Objetivo
Contar dentes por periodicidade angular de borda nas rodas em que a imagem permite, e entregar ao
`gear_search` restrições inteiras em vez de faixas.

## Contexto
`CLAUDE.md` §7 especifica o método: periodicidade angular da borda, contagem manual independente, detecção
computacional, restrições inteiras por razão, teste de candidatos vizinhos, registro de alternativas. O
corpus oferece três alvos: **IMG-0029** (dentado do barrilete parcialmente resolvido), **IMG-0005** (roda
grande esqueletada de 7 braços, em vista rasante — só um arco utilizável) e **IMG-0031** (dentado fino da
roda das horas).

## Fontes permitidas
IMG-0005, IMG-0029, IMG-0031, IMG-0026; quadros adicionais do filme se um deles resolver melhor a borda
(reproduzíveis pelo script existente).

## Entradas
`evidence/image-landmarks/candidatos.csv` (LMK-IMG0029-001, LMK-IMG0005-001);
`solvers/image_metrology/homografia.py`.

## Saídas obrigatórias
1. `solvers/image_metrology/dentes.py` — contagem por periodicidade em perfil de intensidade angular,
   com FFT ou autocorrelação, e teste sobre um perfil sintético de contagem conhecida.
2. `evidence/measurements/P2-007-dentes.csv` — por roda: contagem estimada, arco utilizado, intervalo de
   confiança, candidatos vizinhos não excluídos.
3. Contagem manual independente registrada ao lado da computacional, com a divergência explicitada.
4. `agent-tasks/review/TASK-P2-007.md`.

## Restrições
- Correção de perspectiva **antes** de contar: em IMG-0005 a vista é rasante e contar direto produz erro
  sistemático.
- Se só um arco do perímetro for utilizável, o resultado é uma **faixa de candidatos**, não um número.
- Registrar alternativas até confirmação (§7). Um número isolado sem candidatos vizinhos é suspeito.
- IMG-0031 é quadro de vídeo a 1080p: o dentado das horas pode estar abaixo do limite de resolução. Dizer
  isso em vez de forçar uma contagem.

## Questões abertas endereçadas
Q-TRN-005, Q-BAR-001, Q-TRN-002, Q-IND-001.

## Testes
O `dentes.py` recupera a contagem correta de um perfil sintético com ruído; a contagem manual e a
computacional concordam ou a divergência é explicada.

## Critério de aceitação
Ao menos uma roda com faixa de candidatos estreita o bastante para restringir o `gear_search`, ou a
demonstração documentada de que nenhuma imagem do corpus permite contar.

## Arquivos que podem ser alterados
`solvers/image_metrology/**`, `evidence/measurements/**`, `research/claims.csv`,
`docs/OPEN-QUESTIONS.md`, `docs/RESEARCH-LOG.md`, `agent-tasks/review/TASK-P2-007.md`.

## Arquivos que NÃO podem ser alterados
`CLAUDE.md`, `docs/DECISIONS.md`, `docs/ARCHITECTURE.md`, `engineering/master-parameters.yaml`,
`research/images/catalogo.csv`.
