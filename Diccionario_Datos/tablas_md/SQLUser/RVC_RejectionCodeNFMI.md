# SQLUser.RVC_RejectionCodeNFMI

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RNFMI_RowId | bigint | PK |  | NO | - |
| RNFMI_Code | varchar |  |  | NO | Code |
| RNFMI_CreatedDate | date |  |  | SI | Created Date |
| RNFMI_CreatedTime | time |  |  | SI | Created Time |
| RNFMI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RNFMI_Desc | varchar |  |  | NO | Description |
| RNFMI_UpdatedDate | date |  |  | SI | Updated Date |
| RNFMI_UpdatedTime | time |  |  | SI | Updated Time |
| RNFMI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*