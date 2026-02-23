# questionnaire.QTCWAT1

> Withdrawal Assessment Tool

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Withdrawal Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha destete |
| Q02 | time |  |  | SI | Hora destete |
| Q03 | varchar |  |  | SI | ¿Heces blandas y acuosas? |
| Q04 | varchar |  |  | SI | ¿Vómitos / arcadas / náuseas? |
| Q05 | varchar |  |  | SI | ¿Temperatura sobre 37,8? |
| Q06 | varchar |  |  | SI | Estado |
| Q07 | varchar |  |  | SI | Temblor |
| Q08 | varchar |  |  | SI | Cualquier sudoración |
| Q09 | varchar |  |  | SI | Movimientos anormales o repetitivos |
| Q10 | varchar |  |  | SI | Bostezos o estornudos |
| Q11 | varchar |  |  | SI | Sobresalto al tocar |
| Q12 | varchar |  |  | SI | Tono muscular |
| Q13 | varchar |  |  | SI | Tiempo hasta que se calma (SBS* igual o menor a 1) |
| Q14 | varchar |  |  | SI | Inicie la puntuación WAT-1 desde el primer día del... |
| Q15 | varchar |  |  | SI | Continúe anotando dos veces al día hasta 72 horas ... |
| Q16 | varchar |  |  | SI | WAT-1 debe completarse en conjunto con SBS * al me... |
| Q17 | varchar |  |  | SI | El estímulo progresivo utilizado en la evaluación ... |
| Q18 | varchar |  |  | SI | Obtenga información del registro del paciente (est... |
| Q19 | varchar |  |  | SI | Heces blandas / acuosas: Puntúe 1 si se documentar... |
| Q20 | varchar |  |  | SI | Vómitos / arcadas / náuseas: Puntuación 1 si se do... |
| Q21 | varchar |  |  | SI | Temperatura> 37,8 ° C: puntuación 1 si la temperat... |
| Q22 | varchar |  |  | SI | Observaciones 2 minutos pre estimulación:  |
| Q23 | varchar |  |  | SI | Estado: Puntúe 1 si está despierto y se observa an... |
| Q24 | varchar |  |  | SI | Temblor: Puntúe 1 si se observa un temblor de mode... |
| Q25 | varchar |  |  | SI | Sudoración: Puntúe 1 si hay sudoración durante los... |
| Q26 | varchar |  |  | SI | Movimientos anormales o repetitivos: Puntúe 1 si s... |
| Q27 | varchar |  |  | SI | agitar las piernas o los brazos o arquear el torso... |
| Q28 | varchar |  |  | SI | Bostezos o estornudo s> 1: Puntuación 1 si se obse... |
| Q29 | varchar |  |  | SI | Observaciones 1 minuto post estimulación:  |
| Q30 | varchar |  |  | SI | Sobresalto al tocar: Puntúe 1 si se produce un sob... |
| Q31 | varchar |  |  | SI | Tono muscular: Puntúe 1 si el tono aumentó durante... |
| Q32 | varchar |  |  | SI | Recuperación posterior al estímulo:  |
| Q33 | varchar |  |  | SI | Tiempo para recuperar el estado de calma (SBS1 $ 0... |
| Q34 | varchar |  |  | SI | Sume los 11 números de la columna para obtener el ... |
| Q35 | varchar |  |  | SI | *= State Behavioural Scale |
| Q36 | varchar |  |  | SI | Puntaje |
| Q37 | varchar |  |  | SI | Clasificación |
| Q38 | varchar |  |  | SI | 0 - 12 |
| Q39 | varchar |  |  | SI | Una puntuación WAT-1 más alta indica más síntomas ... |
| Q40 | varchar |  |  | SI | WAT-1 es una escala de 11 ítems / 12 puntos para m... |
| Q41 | varchar |  |  | SI | 0 - 12: Una puntuación WAT-1 más alta indica más s... |
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