# SQLUser.PA_BedHistory

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Gestión de Camas**. Control de ocupación y asignación. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BH_RowId | bigint | PK |  | NO | - |
| BH_AdmTransaction_DR | varchar |  | FK | SI | Des Ref AdmTransaction |
| BH_Bed_DR | varchar |  | FK | SI | Des Ref Bed |
| BH_DateFrom | date |  |  | SI | Date From |
| BH_DateTo | date |  |  | SI | Date To |
| BH_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| BH_TimeFrom | time |  |  | SI | Time From |
| BH_TimeTo | time |  |  | SI | Time To |
| BH_Ward_DR | bigint |  | FK | SI | Des Ref Ward |
| Q16Q1 | - |  |  | SI | Date |
| Q16Q2 | - |  |  | SI | Time |
| Q16Q3 | - |  |  | SI | Catheter Check |
| Q16Q4 | - |  |  | SI | Actions |
| Q16Q7 | - |  |  | SI | Comments |
| Q16Q8 | - |  |  | SI | Urinary specimen taken |
| Q16Q9 | - |  |  | SI | Insertion site swab taken |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*