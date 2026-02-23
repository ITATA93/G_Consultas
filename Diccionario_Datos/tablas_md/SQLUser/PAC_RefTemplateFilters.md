# SQLUser.PAC_RefTemplateFilters

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FILT_ParRef | bigint | PK |  | NO | PAC_RefTemplate Parent Reference |
| ChildQ5DR | - |  |  | SI | Child Reference: Pd catheter |
| FILT_Childsub | double |  |  | NO | Childsub |
| FILT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FILT_ConsultPriority_DR | bigint |  | FK | SI | Des Ref PACWaitingListPriority |
| FILT_CreatedDate | date |  |  | SI | Created Date |
| FILT_CreatedTime | time |  |  | SI | Created Time |
| FILT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FILT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| FILT_Number | varchar |  |  | SI | Number of Parameters |
| FILT_Parameters | varchar |  |  | SI | String of Parameters |
| FILT_Procedures_DR | bigint |  | FK | SI | Des Ref StatePPP |
| FILT_RowId | varchar |  |  | NO | - |
| FILT_Service_DR | varchar |  | FK | SI | Des Ref ARCIM |
| FILT_Speciality_DR | bigint |  | FK | SI | Des Ref CTLoc |
| FILT_UpdatedDate | date |  |  | SI | Updated Date |
| FILT_UpdatedTime | time |  |  | SI | Updated Time |
| FILT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q14Q1 | - |  |  | SI | Date |
| Q14Q2 | - |  |  | SI | Note |
| Q14Q3 | - |  |  | SI | Care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*