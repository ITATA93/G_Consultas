# SQLUser.OE_IconAck

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICONACK_RowId | bigint | PK |  | NO | - |
| ICONACK_Date | date |  |  | SI | Date |
| ICONACK_Display | varchar |  |  | SI | Display |
| ICONACK_IconCode | varchar |  |  | SI | IconCode |
| ICONACK_OrdItem_DR | varchar |  | FK | SI | Des Ref OrdItem |
| ICONACK_Time | time |  |  | SI | Time  |
| ICONACK_User_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q01 | - |  |  | SI | Hand Strength Assessment |
| Q02 | - |  |  | SI | Jamar Dynamometer |
| Q03 | - |  |  | SI | Grip Strength (Left) No 1 |
| Q03ObsDR | - |  |  | SI | Grip Strength (Left) No 1 DR |
| Q04 | - |  |  | SI | Grip Strength (Left) No 2 |
| Q04ObsDR | - |  |  | SI | Grip Strength (Left) No 2 DR |
| Q05 | - |  |  | SI | Grip Strength (Left) No 3 |
| Q05ObsDR | - |  |  | SI | Grip Strength (Left) No 3 DR |
| Q06 | - |  |  | SI | Grip Strength Average (Left) |
| Q06ObsDR | - |  |  | SI | Grip Strength Average (Left)  DR |
| Q07 | - |  |  | SI | Grip Strength Norm (Left) |
| Q07ObsDR | - |  |  | SI | Grip Strength Norm (Left) DR |
| Q08 | - |  |  | SI | Grip Strength (Right) No 1 |
| Q08ObsDR | - |  |  | SI | Grip Strength (Right) No 1 DR |
| Q09 | - |  |  | SI | Grip Strength (Right) No 2 |
| Q09ObsDR | - |  |  | SI | Grip Strength (Right) No 2 DR |
| Q10 | - |  |  | SI | Grip Strength (Right) No 3 |
| Q10ObsDR | - |  |  | SI | Grip Strength (Right) No 3 DR |
| Q11 | - |  |  | SI | Grip Strength Average (Right) |
| Q11ObsDR | - |  |  | SI | Grip Strength Average (Right) DR |
| Q12 | - |  |  | SI | Grip Strength Norm (Right) |
| Q12ObsDR | - |  |  | SI | Grip Strength Norm (Right) DR |
| Q13 | - |  |  | SI | Pinch Gauge |
| Q14 | - |  |  | SI | Lateral Pinch (Left) |
| Q14ObsDR | - |  |  | SI | Lateral Pinch (Left) DR |
| Q15 | - |  |  | SI | Lateral Pinch (Right) |
| Q15ObsDR | - |  |  | SI | Lateral Pinch (Right) DR |
| Q16 | - |  |  | SI | 3 Point Pinch (Left) |
| Q16ObsDR | - |  |  | SI | 3 Point Pinch (Left) DR |
| Q17 | - |  |  | SI | 3 Point Pinch (Right) |
| Q17ObsDR | - |  |  | SI | 3 Point Pinch (Right) DR |
| Q18 | - |  |  | SI | 2 Point Pinch (Left) |
| Q18ObsDR | - |  |  | SI | 2 Point Pinch (Left) DR |
| Q19 | - |  |  | SI | 2 Point Pinch (Right) |
| Q19ObsDR | - |  |  | SI | 2 Point Pinch (Right) DR |
| Q20 | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Occupational Therapist Name |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Signature |
| Q23UDt | - |  |  | SI | Signature Last Updated Date |
| Q23UTm | - |  |  | SI | Signature Last Updated Time |
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