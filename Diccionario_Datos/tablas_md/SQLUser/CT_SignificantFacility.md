# SQLUser.CT_SignificantFacility

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SIGNF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Risk Factors |
| Q02 | - |  |  | SI | Anger |
| Q03 | - |  |  | SI | Self reproach (self-blame / guilt, feeling bad and... |
| Q04 | - |  |  | SI | Current relationships |
| Q05 | - |  |  | SI | How will key person cope? |
| Q06 | - |  |  | SI | Low risk score (< 7) |
| Q07 | - |  |  | SI | • Give a copy of the brochure ''About Grief'' May ... |
| Q08 | - |  |  | SI | Nursing Staff or Social Work / Bereavement Coordin... |
| Q09 | - |  |  | SI | Moderate risk score (7-10) |
| Q10 | - |  |  | SI | • Give a copy of the brochure ''About Grief |
| Q11 | - |  |  | SI | High risk score (11-20) |
| Q12 | - |  |  | SI | • Discuss consent for referral to health professio... |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification |
| Q15 | - |  |  | SI | <7 |
| Q16 | - |  |  | SI | Low risk |
| Q17 | - |  |  | SI | 7-10 |
| Q18 | - |  |  | SI | Moderate risk |
| Q19 | - |  |  | SI | >10 |
| Q20 | - |  |  | SI | High risk |
| Q21 | - |  |  | SI | The Bereavement Risk Index (BRI) is an assessment ... |
| Q22 | - |  |  | SI | interpersonal and situational factors that may pla... |
| Q23 | - |  |  | SI | Name and contact details of bereaved person |
| Q24 | - |  |  | SI | Relationship to deceased person |
| Q25 | - |  |  | SI | Program statement given (to be read to the next of... |
| Q26 | - |  |  | SI | A Bereavement Support Program is offered, in line ... |
| Q27 | - |  |  | SI | This consists of a bereavement support person (a n... |
| Q28 | - |  |  | SI | These calls aim to provide you with additional sup... |
| Q29 | - |  |  | SI | Bereavement follow up |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
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
| SIGNF_Code | varchar |  |  | NO | Code |
| SIGNF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SIGNF_CreatedDate | date |  |  | SI | Created Date |
| SIGNF_CreatedTime | time |  |  | SI | Created Time |
| SIGNF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SIGNF_DateFrom | date |  |  | SI | Date From |
| SIGNF_DateTo | date |  |  | SI | Date To |
| SIGNF_Desc | varchar |  |  | NO | Description |
| SIGNF_NationalCode | varchar |  |  | SI | National Code |
| SIGNF_Owner | varchar |  |  | SI | Owner |
| SIGNF_UpdatedDate | date |  |  | SI | Updated Date |
| SIGNF_UpdatedTime | time |  |  | SI | Updated Time |
| SIGNF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*