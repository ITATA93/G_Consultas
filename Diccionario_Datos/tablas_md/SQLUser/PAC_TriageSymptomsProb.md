# SQLUser.PAC_TriageSymptomsProb

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROB_ParRef | bigint | PK |  | NO | PAC_TriageSymptoms Parent Reference |
| PROB_Acuity_DR | bigint |  | FK | SI | Des Ref Acuity |
| PROB_CTLOC_DR | bigint |  | FK | SI | Location |
| PROB_Childsub | double |  |  | NO | Childsub |
| PROB_Code | varchar |  |  | SI | Code |
| PROB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROB_CreatedDate | date |  |  | SI | Created Date |
| PROB_CreatedTime | time |  |  | SI | Created Time |
| PROB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROB_DateFrom | date |  |  | SI | Date From |
| PROB_DateTo | date |  |  | SI | Date To |
| PROB_Desc | varchar |  |  | SI | Description |
| PROB_NationalCode | varchar |  |  | SI | National Code |
| PROB_ProblemDetails | varchar |  |  | SI | Triage Symptom Problem Details |
| PROB_RowId | varchar |  |  | NO | - |
| PROB_UpdatedDate | date |  |  | SI | Updated Date |
| PROB_UpdatedTime | time |  |  | SI | Updated Time |
| PROB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q88Q1 | - |  |  | SI | Test dose volume (mLs) |
| Q88Q2 | - |  |  | SI | Time |
| Q88Q3 | - |  |  | SI | Test dose anaesthetic |
| Q88Q4 | - |  |  | SI | Other (please specify) |
| Q88Q5 | - |  |  | SI | Concentration (%) |
| Q88Q6 | - |  |  | SI | Vasoconstrictor added |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*