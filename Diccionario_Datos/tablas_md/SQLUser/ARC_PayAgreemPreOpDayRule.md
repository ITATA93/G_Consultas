# SQLUser.ARC_PayAgreemPreOpDayRule

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREOPD_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| PREOPD_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| PREOPD_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| PREOPD_Childsub | double |  |  | NO | Childsub |
| PREOPD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PREOPD_CreatedDate | date |  |  | SI | Created Date |
| PREOPD_CreatedTime | time |  |  | SI | Created Time |
| PREOPD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PREOPD_DateFrom | date |  |  | SI | Date From |
| PREOPD_DateTo | date |  |  | SI | Date To |
| PREOPD_PreOpDays | double |  |  | SI | PreOpDays |
| PREOPD_RowId | varchar |  |  | NO | - |
| PREOPD_StartCasePaymDayOT | varchar |  |  | SI | Start Case Payment on day of OT |
| PREOPD_UpdatedDate | date |  |  | SI | Updated Date |
| PREOPD_UpdatedTime | time |  |  | SI | Updated Time |
| PREOPD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Escala Visual de Fragilidad (EVF) |
| Q02 | - |  |  | SI | Actividades Básicas de la Vida Diaria (ABVD) |
| Q03 | - |  |  | SI | Comer |
| Q04 | - |  |  | SI | Vestirse |
| Q05 | - |  |  | SI | Bañarse |
| Q06 | - |  |  | SI | Usar el retrete |
| Q07 | - |  |  | SI | Arreglarse (lavado de dientes, peinado) |
| Q08 | - |  |  | SI | Continencia de esfínter (Independiente v/s uso pañ... |
| Q09 | - |  |  | SI | Trasnferencia a sillón |
| Q10 | - |  |  | SI | Marcha |
| Q11 | - |  |  | SI | Subir escaleras |
| Q12 | - |  |  | SI | Actividades Instrumentales de la Vida Diaria (AIVD... |
| Q13 | - |  |  | SI | Comprar |
| Q14 | - |  |  | SI | Tomar medicamentos |
| Q15 | - |  |  | SI | Usar teléfono |
| Q16 | - |  |  | SI | Manejar su dinero |
| Q17 | - |  |  | SI | Usar transporte público |
| Q18 | - |  |  | SI | Prepara alimentos |
| Q19 | - |  |  | SI | Hacer aseo |
| Q20 | - |  |  | SI | Lavar su ropa |
| Q21 | - |  |  | SI | Imagen EVF |
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