# SQLUser.NRC_Issues

**Schema:** SQLUser
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ISSUE_RowId | bigint | PK |  | NO | - |
| ChildQ84DR | - |  |  | SI | Child Reference: PA Catheter Check |
| ISSUE_AssessQuestionnaire | varchar |  |  | SI | AssessmentQuestionnaire |
| ISSUE_Code | varchar |  |  | SI | Code |
| ISSUE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ISSUE_CreatedDate | date |  |  | SI | Created Date |
| ISSUE_CreatedTime | time |  |  | SI | Created Time |
| ISSUE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ISSUE_DateFrom | date |  |  | SI | Date From |
| ISSUE_DateTo | date |  |  | SI | Date To |
| ISSUE_Desc | varchar |  |  | SI | Description |
| ISSUE_ObsGrp_DR | bigint |  | FK | SI | Observation Group |
| ISSUE_OrdSet_DR | varchar |  | FK | SI | Order Set |
| ISSUE_Owner | varchar |  |  | SI | Owner |
| ISSUE_UpdatedDate | date |  |  | SI | Updated Date |
| ISSUE_UpdatedTime | time |  |  | SI | Updated Time |
| ISSUE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ISSUE_Url1_DR | varchar |  | FK | SI | URL 1 |
| ISSUE_Url2_DR | varchar |  | FK | SI | URL 2 |
| ISSUE_Url3_DR | varchar |  | FK | SI | URL 3 |
| ISSUE_Url4_DR | varchar |  | FK | SI | URL 4 |
| ISSUE_Url5_DR | varchar |  | FK | SI | URL 5 |
| ISSUE_UserDefWindow_DR | bigint |  | FK | SI | Des Ref SSUserDefWindow |
| Q55Q1 | - |  |  | SI | IV check |
| Q55Q2 | - |  |  | SI | IV access heparin locked and labeled |
| Q55Q3 | - |  |  | SI | Flush bag pressure checked |
| Q55Q4 | - |  |  | SI | Date |
| Q55Q5 | - |  |  | SI | Time |
| Q55Q6 | - |  |  | SI | Note |
| Q55Q7 | - |  |  | SI | Actions |
| Q55Q8 | - |  |  | SI | Dressing status |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*