# questionnaire.QCLXXPSC17

> Cuestionario Pediatryc Symptoms Checklist 17 (PSC-17)

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cuestionario Pediatryc Symptoms Checklist 17 (PSC-17)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | DATOS DE IDENTIFICACIÓN |
| Q02 | varchar |  |  | SI | Establecimiento |
| Q03 | varchar |  |  | SI | Tipo de Enseñanza |
| Q04 | varchar |  |  | SI | Curso |
| Q05 | varchar |  |  | SI | Letra Curso |
| Q06 | varchar |  |  | SI | PREGUNTAS ANTECEDENTES FAMILIARES |
| Q07 | varchar |  |  | SI | a. Edad de la madre al nacer el niño o niña |
| Q08 | varchar |  |  | SI | b. Actualmente, ¿vive con su mamá y su papá? |
| Q09 | varchar |  |  | SI | c. El niño o niña tiene una enfermedad que necesit... |
| Q10 | varchar |  |  | SI | d. Algún familiar que vive con el niño o niña ha s... |
| Q11 | varchar |  |  | SI | e. La familia participa habitualmente en las activ... |
| Q12 | varchar |  |  | SI | CUESTIONARIO DE CONDUCTAS |
| Q13 | varchar |  |  | SI | 1.&nbsp;Es inquieto (a) |
| Q14 | varchar |  |  | SI | 2.&nbsp;Se siente triste |
| Q15 | varchar |  |  | SI | 3.&nbsp;Sueña despierto/ está en su propio mundo |
| Q16 | varchar |  |  | SI | 4.&nbsp;Es egoísta |
| Q17 | varchar |  |  | SI | 5.&nbsp;No comprende los sentimientos de otros |
| Q18 | varchar |  |  | SI | 6. Se siente pesimista / piensa que las cosas son ... |
| Q19 | varchar |  |  | SI | 7. Le cuesta concentrarse |
| Q20 | varchar |  |  | SI | 8. Pelea con otros/as compañeros/as |
| Q21 | varchar |  |  | SI | 9. Se siente poca cosa |
| Q22 | varchar |  |  | SI | 10.&nbsp;Culpa a otros por sus problemas |
| Q23 | varchar |  |  | SI | 11.&nbsp;Se aburre |
| Q24 | varchar |  |  | SI | 12.&nbsp;Ignora las órdenes que le dan |
| Q25 | varchar |  |  | SI | 13.&nbsp;Le cuesta estar tranquilo |
| Q26 | varchar |  |  | SI | 14.&nbsp;Molesta a los demás |
| Q27 | varchar |  |  | SI | 15.&nbsp;Se preocupa mucho |
| Q28 | varchar |  |  | SI | 16.&nbsp;Toma cosas ajenas |
| Q29 | varchar |  |  | SI | 17.&nbsp;Se distrae fácilmente |
| Q30 | varchar |  |  | SI | Subescala Problemas de Atención (PA) |
| Q31 | varchar |  |  | SI | &gt;14 Indica riesgo asociado a Problemas de Atenc... |
| Q32 | varchar |  |  | SI | Subescala Problemas Internalizantes (PI) |
| Q33 | varchar |  |  | SI | &gt;12 Indica riesgo asociado a Problemas Internal... |
| Q34 | varchar |  |  | SI | Subescala Problemas Externalizantes (PE) |
| Q35 | varchar |  |  | SI | &gt;15 Indica riesgo asociado a Problemas External... |
| Q36 | varchar |  |  | SI | Dificultades internalizantes |
| Q37 | varchar |  |  | SI | A mayor puntaje, mayores dificultades internalizan... |
| Q38 | varchar |  |  | SI | Dificultades externalizantes |
| Q39 | varchar |  |  | SI | A mayor puntaje, mayores dificultades externalizan... |
| Q40 | varchar |  |  | SI | Dificultades de atención |
| Q41 | varchar |  |  | SI | A mayor puntaje, mayores dificultades de atención,... |
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