# questionnaire.QCLXXTOKEN

> Token Test (Reducido)

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Token Test (Reducido)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de Evaluación |
| Q02 | date |  |  | SI | Fecha Evaluación |
| Q03 | varchar |  |  | SI | Evaluador |
| Q04 | varchar |  |  | SI | Puntaje Obtenido Parte I |
| Q05 | varchar |  |  | SI | /24 |
| Q06 | varchar |  |  | SI | Use solamente cuadrados y círculos grandes (6 fich... |
| Q07 | varchar |  |  | SI | Puntaje Obtenido Parte II |
| Q08 | varchar |  |  | SI | /24 |
| Q09 | varchar |  |  | SI | Use cuadrados y círculos grandes y chicos (12 fich... |
| Q10 | varchar |  |  | SI | Puntaje Obtenido Parte III |
| Q11 | varchar |  |  | SI | /24 |
| Q12 | varchar |  |  | SI | Use los cuadrados y círculos grandes (6 fichas) |
| Q13 | varchar |  |  | SI | Puntaje Obtenido Parte IV |
| Q14 | varchar |  |  | SI | /24 |
| Q15 | varchar |  |  | SI | Use cuadrados y círculos grandes y chicos (12 fich... |
| Q16 | varchar |  |  | SI | Parte I (Use solamente cuadrados y círculos grande... |
| Q17 | varchar |  |  | SI | Toque el círculo rojo |
| Q18 | varchar |  |  | SI | Observación |
| Q19 | varchar |  |  | SI | Toque el cuadrado azul |
| Q20 | varchar |  |  | SI | Observación |
| Q21 | varchar |  |  | SI | Toque el cuadrado rojo |
| Q22 | varchar |  |  | SI | Observación |
| Q23 | varchar |  |  | SI | Toque el círculo amarillo |
| Q24 | varchar |  |  | SI | Observación |
| Q25 | varchar |  |  | SI | Toque el círculo azul |
| Q26 | varchar |  |  | SI | Observación |
| Q27 | varchar |  |  | SI | Toque el cuadrado amarillo |
| Q28 | varchar |  |  | SI | Observación |
| Q29 | varchar |  |  | SI | Parte II (Use cuadrados y círculos grandes y chico... |
| Q30 | varchar |  |  | SI | Toque el círculo amarillo chico |
| Q31 | varchar |  |  | SI | Observación |
| Q32 | varchar |  |  | SI | Toque el círculo azul grande |
| Q33 | varchar |  |  | SI | Observación |
| Q34 | varchar |  |  | SI | Toque el círculo amarillo grande |
| Q35 | varchar |  |  | SI | Observación |
| Q36 | varchar |  |  | SI | Toque el cuadrado rojo grande |
| Q37 | varchar |  |  | SI | Observación |
| Q38 | varchar |  |  | SI | Toque el círculo azul chico |
| Q39 | varchar |  |  | SI | Observación |
| Q40 | varchar |  |  | SI | Toque el cuadrado amarillo chico |
| Q41 | varchar |  |  | SI | Observación |
| Q42 | varchar |  |  | SI | Parte III (Use los cuadrados y círculos grandes (6... |
| Q43 | varchar |  |  | SI | Toque el círculo amarillo y el cuadrado azul |
| Q44 | varchar |  |  | SI | Observación |
| Q45 | varchar |  |  | SI | Toque el cuadrado azul y el cuadrado amarillo |
| Q46 | varchar |  |  | SI | Observación |
| Q47 | varchar |  |  | SI | Toque el cuadrado rojo y el círculo azul |
| Q48 | varchar |  |  | SI | Observación |
| Q49 | varchar |  |  | SI | Toque el círculo rojo y el cuadrado amarillo |
| Q50 | varchar |  |  | SI | Observación |
| Q51 | varchar |  |  | SI | Toque el círculo azul y el cuadrado rojo |
| Q52 | varchar |  |  | SI | Observación |
| Q53 | varchar |  |  | SI | Toque el cuadrado amarillo y el cuadrado rojo |
| Q54 | varchar |  |  | SI | Observación |
| Q55 | varchar |  |  | SI | Parte IV (Use cuadrados y círculos grandes y chico... |
| Q56 | varchar |  |  | SI | Toque el círculo amarillo chico y el cuadrado rojo... |
| Q57 | varchar |  |  | SI | Observación |
| Q58 | varchar |  |  | SI | Toque el cuadrado azul chico y el círculo amarillo... |
| Q59 | varchar |  |  | SI | Observación |
| Q60 | varchar |  |  | SI | Toque el cuadrado azul grande y el cuadrado rojo c... |
| Q61 | varchar |  |  | SI | Observación |
| Q62 | varchar |  |  | SI | Toque el círculo rojo chico y el círculo amarillo ... |
| Q63 | varchar |  |  | SI | Observación |
| Q64 | varchar |  |  | SI | Toque el círculo amarillo grande y el círculo azul... |
| Q65 | varchar |  |  | SI | Observación |
| Q66 | varchar |  |  | SI | Toque el cuadrado rojo grande y el círculo amarill... |
| Q67 | varchar |  |  | SI | Observación |
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