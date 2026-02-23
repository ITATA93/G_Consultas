# SQLUser.LB_QCBatch

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCB_RowID | bigint | PK |  | NO | - |
| LBQCB_BatchNumber | varchar |  |  | NO | Batch Number
Unique number of the batch within th... |
| LBQCB_Comments | varchar |  |  | SI | Comments |
| LBQCB_ContainerNumber | varchar |  |  | SI | Container Number (Free text field) |
| LBQCB_DateClosed | date |  |  | SI | Closed Date |
| LBQCB_DateOpened | date |  |  | SI | Date In Use  |
| LBQCB_DateReceived | date |  |  | SI | Date Received |
| LBQCB_DisplayDatesOnXAxis | varchar |  |  | SI | Display dates on X Axis of QC Summary Chart |
| LBQCB_ExpiryDate | date |  |  | SI | Expiry Date
Default expiry date for the whole bat... |
| LBQCB_ExpiryWarningDays | integer |  |  | SI | Expiry Warning Days
A warning will be produced a ... |
| LBQCB_LabSites | varchar |  |  | SI | Lab Sites
List of lab sites the batch was used at |
| LBQCB_MaxExtensionDays | integer |  |  | SI | Maximum Extension Days
Default maximum number of ... |
| LBQCB_QCScheme_DR | bigint |  | FK | NO | Quality Control Scheme
Link to the quality contro... |
| LBQCB_ReceivedCondition_DR | bigint |  | FK | SI | Condition when Received |
| LBQCB_SequenceNumber | numeric |  |  | SI | Sequence Number
Sequence of the batch within the ... |
| LBQCB_Supplier_DR | bigint |  | FK | SI | Supplier |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Autonomo |
| Q03 | - |  |  | SI | Total |
| Q04 | - |  |  | SI | Parcial |
| Q05 | - |  |  | SI | Detalle |
| Q06 | - |  |  | SI | Orina |
| Q07 | - |  |  | SI | Anuria |
| Q08 | - |  |  | SI | Incontinencia |
| Q09 | - |  |  | SI | Ocasional |
| Q10 | - |  |  | SI | Permanente |
| Q11 | - |  |  | SI | Retencion |
| Q12 | - |  |  | SI | Disuria |
| Q13 | - |  |  | SI | Dispositivo |
| Q14 | - |  |  | SI | Tipo |
| Q15 | - |  |  | SI | Fecha Colocacion |
| Q16 | - |  |  | SI | Heces |
| Q17 | - |  |  | SI | Estreñimiento |
| Q18 | - |  |  | SI | Laxantes |
| Q19 | - |  |  | SI | Diarrea |
| Q20 | - |  |  | SI | Incontinencia Fecal |
| Q21 | - |  |  | SI | Ocacional |
| Q22 | - |  |  | SI | Permanente |
| Q23 | - |  |  | SI | Ostomia |
| Q24 | - |  |  | SI | Drenajes |
| Q25 | - |  |  | SI | Detalle |
| Q26 | - |  |  | SI | Asp. Gastrica |
| Q27 | - |  |  | SI | Pañal |
| Q28 | - |  |  | SI | Diagnóstico 1 |
| Q29 | - |  |  | SI | Diagnóstico 2 |
| Q30 | - |  |  | SI | Conclusión |
| Q31 | - |  |  | SI | Eliminación |
| Q32 | - |  |  | SI | Descripción Parcial |
| Q33 | - |  |  | SI | Detalle Aps.Gástrica |
| Q34 | - |  |  | SI | Detalle Pañal |
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