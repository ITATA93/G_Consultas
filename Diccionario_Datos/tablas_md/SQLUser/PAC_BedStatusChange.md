# SQLUser.PAC_BedStatusChange

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STAT_ParRef | varchar | PK |  | NO | PAC_Bed Parent Reference |
| ChildQ27DR | - |  |  | SI | Child Reference: Melioidosis titre |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Risk factor(s) |
| Q04 | - |  |  | SI | Other risk factor(s) |
| Q05 | - |  |  | SI | Number of admissions |
| Q06 | - |  |  | SI | Details of previous admissions |
| Q07 | - |  |  | SI | Diagnosis date |
| Q08 | - |  |  | SI | Discharge date |
| Q09 | - |  |  | SI | Disease status |
| Q10 | - |  |  | SI | Melioidosis history |
| Q11 | - |  |  | SI | Inoculation event |
| Q12 | - |  |  | SI | Melioidosis diagnosis (ensure patients diagnosis i... |
| Q13 | - |  |  | SI | Other clinical focus notes |
| Q14 | - |  |  | SI | Blood culture |
| Q15 | - |  |  | SI | Date blood culture completed |
| Q16 | - |  |  | SI | Sputum culture |
| Q17 | - |  |  | SI | Date sputum culture completed |
| Q18 | - |  |  | SI | Urine culture |
| Q19 | - |  |  | SI | Date urine culture completed |
| Q20 | - |  |  | SI | Pus cutlure |
| Q21 | - |  |  | SI | Date pus culture completed |
| Q22 | - |  |  | SI | Septic shock |
| Q23 | - |  |  | SI | Abscesses |
| Q24 | - |  |  | SI | Other location of abscess notes |
| Q25 | - |  |  | SI | Chest X-ray (CXR) |
| Q26 | - |  |  | SI | Date CXR completed |
| Q28 | - |  |  | SI | Intensive Care Unit (ICU) admission |
| Q29 | - |  |  | SI | During ICU admission, patient was |
| Q30 | - |  |  | SI | Antibiotic recommendations |
| Q31 | - |  |  | SI | Compliance |
| Q32 | - |  |  | SI | Antibiotic recommendations |
| Q33 | - |  |  | SI | Compliance |
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
| STAT_Childsub | double |  |  | NO | Childsub |
| STAT_Comment | varchar |  |  | SI | Comment |
| STAT_CreatedDate | date |  |  | SI | Created Date |
| STAT_CreatedTime | time |  |  | SI | Created Time |
| STAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STAT_Date | date |  |  | NO | Date |
| STAT_DateTo | date |  |  | SI | Date To |
| STAT_ReasonNotAvail_DR | bigint |  | FK | SI | Des Ref ReasonNotAvail |
| STAT_ReservedBed | varchar |  |  | SI | Reserve Bed |
| STAT_ReservedByEpisode_DR | bigint |  | FK | SI | Reserved By Episode |
| STAT_RowId | varchar |  |  | NO | - |
| STAT_Status_DR | bigint |  | FK | SI | Des Ref Status |
| STAT_Time | time |  |  | NO | Time |
| STAT_TimeTo | time |  |  | SI | Time To |
| STAT_UpdateDate | date |  |  | SI | UpdateDate |
| STAT_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| STAT_UpdateTime | time |  |  | SI | UpdateTime |
| STAT_UpdatedDate | date |  |  | SI | Updated Date |
| STAT_UpdatedTime | time |  |  | SI | Updated Time |
| STAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| STAT_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*