# SQLUser.PAC_Phototherapy

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHOTO_Code | varchar | PK |  | NO | Code |
| PHOTO_CodeTableTags | varchar | PK |  | SI | List of code table Tags |
| PHOTO_CreatedDate | date | PK |  | SI | Created Date |
| PHOTO_CreatedTime | time | PK |  | SI | Created Time |
| PHOTO_CreatedUser_DR | bigint | PK | FK | SI | Created User |
| PHOTO_Desc | varchar | PK |  | NO | Description |
| PHOTO_Owner | varchar | PK |  | SI | Owner |
| PHOTO_RowId | bigint | PK |  | NO | - |
| PHOTO_UpdatedDate | date | PK |  | SI | Updated Date |
| PHOTO_UpdatedTime | time | PK |  | SI | Updated Time |
| PHOTO_UpdatedUser_DR | bigint | PK | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*