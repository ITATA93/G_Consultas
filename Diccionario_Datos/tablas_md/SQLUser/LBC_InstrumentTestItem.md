# SQLUser.LBC_InstrumentTestItem

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINTI_ParRef | bigint | PK |  | NO | Parent instrument |
| LBCINTI_AntibInstrumentTestItemID | varchar |  |  | SI | Inbound Antibiotic Result Instrument Test Item ID ... |
| LBCINTI_AntibOutboundInstrumentTestItemID | varchar |  |  | SI | Outbound Antibiotic Order Instrument Test Item ID ... |
| LBCINTI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINTI_Enabled | varchar |  |  | SI | Enabled
Flag to indicate whether this test item i... |
| LBCINTI_FileRepeats | varchar |  |  | SI | Directly file all repeats into the test set (do no... |
| LBCINTI_HoldAntibioticOrder | varchar |  |  | SI | Hold antibiotic order until organism result has be... |
| LBCINTI_InstrumentTestItemID | varchar |  |  | SI | Inbound Result Instrument Test Item ID (Channel ID... |
| LBCINTI_InstrumentTestItemIDCaseSensitive | varchar |  |  | SI | Flag to indicate whether the Inbound Result Instru... |
| LBCINTI_OutResultInstrumentTestItemID | varchar |  |  | SI | Outbound Result Instrument Test Item ID (Channel I... |
| LBCINTI_OutboundInstrumentTestItemID | varchar |  |  | SI | Outbound Order Instrument Test Item ID (Channel ID... |
| LBCINTI_POCTOrderItem_DR | varchar |  | FK | SI | POCT Test Set to Order |
| LBCINTI_QCBracketDuration | integer |  |  | SI | QC Bracket Duration |
| LBCINTI_QCBracketDurationUnit | varchar |  |  | SI | QC Bracket Duration unit |
| LBCINTI_QCBracketNumEpisodes | integer |  |  | SI | QC Bracket Number Of Samples |
| LBCINTI_RowID | varchar |  |  | NO | - |
| LBCINTI_Sequence | double |  |  | NO | Display sequence |
| LBCINTI_TestGroups | varchar |  |  | SI | - |
| LBCINTI_TestItem_DR | bigint |  | FK | SI | Test Item |
| LBCINTI_TestItems | varchar |  |  | SI | A list of test items which results will be transmi... |
| Q01 | - |  |  | SI | 1 - ¿Cuántos cigarrillos fuma al día? |
| Q02 | - |  |  | SI | 2 - ¿Cuánto tiempo pasa desde que se levanta hasta... |
| Q03 | - |  |  | SI | 3 - ¿Fuma más en las mañanas? |
| Q04 | - |  |  | SI | 4 - ¿Tiene dificultad para no fumar en lugares don... |
| Q05 | - |  |  | SI | 5 - ¿A qué cigarrillo le costaría más renunciar? |
| Q06 | - |  |  | SI | 6 - ¿Fuma aunque esté enfermo y tenga que pasar la... |
| Q07 | - |  |  | SI | Resultado Dependencia Nicotina |
| Q07ObsDR | - |  |  | SI | Resultado Dependencia Nicotina DR |
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