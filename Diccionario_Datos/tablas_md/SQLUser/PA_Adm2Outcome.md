# SQLUser.PA_Adm2Outcome

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OUTC_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| OUTC_ApOutcome_DR | bigint |  | FK | SI | Des Ref Appt Outcome |
| OUTC_Childsub | double |  |  | NO | Childsub |
| OUTC_CommentHTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| OUTC_CommentHTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| OUTC_Date | date |  |  | SI | Date |
| OUTC_DateOfOutcome | date |  |  | SI | DateOfOutcome |
| OUTC_LastUpdateDate | date |  |  | SI | Last Update Date |
| OUTC_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| OUTC_LastUpdateTime | time |  |  | SI | Last Update Time |
| OUTC_LastUpdateUser_DR | bigint |  | FK | SI | Last Update User |
| OUTC_NewPAReferralPathway_DR | bigint |  | FK | SI | Link to the pathway that has been newly created fo... |
| OUTC_OrderItems | varchar |  |  | SI | OrderItems  |
| OUTC_PARefPathwayStage_DR | varchar |  | FK | SI | Des Ref PARefPathwayStage |
| OUTC_RefPathwayStage_DR | varchar |  | FK | SI | Des Ref PARefPathwayStage |
| OUTC_Remarks | varchar |  |  | SI | Remarks |
| OUTC_RowId | varchar |  |  | NO | - |
| OUTC_Time | time |  |  | SI | Time |
| OUTC_User_DR | bigint |  | FK | SI | Des Ref User |
| OUTC_WaitList_DR | bigint |  | FK | SI | Des Ref PAWaitingList |
| Q01 | - |  |  | SI | PaO2/FiO2 (mmHg) |
| Q02 | - |  |  | SI | Platelets × 10E3/mm3 |
| Q03 | - |  |  | SI | Mean Arterial Pressure (MAP) OR administration of ... |
| Q04 | - |  |  | SI | Glasgow coma scale |
| Q05 | - |  |  | SI | Bilirubin (mg/dl) [μmol/L] |
| Q06 | - |  |  | SI | Creatinine (mg/dl) [μmol/L] OR urine output |
| Q07 | - |  |  | SI | Notes |
| Q08 | - |  |  | SI | 24 - High degree of organ dysfunction  / 0 - Low d... |
| Q09 | - |  |  | SI | A higher number is associated with a higher degree... |
| Q10 | - |  |  | SI | Use the worst value for each physiological variabl... |
| Q11 | - |  |  | SI | Sepsis-related Organ Failure Assessment score (SOF... |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
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