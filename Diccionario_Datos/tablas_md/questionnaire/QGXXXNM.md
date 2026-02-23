# questionnaire.QGXXXNM

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Pallor |
| Q01N | varchar | PK |  | SI | Note |
| Q01ObsDR | varchar | PK | FK | SI | Pallor DR |
| Q02 | varchar | PK |  | SI | Cyanosis |
| Q02N | varchar | PK |  | SI | Note |
| Q02ObsDR | varchar | PK | FK | SI | Cyanosis DR |
| Q03 | varchar | PK |  | SI | Jaundice |
| Q03N | varchar | PK |  | SI | Note |
| Q03ObsDR | varchar | PK | FK | SI | Jaundice DR |
| Q04 | varchar | PK |  | SI | Dehydration |
| Q04N | varchar | PK |  | SI | Note |
| Q04ObsDR | varchar | PK | FK | SI | Dehydration DR |
| Q05 | varchar | PK |  | SI | Erythema |
| Q05N | varchar | PK |  | SI | Note |
| Q05ObsDR | varchar | PK | FK | SI | Erythema DR |
| Q06 | varchar | PK |  | SI | Ecchymosis |
| Q06N | varchar | PK |  | SI | Note |
| Q06ObsDR | varchar | PK | FK | SI | Ecchymosis DR |
| Q07 | varchar | PK |  | SI | Edema |
| Q07N | varchar | PK |  | SI | Note |
| Q07ObsDR | varchar | PK | FK | SI | Edema DR |
| Q08 | varchar | PK |  | SI | Surgical scars |
| Q08N | varchar | PK |  | SI | Note |
| Q08ObsDR | varchar | PK | FK | SI | Surgical scars DR |
| Q09 | varchar | PK |  | SI | Injury treatment |
| Q09D | varchar | PK |  | SI | Dressing |
| Q09L | varchar | PK |  | SI | Localisation |
| Q09ObsDR | varchar | PK | FK | SI | Injury treatment DR |
| Q10 | varchar | PK |  | SI | Burns |
| Q10G | varchar | PK |  | SI | Burns degree |
| Q10GObsDR | varchar | PK | FK | SI | Burns degree DR |
| Q10L | varchar | PK |  | SI | Note / Localisation |
| Q10ObsDR | varchar | PK | FK | SI | Burns DR |
| Q22SkinAppendages | varchar | PK |  | SI | Other |
| Q24 | varchar | PK |  | SI | Ingestion of food |
| Q24ObsDR | varchar | PK | FK | SI | Ingestion of food DR |
| Q25 | varchar | PK |  | SI | Difficulty in chewing |
| Q25ObsDR | varchar | PK | FK | SI | Difficulty in chewing DR |
| Q26 | varchar | PK |  | SI | Meals per day |
| Q26ObsDR | varchar | PK | FK | SI | Meals per day DR |
| Q27 | varchar | PK |  | SI | Liquide volumn |
| Q27ObsDR | varchar | PK | FK | SI | Liquide volumn DR |
| Q28 | varchar | PK |  | SI | Nutrition |
| Q28ObsDR | varchar | PK | FK | SI | Nutrition DR |
| Q29 | varchar | PK |  | SI | Appetite |
| Q29ObsDR | varchar | PK | FK | SI | Appetite DR |
| Q30 | varchar | PK |  | SI | Dysphagia solids |
| Q30ObsDR | varchar | PK | FK | SI | Dysphagia solids DR |
| Q31 | varchar | PK |  | SI | Dysphagia liquids |
| Q31ObsDR | varchar | PK | FK | SI | Dysphagia liquids DR |
| Q32 | varchar | PK |  | SI | Enteral Nutrition (NE) |
| Q32N | varchar | PK |  | SI | Note |
| Q32ObsDR | varchar | PK | FK | SI | Enteral Nutrition (NE) DR |
| Q34 | varchar | PK |  | SI | Parenteral nutrition (TPN) |
| Q34N | varchar | PK |  | SI | Note |
| Q34ObsDR | varchar | PK | FK | SI | Parenteral nutrition (TPN) DR |
| Q36 | varchar | PK |  | SI | Dental prosthetics |
| Q36N | varchar | PK |  | SI | Note |
| Q36ObsDR | varchar | PK | FK | SI | Dental prosthetics DR |
| Q38 | varchar | PK |  | SI | Nutritional status |
| Q38N | varchar | PK |  | SI | Note |
| Q38ObsDR | varchar | PK | FK | SI | Nutritional status DR |
| Q40 | varchar | PK |  | SI | Weight trend |
| Q40ObsDR | varchar | PK | FK | SI | Weight trend DR |
| Q41 | varchar | PK |  | SI | Weight difference in kg |
| Q41ObsDR | varchar | PK | FK | SI | Weight difference in kg DR |
| Q42 | numeric | PK |  | SI | Weight difference in days |
| Q42N | varchar | PK |  | SI | Note |
| Q44 | varchar | PK |  | SI | Height cm |
| Q44ObsDR | varchar | PK | FK | SI | Height cm DR |
| Q45 | varchar | PK |  | SI | Weight kg |
| Q45ObsDR | varchar | PK | FK | SI | Weight kg DR |
| Q46 | varchar | PK |  | SI | BMI |
| Q46N | varchar | PK |  | SI | Note |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*