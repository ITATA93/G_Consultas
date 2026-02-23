# SQLUser.PAC_SuspectCancerType

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANC_RowId | bigint | PK |  | NO | - |
| CANC_Code | varchar |  |  | NO | Code |
| CANC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CANC_CreatedDate | date |  |  | SI | Created Date |
| CANC_CreatedTime | time |  |  | SI | Created Time |
| CANC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANC_DateFrom | date |  |  | SI | Date From |
| CANC_DateTo | date |  |  | SI | Date To |
| CANC_Desc | varchar |  |  | NO | Description |
| CANC_NationalCode | varchar |  |  | SI | National Code |
| CANC_Owner | varchar |  |  | SI | Owner |
| CANC_UpdatedDate | date |  |  | SI | Updated Date |
| CANC_UpdatedTime | time |  |  | SI | Updated Time |
| CANC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | (CLIENT OR ASSESSOR TO COMPLETE) |
| Q04 | - |  |  | SI | Please select the ‘Yes’ box if you have had this s... |
| Q05 | - |  |  | SI | 1. Do you often have headaches? |
| Q06 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q07 | - |  |  | SI | 2. Is your appetite poor? |
| Q08 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q09 | - |  |  | SI | 3. Do you sleep badly? |
| Q10 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q11 | - |  |  | SI | 4. Are you easily frightened? |
| Q12 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q13 | - |  |  | SI | 5. Do your hands shake? |
| Q14 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q15 | - |  |  | SI | 6. Do you feel nervous? |
| Q16 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q17 | - |  |  | SI | 7. Is your digestion poor? |
| Q18 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q19 | - |  |  | SI | 8. Do you have trouble thinking clearly? |
| Q20 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q21 | - |  |  | SI | 9. Do you feel unhappy? |
| Q22 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q23 | - |  |  | SI | 10. Do you cry more than usual? |
| Q24 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q25 | - |  |  | SI | 11. Do you find it difficult to enjoy your daily a... |
| Q26 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q27 | - |  |  | SI | 12. Do you find it difficult to make decisions? |
| Q28 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q29 | - |  |  | SI | 13. Is your daily work suffering? |
| Q30 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q31 | - |  |  | SI | 14. Are you unable to play a useful part in life? |
| Q32 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q33 | - |  |  | SI | 15. Have you lost interest in things? |
| Q34 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q35 | - |  |  | SI | 16. Do you feel that you are a worthless person? |
| Q36 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q37 | - |  |  | SI | 17. Has the thought of ending your life been on yo... |
| Q38 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q39 | - |  |  | SI | 18. Do you feel tired all the time? |
| Q40 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q41 | - |  |  | SI | 19. Do you have uncomfortable feelings in the stom... |
| Q42 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q43 | - |  |  | SI | 20. Are you easily tired? |
| Q44 | - |  |  | SI | Have you had this problem at a time when you were ... |
| Q45 | - |  |  | SI | The self-reporting questionnaire (SRQ) was origina... |
| Q46 | - |  |  | SI | Re-screen using the PsyCheck Screening Tool at the... |
| Q47 | - |  |  | SI | If no improvement in scores evident after re-scree... |
| Q48 | - |  |  | SI | * Regardless of the client’s total score on the SR... |
| Q49 | - |  |  | SI | Instructions and information relating to this tool... |
| Q50 | - |  |  | SI | The PsyCheck Self Reporting Questionnaire (SRQ) wo... |
| Q51 | - |  |  | SI | 0 |
| Q52 | - |  |  | SI | No symptoms of depression, anxiety and/or somatic ... |
| Q53 | - |  |  | SI | Action: Re-screen using the PsyCheck Screening Too... |
| Q54 | - |  |  | SI | Otherwise monitor as required. |
| Q55 | - |  |  | SI | 1 to 4 |
| Q56 | - |  |  | SI | Some symptoms of depression, anxiety and/or somati... |
| Q57 | - |  |  | SI | Action: Give the first session of the PsyCheck Int... |
| Q58 | - |  |  | SI | 5 to 20 |
| Q59 | - |  |  | SI | Considerable symptoms of depression, anxiety and/o... |
| Q60 | - |  |  | SI | Action: Offer Sessions 1–4 of the PsyCheck Interve... |
| Q61 | - |  |  | SI | It was adapted by Lee (2), with permission from th... |
| Q62 | - |  |  | SI | 1. Harding TW, Arango MV de, Baltazar J, et al. Me... |
| Q63 | - |  |  | SI | 2. Lee NK, Jenner L. Development of the PsyCheck s... |
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