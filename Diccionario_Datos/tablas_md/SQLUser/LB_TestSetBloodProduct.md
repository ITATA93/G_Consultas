# SQLUser.LB_TestSetBloodProduct

**Schema:** SQLUser
**Columnas:** 54
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTSBP_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| LBTSBP_ActionStatus | varchar |  |  | SI | Action Status |
| LBTSBP_ActionStatusDate | date |  |  | SI | Date the action Status was updated |
| LBTSBP_ActionStatusTime | time |  |  | SI | Time the action Status was updated |
| LBTSBP_BloodProduct_DR | bigint |  | FK | SI | Blood Product Unit tested by this test set |
| LBTSBP_OverrideReasonComment | varchar |  |  | SI | [DEPRECATED]Move BP-Suitability-Rule-Override deta... |
| LBTSBP_OverrideReason_DR | bigint |  | FK | SI | [DEPRECATED]Move BP-Suitability-Rule-Override deta... |
| LBTSBP_OverrideUser_DR | bigint |  | FK | SI | [DEPRECATED]Move BP-Suitability-Rule-Override deta... |
| LBTSBP_RowID | varchar |  |  | NO | - |
| LBTSBP_Sequence | numeric |  |  | SI | Blood product sequence within the test set |
| QEMEC | - |  |  | SI | Razón Edad Mental vs. Edad Cronológica |
| QMesesEdad | - |  |  | SI | Edad en Meses |
| QPE | - |  |  | SI | Coeficiente de Desarrollo Estándar |
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