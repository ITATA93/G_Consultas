# SQLUser.OR_AnaestSurgPathwayDiscrCount

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISCRCNT_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| DISCRCNT_Childsub | numeric |  |  | NO | Childsub |
| DISCRCNT_DiscrepCount_DR | bigint |  | FK | NO |  Des Ref ORC_DiscrepanciesInCount  |
| DISCRCNT_RowId | varchar |  |  | NO | - |
| Q80Q1 | - |  |  | SI | Date |
| Q80Q2 | - |  |  | SI | Time |
| Q80Q3 | - |  |  | SI | Responsible person |
| Q80Q4 | - |  |  | SI | Action |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*