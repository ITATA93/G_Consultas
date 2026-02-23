# SQLUser.MRC_HDR

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HDR_RowId | bigint | PK |  | NO | - |
| HDR_ChartDR | bigint |  | FK | SI | HDR Chart |
| HDR_Code | varchar |  |  | SI | Code |
| HDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HDR_CreatedDate | date |  |  | SI | Created Date |
| HDR_CreatedTime | time |  |  | SI | Created Time |
| HDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HDR_DateFrom | date |  |  | SI | DateFrom |
| HDR_DateTo | date |  |  | SI | DateTo |
| HDR_DefaultInterval | double |  |  | SI | Default Interval |
| HDR_Desc | varchar |  |  | SI | Description |
| HDR_DispFreeTextProc | varchar |  |  | SI | Display Free Text Procedure Field on Period |
| HDR_Owner | varchar |  |  | SI | Owner |
| HDR_Purpose | varchar |  |  | SI | Purpose |
| HDR_UpdatedDate | date |  |  | SI | Updated Date |
| HDR_UpdatedTime | time |  |  | SI | Updated Time |
| HDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nivel de Sedacion |
| Q02 | - |  |  | SI | Estado del Paciente |
| Q03 | - |  |  | SI | Estado de la Piel |
| Q04 | - |  |  | SI | Estado de la Piel |
| Q05 | - |  |  | SI | Localización Lesión |
| Q06 | - |  |  | SI | Tipo de Lesión |
| Q07 | - |  |  | SI | Uso de Oxigeno |
| Q08 | - |  |  | SI | Uso de Oxigeno |
| Q09 | - |  |  | SI | Dispositivo Via Aerea |
| Q10 | - |  |  | SI | Dispositivo Vía Aerea |
| Q11 | - |  |  | SI | FiO2 % |
| Q12 | - |  |  | SI | Frecuencia del Flujo |
| Q13 | - |  |  | SI | Imágenes  placas  y digitales |
| Q14 | - |  |  | SI | Uso otros equipos |
| Q15 | - |  |  | SI | Monitorización Traslado |
| Q16 | - |  |  | SI | Monitorización de traslado |
| Q17 | - |  |  | SI | Transportado en |
| Q18 | - |  |  | SI | Transportado en |
| Q19 | - |  |  | SI | Destino  Postoperatorio |
| Q20 | - |  |  | SI | Frecuencia Cardiaca |
| Q20ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q21 | - |  |  | SI | Exámenes Previos |
| Q22 | - |  |  | SI | Pertenecias y Accesorios |
| Q23 | - |  |  | SI | Instrucciones para retiro resultado de biopsia |
| Q24 | - |  |  | SI | Indicaciones al Alta (verbal o escrita) |
| Q25 | - |  |  | SI | Comentarios |
| Q26 | - |  |  | SI | Comentarios |
| Q27 | - |  |  | SI | Comentarios |
| Q28 | - |  |  | SI | Comentarios |
| Q29 | - |  |  | SI | Médico / Odontólogo |
| Q30 | - |  |  | SI | Enfermera(o) |
| Q31 | - |  |  | SI | TENS / TONS |
| Q32 | - |  |  | SI | Observaciones Generales |
| Q33 | - |  |  | SI | Entrega Pertenencias Paciente/Acompañante |
| Q34 | - |  |  | SI | Responsables |
| Q35 | - |  |  | SI | Presión Arterial Sistólica |
| Q35ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q36 | - |  |  | SI | Presión Arterial Diastólica |
| Q36ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q37 | - |  |  | SI | Presión Arterial Media |
| Q38 | - |  |  | SI | Frecuencia Respiratoria |
| Q38ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q39 | - |  |  | SI | Saturación O2 |
| Q39ObsDR | - |  |  | SI | Saturación O2 DR |
| Q40 | - |  |  | SI | Hemoglucotest |
| Q40ObsDR | - |  |  | SI | Hemoglucotest DR |
| Q41 | - |  |  | SI | Escala del Dolor (EVA) |
| Q41ObsDR | - |  |  | SI | Escala del Dolor (EVA) DR |
| Q42 | - |  |  | SI | FiO2 |
| Q42ObsDR | - |  |  | SI | FiO2 DR |
| Q43 | - |  |  | SI | Signos Vitales |
| Q44 | - |  |  | SI | Sin dispositivo |
| Q45 | - |  |  | SI | Catéter Venoso Central |
| Q46 | - |  |  | SI | Tamaño Catéter Venoso Central |
| Q47 | - |  |  | SI | Línea Arterial |
| Q48 | - |  |  | SI | Tamaño Línea Arterial |
| Q49 | - |  |  | SI | Vía Venosa Periférica |
| Q50 | - |  |  | SI | Tamaño Vía Venosa Periférica |
| Q51 | - |  |  | SI | Sonda Nasogástrica - Sonda Orogástrica |
| Q52 | - |  |  | SI | Tamaño Sonda Nasogástrica - Sonda Orogástrica |
| Q53 | - |  |  | SI | Gastrostomía |
| Q54 | - |  |  | SI | Tamaño Gastrostomía |
| Q55 | - |  |  | SI | Tubo Endotraqueal |
| Q56 | - |  |  | SI | Tamaño Tubo Endotraqueal |
| Q57 | - |  |  | SI | Traqueostomía |
| Q58 | - |  |  | SI | Tamaño Traqueostomía |
| Q59 | - |  |  | SI | Drenaje Ventricular Externo |
| Q60 | - |  |  | SI | Tamaño Drenaje Ventricular Externo |
| Q61 | - |  |  | SI | Catéter Urinario Permanente |
| Q62 | - |  |  | SI | Tamaño Catéter Urinario Permanente |
| Q63 | - |  |  | SI | Otros Dispositivos |
| Q64 | - |  |  | SI | Dispositivos Invasivos |
| Q65 | - |  |  | SI | Tamaño |
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