# questionnaire.QTCEMLEP

> Formulario de muestras: Sospecha Leptopirosis

**Schema:** questionnaire
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de muestras: Sospecha Leptopirosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombres |
| Q02 | varchar |  |  | SI | Apellido Paterno |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | Rut |
| Q05 | varchar |  |  | SI | Ocupación |
| Q06 | varchar |  |  | SI | Edad |
| Q07 | varchar |  |  | SI | Fecha Nacimiento  |
| Q08 | varchar |  |  | SI | Sexo |
| Q09 | varchar |  |  | SI | Domicilio |
| Q10 | varchar |  |  | SI | Comuna |
| Q11 | varchar |  |  | SI | Diagnóstico |
| Q12 | varchar |  |  | SI | Signos y Síntomas Principales |
| Q13 | varchar |  |  | SI | Tipo de Contacto |
| Q14 | date |  |  | SI | Fecha de inicio de Síntomas |
| Q15 | varchar |  |  | SI | Tratamiento Antibiotico  |
| Q16 | date |  |  | SI | Fecha Inicio del Tratamiento  |
| Q17 | varchar |  |  | SI | Tipo de muestra  |
| Q18 | varchar |  |  | SI | N° de muestra |
| Q19 | varchar |  |  | SI | Examen Solicitado  |
| Q20 | bit |  |  | SI | Suero  |
| Q21 | bit |  |  | SI | 1° muestra |
| Q22 | bit |  |  | SI | ELISA |
| Q23 | bit |  |  | SI | Sangre |
| Q24 | bit |  |  | SI | 2° muestra |
| Q25 | bit |  |  | SI | Otra   |
| Q26 | bit |  |  | SI | 3° muestra |
| Q27 | bit |  |  | SI | MAT |
| Q28 | date |  |  | SI | Fecha de Toma |
| Q29 | varchar |  |  | SI | ELISA_REACTIVO USADO |
| Q30 | varchar |  |  | SI | MICROHEMAGLUTINACION_REACTIVO USADO |
| Q31 | varchar |  |  | SI | OTRO_REACTIVOUSADO |
| Q32 | varchar |  |  | SI | ELISA_N° DE LOTE |
| Q33 | varchar |  |  | SI | MICROHEMAGLUTINACION_N° DE LOTE |
| Q34 | varchar |  |  | SI | OTRO_N° DE LOTE |
| Q35 | varchar |  |  | SI | ELISA_RESULTADO |
| Q36 | varchar |  |  | SI | MICROHEMAGLUTINACION_RESULTADO |
| Q37 | varchar |  |  | SI | OTRO_RESULTADO |
| Q38 | varchar |  |  | SI | Dirección  |
| Q39 | varchar |  |  | SI | Nombre del Establecimiento |
| Q40 | varchar |  |  | SI | Comuna |
| Q41 | varchar |  |  | SI | Profesional Responsable  |
| Q42 | varchar |  |  | SI | Servicio de Salud |
| Q43 | varchar |  |  | SI | Ciudad/Localidad |
| Q44 | numeric |  |  | SI | Fono  |
| Q45 | numeric |  |  | SI | FAX |
| Q46 | varchar |  |  | SI | Servicio Clínico |
| Q47 | varchar |  |  | SI | Observaciones |
| Q48 | varchar |  |  | SI | Solicitud de envio de resultados |
| Q49 | numeric |  |  | SI | Número |
| Q50 | varchar |  |  | SI | Registro de Laboratorio  |
| Q51 | varchar |  |  | SI | Fecha de Recepción  |
| Q52 | numeric |  |  | SI | N° de Muestra |
| Q53 | varchar |  |  | SI | Registro CSP |
| Q54 | varchar |  |  | SI | Con animales |
| Q55 | varchar |  |  | SI | Otro |
| Q56 | varchar |  |  | SI | Indicar |
| Q57 | varchar |  |  | SI | Región |
| Q58 | varchar |  |  | SI | Ciudad |
| Q59 | varchar |  |  | SI | Región |
| Q60 | varchar |  |  | SI | Observaciones |
| Q61 | varchar |  |  | SI | RUT |
| Q62 | varchar |  |  | SI | Ciudad/Localidad |
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