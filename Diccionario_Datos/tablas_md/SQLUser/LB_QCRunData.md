# SQLUser.LB_QCRunData

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCRD_ParRef | bigint | PK |  | NO | - |
| LBQCRDQC_Scheme_DR | bigint |  | FK | SI | QC Scheme Link (for indexing) |
| LBQCRD_10xAction | varchar |  |  | SI | 10x Action
StandardType: LabQCRuleAction |
| LBQCRD_10xSequenceNumber | numeric |  |  | SI | 10x Sequence Number |
| LBQCRD_10xViolation | varchar |  |  | SI | 10x Violation |
| LBQCRD_12sAction | varchar |  |  | SI | 12s Action
StandardType: LabQCRuleAction |
| LBQCRD_12sSequenceNumber | numeric |  |  | SI | 12s Sequence Number |
| LBQCRD_12sViolation | varchar |  |  | SI | 12s Violation |
| LBQCRD_12xAction | varchar |  |  | SI | 12x Action
StandardType: LabQCRuleAction |
| LBQCRD_12xSequenceNumber | numeric |  |  | SI | 12x Sequence Number |
| LBQCRD_12xViolation | varchar |  |  | SI | 12x Violation |
| LBQCRD_13sAction | varchar |  |  | SI | 13s Action
StandardType: LabQCRuleAction |
| LBQCRD_13sSequenceNumber | numeric |  |  | SI | 13s Sequence Number |
| LBQCRD_13sViolation | varchar |  |  | SI | 13s Violation |
| LBQCRD_22sAction | varchar |  |  | SI | 22s Action
StandardType: LabQCRuleAction |
| LBQCRD_22sSequenceNumber | numeric |  |  | SI | 22s Sequence Number |
| LBQCRD_22sViolation | varchar |  |  | SI | 22s Violation |
| LBQCRD_2of32sAction | varchar |  |  | SI | 2of32s Action
StandardType: LabQCRuleAction |
| LBQCRD_2of32sSequenceNumber | numeric |  |  | SI | 2of32s Sequence Number |
| LBQCRD_2of32sViolation | varchar |  |  | SI | 2of32s Violation |
| LBQCRD_31sAction | varchar |  |  | SI | 31s Action
StandardType: LabQCRuleAction |
| LBQCRD_31sSequenceNumber | numeric |  |  | SI | 31s Sequence Number |
| LBQCRD_31sViolation | varchar |  |  | SI | 31s Violation |
| LBQCRD_41sAction | varchar |  |  | SI | 41s Action
StandardType: LabQCRuleAction |
| LBQCRD_41sSequenceNumber | numeric |  |  | SI | 41s Sequence Number |
| LBQCRD_41sViolation | varchar |  |  | SI | 41s Violation |
| LBQCRD_6xAction | varchar |  |  | SI | 6x Action
StandardType: LabQCRuleAction |
| LBQCRD_6xSequenceNumber | numeric |  |  | SI | 6x Sequence Number |
| LBQCRD_6xViolation | varchar |  |  | SI | 6x Violation |
| LBQCRD_7TAction | varchar |  |  | SI | 7T Action
StandardType: LabQCRuleAction |
| LBQCRD_7TSequenceNumber | numeric |  |  | SI | 7T Sequence Number |
| LBQCRD_7TViolation | varchar |  |  | SI | 7T Violation |
| LBQCRD_8xAction | varchar |  |  | SI | 8x Action
StandardType: LabQCRuleAction |
| LBQCRD_8xSequenceNumber | numeric |  |  | SI | 8x Sequence Number |
| LBQCRD_8xViolation | varchar |  |  | SI | 8x Violation |
| LBQCRD_9xAction | varchar |  |  | SI | 9x Action
StandardType: LabQCRuleAction |
| LBQCRD_9xSequenceNumber | numeric |  |  | SI | 9x Sequence Number |
| LBQCRD_9xViolation | varchar |  |  | SI | 9x Violation |
| LBQCRD_CommentDate | date |  |  | SI | Comment date |
| LBQCRD_CommentTime | date |  |  | SI | Comment time |
| LBQCRD_CommentUser_DR | bigint |  | FK | SI | Comment user |
| LBQCRD_Comments | varchar |  |  | SI | Comments |
| LBQCRD_Date | date |  |  | SI | Date of measurement |
| LBQCRD_EnteredByDR | bigint |  | FK | SI | User who (last) entered QC Run Data |
| LBQCRD_Excluded | varchar |  |  | SI | Exlusion Flag |
| LBQCRD_ExcludedDate | date |  |  | SI | Excluded date |
| LBQCRD_ExcludedReason_DR | bigint |  | FK | SI | Reason for exclusion |
| LBQCRD_ExcludedTime | time |  |  | SI | Excluded time |
| LBQCRD_ExcludedUser_DR | bigint |  | FK | SI | User to exclude data |
| LBQCRD_Instrument_DR | bigint |  | FK | SI | Instrument the QC was performed on |
| LBQCRD_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBQCRD_Link_DR | varchar |  | FK | SI | QC Batch Level Value Group Link |
| LBQCRD_NNAction | varchar |  |  | SI | NN Action
StandardType: LabQCRuleAction |
| LBQCRD_NNSequenceNumber | numeric |  |  | SI | NN Sequence Number |
| LBQCRD_NNViolation | varchar |  |  | SI | NN Violation |
| LBQCRD_R4sAction | varchar |  |  | SI | R4s Action
StandardType: LabQCRuleAction |
| LBQCRD_R4sSequenceNumber | numeric |  |  | SI | R4s Sequence Number |
| LBQCRD_R4sViolation | varchar |  |  | SI | R4s Violation |
| LBQCRD_RowID | varchar |  |  | NO | - |
| LBQCRD_SequenceNumber | numeric |  |  | SI | Data sequencene number |
| LBQCRD_Superseded | varchar |  |  | SI | Superseded
Flag to indicate that this data value ... |
| LBQCRD_TRAction | varchar |  |  | SI | TR Action
StandardType: LabQCRuleAction |
| LBQCRD_TRSequenceNumber | numeric |  |  | SI | TR Sequence Number |
| LBQCRD_TRViolation | varchar |  |  | SI | TR Violation |
| LBQCRD_TargetCV | varchar |  |  | SI | Target CV at the time of rule evaluation |
| LBQCRD_TargetMean | varchar |  |  | SI | Target Mean at the time of rule evaluation |
| LBQCRD_TargetSD | varchar |  |  | SI | Target SD at the time of rule evaluation |
| LBQCRD_TargetValues | varchar |  |  | SI | Non-numeric Target Values at the time of rule eval... |
| LBQCRD_TestItem_DR | varchar |  | FK | SI | QC Batch Level Value Group Test Item |
| LBQCRD_Time | time |  |  | SI | Time of measurement |
| LBQCRD_TitreFrom | varchar |  |  | SI | Titre target value from at the time of rule evalua... |
| LBQCRD_TitreTo | varchar |  |  | SI | Titre target value to at the time of rule evaluati... |
| LBQCRD_Value | varchar |  |  | SI | QC measurement |
| Q01 | - |  |  | SI | Tipo de Hospitalizacion |
| Q02 | - |  |  | SI | Clinica / Hospital |
| Q03 | - |  |  | SI | Tipo Cama |
| Q04 | - |  |  | SI | Dias de Estadía |
| Q05 | - |  |  | SI | Fecha de Ingreso |
| Q06 | - |  |  | SI | Fecha de Egreso |
| Q07 | - |  |  | SI | Destino Rescate |
| Q08 | - |  |  | SI | Observaciones |
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