# SQLUser.ORC_LineType

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINTYP_RowId | bigint | PK |  | NO | - |
| LINTYP_Code | varchar |  |  | NO | Code |
| LINTYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LINTYP_CreatedDate | date |  |  | SI | Created Date |
| LINTYP_CreatedTime | time |  |  | SI | Created Time |
| LINTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LINTYP_DateFrom | date |  |  | SI | Date From |
| LINTYP_DateTo | date |  |  | SI | Date To |
| LINTYP_Desc | varchar |  |  | NO | Description |
| LINTYP_Owner | varchar |  |  | SI | Owner |
| LINTYP_UpdatedDate | date |  |  | SI | Updated Date |
| LINTYP_UpdatedTime | time |  |  | SI | Updated Time |
| LINTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Admission date |
| Q04 | - |  |  | SI | Admission time |
| Q05 | - |  |  | SI | Date of initial screening |
| Q06 | - |  |  | SI | Time of initial screening |
| Q07 | - |  |  | SI | a. Use of discharge medications |
| Q08 | - |  |  | SI | b. Post discharge care |
| Q09 | - |  |  | SI | c. Nutritional discharge instructions |
| Q10 | - |  |  | SI | d. Use of medical equipment |
| Q11 | - |  |  | SI | e. Instructions on activity of daily living |
| Q12 | - |  |  | SI | f. How to seek medical services when emergency rel... |
| Q13 | - |  |  | SI | g. Patient's booking for appointment including tes... |
| Q14 | - |  |  | SI | Interventions carried out to achieve educational n... |
| Q15 | - |  |  | SI | The patient or family member has need to have educ... |
| Q16 | - |  |  | SI | The patient needs transportation: |
| Q17 | - |  |  | SI | a. Ambulance / Car |
| Q18 | - |  |  | SI | b. Medivac |
| Q19 | - |  |  | SI | c. Private car |
| Q20 | - |  |  | SI | Interventions carried out to achieve transportatio... |
| Q21 | - |  |  | SI | Patient is in need of referral to: |
| Q22 | - |  |  | SI | a. Social worker / psychologist counselling, for c... |
| Q23 | - |  |  | SI | b. Home healthcare services |
| Q24 | - |  |  | SI | c. Other post-discharge agencies |
| Q25 | - |  |  | SI | Interventions carried out to achieve referral need... |
| Q26 | - |  |  | SI | • Discharge planning screening shall be documented... |
| Q27 | - |  |  | SI | • Physician shall use this checklist during patien... |
| Q28 | - |  |  | SI | • If any box checked yes, physician shall carry ou... |
| Q29 | - |  |  | SI | • The primary nurse shall coordinate the referral ... |
| Q30 | - |  |  | SI | Patient needs support with: |
| Q31 | - |  |  | SI | a. Financial needs expected after discharge |
| Q32 | - |  |  | SI | b. Other discharge planning problems identified at... |
| Q33 | - |  |  | SI | Interventions carried out to achieve financial and... |
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