# SQLUser.ARC_BillGrp

**Schema:** SQLUser
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBG_RowId | bigint | PK |  | NO | - |
| ARCBG_Abbrev | varchar |  |  | SI | Abbreviation |
| ARCBG_Code | varchar |  |  | NO | Billing Group Code |
| ARCBG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCBG_CodeTranslated | varchar |  |  | SI | - |
| ARCBG_ConsiderOrderSet | varchar |  |  | SI | Consider Order Set |
| ARCBG_CreatedDate | date |  |  | SI | Created Date |
| ARCBG_CreatedTime | time |  |  | SI | Created Time |
| ARCBG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBG_DateFrom | date |  |  | SI | Date From |
| ARCBG_DateTo | date |  |  | SI | Date To |
| ARCBG_Desc | varchar |  |  | NO | Billing Group Description |
| ARCBG_DescTranslated | varchar |  |  | SI | - |
| ARCBG_DischPriorityBUP_DR | bigint |  | FK | SI | Des Ref DischPriority Billing Upon Packing |
| ARCBG_DisplayZeroItems | varchar |  |  | SI | Display Zero Items |
| ARCBG_EmergBillingLogic | varchar |  |  | SI | Emergency Billing Logic |
| ARCBG_HCPValue | varchar |  |  | SI | HCP Value |
| ARCBG_InpatBillingLogic | varchar |  |  | SI | Inpatient Billing Logic |
| ARCBG_LabPatMustPayEpisodeTypes | varchar |  |  | SI | Episode Types for Lab Patient Must Pay  |
| ARCBG_MaterialDiffDate | varchar |  |  | SI | Material Diff Date |
| ARCBG_MaterialSameDate | varchar |  |  | SI | Material Same Date |
| ARCBG_MaxOrderNoInGrpWarn | double |  |  | SI | Max Order No In Group Warning |
| ARCBG_OccurenceRule | varchar |  |  | SI | Occurence Rule |
| ARCBG_OutpatBillingLogic | varchar |  |  | SI | Outpatient Billing Logic |
| ARCBG_Owner | varchar |  |  | SI | Owner |
| ARCBG_PatClassif | varchar |  |  | SI | Patient Classification |
| ARCBG_QtyToDay | varchar |  |  | SI | Quantity To Day |
| ARCBG_ServiceDiffDate | varchar |  |  | SI | Service Diff Date |
| ARCBG_ServiceSameDate | varchar |  |  | SI | Service Same Date |
| ARCBG_SubRegion_DR | bigint |  | FK | SI | Sub Region |
| ARCBG_TimeDependent | varchar |  |  | SI | Time Dependent Bill Group |
| ARCBG_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBG_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antecedentes Del Paciente |
| Q02 | - |  |  | SI | Aseo Personal Observación |
| Q03 | - |  |  | SI | Alimentación Observación |
| Q04 | - |  |  | SI | Examen Físico General |
| Q05 | - |  |  | SI | Lesiones por Presión |
| Q06 | - |  |  | SI | Ubicación(es) |
| Q07 | - |  |  | SI | Dimension(es) |
| Q08 | - |  |  | SI | Aspecto |
| Q09 | - |  |  | SI | Evolución |
| Q10 | - |  |  | SI | Acciones a Realizar |
| Q11 | - |  |  | SI | Movilidad |
| Q12 | - |  |  | SI | Realiza Ejercicios Pasivos |
| Q13 | - |  |  | SI | Se Levanta al Paciente |
| Q14 | - |  |  | SI | Usa Silla de Ruedas |
| Q15 | - |  |  | SI | Se realizan cambios de posición |
| Q16 | - |  |  | SI | Observaciones |
| Q17 | - |  |  | SI | Antecedentes del Cuidador |
| Q18 | - |  |  | SI | Administración de Medicamentos por Parte del Cuida... |
| Q19 | - |  |  | SI | Se realiza Capacitación a Cuidador |
| Q20 | - |  |  | SI | Contenido de la Capacitación |
| Q21 | - |  |  | SI | Recepción de Pago de Estipendio |
| Q22 | - |  |  | SI | Fecha Último Retiro |
| Q23 | - |  |  | SI | Mes Cancelado Correspondiente |
| Q24 | - |  |  | SI | Comentarios |
| Q25 | - |  |  | SI | Cuidados de la Piel Observación |
| Q26 | - |  |  | SI | Uso de ayudas técnicas u ortesis |
| Q27 | - |  |  | SI | Resultado Dependencia Indice Barthel |
| Q27ObsDR | - |  |  | SI | Resultado Dependencia Indice Barthel DR |
| Q28 | - |  |  | SI | Oncológico |
| Q29 | - |  |  | SI | Aseo Personal |
| Q30 | - |  |  | SI | Estado de Uñas |
| Q31 | - |  |  | SI | Estado de Uñas Observación |
| Q32 | - |  |  | SI | Alimentación |
| Q33 | - |  |  | SI | Incontinencia |
| Q34 | - |  |  | SI | Incontinencia Observación |
| Q35 | - |  |  | SI | Formas de Apoyo a Incontinencia |
| Q36 | - |  |  | SI | Tendencia a Fecalomas |
| Q37 | - |  |  | SI | Cuidados de la Piel |
| Q38 | - |  |  | SI | Factores de Riesgo mas Importantes |
| Q39 | - |  |  | SI | Formas de Apoyo a Incontinencia Obs |
| Q40 | - |  |  | SI | Tendencia a Fecalomas Obs. |
| Q41 | - |  |  | SI | En espera de apoyo monetario |
| Q43 | - |  |  | SI | Se realiza evaluación de sobrecarga anual |
| Q44 | - |  |  | SI | EMPAM Vigente |
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