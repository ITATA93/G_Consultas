# SQLUser.PAC_IDStatus

**Schema:** SQLUser
**Columnas:** 184
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IDSTAT_RowId | bigint | PK |  | NO | - |
| ChildQ12DR | - |  |  | SI | Child Reference: Family history |
| IDSTAT_Code | varchar |  |  | NO | Code |
| IDSTAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IDSTAT_CreatedDate | date |  |  | SI | Created Date |
| IDSTAT_CreatedTime | time |  |  | SI | Created Time |
| IDSTAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IDSTAT_DateFrom | date |  |  | SI | Date From |
| IDSTAT_DateTo | date |  |  | SI | Date To |
| IDSTAT_Desc | varchar |  |  | NO | Description |
| IDSTAT_Owner | varchar |  |  | SI | Owner |
| IDSTAT_UpdatedDate | date |  |  | SI | Updated Date |
| IDSTAT_UpdatedTime | time |  |  | SI | Updated Time |
| IDSTAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Last mammogram dates |
| Q02 | - |  |  | SI | Facility / Location of last mammogram |
| Q03 | - |  |  | SI | Are you pregnant (or possibly pregnant)? |
| Q04 | - |  |  | SI | Are you currently nursing? |
| Q05 | - |  |  | SI | First day of last menstruation |
| Q06 | - |  |  | SI | Age of first menstruation |
| Q07 | - |  |  | SI | Since when? |
| Q08 | - |  |  | SI | Are you in menopause? |
| Q09 | - |  |  | SI | Have you had a hysterectomy? |
| Q10 | - |  |  | SI | If so, medication / dosage |
| Q100 | - |  |  | SI | Extra Label 52 |
| Q101 | - |  |  | SI | Extra Label 53 |
| Q102 | - |  |  | SI | Extra Label 54 |
| Q103 | - |  |  | SI | Extra Label 55 |
| Q104 | - |  |  | SI | Extra Label 56 |
| Q105 | - |  |  | SI | Extra Label 57 |
| Q106 | - |  |  | SI | Extra Label 58 |
| Q107 | - |  |  | SI | Extra Label 59 |
| Q108 | - |  |  | SI | Extra Label 60 |
| Q109 | - |  |  | SI | Extra Signature 1 Date |
| Q11 | - |  |  | SI | Are you receiving hormonal therapy? |
| Q110 | - |  |  | SI | Extra Signature 2 Date |
| Q111 | - |  |  | SI | Extra Signature 3 Date |
| Q112 | - |  |  | SI | Extra Label 61 |
| Q113 | - |  |  | SI | Extra Label 62 |
| Q114 | - |  |  | SI | Extra Label 63 |
| Q115 | - |  |  | SI | Extra Label 64 |
| Q116 | - |  |  | SI | Extra Label 65 |
| Q117 | - |  |  | SI | Extra Label 66 |
| Q118 | - |  |  | SI | Extra Label 67 |
| Q119 | - |  |  | SI | Extra Label 68 |
| Q120 | - |  |  | SI | Extra Label 69 |
| Q121 | - |  |  | SI | Extra Label 70 |
| Q122 | - |  |  | SI | Date |
| Q123 | - |  |  | SI | Time |
| Q13 | - |  |  | SI | Do you have a family history of breast or ovarian ... |
| Q14 | - |  |  | SI | Please elaborate |
| Q15 | - |  |  | SI | Have members of your family been diagnosed with ot... |
| Q16 | - |  |  | SI | Right breast - When? |
| Q17 | - |  |  | SI | Right breast - Type |
| Q18 | - |  |  | SI | Left breast - When? |
| Q19 | - |  |  | SI | Left breast - Type |
| Q20 | - |  |  | SI | Have you personally had breast cancer? |
| Q21 | - |  |  | SI | Which breast? |
| Q22 | - |  |  | SI | When? |
| Q23 | - |  |  | SI | Result |
| Q24 | - |  |  | SI | Have you had breast surgery? |
| Q25 | - |  |  | SI | Which breast? |
| Q26 | - |  |  | SI | When? |
| Q27 | - |  |  | SI | To the breast? |
| Q28 | - |  |  | SI | When? |
| Q29 | - |  |  | SI | Why? |
| Q30 | - |  |  | SI | To the chest? |
| Q31 | - |  |  | SI | Have you received radiation therapy? |
| Q32 | - |  |  | SI | Type |
| Q33 | - |  |  | SI | Do you have breast implants? |
| Q34 | - |  |  | SI | Injury in |
| Q35 | - |  |  | SI | When? |
| Q36 | - |  |  | SI | Has your breast ever been injured? |
| Q37 | - |  |  | SI | Abnormality |
| Q38 | - |  |  | SI | Which breast? |
| Q39 | - |  |  | SI | Comment |
| Q40 | - |  |  | SI | Have you or your doctor noted an abnormality? |
| Q41 | - |  |  | SI | I have no further questions and consent to the pro... |
| Q42 | - |  |  | SI | Signature |
| Q42UDt | - |  |  | SI | Signature Last Updated Date |
| Q42UTm | - |  |  | SI | Signature Last Updated Time |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | (oral contraceptives, postmenopausal replacement) |
| Q45 | - |  |  | SI | (mastectomy, biopsy, lumpectomy, breast reduction) |
| Q46 | - |  |  | SI | Extra Signature 1 |
| Q46UDt | - |  |  | SI | Extra Signature 1 Last Updated Date |
| Q46UTm | - |  |  | SI | Extra Signature 1 Last Updated Time |
| Q47 | - |  |  | SI | Extra Signature 2 |
| Q47UDt | - |  |  | SI | Extra Signature 2 Last Updated Date |
| Q47UTm | - |  |  | SI | Extra Signature 2 Last Updated Time |
| Q48 | - |  |  | SI | Extra Signature 3 |
| Q48UDt | - |  |  | SI | Extra Signature 3 Last Updated Date |
| Q48UTm | - |  |  | SI | Extra Signature 3 Last Updated Time |
| Q49 | - |  |  | SI | Extra Label 1 |
| Q50 | - |  |  | SI | Extra Label 2 |
| Q51 | - |  |  | SI | Extra Label 3 |
| Q52 | - |  |  | SI | Extra Label 4 |
| Q53 | - |  |  | SI | Extra Label 5 |
| Q54 | - |  |  | SI | Extra Label 6 |
| Q55 | - |  |  | SI | Extra Label 7 |
| Q56 | - |  |  | SI | Extra Label 8 |
| Q57 | - |  |  | SI | Extra Label 9 |
| Q58 | - |  |  | SI | Extra Label 10 |
| Q59 | - |  |  | SI | Extra Label 11 |
| Q60 | - |  |  | SI | Extra Label 12 |
| Q61 | - |  |  | SI | Extra Label 13 |
| Q62 | - |  |  | SI | Extra Label 14 |
| Q63 | - |  |  | SI | Extra Label 15 |
| Q64 | - |  |  | SI | Extra Label 16 |
| Q65 | - |  |  | SI | Extra Label 17 |
| Q66 | - |  |  | SI | Extra Label 18 |
| Q67 | - |  |  | SI | Extra Label 19 |
| Q68 | - |  |  | SI | Extra Label 20 |
| Q69 | - |  |  | SI | Extra Label 21 |
| Q70 | - |  |  | SI | Extra Label 22 |
| Q71 | - |  |  | SI | Extra Label 23 |
| Q72 | - |  |  | SI | Extra Label 24 |
| Q73 | - |  |  | SI | Extra Label 25 |
| Q74 | - |  |  | SI | Extra Label 26 |
| Q75 | - |  |  | SI | Extra Label 27 |
| Q76 | - |  |  | SI | Extra Label 28 |
| Q77 | - |  |  | SI | Extra Label 29 |
| Q78 | - |  |  | SI | Extra Label 30 |
| Q79 | - |  |  | SI | Extra Label 31 |
| Q80 | - |  |  | SI | Extra Label 32 |
| Q81 | - |  |  | SI | Extra Label 33 |
| Q82 | - |  |  | SI | Extra Label 34 |
| Q83 | - |  |  | SI | Extra Label 35 |
| Q84 | - |  |  | SI | Extra Label 36 |
| Q85 | - |  |  | SI | Extra Label 37 |
| Q86 | - |  |  | SI | Extra Label 38 |
| Q87 | - |  |  | SI | Extra Label 39 |
| Q88 | - |  |  | SI | Extra Label 40 |
| Q89 | - |  |  | SI | Extra Label 41 |
| Q90 | - |  |  | SI | Extra Label 42 |
| Q91 | - |  |  | SI | Extra Label 43 |
| Q92 | - |  |  | SI | Extra Label 44 |
| Q93 | - |  |  | SI | Extra Label 45 |
| Q94 | - |  |  | SI | Extra Label 46 |
| Q95 | - |  |  | SI | Extra Label 47 |
| Q96 | - |  |  | SI | Extra Label 48 |
| Q97 | - |  |  | SI | Extra Label 49 |
| Q98 | - |  |  | SI | Extra Label 50 |
| Q99 | - |  |  | SI | Extra Label 51 |
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