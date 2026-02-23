# questionnaire.QTCVHI

> Voice Handicap Index

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Voice Handicap Index

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of examination |
| Q02 | time |  |  | SI | Time of examination |
| Q03 | varchar |  |  | SI | These are statements that many people have used to... |
| Q04 | varchar |  |  | SI | My voice makes it difficult for people to hear me |
| Q05 | varchar |  |  | SI | People have difficulty understanding me in a noisy... |
| Q06 | varchar |  |  | SI | My family has difficulty hearing me when I call th... |
| Q07 | varchar |  |  | SI | I use the phone less often than I would like to |
| Q08 | varchar |  |  | SI | I tend to avoid groups of people because of my voi... |
| Q09 | varchar |  |  | SI | I speak with friends, neighbours, or relatives les... |
| Q10 | varchar |  |  | SI | People ask me to repeat myself when speaking face-... |
| Q11 | varchar |  |  | SI | My voice difficulties restrict my personal and soc... |
| Q12 | varchar |  |  | SI | I feel left out of conversations because of my voi... |
| Q13 | varchar |  |  | SI | My voice problem causes me to lose income |
| Q14 | varchar |  |  | SI | I run out of air when I talk |
| Q15 | varchar |  |  | SI | The sound of my voice varies throughout the day |
| Q16 | varchar |  |  | SI | People ask, What's wrong with your voice? |
| Q17 | varchar |  |  | SI | My voice sounds creaky and dry |
| Q18 | varchar |  |  | SI | I feel as though I have to strain to produce voice |
| Q19 | varchar |  |  | SI | The clarity of my voice is unpredictable |
| Q20 | varchar |  |  | SI | I try to change my voice to sound different |
| Q21 | varchar |  |  | SI | I use a great deal of effort to speak |
| Q22 | varchar |  |  | SI | My voice is worse in the evening |
| Q23 | varchar |  |  | SI | My voice gives out on me in the middle of speaking |
| Q24 | varchar |  |  | SI | I am tense when talking to others because of my vo... |
| Q25 | varchar |  |  | SI | People seem irritated with my voice |
| Q26 | varchar |  |  | SI | I find other people do not understand my voice pro... |
| Q27 | varchar |  |  | SI | My voice problem upsets me |
| Q28 | varchar |  |  | SI | I am less outgoing because of my voice problem |
| Q29 | varchar |  |  | SI | My voice makes me feel handicapped |
| Q30 | varchar |  |  | SI | I feel annoyed when people ask me to repeat |
| Q31 | varchar |  |  | SI | I feel embarrassed when people ask me to repeat |
| Q32 | varchar |  |  | SI | My voice makes me feel incompetent |
| Q33 | varchar |  |  | SI | I am ashamed of my voice problem |
| Q34 | varchar |  |  | SI | These are statements that many people have used to... |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | : |
| Q37 | varchar |  |  | SI | Classification |
| Q38 | varchar |  |  | SI | 0 - 30 : Mild - Minimal amount of handicap |
| Q39 | varchar |  |  | SI | 31 - 60 : Moderate - Often seen in patients with v... |
| Q40 | varchar |  |  | SI | 60 - 120 : Severe - Often seen in patients with vo... |
| Q41 | varchar |  |  | SI | The Voice Handicap Index is a tool for assessment ... |
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