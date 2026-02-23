# questionnaire.QTCDEMMI

> de Morton Mobility Index (DEMMI)

**Schema:** questionnaire
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* de Morton Mobility Index (DEMMI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bed |
| Q04 | varchar |  |  | SI | Bridge |
| Q05 | varchar |  |  | SI | Roll onto side |
| Q06 | varchar |  |  | SI | Lying to sitting |
| Q07 | varchar |  |  | SI | Chair |
| Q08 | varchar |  |  | SI | Sit unsupported in chair |
| Q09 | varchar |  |  | SI | Sit to stand from chair |
| Q10 | varchar |  |  | SI | Sit to stand without using arms |
| Q11 | varchar |  |  | SI | Static balance (no gait aid) |
| Q12 | varchar |  |  | SI | Stand unsupported |
| Q13 | varchar |  |  | SI | Stand feet together |
| Q14 | varchar |  |  | SI | Stand on toes |
| Q15 | varchar |  |  | SI | Tandem stand with eyes closed |
| Q16 | varchar |  |  | SI | Walking |
| Q17 | varchar |  |  | SI | Gait aid used |
| Q18 | varchar |  |  | SI | Other gait aid used |
| Q19 | varchar |  |  | SI | Walking distance (with or without gait aid) |
| Q20 | varchar |  |  | SI | Walking independence |
| Q21 | varchar |  |  | SI | Dynamic balance (no gait aid) |
| Q22 | varchar |  |  | SI | Pick up pen from floor |
| Q23 | varchar |  |  | SI | Walks 4 steps backwards |
| Q24 | varchar |  |  | SI | Jump |
| Q25 | numeric |  |  | SI | DEMMI SCORE (MDC90 = 9 points; MCID = 10 points) |
| Q26 | varchar |  |  | SI | Notes |
| Q27 | varchar |  |  | SI | Item Instructions |
| Q28 | varchar |  |  | SI | Bed |
| Q29 | varchar |  |  | SI | 1. Person is lying supine and is asked to bend the... |
| Q30 | varchar |  |  | SI | 2. Person is lying supine and is asked to roll ont... |
| Q31 | varchar |  |  | SI | 3. Person is lying supine and is asked to sit up o... |
| Q32 | varchar |  |  | SI | Chair |
| Q33 | varchar |  |  | SI | 4. Person is asked to maintain sitting balance for... |
| Q34 | varchar |  |  | SI | 5. Person is asked to rise from sitting to standin... |
| Q35 | varchar |  |  | SI | 6. Person is asked to stand with their arms crosse... |
| Q36 | varchar |  |  | SI | Static Balance |
| Q37 | varchar |  |  | SI | 7. The person is asked if they can stand for 10 se... |
| Q38 | varchar |  |  | SI | 8. The person is asked if, for 10 seconds, they ca... |
| Q39 | varchar |  |  | SI | 9. The person is asked if they can stand on their ... |
| Q40 | varchar |  |  | SI | 10. The person is asked to place the heel of one f... |
| Q41 | varchar |  |  | SI | Walking |
| Q42 | varchar |  |  | SI | 11. Persons will be asked to walk with their curre... |
| Q43 | varchar |  |  | SI | If either of two gait aids could be used, the aid ... |
| Q44 | varchar |  |  | SI | 12. Independence is assessed over the person’s max... |
| Q45 | varchar |  |  | SI | Dynamic Balance |
| Q46 | varchar |  |  | SI | 13. A pen is placed 5 cm in front of the person’s ... |
| Q47 | varchar |  |  | SI | 14. Walks backwards 4 steps. Person remains steady... |
| Q48 | varchar |  |  | SI | 15. Person can jump. Both feet clear the ground. P... |
| Q49 | varchar |  |  | SI | Definitions |
| Q50 | varchar |  |  | SI | Minimal assistance = “hands on” physical but minim... |
| Q51 | varchar |  |  | SI | Supervision = another person monitors the activity... |
| Q52 | varchar |  |  | SI | Independent = the presence of another person is no... |
| Q53 | varchar |  |  | SI | Protocol for administration of the DEMMI |
| Q54 | varchar |  |  | SI | 1. Testing should be performed at the person’s bed... |
| Q55 | varchar |  |  | SI | 2. Testing should be performed when the person has... |
| Q56 | varchar |  |  | SI | 3. The test should be administered in the sequence... |
| Q57 | varchar |  |  | SI | 4. Each item should be explained and, if necessary... |
| Q58 | varchar |  |  | SI | 5. Items should be ticked to indicate item success... |
| Q59 | varchar |  |  | SI | 6. Items should not be tested if either the test a... |
| Q60 | varchar |  |  | SI | 7. Persons should be scored based on their first a... |
| Q61 | varchar |  |  | SI | 8. If an item is not appropriate given a person’s ... |
| Q62 | varchar |  |  | SI | 9. Persons can be encouraged but feedback should n... |
| Q63 | varchar |  |  | SI | 10. Three equipment items are required: chair with... |
| Q64 | varchar |  |  | SI | 11. The person administering the test manipulates ... |
| Q65 | varchar |  |  | SI | Unless the person requires minimal assistance to p... |
| Q66 | varchar |  |  | SI | 12. For persons that require a rest after each ite... |
| Q67 | varchar |  |  | SI | 13. For person’s who have low level mobility and r... |
| Q68 | varchar |  |  | SI | 14. Bed transfers: the bed height should be approp... |
| Q69 | varchar |  |  | SI | The person cannot use an external device such as t... |
| Q70 | varchar |  |  | SI | 15. Chair transfers: A standardised chair height o... |
| Q71 | varchar |  |  | SI | 16. Balance: Shoes cannot be worn for balance test... |
| Q72 | varchar |  |  | SI | For sitting balance, neither the arm rests or the ... |
| Q73 | varchar |  |  | SI | Standing balance tests should be performed with th... |
| Q74 | varchar |  |  | SI | If a person displays unsteadiness or significant s... |
| Q75 | varchar |  |  | SI | 17. Walking: Appropriate shoes can be worn for wal... |
| Q76 | varchar |  |  | SI | 18. Scoring: Using&nbsp;the&nbsp;conversion table ... |
| Q77 | varchar |  |  | SI | Please refer to the DEMMI Handbook for more inform... |
| Q78 | varchar |  |  | SI | de Morton Mobility Index (demmi.org.au) |
| Q79 | varchar |  |  | SI | © Copyright de Morton, Davidson & Keating 2007. |
| Q80 | varchar |  |  | SI | The DEMMI may be printed or reproduced without alt... |
| Q81 | varchar |  |  | SI | natalie.demorton@med.monash.edu.au. |
| Q82 | varchar |  |  | SI | The development of the DEMMI has been supported by... |
| Q83 | varchar |  |  | SI | Funded by the HCF Health and Medical Research Foun... |
| Q84 | varchar |  |  | SI | de&nbsp;Morton NA, Davidson M, Keating JL. The de ... |
| Q85 | varchar |  |  | SI | https://www.demmi.org.au/downloads/demmi.pdf |
| Q86 | varchar |  |  | SI | The DEMMI, de Morton Mobility Index, is an advance... |
| Q87 | varchar |  |  | SI | Raw Score |
| Q88 | varchar |  |  | SI | Score |
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