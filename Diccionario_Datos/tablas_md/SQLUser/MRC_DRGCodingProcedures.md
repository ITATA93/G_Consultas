# SQLUser.MRC_DRGCodingProcedures

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROC_ParRef | bigint | PK |  | NO | MRC_DRGCoding Parent Reference |
| PROC_Childsub | double |  |  | NO | Childsub |
| PROC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROC_CreatedDate | date |  |  | SI | Created Date |
| PROC_CreatedTime | time |  |  | SI | Created Time |
| PROC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROC_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| PROC_RowId | varchar |  |  | NO | - |
| PROC_UpdatedDate | date |  |  | SI | Updated Date |
| PROC_UpdatedTime | time |  |  | SI | Updated Time |
| PROC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q69Q1 | - |  |  | SI | Pulso |
| Q69Q2 | - |  |  | SI | Lateralidad |
| Q69Q3 | - |  |  | SI | Hallazgos |
| Q69Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*