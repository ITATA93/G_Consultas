# lab.CTBB_TransactionStatus

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBTRS_ParRef | varchar | PK |  | NO | CTBB_Transaction Parent Reference |
| BBTRS_AcceptableFlag | varchar |  |  | SI | Acceptable Flag |
| BBTRS_AllowedOutside | varchar |  |  | SI | Allowable outside controlled area |
| BBTRS_BBModule | varchar |  |  | SI | BB Module (Receive,Split,Trans,Issue,Correc) |
| BBTRS_BBSuperUserOnly | varchar |  |  | SI | BB Super User Only |
| BBTRS_NullFlag | varchar |  |  | SI | Null Flag |
| BBTRS_PatientRequired | varchar |  |  | SI | Patient Required |
| BBTRS_RowID | varchar |  |  | NO | - |
| BBTRS_Sequence | numeric |  |  | NO | Sequence |
| BBTRS_StatusAfter_DR | varchar |  | FK | SI | Status After |
| BBTRS_StatusBefore_DR | varchar |  | FK | SI | Status Before DR |
| BBTRS_XMReaction | varchar |  |  | SI | XM Reaction |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*