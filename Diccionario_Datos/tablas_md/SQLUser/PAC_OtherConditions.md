# SQLUser.PAC_OtherConditions

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTHCON_Code | varchar | PK |  | NO | Code |
| OTHCON_CodeTableTags | varchar | PK |  | SI | List of code table Tags |
| OTHCON_CreatedDate | date | PK |  | SI | Created Date |
| OTHCON_CreatedTime | time | PK |  | SI | Created Time |
| OTHCON_CreatedUser_DR | bigint | PK | FK | SI | Created User |
| OTHCON_DateFrom | date | PK |  | SI | Date From |
| OTHCON_DateTo | date | PK |  | SI | Date To |
| OTHCON_Desc | varchar | PK |  | NO | Description |
| OTHCON_Owner | varchar | PK |  | SI | Owner |
| OTHCON_RowId | bigint | PK |  | NO | - |
| OTHCON_UpdatedDate | date | PK |  | SI | Updated Date |
| OTHCON_UpdatedTime | time | PK |  | SI | Updated Time |
| OTHCON_UpdatedUser_DR | bigint | PK | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*