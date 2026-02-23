# questionnaire.QTCEPSICOAB

> Evaluación Psicosocial Abreviada (EPSA)

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Psicosocial Abreviada (EPSA)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ11 | varchar |  |  | SI | - |
| Q11 | varchar |  |  | SI | Hay algún otro factor que deba ser considerado |
| Q12 | varchar |  |  | SI | ¿Ha pensado en interrumpir la gestación? o ¿Prefer... |
| Q13 | varchar |  |  | SI | Marque SI, si pensó en interrumpir o aún se siente... |
| Q14 | varchar |  |  | SI | (pareja, familia u otro que acompañe en el proceso... |
| Q15 | varchar |  |  | SI | ¿Se siente insatisfecha con el apoyo recibido de l... |
| Q16 | varchar |  |  | SI | Marque SI, si se siente insatisfecha |
| Q17 | varchar |  |  | SI | a. ¿Se ha sentido cansada(o) o decaída(o) casi tod... |
| Q18 | varchar |  |  | SI | b. ¿Se ha sentido triste o deprimida(o) o pesimist... |
| Q19 | varchar |  |  | SI | c. ¿Siente que ya no disfruta o ha perdido interés... |
| Q20 | varchar |  |  | SI | Marque SI, s i una o más respuestas son afirmativa... |
| Q21 | varchar |  |  | SI | ¿Ha consumido durante este embarazo alguna de esta... |
| Q22 | varchar |  |  | SI | a) Cigarrillo |
| Q23 | varchar |  |  | SI | b) Cerveza, vino, trago fuerte u otras bebidas con... |
| Q24 | varchar |  |  | SI | c) Tranquilizante sin receta médica |
| Q25 | varchar |  |  | SI | d) Marihuana, coca, pasta base, anfetamina u otra ... |
| Q26 | varchar |  |  | SI | Marque SI, si ha consumido cualquiera de estas sus... |
| Q27 | varchar |  |  | SI | a. ¿Alguien la ha insultado, humillado o amenazado... |
| Q28 | varchar |  |  | SI | b. ¿Alguien la ha golpeado o empujado? VIOLENCIA F... |
| Q29 | varchar |  |  | SI | c. ¿Este embarazo es consecuencia de una relación ... |
| Q30 | varchar |  |  | SI | Marque SI, si le ha sucedido cualquiera de estas m... |
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
| Qa1 | varchar |  |  | SI | Ingreso posterior a las 20 semanas |
| Qa2 | varchar |  |  | SI | Escolaridad <= 6º básico |
| Qa3 | varchar |  |  | SI | Edad <= a 17 años |
| Qps1 | varchar |  |  | SI | Rechazo al embarazo |
| Qps2 | varchar |  |  | SI | Insuficiente apoyo social familiar |
| Qps3 | varchar |  |  | SI | Síntomas depresivos |
| Qps4 | varchar |  |  | SI | Uso o abuso de sustancias |
| Qps5 | varchar |  |  | SI | Violencia de género - pareja o una figura masculin... |
| Qps6 | varchar |  |  | SI | Describa |
| Qqr | varchar |  |  | SI | Riesgo Psicosocial Abreviado |
| QqrObsDR | varchar |  | FK | SI | Riesgo Psicosocial Abreviado DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*