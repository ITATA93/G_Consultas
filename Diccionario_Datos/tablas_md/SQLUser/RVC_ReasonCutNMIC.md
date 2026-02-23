# SQLUser.RVC_ReasonCutNMIC

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración RV**. Parámetros de revisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNMIC_RowId | bigint | PK |  | NO | - |
| CNMIC_Code | varchar |  |  | NO | Code |
| CNMIC_CreatedDate | date |  |  | SI | Created Date |
| CNMIC_CreatedTime | time |  |  | SI | Created Time |
| CNMIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNMIC_Desc | varchar |  |  | NO | Description |
| CNMIC_UpdatedDate | date |  |  | SI | Updated Date |
| CNMIC_UpdatedTime | time |  |  | SI | Updated Time |
| CNMIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*