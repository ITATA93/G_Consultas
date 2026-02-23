# SQLUser.AR_HICInHospitalClaimRep

**Schema:** SQLUser
**Columnas:** 56
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IHCR_RowID | bigint | PK |  | NO | - |
| IHCR_InHospitalClaim_DR | bigint |  | FK | SI | The claim the report is for |
| IHCR_PaymentAllocatedFlag | bit |  |  | SI | Payment allocated flag
This flag indicates if a p... |
| IHCR_ReportType | varchar |  |  | SI | Report type
Payment or processing
Standard type:... |
| IHCR_RetrievalDate | date |  |  | SI | Date report retrieved |
| IHCR_RetrievalTime | time |  |  | SI | Time report retrieved |
| IHCR_RetrievalUser_DR | bigint |  | FK | SI | The user that retrieved the report
Blank if retri... |
| IHCR_StatusCode | varchar |  |  | SI | HIC Status Code |
| IHCR_TransactionID | varchar |  |  | SI | Transaction ID
A unique identifier maintained thr... |
| Q01 | - |  |  | SI | Anamnesis Psicosocial |
| Q02 | - |  |  | SI | Conductas Desadaptativas |
| Q03 | - |  |  | SI | Conductas Desadaptativas e Infracción a la Ley (Dr... |
| Q04 | - |  |  | SI | Abordaje Familiar de la Adicción y Estrategias de ... |
| Q05 | - |  |  | SI | Profesional Responsable |
| Q06 | - |  |  | SI | Fecha de Ingreso |
| Q07 | - |  |  | SI | Hora de Ingreso |
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