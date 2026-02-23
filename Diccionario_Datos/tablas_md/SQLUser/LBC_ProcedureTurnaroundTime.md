# SQLUser.LBC_ProcedureTurnaroundTime

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPRTT_ParRef | bigint | PK |  | NO | Parent Reference to procedure |
| LBCPRTT_AlertTurnaroundTime | integer |  |  | SI | Alert Turnaround Time (minutes)  |
| LBCPRTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPRTT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPRTT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPRTT_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCPRTT_MaxOutlierTime | integer |  |  | SI | Max Outlier Time  (minutes) |
| LBCPRTT_Priority_DR | bigint |  | FK | SI | Priority |
| LBCPRTT_RowID | varchar |  |  | NO | - |
| LBCPRTT_TargetTurnaroundTime | integer |  |  | SI | Target Turnaround Time (minutes) |
| Q01 | - |  |  | SI | Consentimiento informado |
| Q02 | - |  |  | SI | Consentimiento para toma de muestra |
| Q03 | - |  |  | SI | Indicaciones de preingreso orales y escritas |
| Q04 | - |  |  | SI | Preanestesia |
| Q05 | - |  |  | SI | ASA |
| Q06 | - |  |  | SI | Día |
| Q07 | - |  |  | SI | Requiere preparación de colon hospitalaria: Poliet... |
| Q08 | - |  |  | SI | Requiere cama en intermedio |
| Q09 | - |  |  | SI | Características de interés (ej: obesidad, sintrón.... |
| Q10 | - |  |  | SI | Tipo de cáncer (AP y grado de diferenciación) |
| Q11 | - |  |  | SI | Estadío de la FIGO |
| Q12 | - |  |  | SI | Planteamiento quirúrgico |
| Q13 | - |  |  | SI | Otras observaciones |
| Q14 | - |  |  | SI | Profesional |
| Q15 | - |  |  | SI | Fecha |
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