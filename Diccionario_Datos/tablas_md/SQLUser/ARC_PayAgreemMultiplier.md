# SQLUser.ARC_PayAgreemMultiplier

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MULT_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| MULT_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| MULT_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| MULT_Childsub | double |  |  | NO | Childsub |
| MULT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MULT_CreatedDate | date |  |  | SI | Created Date |
| MULT_CreatedTime | time |  |  | SI | Created Time |
| MULT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MULT_DateFrom | date |  |  | SI | Date From |
| MULT_DateTo | date |  |  | SI | Date To |
| MULT_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| MULT_EpisodeType | varchar |  |  | SI | EpisodeType |
| MULT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MULT_ItmMast_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| MULT_Multiplier | double |  |  | SI | Multiplier |
| MULT_Rank | double |  |  | SI | Rank |
| MULT_RowId | varchar |  |  | NO | - |
| MULT_ServCat_DR | bigint |  | FK | SI | Des Ref ARCServCat |
| MULT_UpdatedDate | date |  |  | SI | Updated Date |
| MULT_UpdatedTime | time |  |  | SI | Updated Time |
| MULT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Condición Física General |
| Q02 | - |  |  | SI | Estado Mental |
| Q03 | - |  |  | SI | Movilidad |
| Q04 | - |  |  | SI | Actividad |
| Q05 | - |  |  | SI | Nutrición&nbsp |
| Q06 | - |  |  | SI | Humedad |
| Q07 | - |  |  | SI | Riesgo Alto: Menor a 13 puntos. |
| Q08 | - |  |  | SI | Riesgo Moderado: Desde 13 hasta 17 puntos. |
| Q09 | - |  |  | SI | Riesgo Bajo: Mayor a 17 puntos. |
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