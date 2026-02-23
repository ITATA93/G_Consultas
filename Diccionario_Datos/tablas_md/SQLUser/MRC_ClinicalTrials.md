# SQLUser.MRC_ClinicalTrials

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLTR_RowId | bigint | PK |  | NO | - |
| CLTR_Associate | varchar |  |  | SI | Clinical Research Associate |
| CLTR_Centre | varchar |  |  | SI | Clinical Trial Centre |
| CLTR_Code | varchar |  |  | NO | Code |
| CLTR_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CLTR_Coinvestigator | varchar |  |  | SI | Co-investigator [DEPRECATED] TC-217569 - Use Co-in... |
| CLTR_CoinvestigatorCareProv_DR | varchar |  | FK | SI | Co-investigator Care Provider List |
| CLTR_CreatedDate | date |  |  | SI | Created Date |
| CLTR_CreatedTime | time |  |  | SI | Created Time |
| CLTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLTR_DateFrom | date |  |  | SI | Date From |
| CLTR_DateLastAmend | date |  |  | SI | Date of last amendment |
| CLTR_DateTo | date |  |  | SI | Date To |
| CLTR_Desc | varchar |  |  | NO | Name |
| CLTR_DescLong | varchar |  |  | SI | Long Description |
| CLTR_Investigator | varchar |  |  | SI | Investigator [DEPRECATED] TC-217569 - Replaced by ... |
| CLTR_InvestigatorCareProv_DR | varchar |  | FK | SI | Investigator Care Provider |
| CLTR_Owner | varchar |  |  | SI | Code Table Owner |
| CLTR_PromCode | varchar |  |  | SI | Promoter Code |
| CLTR_Promoter | varchar |  |  | SI | Promoter |
| CLTR_UpdatedDate | date |  |  | SI | Updated Date |
| CLTR_UpdatedTime | time |  |  | SI | Updated Time |
| CLTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ173DR | - |  |  | SI | Child Reference: Evaluación de Pies |
| Q172Q1 | - |  |  | SI | Lesión |
| Q172Q2 | - |  |  | SI | Lateralidad |
| Q172Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*