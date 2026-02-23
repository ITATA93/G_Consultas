# questionnaire.QCLXXCAP15

> CAPE- P15

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile. *(CAPE- P15)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Evaluación |
| Q02 | time |  |  | SI | Hora de Evaluación |
| Q03 | varchar |  |  | SI | 1. ¿Has sentido como si la gente te lanzara indire... |
| Q04 | varchar |  |  | SI | 1. ¿Has sentido como si la gente te lanzara indire... |
| Q05 | varchar |  |  | SI | 2. ¿Has sentido como si algunas personas no son lo... |
| Q06 | varchar |  |  | SI | 2. ¿Has sentido como si algunas personas no son lo... |
| Q07 | varchar |  |  | SI | 3. ¿Has sentido como que te persiguen de alguna ma... |
| Q08 | varchar |  |  | SI | 3. ¿Has sentido como que te persiguen de alguna ma... |
| Q09 | varchar |  |  | SI | 4.¿Has sentido como si hubiera una conspiración en... |
| Q10 | varchar |  |  | SI | 4. ¿Has sentido como si hubiera una conspiración e... |
| Q11 | varchar |  |  | SI | 5.¿Has sentido que la gente te mira extraño debido... |
| Q12 | varchar |  |  | SI | 5. ¿Has sentido que la gente te mira extraño debid... |
| Q13 | varchar |  |  | SI | 6. ¿Has sentido que ciertos artefactos electrónico... |
| Q14 | varchar |  |  | SI | 6. ¿Has sentido que ciertos artefactos electrónico... |
| Q15 | varchar |  |  | SI | 7. ¿Has sentido como si te estuvieran sacando los ... |
| Q16 | varchar |  |  | SI | 7. ¿Has sentido como si te estuvieran sacando los ... |
| Q17 | varchar |  |  | SI | 8.¿Has sentido como si tus pensamientos no fueran ... |
| Q18 | varchar |  |  | SI | 8. ¿Has sentido como si tus pensamientos no fueran... |
| Q19 | varchar |  |  | SI | 9. ¿Has tenido pensamientos tan intensos que te pr... |
| Q20 | varchar |  |  | SI | 9. ¿Has tenido pensamientos tan intensos que te pr... |
| Q21 | varchar |  |  | SI | 10. ¿Sientes como si tus pensamientos se repitiera... |
| Q22 | varchar |  |  | SI | 10. ¿Sientes como si tus pensamientos se repitiera... |
| Q23 | varchar |  |  | SI | 11. ¿Has sentido como si estuvieras bajo el contro... |
| Q24 | varchar |  |  | SI | 11. ¿Has sentido como si estuvieras bajo el contro... |
| Q25 | varchar |  |  | SI | 12. ¿Has sentido como si un doble hubiera tomado e... |
| Q26 | varchar |  |  | SI | 12. ¿Has sentido como si un doble hubiera tomado e... |
| Q27 | varchar |  |  | SI | 13.¿Has escuchado voces cuando estas solo? |
| Q28 | varchar |  |  | SI | 13. ¿Has escuchado voces cuando estas solo? Cuánto... |
| Q29 | varchar |  |  | SI | 14. ¿Has escuchado voces hablando entre sí cuando ... |
| Q30 | varchar |  |  | SI | 14. ¿Has escuchado voces hablando entre sí cuando ... |
| Q31 | varchar |  |  | SI | 15. ¿Has vistos objetos, personas o animales que o... |
| Q32 | varchar |  |  | SI | 15. ¿Has vistos objetos, personas o animales que o... |
| Q33 | numeric |  |  | SI | Promedio de Frecuencia |
| Q34 | numeric |  |  | SI | Promedio de Estrés |
| Q35 | varchar |  |  | SI | Deberá realizarse derivación a Especialidad para e... |
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