# SQLUser.LBC_TestSetRevisionMultipleRules

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRMR_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetRevisionDR |
| LBCTSRMR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRMR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRMR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRMR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRMR_RowID | varchar |  |  | NO | - |
| LBCTSRMR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCTSRMR_SortOrder | varchar |  |  | SI | Sort Order |
| Q01 | - |  |  | SI | Solicitud Certificado Nacimiento |
| Q02 | - |  |  | SI | Ingreso al SIGGES |
| Q03 | - |  |  | SI | Resultado HTO (Hematocrito) |
| Q03ObsDR | - |  |  | SI | Resultado HTO (Hematocrito) DR |
| Q04 | - |  |  | SI | Fecha HTO (Hematocrito) |
| Q05 | - |  |  | SI | Periodo HTO (Hematocrito) |
| Q06 | - |  |  | SI | Periodo Fosfatasas Alcalinas |
| Q07 | - |  |  | SI | Resultado Fosfatasas Alcalinas |
| Q07ObsDR | - |  |  | SI | Resultado Fosfatasas Alcalinas DR |
| Q08 | - |  |  | SI | Fecha Fosfatasas Alcalinas |
| Q09 | - |  |  | SI | Resultado Fondo de Ojo |
| Q10 | - |  |  | SI | Resultado Ecocardiograma |
| Q10ObsDR | - |  |  | SI | Resultado Ecocardiograma DR |
| Q11 | - |  |  | SI | Fecha Fondo de Ojo |
| Q12 | - |  |  | SI | Periodo Fondo de Ojo |
| Q13 | - |  |  | SI | Fecha Ecocardiograma |
| Q14 | - |  |  | SI | Periodo Ecocardiograma |
| Q15 | - |  |  | SI | Resultado Ecografía Cerebral |
| Q15ObsDR | - |  |  | SI | Resultado Ecografía Cerebral DR |
| Q16 | - |  |  | SI | Fecha Ecografía Cerebral |
| Q17 | - |  |  | SI | Periodo de Ecografía Cerebral |
| Q18 | - |  |  | SI | Estudio Auditivo |
| Q19 | - |  |  | SI | Fecha Estudio Auditivo |
| Q20 | - |  |  | SI | Emisiones OA Oido Derecho |
| Q21 | - |  |  | SI | Emisiones OA Oido Izquierdo |
| Q22 | - |  |  | SI | Potenciales Oido Izquierdo |
| Q23 | - |  |  | SI | Potenciales Oido Derecho |
| Q24 | - |  |  | SI | Entrega Formulario de Leche |
| Q25 | - |  |  | SI | Fecha Citación Poli Seguimiento |
| Q26 | - |  |  | SI | Resultado del Fondo de Ojo |
| Q27 | - |  |  | SI | Leyes Vigentes Pcte Prematuro |
| Q28 | - |  |  | SI | Comentario 01 |
| Q29 | - |  |  | SI | Comentario 02 |
| Q30 | - |  |  | SI | Comentario 12 |
| Q31 | - |  |  | SI | Información Complementaria al Alta	 |
| Q32 | - |  |  | SI | Comentario 05 |
| Q33 | - |  |  | SI | Periodo Fosfatasas Alcalinas |
| Q34 | - |  |  | SI | Comentario 14 |
| Q35 | - |  |  | SI | Comentario 17 |
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