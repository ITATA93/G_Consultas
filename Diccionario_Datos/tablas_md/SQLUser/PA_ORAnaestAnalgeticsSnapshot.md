# SQLUser.PA_ORAnaestAnalgeticsSnapshot

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAANL_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| ChildQ18DR | - |  |  | SI | Child Reference: Listado Técnica Analgésica |
| PAANL_ChildSub | double |  |  | NO | Childsub |
| PAANL_RowId | varchar |  |  | NO | - |
| PAANL_Type_DR | bigint |  | FK | SI | Des Ref PACAnalgetics |
| Q17Q1 | - |  |  | SI | Método |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*