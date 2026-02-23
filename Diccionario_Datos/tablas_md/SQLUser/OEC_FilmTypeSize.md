# SQLUser.OEC_FilmTypeSize

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FTS_RowId | bigint | PK |  | NO | - |
| FTS_Code | varchar |  |  | NO | Code |
| FTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FTS_CreatedDate | date |  |  | SI | Created Date |
| FTS_CreatedTime | time |  |  | SI | Created Time |
| FTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FTS_Desc | varchar |  |  | NO | Description |
| FTS_Owner | varchar |  |  | SI | Owner |
| FTS_UpdatedDate | date |  |  | SI | Updated Date |
| FTS_UpdatedTime | time |  |  | SI | Updated Time |
| FTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q204Q1 | - |  |  | SI | Method |
| Q204Q10 | - |  |  | SI | Distance |
| Q204Q2 | - |  |  | SI | Glasses |
| Q204Q3 | - |  |  | SI | Phoria / Tropia |
| Q204Q4 | - |  |  | SI | Laterality |
| Q204Q5 | - |  |  | SI | Prism dioptres |
| Q204Q6 | - |  |  | SI | Degrees |
| Q204Q7 | - |  |  | SI | Distance measurement |
| Q204Q8 | - |  |  | SI | Measurement unit |
| Q204Q9 | - |  |  | SI | Distance |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*