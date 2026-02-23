# SQLUser.PAC_DefaultAdmDepartment

**Schema:** SQLUser
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEFDEP_RowId | bigint | PK |  | NO | - |
| DEFDEP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEFDEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEFDEP_CreatedDate | date |  |  | SI | Created Date |
| DEFDEP_CreatedTime | time |  |  | SI | Created Time |
| DEFDEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEFDEP_ExecLoc_DR | bigint |  | FK | NO | Des Ref CTLOC |
| DEFDEP_InsType_DR | bigint |  | FK | NO | Des Ref InsType |
| DEFDEP_Owner | varchar |  |  | SI | Owner |
| DEFDEP_RBC_ServiceGroup_DR | bigint |  | FK | NO | Des Ref RBC Service Group |
| DEFDEP_ServiceKey | varchar |  |  | SI | Service Key |
| DEFDEP_UpdatedDate | date |  |  | SI | Updated Date |
| DEFDEP_UpdatedTime | time |  |  | SI | Updated Time |
| DEFDEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | During the past 7 days, how often has your knee be... |
| Q04 | - |  |  | SI | During the past 7 days, how often has your knee ma... |
| Q05 | - |  |  | SI | During the past 7 days, how often did your knee ge... |
| Q06 | - |  |  | SI | During the past 7 days, how often have you been ab... |
| Q07 | - |  |  | SI | During the past 7 days, how often have you been ab... |
| Q08 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q09 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q10 | - |  |  | SI | During the past month, how often have you experien... |
| Q11 | - |  |  | SI | How much knee pain have you experienced in the pas... |
| Q12 | - |  |  | SI | Twisting / Pivoting on your injured knee when walk... |
| Q13 | - |  |  | SI | Fully straightening your injured knee |
| Q14 | - |  |  | SI | Fully bending your injured knee |
| Q15 | - |  |  | SI | Walking upstairs |
| Q16 | - |  |  | SI | Walking downstairs |
| Q17 | - |  |  | SI | Sitting with your injured knee bent |
| Q18 | - |  |  | SI | Standing upright on both legs for any amount of ti... |
| Q19 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q20 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q21 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q22 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q23 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q24 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q25 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q26 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q27 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q28 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q29 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q30 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q31 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q32 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q33 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q34 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q35 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q36 | - |  |  | SI | How often do you think about your knee problem? |
| Q37 | - |  |  | SI | How much have you changed your lifestyle because o... |
| Q38 | - |  |  | SI | How much do you trust your injured knee? |
| Q39 | - |  |  | SI | Overall, how much difficulty do you have with your... |
| Q40 | - |  |  | SI | How much difficulty have you had getting to school... |
| Q41 | - |  |  | SI | How much difficulty have you had to do things with... |
| Q42 | - |  |  | SI | Symptoms Score |
| Q43 | - |  |  | SI | Pain Score |
| Q44 | - |  |  | SI | ADL Score |
| Q45 | - |  |  | SI | Sports / Play Score |
| Q46 | - |  |  | SI | QOL Score |
| Q47 | - |  |  | SI | KOOS Symptoms Score |
| Q48 | - |  |  | SI | KOOS Pain Score |
| Q49 | - |  |  | SI | KOOS ADL Score |
| Q50 | - |  |  | SI | KOOS Sports / Play Score |
| Q51 | - |  |  | SI | KOOS QOL Score |
| Q52 | - |  |  | SI | Score |
| Q53 | - |  |  | SI | Classification |
| Q54 | - |  |  | SI | 0 |
| Q55 | - |  |  | SI | Representing extreme knee problems |
| Q56 | - |  |  | SI | 0 - 100 |
| Q57 | - |  |  | SI | Scores range from 0 to 100 with a score of 0 indic... |
| Q58 | - |  |  | SI | 0 - 100: Scores range from 0 to 100 with a score o... |
| Q59 | - |  |  | SI | 100: Representing no knee problems. |
| Q60 | - |  |  | SI | The KOOS-Child is a patient-reported scoring tool ... |
| Q61 | - |  |  | SI | During the past 7 days, how much difficulty have y... |
| Q62 | - |  |  | SI | Scores range from 0 to 100 with a score of 0 indic... |
| Q63 | - |  |  | SI | KOOS Symptoms Score |
| Q64 | - |  |  | SI | KOOS Pain Score |
| Q65 | - |  |  | SI | KOOS ADL Score |
| Q66 | - |  |  | SI | KOOS Sports / Play Score |
| Q67 | - |  |  | SI | KOOS QOL Score |
| Q68 | - |  |  | SI | KOOS Symptoms Score (DisplayOnly) |
| Q69 | - |  |  | SI | KOOS Pain Score (DisplayOnly) |
| Q70 | - |  |  | SI | KOOS ADL Score (DisplayOnly) |
| Q71 | - |  |  | SI | KOOS Sports / Play Score (DisplayOnly) |
| Q72 | - |  |  | SI | KOOS QOL Score (DisplayOnly) |
| Q73 | - |  |  | SI | Please always click Apply then Update to get the s... |
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