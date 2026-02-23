# SQLUser.AR_CloseShiftReceipt

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REC_ParRef | bigint | PK |  | NO | AR_CloseShift Parent Reference |
| ChildQ26DR | - |  |  | SI | Child Reference: Localización y Profundidad de la/... |
| Q01 | - |  |  | SI | Fecha Accidente |
| Q02 | - |  |  | SI | Hora Accidente |
| Q03 | - |  |  | SI | Fecha de Atención |
| Q04 | - |  |  | SI | Hora de Atención |
| Q05 | - |  |  | SI | Nombre de Acompañante |
| Q06 | - |  |  | SI | Parentesco |
| Q07 | - |  |  | SI | Lugar del accidente |
| Q08 | - |  |  | SI | Circunstancias del accidente |
| Q09 | - |  |  | SI | Accidente presenciado&nbsp |
| Q10 | - |  |  | SI | Observaciones&nbsp |
| Q11 | - |  |  | SI | Agente Causal de la quemadura |
| Q12 | - |  |  | SI | Mecanismo de Acción |
| Q13 | - |  |  | SI | Lesiones Concomitantes |
| Q14 | - |  |  | SI | Tiempo de Evolución |
| Q15 | - |  |  | SI | Primera atención |
| Q16 | - |  |  | SI | Tratamiento en Casa |
| Q17 | - |  |  | SI | Otorgada por |
| Q18 | - |  |  | SI | Observaciones de primera atención |
| Q19 | - |  |  | SI | Extensión de la/las Quemadura |
| Q20 | - |  |  | SI | Superficie de la Palma (%) |
| Q21 | - |  |  | SI | Observaciones |
| Q22 | - |  |  | SI | Wallace (9%)&nbsp |
| Q23 | - |  |  | SI | Observaciones |
| Q24 | - |  |  | SI | Tabla de Lund y Browde (niños) (%) |
| Q25 | - |  |  | SI | Observaciones |
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
| REC_ARREC_DR | bigint |  | FK | SI | Des Ref ARREC |
| REC_ARRPM_DR | varchar |  | FK | SI | Des Ref ARRPM |
| REC_CardAmt | double |  |  | SI | CardAmt |
| REC_CashAmt | double |  |  | SI | Cash Amt |
| REC_ChequeAmt | double |  |  | SI | ChequeAmt |
| REC_Childsub | double |  |  | NO | Childsub |
| REC_DirectPaymentAmt | double |  |  | SI | Direct Payment Amt |
| REC_RowId | varchar |  |  | NO | - |
| REC_TransType | varchar |  |  | SI | TransType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*