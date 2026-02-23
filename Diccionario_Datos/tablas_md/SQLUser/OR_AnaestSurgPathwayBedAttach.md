# SQLUser.OR_AnaestSurgPathwayBedAttach

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BEDATT_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| BEDATT_Childsub | numeric |  |  | NO | Childsub |
| BEDATT_Equipment_DR | bigint |  | FK | NO |  Des Ref ORC_Equipment |
| BEDATT_RowId | varchar |  |  | NO | - |
| ChildQ02DR | - |  |  | SI | Child Reference: Staff members present |
| Q16Q1 | - |  |  | SI | Name |
| Q16Q2 | - |  |  | SI | Language |
| Q16Q3 | - |  |  | SI | Time arrived |
| Q16Q4 | - |  |  | SI | Time departed |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*