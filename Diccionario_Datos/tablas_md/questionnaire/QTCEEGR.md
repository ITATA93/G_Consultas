# questionnaire.QTCEEGR

> Egreso de Recuperación

**Schema:** questionnaire
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Egreso de Recuperación

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nivel de Sedacion |
| Q02 | varchar |  |  | SI | Estado del Paciente |
| Q03 | varchar |  |  | SI | Estado de la Piel |
| Q04 | varchar |  |  | SI | Estado de la Piel |
| Q05 | varchar |  |  | SI | Localización Lesión |
| Q06 | varchar |  |  | SI | Tipo de Lesión |
| Q07 | varchar |  |  | SI | Uso de Oxigeno |
| Q08 | varchar |  |  | SI | Uso de Oxigeno |
| Q09 | varchar |  |  | SI | Dispositivo Via Aerea |
| Q10 | varchar |  |  | SI | Dispositivo Vía Aerea |
| Q11 | numeric |  |  | SI | FiO2 % |
| Q12 | varchar |  |  | SI | Frecuencia del Flujo |
| Q13 | varchar |  |  | SI | Imágenes  placas  y digitales |
| Q14 | varchar |  |  | SI | Uso otros equipos |
| Q15 | varchar |  |  | SI | Monitorización Traslado |
| Q16 | varchar |  |  | SI | Monitorización de traslado |
| Q17 | varchar |  |  | SI | Transportado en |
| Q18 | varchar |  |  | SI | Transportado en |
| Q19 | varchar |  |  | SI | Destino  Postoperatorio |
| Q20 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q20ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q21 | varchar |  |  | SI | Exámenes Previos |
| Q22 | varchar |  |  | SI | Pertenecias y Accesorios |
| Q23 | varchar |  |  | SI | Instrucciones para retiro resultado de biopsia |
| Q24 | varchar |  |  | SI | Indicaciones al Alta (verbal o escrita) |
| Q25 | varchar |  |  | SI | Comentarios |
| Q26 | varchar |  |  | SI | Comentarios |
| Q27 | varchar |  |  | SI | Comentarios |
| Q28 | varchar |  |  | SI | Comentarios |
| Q29 | varchar |  |  | SI | Médico / Odontólogo |
| Q30 | varchar |  |  | SI | Enfermera(o) |
| Q31 | varchar |  |  | SI | TENS / TONS |
| Q32 | varchar |  |  | SI | Observaciones Generales |
| Q33 | varchar |  |  | SI | Entrega Pertenencias Paciente/Acompañante |
| Q34 | varchar |  |  | SI | Responsables |
| Q35 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q35ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q36 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q36ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q37 | varchar |  |  | SI | Presión Arterial Media |
| Q38 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q38ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q39 | varchar |  |  | SI | Saturación O2 |
| Q39ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q40 | varchar |  |  | SI | Hemoglucotest |
| Q40ObsDR | varchar |  | FK | SI | Hemoglucotest DR |
| Q41 | varchar |  |  | SI | Escala del Dolor (EVA) |
| Q41ObsDR | varchar |  | FK | SI | Escala del Dolor (EVA) DR |
| Q42 | varchar |  |  | SI | FiO2 |
| Q42ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q43 | varchar |  |  | SI | Signos Vitales |
| Q44 | varchar |  |  | SI | Sin dispositivo |
| Q45 | varchar |  |  | SI | Catéter Venoso Central |
| Q46 | varchar |  |  | SI | Tamaño Catéter Venoso Central |
| Q47 | varchar |  |  | SI | Línea Arterial |
| Q48 | varchar |  |  | SI | Tamaño Línea Arterial |
| Q49 | varchar |  |  | SI | Vía Venosa Periférica |
| Q50 | varchar |  |  | SI | Tamaño Vía Venosa Periférica |
| Q51 | varchar |  |  | SI | Sonda Nasogástrica - Sonda Orogástrica |
| Q52 | varchar |  |  | SI | Tamaño Sonda Nasogástrica - Sonda Orogástrica |
| Q53 | varchar |  |  | SI | Gastrostomía |
| Q54 | varchar |  |  | SI | Tamaño Gastrostomía |
| Q55 | varchar |  |  | SI | Tubo Endotraqueal |
| Q56 | varchar |  |  | SI | Tamaño Tubo Endotraqueal |
| Q57 | varchar |  |  | SI | Traqueostomía |
| Q58 | varchar |  |  | SI | Tamaño Traqueostomía |
| Q59 | varchar |  |  | SI | Drenaje Ventricular Externo |
| Q60 | varchar |  |  | SI | Tamaño Drenaje Ventricular Externo |
| Q61 | varchar |  |  | SI | Catéter Urinario Permanente |
| Q62 | varchar |  |  | SI | Tamaño Catéter Urinario Permanente |
| Q63 | varchar |  |  | SI | Otros Dispositivos |
| Q64 | varchar |  |  | SI | Dispositivos Invasivos |
| Q65 | varchar |  |  | SI | Tamaño |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*