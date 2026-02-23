# SQLUser.AR_HICInHospitalClaimStatus

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IHCS_ParRef | bigint | PK |  | NO | - |
| IHCS_AssociateName | varchar |  |  | SI | Name of the associated fund |
| IHCS_LodgementDateTime | varchar |  |  | SI | Date and time of lodgement in medicare's format DD... |
| IHCS_ProcessStatusCode | varchar |  |  | SI | Code to indicate the processing status of the clai... |
| IHCS_ReferenceId | varchar |  |  | SI | Claim ID |
| IHCS_ReportStatusCode | varchar |  |  | SI | Code to indicate the report status
PROCESSING 
I... |
| IHCS_RequestContentType | varchar |  |  | SI | Request type of the claim |
| IHCS_RowID | varchar |  |  | NO | - |
| IHCS_StatusRequestDate | date |  |  | SI | Date of the status request |
| IHCS_StatusRequestTime | time |  |  | SI | Time of the status request |
| IHCS_StatusRequestTransactionID | varchar |  |  | SI | Transaction ID of the status request |
| IHCS_StatusRequestUser_DR | bigint |  | FK | SI | Status request user |
| IHCS_TransactionId | varchar |  |  | SI | Transaction ID
Already resolved to a claim transa... |
| Q61Q1 | - |  |  | SI | Evaluación |
| Q61Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*