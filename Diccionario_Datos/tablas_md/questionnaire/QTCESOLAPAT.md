# questionnaire.QTCESOLAPAT

> Solicitud de Examen Anatomía Patológica

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Examen Anatomía Patológica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de Examen |
| Q02 | varchar |  |  | SI | Servicio o Unidad de Procedencia |
| Q03 | varchar |  |  | SI | Nombre del Paciente |
| Q03b | varchar |  |  | SI | Apellido Paterno |
| Q03c | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | RUN |
| Q05 | varchar |  |  | SI | Fecha de Nacimiento |
| Q06 | varchar |  |  | SI | Sexo |
| Q07 | varchar |  |  | SI | Edad |
| Q08 | varchar |  |  | SI | Previsión de Salud |
| Q08p | varchar |  |  | SI | Plan |
| Q09 | varchar |  |  | SI | Dirección |
| Q09n | varchar |  |  | SI | Dirección Paciente Número |
| Q10 | varchar |  |  | SI | Nombre Completo Médico Quien Solicita |
| Q11 | date |  |  | SI | Fecha Toma de Muestra |
| Q12 | time |  |  | SI | Hora Toma de Muestra |
| Q13 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q14 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO  01         |
| Q15 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q16 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 02 |
| Q17 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q18 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 03 |
| Q19 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q20 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 04 |
| Q21 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q22 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 05 |
| Q23 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q24 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 06 |
| Q25 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q26 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 07 |
| Q27 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q28 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 08 |
| Q29 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q30 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 09 |
| Q31 | varchar |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q32 | varchar |  |  | SI | DIAGNÓSTICO CLÍNICO 10 |
| Q33 | varchar |  |  | SI | Antecedentes Clínicos y Tratamientos Previos |
| Q34 | varchar |  |  | SI | Nombre y Firma Médico |
| Q35 | varchar |  |  | SI | Nombre Responsable de Acopio |
| Q36 | varchar |  |  | SI | Examen Macroscópico |
| Q36b | varchar |  |  | SI | Detalle Diagnóstico Microscópico |
| Q37 | varchar |  |  | SI | Órgano |
| Q38 | varchar |  |  | SI | Diagnóstico Microscópico |
| Q39 | varchar |  |  | SI | Anatomo Patólogo |
| Q40 | varchar |  |  | SI | Nº Examen |
| Q41 | date |  |  | SI | Fecha de Diagnóstico |
| Q42 | date |  |  | SI | Fecha de Recepción |
| Q48 | bit |  |  | SI | Informe de Sospecha de Malignidad |
| Q49 | varchar |  |  | SI | Servicio o Unidad de Procedencia |
| Q50 | varchar |  |  | SI | Servicio o Unidad de Destino |
| Q52 | varchar |  |  | SI | N° de Pabellón |
| Q53 | varchar |  |  | SI | Antecedentes PAP anterior |
| Q55 | varchar |  |  | SI | Motivo PAP |
| Q56 | varchar |  |  | SI | Test VPH |
| Q57 | varchar |  |  | SI | Actividad en que se toma la muestra |
| Q58 | varchar |  |  | SI | Tipo de muestra PAP |
| Q59 | varchar |  |  | SI | Estado del cuello |
| Q60 | varchar |  |  | SI | Tratamiento efectuado |
| Q61 | date |  |  | SI | Fecha del Tratamiento |
| Q62 | varchar |  |  | SI | Vacuna VPH |
| Q63 | date |  |  | SI | FUR / Menopausia |
| Q64 | varchar |  |  | SI | Gestación actual |
| Q65 | varchar |  |  | SI | Método anticonceptivo |
| Q66 | varchar |  |  | SI | Amenorrea |
| Q67 | varchar |  |  | SI | Tipo amenorrea |
| Q68 | varchar |  |  | SI | Tipo Amenorrea (Otro) |
| Q69 | varchar |  |  | SI | Menopausia |
| Q70 | varchar |  |  | SI | Terapia hormonal de la menopausia (THM) |
| Q71 | varchar |  |  | SI | Edad Gestacional |
| Q72 | varchar |  |  | SI | N° de Registro |
| Q73 | date |  |  | SI | Fecha de Cirugía |
| Q74 | time |  |  | SI | Hora de Cirugía |
| Q75 | varchar |  |  | SI | Sala / Cama |
| Q76 | varchar |  |  | SI | Cama |
| Q77 | numeric |  |  | SI | Cantidad de Contenedores |
| Q78 | varchar |  |  | SI | Número de Orden |
| Q79 | varchar |  |  | SI | N° de Cirugía |
| Q80 | varchar |  |  | SI | Cirugía /&nbsp;Procedimiento Principal |
| Q81 | bit |  |  | SI | Todas las muestras del mismo Órgano/Tejido y Diagn... |
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