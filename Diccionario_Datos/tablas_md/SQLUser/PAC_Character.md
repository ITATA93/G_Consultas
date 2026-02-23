# SQLUser.PAC_Character

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CHAR_RowId | bigint | PK |  | NO | - |
| CHAR_Code | varchar |  |  | NO | Code |
| CHAR_CreatedDate | date |  |  | SI | Created Date |
| CHAR_CreatedTime | time |  |  | SI | Created Time |
| CHAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CHAR_Desc | varchar |  |  | NO | Description |
| CHAR_UpdatedDate | date |  |  | SI | Updated Date |
| CHAR_UpdatedTime | time |  |  | SI | Updated Time |
| CHAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q24Q1 | - |  |  | SI | Type of balloon |
| Q24Q2 | - |  |  | SI | Balloon size (mm) |
| Q24Q3 | - |  |  | SI | Balloon length (mm) |
| Q24Q4 | - |  |  | SI | Balloon inflation time (min/sec) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*