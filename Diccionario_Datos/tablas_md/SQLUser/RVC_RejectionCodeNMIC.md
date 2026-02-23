# SQLUser.RVC_RejectionCodeNMIC

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RNMIC_RowId | bigint | PK |  | NO | - |
| RNMIC_Code | varchar |  |  | NO | Code |
| RNMIC_CreatedDate | date |  |  | SI | Created Date |
| RNMIC_CreatedTime | time |  |  | SI | Created Time |
| RNMIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RNMIC_Desc | varchar |  |  | NO | Description |
| RNMIC_UpdatedDate | date |  |  | SI | Updated Date |
| RNMIC_UpdatedTime | time |  |  | SI | Updated Time |
| RNMIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*