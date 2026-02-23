# SQLUser.ARC_ItemCatQuestion

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUES_ParRef | bigint | PK |  | NO | ARC_ItemCat Parent Reference |
| Q01 | - |  |  | SI | Date of Recording |
| Q02 | - |  |  | SI | Date of Analysis |
| Q03 | - |  |  | SI | ECG performed by |
| Q04 | - |  |  | SI | Cardiac Clinical Physiologist Report |
| Q05 | - |  |  | SI | Heart rate |
| Q06 | - |  |  | SI | Rhythm |
| Q07 | - |  |  | SI | QRS axis |
| Q08 | - |  |  | SI | PR interval |
| Q09 | - |  |  | SI | QRS duration |
| Q10 | - |  |  | SI | QTc |
| Q11 | - |  |  | SI | Evidence of LVH |
| Q12 | - |  |  | SI | ST segment |
| Q13 | - |  |  | SI | T wave abnormalities |
| Q14 | - |  |  | SI | Other significant findings |
| Q15 | - |  |  | SI | Conclusion |
| Q16 | - |  |  | SI | Reported by |
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
| QUES_ClinicalDetails | varchar |  |  | SI | ClinicalDetails |
| QUES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUES_CreatedDate | date |  |  | SI | Created Date |
| QUES_CreatedTime | time |  |  | SI | Created Time |
| QUES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUES_DateFrom | date |  |  | SI | Date From |
| QUES_DateTo | date |  |  | SI | Date To |
| QUES_ForSpecCollection | varchar |  |  | SI | ForSpecimenCollection  |
| QUES_Mandatory | varchar |  |  | SI | Mandatory |
| QUES_Owner | varchar |  |  | SI | Owner - DEPRECATED - Code Table Overrides |
| QUES_Question_DR | bigint |  | FK | SI | Des Ref Question |
| QUES_RowId | varchar |  |  | NO | - |
| QUES_UpdatedDate | date |  |  | SI | Updated Date |
| QUES_UpdatedTime | time |  |  | SI | Updated Time |
| QUES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*