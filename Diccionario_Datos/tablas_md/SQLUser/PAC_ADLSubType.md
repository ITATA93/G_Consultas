# SQLUser.PAC_ADLSubType

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADLST_RowId | bigint | PK |  | NO | - |
| ADLST_Code | varchar |  |  | NO | Code |
| ADLST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADLST_CreatedDate | date |  |  | SI | Created Date |
| ADLST_CreatedTime | time |  |  | SI | Created Time |
| ADLST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADLST_DateFrom | date |  |  | SI | Date From |
| ADLST_DateTo | date |  |  | SI | Date To |
| ADLST_Desc | varchar |  |  | NO | Description |
| ADLST_NationalCode | varchar |  |  | SI | National Code |
| ADLST_Owner | varchar |  |  | SI | Owner |
| ADLST_UpdatedDate | date |  |  | SI | Updated Date |
| ADLST_UpdatedTime | time |  |  | SI | Updated Time |
| ADLST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Instructions: Choose the best answer for how you f... |
| Q04 | - |  |  | SI | Are you basically satisfied with your life? |
| Q05 | - |  |  | SI | Have you dropped many of your activities and inter... |
| Q06 | - |  |  | SI | Do you feel that your life is empty? |
| Q07 | - |  |  | SI | Do you often get bored? |
| Q08 | - |  |  | SI | Are you in good spirits most of the time? |
| Q09 | - |  |  | SI | Are you afraid that something bad is going to happ... |
| Q10 | - |  |  | SI | Do you feel happy most of the time? |
| Q11 | - |  |  | SI | Do you often feel helpless? |
| Q12 | - |  |  | SI | Do you prefer to stay at home, rather than going o... |
| Q13 | - |  |  | SI | Do you feel you have more problems with memory tha... |
| Q14 | - |  |  | SI | Do you think it is wonderful to be alive? |
| Q15 | - |  |  | SI | Do you feel pretty worthless the way you are now? |
| Q16 | - |  |  | SI | Do you feel full of energy? |
| Q17 | - |  |  | SI | Do you feel that your situation is hopeless? |
| Q18 | - |  |  | SI | Do you think that most people are better off than ... |
| Q19 | - |  |  | SI | • Choose the best answer for how you felt over the... |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | Approximated in-hospital mortality rates |
| Q23 | - |  |  | SI | 0-5 |
| Q24 | - |  |  | SI | Normal |
| Q25 | - |  |  | SI | ≥6 |
| Q26 | - |  |  | SI | Suggests depression |
| Q27 | - |  |  | SI | 0-5: Normal |
| Q28 | - |  |  | SI | ≥6: Suggests depression |
| Q29 | - |  |  | SI | The Geriatric Depression Scale (GDS) (15 point ver... |
| Q30 | - |  |  | SI | • Sheikh JI, Yesavage JA. Geriatric Depression Sca... |
| Q31 | - |  |  | SI | • Yesavage JA, Brink TL, Rose TL,&nbsp |
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