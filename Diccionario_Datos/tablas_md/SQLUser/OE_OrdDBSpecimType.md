# SQLUser.OE_OrdDBSpecimType

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DBSPEC_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| DBSPEC_Childsub | double |  |  | NO | Childsub |
| DBSPEC_RowId | varchar |  |  | NO | - |
| DBSPEC_SpecType | varchar |  |  | SI | Spec Type |
| Q01 | - |  |  | SI | Functional Reach Left |
| Q02 | - |  |  | SI | Functional Reach Right |
| Q03 | - |  |  | SI | Step Test (15 secs) Left Up |
| Q04 | - |  |  | SI | Step Test (15 secs) Right Up |
| Q05 | - |  |  | SI | Smart Balance Master Assessment |
| Q06 | - |  |  | SI | Composite Score (SOT) |
| Q07 | - |  |  | SI | Test |
| Q08 | - |  |  | SI | Position |
| Q09 | - |  |  | SI | (score time up to 30 sec) |
| Q10 | - |  |  | SI | Surface |
| Q11 | - |  |  | SI | Eyes |
| Q12 | - |  |  | SI | FA |
| Q13 | - |  |  | SI | FT |
| Q14 | - |  |  | SI | Tandem Left |
| Q15 | - |  |  | SI | Tandem Right |
| Q16 | - |  |  | SI | SLS Left |
| Q17 | - |  |  | SI | SLS Right |
| Q18 | - |  |  | SI | Firm |
| Q19 | - |  |  | SI | Open |
| Q20 | - |  |  | SI | Firm Surface, Open Eyes, FA |
| Q21 | - |  |  | SI | Firm Surface, Open Eyes, FT |
| Q22 | - |  |  | SI | Firm Surface, Open Eyes, Tandem Left |
| Q23 | - |  |  | SI | Firm Surface, Open Eyes, Tandem Right |
| Q24 | - |  |  | SI | Firm Surface, Open Eyes, SLS Left |
| Q25 | - |  |  | SI | Firm Surface, Open Eyes, SLS Right |
| Q26 | - |  |  | SI | Firm |
| Q27 | - |  |  | SI | Closed |
| Q28 | - |  |  | SI | Firm Surface, Closed Eyes, FA |
| Q29 | - |  |  | SI | Firm Surface, Closed Eyes, FT |
| Q30 | - |  |  | SI | Firm Surface, Closed Eyes, Tandem Left |
| Q31 | - |  |  | SI | Firm Surface, Closed Eyes, Tandem Right |
| Q32 | - |  |  | SI | Firm Surface, Closed Eyes, SLS Left |
| Q33 | - |  |  | SI | Firm Surface, Closed Eyes, SLS Right |
| Q34 | - |  |  | SI | Foam / Soft |
| Q35 | - |  |  | SI | Open |
| Q36 | - |  |  | SI | Foam/Soft Surface, Open Eyes, FA |
| Q37 | - |  |  | SI | Foam/Soft Surface, Open Eyes, FT |
| Q38 | - |  |  | SI | Foam/Soft Surface, Open Eyes, Tandem Left |
| Q39 | - |  |  | SI | Foam/Soft Surface, Open Eyes, Tandem Right |
| Q40 | - |  |  | SI | Foam/Soft Surface, Open Eyes, SLS Left |
| Q41 | - |  |  | SI | Foam/Soft Surface, Open Eyes, SLS Right |
| Q42 | - |  |  | SI | Foam / Soft |
| Q43 | - |  |  | SI | Closed |
| Q44 | - |  |  | SI | Foam/Soft Surface, Closed Eyes, FA |
| Q45 | - |  |  | SI | Foam/Soft Surface, Closed Eyes, FT |
| Q46 | - |  |  | SI | Foam/Soft Surface, Closed Eyes, Tandem Left |
| Q47 | - |  |  | SI | Foam/Soft Surface, Closed Eyes, Tandem Right |
| Q48 | - |  |  | SI | Foam/Soft Surface, Closed Eyes, SLS Left |
| Q49 | - |  |  | SI | Foam/Soft Surface, Closed Eyes, SLS Right |
| Q50 | - |  |  | SI | Comments |
| Q51 | - |  |  | SI | Limits of Stability (Internal / External Perturbat... |
| Q52 | - |  |  | SI | Ankle Strategy |
| Q53 | - |  |  | SI | Hip Strategy |
| Q54 | - |  |  | SI | Step Strategy |
| Q55 | - |  |  | SI | The Clinical Test of Sensory Interaction of Balanc... |
| Q56 | - |  |  | SI | Balance Measures |
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