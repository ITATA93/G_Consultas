# questionnaire.QTCEEOAP

> Estudio Obligatorio a Prematuro <32 Semanas y/o <1500grs.

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estudio Obligatorio a Prematuro <32 Semanas y/o <1500grs.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Solicitud Certificado Nacimiento |
| Q02 | varchar |  |  | SI | Ingreso al SIGGES |
| Q03 | varchar |  |  | SI | Resultado HTO (Hematocrito) |
| Q03ObsDR | varchar |  | FK | SI | Resultado HTO (Hematocrito) DR |
| Q04 | date |  |  | SI | Fecha HTO (Hematocrito) |
| Q05 | varchar |  |  | SI | Periodo HTO (Hematocrito) |
| Q06 | varchar |  |  | SI | Periodo Fosfatasas Alcalinas |
| Q07 | varchar |  |  | SI | Resultado Fosfatasas Alcalinas |
| Q07ObsDR | varchar |  | FK | SI | Resultado Fosfatasas Alcalinas DR |
| Q08 | date |  |  | SI | Fecha Fosfatasas Alcalinas |
| Q09 | varchar |  |  | SI | Resultado Fondo de Ojo |
| Q10 | varchar |  |  | SI | Resultado Ecocardiograma |
| Q10ObsDR | varchar |  | FK | SI | Resultado Ecocardiograma DR |
| Q11 | date |  |  | SI | Fecha Fondo de Ojo |
| Q12 | varchar |  |  | SI | Periodo Fondo de Ojo |
| Q13 | date |  |  | SI | Fecha Ecocardiograma |
| Q14 | varchar |  |  | SI | Periodo Ecocardiograma |
| Q15 | varchar |  |  | SI | Resultado Ecografía Cerebral |
| Q15ObsDR | varchar |  | FK | SI | Resultado Ecografía Cerebral DR |
| Q16 | date |  |  | SI | Fecha Ecografía Cerebral |
| Q17 | varchar |  |  | SI | Periodo de Ecografía Cerebral |
| Q18 | varchar |  |  | SI | Estudio Auditivo |
| Q19 | date |  |  | SI | Fecha Estudio Auditivo |
| Q20 | varchar |  |  | SI | Emisiones OA Oido Derecho |
| Q21 | varchar |  |  | SI | Emisiones OA Oido Izquierdo |
| Q22 | varchar |  |  | SI | Potenciales Oido Izquierdo |
| Q23 | varchar |  |  | SI | Potenciales Oido Derecho |
| Q24 | varchar |  |  | SI | Entrega Formulario de Leche |
| Q25 | varchar |  |  | SI | Fecha Citación Poli Seguimiento |
| Q26 | varchar |  |  | SI | Resultado del Fondo de Ojo |
| Q27 | varchar |  |  | SI | Leyes Vigentes Pcte Prematuro |
| Q28 | varchar |  |  | SI | Comentario 01 |
| Q29 | varchar |  |  | SI | Comentario 02 |
| Q30 | varchar |  |  | SI | Comentario 12 |
| Q31 | varchar |  |  | SI | Información Complementaria al Alta	 |
| Q32 | varchar |  |  | SI | Comentario 05 |
| Q33 | varchar |  |  | SI | Periodo Fosfatasas Alcalinas |
| Q34 | varchar |  |  | SI | Comentario 14 |
| Q35 | varchar |  |  | SI | Comentario 17 |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*