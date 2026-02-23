# questionnaire.QCLXXDISMOT

> Escala de Disfunción Motora

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Disfunción Motora

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Hombro Izquierdo |
| Q02 | varchar |  |  | SI | Hombro Derecho |
| Q03 | varchar |  |  | SI | Codo Izquierdo |
| Q04 | varchar |  |  | SI | Codo Derecho |
| Q05 | varchar |  |  | SI | Muñeca Izquierda |
| Q06 | varchar |  |  | SI | Muñeca Derecha |
| Q07 | varchar |  |  | SI | Dedos Mano Izquierda |
| Q08 | varchar |  |  | SI | Dedos Mano Derecha |
| Q09 | varchar |  |  | SI | Cadera Izquierda |
| Q10 | varchar |  |  | SI | Cadera Derecha |
| Q11 | varchar |  |  | SI | Rodilla izquierda |
| Q12 | varchar |  |  | SI | Rodilla Derecha |
| Q13 | varchar |  |  | SI | Tobillo Izquierdo |
| Q14 | varchar |  |  | SI | Tobillo Derecho |
| Q15 | varchar |  |  | SI | Pie Izquierdo |
| Q16 | varchar |  |  | SI | Pie Derecho |
| Q17 | varchar |  |  | SI | Comentarios |
| Q18 | varchar |  |  | SI | Escala de Disfuncion Motora (Sensibilida) |
| Q19 | varchar |  |  | SI | Resultado |
| Q20 | varchar |  |  | SI | Profesional de Salud |
| Q21 | varchar |  |  | SI | M0: Sin pruebas de contractilidad, espasmo o espas... |
| Q22 | varchar |  |  | SI | M1: Manisfestaciones ligeras de contractilidad; no... |
| Q23 | varchar |  |  | SI | M2: Movimiento en toda su amplitud al suprimir la ... |
| Q24 | varchar |  |  | SI | M3: Arco completo de movimiento contra la acción d... |
| Q25 | varchar |  |  | SI | M4: Arco completo de Movimiento contra la acción d... |
| Q26 | varchar |  |  | SI | M5: Arco completo de movimiento contra la acción d... |
| Q27 | varchar |  |  | SI | 0: Inmovilidad |
| Q28 | varchar |  |  | SI | 1: Vestigios |
| Q29 | varchar |  |  | SI | 2: Malo |
| Q30 | varchar |  |  | SI | 3: Regular |
| Q31 | varchar |  |  | SI | 4: Bueno |
| Q32 | varchar |  |  | SI | 5: Normal |
| Q33 | varchar |  |  | SI | Puntaje |
| Q34 | varchar |  |  | SI | Resultado |
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