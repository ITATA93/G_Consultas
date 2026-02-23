# questionnaire.QTCCFNSI

> Needle Stick Incident

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Needle Stick Incident

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Date of occurrence |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Day |
| Q04 | time |  |  | SI | Time |
| Q05 | varchar |  |  | SI | Healthcare worker / employee job category  |
| Q06 | varchar |  |  | SI | Specify |
| Q07 | varchar |  |  | SI | Healthcare worker / employee department |
| Q08 | varchar |  |  | SI | Department |
| Q09 | varchar |  |  | SI | Unit / Ward |
| Q10 | varchar |  |  | SI | Location of injury / exposure |
| Q11 | varchar |  |  | SI | Employee's HBV Immunization Status |
| Q12 | varchar |  |  | SI | Part B |
| Q13 | varchar |  |  | SI | Source serology |
| Q14 | varchar |  |  | SI | Was the source patient identifiable? |
| Q15 | varchar |  |  | SI | Serology of source patient |
| Q16 | varchar |  |  | SI | Supervisor / HOD |
| Q17 | date |  |  | SI | Date |
| Q18 | time |  |  | SI | Time |
| Q19 | longvarbinary |  |  | SI | signature |
| Q19UDt | date |  |  | SI | signature Last Updated Date |
| Q19UTm | time |  |  | SI | signature Last Updated Time |
| Q20 | varchar |  |  | SI | Part C |
| Q21 | varchar |  |  | SI | Staff health clinic/ED use |
| Q22 | varchar |  |  | SI | A Needle stick / sharps injury |
| Q23 | varchar |  |  | SI | Was the sharp that caused the injury contaminated? |
| Q24 | varchar |  |  | SI | Was blood visible on the device? |
| Q25 | varchar |  |  | SI | For what purpose was the sharp that caused the inj... |
| Q26 | varchar |  |  | SI | If used to draw blood was it? |
| Q27 | varchar |  |  | SI | Specify |
| Q28 | varchar |  |  | SI | Describe how did the injury/ exposure occur? |
| Q29 | varchar |  |  | SI | What type of device caused the injury? |
| Q30 | varchar |  |  | SI | How deep was the injury? |
| Q31 | varchar |  |  | SI | B Blood/ body fluid exposure |
| Q32 | varchar |  |  | SI | Was the body fluid visibly stained with blood |
| Q33 | varchar |  |  | SI | Which body surfaces of the healthcare worker was i... |
| Q34 | varchar |  |  | SI | Specify |
| Q35 | varchar |  |  | SI | Which barrier garment were worn at the time of exp... |
| Q36 | varchar |  |  | SI | What was the exposure the result of ? |
| Q37 | varchar |  |  | SI | Other specify |
| Q38 | varchar |  |  | SI | How long was the blood or bloody fluid in contact ... |
| Q39 | varchar |  |  | SI | How much blood / body fluid came in contact with h... |
| Q40 | varchar |  |  | SI | SHC/ED Physician |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
| Q43 | longvarbinary |  |  | SI | Signature |
| Q43UDt | date |  |  | SI | Signature Last Updated Date |
| Q43UTm | time |  |  | SI | Signature Last Updated Time |
| Q44 | varchar |  |  | SI | Mark the location of injury |
| Q45 | varchar |  |  | SI | Specify |
| Q46 | varchar |  |  | SI | Specify |
| Q47 | varchar |  |  | SI | Specify |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
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