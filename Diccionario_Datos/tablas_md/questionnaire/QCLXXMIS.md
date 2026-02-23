# questionnaire.QCLXXMIS

> MIS

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile. *(MIS)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | Responsable de Evaluación |
| Q04 | varchar |  |  | SI | Aplicación de la prueba |
| Q05 | varchar |  |  | SI | Otros Motivos |
| Q06 | varchar |  |  | SI | Lectura : |
| Q07 | varchar |  |  | SI | Caballo |
| Q08 | varchar |  |  | SI | Clavel |
| Q09 | varchar |  |  | SI | Pantalón |
| Q10 | varchar |  |  | SI | Violín |
| Q11 | varchar |  |  | SI | ¿Por qué no aplica? |
| Q12 | varchar |  |  | SI | Total Lectura |
| Q13 | varchar |  |  | SI | Identificación : |
| Q14 | varchar |  |  | SI | Caballo |
| Q15 | varchar |  |  | SI | Clavel |
| Q16 | varchar |  |  | SI | Pantalón |
| Q17 | varchar |  |  | SI | Violín |
| Q18 | varchar |  |  | SI | ¿Por qué no aplica? |
| Q19 | varchar |  |  | SI | Total Identificación |
| Q20 | varchar |  |  | SI | Recuerdo Libre : |
| Q21 | varchar |  |  | SI | Caballo |
| Q22 | varchar |  |  | SI | Clavel |
| Q23 | varchar |  |  | SI | Pantalón |
| Q24 | varchar |  |  | SI | Violín |
| Q25 | varchar |  |  | SI | ¿Por qué no aplica? |
| Q26 | varchar |  |  | SI | Total Recuerdo Libre |
| Q27 | varchar |  |  | SI | Recuerdo con Clave : |
| Q28 | varchar |  |  | SI | ¿Cuál era el animal? (Caballo) |
| Q29 | varchar |  |  | SI | ¿Cuál era la flor? (Clavel) |
| Q30 | varchar |  |  | SI | ¿Cuál era la prenda de vestir?(Pantalón) |
| Q31 | varchar |  |  | SI | ¿Cuál era el instrumentomusical? (Violín) |
| Q32 | varchar |  |  | SI | ¿Por qué no aplica? |
| Q33 | varchar |  |  | SI | Total Recuerdo con Clave |
| Q34 | varchar |  |  | SI | TOTAL MIS |
| Q35 | varchar |  |  | SI | Intrusiones |
| Q36 | varchar |  |  | SI | Observaciones |
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