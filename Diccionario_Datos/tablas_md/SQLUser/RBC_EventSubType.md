# SQLUser.RBC_EventSubType

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUB_ParRef | bigint | PK |  | NO | RBC_EventType Parent Reference |
| SUB_Childsub | double |  |  | NO | Childsub |
| SUB_Code | varchar |  |  | SI | Code |
| SUB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUB_CreatedDate | date |  |  | SI | Created Date |
| SUB_CreatedTime | time |  |  | SI | Created Time |
| SUB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUB_DateFrom | date |  |  | SI | DateFrom |
| SUB_DateTo | date |  |  | SI | DateTo |
| SUB_Desc | varchar |  |  | SI | Description |
| SUB_RowId | varchar |  |  | NO | - |
| SUB_UpdatedDate | date |  |  | SI | Updated Date |
| SUB_UpdatedTime | time |  |  | SI | Updated Time |
| SUB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*