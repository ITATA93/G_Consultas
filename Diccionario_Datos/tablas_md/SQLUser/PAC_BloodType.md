# SQLUser.PAC_BloodType

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLDT_RowId | bigint | PK |  | NO | - |
| BLDT_Code | varchar |  |  | NO | Blood Type Code |
| BLDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLDT_CodeTranslated | varchar |  |  | SI | - |
| BLDT_CreatedDate | date |  |  | SI | Created Date |
| BLDT_CreatedTime | time |  |  | SI | Created Time |
| BLDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLDT_Desc | varchar |  |  | NO | Description |
| BLDT_DescTranslated | varchar |  |  | SI | - |
| BLDT_Owner | varchar |  |  | SI | Owner |
| BLDT_RhesusStatus_DR | bigint |  | FK | SI | Des Ref PACRhesusStatus |
| BLDT_UpdatedDate | date |  |  | SI | Updated Date |
| BLDT_UpdatedTime | time |  |  | SI | Updated Time |
| BLDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Over the past 6 months |
| Q02 | - |  |  | SI | How do you rate your confidence that you could get... |
| Q03 | - |  |  | SI | When you had erections with sexual stimulation, ho... |
| Q04 | - |  |  | SI | During sexual intercourse, how often were you able... |
| Q05 | - |  |  | SI | During sexual intercourse, how difficult was it to... |
| Q06 | - |  |  | SI | When you attempted sexual intercourse, how often w... |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | A self-administered tool which is an abridged five... |
| Q10 | - |  |  | SI | 5–7 |
| Q11 | - |  |  | SI | Severe erectile dysfunction |
| Q12 | - |  |  | SI | 8–11 |
| Q13 | - |  |  | SI | Moderate erectile dysfunction |
| Q14 | - |  |  | SI | 12–16 |
| Q15 | - |  |  | SI | Mild to moderate erectile dysfunction |
| Q16 | - |  |  | SI | 17–21 |
| Q17 | - |  |  | SI | Mild erectile dysfunction |
| Q18 | - |  |  | SI | 22–25 |
| Q19 | - |  |  | SI | No erectile dysfunction |
| Q20 | - |  |  | SI | IIEF-5 Scoring |
| Q21 | - |  |  | SI | The IIEF-5 score is the sum of the ordinal respons... |
| Q22 | - |  |  | SI | 22–25: No erectile dysfunction |
| Q23 | - |  |  | SI | 17–21: Mild erectile dysfunction |
| Q24 | - |  |  | SI | 12–16: Mild to moderate erectile dysfunction |
| Q25 | - |  |  | SI | 8–11: Moderate erectile dysfunction |
| Q26 | - |  |  | SI | 5–7: Severe erectile dysfunction |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Time |
| Q29 | - |  |  | SI | Rosen R, Cappelleri J, Smith M, Lipsky J, Peña B. ... |
| Q30 | - |  |  | SI | Int J Impot Res 1999 |
| Q31 | - |  |  | SI | A self-administered tool which is an abridged five... |
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