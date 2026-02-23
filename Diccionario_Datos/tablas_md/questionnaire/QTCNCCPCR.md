# questionnaire.QTCNCCPCR

> The non-communicating children's pain checklist (NCCPC) - Revised (NCCPC-R)

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The non-communicating children's pain checklist (NCCPC) - Revised (NCCPC-R)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | How often has this child shown these behaviours in... |
| Q04 | varchar |  |  | SI | (for example, this child does not eat solid food o... |
| Q05 | varchar |  |  | SI | 1a Moaning, whining, whimpering (fairly soft) |
| Q06 | varchar |  |  | SI | 1b Crying (moderately loud) |
| Q07 | varchar |  |  | SI | 1c Screaming / Yelling (very loud) |
| Q08 | varchar |  |  | SI | 1d A specific sound or word for pain (e.g., a word... |
| Q09 | varchar |  |  | SI | Vocal Score |
| Q10 | varchar |  |  | SI | 2a Not cooperating, cranky, irritable, unhappy |
| Q11 | varchar |  |  | SI | 2b Less interaction with others, withdrawn |
| Q12 | varchar |  |  | SI | 2c Seeking comfort or physical closeness |
| Q13 | varchar |  |  | SI | 2d Being difficult to distract, not able to satisf... |
| Q14 | varchar |  |  | SI | Social Score |
| Q15 | varchar |  |  | SI | 3a A furrowed brow |
| Q16 | varchar |  |  | SI | 3b A change in eyes, including: squinching of eyes... |
| Q17 | varchar |  |  | SI | 3c Turning down of mouth, not smiling |
| Q18 | varchar |  |  | SI | 3e Clenching or grinding teeth, chewing or thrusti... |
| Q19 | varchar |  |  | SI | Facial Score |
| Q20 | varchar |  |  | SI | 4a Not moving, less active, quiet |
| Q21 | varchar |  |  | SI | 4b Jumping around, agitated, fidgety |
| Q22 | varchar |  |  | SI | Activity Score |
| Q23 | varchar |  |  | SI | 5a Floppy |
| Q24 | varchar |  |  | SI | 5b Stiff, spastic, tense, rigid |
| Q25 | varchar |  |  | SI | 5c Gesturing to or touching part of the body that ... |
| Q26 | varchar |  |  | SI | 5d Protecting, favoring or guarding part of the bo... |
| Q27 | varchar |  |  | SI | 5e Flinching or moving the body part away, being s... |
| Q28 | varchar |  |  | SI | 5f Moving the body in a specific way to show pain ... |
| Q29 | varchar |  |  | SI | Body and Limbs Score |
| Q30 | varchar |  |  | SI | 6a Shivering |
| Q31 | varchar |  |  | SI | 6b Change in color, pallor |
| Q32 | varchar |  |  | SI | 6c Sweating, perspiring |
| Q33 | varchar |  |  | SI | 6d Tears |
| Q34 | varchar |  |  | SI | 6e Sharp intake of breath, gasping |
| Q35 | varchar |  |  | SI | 6f Breath holding |
| Q36 | varchar |  |  | SI | Physiological Score |
| Q37 | varchar |  |  | SI | 7a Eating less, not interested in food |
| Q38 | varchar |  |  | SI | 7b Increase in sleep |
| Q39 | varchar |  |  | SI | 7c Decrease in sleep |
| Q40 | varchar |  |  | SI | Eating / Sleeping Score |
| Q41 | varchar |  |  | SI | ≥ 7 |
| Q42 | varchar |  |  | SI | 1 - 6 |
| Q43 | varchar |  |  | SI | Score |
| Q44 | varchar |  |  | SI | Classification |
| Q45 | varchar |  |  | SI | >= 7: Pain |
| Q46 | varchar |  |  | SI | 1 - 6: No pain |
| Q47 | varchar |  |  | SI | Revised (NCCPC-R) has displayed preliminary validi... |
| Q48 | varchar |  |  | SI | Total Score |
| Q49 | varchar |  |  | SI | Pain |
| Q50 | varchar |  |  | SI | No pain |
| Q51 | varchar |  |  | SI | 0 - 120: The higher the score, greater the pain |
| Q52 | varchar |  |  | SI | 3d Lips puckering up, tight, pouting, or quivering |
| Q53 | varchar |  |  | SI | Vocal Score |
| Q54 | varchar |  |  | SI | Social Score |
| Q55 | varchar |  |  | SI | Facial Score |
| Q56 | varchar |  |  | SI | Activity Score |
| Q57 | varchar |  |  | SI | Body and Limbs Score |
| Q58 | varchar |  |  | SI | Physiological Score |
| Q59 | varchar |  |  | SI | Eating / Sleeping Score |
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