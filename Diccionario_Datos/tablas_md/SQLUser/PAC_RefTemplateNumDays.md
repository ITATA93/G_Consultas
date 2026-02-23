# SQLUser.PAC_RefTemplateNumDays

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NUMD_ParRef | bigint | PK |  | NO | PAC_RefTemplate Parent Reference |
| NUMD_Childsub | double |  |  | NO | Childsub |
| NUMD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NUMD_CreatedDate | date |  |  | SI | Created Date |
| NUMD_CreatedTime | time |  |  | SI | Created Time |
| NUMD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NUMD_NumberOfDays | double |  |  | SI | NumberOfDays |
| NUMD_RowId | varchar |  |  | NO | - |
| NUMD_State_DR | bigint |  | FK | SI | Des Ref Sate |
| NUMD_UpdatedDate | date |  |  | SI | Updated Date |
| NUMD_UpdatedTime | time |  |  | SI | Updated Time |
| NUMD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q5Q1 | - |  |  | SI | Insertion date |
| Q5Q2 | - |  |  | SI | Surgeon |
| Q5Q3 | - |  |  | SI | Type of catheter |
| Q5Q4 | - |  |  | SI | Complication |
| Q5Q5 | - |  |  | SI | Addtional details |
| Q5Q6 | - |  |  | SI | Removal date |
| Q5Q7 | - |  |  | SI | Reason for removal |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*