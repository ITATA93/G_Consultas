# SQLUser.ORC_CatheterRoute

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHRT_RowId | bigint | PK |  | NO | - |
| CTHRT_Code | varchar |  |  | NO | Code |
| CTHRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTHRT_CreatedDate | date |  |  | SI | Created Date |
| CTHRT_CreatedTime | time |  |  | SI | Created Time |
| CTHRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTHRT_DateFrom | date |  |  | SI | Date From |
| CTHRT_DateTo | date |  |  | SI | Date To |
| CTHRT_Desc | varchar |  |  | NO | Description |
| CTHRT_Owner | varchar |  |  | SI | Owner |
| CTHRT_UpdatedDate | date |  |  | SI | Updated Date |
| CTHRT_UpdatedTime | time |  |  | SI | Updated Time |
| CTHRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of occurrence |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Day |
| Q04 | - |  |  | SI | Time |
| Q05 | - |  |  | SI | Healthcare worker / employee job category |
| Q06 | - |  |  | SI | Specify |
| Q07 | - |  |  | SI | Healthcare worker / employee department |
| Q08 | - |  |  | SI | Department |
| Q09 | - |  |  | SI | Unit / Ward |
| Q10 | - |  |  | SI | Location of injury / exposure |
| Q11 | - |  |  | SI | Employee's HBV Immunization Status |
| Q12 | - |  |  | SI | Part B |
| Q13 | - |  |  | SI | Source serology |
| Q14 | - |  |  | SI | Was the source patient identifiable? |
| Q15 | - |  |  | SI | Serology of source patient |
| Q16 | - |  |  | SI | Supervisor / HOD |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
| Q19 | - |  |  | SI | signature |
| Q19UDt | - |  |  | SI | signature Last Updated Date |
| Q19UTm | - |  |  | SI | signature Last Updated Time |
| Q20 | - |  |  | SI | Part C |
| Q21 | - |  |  | SI | Staff health clinic/ED use |
| Q22 | - |  |  | SI | A Needle stick / sharps injury |
| Q23 | - |  |  | SI | Was the sharp that caused the injury contaminated? |
| Q24 | - |  |  | SI | Was blood visible on the device? |
| Q25 | - |  |  | SI | For what purpose was the sharp that caused the inj... |
| Q26 | - |  |  | SI | If used to draw blood was it? |
| Q27 | - |  |  | SI | Specify |
| Q28 | - |  |  | SI | Describe how did the injury/ exposure occur? |
| Q29 | - |  |  | SI | What type of device caused the injury? |
| Q30 | - |  |  | SI | How deep was the injury? |
| Q31 | - |  |  | SI | B Blood/ body fluid exposure |
| Q32 | - |  |  | SI | Was the body fluid visibly stained with blood |
| Q33 | - |  |  | SI | Which body surfaces of the healthcare worker was i... |
| Q34 | - |  |  | SI | Specify |
| Q35 | - |  |  | SI | Which barrier garment were worn at the time of exp... |
| Q36 | - |  |  | SI | What was the exposure the result of ? |
| Q37 | - |  |  | SI | Other specify |
| Q38 | - |  |  | SI | How long was the blood or bloody fluid in contact ... |
| Q39 | - |  |  | SI | How much blood / body fluid came in contact with h... |
| Q40 | - |  |  | SI | SHC/ED Physician |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
| Q43 | - |  |  | SI | Signature |
| Q43UDt | - |  |  | SI | Signature Last Updated Date |
| Q43UTm | - |  |  | SI | Signature Last Updated Time |
| Q44 | - |  |  | SI | Mark the location of injury |
| Q45 | - |  |  | SI | Specify |
| Q46 | - |  |  | SI | Specify |
| Q47 | - |  |  | SI | Specify |
| Q48 | - |  |  | SI | Date |
| Q49 | - |  |  | SI | Time |
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