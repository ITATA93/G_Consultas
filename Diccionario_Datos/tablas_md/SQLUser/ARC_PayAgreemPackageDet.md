# SQLUser.ARC_PayAgreemPackageDet

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | varchar | PK |  | NO | ARC_PayAgreemPackage Parent Reference |
| DET_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DET_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_LimitQty | double |  |  | SI | LimitQty |
| DET_OrdCateg_DR | bigint |  | FK | SI | Des Ref OrdCateg |
| DET_PriceOverLimit | double |  |  | SI | PriceOverLimit |
| DET_PriceUnderLimit | double |  |  | SI | PriceUnderLimit |
| DET_RowId | varchar |  |  | NO | - |
| DET_SubCateg_DR | bigint |  | FK | SI | Des Ref SubCateg |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Adulto |
| Q03 | - |  |  | SI | Relación con el Usuario |
| Q04 | - |  |  | SI | Teléfono de Contacto |
| Q05 | - |  |  | SI | Correo Electrónico |
| Q06 | - |  |  | SI | Agudeza Visual Ojo con TO |
| Q07 | - |  |  | SI | RSH |
| Q08 | - |  |  | SI | Ocupación |
| Q09 | - |  |  | SI | Redes Familiares y Sociales |
| Q10 | - |  |  | SI | Credencial Discapacidad |
| Q11 | - |  |  | SI | Acreditación INDH |
| Q12 | - |  |  | SI | Integrante del Hogar |
| Q13 | - |  |  | SI | Resultado Escala Riesgo Social |
| Q14 | - |  |  | SI | Nivel de Estudios |
| Q15 | - |  |  | SI | Información del estudio |
| Q16 | - |  |  | SI | Observaciones |
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