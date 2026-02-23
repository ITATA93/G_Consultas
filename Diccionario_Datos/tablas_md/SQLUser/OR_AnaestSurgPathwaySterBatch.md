# SQLUser.OR_AnaestSurgPathwaySterBatch

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STERBT_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| Q68Q1 | - |  |  | SI | Care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| STERBT_BatchNo | varchar |  |  | SI | BatchNo |
| STERBT_Childsub | numeric |  |  | NO | Childsub |
| STERBT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*