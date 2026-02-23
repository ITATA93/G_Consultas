# questionnaire.QTCEMIAB

> Minimental Abreviado

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Minimental Abreviado

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Mes |
| Q10 | varchar |  |  | SI | Arbol |
| Q11 | varchar |  |  | SI | Mesa |
| Q12 | varchar |  |  | SI | Avión |
| Q14 | varchar |  |  | SI | 1 |
| Q15 | varchar |  |  | SI | 3 |
| Q16 | varchar |  |  | SI | 5 |
| Q17 | varchar |  |  | SI | 7 |
| Q18 | varchar |  |  | SI | 9 |
| Q2 | varchar |  |  | SI | Día Mes |
| Q20 | varchar |  |  | SI | Toma el papel con la mano derecha |
| Q21 | varchar |  |  | SI | Dobla por la mitad con ambas manos |
| Q22 | varchar |  |  | SI | Coloca sobre las piernas |
| Q24 | varchar |  |  | SI | Árbol |
| Q29 | varchar |  |  | SI | Resultado de MSSE |
| Q29ObsDR | varchar |  | FK | SI | Resultado de MSSE DR |
| Q3 | varchar |  |  | SI | Año |
| Q30 | numeric |  |  | SI | Número de Repeticiones |
| Q31 | varchar |  |  | SI | Arbol |
| Q32 | varchar |  |  | SI | Mesa |
| Q33 | varchar |  |  | SI | Avión |
| Q34 | varchar |  |  | SI | SubTotal Item 1 |
| Q35 | varchar |  |  | SI | Subtotal Item 2 |
| Q36 | varchar |  |  | SI | Subtotal Item 3 |
| Q37 | varchar |  |  | SI | SubTotal Item 4 |
| Q38 | varchar |  |  | SI | SubTotal Item 5 |
| Q39 | varchar |  |  | SI | SubTotal Item 6 |
| Q4 | varchar |  |  | SI | Día Semana |
| Q40 | date |  |  | SI | Fecha Vigencia |
| Q41 | varchar |  |  | SI | 1. Por favor dígame la fecha de hoy |
| Q42 | varchar |  |  | SI | 2. Ahora le voy a nombrar tres objetos. Después qu... |
| Q43 | varchar |  |  | SI | ¿Tiene alguna pregunta que hacerme? |
| Q44 | varchar |  |  | SI | 3. Ahora voy a decirle unos números y quiero que m... |
| Q45 | varchar |  |  | SI | 4. Le voy a dar un papel; tómelo con su mano derec... |
| Q46 | varchar |  |  | SI | 5. Hace un momento le leí una serie de 3 palabras ... |
| Q47 | varchar |  |  | SI | 6. Por favor copie este dibujo. |
| Q48 | varchar |  |  | SI | Sondee el mes, el día del mes, el año y el día de ... |
| Q49 | varchar |  |  | SI | Explique bien para que el entrevistado entienda la... |
| Q50 | varchar |  |  | SI | Si para algún objeto, la respuesta no es correcta,... |
| Q51 | varchar |  |  | SI | Anote la respuesta (el número), en el espacio corr... |
| Q52 | varchar |  |  | SI | La puntuación es el número  de dígitos en el orden... |
| Q53 | varchar |  |  | SI | Entréguele el papel y anote un punto por cada acci... |
| Q55 | varchar |  |  | SI | Un punto por cada palabra que recuerde. No importa... |
| Q56 | varchar |  |  | SI | Muestre al entrevistado el dibujo con los círculos... |
| Q57 | varchar |  |  | SI | Objetos mencionados anteriormente. |
| Q58 | varchar |  |  | SI | Recuerde Ingresar Resultado en Forma Manual en Cue... |
| Q8 | varchar |  |  | SI | Objetos mencionados anteriormente |
| Q9 | varchar |  |  | SI | Copie el dibujo |
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