# SQLUser.FHC_Area

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCA_RowId | bigint | PK |  | NO | - |
| FHCA_Code | varchar |  |  | NO | Area Code |
| FHCA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCA_CreatedDate | date |  |  | SI | Created Date |
| FHCA_CreatedTime | time |  |  | SI | Created Time |
| FHCA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCA_DateFrom | date |  |  | NO | Date From |
| FHCA_DateTo | date |  |  | SI | Date To |
| FHCA_Desc | varchar |  |  | NO | Area Description |
| FHCA_Hosp_DR | bigint |  | FK | SI | Des Ref to CTHospital |
| FHCA_NationalCode | varchar |  |  | SI | National Code |
| FHCA_Owner | varchar |  |  | SI | Owner |
| FHCA_Segment_DR | bigint |  | FK | SI | Des Ref to FHCSegment |
| FHCA_TypeOfArea_DR | bigint |  | FK | SI | Des Ref to FHCTypeOfArea |
| FHCA_UpdatedDate | date |  |  | SI | Updated Date |
| FHCA_UpdatedTime | time |  |  | SI | Updated Time |
| FHCA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Skin preparation |
| Q10 | - |  |  | SI | Body Map |
| Q11 | - |  |  | SI | Swab, needle and instrument count |
| Q12 | - |  |  | SI | Pre op count consultant / scrub practitioner |
| Q13 | - |  |  | SI | Pre op count circulating practitioner |
| Q14 | - |  |  | SI | Final count consultant / scrub practitioner |
| Q15 | - |  |  | SI | Final count circulating practitioner |
| Q16 | - |  |  | SI | Swabs, needles and instruments correct |
| Q17 | - |  |  | SI | If No, please indicate count discrepancy and actio... |
| Q18 | - |  |  | SI | Packs remaining in situ |
| Q19 | - |  |  | SI | Number |
| Q2 | - |  |  | SI | Irrigation fluid used |
| Q20 | - |  |  | SI | Type |
| Q21 | - |  |  | SI | Position |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
| Q24 | - |  |  | SI | Body map |
| Q3 | - |  |  | SI | Infiltration / anaesthetic type (specify) |
| Q4 | - |  |  | SI | Type and number of specimens (specify) |
| Q5 | - |  |  | SI | Diathermy plate/pad removed and site shows no adve... |
| Q6 | - |  |  | SI | Skin closure if applicable |
| Q7 | - |  |  | SI | If Other, please detail |
| Q8 | - |  |  | SI | Procedure performed |
| Q9 | - |  |  | SI | See operation note for any post procedural instruc... |
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