# SQLUser.MR_PictConsRef

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REF_ParRef | varchar | PK |  | NO | MR_Pictures Parent Reference |
| ChildQ04DR | - |  |  | SI | Child Reference: Pressure Areas |
| Q03Q1 | - |  |  | SI | Dressing Location |
| Q03Q2 | - |  |  | SI | Dressing Type |
| Q03Q3 | - |  |  | SI | Dressing Condition |
| Q03Q4 | - |  |  | SI | Exudate |
| Q03Q5 | - |  |  | SI | Odour |
| Q03Q6 | - |  |  | SI | Next Scheduled Dressing Change |
| Q03Q7 | - |  |  | SI | Wound Examination. Size (Length / Width / Depth in... |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REF_Childsub | double |  |  | NO | Childsub |
| REF_ConsultRef_DR | varchar |  | FK | SI | Des Ref ConsultRef |
| REF_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*