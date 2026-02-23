# questionnaire.QTCEEFAMA

> Evaluación Funcional del Adulto Mayor (EFAM A)

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Funcional del Adulto Mayor (EFAM A)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ06 | varchar |  |  | SI | - |
| CQ1 | varchar |  |  | SI | - |
| CQ2 | varchar |  |  | SI | - |
| CQ3 | varchar |  |  | SI | - |
| CQ4 | varchar |  |  | SI | - |
| CQ5 | varchar |  |  | SI | - |
| CQ7 | varchar |  |  | SI | - |
| CQ8 | varchar |  |  | SI | - |
| CQ9 | varchar |  |  | SI | - |
| Q06 | varchar |  |  | SI | Aplique Minimental Abreviado |
| Q1 | varchar |  |  | SI | ¿Puede bañarse o ducharse? |
| Q10 | varchar |  |  | SI | Resultado EFAM A |
| Q10ObsDR | varchar |  | FK | SI | Resultado EFAM A DR |
| Q11 | varchar |  |  | SI | Con los brazos extendidos lo máximo posible sobre ... |
| Q12 | varchar |  |  | SI | De pie y derecho, agáchese, tomar un objeto desde ... |
| Q13 | varchar |  |  | SI | MMSE |
| Q14 | varchar |  |  | SI | Con los brazos extendidos lo máximo posible sobre ... |
| Q15 | varchar |  |  | SI | Recuerde Ingresar Resultado en Forma Manual en Cue... |
| Q2 | varchar |  |  | SI | ¿Es Ud, Capaz de manejar su propio dinero? |
| Q3 | varchar |  |  | SI | ¿Puede Ud. tomar sus medicamentos? |
| Q4 | varchar |  |  | SI | ¿Prepara Ud. su comida? |
| Q5 | varchar |  |  | SI | ¿Puede hacer las tareas de la casa? |
| Q7 | varchar |  |  | SI | Escolaridad. Pregunte por los años de escolaridad ... |
| Q8 | varchar |  |  | SI | El adulto mayor de pie intentará tomar un objeto r... |
| Q9 | varchar |  |  | SI | En posición de pie, encuclillese, tome el objeto d... |
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