# SQLUser.INC_StockOutType

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STOUT_RowId | bigint | PK |  | NO | - |
| Q25Q1 | - |  |  | SI | Motivos |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| STOUT_Code | varchar |  |  | NO | Code |
| STOUT_CreatedDate | date |  |  | SI | Created Date |
| STOUT_CreatedTime | time |  |  | SI | Created Time |
| STOUT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STOUT_Desc | varchar |  |  | NO | description |
| STOUT_UpdatedDate | date |  |  | SI | Updated Date |
| STOUT_UpdatedTime | time |  |  | SI | Updated Time |
| STOUT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*