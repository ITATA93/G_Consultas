# SQLUser.RVC_ReviewType

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTYP_RowId | bigint | PK |  | NO | - |
| RTYP_Code | varchar |  |  | NO | Code |
| RTYP_CreatedDate | date |  |  | SI | Created Date |
| RTYP_CreatedTime | time |  |  | SI | Created Time |
| RTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTYP_Desc | varchar |  |  | NO | Description |
| RTYP_PatientType | varchar |  |  | SI | Patient Type |
| RTYP_Type | varchar |  |  | NO | Type |
| RTYP_UpdatedDate | date |  |  | SI | Updated Date |
| RTYP_UpdatedTime | time |  |  | SI | Updated Time |
| RTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*