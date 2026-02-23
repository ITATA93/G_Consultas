# SQLUser.ORC_AuscultationBCF

**Schema:** SQLUser
**Columnas:** 148
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUSBCF_RowId | bigint | PK |  | NO | - |
| AUSBCF_Code | varchar |  |  | NO | Code |
| AUSBCF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AUSBCF_CreatedDate | date |  |  | SI | Created Date |
| AUSBCF_CreatedTime | time |  |  | SI | Created Time |
| AUSBCF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AUSBCF_DateFrom | date |  |  | SI | Date From |
| AUSBCF_DateTo | date |  |  | SI | Date To |
| AUSBCF_Desc | varchar |  |  | NO | Description |
| AUSBCF_Owner | varchar |  |  | SI | Owner |
| AUSBCF_UpdatedDate | date |  |  | SI | Updated Date |
| AUSBCF_UpdatedTime | time |  |  | SI | Updated Time |
| AUSBCF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | 1. Bring thumb extended on forehead, other fingers... |
| Q11 | - |  |  | SI | 1. Bring thumb extended on forehead, other fingers... |
| Q12 | - |  |  | SI | 2. Wipe dust from shoulder |
| Q13 | - |  |  | SI | 2. Wipe dust from shoulder (left) |
| Q14 | - |  |  | SI | Additional instruction: For the next five gestures... |
| Q15 | - |  |  | SI | 3. Drink from a glass |
| Q16 | - |  |  | SI | 3. Drink from a glass |
| Q17 | - |  |  | SI | 3. Drink from a glass (left) |
| Q18 | - |  |  | SI | 4. Smoke a cigarette |
| Q19 | - |  |  | SI | 4. Smoke a cigarette |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | 4. Smoke a cigarette (left) |
| Q21 | - |  |  | SI | 5. Use a hammer |
| Q22 | - |  |  | SI | 5. Use a hammer |
| Q23 | - |  |  | SI | 5. Use a hammer (left) |
| Q24 | - |  |  | SI | 6. Use scissors |
| Q25 | - |  |  | SI | 6. Use scissors |
| Q26 | - |  |  | SI | 6. Use scissors (left) |
| Q27 | - |  |  | SI | 7. Use a stamp to postmark |
| Q28 | - |  |  | SI | 7. Use a stamp to postmark |
| Q29 | - |  |  | SI | 7. Use a stamp to postmark (left) |
| Q30 | - |  |  | SI | Pantomime |
| Q31 | - |  |  | SI | General instruction: Now gestures are asked. liste... |
| Q32 | - |  |  | SI | 8. Show as if someone is crazy* |
| Q33 | - |  |  | SI | *repetitive tapping of the index finger at the tem... |
| Q34 | - |  |  | SI | 8. Show as if someone is crazy* |
| Q35 | - |  |  | SI | 8. Show as if someone is crazy (left) |
| Q36 | - |  |  | SI | 9 . Make a threatening sign** |
| Q37 | - |  |  | SI | **upraised clenched fist (upraised index finger or... |
| Q38 | - |  |  | SI | 9 . Make a threatening sign** |
| Q39 | - |  |  | SI | 9 . Make a threatening sign (left) |
| Q3a | - |  |  | SI | 1. Vanbellingen T, Kersten B, Hemelrijk BV, Wincke... |
| Q3b | - |  |  | SI | 2. Vanbellingen T, Kersten B, Winckel AV de, Belli... |
| Q4 | - |  |  | SI | Limb assessed |
| Q40 | - |  |  | SI | Additional instruction: Again, imagine holding a t... |
| Q41 | - |  |  | SI | 10. Brush your teeth |
| Q42 | - |  |  | SI | 10. Brush your teeth |
| Q43 | - |  |  | SI | 10. Brush your teeth (left) |
| Q44 | - |  |  | SI | 11. Comb your hair |
| Q45 | - |  |  | SI | 11. Comb your hair |
| Q46 | - |  |  | SI | 11. Comb your hair (left) |
| Q47 | - |  |  | SI | 12. Use a screwdriver |
| Q48 | - |  |  | SI | 12. Use a screwdriver |
| Q49 | - |  |  | SI | 12. Use a screwdriver (left) |
| Q5 | - |  |  | SI | Imitation |
| Q50 | - |  |  | SI | Item 1 = meaningless |
| Q51 | - |  |  | SI | Instructions |
| Q52 | - |  |  | SI | The patient is seated in front of the examiner |
| Q53 | - |  |  | SI | Hemiparetic patients execute the gestures with the... |
| Q54 | - |  |  | SI | Test evaluation |
| Q55 | - |  |  | SI | Dichotomous scale: 0 = fail, 1 = pass |
| Q56 | - |  |  | SI | Maximum score = 12 |
| Q57 | - |  |  | SI | Total cut-off score <9 |
| Q58 | - |  |  | SI | Severe apraxia <5 |
| Q59 | - |  |  | SI | Score 0 (Fail) = |
| Q6 | - |  |  | SI | General instruction: Seven gestures are demonstrat... |
| Q60 | - |  |  | SI | No movement or unrecognizable movement. Seeking an... |
| Q61 | - |  |  | SI | Errors grossly affecting trajectory or incorrect s... |
| Q62 | - |  |  | SI | Final position is false, major errors in spatial o... |
| Q63 | - |  |  | SI | Errors subtly affecting trajectory, and persisting... |
| Q64 | - |  |  | SI | Score 1 (Pass) = |
| Q65 | - |  |  | SI | Errors subtly affecting trajectory, but corrected.... |
| Q66 | - |  |  | SI | Errors not affecting trajectory. Movement is too s... |
| Q67 | - |  |  | SI | Normal movement |
| Q68 | - |  |  | SI | Also when brief substitutions or perseverations oc... |
| Q7 | - |  |  | SI | Right |
| Q70 | - |  |  | SI | 2. Wipe dust from shoulder |
| Q71 | - |  |  | SI | Right |
| Q72 | - |  |  | SI | Right |
| Q73 | - |  |  | SI | Right |
| Q74 | - |  |  | SI | Right |
| Q75 | - |  |  | SI | Right |
| Q76 | - |  |  | SI | Right |
| Q77 | - |  |  | SI | Right |
| Q78 | - |  |  | SI | Right |
| Q79 | - |  |  | SI | Right |
| Q8 | - |  |  | SI | Left |
| Q80 | - |  |  | SI | Right |
| Q81 | - |  |  | SI | Right |
| Q82 | - |  |  | SI | Right |
| Q83 | - |  |  | SI | Left |
| Q84 | - |  |  | SI | Left |
| Q85 | - |  |  | SI | Left |
| Q86 | - |  |  | SI | Left |
| Q87 | - |  |  | SI | Left |
| Q88 | - |  |  | SI | Left |
| Q89 | - |  |  | SI | Left |
| Q9 | - |  |  | SI | 1. Bring thumb extended on forehead, other fingers... |
| Q90 | - |  |  | SI | Left |
| Q91 | - |  |  | SI | Left |
| Q92 | - |  |  | SI | Left |
| Q93 | - |  |  | SI | Left |
| Q94 | - |  |  | SI | Left |
| Q95 | - |  |  | SI | The Apraxia Screen of TULIA (AST) is a bedside scr... |
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