# questionnaire.QTCENIAP

> Notificación de Caso Sospechoso de Intoxicación Aguda por Plaguicida

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notificación de Caso Sospechoso de Intoxicación Aguda por Plaguicida

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Notificación |
| Q02 | varchar |  |  | SI | N° Correlativo del Caso |
| Q03 | numeric |  |  | SI | N° Caso |
| Q04 | varchar |  |  | SI | Lugar de Ocurrencia de la Intoxicación |
| Q05 | varchar |  |  | SI | Otro |
| Q06 | varchar |  |  | SI | Nombre |
| Q07 | varchar |  |  | SI | C |
| Q08 | varchar |  |  | SI | Dirección |
| Q09 | varchar |  |  | SI | Comuna |
| Q10 | varchar |  |  | SI | Localidad |
| Q11 | numeric |  |  | SI | Fono |
| Q12 | varchar |  |  | SI | Nombre del Empleador |
| Q13 | numeric |  |  | SI | Fono |
| Q14 | varchar |  |  | SI | Tipo de Exposición |
| Q15 | varchar |  |  | SI | Actividad al momento de la exposición |
| Q16 | varchar |  |  | SI | Otro |
| Q17 | varchar |  |  | SI | Nombre 1 |
| Q18 | varchar |  |  | SI | Nombre 2 |
| Q19 | bit |  |  | SI | Desconocido |
| Q20 | date |  |  | SI | Fecha primeros síntomas |
| Q21 | time |  |  | SI | Hora |
| Q22 | varchar |  |  | SI | Localizado |
| Q23 | varchar |  |  | SI | Sistémico |
| Q24 | varchar |  |  | SI | Otros |
| Q25 | varchar |  |  | SI | Vía de Exposición |
| Q26 | varchar |  |  | SI | Test de Colinesterasa |
| Q27 | varchar |  |  | SI | Resultado |
| Q28 | varchar |  |  | SI | Test de Colinesterasa 2 |
| Q29 | varchar |  |  | SI | Cuál? |
| Q30 | bit |  |  | SI | No Corresponde |
| Q31 | varchar |  |  | SI | Destino del Intoxicado |
| Q32 | varchar |  |  | SI | Licencia o Reposo Médico |
| Q33 | numeric |  |  | SI | N° Días |
| Q34 | varchar |  |  | SI | Este Caso es parte de un brote |
| Q35 | numeric |  |  | SI | N° Probable de casos |
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