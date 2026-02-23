# SQLUser.ORC_BladeType

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLDTP_RowId | bigint | PK |  | NO | - |
| BLDTP_Code | varchar |  |  | NO | Blade Type Code |
| BLDTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLDTP_CreatedDate | date |  |  | SI | Created Date |
| BLDTP_CreatedTime | time |  |  | SI | Created Time |
| BLDTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLDTP_DateFrom | date |  |  | SI | Date From |
| BLDTP_DateTo | date |  |  | SI | Date To |
| BLDTP_Desc | varchar |  |  | NO | Blade Description |
| BLDTP_Owner | varchar |  |  | SI | Owner |
| BLDTP_UpdatedDate | date |  |  | SI | Updated Date |
| BLDTP_UpdatedTime | time |  |  | SI | Updated Time |
| BLDTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Has a diagnosis recorded |
| Q02 | - |  |  | SI | Diagnosis type |
| Q03 | - |  |  | SI | Has allergy recorded (includes nil known) - patien... |
| Q04 | - |  |  | SI | Has patient alert recorded |
| Q05 | - |  |  | SI | Has a problem recorded |
| Q06 | - |  |  | SI | Has a family history recorded |
| Q07 | - |  |  | SI | Has a current condition recorded |
| Q08 | - |  |  | SI | Has a past condition recorded |
| Q09 | - |  |  | SI | Has a medication history recorded |
| Q10 | - |  |  | SI | Has a surgical history recorded |
| Q11 | - |  |  | SI | Has social history recorded |
| Q12 | - |  |  | SI | Has at least one clinical note |
| Q13 | - |  |  | SI | Clinical note care provider type |
| Q14 | - |  |  | SI | Has at least one observation recorded |
| Q15 | - |  |  | SI | Observations within one hour of admission or arriv... |
| Q16 | - |  |  | SI | Has at least one active clinical note (ACN) entry |
| Q17 | - |  |  | SI | ACN Entry by care provider type |
| Q18 | - |  |  | SI | Has at least one order placed |
| Q19 | - |  |  | SI | Orders by category |
| Q20 | - |  |  | SI | Orders by care provider |
| Q21 | - |  |  | SI | Order alerts overriden (excluding duplication) |
| Q22 | - |  |  | SI | Duplication alerts overriden |
| Q23 | - |  |  | SI | Order alerts by severity |
| Q24 | - |  |  | SI | Has scanned document attached |
| Q25 | - |  |  | SI | Fall risk assessment completed |
| Q26 | - |  |  | SI | VTE risk assessment completed |
| Q27 | - |  |  | SI | Nutrition screening assessment completed |
| Q28 | - |  |  | SI | Patient safety incident completed |
| Q29 | - |  |  | SI | Patient safety incident type |
| Q30 | - |  |  | SI | Pain assessment completed |
| Q31 | - |  |  | SI | Braden assessment completed (Adults) |
| Q32 | - |  |  | SI | Braden assessment completed (Child) |
| Q33 | - |  |  | SI | Braden severity |
| Q34 | - |  |  | SI | Waterlow assessment completed |
| Q35 | - |  |  | SI | Waterlow assessment severity |
| Q36 | - |  |  | SI | Central line bundle checklist completed |
| Q37 | - |  |  | SI | Catheter insertion bundle checklist completed |
| Q38 | - |  |  | SI | Ventilator acquired pneumonia checklist completed |
| Q39 | - |  |  | SI | Other bundle |
| Q40 | - |  |  | SI | Review of systems completed |
| Q41 | - |  |  | SI | Physical exam completed |
| Q42 | - |  |  | SI | Clinical pathway initiated	 |
| Q43 | - |  |  | SI | Nursing care plans initiated |
| Q44 | - |  |  | SI | Discharge summary  completed |
| Q45 | - |  |  | SI | Handover completed(at least one) |
| Q46 | - |  |  | SI | The Benefits realisation questionnaire is created ... |
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