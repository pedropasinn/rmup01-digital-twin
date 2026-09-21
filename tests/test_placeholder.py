"""Testes vazios da Fase 0: cada pasta ganha testes reais quando o subsistema existir."""
import csv, pathlib
RAIZ = pathlib.Path(__file__).resolve().parents[1]

def test_esquemas_existem():
    for f in ['research/source-manifest.csv', 'research/claims.csv', 'evidence/evidence-ledger.csv', 'engineering/master-parameters.yaml']:
        assert (RAIZ / f).exists(), f

def test_ledger_cabecalho():
    with open(RAIZ / 'evidence/evidence-ledger.csv', encoding='utf-8') as fh:
        cab = next(csv.reader(fh))
    assert cab[:3] == ['evidence_id', 'claim_id', 'parameter_id']
