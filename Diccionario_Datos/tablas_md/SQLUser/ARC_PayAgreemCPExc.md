# SQLUser.ARC_PayAgreemCPExc

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPEXC_ParRef | bigint | PK |  | NO | ARC_PayAgreement Parent Reference |
| CPEXC_AdmSource | varchar |  |  | SI | AdmSource |
| CPEXC_BillGrp | varchar |  |  | SI | ARCBillGrp |
| CPEXC_Childsub | double |  |  | NO | Childsub |
| CPEXC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CPEXC_CreatedDate | date |  |  | SI | Created Date |
| CPEXC_CreatedTime | time |  |  | SI | Created Time |
| CPEXC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPEXC_DischDestin | varchar |  |  | SI | DischargeDestination |
| CPEXC_MaxAnaesthDays | double |  |  | SI | Maximum Anaesthetic Records  |
| CPEXC_MaxBillGrpDays | double |  |  | SI | Maximum Billing Group Days |
| CPEXC_MaxItemsAnaestTheatre | double |  |  | SI | Maximum Items per Anaesthetic/Theatre Record |
| CPEXC_MaxRoomTypeDays | double |  |  | SI | Maximum Room Type Days  |
| CPEXC_RevertPerDiemNoTheatre | varchar |  |  | SI | Revert to Per Diem if no Theatre |
| CPEXC_RoomType | varchar |  |  | SI | RoomType |
| CPEXC_RowId | varchar |  |  | NO | - |
| CPEXC_UpdatedDate | date |  |  | SI | Updated Date |
| CPEXC_UpdatedTime | time |  |  | SI | Updated Time |
| CPEXC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Responsable |
| Q02 | - |  |  | SI | ¿A quién se aplica? |
| Q03 | - |  |  | SI | Estadio en el que se encuentra el paciente |
| Q04 | - |  |  | SI | No aplica |
| Q05 | - |  |  | SI | Observaciones |
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