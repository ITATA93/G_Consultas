# SQLUser.ORC_CannulaInsertionSite

**Schema:** SQLUser
**Columnas:** 141
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAINSI_RowId | bigint | PK |  | NO | - |
| CAINSI_Code | varchar |  |  | NO | Code |
| CAINSI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CAINSI_CreatedDate | date |  |  | SI | Created Date |
| CAINSI_CreatedTime | time |  |  | SI | Created Time |
| CAINSI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CAINSI_DateFrom | date |  |  | SI | Date From |
| CAINSI_DateTo | date |  |  | SI | Date To |
| CAINSI_Desc | varchar |  |  | NO | Description |
| CAINSI_Owner | varchar |  |  | SI | Owner |
| CAINSI_UpdatedDate | date |  |  | SI | Updated Date |
| CAINSI_UpdatedTime | time |  |  | SI | Updated Time |
| CAINSI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Performing the Assessment of Neuromuscular Maturit... |
| Q02 | - |  |  | SI | Posture |
| Q03 | - |  |  | SI | Square Window (Wrist) |
| Q04 | - |  |  | SI | Arm recoil |
| Q05 | - |  |  | SI | Popliteal angle |
| Q06 | - |  |  | SI | Scarf sign |
| Q07 | - |  |  | SI | Heel to ear |
| Q08 | - |  |  | SI | Performing the Assessment of Physical Activity |
| Q09 | - |  |  | SI | Skin |
| Q10 | - |  |  | SI | Lanugo |
| Q11 | - |  |  | SI | Plantar surface |
| Q12 | - |  |  | SI | Breast |
| Q13 | - |  |  | SI | Eye / ear |
| Q14 | - |  |  | SI | Genitals (Male) |
| Q15 | - |  |  | SI | Genitals (Female) |
| Q16 | - |  |  | SI | Total Neuromuscular Maturity Score |
| Q17 | - |  |  | SI | Total Physical Maturity Score |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Gest. Age by Maturity Rating (weeks) |
| Q20 | - |  |  | SI | Time of exam |
| Q21 | - |  |  | SI | Date of exam |
| Q22 | - |  |  | SI | Age at exam (hours) |
| Q23 | - |  |  | SI | Gestation by dates (weeks) |
| Q24 | - |  |  | SI | Birth date (hour) |
| Q25 | - |  |  | SI | APGAR (1 min) |
| Q26 | - |  |  | SI | APGAR (5 min) |
| Q27 | - |  |  | SI | Maturity Ring |
| Q28 | - |  |  | SI | Total Score |
| Q29 | - |  |  | SI | -10 |
| Q30 | - |  |  | SI | -5 |
| Q31 | - |  |  | SI | 0 |
| Q32 | - |  |  | SI | 5 |
| Q33 | - |  |  | SI | 10 |
| Q34 | - |  |  | SI | 15 |
| Q35 | - |  |  | SI | 20 |
| Q36 | - |  |  | SI | 25 |
| Q37 | - |  |  | SI | 30 |
| Q38 | - |  |  | SI | 35 |
| Q39 | - |  |  | SI | 40 |
| Q40 | - |  |  | SI | 45 |
| Q41 | - |  |  | SI | 50 |
| Q42 | - |  |  | SI | Weeks |
| Q43 | - |  |  | SI | 20 |
| Q44 | - |  |  | SI | 22 |
| Q45 | - |  |  | SI | 24 |
| Q46 | - |  |  | SI | 26 |
| Q47 | - |  |  | SI | 28 |
| Q48 | - |  |  | SI | 30 |
| Q49 | - |  |  | SI | 32 |
| Q50 | - |  |  | SI | 34 |
| Q51 | - |  |  | SI | 36 |
| Q52 | - |  |  | SI | 38 |
| Q53 | - |  |  | SI | 40 |
| Q54 | - |  |  | SI | 42 |
| Q55 | - |  |  | SI | 44 |
| Q56 | - |  |  | SI | Date |
| Q57 | - |  |  | SI | Time |
| Q58 | - |  |  | SI | Ballard JL, Khoury JC, Wedig KL, Wang L, Eilers-Wa... |
| Q59 | - |  |  | SI | A system for estimating newborn gestational age by... |
| Q60 | - |  |  | SI | Total Score |
| Q61 | - |  |  | SI | -10 |
| Q62 | - |  |  | SI | -5 |
| Q63 | - |  |  | SI | 0 |
| Q64 | - |  |  | SI | 5 |
| Q65 | - |  |  | SI | 10 |
| Q66 | - |  |  | SI | 15 |
| Q67 | - |  |  | SI | 20 |
| Q68 | - |  |  | SI | 25 |
| Q69 | - |  |  | SI | 30 |
| Q70 | - |  |  | SI | 35 |
| Q71 | - |  |  | SI | 40 |
| Q72 | - |  |  | SI | 45 |
| Q73 | - |  |  | SI | 50 |
| Q74 | - |  |  | SI | Weeks |
| Q75 | - |  |  | SI | 20 |
| Q76 | - |  |  | SI | 22 |
| Q77 | - |  |  | SI | 24 |
| Q78 | - |  |  | SI | 26 |
| Q79 | - |  |  | SI | 28 |
| Q80 | - |  |  | SI | 30 |
| Q81 | - |  |  | SI | 32 |
| Q82 | - |  |  | SI | 34 |
| Q83 | - |  |  | SI | 36 |
| Q84 | - |  |  | SI | 38 |
| Q85 | - |  |  | SI | 40 |
| Q86 | - |  |  | SI | 42 |
| Q87 | - |  |  | SI | 44 |
| Q88 | - |  |  | SI | Please refer to the maturity ring score table in t... |
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