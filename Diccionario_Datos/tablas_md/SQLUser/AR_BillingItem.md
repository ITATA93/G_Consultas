# SQLUser.AR_BillingItem

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARBI_RowID | bigint | PK |  | NO | - |
| ARBI_BillItem_DR | bigint |  | FK | NO | Billing Item |
| ARBI_BillRule_DR | varchar |  | FK | SI | Billing Rule |
| ARBI_ConeRule_DR | varchar |  | FK | SI | Coning Rule |
| ARBI_DateOfService | date |  |  | SI | Date of Service |
| ARBI_Initiation_DR | bigint |  | FK | SI | Initiation Code |
| ARBI_LabEpisode_DR | bigint |  | FK | SI | LBEpisode Reference |
| ARBI_LocLabBilling_DR | varchar |  | FK | SI | Location Lab Billing |
| ARBI_MasterLabEpisode_DR | bigint |  | FK | SI | Master Lab Episode
The Patient details are based ... |
| ARBI_OrdItem_DR | varchar |  | FK | SI | OrderItem Reference |
| ARBI_PAAdm_DR | bigint |  | FK | SI | Admission
PAAdm (Admission Episode) |
| ARBI_PAPerson_DR | bigint |  | FK | SI | Patient
PAPerson (Patient) (User.PAPerson)  |
| ARBI_PaymentAgreement_DR | bigint |  | FK | SI | Payment Agreement |
| ARBI_Price | double |  |  | SI | Price |
| ARBI_ScheduleTariffBillingItem_DR | varchar |  | FK | SI | Schedule Tarif Billing Item |
| ARBI_ScheduleTariff_DR | varchar |  | FK | SI | Billing Schedule Tariff |
| ARBI_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container |
| ARBI_Status | varchar |  |  | SI | Billing Item Status |
| ARBI_TestSet_DR | bigint |  | FK | SI | Test Set |
| Q09 | - |  |  | SI | Acompañado Por |
| Q10 | - |  |  | SI | Comentarios del acompañante |
| Q11 | - |  |  | SI | Tipo de Ingreso |
| Q12 | - |  |  | SI | Comentarios del Tipo de Ingreso |
| Q13 | - |  |  | SI | Medio de Llegada |
| Q14 | - |  |  | SI | Comentarios de la Forma de Ingreso |
| Q15 | - |  |  | SI | Nombre Contacto Emergencia |
| Q16 | - |  |  | SI | Parentesco |
| Q166 | - |  |  | SI | Comentario de brazalete de alergias |
| Q17 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q18 | - |  |  | SI | Información Entregada Por |
| Q19 | - |  |  | SI | Comentarios de la información entregada |
| Q20 | - |  |  | SI | Origen del Paciente |
| Q21 | - |  |  | SI | Comentarios del Origen del Paciente |
| Q22 | - |  |  | SI | Primera Atención Salud Mental |
| Q23 | - |  |  | SI | Comentario de la Primera Atención de Salud Mental |
| Q236 | - |  |  | SI | Profesional de Salud |
| Q24 | - |  |  | SI | Paciente Crónico Salud Mental |
| Q25 | - |  |  | SI | Comentario de Paciente Crónico |
| Q26 | - |  |  | SI | Ingresos Previos |
| Q27 | - |  |  | SI | Comentario de Ingresos Previos |
| Q28 | - |  |  | SI | Comienzo y evolución de la enfermedad |
| Q28a | - |  |  | SI | Adherenia/Control Tratamiento (Check) |
| Q29 | - |  |  | SI | Comentarios Adherencia/Control Tratamiento |
| Q30 | - |  |  | SI | Situación laboral/Ocupación |
| Q31 | - |  |  | SI | Núcleo de Convivencia |
| Q32 | - |  |  | SI | Enfermedades Psiquiátricas Familiares |
| Q33 | - |  |  | SI | Comentario de Enfermedades Psiquiátricas Familiare... |
| Q34 | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q35 | - |  |  | SI | Comentario del Brazalete de Identificación |
| Q36 | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q37 | - |  |  | SI | Comentario de Brazalete con Datos Completos y Legi... |
| Q38 | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q39 | - |  |  | SI | Dispositivos Artificiales |
| Q40 | - |  |  | SI | Comentario de Dispositivos Artificiales |
| Q41 | - |  |  | SI | Otro dispositivo |
| Q42 | - |  |  | SI | Dispositivos Clínicos |
| Q43 | - |  |  | SI | Comentario de Dispositivos Clínicos |
| Q44 | - |  |  | SI | Otro Dispositivo |
| Q45 | - |  |  | SI | Exámenes que Trae el Paciente |
| Q46 | - |  |  | SI | Comentario de los Exámenes |
| Q47 | - |  |  | SI | Otro Examen |
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