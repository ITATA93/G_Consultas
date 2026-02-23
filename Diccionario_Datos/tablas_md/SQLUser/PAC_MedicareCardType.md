# SQLUser.PAC_MedicareCardType

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MCCT_RowId | bigint | PK |  | NO | - |
| MCCT_Code | varchar |  |  | NO | Code |
| MCCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MCCT_CreatedDate | date |  |  | SI | Created Date |
| MCCT_CreatedTime | time |  |  | SI | Created Time |
| MCCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MCCT_DateFrom | date |  |  | SI | Date From |
| MCCT_DateTo | date |  |  | SI | Date To |
| MCCT_Desc | varchar |  |  | NO | Description |
| MCCT_Owner | varchar |  |  | SI | Owner |
| MCCT_UpdatedDate | date |  |  | SI | Updated Date |
| MCCT_UpdatedTime | time |  |  | SI | Updated Time |
| MCCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Reason for appointment |
| Q04 | - |  |  | SI | Consent obtained |
| Q05 | - |  |  | SI | Coagulation profile |
| Q06 | - |  |  | SI | Activated Partial Thromboplastin Time (APPT)	 |
| Q07 | - |  |  | SI | Allergies checked |
| Q08 | - |  |  | SI | Patient has pacemaker |
| Q09 | - |  |  | SI | Location of insertion |
| Q10 | - |  |  | SI | Other location of insertion details |
| Q11 | - |  |  | SI | Oxygen saturation |
| Q12 | - |  |  | SI | Blood pressure |
| Q13 | - |  |  | SI | CO2	 |
| Q14 | - |  |  | SI | Electrocardiogram |
| Q15 | - |  |  | SI | INSERTION SHOULD STOP IF ASEPSIS IS BREACHED |
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