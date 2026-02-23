# questionnaire.QTCEEDGYESA

> Escala de Depresión Geriátrica de Yesavage

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Depresión Geriátrica de Yesavage

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Esta basicamente satisfecho con su vida |
| Q02 | varchar |  |  | SI | Ha renunciado a muchas de sus actividades e intere... |
| Q03 | varchar |  |  | SI | Siente que su vida esta vacía |
| Q04 | varchar |  |  | SI | Se encuentra a menudo aburrido |
| Q05 | varchar |  |  | SI | Tiene esperanza en el futuro |
| Q06 | varchar |  |  | SI | Sufre molestias por pensamientos que no pueda saca... |
| Q07 | varchar |  |  | SI | Tiene a menudo buen animo |
| Q08 | varchar |  |  | SI | Tiene miedo de que algo le este pasando |
| Q09 | varchar |  |  | SI | Se siente feliz muchas veces |
| Q10 | varchar |  |  | SI | Se siente a menudo abandonado |
| Q11 | varchar |  |  | SI | Esta a menudo intranquilo e inquieto |
| Q12 | varchar |  |  | SI | Prefiere quedarse en casa que acaso salir y hacer ... |
| Q13 | varchar |  |  | SI | Frecuentemente està preocupado por el futuro |
| Q14 | varchar |  |  | SI | Encuentra que tiene mas problemas de memoria que l... |
| Q15 | varchar |  |  | SI | Piensa que es maravilloso vivir |
| Q16 | varchar |  |  | SI | Se siente a menudo desanimado y melancòlico |
| Q17 | varchar |  |  | SI | Se siente bastante inùtil en el medio en que està |
| Q18 | varchar |  |  | SI | Està muy preocupado por el pasado |
| Q19 | varchar |  |  | SI | Encuentra la vida muy estimulante |
| Q20 | varchar |  |  | SI | Es difìcil para usted poner en marcha nuevos proye... |
| Q21 | varchar |  |  | SI | Se siente lleno de energia |
| Q22 | varchar |  |  | SI | Siente que su situacion es desesperada |
| Q23 | varchar |  |  | SI | Cree que mucha gente esta mejor que usted |
| Q24 | varchar |  |  | SI | Frecuentemente esta preocupado por pequeñas cosas |
| Q25 | varchar |  |  | SI | Frecuentemente siente ganas de llorar |
| Q26 | varchar |  |  | SI | Tiene problemas para concentrarse |
| Q27 | varchar |  |  | SI | Se siente mejor por la mañana al levantarse |
| Q28 | varchar |  |  | SI | Prefiere evitar reuniones sociales |
| Q29 | varchar |  |  | SI | Es fàcil para usted tomar decisiones |
| Q30 | varchar |  |  | SI | Su mente esta tan clara como lo acostumbraba a est... |
| Q31 | varchar |  |  | SI | Puntaje Total Escala  |
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