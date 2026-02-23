# lab.DEB_DebtorTransaction

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBTR_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBTR_Comment | varchar |  |  | SI | Comment |
| DEBTR_DateOfTransaction | date |  |  | NO | Date Of Transaction |
| DEBTR_RowId | varchar |  |  | NO | - |
| DEBTR_TransactionRID | varchar |  |  | NO | Transaction RID |
| DEBTR_Type | varchar |  |  | NO | Type |
| DEBTR_xxx1 | varchar |  |  | SI | Date |
| DEBTR_xxx2 | varchar |  |  | SI | Amount |
| DEBTR_xxx3 | varchar |  |  | SI | Amount Remaining |
| DEBTR_xxx4 | varchar |  |  | SI | Comment 2 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*