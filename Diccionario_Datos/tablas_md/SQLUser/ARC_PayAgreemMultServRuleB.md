# SQLUser.ARC_PayAgreemMultServRuleB

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MSRULEB_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| MSRULEB_Childsub | double |  |  | NO | Childsub |
| MSRULEB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MSRULEB_CreatedDate | date |  |  | SI | Created Date |
| MSRULEB_CreatedTime | time |  |  | SI | Created Time |
| MSRULEB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MSRULEB_DateFrom | date |  |  | SI | Date From |
| MSRULEB_DateTo | date |  |  | SI | Date To |
| MSRULEB_ItemCatConsult_DR | bigint |  | FK | SI | Des Ref ARCItemCat Consultation |
| MSRULEB_ItemCatRType_DR | bigint |  | FK | SI | Des Ref ARCItemCat RType |
| MSRULEB_RowId | varchar |  |  | NO | - |
| MSRULEB_ScheduleFee1 | double |  |  | SI | Schedule Fee 1 |
| MSRULEB_ScheduleFee1Amount | double |  |  | SI | Schedule Fee 1 Amount |
| MSRULEB_ScheduleFee2 | double |  |  | SI | Schedule Fee 2 |
| MSRULEB_ScheduleFee2Amount | double |  |  | SI | Schedule Fee 2 Amount |
| MSRULEB_Tariff_DR | bigint |  | FK | SI | Des Ref ARCTariff |
| MSRULEB_UpdatedDate | date |  |  | SI | Updated Date |
| MSRULEB_UpdatedTime | time |  |  | SI | Updated Time |
| MSRULEB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | (Grade): Grado global de alteración vocal, o de di... |
| Q02 | - |  |  | SI | (Roughness): Importancia de la ronquera y aspereza |
| Q03 | - |  |  | SI | (Asthenicity): Grado de astenia o fatiga vocal |
| Q04 | - |  |  | SI | (Breathiness): Sensación de voz aérea, reflejando ... |
| Q05 | - |  |  | SI | (Strain): Evalúa el grado de tensión, constreñimie... |
| Q06 | - |  |  | SI | Observaciones/Interpretación |
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