# SQLUser.BLC_DRG_Tariff

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TAR_RowId | bigint | PK |  | NO | - |
| ChildQ07DR | - |  |  | SI | Child Reference: Sesiones |
| Q01 | - |  |  | SI | Sector |
| Q02 | - |  |  | SI | Telefono |
| Q03 | - |  |  | SI | Hospitalización |
| Q04 | - |  |  | SI | Fecha |
| Q05 | - |  |  | SI | Diagnóstico |
| Q06 | - |  |  | SI | Resultado EFAM |
| Q08 | - |  |  | SI | Índice de comorbilidad de Charlson |
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
| TAR_Class1_DR | bigint |  | FK | SI | Des Ref Class1 |
| TAR_Class2_DR | bigint |  | FK | SI | Des Ref Class2 |
| TAR_Class3_DR | bigint |  | FK | SI | Des Ref Class3 |
| TAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TAR_CostWeightEdition_DR | bigint |  | FK | SI | Des Ref CostWeightEdition |
| TAR_CreatedDate | date |  |  | SI | Created Date |
| TAR_CreatedTime | time |  |  | SI | Created Time |
| TAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TAR_DRGCategory_DR | bigint |  | FK | SI | Des Ref DRGCategory |
| TAR_DRGType_DR | bigint |  | FK | SI | Des Ref DRG Type |
| TAR_DRG_DR | bigint |  | FK | SI | Des Ref DRG |
| TAR_DateFrom | date |  |  | NO | Date From |
| TAR_DayHospitalTariff | double |  |  | SI | Day Hospital Tariff |
| TAR_ExtraHighTrimPoint | double |  |  | SI | Extra High Trim Point |
| TAR_ExtraTariffPerDay | double |  |  | SI | Extra Tariff Per Day |
| TAR_HITH_Outlier | double |  |  | SI | HITH Outlier |
| TAR_HospDRGCateg_DR | bigint |  | FK | SI | Des Ref HospDRGCateg |
| TAR_Kind | varchar |  |  | SI | Kind |
| TAR_LimitDay | double |  |  | SI | Limit Day |
| TAR_MedTarget | varchar |  |  | SI | Med Target |
| TAR_NormalTariff | double |  |  | SI | Normal Tariff |
| TAR_OneDayTariff | double |  |  | SI | One Day Tariff |
| TAR_Owner | varchar |  |  | SI | Owner |
| TAR_ReabilitaionExtraTariffPerDay | double |  |  | SI | Reabilitaion Extra Tariff Per Day |
| TAR_ReabilitaionLimitDay | double |  |  | SI | Reabilitaion Limit Day |
| TAR_ReabilitationTariff | double |  |  | SI | Reabilitation Tariff |
| TAR_SameDayOneDay | varchar |  |  | SI | SameDay/OneDay |
| TAR_ShortStayFlag_DR | bigint |  | FK | SI | Des Ref MRCShortStayFlag |
| TAR_ShortStayTariff | double |  |  | SI | Short Stay Tariff |
| TAR_UpdatedDate | date |  |  | SI | Updated Date |
| TAR_UpdatedTime | time |  |  | SI | Updated Time |
| TAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| TAR_Version_DR | bigint |  | FK | SI | Des Ref Version |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*