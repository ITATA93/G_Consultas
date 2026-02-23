# SQLUser.LBC_InstrumentReactionTrans

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINRT_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINRT_DateFrom | date |  |  | SI | Date From |
| LBCINRT_DateTo | date |  |  | SI | Date To |
| LBCINRT_InstrumentReaction | varchar |  |  | SI | Instrument Reaction |
| LBCINRT_Reaction_DR | bigint |  | FK | SI | Internal Reaction |
| LBCINRT_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Extra Oral |
| Q04 | - |  |  | SI | Face |
| Q05 | - |  |  | SI | Symmetry/ Asymmetry |
| Q06 | - |  |  | SI | Profile |
| Q07 | - |  |  | SI | Intra Oral |
| Q08 | - |  |  | SI | Oral hygiene |
| Q09 | - |  |  | SI | Calculus |
| Q09a | - |  |  | SI | Calculus details |
| Q10 | - |  |  | SI | Stain |
| Q10a | - |  |  | SI | Stain Details |
| Q11 | - |  |  | SI | Oral mucosa |
| Q11a | - |  |  | SI | Abnormal oral mucosa |
| Q12 | - |  |  | SI | Tounge |
| Q13 | - |  |  | SI | Jaw relations |
| Q14 | - |  |  | SI | Others |
| Q15 | - |  |  | SI | Occlusion |
| Q16 | - |  |  | SI | Torus palatinus |
| Q17 | - |  |  | SI | Torus mandibularis |
| Q18 | - |  |  | SI | Palatum |
| Q19 | - |  |  | SI | Diastema |
| Q20 | - |  |  | SI | Diastema details |
| Q21 | - |  |  | SI | Dental anomalies |
| Q22 | - |  |  | SI | Anomalies details |
| Q23 | - |  |  | SI | Others details |
| Q24 | - |  |  | SI | Decay |
| Q25 | - |  |  | SI | Missing |
| Q26 | - |  |  | SI | Filling |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*