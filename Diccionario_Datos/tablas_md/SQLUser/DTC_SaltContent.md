# SQLUser.DTC_SaltContent

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SAL_RowId | bigint | PK |  | NO | - |
| Q40Q1 | - |  |  | SI | Date |
| Q40Q2 | - |  |  | SI | Care provider |
| Q40Q3 | - |  |  | SI | Care provider status |
| Q40Q4 | - |  |  | SI | Other status |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SAL_Code | varchar |  |  | NO | Code |
| SAL_CreatedDate | date |  |  | SI | Created Date |
| SAL_CreatedTime | time |  |  | SI | Created Time |
| SAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SAL_Desc | varchar |  |  | NO | Description |
| SAL_UpdatedDate | date |  |  | SI | Updated Date |
| SAL_UpdatedTime | time |  |  | SI | Updated Time |
| SAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*