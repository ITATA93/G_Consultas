# questionnaire.QGXXXBCC

> Beliefs, Coping, Compliance

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Beliefs, Coping, Compliance

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bigint |  |  | SI | Problems associated with loss of function / body c... |
| Q01TxtOnly | bigint |  |  | SI | Problems associated with loss of function / body c... |
| Q02 | varchar |  |  | SI | Concern about the disease: |
| Q03 | varchar |  |  | SI | Acceptance |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Acceptance DR |
| Q05 | varchar |  |  | SI | Anxiety |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Anxiety DR |
| Q07 | varchar |  |  | SI | Aggression |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Aggression DR |
| Q09 | varchar |  |  | SI | Agitation |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Agitation DR |
| Q11 | varchar |  |  | SI | Depression |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Depression DR |
| Q13 | varchar |  |  | SI | Crying |
| Q13N | varchar |  |  | SI | Note |
| Q13ObsDR | varchar |  | FK | SI | Crying DR |
| Q15 | varchar |  |  | SI | Religion related |
| Q15ObsDR | varchar |  | FK | SI | Religion related DR |
| Q16 | bigint |  |  | SI | Notes and rules observed by culture or religion |
| Q16TxtOnly | bigint |  |  | SI | Notes and rules observed by culture or religion Pl... |
| Q17 | varchar |  |  | SI | Values and Beliefs |
| Q18 | varchar |  |  | SI | Perception |
| Q19 | varchar |  |  | SI | Family / Relationship Concerns	 |
| Q20 | varchar |  |  | SI | Action taken	 |
| Q21 | date |  |  | SI | Date |
| Q22 | varchar |  |  | SI | Emotional Concerns or other difficult thoughts and... |
| Q23 | varchar |  |  | SI | Action taken	 |
| Q24 | date |  |  | SI | Date |
| Q25 | varchar |  |  | SI | Spiritual, religious or cultural beliefs, practice... |
| Q26 | varchar |  |  | SI | Action taken	 |
| Q27 | date |  |  | SI | Date |
| Q28 | varchar |  |  | SI | Would you like to talk to the hospital chaplain ab... |
| Q29 | varchar |  |  | SI | Comment  |
| Q30 | date |  |  | SI | Date |
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