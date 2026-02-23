# SQLUser.APC_VendCat

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Pagar (AP)**. Gestión de proveedores y compras.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APCVC_RowId | bigint | PK |  | NO | - |
| APCVC_CoCode_DR | bigint |  | FK | SI | Des Ref to CTCO |
| APCVC_Code | varchar |  |  | NO | APCVC Code |
| APCVC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APCVC_CreatedDate | date |  |  | SI | Created Date |
| APCVC_CreatedTime | time |  |  | SI | Created Time |
| APCVC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APCVC_Desc | varchar |  |  | NO | APCVC Description |
| APCVC_Owner | varchar |  |  | SI | Owner |
| APCVC_RcFlag | varchar |  |  | SI | Archived Flag |
| APCVC_UpdatedDate | date |  |  | SI | Updated Date |
| APCVC_UpdatedTime | time |  |  | SI | Updated Time |
| APCVC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ51DR | - |  |  | SI | Child Reference: Detalle de Contenedores |
| Q01 | - |  |  | SI | Tipo de Examen |
| Q02 | - |  |  | SI | Servicio o Unidad de Procedencia |
| Q03 | - |  |  | SI | Nombre del Paciente |
| Q03b | - |  |  | SI | Apellido Paterno |
| Q03c | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | RUN |
| Q05 | - |  |  | SI | Fecha de Nacimiento |
| Q06 | - |  |  | SI | Sexo |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Previsión de Salud |
| Q08p | - |  |  | SI | Plan |
| Q09 | - |  |  | SI | Dirección |
| Q09n | - |  |  | SI | Dirección Paciente Número |
| Q10 | - |  |  | SI | Nombre Completo Médico Quien Solicita |
| Q11 | - |  |  | SI | Fecha Toma de Muestra |
| Q12 | - |  |  | SI | Hora Toma de Muestra |
| Q13 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q14 | - |  |  | SI | DIAGNÓSTICO CLÍNICO  01 |
| Q15 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q16 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 02 |
| Q17 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q18 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 03 |
| Q19 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q20 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 04 |
| Q21 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q22 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 05 |
| Q23 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q24 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 06 |
| Q25 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q26 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 07 |
| Q27 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q28 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 08 |
| Q29 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q30 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 09 |
| Q31 | - |  |  | SI | Órgano, Tejido, Localización de Origen y Lateralid... |
| Q32 | - |  |  | SI | DIAGNÓSTICO CLÍNICO 10 |
| Q33 | - |  |  | SI | Antecedentes Clínicos y Tratamientos Previos |
| Q34 | - |  |  | SI | Nombre y Firma Médico |
| Q35 | - |  |  | SI | Nombre Responsable de Acopio |
| Q36 | - |  |  | SI | Examen Macroscópico |
| Q36b | - |  |  | SI | Detalle Diagnóstico Microscópico |
| Q37 | - |  |  | SI | Órgano |
| Q38 | - |  |  | SI | Diagnóstico Microscópico |
| Q39 | - |  |  | SI | Anatomo Patólogo |
| Q40 | - |  |  | SI | Nº Examen |
| Q41 | - |  |  | SI | Fecha de Diagnóstico |
| Q42 | - |  |  | SI | Fecha de Recepción |
| Q48 | - |  |  | SI | Informe de Sospecha de Malignidad |
| Q49 | - |  |  | SI | Servicio o Unidad de Procedencia |
| Q50 | - |  |  | SI | Servicio o Unidad de Destino |
| Q52 | - |  |  | SI | N° de Pabellón |
| Q53 | - |  |  | SI | Antecedentes PAP anterior |
| Q55 | - |  |  | SI | Motivo PAP |
| Q56 | - |  |  | SI | Test VPH |
| Q57 | - |  |  | SI | Actividad en que se toma la muestra |
| Q58 | - |  |  | SI | Tipo de muestra PAP |
| Q59 | - |  |  | SI | Estado del cuello |
| Q60 | - |  |  | SI | Tratamiento efectuado |
| Q61 | - |  |  | SI | Fecha del Tratamiento |
| Q62 | - |  |  | SI | Vacuna VPH |
| Q63 | - |  |  | SI | FUR / Menopausia |
| Q64 | - |  |  | SI | Gestación actual |
| Q65 | - |  |  | SI | Método anticonceptivo |
| Q66 | - |  |  | SI | Amenorrea |
| Q67 | - |  |  | SI | Tipo amenorrea |
| Q68 | - |  |  | SI | Tipo Amenorrea (Otro) |
| Q69 | - |  |  | SI | Menopausia |
| Q70 | - |  |  | SI | Terapia hormonal de la menopausia (THM) |
| Q71 | - |  |  | SI | Edad Gestacional |
| Q72 | - |  |  | SI | N° de Registro |
| Q73 | - |  |  | SI | Fecha de Cirugía |
| Q74 | - |  |  | SI | Hora de Cirugía |
| Q75 | - |  |  | SI | Sala / Cama |
| Q76 | - |  |  | SI | Cama |
| Q77 | - |  |  | SI | Cantidad de Contenedores |
| Q78 | - |  |  | SI | Número de Orden |
| Q79 | - |  |  | SI | N° de Cirugía |
| Q80 | - |  |  | SI | Cirugía /&nbsp |
| Q81 | - |  |  | SI | Todas las muestras del mismo Órgano/Tejido y Diagn... |
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