# SQLUser.RBC_LeafletType

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LFT_RowId | bigint | PK |  | NO | - |
| LFT_Code | varchar |  |  | NO | Code |
| LFT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LFT_CreatedDate | date |  |  | SI | Created Date |
| LFT_CreatedTime | time |  |  | SI | Created Time |
| LFT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LFT_DateFrom | date |  |  | SI | Date From |
| LFT_DateTo | date |  |  | SI | Date To |
| LFT_Desc | varchar |  |  | NO | Description |
| LFT_Owner | varchar |  |  | SI | Owner |
| LFT_UpdatedDate | date |  |  | SI | Updated Date |
| LFT_UpdatedTime | time |  |  | SI | Updated Time |
| LFT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*