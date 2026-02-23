# SQLUser.CT_ProviderDigitalAccess

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRODA_RowId | bigint | PK |  | NO | - |
| PRODA_AuthorisationCode | varchar |  |  | SI | Authorisation Code |
| PRODA_Code | varchar |  |  | NO | ID |
| PRODA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRODA_CreatedDate | date |  |  | SI | Created Date |
| PRODA_CreatedTime | time |  |  | SI | Created Time |
| PRODA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRODA_DateFrom | date |  |  | SI | Date From |
| PRODA_DateTo | date |  |  | SI | Date To |
| PRODA_Desc | varchar |  |  | NO | Organisation ID |
| PRODA_DeviceExpiryDate | date |  |  | SI | Device Expiry Date |
| PRODA_DeviceExpiryTime | time |  |  | SI | Device Expiry Time |
| PRODA_DeviceName | varchar |  |  | NO | Device Name |
| PRODA_DeviceStatusActive | varchar |  |  | SI | Device Status Active |
| PRODA_DigitalAccessAction_DR | bigint |  | FK | SI | Des RefCTDigitalAccessAction |
| PRODA_ErrorCode | varchar |  |  | SI | Error Code |
| PRODA_ErrorDescription | varchar |  |  | SI | Error Description |
| PRODA_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PRODA_KeyExpiryDate | date |  |  | SI | Key Expiry Date |
| PRODA_KeyExpiryTime | time |  |  | SI | Key Expiry Time |
| PRODA_KeyStatusActive | varchar |  |  | SI | Key Status Active |
| PRODA_MinorID | varchar |  |  | SI | Minor ID |
| PRODA_Owner | varchar |  |  | SI | Owner |
| PRODA_PrivateKey | varchar |  |  | SI | Private Key |
| PRODA_PublicKey | varchar |  |  | SI | Public Key |
| PRODA_UpdatedDate | date |  |  | SI | Updated Date |
| PRODA_UpdatedTime | time |  |  | SI | Updated Time |
| PRODA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Prescribed treatment completed |
| Q04 | - |  |  | SI | Reason prescribed treatment was not completed |
| Q05 | - |  |  | SI | Initial drain (mls) |
| Q06 | - |  |  | SI | Total ultrafiltration (mls) |
| Q07 | - |  |  | SI | Average dwell time (min) |
| Q08 | - |  |  | SI | Lost dwell time (min) |
| Q09 | - |  |  | SI | Added dwell time (min) |
| Q10 | - |  |  | SI | Machine alarms / issues during treatment |
| Q11 | - |  |  | SI | Machine alarms / issues details |
| Q12 | - |  |  | SI | Effluent clarity |
| Q13 | - |  |  | SI | Other effluent clarity details, if applicable |
| Q14 | - |  |  | SI | Catheter securely immobilised |
| Q15 | - |  |  | SI | Other catheter securely immobilised details |
| Q16 | - |  |  | SI | Exit site condition |
| Q17 | - |  |  | SI | Action taken |
| Q18 | - |  |  | SI | Exit site dressing attended |
| Q19 | - |  |  | SI | Reason why exit site dressing not attended to |
| Q20 | - |  |  | SI | Attended by |
| Q21 | - |  |  | SI | Automated dialysis notes |
| Q22 | - |  |  | SI | Effluent clarity |
| Q23 | - |  |  | SI | Effluent clarity |
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