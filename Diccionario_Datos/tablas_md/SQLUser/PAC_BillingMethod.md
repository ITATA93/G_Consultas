# SQLUser.PAC_BillingMethod

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLM_RowId | bigint | PK |  | NO | - |
| BLM_Code | varchar |  |  | NO | Code |
| BLM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLM_CreatedDate | date |  |  | SI | Created Date |
| BLM_CreatedTime | time |  |  | SI | Created Time |
| BLM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLM_DateFrom | date |  |  | SI | Date From |
| BLM_DateTo | date |  |  | SI | Date To |
| BLM_Desc | varchar |  |  | NO | Description |
| BLM_NationalCode | varchar |  |  | SI | National Code |
| BLM_Owner | varchar |  |  | SI | Owner |
| BLM_UpdatedDate | date |  |  | SI | Updated Date |
| BLM_UpdatedTime | time |  |  | SI | Updated Time |
| BLM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Completion of this screening tool is recommended i... |
| Q02 | - |  |  | SI | NOTE: If the patient is non-English speaking this ... |
| Q03 | - |  |  | SI | Name of family member who helped gather informatio... |
| Q04 | - |  |  | SI | Relationship |
| Q05 | - |  |  | SI | Patient is able to get other people's attention, i... |
| Q06 | - |  |  | SI | Patient is able to inform me of what happened to b... |
| Q07 | - |  |  | SI | Patient is able to understand their medical condit... |
| Q08 | - |  |  | SI | Patient is able to understand the implications of ... |
| Q09 | - |  |  | SI | Patient is able to follow instructions e.g. “lean ... |
| Q10 | - |  |  | SI | Patient is able to express their feelings |
| Q11 | - |  |  | SI | Patient is able to provide information about their... |
| Q12 | - |  |  | SI | Patient is able to understand and remember informa... |
| Q13 | - |  |  | SI | Patient is able to  ask questions about their care |
| Q14 | - |  |  | SI | Patient is able to inform me about any medical con... |
| Q15 | - |  |  | SI | Patient is able to inform me of any pain or discom... |
| Q16 | - |  |  | SI | Patient is able to inform me of what they do or do... |
| Q17 | - |  |  | SI | Patient is able to call a nurse if they need to |
| Q18 | - |  |  | SI | Patient is able to speak without slurring their sp... |
| Q19 | - |  |  | SI | Any score of 1 or above : Please contact the speec... |
| Q20 | - |  |  | SI | Relationship |
| Q21 | - |  |  | SI | The Inpatient Functional Communication Inventory f... |
| Q22 | - |  |  | SI | Score = 0 : No speech pathologist follow-up requir... |
| Q23 | - |  |  | SI | Instructions |
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