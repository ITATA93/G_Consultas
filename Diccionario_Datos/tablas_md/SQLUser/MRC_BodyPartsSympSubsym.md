# SQLUser.MRC_BodyPartsSympSubsym

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBS_ParRef | varchar | PK |  | NO | MRC_BodyPartsSymptoms Parent Reference |
| Q79Q1 | - |  |  | SI | Hallazgos |
| Q79Q2 | - |  |  | SI | Ubicación |
| Q79Q3 | - |  |  | SI | Lateralidad |
| Q79Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUBS_Childsub | double |  |  | NO | Childsub |
| SUBS_Code | varchar |  |  | NO | Code |
| SUBS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUBS_CreatedDate | date |  |  | SI | Created Date |
| SUBS_CreatedTime | time |  |  | SI | Created Time |
| SUBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBS_Desc | varchar |  |  | NO | Description |
| SUBS_RowId | varchar |  |  | NO | - |
| SUBS_UpdatedDate | date |  |  | SI | Updated Date |
| SUBS_UpdatedTime | time |  |  | SI | Updated Time |
| SUBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*