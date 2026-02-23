# SQLUser.AR_BillAuditGroupCharges

**Schema:** SQLUser
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | AR_PatBillGroup Parent Reference |
| ITM_ANAEST_Duration | double |  |  | SI | ANAEST_Duration |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_Account | varchar |  |  | SI | Account |
| ITM_ActRAPaymAmount | double |  |  | SI | Activity RA Payment amount  |
| ITM_ActivityID | varchar |  |  | SI | Activity ID |
| ITM_AmtPayorPaid | double |  |  | SI | Amt Payor Paid |
| ITM_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| ITM_BillClaimStatus_DR | bigint |  | FK | SI | Des Ref ARCBillClaimStatus |
| ITM_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_DailyQty | double |  |  | SI | Daily Qty |
| ITM_Date | date |  |  | SI | Order Date |
| ITM_Depart_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| ITM_HandiShare | double |  |  | SI | Handicapped Association Share |
| ITM_InsCompanyShare | double |  |  | SI | Insurance Company Share |
| ITM_InsCoverStatus_DR | bigint |  | FK | SI | Des Ref to InsCoverStatus |
| ITM_InsuranceType_DR | bigint |  | FK | SI | Des Ref InsuranceType |
| ITM_ItemPriceItaly_DR | varchar |  | FK | SI | Des Ref ItemPriceItaly |
| ITM_LineTotal | double |  |  | SI | Line Total |
| ITM_LocalGovtShare | double |  |  | SI | Local Govt Share |
| ITM_MaterialTotal | double |  |  | SI | Material Total |
| ITM_MedisaveCode | varchar |  |  | SI | MedisaveCode |
| ITM_NoTimes | double |  |  | SI | No of Times |
| ITM_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| ITM_OrdCategGroup_DR | bigint |  | FK | SI | Des Ref OrdCategGroup |
| ITM_OrdCateg_DR | bigint |  | FK | SI | Des Ref OrdCateg |
| ITM_OrdSubCat_DR | bigint |  | FK | SI | Des Ref OrdSubCat |
| ITM_OrderTime | time |  |  | SI | Order Time |
| ITM_PAADM_DR | bigint |  | FK | SI | Des Ref to PAADM |
| ITM_PatInsFlag | varchar |  |  | SI | Patient Insurance Flag |
| ITM_PatientShare | double |  |  | SI | Patient Share |
| ITM_PrescNo | varchar |  |  | SI | Prescription No |
| ITM_RVI_BiilGrp_DR | varchar |  | FK | SI | Des REf BiilGrp_DR |
| ITM_ReasonActDenial_DR | bigint |  | FK | SI | Des Ref ARCReasonForActivityDenial |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_ServiceCharge | varchar |  |  | SI | Service charge applied to this item |
| ITM_ServiceMaterial | varchar |  |  | SI | Service/Material |
| ITM_ServiceTotal | double |  |  | SI | Service Total |
| ITM_SpecialistSurcharge | double |  |  | SI | Specialist Surcharge |
| ITM_UnSettled | varchar |  |  | SI | UnSettled |
| ITM_UnitPrice | double |  |  | SI | Unit Price |
| Q01 | - |  |  | SI | Motivo de Ingreso |
| Q02 | - |  |  | SI | Acompañado por |
| Q03 | - |  |  | SI | Medio de Llegada |
| Q04 | - |  |  | SI | Otro Medio de Llegada |
| Q05 | - |  |  | SI | Nombre Contacto Emergencia |
| Q06 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q07 | - |  |  | SI | Información Entregada por |
| Q08 | - |  |  | SI | Otro Infor entregada |
| Q09 | - |  |  | SI | Origen del Paciente |
| Q10 | - |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q11 | - |  |  | SI | Aislamiento |
| Q12 | - |  |  | SI | Comentario Aislamiento |
| Q13 | - |  |  | SI | Aislamiento de Contacto ¿Requiere Aseo Especial? (... |
| Q14 | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q15 | - |  |  | SI | Comentario Brazalete Identificación |
| Q16 | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q17 | - |  |  | SI | Comentarios Brazalete con Datos Completos y Legibl... |
| Q170 | - |  |  | SI | Profesional de Salud |
| Q18 | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q180 | - |  |  | SI | Comentario Acompañado |
| Q19 | - |  |  | SI | comentario Brazalete de Alergias |
| Q20 | - |  |  | SI | Dispositivos Clínicos |
| Q21 | - |  |  | SI | Otro Dispositivo Clínico |
| Q22 | - |  |  | SI | Dispositivos Artificiales |
| Q23 | - |  |  | SI | Otro dispositivo artificial |
| Q24 | - |  |  | SI | Exámenes que Trae el Paciente |
| Q25 | - |  |  | SI | Otro Examen |
| Q26 | - |  |  | SI | Anamnesis Próxima |
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