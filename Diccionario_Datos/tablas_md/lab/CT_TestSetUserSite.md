# lab.CT_TestSetUserSite

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSG_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSG_CompletionDate | varchar |  |  | SI | Completion Date |
| CTTSG_CompletionTime | varchar |  |  | SI | Completion Time |
| CTTSG_ForcedMove | varchar |  |  | SI | Forced Move |
| CTTSG_LabelAliquot_DR | varchar |  | FK | SI | Label Aliquot DR |
| CTTSG_LabelMain_DR | varchar |  | FK | SI | Label Main DR |
| CTTSG_MoveToRefferalLab_DR | varchar |  | FK | SI | move to RefferalLab DR |
| CTTSG_MoveToUserSite_DR | varchar |  | FK | SI | move to User Site DR |
| CTTSG_RowID | varchar |  |  | NO | - |
| CTTSG_UserSite_DR | varchar |  | FK | NO | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*