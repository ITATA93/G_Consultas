# SQLUser.MH_DetAgent

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGN_ParRef | bigint | PK |  | NO | MH_Detention Parent Reference |
| AGN_Address1 | varchar |  |  | SI | Address1 |
| AGN_Address2 | varchar |  |  | SI | Address2 |
| AGN_Agent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| AGN_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| AGN_Childsub | double |  |  | NO | Childsub |
| AGN_City_DR | bigint |  | FK | SI | Des Ref CTCity |
| AGN_Country_DR | bigint |  | FK | SI | Des Ref CTCountry |
| AGN_DateFrom | date |  |  | SI | DateFrom |
| AGN_DateTo | date |  |  | SI | DateTo |
| AGN_Deleted | varchar |  |  | SI | Deleted |
| AGN_GeneralPhone | varchar |  |  | SI | GeneralPhone |
| AGN_MainRole | varchar |  |  | SI | MainRole |
| AGN_Name | varchar |  |  | SI | Name |
| AGN_OtherPhone | varchar |  |  | SI | OtherPhone |
| AGN_PostCode_DR | bigint |  | FK | SI | Des Ref CTZip |
| AGN_Role_DR | bigint |  | FK | SI | Des Ref CTRole |
| AGN_RowId | varchar |  |  | NO | - |
| Q1DSinf | - |  |  | SI | Cota Inferior -1DS |
| Q1DSsup | - |  |  | SI | Cota Superior 1DS |
| Q2DSinf | - |  |  | SI | Cota Inferior -2DS |
| Q2DSsup | - |  |  | SI | Cota Superior 2DS |
| Q3DSinf | - |  |  | SI | Cota Inferior -3DS |
| Q3DSsup | - |  |  | SI | Cota Superior 3DS |
| QDias | - |  |  | SI | Edad Corregida en Días |
| QMEDIA | - |  |  | SI | Mediana |
| QMeses | - |  |  | SI | Edad Corregida en Meses |
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