# SQLUser.OEC_ConsultCategQuestion

**Schema:** SQLUser
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUES_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| Q01 | - |  |  | SI | Pallor |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Pallor DR |
| Q02 | - |  |  | SI | Cyanosis |
| Q02N | - |  |  | SI | Note |
| Q02ObsDR | - |  |  | SI | Cyanosis DR |
| Q03 | - |  |  | SI | Jaundice |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Jaundice DR |
| Q04 | - |  |  | SI | Dehydration |
| Q04N | - |  |  | SI | Note |
| Q04ObsDR | - |  |  | SI | Dehydration DR |
| Q05 | - |  |  | SI | Erythema |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Erythema DR |
| Q06 | - |  |  | SI | Ecchymosis |
| Q06N | - |  |  | SI | Note |
| Q06ObsDR | - |  |  | SI | Ecchymosis DR |
| Q07 | - |  |  | SI | Edema |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Edema DR |
| Q08 | - |  |  | SI | Surgical scars |
| Q08N | - |  |  | SI | Note |
| Q08ObsDR | - |  |  | SI | Surgical scars DR |
| Q09 | - |  |  | SI | Injury treatment |
| Q09D | - |  |  | SI | Dressing |
| Q09L | - |  |  | SI | Localisation |
| Q09ObsDR | - |  |  | SI | Injury treatment DR |
| Q10 | - |  |  | SI | Burns |
| Q10G | - |  |  | SI | Burns degree |
| Q10GObsDR | - |  |  | SI | Burns degree DR |
| Q10L | - |  |  | SI | Note / Localisation |
| Q10ObsDR | - |  |  | SI | Burns DR |
| Q22SkinAppendages | - |  |  | SI | Other |
| Q24 | - |  |  | SI | Ingestion of food |
| Q24ObsDR | - |  |  | SI | Ingestion of food DR |
| Q25 | - |  |  | SI | Difficulty in chewing |
| Q25ObsDR | - |  |  | SI | Difficulty in chewing DR |
| Q26 | - |  |  | SI | Meals per day |
| Q26ObsDR | - |  |  | SI | Meals per day DR |
| Q27 | - |  |  | SI | Liquid volume |
| Q27ObsDR | - |  |  | SI | Liquid volume DR |
| Q28 | - |  |  | SI | Nutrition |
| Q28ObsDR | - |  |  | SI | Nutrition DR |
| Q29 | - |  |  | SI | Appetite |
| Q29ObsDR | - |  |  | SI | Appetite DR |
| Q30 | - |  |  | SI | Dysphagia solids |
| Q30ObsDR | - |  |  | SI | Dysphagia solids DR |
| Q31 | - |  |  | SI | Dysphagia liquids |
| Q31ObsDR | - |  |  | SI | Dysphagia liquids DR |
| Q32 | - |  |  | SI | Enteral Nutrition (EN) |
| Q32N | - |  |  | SI | Note |
| Q32ObsDR | - |  |  | SI | Enteral Nutrition (EN) DR |
| Q34 | - |  |  | SI | Parenteral nutrition (PN) |
| Q34N | - |  |  | SI | Note |
| Q34ObsDR | - |  |  | SI | Parenteral nutrition (PN) DR |
| Q36 | - |  |  | SI | Dental prosthetics |
| Q36N | - |  |  | SI | Note |
| Q36ObsDR | - |  |  | SI | Dental prosthetics DR |
| Q38 | - |  |  | SI | Nutritional status |
| Q38N | - |  |  | SI | Note |
| Q38ObsDR | - |  |  | SI | Nutritional status DR |
| Q40 | - |  |  | SI | Weight trend |
| Q40ObsDR | - |  |  | SI | Weight trend DR |
| Q41 | - |  |  | SI | Weight difference in kg |
| Q41ObsDR | - |  |  | SI | Weight difference in kg DR |
| Q42 | - |  |  | SI | Weight difference in days |
| Q42N | - |  |  | SI | Note |
| Q44 | - |  |  | SI | Height cm |
| Q44ObsDR | - |  |  | SI | Height cm DR |
| Q45 | - |  |  | SI | Weight kg |
| Q45ObsDR | - |  |  | SI | Weight kg DR |
| Q46 | - |  |  | SI | BMI |
| Q46N | - |  |  | SI | Note |
| Q48 | - |  |  | SI | Skin turgor |
| Q48N | - |  |  | SI | Note |
| Q48ObsDR | - |  |  | SI | Skin turgor DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| QUES_Childsub | double |  |  | NO | Childsub |
| QUES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUES_CreatedDate | date |  |  | SI | Created Date |
| QUES_CreatedTime | time |  |  | SI | Created Time |
| QUES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUES_PrimaryQuestionnaire | varchar |  |  | SI | PrimaryQuestionnaire |
| QUES_RowId | varchar |  |  | NO | - |
| QUES_UpdatedDate | date |  |  | SI | Updated Date |
| QUES_UpdatedTime | time |  |  | SI | Updated Time |
| QUES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QUES_UserDefWindow_DR | bigint |  | FK | SI | Des Ref UserDefWindow |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*