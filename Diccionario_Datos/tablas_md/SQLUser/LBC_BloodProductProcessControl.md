# SQLUser.LBC_BloodProductProcessControl

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPPC_RowID | bigint | PK |  | NO | - |
| LBCBPPC_Code | varchar |  |  | NO | Code |
| LBCBPPC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCBPPC_CreatedDate | date |  |  | SI | Created Date |
| LBCBPPC_CreatedTime | time |  |  | SI | Created Time |
| LBCBPPC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPPC_DateFrom | date |  |  | SI | From Date |
| LBCBPPC_DateTo | date |  |  | SI | To Date |
| LBCBPPC_Desc | varchar |  |  | NO | Description |
| LBCBPPC_Owner | varchar |  |  | SI | Owner |
| LBCBPPC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPPC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPPC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Were any treatments withheld from this patient	 |
| Q02 | - |  |  | SI | Was treatment withdrawn from this patient?	 |
| Q03 | - |  |  | SI | Was there a discussion with the family prior to wi... |
| Q04 | - |  |  | SI | Treatment discussion withdrawal lead by	 |
| Q05 | - |  |  | SI | Date of withdrawal	 |
| Q06 | - |  |  | SI | Time of withdrawal	 |
| Q07 | - |  |  | SI | Was there a Brainstem death test?	 |
| Q08 | - |  |  | SI | Was a SNOD referral undertaken?	 |
| Q09 | - |  |  | SI | If so by whom?	 |
| Q10 | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Is the patient unconscious	 |
| Q12 | - |  |  | SI | Is there a response to supra orbital pressure	 |
| Q13 | - |  |  | SI | Is there a carotid pulse?	 |
| Q14 | - |  |  | SI | Are  heart sounds audible on ausciltation	 |
| Q15 | - |  |  | SI | Is there respiratory effort	 |
| Q16 | - |  |  | SI | Are breath sounds audible on ausciltation	 |
| Q17 | - |  |  | SI | Do the pupils react to light	 |
| Q18 | - |  |  | SI | Have you observed the above parameters for 5 minut... |
| Q19 | - |  |  | SI | Date of death 	 |
| Q20 | - |  |  | SI | Time of Death	 |
| Q21 | - |  |  | SI | Name of verifying Doctor	 |
| Q22 | - |  |  | SI | Grade |
| Q23 | - |  |  | SI | GMC number	 |
| Q24 | - |  |  | SI | Note |
| Q25 | - |  |  | SI | Systolic |
| Q25ObsDR | - |  |  | SI | Systolic DR |
| Q26 | - |  |  | SI | Pulse |
| Q26ObsDR | - |  |  | SI | Pulse DR |
| Q27 | - |  |  | SI | Note |
| Q28 | - |  |  | SI | Date From	 |
| Q29 | - |  |  | SI | Date To	 |
| Q30 | - |  |  | SI | Title |
| Q31 | - |  |  | SI | Surname |
| Q32 | - |  |  | SI | Forename |
| Q33 | - |  |  | SI | Other Name	 |
| Q34 | - |  |  | SI | Date of Birth	 |
| Q35 | - |  |  | SI | Professional Registration Issuer	 |
| Q36 | - |  |  | SI | Professional Body Registration	 |
| Q37 | - |  |  | SI | Diastolic |
| Q37ObsDR | - |  |  | SI | Diastolic DR |
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