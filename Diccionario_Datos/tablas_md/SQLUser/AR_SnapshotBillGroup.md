# SQLUser.AR_SnapshotBillGroup

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BGRP_ParRef | bigint | PK |  | NO | AR_SnapshotBill Parent Reference |
| BGRP_AAServiceTotal | double |  |  | SI | Authorised Allowed Service Total |
| BGRP_AATotal | double |  |  | SI | Author Allowed Total |
| BGRP_ADServiceTotal | double |  |  | SI | Authorised Disalllowed Service Total |
| BGRP_ADTotal | double |  |  | SI | Author Disallowed Total |
| BGRP_BillGroup_DR | varchar |  | FK | NO | Des Ref to BillSubGroup |
| BGRP_Childsub | double |  |  | NO | Childsub |
| BGRP_RowId | varchar |  |  | NO | - |
| BGRP_SpecSurcharge | double |  |  | SI | Specialist Surcharge |
| ChildQ16DR | - |  |  | SI | Child Reference: Procedimientos Secundarios |
| Q01 | - |  |  | SI | Se verifica identificación del paciente |
| Q02 | - |  |  | SI | Se verifica alergias del paciente |
| Q03 | - |  |  | SI | Consentimiento informado firmado y completo |
| Q04 | - |  |  | SI | Paciente correctamente preparado |
| Q05 | - |  |  | SI | Paciente apto para el procedimiento según protocol... |
| Q06 | - |  |  | SI | Paciente conectado a monitor multiparámetro |
| Q07 | - |  |  | SI | Paciente en posición correcta y segura |
| Q08 | - |  |  | SI | Vía venosa fija y permeable |
| Q09 | - |  |  | SI | Se verifica con el médico procedimiento y exámenes... |
| Q10 | - |  |  | SI | Se dispone del material necesario para realizar el... |
| Q11 | - |  |  | SI | Funcionamiento adecuado de aspiración, aire, irrig... |
| Q12 | - |  |  | SI | Responsable |
| Q13 | - |  |  | SI | Cirugía/Procedimiento |
| Q14 | - |  |  | SI | Lateralidad |
| Q15 | - |  |  | SI | Detalle Lateralidad |
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