# SQLUser.LBC_InstrumentProcedureResultTrans

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINPT_ParRef | varchar | PK |  | NO | Parent instrument DR |
| LBCINPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINPT_DateFrom | date |  |  | SI | Date From |
| LBCINPT_DateTo | date |  |  | SI | Date To |
| LBCINPT_InstrumentResult | varchar |  |  | SI | Instrument result |
| LBCINPT_InstrumentResultFrom | varchar |  |  | SI | Instrument Result From |
| LBCINPT_InstrumentResultTo | varchar |  |  | SI | Instrument Result To |
| LBCINPT_Result | varchar |  |  | SI | Internal result |
| LBCINPT_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bed |
| Q04 | - |  |  | SI | Bridge |
| Q05 | - |  |  | SI | Roll onto side |
| Q06 | - |  |  | SI | Lying to sitting |
| Q07 | - |  |  | SI | Chair |
| Q08 | - |  |  | SI | Sit unsupported in chair |
| Q09 | - |  |  | SI | Sit to stand from chair |
| Q10 | - |  |  | SI | Sit to stand without using arms |
| Q11 | - |  |  | SI | Static balance (no gait aid) |
| Q12 | - |  |  | SI | Stand unsupported |
| Q13 | - |  |  | SI | Stand feet together |
| Q14 | - |  |  | SI | Stand on toes |
| Q15 | - |  |  | SI | Tandem stand with eyes closed |
| Q16 | - |  |  | SI | Walking |
| Q17 | - |  |  | SI | Gait aid used |
| Q18 | - |  |  | SI | Other gait aid used |
| Q19 | - |  |  | SI | Walking distance (with or without gait aid) |
| Q20 | - |  |  | SI | Walking independence |
| Q21 | - |  |  | SI | Dynamic balance (no gait aid) |
| Q22 | - |  |  | SI | Pick up pen from floor |
| Q23 | - |  |  | SI | Walks 4 steps backwards |
| Q24 | - |  |  | SI | Jump |
| Q25 | - |  |  | SI | DEMMI SCORE (MDC90 = 9 points |
| Q26 | - |  |  | SI | Notes |
| Q27 | - |  |  | SI | Item Instructions |
| Q28 | - |  |  | SI | Bed |
| Q29 | - |  |  | SI | 1. Person is lying supine and is asked to bend the... |
| Q30 | - |  |  | SI | 2. Person is lying supine and is asked to roll ont... |
| Q31 | - |  |  | SI | 3. Person is lying supine and is asked to sit up o... |
| Q32 | - |  |  | SI | Chair |
| Q33 | - |  |  | SI | 4. Person is asked to maintain sitting balance for... |
| Q34 | - |  |  | SI | 5. Person is asked to rise from sitting to standin... |
| Q35 | - |  |  | SI | 6. Person is asked to stand with their arms crosse... |
| Q36 | - |  |  | SI | Static Balance |
| Q37 | - |  |  | SI | 7. The person is asked if they can stand for 10 se... |
| Q38 | - |  |  | SI | 8. The person is asked if, for 10 seconds, they ca... |
| Q39 | - |  |  | SI | 9. The person is asked if they can stand on their ... |
| Q40 | - |  |  | SI | 10. The person is asked to place the heel of one f... |
| Q41 | - |  |  | SI | Walking |
| Q42 | - |  |  | SI | 11. Persons will be asked to walk with their curre... |
| Q43 | - |  |  | SI | If either of two gait aids could be used, the aid ... |
| Q44 | - |  |  | SI | 12. Independence is assessed over the person’s max... |
| Q45 | - |  |  | SI | Dynamic Balance |
| Q46 | - |  |  | SI | 13. A pen is placed 5 cm in front of the person’s ... |
| Q47 | - |  |  | SI | 14. Walks backwards 4 steps. Person remains steady... |
| Q48 | - |  |  | SI | 15. Person can jump. Both feet clear the ground. P... |
| Q49 | - |  |  | SI | Definitions |
| Q50 | - |  |  | SI | Minimal assistance = “hands on” physical but minim... |
| Q51 | - |  |  | SI | Supervision = another person monitors the activity... |
| Q52 | - |  |  | SI | Independent = the presence of another person is no... |
| Q53 | - |  |  | SI | Protocol for administration of the DEMMI |
| Q54 | - |  |  | SI | 1. Testing should be performed at the person’s bed... |
| Q55 | - |  |  | SI | 2. Testing should be performed when the person has... |
| Q56 | - |  |  | SI | 3. The test should be administered in the sequence... |
| Q57 | - |  |  | SI | 4. Each item should be explained and, if necessary... |
| Q58 | - |  |  | SI | 5. Items should be ticked to indicate item success... |
| Q59 | - |  |  | SI | 6. Items should not be tested if either the test a... |
| Q60 | - |  |  | SI | 7. Persons should be scored based on their first a... |
| Q61 | - |  |  | SI | 8. If an item is not appropriate given a person’s ... |
| Q62 | - |  |  | SI | 9. Persons can be encouraged but feedback should n... |
| Q63 | - |  |  | SI | 10. Three equipment items are required: chair with... |
| Q64 | - |  |  | SI | 11. The person administering the test manipulates ... |
| Q65 | - |  |  | SI | Unless the person requires minimal assistance to p... |
| Q66 | - |  |  | SI | 12. For persons that require a rest after each ite... |
| Q67 | - |  |  | SI | 13. For person’s who have low level mobility and r... |
| Q68 | - |  |  | SI | 14. Bed transfers: the bed height should be approp... |
| Q69 | - |  |  | SI | The person cannot use an external device such as t... |
| Q70 | - |  |  | SI | 15. Chair transfers: A standardised chair height o... |
| Q71 | - |  |  | SI | 16. Balance: Shoes cannot be worn for balance test... |
| Q72 | - |  |  | SI | For sitting balance, neither the arm rests or the ... |
| Q73 | - |  |  | SI | Standing balance tests should be performed with th... |
| Q74 | - |  |  | SI | If a person displays unsteadiness or significant s... |
| Q75 | - |  |  | SI | 17. Walking: Appropriate shoes can be worn for wal... |
| Q76 | - |  |  | SI | 18. Scoring: Using&nbsp |
| Q77 | - |  |  | SI | Please refer to the DEMMI Handbook for more inform... |
| Q78 | - |  |  | SI | de Morton Mobility Index (demmi.org.au) |
| Q79 | - |  |  | SI | © Copyright de Morton, Davidson & Keating 2007. |
| Q80 | - |  |  | SI | The DEMMI may be printed or reproduced without alt... |
| Q81 | - |  |  | SI | natalie.demorton@med.monash.edu.au. |
| Q82 | - |  |  | SI | The development of the DEMMI has been supported by... |
| Q83 | - |  |  | SI | Funded by the HCF Health and Medical Research Foun... |
| Q84 | - |  |  | SI | de&nbsp |
| Q85 | - |  |  | SI | https://www.demmi.org.au/downloads/demmi.pdf |
| Q86 | - |  |  | SI | The DEMMI, de Morton Mobility Index, is an advance... |
| Q87 | - |  |  | SI | Raw Score |
| Q88 | - |  |  | SI | Score |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*