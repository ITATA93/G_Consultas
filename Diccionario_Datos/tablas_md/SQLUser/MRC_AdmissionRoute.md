# SQLUser.MRC_AdmissionRoute

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMR_RowId | bigint | PK |  | NO | - |
| ADMR_Code | varchar |  |  | NO | Code |
| ADMR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMR_CreatedDate | date |  |  | SI | Created Date |
| ADMR_CreatedTime | time |  |  | SI | Created Time |
| ADMR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMR_Desc | varchar |  |  | NO | Description |
| ADMR_Owner | varchar |  |  | SI | Owner |
| ADMR_UpdatedDate | date |  |  | SI | Updated Date |
| ADMR_UpdatedTime | time |  |  | SI | Updated Time |
| ADMR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ99DR | - |  |  | SI | Child Reference: Abdomen |
| Q93Q1 | - |  |  | SI | Ritmo |
| Q93Q2 | - |  |  | SI | Ruidos |
| Q93Q3 | - |  |  | SI | Soplos |
| Q93Q4 | - |  |  | SI | Grado (soplo) |
| Q93Q5 | - |  |  | SI | Ubicación |
| Q93Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*