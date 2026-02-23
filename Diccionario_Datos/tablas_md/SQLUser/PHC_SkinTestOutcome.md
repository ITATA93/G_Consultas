# SQLUser.PHC_SkinTestOutcome

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SKTO_RowId | bigint | PK |  | NO | - |
| SKOT_CanAdminister | varchar |  |  | SI | CanAdminister |
| SKTO_Code | varchar |  |  | SI | Code |
| SKTO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SKTO_CreatedDate | date |  |  | SI | Created Date |
| SKTO_CreatedTime | time |  |  | SI | Created Time |
| SKTO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SKTO_DateFrom | date |  |  | SI | Date From |
| SKTO_DateTo | date |  |  | SI | Date To |
| SKTO_Desc | varchar |  |  | SI | Description |
| SKTO_Owner | varchar |  |  | SI | Owner |
| SKTO_UpdatedDate | date |  |  | SI | Updated Date |
| SKTO_UpdatedTime | time |  |  | SI | Updated Time |
| SKTO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*