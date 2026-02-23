# SQLUser.RVC_ReasonCutNFMI

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNFMI_RowId | bigint | PK |  | NO | - |
| CNFMI_Code | varchar |  |  | NO | Code |
| CNFMI_CreatedDate | date |  |  | SI | Created Date |
| CNFMI_CreatedTime | time |  |  | SI | Created Time |
| CNFMI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNFMI_Desc | varchar |  |  | NO | Description |
| CNFMI_UpdatedDate | date |  |  | SI | Updated Date |
| CNFMI_UpdatedTime | time |  |  | SI | Updated Time |
| CNFMI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*