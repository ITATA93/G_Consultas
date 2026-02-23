# SQLUser.PAC_Clinic

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLN_RowId | bigint | PK |  | NO | - |
| CLN_Address1 | varchar |  |  | SI | Address1 |
| CLN_Address2 | varchar |  |  | SI | Address2 |
| CLN_BusPhone | varchar |  |  | SI | Business Phone |
| CLN_City_DR | bigint |  | FK | SI | Des Ref City |
| CLN_Code | varchar |  |  | NO | Code |
| CLN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLN_CodeTranslated | varchar |  |  | SI | Code Translated |
| CLN_ConfidentialFax | varchar |  |  | SI | Confidential Fax |
| CLN_CreatedDate | date |  |  | SI | Created Date |
| CLN_CreatedTime | time |  |  | SI | Created Time |
| CLN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLN_DateFrom | date |  |  | SI | Date From |
| CLN_DateTo | date |  |  | SI | Date To |
| CLN_Desc | varchar |  |  | NO | Description |
| CLN_DescTranslated | varchar |  |  | SI | Desc Translated |
| CLN_Email | varchar |  |  | SI | Email |
| CLN_Fax | varchar |  |  | SI | Fax |
| CLN_HCA_DR | bigint |  | FK | SI | Des Ref CTHealthCareArea |
| CLN_Owner | varchar |  |  | SI | Owner |
| CLN_Phone | varchar |  |  | SI | Phone |
| CLN_ProviderNo | varchar |  |  | SI | ProviderNo |
| CLN_Text1 | varchar |  |  | SI | Text1 |
| CLN_Text2 | varchar |  |  | SI | Text2 |
| CLN_UpdatedDate | date |  |  | SI | Updated Date |
| CLN_UpdatedTime | time |  |  | SI | Updated Time |
| CLN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CLN_VEMD | varchar |  |  | SI | VEMD |
| CLN_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| ChildQ19DR | - |  |  | SI | Child Reference: Other symptoms |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Recall timeframe |
| Q04 | - |  |  | SI | Considering the last 3 days, please select appropr... |
| Q05 | - |  |  | SI | Considering the last week, please select appropria... |
| Q06 | - |  |  | SI | Q1. What have been your main problems or concerns? |
| Q07 | - |  |  | SI | Q2. Below is a list of symptoms, which you may or ... |
| Q08 | - |  |  | SI | Pain |
| Q09 | - |  |  | SI | Shortness of breath |
| Q10 | - |  |  | SI | Weakness or lack of energy |
| Q11 | - |  |  | SI | Nausea (feeling like you are going to be sick) |
| Q12 | - |  |  | SI | Vomiting (being sick) |
| Q13 | - |  |  | SI | Poor appetite |
| Q14 | - |  |  | SI | Constipation |
| Q15 | - |  |  | SI | Sore or dry mouth |
| Q16 | - |  |  | SI | Drowsiness |
| Q17 | - |  |  | SI | Poor mobility |
| Q18 | - |  |  | SI | Are there any other symptoms? |
| Q20 | - |  |  | SI | Q3. Have you been feeling anxious or worried about... |
| Q21 | - |  |  | SI | Q4. Have any of your family or friends been anxiou... |
| Q22 | - |  |  | SI | Q5. Have you been feeling depressed? |
| Q23 | - |  |  | SI | Q6. Have you felt at peace? |
| Q24 | - |  |  | SI | Q7. Have you been able to share how you are feelin... |
| Q25 | - |  |  | SI | Q8. Have you had as much information as you wanted... |
| Q26 | - |  |  | SI | Q10. How did you complete this questionnaire? |
| Q27 | - |  |  | SI | Q9. Have any practical problems resulting from you... |
| Q28 | - |  |  | SI | If you are worried about any of the issues raised ... |
| Q29 | - |  |  | SI | Guidelines |
| Q30 | - |  |  | SI | The POS measures are a family of tools to measure ... |
| Q31 | - |  |  | SI | The POS measures are specifically developed for us... |
| Q32 | - |  |  | SI | POS is designed to be responsive to change. It can... |
| Q34 | - |  |  | SI | https://pos-pal.org/maix/how-to-administer.php |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | Classification |
| Q37 | - |  |  | SI | • The Palliative Care Outcome Scale (POS) measures... |
| Q38 | - |  |  | SI | • The POS measures are specifically developed for ... |
| Q39 | - |  |  | SI | • POS is designed to be responsive to change. It c... |
| Q40 | - |  |  | SI | • Changes in scores over time are important to det... |
| Q41 | - |  |  | SI | • IPOS results can be used to calculate i) individ... |
| Q41a | - |  |  | SI | • Individual item scores are useful when tracking ... |
| Q42 | - |  |  | SI | • https://pos-pal.org/maix/how-to-score.php#:~:tex... |
| Q46 | - |  |  | SI | 0 - 68 |
| Q47 | - |  |  | SI | Higher scores are indicative of a higher level of ... |
| Q48 | - |  |  | SI | 0 - 68: Higher scores are indicative of a higher l... |
| Q50 | - |  |  | SI | • If additional symptoms are identified at the end... |
| Q51 | - |  |  | SI | • However, if an additional symptom score is used ... |
| Q52 | - |  |  | SI | • Note that Question 1, the additional symptoms fr... |
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