# SQLUser.MRC_DRGCodingICD

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICD_ParRef | bigint | PK |  | NO | MRC_DRGCoding Parent Reference |
| ChildQ69DR | - |  |  | SI | Child Reference: Pulsos periféricos |
| ICD_Childsub | double |  |  | NO | Childsub |
| ICD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ICD_CreatedDate | date |  |  | SI | Created Date |
| ICD_CreatedTime | time |  |  | SI | Created Time |
| ICD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ICD_ICD_DR | bigint |  | FK | SI | Des Ref ICD |
| ICD_RowId | varchar |  |  | NO | - |
| ICD_UpdatedDate | date |  |  | SI | Updated Date |
| ICD_UpdatedTime | time |  |  | SI | Updated Time |
| ICD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q65Q1 | - |  |  | SI | Hallazgos |
| Q65Q2 | - |  |  | SI | Extremidad superior |
| Q65Q3 | - |  |  | SI | Extremidad inferior |
| Q65Q4 | - |  |  | SI | Topografía |
| Q65Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*