# questionnaire.QTCEPFEFFER

> Actividades Funcionales Pfeffer

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Actividades Funcionales Pfeffer

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ1 | varchar |  |  | SI | - |
| CQ12 | varchar |  |  | SI | - |
| CQ13 | varchar |  |  | SI | - |
| CQ2 | varchar |  |  | SI | - |
| CQ3 | varchar |  |  | SI | - |
| CQ4 | varchar |  |  | SI | - |
| CQ5 | varchar |  |  | SI | - |
| CQ6 | varchar |  |  | SI | - |
| CQ7 | varchar |  |  | SI | - |
| CQ8 | varchar |  |  | SI | - |
| CQ9 | varchar |  |  | SI | - |
| Q1 | varchar |  |  | SI | ¿Maneja él/ella su propio dinero? |
| Q10 | varchar |  |  | SI | Resultado |
| Q11 | varchar |  |  | SI | Resultado actividades funcionales Pfeffer |
| Q11ObsDR | varchar |  | FK | SI | Resultado actividades funcionales Pfeffer DR |
| Q12 | varchar |  |  | SI | ¿Es él/ella capaz de recordar compromisos, acontec... |
| Q13 | varchar |  |  | SI | ¿Es él/ella capaz de pasear por el vecindario y en... |
| Q14 | varchar |  |  | SI | El screening es positivo cuando el puntaje es igua... |
| Q15 | varchar |  |  | SI | Recuerde Ingresar Resultado en Forma Manual en Cue... |
| Q2 | varchar |  |  | SI | ¿Es él/ella capaz de comprar ropas solo, cosas par... |
| Q3 | varchar |  |  | SI | ¿Es él/ella capaz de calentar agua para el café o ... |
| Q4 | varchar |  |  | SI | ¿Es él/ella capaz de preparar una comida? |
| Q5 | varchar |  |  | SI | ¿Es él/ella de mantenerse al tanto de los aconteci... |
| Q6 | varchar |  |  | SI | ¿Es él/ella capaz de poner atención y entender y d... |
| Q7 | varchar |  |  | SI | ¿Es él/ella capaz de manejar sus propios medicamen... |
| Q8 | varchar |  |  | SI | ¿Es él/ella capaz de saludar a sus amigos adecuada... |
| Q9 | varchar |  |  | SI | ¿Puede él/ella ser dejado en casa en forma segura? |
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