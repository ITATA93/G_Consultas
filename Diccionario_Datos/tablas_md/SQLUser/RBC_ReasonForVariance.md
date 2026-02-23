# SQLUser.RBC_ReasonForVariance

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAVAR_RowId | bigint | PK |  | NO | - |
| REAVAR_Code | varchar |  |  | NO | Code |
| REAVAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REAVAR_CreatedDate | date |  |  | SI | Created Date |
| REAVAR_CreatedTime | time |  |  | SI | Created Time |
| REAVAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REAVAR_DateFrom | date |  |  | SI | Date From |
| REAVAR_DateTo | date |  |  | SI | Date To |
| REAVAR_Desc | varchar |  |  | NO | Description |
| REAVAR_Owner | varchar |  |  | SI | Owner |
| REAVAR_UpdatedDate | date |  |  | SI | Updated Date |
| REAVAR_UpdatedTime | time |  |  | SI | Updated Time |
| REAVAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*