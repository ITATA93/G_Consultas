# SQLUser.MR_PictEnqCont

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENQ_ParRef | varchar | PK |  | NO | MR_Pictures Parent Reference |
| ChildQ02DR | - |  |  | SI | Child Reference: Drains |
| ENQ_Childsub | double |  |  | NO | Childsub |
| ENQ_EnquiryContact_DR | bigint |  | FK | SI | Des Ref PAEnquiryContact |
| ENQ_RowId | varchar |  |  | NO | - |
| Q04Q1 | - |  |  | SI | Location / Condition |
| Q04Q2 | - |  |  | SI | Condition |
| Q04Q3 | - |  |  | SI | Ulcer Grading |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*