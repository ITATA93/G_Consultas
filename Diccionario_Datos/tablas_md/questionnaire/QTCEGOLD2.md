# questionnaire.QTCEGOLD2

> Escala de Goldberg

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Goldberg

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. ¿ Se ha sentido muy excitado, nervioso o en ten... |
| Q02 | varchar |  |  | SI | 2. ¿Ha estado muy preocupado por algo? |
| Q03 | varchar |  |  | SI | 3. ¿Se ha sentido muy irritable? |
| Q04 | varchar |  |  | SI | 4. ¿Ha tenido dificultad para relajarse? |
| Q05 | varchar |  |  | SI | 5. ¿Ha dormido mal, ha tenido dificultades para do... |
| Q06 | varchar |  |  | SI | 6. ¿Ha tenido dolores de cabeza o nuca? |
| Q07 | varchar |  |  | SI | 7. ¿Ha tenido alguno de los siguientes síntomas: t... |
| Q08 | varchar |  |  | SI | 8. ¿Ha estado preocupado por su salud? |
| Q09 | varchar |  |  | SI | 9. ¿Ha tenido alguna dificultad para conciliar el ... |
| Q10 | varchar |  |  | SI | 1. ¿Se ha sentido con poca energía? |
| Q11 | varchar |  |  | SI | 2. ¿Ha perdido usted su interés por las cosas? |
| Q12 | varchar |  |  | SI | 3. ¿Ha perdido la confianza en sí mismo? |
| Q13 | varchar |  |  | SI | 4. ¿Se ha sentido usted desesperanzado, sin espera... |
| Q14 | varchar |  |  | SI | 5 ¿Ha tenido dificultades para concentrarse? |
| Q15 | varchar |  |  | SI | 6 ¿Ha perdido peso? (a causa de su falta de apetit... |
| Q16 | varchar |  |  | SI | 7 ¿Se ha estado despertando demasiado temprano? |
| Q17 | varchar |  |  | SI | 8 ¿Se ha sentido usted enlentecido? |
| Q18 | varchar |  |  | SI | 9 ¿Cree usted que ha tenido tendencia a encontrars... |
| Q19 | varchar |  |  | SI | Puntaje Subescala de Ansiedad |
| Q20 | varchar |  |  | SI | Puntaje Subescala de Depresión |
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