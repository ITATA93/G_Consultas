# SQLUser.PAC_WLTypeOfOffers

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLTOF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Feeding (cutting, opening containers, pouring, bri... |
| Q02 | - |  |  | SI | Bathing (soaping, washing, drying body and head, m... |
| Q03 | - |  |  | SI | Upper body |
| Q04 | - |  |  | SI |  Lower body	 |
| Q05 | - |  |  | SI | Dressing (clothes, shoes, permanent orthoses: dres... |
| Q06 | - |  |  | SI | Upper body |
| Q07 | - |  |  | SI | Lower body	 |
| Q08 | - |  |  | SI | Grooming (washing hands and face, brushing teeth, ... |
| Q09 | - |  |  | SI | Sub Total ( Self-Care ) |
| Q10 | - |  |  | SI | Respiration |
| Q11 | - |  |  | SI | Sphincter Management - Bladder 	 |
| Q12 | - |  |  | SI | Sphincter Management - Bowel	 |
| Q13 | - |  |  | SI | Use of Toilet (perineal hygiene, adjustment of clo... |
| Q14 | - |  |  | SI | Sub Total	( Respiration and Sphincter Management ) |
| Q15 | - |  |  | SI | Mobility in Bed and Action to Prevent Pressure Sor... |
| Q16 | - |  |  | SI | Transfers: bed-wheelchair  (locking wheelchair, li... |
| Q17 | - |  |  | SI | Transfers: wheelchair-toilet-tub (if uses toilet w... |
| Q18 | - |  |  | SI | Mobility (indoor and outdoor on even surface)	 |
| Q19 | - |  |  | SI | Mobility Indoors	 |
| Q20 | - |  |  | SI | Mobility for Moderate Distances (10-100 meters)	 |
| Q21 | - |  |  | SI | Mobility Outdoors (more than 100 meters)	 |
| Q22 | - |  |  | SI | Stair Management	 |
| Q23 | - |  |  | SI | Transfers: wheelchair-car (approaching car, lockin... |
| Q24 | - |  |  | SI | Transfers: ground-wheelchair	 |
| Q25 | - |  |  | SI | Sub Total	( Mobility ''room and toilet '' ) |
| Q26 | - |  |  | SI | Total Score |
| Q27 | - |  |  | SI | Completed at |
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
| WLTOF_Code | varchar |  |  | NO | Code |
| WLTOF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLTOF_CreatedDate | date |  |  | SI | Created Date |
| WLTOF_CreatedTime | time |  |  | SI | Created Time |
| WLTOF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLTOF_DateFrom | date |  |  | SI | DateFrom |
| WLTOF_DateTo | date |  |  | SI | DateTo |
| WLTOF_Desc | varchar |  |  | NO | Description |
| WLTOF_FieldToDenote | varchar |  |  | SI | FieldToDenote |
| WLTOF_Owner | varchar |  |  | SI | Owner |
| WLTOF_ResetOfferOutcome | varchar |  |  | SI | ResetOfferOutcome |
| WLTOF_UpdatedDate | date |  |  | SI | Updated Date |
| WLTOF_UpdatedTime | time |  |  | SI | Updated Time |
| WLTOF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*