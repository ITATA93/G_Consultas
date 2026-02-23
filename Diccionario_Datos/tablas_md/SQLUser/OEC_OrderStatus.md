# SQLUser.OEC_OrderStatus

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OSTAT_RowId | bigint | PK |  | NO | - |
| OSTAT_Activate | varchar |  |  | SI | Activate |
| OSTAT_Code | varchar |  |  | NO | Code |
| OSTAT_Color | varchar |  |  | SI | Color |
| OSTAT_CreatedDate | date |  |  | SI | Created Date |
| OSTAT_CreatedTime | time |  |  | SI | Created Time |
| OSTAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OSTAT_Desc | varchar |  |  | NO | Description |
| OSTAT_UpdatedDate | date |  |  | SI | Updated Date |
| OSTAT_UpdatedTime | time |  |  | SI | Updated Time |
| OSTAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Mechanism |
| Q01N | - |  |  | SI | Note |
| Q02 | - |  |  | SI | Describe injury |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Neck pain / injury |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Shouder pain / injury |
| Q04N | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Upper arm pain / injury |
| Q05N | - |  |  | SI | Note |
| Q06 | - |  |  | SI | Elbow pain / injury |
| Q06N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Forearm pain / injury |
| Q07N | - |  |  | SI | Note |
| Q08 | - |  |  | SI | Hand or wrist pain / injury |
| Q08N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Hip / proximal femur pain / injury |
| Q09N | - |  |  | SI | Note |
| Q09Y | - |  |  | SI | If yes |
| Q11 | - |  |  | SI | Thigh and femur pain / injury |
| Q11N | - |  |  | SI | Note |
| Q12 | - |  |  | SI | Knee pain / injury |
| Q12N | - |  |  | SI | Note |
| Q13 | - |  |  | SI | Calf / lower leg pain / injury |
| Q13N | - |  |  | SI | Note |
| Q14 | - |  |  | SI | Ankle pain / injury |
| Q14N | - |  |  | SI | Note |
| Q15 | - |  |  | SI | Foot pain / injury |
| Q15N | - |  |  | SI | Note |
| Q16 | - |  |  | SI | Lacerations or abrasions |
| Q16N | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Numbness or paresthesia distal to injury |
| Q17N | - |  |  | SI | Note |
| Q18 | - |  |  | SI | Weakness distal to injury |
| Q18N | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Cyanosis or discolouration distal to injury |
| Q19N | - |  |  | SI | Note |
| Q20 | - |  |  | SI | Inability to grasp or lift |
| Q20N | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Inability to walk or bear weight |
| Q21N | - |  |  | SI | Note |
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