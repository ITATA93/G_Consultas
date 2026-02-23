# SQLUser.ARC_PayAgreemTarAdjBillSub

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BS_ParRef | varchar | PK |  | NO | ARC_PayAgreemTarAdjust Parent Reference |
| BS_Adjustment | double |  |  | SI | Adjustment |
| BS_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| BS_Childsub | double |  |  | NO | Childsub |
| BS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BS_CreatedDate | date |  |  | SI | Created Date |
| BS_CreatedTime | time |  |  | SI | Created Time |
| BS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BS_DateFrom | date |  |  | SI | Date From |
| BS_DateTo | date |  |  | SI | Date To |
| BS_MultFactor | double |  |  | SI | Multiplier Factor |
| BS_RowId | varchar |  |  | NO | - |
| BS_Type | varchar |  |  | SI | Type |
| BS_UpdatedDate | date |  |  | SI | Updated Date |
| BS_UpdatedTime | time |  |  | SI | Updated Time |
| BS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ10DR | - |  |  | SI | Child Reference: Intervención con Usuario |
| Q01 | - |  |  | SI | Medicamento (princicio activo) |
| Q02 | - |  |  | SI | RNM |
| Q03 | - |  |  | SI | PRM |
| Q04 | - |  |  | SI | Observaciones |
| Q05 | - |  |  | SI | ¿Potencial o presente? |
| Q06 | - |  |  | SI | Medida de intervención |
| Q07 | - |  |  | SI | Justificación |
| Q08 | - |  |  | SI | Meta |
| Q11 | - |  |  | SI | Avance 1 |
| Q12 | - |  |  | SI | Avance 2 |
| Q13 | - |  |  | SI | ¿Resuelto? |
| Q14 | - |  |  | SI | Decisión |
| Q15 | - |  |  | SI | Medicamento (principio activo) |
| Q16 | - |  |  | SI | RNM |
| Q17 | - |  |  | SI | PRM |
| Q18 | - |  |  | SI | Observaciones |
| Q19 | - |  |  | SI | ¿Potencial o presente? |
| Q20 | - |  |  | SI | Medida de intervención |
| Q21 | - |  |  | SI | Justificación |
| Q22 | - |  |  | SI | Meta |
| Q25 | - |  |  | SI | Avance 1 |
| Q26 | - |  |  | SI | Avance 2 |
| Q27 | - |  |  | SI | ¿Resuelto? |
| Q28 | - |  |  | SI | Decición |
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