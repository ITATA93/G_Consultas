# SQLUser.PAC_SnomedExcludedWords

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOEW_RowId | bigint | PK |  | NO | - |
| Q06Q1 | - |  |  | SI | Medication |
| Q06Q2 | - |  |  | SI | Strength |
| Q06Q3 | - |  |  | SI | Quantity |
| Q06Q4 | - |  |  | SI | Storage location |
| Q06Q5 | - |  |  | SI | Other storage location |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNOEW_CreatedDate | date |  |  | SI | Created Date |
| SNOEW_CreatedTime | time |  |  | SI | Created Time |
| SNOEW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOEW_Keyword | varchar |  |  | SI | Keyword |
| SNOEW_Language_DR | bigint |  | FK | SI | Des Ref SSLanguage |
| SNOEW_UpdatedDate | date |  |  | SI | Updated Date |
| SNOEW_UpdatedTime | time |  |  | SI | Updated Time |
| SNOEW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*