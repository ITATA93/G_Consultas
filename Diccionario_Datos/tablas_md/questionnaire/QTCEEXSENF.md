# questionnaire.QTCEEXSENF

> Examen Segmentario

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Segmentario

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo Examen Físico |
| Q02 | varchar |  |  | SI | Estado General |
| Q03 | varchar |  |  | SI | Estado Psíquico |
| Q04 | varchar |  |  | SI | Otro Estado Psíquico |
| Q05 | varchar |  |  | SI | Conciencia |
| Q05ObsDR | varchar |  | FK | SI | Conciencia DR |
| Q06 | varchar |  |  | SI | Piel |
| Q06ObsDR | varchar |  | FK | SI | Piel DR |
| Q07 | varchar |  |  | SI | Mucosas |
| Q07ObsDR | varchar |  | FK | SI | Mucosas DR |
| Q08 | varchar |  |  | SI | Cabeza - Cara |
| Q08ObsDR | varchar |  | FK | SI | Cabeza - Cara DR |
| Q09 | varchar |  |  | SI | Pupilas |
| Q09ObsDR | varchar |  | FK | SI | Pupilas DR |
| Q10 | varchar |  |  | SI | Conjuntivas |
| Q10ObsDR | varchar |  | FK | SI | Conjuntivas DR |
| Q11 | varchar |  |  | SI | Dentadura |
| Q11ObsDR | varchar |  | FK | SI | Dentadura DR |
| Q12 | varchar |  |  | SI | Lenguaje |
| Q13 | varchar |  |  | SI | Cuello |
| Q13ObsDR | varchar |  | FK | SI | Cuello DR |
| Q14 | varchar |  |  | SI | Vía Aérea |
| Q14ObsDR | varchar |  | FK | SI | Vía Aérea DR |
| Q15 | varchar |  |  | SI | Respiración |
| Q16 | varchar |  |  | SI | Tórax |
| Q16ObsDR | varchar |  | FK | SI | Tórax DR |
| Q17 | varchar |  |  | SI | Extremidades Superiores |
| Q17ObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q18 | varchar |  |  | SI | Abdomen |
| Q18ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q19 | varchar |  |  | SI | Genito-Urinario |
| Q19ObsDR | varchar |  | FK | SI | Genito-Urinario DR |
| Q20 | varchar |  |  | SI | Extremidades Inferiores |
| Q20ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q21 | varchar |  |  | SI | Edema |
| Q21ObsDR | varchar |  | FK | SI | Edema DR |
| Q22 | varchar |  |  | SI | Comentario 1 |
| Q23 | varchar |  |  | SI | Comentario 2 |
| Q24 | varchar |  |  | SI | Comentario 3 |
| Q25 | varchar |  |  | SI | Comentario 4 |
| Q26 | varchar |  |  | SI | Comentario 5 |
| Q27 | varchar |  |  | SI | Comentario 6 |
| Q28 | varchar |  |  | SI | Comentario 7 |
| Q29 | varchar |  |  | SI | Comentario 8 |
| Q30 | varchar |  |  | SI | Comentario 9 |
| Q31 | varchar |  |  | SI | Comentario 10 |
| Q32 | varchar |  |  | SI | Comentario 11 |
| Q33 | varchar |  |  | SI | Comentario 12 |
| Q34 | varchar |  |  | SI | Comentario 13 |
| Q35 | varchar |  |  | SI | Comentario 14 |
| Q36 | varchar |  |  | SI | Comentario 15 |
| Q37 | varchar |  |  | SI | Comentario 16 |
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