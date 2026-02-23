# SQLUser.OR_AnaestSurgPathwayPresAreaCare

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESAC_ParRef | varchar | PK |  | NO | - |
| PRESAC_Childsub | numeric |  |  | NO | Childsub |
| PRESAC_PresAreaCare_DR | bigint |  | FK | NO |  Des Ref ORC_Equipment |
| PRESAC_RowId | varchar |  |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Initial measurement - position of the patient's th... |
| Q11 | - |  |  | SI | Trial one (practice) measurement (centimetres) |
| Q12 | - |  |  | SI | Trial two measurement (centimetres) |
| Q13 | - |  |  | SI | Trial three measurement (centimetres) |
| Q14 | - |  |  | SI | Trial one (practice) functional reach (centimetres... |
| Q15 | - |  |  | SI | Trial two functional reach (centimetres) |
| Q16 | - |  |  | SI | Trial three functional reach (centimetres) |
| Q17 | - |  |  | SI | Average of trial 2 and 3 functional reach only (ce... |
| Q18 | - |  |  | SI | Guidelines |
| Q19 | - |  |  | SI | The patient is instructed to stand next to, but no... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | The assessor records the starting position at the ... |
| Q21 | - |  |  | SI | Instruct the patient to Reach as far as you can fo... |
| Q22 | - |  |  | SI | The location of the 3rd metacarpal is recorded. |
| Q23 | - |  |  | SI | Scores are determined by assessing the difference ... |
| Q24 | - |  |  | SI | Three trials are done and the average of the last ... |
| Q25 | - |  |  | SI | Trial one (practice) measurement (centimetres) |
| Q26 | - |  |  | SI | Trial two measurement (centimetres) |
| Q27 | - |  |  | SI | Trial three measurement (centimetres) |
| Q28 | - |  |  | SI | Initial measurement |
| Q29 | - |  |  | SI | Trial one |
| Q3 | - |  |  | SI | Duncan PW, Weiner DK, Chandler J, Studenski S. Fun... |
| Q30 | - |  |  | SI | Trial two |
| Q31 | - |  |  | SI | Trial three |
| Q32 | - |  |  | SI | Functional reach |
| Q4 | - |  |  | SI | Functional Reach Score Sheet |
| Q5 | - |  |  | SI | Initial measurement - position of the patient's th... |
| Q6 | - |  |  | SI | Trial one (practice) functional reach (centimetres... |
| Q7 | - |  |  | SI | Trial two functional reach (centimetres) |
| Q8 | - |  |  | SI | Trial three  functional reach (centimetres) |
| Q9 | - |  |  | SI | Average of trial 2 and 3 functional reach only (ce... |
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