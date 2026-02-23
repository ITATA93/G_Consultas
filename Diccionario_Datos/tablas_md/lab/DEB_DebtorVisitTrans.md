# lab.DEB_DebtorVisitTrans

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBVT_ParRef | varchar | PK |  | NO | DEB_DebtorVisits Parent Reference |
| DEBVT_Amount | double |  |  | SI | Amount |
| DEBVT_Date | date |  |  | SI | Date |
| DEBVT_RowId | varchar |  |  | NO | - |
| DEBVT_TransactionRID | varchar |  |  | NO | Transaction RID |
| DEBVT_Type | varchar |  |  | NO | Transaction Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*