# SQLUser.RTC_MRecordTypeLinkTypes

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_ParRef | bigint | PK |  | NO | RTC_MRecordType Parent Reference |
| LINK_Childsub | double |  |  | NO | Childsub |
| LINK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LINK_CreatedDate | date |  |  | SI | Created Date |
| LINK_CreatedTime | time |  |  | SI | Created Time |
| LINK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LINK_MRType_DR | bigint |  | FK | SI | Des Ref MRType |
| LINK_RowId | varchar |  |  | NO | - |
| LINK_UpdatedDate | date |  |  | SI | Updated Date |
| LINK_UpdatedTime | time |  |  | SI | Updated Time |
| LINK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*