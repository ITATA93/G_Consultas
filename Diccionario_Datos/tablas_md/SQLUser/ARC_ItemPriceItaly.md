# SQLUser.ARC_ItemPriceItaly

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ITP_AccoutCode | varchar |  |  | SI | Account Code |
| ITP_BaseUnit | double |  |  | SI | Base Unit |
| ITP_BedType_DR | bigint |  | FK | SI | Des Ref BedType |
| ITP_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| ITP_Childsub | double |  |  | NO | Childsub |
| ITP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITP_Country_DR | bigint |  | FK | SI | Des Ref to CTCountry |
| ITP_CreatedDate | date |  |  | SI | Created Date |
| ITP_CreatedTime | time |  |  | SI | Created Time |
| ITP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITP_Currency_DR | bigint |  | FK | SI | Des Ref Currency |
| ITP_DateFrom | date |  |  | NO | Date From |
| ITP_DateTo | date |  |  | SI | Date To |
| ITP_DayFrom | integer |  |  | SI | Day From |
| ITP_DayTo | integer |  |  | SI | Day To |
| ITP_EpisBill_DR | bigint |  | FK | SI | Des Ref EpisBill |
| ITP_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| ITP_EpisodeType | varchar |  |  | SI | Episode Type |
| ITP_ExcludeVAT | varchar |  |  | SI | ExcludeVAT |
| ITP_ExternalCareProv | varchar |  |  | SI | External Care Provider |
| ITP_HospitalDR | bigint |  | FK | SI | Hospital dr |
| ITP_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| ITP_Location_DR | bigint |  | FK | SI | Des Ref Location |
| ITP_MainOrderTariffPrice | varchar |  |  | SI | Main Order Tariff Price |
| ITP_NationalityGroup_DR | bigint |  | FK | SI | Des Ref to CTNationalityGroup |
| ITP_OperCateg_DR | bigint |  | FK | SI | Des Ref ORCOperationCategory |
| ITP_PayorAmt | double |  |  | SI | PayorAmt |
| ITP_PayorGroup_DR | bigint |  | FK | SI | Des Ref PayorGroup |
| ITP_PayorShare | double |  |  | SI | Payor Share |
| ITP_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| ITP_Price | double |  |  | NO | Price |
| ITP_Rank | double |  |  | SI | Rank |
| ITP_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ITP_RowId | varchar |  |  | NO | - |
| ITP_Speciality_DR | bigint |  | FK | SI | Des Ref Speciality |
| ITP_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| ITP_UOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| ITP_UpdatedDate | date |  |  | SI | Updated Date |
| ITP_UpdatedTime | time |  |  | SI | Updated Time |
| ITP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ITP_UrgentFee | double |  |  | SI | UrgentFee |
| ITP_UrgentFeeRate | double |  |  | SI | ITP_UrgentFeeRate |
| QEpisodeID | - |  |  | SI | EpisodeID |
| QFecha | - |  |  | SI | Fecha Executado |
| QHora | - |  |  | SI | Hora Executado |
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
| QUsuario | - |  |  | SI | Usuario |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*