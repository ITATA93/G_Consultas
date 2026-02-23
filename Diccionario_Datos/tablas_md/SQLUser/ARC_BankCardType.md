# SQLUser.ARC_BankCardType

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARD_RowId | bigint | PK |  | NO | - |
| CARD_Code | varchar |  |  | NO | Code |
| CARD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CARD_CreatedDate | date |  |  | SI | Created Date |
| CARD_CreatedTime | time |  |  | SI | Created Time |
| CARD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CARD_DateFrom | date |  |  | SI | Date From |
| CARD_DateTo | date |  |  | SI | Date To |
| CARD_Desc | varchar |  |  | NO | Description |
| CARD_Owner | varchar |  |  | SI | Owner |
| CARD_Prefix | varchar |  |  | SI | Prefix |
| CARD_UpdatedDate | date |  |  | SI | Updated Date |
| CARD_UpdatedTime | time |  |  | SI | Updated Time |
| CARD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | DATOS DE IDENTIFICACIÓN |
| Q02 | - |  |  | SI | Establecimiento |
| Q03 | - |  |  | SI | Tipo de Enseñanza |
| Q04 | - |  |  | SI | Curso |
| Q05 | - |  |  | SI | Letra Curso |
| Q06 | - |  |  | SI | PREGUNTAS ANTECEDENTES FAMILIARES |
| Q07 | - |  |  | SI | a. Edad de la madre al nacer el niño o niña |
| Q08 | - |  |  | SI | b. Actualmente, ¿vive con su mamá y su papá? |
| Q09 | - |  |  | SI | c. El niño o niña tiene una enfermedad que necesit... |
| Q10 | - |  |  | SI | d. Algún familiar que vive con el niño o niña ha s... |
| Q11 | - |  |  | SI | e. La familia participa habitualmente en las activ... |
| Q12 | - |  |  | SI | CUESTIONARIO DE CONDUCTAS |
| Q13 | - |  |  | SI | 1.&nbsp |
| Q14 | - |  |  | SI | 2.&nbsp |
| Q15 | - |  |  | SI | 3.&nbsp |
| Q16 | - |  |  | SI | 4.&nbsp |
| Q17 | - |  |  | SI | 5.&nbsp |
| Q18 | - |  |  | SI | 6. Se siente pesimista / piensa que las cosas son ... |
| Q19 | - |  |  | SI | 7. Le cuesta concentrarse |
| Q20 | - |  |  | SI | 8. Pelea con otros/as compañeros/as |
| Q21 | - |  |  | SI | 9. Se siente poca cosa |
| Q22 | - |  |  | SI | 10.&nbsp |
| Q23 | - |  |  | SI | 11.&nbsp |
| Q24 | - |  |  | SI | 12.&nbsp |
| Q25 | - |  |  | SI | 13.&nbsp |
| Q26 | - |  |  | SI | 14.&nbsp |
| Q27 | - |  |  | SI | 15.&nbsp |
| Q28 | - |  |  | SI | 16.&nbsp |
| Q29 | - |  |  | SI | 17.&nbsp |
| Q30 | - |  |  | SI | Subescala Problemas de Atención (PA) |
| Q31 | - |  |  | SI | &gt |
| Q32 | - |  |  | SI | Subescala Problemas Internalizantes (PI) |
| Q33 | - |  |  | SI | &gt |
| Q34 | - |  |  | SI | Subescala Problemas Externalizantes (PE) |
| Q35 | - |  |  | SI | &gt |
| Q36 | - |  |  | SI | Dificultades internalizantes |
| Q37 | - |  |  | SI | A mayor puntaje, mayores dificultades internalizan... |
| Q38 | - |  |  | SI | Dificultades externalizantes |
| Q39 | - |  |  | SI | A mayor puntaje, mayores dificultades externalizan... |
| Q40 | - |  |  | SI | Dificultades de atención |
| Q41 | - |  |  | SI | A mayor puntaje, mayores dificultades de atención,... |
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