# SQLUser.PAC_SourceOfAttendance

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ATTEND_RowId | bigint | PK |  | NO | - |
| ATTEND_BookPastGD | varchar |  |  | SI | BookPastGD |
| ATTEND_BookPastGDType | varchar |  |  | SI | BookPastGDType |
| ATTEND_Code | varchar |  |  | NO | Code |
| ATTEND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ATTEND_CreatedDate | date |  |  | SI | Created Date |
| ATTEND_CreatedTime | time |  |  | SI | Created Time |
| ATTEND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ATTEND_DateFrom | date |  |  | SI | Date From |
| ATTEND_DateTo | date |  |  | SI | Date To |
| ATTEND_Desc | varchar |  |  | NO | Description |
| ATTEND_EpisodeType | varchar |  |  | SI | Episode Type |
| ATTEND_MandatoryRefDoctor | varchar |  |  | SI | Mandatory Ref Doctor |
| ATTEND_MandatoryRefHospital | varchar |  |  | SI | Mandatory Ref Hospital |
| ATTEND_NationalCode | varchar |  |  | SI | National Code |
| ATTEND_Owner | varchar |  |  | SI | Owner |
| ATTEND_RefType | varchar |  |  | SI | Referrer Type |
| ATTEND_StatisticIndicator | varchar |  |  | SI | Status Indicator |
| ATTEND_UpdatedDate | date |  |  | SI | Updated Date |
| ATTEND_UpdatedTime | time |  |  | SI | Updated Time |
| ATTEND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Cardiac procedure |
| Q04 | - |  |  | SI | Other procedure |
| Q05 | - |  |  | SI | Date accepted |
| Q06 | - |  |  | SI | Date of procedure |
| Q07 | - |  |  | SI | Current admission status |
| Q08 | - |  |  | SI | Community |
| Q09 | - |  |  | SI | Primary health care provider |
| Q10 | - |  |  | SI | Referral to receiving hospital sent |
| Q11 | - |  |  | SI | Referral to receiving hospital received |
| Q12 | - |  |  | SI | Receiving hospital |
| Q13 | - |  |  | SI | Receiving doctor |
| Q14 | - |  |  | SI | Receiving hospital notified |
| Q15 | - |  |  | SI | Primary health care provider notified |
| Q16 | - |  |  | SI | Primary health care provider notified of travel da... |
| Q17 | - |  |  | SI | Rheumatic heart disease register notified |
| Q18 | - |  |  | SI | Receiving hospital aboriginal liaison officer noti... |
| Q19 | - |  |  | SI | Patient aware |
| Q20 | - |  |  | SI | Renal patient |
| Q21 | - |  |  | SI | On dialysis |
| Q22 | - |  |  | SI | Current renal services notified |
| Q23 | - |  |  | SI | Receiving renal services notified |
| Q24 | - |  |  | SI | Notification notes |
| Q25 | - |  |  | SI | Screening tool sent to primary health care provide... |
| Q26 | - |  |  | SI | Dental clearance complete |
| Q27 | - |  |  | SI | Screening completed / forwarded to receiving hospi... |
| Q28 | - |  |  | SI | Screening notes |
| Q29 | - |  |  | SI | Date of travel |
| Q30 | - |  |  | SI | Escort name |
| Q31 | - |  |  | SI | Escort date of birth |
| Q32 | - |  |  | SI | Travel booking complete |
| Q33 | - |  |  | SI | Travel notes |
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