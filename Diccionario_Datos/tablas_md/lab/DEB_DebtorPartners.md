# lab.DEB_DebtorPartners

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBPR_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBPR_DateEnd | date |  |  | SI | End Date |
| DEBPR_DateStart | date |  |  | SI | Start Date |
| DEBPR_Partner_DR | varchar |  | FK | NO | Des RefPartner |
| DEBPR_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*