# SQLUser.FHC_Appliances

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCA_RowId | bigint | PK |  | NO | - |
| FHCA_Code | varchar |  |  | NO | Appliances Code |
| FHCA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCA_CreatedDate | date |  |  | SI | Created Date |
| FHCA_CreatedTime | time |  |  | SI | Created Time |
| FHCA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCA_DateFrom | date |  |  | NO | Date From |
| FHCA_DateTo | date |  |  | SI | Date To |
| FHCA_Desc | varchar |  |  | NO | Appliances Description |
| FHCA_NationalCode | varchar |  |  | SI | National Code |
| FHCA_Owner | varchar |  |  | SI | Owner |
| FHCA_UpdatedDate | date |  |  | SI | Updated Date |
| FHCA_UpdatedTime | time |  |  | SI | Updated Time |
| FHCA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Persons present at time of death |
| Q02 | - |  |  | SI | Relative or carer present at time of death |
| Q03 | - |  |  | SI | Have the relative or carer been notified? |
| Q04 | - |  |  | SI | Name of person informed |
| Q05 | - |  |  | SI | Relationship to the patient |
| Q06 | - |  |  | SI | Comments |
| Q07 | - |  |  | SI | Contact number for person informed |
| Q08 | - |  |  | SI | Is the coroner likely to be involved? |
| Q09 | - |  |  | SI | Last offices are undertaken according to policy an... |
| Q10 | - |  |  | SI | Comment |
| Q11 | - |  |  | SI | The patient is treated with respect and dignity wh... |
| Q12 | - |  |  | SI | Comment |
| Q13 | - |  |  | SI | Universal precautions & local policy and procedure... |
| Q14 | - |  |  | SI | Comment |
| Q15 | - |  |  | SI | Spiritual, religious, cultural rituals, needs met. |
| Q16 | - |  |  | SI | Comment |
| Q17 | - |  |  | SI | Organisational policy followed for the management ... |
| Q18 | - |  |  | SI | Comment |
| Q19 | - |  |  | SI | Organisational policy followed for the management ... |
| Q20 | - |  |  | SI | Comment |
| Q21 | - |  |  | SI | Ensure the relative or carer can express an unders... |
| Q22 | - |  |  | SI | Conversation with relative or carer explaining the... |
| Q23 | - |  |  | SI | Comment |
| Q24 | - |  |  | SI | Grievance leaflet given to relative or carer |
| Q25 | - |  |  | SI | Comment |
| Q26 | - |  |  | SI | Appropriate documentation given to relative or car... |
| Q27 | - |  |  | SI | Comment |
| Q28 | - |  |  | SI | Information given regarding how and when to contac... |
| Q29 | - |  |  | SI | Comment |
| Q30 | - |  |  | SI | Where appropriate, wishes regarding tissue / organ... |
| Q31 | - |  |  | SI | Comment |
| Q32 | - |  |  | SI | Discuss as appropriate: viewing the body / the nee... |
| Q33 | - |  |  | SI | Comment |
| Q34 | - |  |  | SI | Information given to families on child bereavement... |
| Q35 | - |  |  | SI | Comment |
| Q36 | - |  |  | SI | Ensure the primary health care team/GP are notifie... |
| Q37 | - |  |  | SI | Comment	 |
| Q38 | - |  |  | SI | Primary health care team/GP notified of patients d... |
| Q39 | - |  |  | SI | Comment |
| Q40 | - |  |  | SI | Document Variance |
| Q41 | - |  |  | SI | Ensure the patient's death communicated to appropr... |
| Q42 | - |  |  | SI | e.g Bereavement office / general office / palliati... |
| Q43 | - |  |  | SI | Comment |
| Q44 | - |  |  | SI | Relevant services notified of patients death? |
| Q45 | - |  |  | SI | Comment |
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