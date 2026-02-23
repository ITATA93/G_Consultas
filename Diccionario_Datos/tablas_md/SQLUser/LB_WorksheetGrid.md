# SQLUser.LB_WorksheetGrid

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWG_RowID | bigint | PK |  | NO | - |
| ChildQ39DR | - |  |  | SI | Child Reference: Abdomen y dorso |
| LBWG_Comments | varchar |  |  | SI | Comments |
| LBWG_DateCreated | date |  |  | NO | Date Created |
| LBWG_WorksheetSystemID | varchar |  |  | SI | System Counter ID |
| LBWG_Worksheet_DR | bigint |  | FK | NO | Code Table Reference |
| Q35Q1 | - |  |  | SI | Percusión |
| Q35Q2 | - |  |  | SI | Auscultación |
| Q35Q3 | - |  |  | SI | Localización |
| Q35Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*