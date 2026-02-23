# lab.CTBB_TransfusionEvent

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBTE_RowID | varchar | PK |  | NO | - |
| BBTE_BloodProduct_DR | varchar |  | FK | SI | Blood Product DR |
| BBTE_Code | varchar |  |  | NO | Code |
| BBTE_Description | varchar |  |  | SI | Description |
| BBTE_NumberOfUnits | numeric |  |  | SI | Number Of Units |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*