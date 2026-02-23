# SQLUser.ARC_BillSub

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCSG_ARCBG_ParRef | bigint | PK |  | NO | Des Ref to ARCBG |
| ARCSG_Abbrev | varchar |  |  | SI | Abbreviation |
| ARCSG_ChildSub | numeric |  |  | NO | ARCSG_ChildSub |
| ARCSG_Code | varchar |  |  | NO | Billing Sub Group Code |
| ARCSG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCSG_CodeTranslated | varchar |  |  | SI | - |
| ARCSG_ConsiderOrderSet | varchar |  |  | SI | Consider Order Set |
| ARCSG_CreatedDate | date |  |  | SI | Created Date |
| ARCSG_CreatedTime | time |  |  | SI | Created Time |
| ARCSG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCSG_DateFrom | date |  |  | SI | Date From |
| ARCSG_DateTo | date |  |  | SI | Date To |
| ARCSG_Desc | varchar |  |  | NO | Billing Sub Group Description |
| ARCSG_DescTranslated | varchar |  |  | SI | - |
| ARCSG_DischPriorityBUP_DR | bigint |  | FK | SI | Des Ref DischPriority Billing Upon Packing |
| ARCSG_DisplayZeroItems | varchar |  |  | SI | Display Zero Items |
| ARCSG_EmergBillingLogic | varchar |  |  | SI | Emergency Billing Logic |
| ARCSG_InpatBillingLogic | varchar |  |  | SI | Inpatient Billing Logic |
| ARCSG_LabPatMustPayEpisodeTypes | varchar |  |  | SI | Episode Types for Lab Patient Must Pay  |
| ARCSG_MaterialDiffDate | varchar |  |  | SI | Material Diff Date |
| ARCSG_MaterialSameDate | varchar |  |  | SI | Material Same Date |
| ARCSG_MinAmount | double |  |  | SI | MinAmount |
| ARCSG_OccurenceRule | varchar |  |  | SI | Occurence Rule |
| ARCSG_OutpatBillingLogic | varchar |  |  | SI | Outpatient Billing Logic |
| ARCSG_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| ARCSG_QtyToDay | varchar |  |  | SI | Quantity To Day |
| ARCSG_RevOrder | double |  |  | SI | Review Screen Order |
| ARCSG_RowId | varchar |  |  | NO | - |
| ARCSG_ServiceDiffDate | varchar |  |  | SI | Service Diff Date |
| ARCSG_ServiceSameDate | varchar |  |  | SI | Service Same Date |
| ARCSG_UpdatedDate | date |  |  | SI | Updated Date |
| ARCSG_UpdatedTime | time |  |  | SI | Updated Time |
| ARCSG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ02DR | - |  |  | SI | Child Reference: Registro de Insumos Especiales |
| Q01 | - |  |  | SI | Insumos Especiales |
| Q03 | - |  |  | SI | Vías |
| Q04 | - |  |  | SI | Biopsias |
| Q05 | - |  |  | SI | Tipo Cirugía |
| Q06 | - |  |  | SI | Indicaciones |
| Q07 | - |  |  | SI | Instrumental Especial |
| Q08 | - |  |  | SI | Equipamiento |
| Q09 | - |  |  | SI | Posicionadores |
| Q10 | - |  |  | SI | Días Aprox. Hospitalización |
| Q11 | - |  |  | SI | MQ |
| Q12 | - |  |  | SI | UTI |
| Q13 | - |  |  | SI | UCI |
| Q14 | - |  |  | SI | Camas |
| Q15 | - |  |  | SI | UCO |
| Q16 | - |  |  | SI | Oncología |
| Q17 | - |  |  | SI | Pediatría |
| Q18 | - |  |  | SI | Neonatología |
| Q19 | - |  |  | SI | Aislamiento |
| Q20 | - |  |  | SI | Detalle Aislamiento |
| Q21 | - |  |  | SI | Hemoderivados |
| Q22 | - |  |  | SI | Requerimientos Especiales |
| Q23 | - |  |  | SI | Otros |
| Q24 | - |  |  | SI | Otros Antecedentes |
| Q25 | - |  |  | SI | Detalle Antecedentes |
| Q26 | - |  |  | SI | Tiempo Cirujano (minutos) |
| Q27 | - |  |  | SI | Tiempo Total Ocupación (minutos) |
| Q28 | - |  |  | SI | Antecedentes del Paciente |
| Q29 | - |  |  | SI | Duración Estimada |
| Q30 | - |  |  | SI | Número |
| Q31 | - |  |  | SI | Alergia |
| Q32 | - |  |  | SI | Detalle Alergia |
| Q33 | - |  |  | SI | Contacto |
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