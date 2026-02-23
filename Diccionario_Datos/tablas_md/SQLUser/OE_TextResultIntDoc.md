# SQLUser.OE_TextResultIntDoc

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTDOC_ParRef | bigint | PK |  | NO | OE_TextResult Parent Reference |
| ChildQ41DR | - |  |  | SI | Child Reference: Signs |
| INTDOC_Childsub | double |  |  | NO | Childsub |
| INTDOC_IntDoc_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| INTDOC_RowId | varchar |  |  | NO | - |
| Q26Q1 | - |  |  | SI | Activity |
| Q26Q2 | - |  |  | SI | Right arm |
| Q26Q3 | - |  |  | SI | Left arm |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*