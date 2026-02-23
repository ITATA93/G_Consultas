# SQLUser.RBC_ApptType

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AT_RowId | bigint | PK |  | NO | - |
| AT_Code | varchar |  |  | NO | Code |
| AT_CreatedDate | date |  |  | SI | Created Date |
| AT_CreatedTime | time |  |  | SI | Created Time |
| AT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AT_Desc | varchar |  |  | NO | Description |
| AT_NumberOfSlots | double |  |  | SI | Number of Slots |
| AT_UpdatedDate | date |  |  | SI | Updated Date |
| AT_UpdatedTime | time |  |  | SI | Updated Time |
| AT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*