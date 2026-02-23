# questionnaire.QTCPSRQ

> PsyCheck Self Reporting Questionnaire (SRQ)

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* PsyCheck Self Reporting Questionnaire (SRQ)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | (CLIENT OR ASSESSOR TO COMPLETE) |
| Q04 | varchar |  |  | SI | Please select the ‘Yes’ box if you have had this s... |
| Q05 | varchar |  |  | SI | 1. Do you often have headaches? |
| Q06 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q07 | varchar |  |  | SI | 2. Is your appetite poor? |
| Q08 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q09 | varchar |  |  | SI | 3. Do you sleep badly? |
| Q10 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q11 | varchar |  |  | SI | 4. Are you easily frightened? |
| Q12 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q13 | varchar |  |  | SI | 5. Do your hands shake? |
| Q14 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q15 | varchar |  |  | SI | 6. Do you feel nervous? |
| Q16 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q17 | varchar |  |  | SI | 7. Is your digestion poor? |
| Q18 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q19 | varchar |  |  | SI | 8. Do you have trouble thinking clearly? |
| Q20 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q21 | varchar |  |  | SI | 9. Do you feel unhappy? |
| Q22 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q23 | varchar |  |  | SI | 10. Do you cry more than usual? |
| Q24 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q25 | varchar |  |  | SI | 11. Do you find it difficult to enjoy your daily a... |
| Q26 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q27 | varchar |  |  | SI | 12. Do you find it difficult to make decisions? |
| Q28 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q29 | varchar |  |  | SI | 13. Is your daily work suffering? |
| Q30 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q31 | varchar |  |  | SI | 14. Are you unable to play a useful part in life? |
| Q32 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q33 | varchar |  |  | SI | 15. Have you lost interest in things? |
| Q34 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q35 | varchar |  |  | SI | 16. Do you feel that you are a worthless person? |
| Q36 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q37 | varchar |  |  | SI | 17. Has the thought of ending your life been on yo... |
| Q38 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q39 | varchar |  |  | SI | 18. Do you feel tired all the time? |
| Q40 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q41 | varchar |  |  | SI | 19. Do you have uncomfortable feelings in the stom... |
| Q42 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q43 | varchar |  |  | SI | 20. Are you easily tired? |
| Q44 | varchar |  |  | SI | Have you had this problem at a time when you were ... |
| Q45 | varchar |  |  | SI | The self-reporting questionnaire (SRQ) was origina... |
| Q46 | varchar |  |  | SI | Re-screen using the PsyCheck Screening Tool at the... |
| Q47 | varchar |  |  | SI | If no improvement in scores evident after re-scree... |
| Q48 | varchar |  |  | SI | * Regardless of the client’s total score on the SR... |
| Q49 | varchar |  |  | SI | Instructions and information relating to this tool... |
| Q50 | varchar |  |  | SI | The PsyCheck Self Reporting Questionnaire (SRQ) wo... |
| Q51 | varchar |  |  | SI | 0 |
| Q52 | varchar |  |  | SI | No symptoms of depression, anxiety and/or somatic ... |
| Q53 | varchar |  |  | SI | Action: Re-screen using the PsyCheck Screening Too... |
| Q54 | varchar |  |  | SI | Otherwise monitor as required. |
| Q55 | varchar |  |  | SI | 1 to 4  |
| Q56 | varchar |  |  | SI | Some symptoms of depression, anxiety and/or somati... |
| Q57 | varchar |  |  | SI | Action: Give the first session of the PsyCheck Int... |
| Q58 | varchar |  |  | SI | 5 to 20 |
| Q59 | varchar |  |  | SI | Considerable symptoms of depression, anxiety and/o... |
| Q60 | varchar |  |  | SI | Action: Offer Sessions 1–4 of the PsyCheck Interve... |
| Q61 | varchar |  |  | SI | It was adapted by Lee (2), with permission from th... |
| Q62 | varchar |  |  | SI | 1. Harding TW, Arango MV de, Baltazar J, et al. Me... |
| Q63 | varchar |  |  | SI | 2. Lee NK, Jenner L. Development of the PsyCheck s... |
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