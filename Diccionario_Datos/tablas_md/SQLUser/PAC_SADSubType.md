# SQLUser.PAC_SADSubType

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SADST_ParRef | bigint | PK |  | NO | PAC_DocumentType Parent Reference |
| ChildQ13DR | - |  |  | SI | Child Reference: Walking recovery |
| Q11Q1 | - |  |  | SI | Micro goal |
| Q11Q2 | - |  |  | SI | Timing |
| Q11Q3 | - |  |  | SI | Outcome |
| Q11Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SADST_Childsub | double |  |  | NO | Childsub |
| SADST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SADST_CreatedDate | date |  |  | SI | Created Date |
| SADST_CreatedTime | time |  |  | SI | Created Time |
| SADST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SADST_RowId | varchar |  |  | NO | - |
| SADST_ScanAdmDocSubType_DR | bigint |  | FK | SI | Des Ref ScanAdmDocSubType |
| SADST_UpdatedDate | date |  |  | SI | Updated Date |
| SADST_UpdatedTime | time |  |  | SI | Updated Time |
| SADST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*