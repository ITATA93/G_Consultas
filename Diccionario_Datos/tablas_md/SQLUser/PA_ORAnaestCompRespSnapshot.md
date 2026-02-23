# SQLUser.PA_ORAnaestCompRespSnapshot

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAACR_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAACR_ChildSub | double |  |  | NO | Childsub |
| PAACR_RowId | varchar |  |  | NO | - |
| PAACR_Type_DR | bigint |  | FK | SI | Des Ref User.ORCAncillaryCareEquipment |
| Q09Q1 | - |  |  | SI | Complicación |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*