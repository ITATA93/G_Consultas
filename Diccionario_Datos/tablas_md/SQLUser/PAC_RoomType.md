# SQLUser.PAC_RoomType

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOMT_RowId | bigint | PK |  | NO | - |
| ChildQ7DR | - |  |  | SI | Child Reference: Recovery of responsiveness and en... |
| Q1 | - |  |  | SI | Timing |
| Q10 | - |  |  | SI | Transfer recovery planned? |
| Q12 | - |  |  | SI | Walking recovery planned? |
| Q14 | - |  |  | SI | Stairs recovery planned? |
| Q16 | - |  |  | SI | Pain control planned? |
| Q18 | - |  |  | SI | Fall prevention planned? |
| Q2 | - |  |  | SI | Timing, notes |
| Q20 | - |  |  | SI | Family / Social / Work reintegration (prescription... |
| Q22 | - |  |  | SI | Physiotherapist plan notes |
| Q23 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Time |
| Q25 | - |  |  | SI | Recovery / Improvement of autonomy in activities o... |
| Q3 | - |  |  | SI | Goals planned |
| Q4 | - |  |  | SI | Clinical stability and secondary damage prevention... |
| Q6 | - |  |  | SI | Recovery of responsiveness and environmental conta... |
| Q8 | - |  |  | SI | Recovery / improvement of motor / sensory impairme... |
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
| ROOMT_ARCIM_DR | varchar |  | FK | SI | Des REf ARCIM |
| ROOMT_AccommodationCode_DR | bigint |  | FK | SI | Des Ref Accommodation Code |
| ROOMT_BillByMinutes | varchar |  |  | SI | Bill By Minutes |
| ROOMT_Code | varchar |  |  | NO | Code |
| ROOMT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROOMT_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| ROOMT_CreatedDate | date |  |  | SI | Created Date |
| ROOMT_CreatedTime | time |  |  | SI | Created Time |
| ROOMT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOMT_DateFrom | date |  |  | SI | Date From |
| ROOMT_DateTo | date |  |  | SI | Date To |
| ROOMT_Desc | varchar |  |  | NO | Description |
| ROOMT_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| ROOMT_HCPValue | varchar |  |  | SI | HCP Value |
| ROOMT_Owner | varchar |  |  | SI | Owner |
| ROOMT_PrivateRoom | varchar |  |  | SI | Private Room |
| ROOMT_Rank | double |  |  | SI | Rank |
| ROOMT_StepDownDay1 | varchar |  |  | SI | Step Down Day 1 |
| ROOMT_UpdatedDate | date |  |  | SI | Updated Date |
| ROOMT_UpdatedTime | time |  |  | SI | Updated Time |
| ROOMT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*