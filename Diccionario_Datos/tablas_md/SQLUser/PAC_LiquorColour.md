# SQLUser.PAC_LiquorColour

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIQCOLOR_RowId | bigint | PK |  | NO | - |
| LIQCOLOR_Active | varchar |  |  | SI | Active flag |
| LIQCOLOR_Code | varchar |  |  | NO | Code |
| LIQCOLOR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LIQCOLOR_CreatedDate | date |  |  | SI | Created Date |
| LIQCOLOR_CreatedTime | time |  |  | SI | Created Time |
| LIQCOLOR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LIQCOLOR_DateFrom | date |  |  | SI | Date From |
| LIQCOLOR_DateTo | date |  |  | SI | Date To |
| LIQCOLOR_Desc | varchar |  |  | NO | Description |
| LIQCOLOR_NationalCode | varchar |  |  | SI | National Code |
| LIQCOLOR_Owner | varchar |  |  | SI | Owner |
| LIQCOLOR_UpdatedDate | date |  |  | SI | Updated Date |
| LIQCOLOR_UpdatedTime | time |  |  | SI | Updated Time |
| LIQCOLOR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | How often has this child shown these behaviours in... |
| Q04 | - |  |  | SI | (for example, this child does not eat solid food o... |
| Q05 | - |  |  | SI | 1a Moaning, whining, whimpering (fairly soft) |
| Q06 | - |  |  | SI | 1b Crying (moderately loud) |
| Q07 | - |  |  | SI | 1c Screaming / Yelling (very loud) |
| Q08 | - |  |  | SI | 1d A specific sound or word for pain (e.g., a word... |
| Q09 | - |  |  | SI | Vocal Score |
| Q10 | - |  |  | SI | 2a Not cooperating, cranky, irritable, unhappy |
| Q11 | - |  |  | SI | 2b Less interaction with others, withdrawn |
| Q12 | - |  |  | SI | 2c Seeking comfort or physical closeness |
| Q13 | - |  |  | SI | 2d Being difficult to distract, not able to satisf... |
| Q14 | - |  |  | SI | Social Score |
| Q15 | - |  |  | SI | 3a A furrowed brow |
| Q16 | - |  |  | SI | 3b A change in eyes, including: squinching of eyes... |
| Q17 | - |  |  | SI | 3c Turning down of mouth, not smiling |
| Q18 | - |  |  | SI | 3e Clenching or grinding teeth, chewing or thrusti... |
| Q19 | - |  |  | SI | Facial Score |
| Q20 | - |  |  | SI | 4a Not moving, less active, quiet |
| Q21 | - |  |  | SI | 4b Jumping around, agitated, fidgety |
| Q22 | - |  |  | SI | Activity Score |
| Q23 | - |  |  | SI | 5a Floppy |
| Q24 | - |  |  | SI | 5b Stiff, spastic, tense, rigid |
| Q25 | - |  |  | SI | 5c Gesturing to or touching part of the body that ... |
| Q26 | - |  |  | SI | 5d Protecting, favoring or guarding part of the bo... |
| Q27 | - |  |  | SI | 5e Flinching or moving the body part away, being s... |
| Q28 | - |  |  | SI | 5f Moving the body in a specific way to show pain ... |
| Q29 | - |  |  | SI | Body and Limbs Score |
| Q30 | - |  |  | SI | 6a Shivering |
| Q31 | - |  |  | SI | 6b Change in color, pallor |
| Q32 | - |  |  | SI | 6c Sweating, perspiring |
| Q33 | - |  |  | SI | 6d Tears |
| Q34 | - |  |  | SI | 6e Sharp intake of breath, gasping |
| Q35 | - |  |  | SI | 6f Breath holding |
| Q36 | - |  |  | SI | Physiological Score |
| Q37 | - |  |  | SI | 7a Eating less, not interested in food |
| Q38 | - |  |  | SI | 7b Increase in sleep |
| Q39 | - |  |  | SI | 7c Decrease in sleep |
| Q40 | - |  |  | SI | Eating / Sleeping Score |
| Q41 | - |  |  | SI | ≥ 7 |
| Q42 | - |  |  | SI | 1 - 6 |
| Q43 | - |  |  | SI | Score |
| Q44 | - |  |  | SI | Classification |
| Q45 | - |  |  | SI | >= 7: Pain |
| Q46 | - |  |  | SI | 1 - 6: No pain |
| Q47 | - |  |  | SI | Revised (NCCPC-R) has displayed preliminary validi... |
| Q48 | - |  |  | SI | Total Score |
| Q49 | - |  |  | SI | Pain |
| Q50 | - |  |  | SI | No pain |
| Q51 | - |  |  | SI | 0 - 120: The higher the score, greater the pain |
| Q52 | - |  |  | SI | 3d Lips puckering up, tight, pouting, or quivering |
| Q53 | - |  |  | SI | Vocal Score |
| Q54 | - |  |  | SI | Social Score |
| Q55 | - |  |  | SI | Facial Score |
| Q56 | - |  |  | SI | Activity Score |
| Q57 | - |  |  | SI | Body and Limbs Score |
| Q58 | - |  |  | SI | Physiological Score |
| Q59 | - |  |  | SI | Eating / Sleeping Score |
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