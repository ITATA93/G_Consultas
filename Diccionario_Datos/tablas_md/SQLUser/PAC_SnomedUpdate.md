# SQLUser.PAC_SnomedUpdate

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOUPD_RowId | bigint | PK |  | NO | - |
| ChildQ22DR | - |  |  | SI | Child Reference: Muscle lenght |
| Q19Q1 | - |  |  | SI | Body location |
| Q19Q2 | - |  |  | SI | Range of movement: passive |
| Q19Q3 | - |  |  | SI | Altered passive ROM: degrees |
| Q19Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNOUPD_Code | varchar |  |  | NO | Distribution Package |
| SNOUPD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SNOUPD_CreatedDate | date |  |  | SI | Created Date |
| SNOUPD_CreatedTime | time |  |  | SI | Created Time |
| SNOUPD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOUPD_Desc | date |  |  | NO | Release Date |
| SNOUPD_Owner | varchar |  |  | SI | Owner |
| SNOUPD_UpdatedDate | date |  |  | SI | Updated Date |
| SNOUPD_UpdatedTime | time |  |  | SI | Updated Time |
| SNOUPD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SNOUPD_UploadDate | date |  |  | SI | Upload Date |
| SNOUPD_UploadTime | time |  |  | SI | Upload Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*