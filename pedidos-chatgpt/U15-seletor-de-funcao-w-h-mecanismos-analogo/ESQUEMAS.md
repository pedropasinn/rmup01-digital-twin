# Esquemas dos CSV do projeto

source-manifest.csv: source_id,type,title,author,outlet,date,url,language,accessed_at,local_path,sha256,rights,claims_supported,visual_quality,reliability,notes

claims.csv: claim_id,subsystem,statement,evidence_class,source_ids,parameter_id,status,created_at,notes

evidence-ledger.csv: evidence_id,claim_id,parameter_id,part_id,source_id,evidence_class,method,nominal_value,unit,lower_bound,upper_bound,confidence_notes,status,created_at,updated_at
