# SQLUser.PA_ORAnaestLineSnapshot

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAALINE_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| ChildQ80DR | - |  |  | SI | Child Reference: Desarrollo Psicomotor |
| PAALINE_ChildSub | double |  |  | NO | Childsub |
| PAALINE_RowId | varchar |  |  | NO | - |
| PAALINE_Type_DR | bigint |  | FK | SI | Des Ref ORCLineType |
| Q231Q1 | - |  |  | SI | N° Lesión |
| Q231Q2 | - |  |  | SI | Ubicación |
| Q231Q3 | - |  |  | SI | Lateralidad |
| Q231Q4 | - |  |  | SI | Origen |
| Q231Q5 | - |  |  | SI | Grado |
| Q231Q6 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*