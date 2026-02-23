# SQLUser.PHC_AIFANotes

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AIFAN_RowId | bigint | PK |  | NO | - |
| AIFAN_Code | varchar |  |  | NO | Code |
| AIFAN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AIFAN_CreatedDate | date |  |  | SI | Created Date |
| AIFAN_CreatedTime | time |  |  | SI | Created Time |
| AIFAN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AIFAN_DateFrom | date |  |  | SI | Date From |
| AIFAN_DateTo | date |  |  | SI | Date To |
| AIFAN_Desc | varchar |  |  | NO | Description |
| AIFAN_HTMLDesc | bigint |  |  | SI | Des Ref websys.Document |
| AIFAN_HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| AIFAN_LongDesc | varchar |  |  | SI | LongDescription |
| AIFAN_Owner | varchar |  |  | SI | Owner |
| AIFAN_UpdatedDate | date |  |  | SI | Updated Date |
| AIFAN_UpdatedTime | time |  |  | SI | Updated Time |
| AIFAN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*