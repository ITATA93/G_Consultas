# SQLUser.MRC_ClinPathOutcome

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLPO_RowId | bigint | PK |  | NO | - |
| CLPO_Code | varchar |  |  | NO | Code |
| CLPO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLPO_CreatedDate | date |  |  | SI | Created Date |
| CLPO_CreatedTime | time |  |  | SI | Created Time |
| CLPO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLPO_DateFrom | date |  |  | SI | Date From |
| CLPO_DateTo | date |  |  | SI | Date To |
| CLPO_Desc | varchar |  |  | NO | Description |
| CLPO_Owner | varchar |  |  | SI | Owner |
| CLPO_UpdatedDate | date |  |  | SI | Updated Date |
| CLPO_UpdatedTime | time |  |  | SI | Updated Time |
| CLPO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Mes |
| Q10 | - |  |  | SI | Arbol |
| Q11 | - |  |  | SI | Mesa |
| Q12 | - |  |  | SI | Avión |
| Q14 | - |  |  | SI | 1 |
| Q15 | - |  |  | SI | 3 |
| Q16 | - |  |  | SI | 5 |
| Q17 | - |  |  | SI | 7 |
| Q18 | - |  |  | SI | 9 |
| Q2 | - |  |  | SI | Día Mes |
| Q20 | - |  |  | SI | Toma el papel con la mano derecha |
| Q21 | - |  |  | SI | Dobla por la mitad con ambas manos |
| Q22 | - |  |  | SI | Coloca sobre las piernas |
| Q24 | - |  |  | SI | Árbol |
| Q29 | - |  |  | SI | Resultado de MSSE |
| Q29ObsDR | - |  |  | SI | Resultado de MSSE DR |
| Q3 | - |  |  | SI | Año |
| Q30 | - |  |  | SI | Número de Repeticiones |
| Q31 | - |  |  | SI | Arbol |
| Q32 | - |  |  | SI | Mesa |
| Q33 | - |  |  | SI | Avión |
| Q34 | - |  |  | SI | SubTotal Item 1 |
| Q35 | - |  |  | SI | Subtotal Item 2 |
| Q36 | - |  |  | SI | Subtotal Item 3 |
| Q37 | - |  |  | SI | SubTotal Item 4 |
| Q38 | - |  |  | SI | SubTotal Item 5 |
| Q39 | - |  |  | SI | SubTotal Item 6 |
| Q4 | - |  |  | SI | Día Semana |
| Q40 | - |  |  | SI | Fecha Vigencia |
| Q41 | - |  |  | SI | 1. Por favor dígame la fecha de hoy |
| Q42 | - |  |  | SI | 2. Ahora le voy a nombrar tres objetos. Después qu... |
| Q43 | - |  |  | SI | ¿Tiene alguna pregunta que hacerme? |
| Q44 | - |  |  | SI | 3. Ahora voy a decirle unos números y quiero que m... |
| Q45 | - |  |  | SI | 4. Le voy a dar un papel |
| Q46 | - |  |  | SI | 5. Hace un momento le leí una serie de 3 palabras ... |
| Q47 | - |  |  | SI | 6. Por favor copie este dibujo. |
| Q48 | - |  |  | SI | Sondee el mes, el día del mes, el año y el día de ... |
| Q49 | - |  |  | SI | Explique bien para que el entrevistado entienda la... |
| Q50 | - |  |  | SI | Si para algún objeto, la respuesta no es correcta,... |
| Q51 | - |  |  | SI | Anote la respuesta (el número), en el espacio corr... |
| Q52 | - |  |  | SI | La puntuación es el número  de dígitos en el orden... |
| Q53 | - |  |  | SI | Entréguele el papel y anote un punto por cada acci... |
| Q55 | - |  |  | SI | Un punto por cada palabra que recuerde. No importa... |
| Q56 | - |  |  | SI | Muestre al entrevistado el dibujo con los círculos... |
| Q57 | - |  |  | SI | Objetos mencionados anteriormente. |
| Q58 | - |  |  | SI | Recuerde Ingresar Resultado en Forma Manual en Cue... |
| Q8 | - |  |  | SI | Objetos mencionados anteriormente |
| Q9 | - |  |  | SI | Copie el dibujo |
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