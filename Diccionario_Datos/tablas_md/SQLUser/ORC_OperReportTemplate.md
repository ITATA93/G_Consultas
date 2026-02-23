# SQLUser.ORC_OperReportTemplate

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPREPTMP_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: During Dobutamine Infusion |
| OPREPTMP_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| OPREPTMP_Code | varchar |  |  | NO | Code |
| OPREPTMP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPREPTMP_CreatedDate | date |  |  | SI | Created Date |
| OPREPTMP_CreatedTime | time |  |  | SI | Created Time |
| OPREPTMP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPREPTMP_DateFrom | date |  |  | SI | Date From |
| OPREPTMP_DateTo | date |  |  | SI | Date To |
| OPREPTMP_Desc | varchar |  |  | NO | Description |
| OPREPTMP_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| OPREPTMP_OperationNote | longvarchar |  |  | SI | Operation Note |
| OPREPTMP_Owner | varchar |  |  | SI | Owner |
| OPREPTMP_UpdatedDate | date |  |  | SI | Updated Date |
| OPREPTMP_UpdatedTime | time |  |  | SI | Updated Time |
| OPREPTMP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Nothing by mouth (NPO) for 4 hours before this pro... |
| Q04 | - |  |  | SI | Please notify the doctor |
| Q05 | - |  |  | SI | Has the patient discontinued their beta-blocker me... |
| Q06 | - |  |  | SI | Please notify the doctor |
| Q07 | - |  |  | SI | Target heart rate (/min) |
| Q08 | - |  |  | SI | Initial systolic BP (mmHg) |
| Q08ObsDR | - |  |  | SI | Initial systolic BP (mmHg) DR |
| Q09 | - |  |  | SI | Initial diastolic BP (mmHg) |
| Q09ObsDR | - |  |  | SI | Initial diastolic BP (mmHg) DR |
| Q10 | - |  |  | SI | Initial heart rate (/min) |
| Q10ObsDR | - |  |  | SI | Initial heart rate (/min) DR |
| Q13 | - |  |  | SI | Comment |
| Q14 | - |  |  | SI | Recorded by |
| Q15 | - |  |  | SI | Verified by |
| Q16 | - |  |  | SI | Signed (reporting physician) |
| Q16UDt | - |  |  | SI | Signed (reporting physician) Last Updated Date |
| Q16UTm | - |  |  | SI | Signed (reporting physician) Last Updated Time |
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