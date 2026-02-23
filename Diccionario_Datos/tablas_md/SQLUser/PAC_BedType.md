# SQLUser.PAC_BedType

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BEDTP_RowId | bigint | PK |  | NO | - |
| BEDTP_BedTypeCode_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| BEDTP_CalcAverAccom | varchar |  |  | SI | CalcAverAccom |
| BEDTP_Code | varchar |  |  | NO | Bed Type Code |
| BEDTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BEDTP_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| BEDTP_CreatedDate | date |  |  | SI | Created Date |
| BEDTP_CreatedTime | time |  |  | SI | Created Time |
| BEDTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BEDTP_DateFrom | date |  |  | SI | Date From |
| BEDTP_DateTo | date |  |  | SI | Date To |
| BEDTP_DaySurgeryFlag | varchar |  |  | SI | Day Surgery Flag |
| BEDTP_Desc | varchar |  |  | NO | Bed Type Description |
| BEDTP_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| BEDTP_ICUFlag | varchar |  |  | SI | ICU Flag |
| BEDTP_IconExpr | varchar |  |  | SI | Icon Expression |
| BEDTP_IconName | varchar |  |  | SI | Icon Name |
| BEDTP_MaternityFlag | varchar |  |  | SI | Maternity Bed Flag |
| BEDTP_NNICFlag | varchar |  |  | SI | NNIC Bed Flag |
| BEDTP_Owner | varchar |  |  | SI | Owner |
| BEDTP_RcFlag | varchar |  |  | SI | Archived Flag |
| BEDTP_RoomType_DR | bigint |  | FK | SI | Des Ref to ARCIM |
| BEDTP_UpdatedDate | date |  |  | SI | Updated Date |
| BEDTP_UpdatedTime | time |  |  | SI | Updated Time |
| BEDTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Treatment name |
| Q02 | - |  |  | SI | Treatment duration |
| Q03 | - |  |  | SI | Previous treatment |
| Q04 | - |  |  | SI | Patients Given Name |
| Q05 | - |  |  | SI | Patient's Surname |
| Q06 | - |  |  | SI | I, |
| Q07 | - |  |  | SI | • Flu like symptoms |
| Q08 | - |  |  | SI | • Skin rashes, itchiness, dry skin |
| Q09 | - |  |  | SI | • Loss of appetite, nausea, diarrhoea |
| Q10 | - |  |  | SI | I agree to inform the hospital pharmacy at least o... |
| Q11 | - |  |  | SI | Patient's signature |
| Q11UDt | - |  |  | SI | Patient's signature Last Updated Date |
| Q11UTm | - |  |  | SI | Patient's signature Last Updated Time |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | , agree to commence treatment for my liver disease... |
| Q14 | - |  |  | SI | Pathology service |
| Q15 | - |  |  | SI | Genotype |
| Q16 | - |  |  | SI | Fibroscan / Genotype result |
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