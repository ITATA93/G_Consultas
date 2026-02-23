# SQLUser.RBC_ReasonNotAvail

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RNAV_RowId | bigint | PK |  | NO | - |
| RNAV_Code | varchar |  |  | NO | Code |
| RNAV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RNAV_CreatedDate | date |  |  | SI | Created Date |
| RNAV_CreatedTime | time |  |  | SI | Created Time |
| RNAV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RNAV_DateFrom | date |  |  | SI | Date From |
| RNAV_DateTo | date |  |  | SI | Date To |
| RNAV_Desc | varchar |  |  | NO | Description |
| RNAV_Owner | varchar |  |  | SI | Owner |
| RNAV_Type | varchar |  |  | SI | Type |
| RNAV_UpdatedDate | date |  |  | SI | Updated Date |
| RNAV_UpdatedTime | time |  |  | SI | Updated Time |
| RNAV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*