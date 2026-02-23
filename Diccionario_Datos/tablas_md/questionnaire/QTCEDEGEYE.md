# questionnaire.QTCEDEGEYE

> Depresión Geriátrica Yesavage

**Schema:** questionnaire
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Depresión Geriátrica Yesavage

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | ¿Se considera satisfecho de su vida? |
| Q10 | varchar |  |  | SI | ¿Siente que tiene más problemas con su memoria que... |
| Q11 | varchar |  |  | SI | ¿Piensa que es maravilloso estar vivo? |
| Q12 | varchar |  |  | SI | ¿Se siente muy inútil como está en este momento? |
| Q13 | varchar |  |  | SI | ¿Se siente lleno de energías? |
| Q14 | varchar |  |  | SI | ¿Siente su situación como sin esperanzas? |
| Q15 | varchar |  |  | SI | ¿Cree que la mayoría está mejor que usted? |
| Q17 | varchar |  |  | SI | Resultado de Escala de Depresión Geriátrica |
| Q17ObsDR | varchar |  | FK | SI | Resultado de Escala de Depresión Geriátrica DR |
| Q2 | varchar |  |  | SI | ¿Ha ido abandonando muchas de sus actividades e in... |
| Q3 | varchar |  |  | SI | ¿Se aburre a menudo? |
| Q4 | varchar |  |  | SI | ¿Siente que su vida está vacía? |
| Q5 | varchar |  |  | SI | ¿Está de buen ánimo la mayor parte del tiempo? |
| Q6 | varchar |  |  | SI | ¿Tiene miedo que le pueda ocurrir algo malo? |
| Q7 | varchar |  |  | SI | ¿Está contento la mayor parte del tiempo? |
| Q8 | varchar |  |  | SI | ¿Se siente a menudo desvalido? |
| Q9 | varchar |  |  | SI | ¿Prefiere quedarse en casa en vez de hacer otras c... |
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