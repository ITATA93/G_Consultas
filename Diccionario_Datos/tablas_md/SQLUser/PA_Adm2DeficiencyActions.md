# SQLUser.PA_Adm2DeficiencyActions

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEFACT_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| DEFACT_Action | varchar |  |  | SI | Action |
| DEFACT_Childsub | double |  |  | NO | Childsub |
| DEFACT_Comments | varchar |  |  | SI | Comments |
| DEFACT_Date | date |  |  | SI | Date |
| DEFACT_EarliestDestructionDate | date |  |  | SI | EarliestDestructionDate |
| DEFACT_RetentionStatus_DR | bigint |  | FK | SI | Des Ref RetentionStaus |
| DEFACT_RowId | varchar |  |  | NO | - |
| DEFACT_Time | time |  |  | SI | Time |
| DEFACT_UserUpdated_DR | bigint |  | FK | SI | Des Ref UserUpdated |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient experience with blood glucose level (BGL) ... |
| Q04 | - |  |  | SI | Monitor status |
| Q05 | - |  |  | SI | Type of monitor given |
| Q06 | - |  |  | SI | Monitor orientation provided |
| Q07 | - |  |  | SI | Lancet device explained |
| Q08 | - |  |  | SI | Proficiency: lancet device use |
| Q09 | - |  |  | SI | BGL testing times explained |
| Q10 | - |  |  | SI | Proficiency: BGL testing times |
| Q11 | - |  |  | SI | Explanation of use of test strip including |
| Q12 | - |  |  | SI | Proficiency: use of test strip |
| Q13 | - |  |  | SI | Sharps disposal bin explained |
| Q14 | - |  |  | SI | Proficiency: sharps disposal |
| Q15 | - |  |  | SI | Proficiency: importance of clean hands |
| Q16 | - |  |  | SI | Proficiency: recording BGL reading from monitor to... |
| Q17 | - |  |  | SI | Notes |
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