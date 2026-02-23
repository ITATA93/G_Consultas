# SQLUser.OE_TextResultNok

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOK_ParRef | bigint | PK |  | NO | OE_TextResult Parent Reference |
| ChildQ42DR | - |  |  | SI | Child Reference: Range of  Motion (ROM) |
| NOK_Childsub | double |  |  | NO | Childsub |
| NOK_Nok_DR | varchar |  | FK | SI | Des Ref PANok |
| NOK_RowId | varchar |  |  | NO | - |
| Q41Q1 | - |  |  | SI | Tenderness |
| Q41Q2 | - |  |  | SI | Other location |
| Q41Q3 | - |  |  | SI | Right arm |
| Q41Q4 | - |  |  | SI | Left arm |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*