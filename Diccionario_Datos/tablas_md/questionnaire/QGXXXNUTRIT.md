# questionnaire.QGXXXNUTRIT

> Nutritional Asessment

**Schema:** questionnaire
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nutritional Asessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pallor |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Pallor DR |
| Q02 | varchar |  |  | SI | Cyanosis |
| Q02N | varchar |  |  | SI | Note |
| Q02ObsDR | varchar |  | FK | SI | Cyanosis DR |
| Q03 | varchar |  |  | SI | Jaundice |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Jaundice DR |
| Q04 | varchar |  |  | SI | Dehydration |
| Q04N | varchar |  |  | SI | Note |
| Q04ObsDR | varchar |  | FK | SI | Dehydration DR |
| Q05 | varchar |  |  | SI | Erythema |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Erythema DR |
| Q06 | varchar |  |  | SI | Ecchymosis |
| Q06N | varchar |  |  | SI | Note |
| Q06ObsDR | varchar |  | FK | SI | Ecchymosis DR |
| Q07 | varchar |  |  | SI | Edema |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Edema DR |
| Q08 | varchar |  |  | SI | Surgical scars |
| Q08N | varchar |  |  | SI | Note |
| Q08ObsDR | varchar |  | FK | SI | Surgical scars DR |
| Q09 | varchar |  |  | SI | Injury treatment |
| Q09D | varchar |  |  | SI | Dressing |
| Q09L | varchar |  |  | SI | Localisation |
| Q09ObsDR | varchar |  | FK | SI | Injury treatment DR |
| Q10 | varchar |  |  | SI | Burns |
| Q10G | varchar |  |  | SI | Burns degree |
| Q10GObsDR | varchar |  | FK | SI | Burns degree DR |
| Q10L | varchar |  |  | SI | Note / Localisation |
| Q10ObsDR | varchar |  | FK | SI | Burns DR |
| Q22SkinAppendages | varchar |  |  | SI | Other |
| Q24 | varchar |  |  | SI | Ingestion of food |
| Q24ObsDR | varchar |  | FK | SI | Ingestion of food DR |
| Q25 | varchar |  |  | SI | Difficulty in chewing |
| Q25ObsDR | varchar |  | FK | SI | Difficulty in chewing DR |
| Q26 | varchar |  |  | SI | Meals per day |
| Q26ObsDR | varchar |  | FK | SI | Meals per day DR |
| Q27 | varchar |  |  | SI | Liquid volume |
| Q27ObsDR | varchar |  | FK | SI | Liquid volume DR |
| Q28 | varchar |  |  | SI | Nutrition |
| Q28ObsDR | varchar |  | FK | SI | Nutrition DR |
| Q29 | varchar |  |  | SI | Appetite |
| Q29ObsDR | varchar |  | FK | SI | Appetite DR |
| Q30 | varchar |  |  | SI | Dysphagia solids |
| Q30ObsDR | varchar |  | FK | SI | Dysphagia solids DR |
| Q31 | varchar |  |  | SI | Dysphagia liquids |
| Q31ObsDR | varchar |  | FK | SI | Dysphagia liquids DR |
| Q32 | varchar |  |  | SI | Enteral Nutrition (EN) |
| Q32N | varchar |  |  | SI | Note |
| Q32ObsDR | varchar |  | FK | SI | Enteral Nutrition (EN) DR |
| Q34 | varchar |  |  | SI | Parenteral nutrition (PN) |
| Q34N | varchar |  |  | SI | Note |
| Q34ObsDR | varchar |  | FK | SI | Parenteral nutrition (PN) DR |
| Q36 | varchar |  |  | SI | Dental prosthetics |
| Q36N | varchar |  |  | SI | Note |
| Q36ObsDR | varchar |  | FK | SI | Dental prosthetics DR |
| Q38 | varchar |  |  | SI | Nutritional status |
| Q38N | varchar |  |  | SI | Note |
| Q38ObsDR | varchar |  | FK | SI | Nutritional status DR |
| Q40 | varchar |  |  | SI | Weight trend |
| Q40ObsDR | varchar |  | FK | SI | Weight trend DR |
| Q41 | varchar |  |  | SI | Weight difference in kg |
| Q41ObsDR | varchar |  | FK | SI | Weight difference in kg DR |
| Q42 | numeric |  |  | SI | Weight difference in days |
| Q42N | varchar |  |  | SI | Note |
| Q44 | varchar |  |  | SI | Height cm |
| Q44ObsDR | varchar |  | FK | SI | Height cm DR |
| Q45 | varchar |  |  | SI | Weight kg |
| Q45ObsDR | varchar |  | FK | SI | Weight kg DR |
| Q46 | varchar |  |  | SI | BMI |
| Q46N | varchar |  |  | SI | Note |
| Q48 | varchar |  |  | SI | Skin turgor |
| Q48N | varchar |  |  | SI | Note |
| Q48ObsDR | varchar |  | FK | SI | Skin turgor DR |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*