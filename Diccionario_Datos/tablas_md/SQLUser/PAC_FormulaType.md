# SQLUser.PAC_FormulaType

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FRMLTYPE_RowId | bigint | PK |  | NO | - |
| FRMLTYPE_Active | varchar |  |  | SI | Active |
| FRMLTYPE_Code | varchar |  |  | NO | Code |
| FRMLTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FRMLTYPE_CreatedDate | date |  |  | SI | Created Date |
| FRMLTYPE_CreatedTime | time |  |  | SI | Created Time |
| FRMLTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FRMLTYPE_DateFrom | date |  |  | SI | Date From |
| FRMLTYPE_DateTo | date |  |  | SI | Date To |
| FRMLTYPE_Desc | varchar |  |  | NO | Description |
| FRMLTYPE_NationalCode | varchar |  |  | SI | National Code |
| FRMLTYPE_Owner | varchar |  |  | SI | Owner |
| FRMLTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| FRMLTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| FRMLTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Over the last two weeks how often have you been bo... |
| Q02 | - |  |  | SI | Little interest or pleasure in doing things |
| Q03 | - |  |  | SI | Feeling down, depressed or hopeless |
| Q04 | - |  |  | SI | Trouble falling or staying asleep or sleeping too ... |
| Q05 | - |  |  | SI | Feeling tired or having little energy |
| Q06 | - |  |  | SI | Poor appetite or over-eating |
| Q07 | - |  |  | SI | Feeling bad about yourself – or that you are a fai... |
| Q08 | - |  |  | SI | Trouble concentrating on things, such as reading t... |
| Q09 | - |  |  | SI | Moving or speaking so slowly that other people cou... |
| Q10 | - |  |  | SI | Thoughts that you would be better off dead or of h... |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | None |
| Q14 | - |  |  | SI | 0 - 4 |
| Q15 | - |  |  | SI | Mild |
| Q16 | - |  |  | SI | 5 - 9 |
| Q17 | - |  |  | SI | Moderate |
| Q18 | - |  |  | SI | 10 - 14 |
| Q19 | - |  |  | SI | Moderately Severe |
| Q20 | - |  |  | SI | 15 - 19 |
| Q21 | - |  |  | SI | Severe |
| Q22 | - |  |  | SI | 20 - 27 |
| Q23 | - |  |  | SI | 0 to 4: None |
| Q24 | - |  |  | SI | 5 to 9: Mild |
| Q25 | - |  |  | SI | 10 to 14: Moderate |
| Q26 | - |  |  | SI | 15 to 19: Moderately Severe |
| Q27 | - |  |  | SI | 20 to 27: Severe |
| Q28 | - |  |  | SI | The patient health questionnaire (PHQ-9) is a mult... |
| Q29 | - |  |  | SI | Date |
| Q30 | - |  |  | SI | Time |
| Q31 | - |  |  | SI | If you checked off any problems, how difficult hav... |
| Q32 | - |  |  | SI | Notes |
| Q33 | - |  |  | SI | Kroenke K, Spitzer RL, Williams JBW. The PHQ‐9: Va... |
| Q34 | - |  |  | SI | No permission required to reproduce, translate, di... |
| Q35 | - |  |  | SI | If you checked off any problems, how difficult hav... |
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