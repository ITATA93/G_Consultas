# SQLUser.LBDR_TestSetLinkEpisode

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRTSLE_RowID | bigint | PK |  | NO | - |
| LBDRTSLE_CollectionDateTime | varchar |  |  | SI | Collection date/time |
| LBDRTSLE_DOB | varchar |  |  | SI | Patient DateOfBirth |
| LBDRTSLE_EpisodeNumber | varchar |  |  | SI | Episode Number |
| LBDRTSLE_FirstName | varchar |  |  | SI | Patient FirstName |
| LBDRTSLE_Header | varchar |  |  | SI | Linked TestSet Header
  Like "Linked TestSet" |
| LBDRTSLE_Surname | varchar |  |  | SI | Patient Surname |
| LBDRTSLE_URN | varchar |  |  | SI | Patient URN |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Autonomo (OLD) |
| Q03 | - |  |  | SI | Total (OLD) |
| Q04 | - |  |  | SI | Parcial (OLD) |
| Q05 | - |  |  | SI | Protesis Dental |
| Q06 | - |  |  | SI | Dificultad al Masticar o Deglutir |
| Q07 | - |  |  | SI | Detalle |
| Q08 | - |  |  | SI | Nauseas |
| Q09 | - |  |  | SI | Vomitos |
| Q10 | - |  |  | SI | Detalle |
| Q11 | - |  |  | SI | Dispepsia |
| Q12 | - |  |  | SI | Hidratacion |
| Q13 | - |  |  | SI | Dieta Habitual |
| Q14 | - |  |  | SI | Dieta Desequilibrada |
| Q15 | - |  |  | SI | Intolerancia y/o alergias alimentarias |
| Q16 | - |  |  | SI | Detalle |
| Q17 | - |  |  | SI | Dieta Prescrita |
| Q18 | - |  |  | SI | Detalle |
| Q19 | - |  |  | SI | N. Parenteral |
| Q20 | - |  |  | SI | N. Enteral |
| Q21 | - |  |  | SI | Suplementos |
| Q22 | - |  |  | SI | Diagnostico 1 |
| Q23 | - |  |  | SI | Diagnostico 2 |
| Q24 | - |  |  | SI | Conclusion |
| Q25 | - |  |  | SI | Pecho Materno |
| Q26 | - |  |  | SI | Alimentación |
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