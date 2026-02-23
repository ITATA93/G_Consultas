# SQLUser.PHC_Type

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCPT_RowId | bigint | PK |  | NO | - |
| PHCPT_Code | varchar |  |  | NO | Code |
| PHCPT_CreatedDate | date |  |  | SI | Created Date |
| PHCPT_CreatedTime | time |  |  | SI | Created Time |
| PHCPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCPT_Desc | varchar |  |  | SI | Description |
| PHCPT_UpdatedDate | date |  |  | SI | Updated Date |
| PHCPT_UpdatedTime | time |  |  | SI | Updated Time |
| PHCPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*