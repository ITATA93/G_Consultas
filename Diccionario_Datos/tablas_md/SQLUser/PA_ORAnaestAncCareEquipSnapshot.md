# SQLUser.PA_ORAnaestAncCareEquipSnapshot

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAACE_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| ChildQ23DR | - |  |  | SI | Child Reference: Listado Complicaciones del parto |
| PAACE_ChildSub | double |  |  | NO | Childsub |
| PAACE_RowId | varchar |  |  | NO | - |
| PAACE_Type_DR | bigint |  | FK | SI | Des Ref User.ORCAncillaryCareEquipment |
| Q18Q1 | - |  |  | SI | Técnica |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*