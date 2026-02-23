# SQLUser.RBC_ServInfEBooking

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SERINFEB_RowId | bigint | PK |  | NO | - |
| SERINFEB_Code | varchar |  |  | NO | Code |
| SERINFEB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SERINFEB_CreatedDate | date |  |  | SI | Created Date |
| SERINFEB_CreatedTime | time |  |  | SI | Created Time |
| SERINFEB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SERINFEB_DateFrom | date |  |  | SI | DateFrom |
| SERINFEB_DateTo | date |  |  | SI | DateTo |
| SERINFEB_Desc | varchar |  |  | NO | Description |
| SERINFEB_Owner | varchar |  |  | SI | Owner |
| SERINFEB_UpdatedDate | date |  |  | SI | Updated Date |
| SERINFEB_UpdatedTime | time |  |  | SI | Updated Time |
| SERINFEB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*