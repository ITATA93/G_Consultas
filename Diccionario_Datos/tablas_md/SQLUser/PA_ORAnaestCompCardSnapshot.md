# SQLUser.PA_ORAnaestCompCardSnapshot

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAACC_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| ChildQ25DR | - |  |  | SI | Child Reference: Listado Complicaciones del puerpe... |
| PAACC_ChildSub | double |  |  | NO | Childsub |
| PAACC_RowId | varchar |  |  | NO | - |
| PAACC_Type_DR | bigint |  | FK | SI | Des Ref ORCAnaestComplications |
| Q23Q1 | - |  |  | SI | Complicación |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*