# SQLUser.PAC_NonGovOrg

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NGO_RowId | bigint | PK |  | NO | - |
| NGO_Address | varchar |  |  | SI | Address |
| NGO_City_DR | bigint |  | FK | SI | Des Ref City |
| NGO_Code | varchar |  |  | NO | Code |
| NGO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NGO_ContactMethod | varchar |  |  | SI | Contact Method |
| NGO_CreatedDate | date |  |  | SI | Created Date |
| NGO_CreatedTime | time |  |  | SI | Created Time |
| NGO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NGO_DateFrom | date |  |  | SI | DateFrom |
| NGO_DateTo | date |  |  | SI | DateTo |
| NGO_Desc | varchar |  |  | NO | Description |
| NGO_Email | varchar |  |  | SI | Email |
| NGO_Fax | varchar |  |  | SI | Fax |
| NGO_Owner | varchar |  |  | SI | Owner |
| NGO_PathologyProvider | varchar |  |  | SI | Pathology Provider |
| NGO_Phone | varchar |  |  | SI | Phone |
| NGO_Province_DR | bigint |  | FK | SI | Des Ref Province |
| NGO_School | varchar |  |  | SI | School |
| NGO_UpdatedDate | date |  |  | SI | Updated Date |
| NGO_UpdatedTime | time |  |  | SI | Updated Time |
| NGO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| NGO_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| Q01 | - |  |  | SI | Global Abduction |
| Q02 | - |  |  | SI | Global External Rotation |
| Q03 | - |  |  | SI | Hand to Neck |
| Q04 | - |  |  | SI | Hand to Spine |
| Q05 | - |  |  | SI | Hand to Mouth |
| Q06 | - |  |  | SI | Internal Rotation |
| Q07 | - |  |  | SI | The Mallet grading system is a commonly used funct... |
| Q08 | - |  |  | SI | Not Testable |
| Q09 | - |  |  | SI | Grade I |
| Q10 | - |  |  | SI | Grade II |
| Q11 | - |  |  | SI | Grade III |
| Q12 | - |  |  | SI | Grade IV |
| Q13 | - |  |  | SI | Grade V |
| Q14 | - |  |  | SI | Global Abduction Score |
| Q14G | - |  |  | SI | Global Abduction Grade |
| Q15 | - |  |  | SI | Global External Rotation Score |
| Q15G | - |  |  | SI | Global External Rotation Grade |
| Q16 | - |  |  | SI | Hand to Neck Score |
| Q16G | - |  |  | SI | Hand to Neck Grade |
| Q17 | - |  |  | SI | Hand to Spine Score |
| Q17G | - |  |  | SI | Hand to Spine Grade |
| Q18 | - |  |  | SI | Hand to Mouth Score |
| Q18G | - |  |  | SI | Hand to Mouth Grade |
| Q19 | - |  |  | SI | Internal Rotation Score |
| Q19G | - |  |  | SI | Internal Rotation Grade |
| Q20 | - |  |  | SI | Please refer to legend for grading |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*