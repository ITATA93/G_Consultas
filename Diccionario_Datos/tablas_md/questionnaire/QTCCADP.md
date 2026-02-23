# questionnaire.QTCCADP

> Care After Death Pathway

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Care After Death Pathway

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Persons present at time of death |
| Q02 | varchar |  |  | SI | Relative or carer present at time of death |
| Q03 | varchar |  |  | SI | Have the relative or carer been notified? |
| Q04 | varchar |  |  | SI | Name of person informed |
| Q05 | varchar |  |  | SI | Relationship to the patient |
| Q06 | varchar |  |  | SI | Comments |
| Q07 | numeric |  |  | SI | Contact number for person informed |
| Q08 | varchar |  |  | SI | Is the coroner likely to be involved? |
| Q09 | varchar |  |  | SI | Last offices are undertaken according to policy an... |
| Q10 | varchar |  |  | SI | Comment |
| Q11 | varchar |  |  | SI | The patient is treated with respect and dignity wh... |
| Q12 | varchar |  |  | SI | Comment |
| Q13 | varchar |  |  | SI | Universal precautions & local policy and procedure... |
| Q14 | varchar |  |  | SI | Comment |
| Q15 | varchar |  |  | SI | Spiritual, religious, cultural rituals, needs met. |
| Q16 | varchar |  |  | SI | Comment |
| Q17 | varchar |  |  | SI | Organisational policy followed for the management ... |
| Q18 | varchar |  |  | SI | Comment |
| Q19 | varchar |  |  | SI | Organisational policy followed for the management ... |
| Q20 | varchar |  |  | SI | Comment |
| Q21 | varchar |  |  | SI | Ensure the relative or carer can express an unders... |
| Q22 | varchar |  |  | SI | Conversation with relative or carer explaining the... |
| Q23 | varchar |  |  | SI | Comment |
| Q24 | varchar |  |  | SI | Grievance leaflet given to relative or carer |
| Q25 | varchar |  |  | SI | Comment |
| Q26 | varchar |  |  | SI | Appropriate documentation given to relative or car... |
| Q27 | varchar |  |  | SI | Comment |
| Q28 | varchar |  |  | SI | Information given regarding how and when to contac... |
| Q29 | varchar |  |  | SI | Comment |
| Q30 | varchar |  |  | SI | Where appropriate, wishes regarding tissue / organ... |
| Q31 | varchar |  |  | SI | Comment |
| Q32 | varchar |  |  | SI | Discuss as appropriate: viewing the body / the nee... |
| Q33 | varchar |  |  | SI | Comment |
| Q34 | varchar |  |  | SI | Information given to families on child bereavement... |
| Q35 | varchar |  |  | SI | Comment |
| Q36 | varchar |  |  | SI | Ensure the primary health care team/GP are notifie... |
| Q37 | varchar |  |  | SI | Comment	 |
| Q38 | varchar |  |  | SI | Primary health care team/GP notified of patients d... |
| Q39 | varchar |  |  | SI | Comment |
| Q40 | varchar |  |  | SI | Document Variance |
| Q41 | varchar |  |  | SI | Ensure the patient's death communicated to appropr... |
| Q42 | varchar |  |  | SI | e.g Bereavement office / general office / palliati... |
| Q43 | varchar |  |  | SI | Comment |
| Q44 | varchar |  |  | SI | Relevant services notified of patients death? |
| Q45 | varchar |  |  | SI | Comment |
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