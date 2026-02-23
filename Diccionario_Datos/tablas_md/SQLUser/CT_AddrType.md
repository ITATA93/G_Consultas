# SQLUser.CT_AddrType

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTADR_RowId | bigint | PK |  | NO | - |
| CTADR_Blk | double |  |  | SI | Block |
| CTADR_Code | varchar |  |  | NO | Address Type Code |
| CTADR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTADR_CreatedDate | date |  |  | SI | Created Date |
| CTADR_CreatedTime | time |  |  | SI | Created Time |
| CTADR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTADR_DateFrom | date |  |  | SI | Date From |
| CTADR_DateTo | date |  |  | SI | Date To |
| CTADR_Desc | varchar |  |  | NO | Address Type Description |
| CTADR_Level | double |  |  | SI | Level (allow input?) |
| CTADR_Mail | varchar |  |  | SI | Mail |
| CTADR_Owner | varchar |  |  | SI | Owner |
| CTADR_Priority | varchar |  |  | SI | Priority |
| CTADR_RestrictFromLookUp | varchar |  |  | SI | RestrictFromLookUp |
| CTADR_Street | double |  |  | SI | Street Name (allow input?) |
| CTADR_Unit | double |  |  | SI | Unit (allow input?) |
| CTADR_UpdatedDate | date |  |  | SI | Updated Date |
| CTADR_UpdatedTime | time |  |  | SI | Updated Time |
| CTADR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTADR_Zip | double |  |  | SI | Postal Code (allow input?) |
| Q01 | - |  |  | SI | 1. Investigación Preliminar / Prueba Indirecta de ... |
| Q02 | - |  |  | SI | Vigilancia |
| Q03 | - |  |  | SI | Tos y/o carraspeo (tos voluntaria) |
| Q04 | - |  |  | SI | Deglución exitosa |
| Q05 | - |  |  | SI | Sialorrea |
| Q06 | - |  |  | SI | Cambios en la voz (ronca, húmeda, débil) |
| Q07 | - |  |  | SI | Total Preliminar |
| Q08 | - |  |  | SI | 2. Prueba Directa de Deglución |
| Q09 | - |  |  | SI | SEMISÓLIDO |
| Q10 | - |  |  | SI | Deglución SS |
| Q11 | - |  |  | SI | Tos (involuntaria) SS |
| Q12 | - |  |  | SI | Sialorrea SS |
| Q13 | - |  |  | SI | Cambios en la voz SS |
| Q14 | - |  |  | SI | Total Semisólido |
| Q15 | - |  |  | SI | LÍQUIDO |
| Q16 | - |  |  | SI | Deglución L |
| Q17 | - |  |  | SI | Tos (involuntaria) L |
| Q18 | - |  |  | SI | Sialorrea L |
| Q19 | - |  |  | SI | Cambios en la voz L |
| Q20 | - |  |  | SI | Total Líquido |
| Q21 | - |  |  | SI | SÓLIDO |
| Q22 | - |  |  | SI | Deglución S |
| Q23 | - |  |  | SI | Tos (involuntaria) S |
| Q24 | - |  |  | SI | Sialorrea S |
| Q25 | - |  |  | SI | Cambios en la voz S |
| Q26 | - |  |  | SI | Total Sólido |
| Q27 | - |  |  | SI | Fecha de Evaluación |
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