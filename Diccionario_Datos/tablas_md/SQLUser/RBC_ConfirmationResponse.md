# SQLUser.RBC_ConfirmationResponse

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONFRESP_RowId | bigint | PK |  | NO | - |
| CONFRESP_Code | varchar |  |  | NO | Code |
| CONFRESP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONFRESP_CreatedDate | date |  |  | SI | Created Date |
| CONFRESP_CreatedTime | time |  |  | SI | Created Time |
| CONFRESP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONFRESP_DateFrom | date |  |  | SI | Date From |
| CONFRESP_DateTo | date |  |  | SI | Date To |
| CONFRESP_Desc | varchar |  |  | NO | Description |
| CONFRESP_NationalCode | varchar |  |  | SI | National Code |
| CONFRESP_Owner | varchar |  |  | SI | Owner |
| CONFRESP_UpdatedDate | date |  |  | SI | Updated Date |
| CONFRESP_UpdatedTime | time |  |  | SI | Updated Time |
| CONFRESP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*