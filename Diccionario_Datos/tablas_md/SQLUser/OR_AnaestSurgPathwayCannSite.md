# SQLUser.OR_AnaestSurgPathwayCannSite

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANNS_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| CANNS_CannInsSite_DR | bigint |  | FK | NO |  Des Ref ORCCannulaInsertionSite |
| CANNS_Childsub | numeric |  |  | NO | Childsub |
| CANNS_RowId | varchar |  |  | NO | - |
| Q02Q1 | - |  |  | SI | Name |
| Q02Q2 | - |  |  | SI | Position |
| Q02Q3 | - |  |  | SI | Speciality |
| Q02Q4 | - |  |  | SI | Time arrived |
| Q02Q5 | - |  |  | SI | Time departed |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*