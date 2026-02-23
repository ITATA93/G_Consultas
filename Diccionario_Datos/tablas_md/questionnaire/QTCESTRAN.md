# questionnaire.QTCESTRAN

> Solicitud de Transfusión

**Schema:** questionnaire
**Columnas:** 182
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Transfusión

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Motivo de la Indicación |
| Q02 | varchar |  |  | SI | Carácter de la Transfusión |
| Q03 | date |  |  | SI | Fecha programada |
| Q04 | varchar |  |  | SI | Transfusiones Previas |
| Q05 | varchar |  |  | SI | Reacciones Adversas |
| Q06 | varchar |  |  | SI | Cuando? |
| Q07 | varchar |  |  | SI | Cuáles? |
| Q08 | numeric |  |  | SI | Globulos Rojos |
| Q09 | numeric |  |  | SI | Globulos Rojos Pobres en Leucocitos |
| Q10 | numeric |  |  | SI | Plasma Fresco Congelado |
| Q100 | varchar |  |  | SI | Tipo unidad Concentrado plaquetario de aféresis |
| Q101 | varchar |  |  | SI | Tipo unidad Plasma fresco Congelado |
| Q102 | varchar |  |  | SI | Tipo unidad Crioprecipitado |
| Q103 | varchar |  |  | SI | Reserva de Pabellón |
| Q104 | numeric |  |  | SI | Progenitores |
| Q105 | varchar |  |  | SI | Tipo unidad Progenitores |
| Q106 | bit |  |  | SI | Filtrados (Progenitores) |
| Q107 | bit |  |  | SI | Irradiados (Progenitores) |
| Q108 | varchar |  |  | SI | Comentario Progenitores |
| Q109 | varchar |  |  | SI | Otros ¿Cuál? |
| Q11 | numeric |  |  | SI | Plaquetas |
| Q110 | numeric |  |  | SI | Otros Cantidad |
| Q111 | varchar |  |  | SI | Tipo unidad Otros |
| Q112 | bit |  |  | SI | Filtrados (Otros) |
| Q113 | bit |  |  | SI | Irradiados (Otros) |
| Q114 | varchar |  |  | SI | Comentario Otros |
| Q115 | numeric |  |  | SI | Test Rápido de Hemoglobina |
| Q116 | bit |  |  | SI | No Aplica / Sin Resultado (Test Rápido de Hemoglob... |
| Q117 | varchar |  |  | SI | Criterio indicación médica para Glóbulos Rojos |
| Q118 | varchar |  |  | SI | Criterio indicación médica Plaquetas |
| Q119 | varchar |  |  | SI | Trombocitopenia por falla medular |
| Q12 | numeric |  |  | SI | Crioprecipitado |
| Q120 | varchar |  |  | SI | Trombocitopenia por consumo |
| Q121 | varchar |  |  | SI | Trombocitopenia por destrucción aumentada |
| Q122 | varchar |  |  | SI | Disfunción plaquetaria congénita o adquirida |
| Q123 | varchar |  |  | SI | Criterio indicación médica Plasma Fresco Congelado |
| Q124 | varchar |  |  | SI | Criterio indicación médica Crioprecipitados |
| Q125 | varchar |  |  | SI | Otra comorbilidad concentrado de glóbulos rojos le... |
| Q126 | varchar |  |  | SI | Otra comorbilidad concentrado unitario de plaqueta... |
| Q127 | varchar |  |  | SI | Otra comorbilidad concentrado plaquetario de afére... |
| Q128 | varchar |  |  | SI | Otra comorbilidad plasma fresco congelado |
| Q129 | varchar |  |  | SI | Otra comorbilidad crioprecipitado |
| Q13 | varchar |  |  | SI | Carácter de la Transfusión |
| Q14 | varchar |  |  | SI | Transfusiones Previas |
| Q15 | varchar |  |  | SI | Reacciones Adversas |
| Q16 | varchar |  |  | SI | Edad |
| Q17 | varchar |  |  | SI | Peso |
| Q17ObsDR | varchar |  | FK | SI | Peso DR |
| Q18 | varchar |  |  | SI | Talla |
| Q18ObsDR | varchar |  | FK | SI | Talla DR |
| Q19 | varchar |  |  | SI | Grupo ABO y Rh |
| Q20 | date |  |  | SI | Para el día |
| Q21 | time |  |  | SI | Hora |
| Q22 | varchar |  |  | SI | Lugar |
| Q23 | date |  |  | SI | Para el día |
| Q24 | time |  |  | SI | Hora |
| Q25 | date |  |  | SI | Fecha Transfusión Previa |
| Q26 | date |  |  | SI | Fecha Reacciones Adversas |
| Q27 | varchar |  |  | SI | Tipo de Reacción |
| Q28 | numeric |  |  | SI | Concentrado de Glóbulos Rojos Leucorreducidos |
| Q29 | bit |  |  | SI | Irradiados (Concentrado de Glóbulos Rojos Leucorre... |
| Q30 | bit |  |  | SI | Filtrados (Concentrado de Glóbulos Rojos Leucorred... |
| Q31 | numeric |  |  | SI | Concentrado Unitario de Plaquetas |
| Q32 | bit |  |  | SI | Irradiados (Concentrado Unitario de Plaquetas) |
| Q33 | bit |  |  | SI | Filtrados (Concentrado Unitario de Plaquetas) |
| Q34 | numeric |  |  | SI | Concentrado Plaquetario de Aféresis |
| Q35 | bit |  |  | SI | Irradiados (Concentrado Plaquetario de Aféresis) |
| Q36 | bit |  |  | SI | Filtrados (Concentrado Plaquetario de Aféresis) |
| Q37 | numeric |  |  | SI | Plasma Fresco Congelado |
| Q38 | bit |  |  | SI | Irradiados (Plasma Fresco Congelado) |
| Q39 | bit |  |  | SI | Filtrados (Plasma Fresco Congelado) |
| Q40 | numeric |  |  | SI | Crioprecipitado |
| Q41 | bit |  |  | SI | Irradiados (Crioprecipitado) |
| Q42 | bit |  |  | SI | Filtrados (Crioprecipitado) |
| Q43 | date |  |  | SI | Fecha |
| Q44 | varchar |  |  | SI | Hematocrito |
| Q44ObsDR | varchar |  | FK | SI | Hematocrito DR |
| Q45 | varchar |  |  | SI | Hemoglobina |
| Q45ObsDR | varchar |  | FK | SI | Hemoglobina DR |
| Q46 | varchar |  |  | SI | Recuento Plaquetario |
| Q46ObsDR | varchar |  | FK | SI | Recuento Plaquetario DR |
| Q47 | varchar |  |  | SI | TP |
| Q47ObsDR | varchar |  | FK | SI | TP DR |
| Q48 | varchar |  |  | SI | TTPA |
| Q48ObsDR | varchar |  | FK | SI | TTPA DR |
| Q49 | varchar |  |  | SI | INR |
| Q49ObsDR | varchar |  | FK | SI | INR DR |
| Q50 | varchar |  |  | SI | Fibrinógeno |
| Q50ObsDR | varchar |  | FK | SI | Fibrinógeno DR |
| Q51 | varchar |  |  | SI | Otros |
| Q52 | varchar |  |  | SI | Edad |
| Q53 | varchar |  |  | SI | Grupo ABO y Rh |
| Q53ObsDR | varchar |  | FK | SI | Grupo ABO y Rh DR |
| Q54 | varchar |  |  | SI | TTPA |
| Q54ObsDR | varchar |  | FK | SI | TTPA DR |
| Q55 | varchar |  |  | SI | INR |
| Q55ObsDR | varchar |  | FK | SI | INR DR |
| Q56 | date |  |  | SI | Fecha Solicitud |
| Q57 | time |  |  | SI | Hora Solicitud |
| Q58 | varchar |  |  | SI | Nombre Paciente |
| Q59 | varchar |  |  | SI | Apellido Paterno |
| Q60 | varchar |  |  | SI | Apellido Materno |
| Q61 | varchar |  |  | SI | RUN |
| Q62 | varchar |  |  | SI | Unidad/ Servicio / Local (ambulatorio) |
| Q63 | varchar |  |  | SI | Sala |
| Q64 | varchar |  |  | SI | Diagnóstico |
| Q65 | varchar |  |  | SI | N° Folio |
| Q66 | varchar |  |  | SI | Medico Solicitante |
| Q67 | numeric |  |  | SI | Plasma Inmune (HANTA)  |
| Q68 | bit |  |  | SI | Filtrado |
| Q69 | bit |  |  | SI | Irradiado |
| Q70 | bit |  |  | SI | No Aplica / Sin Resultado (Hematocrito) |
| Q71 | bit |  |  | SI | No Aplica / Sin Resultado (Hemoglobina) |
| Q72 | bit |  |  | SI | No Aplica / Sin Resultado (Recuento Plaquetario) |
| Q73 | bit |  |  | SI | No Aplica / Sin Resultado (TP) |
| Q74 | bit |  |  | SI | No Aplica / Sin Resultado (TTPA) |
| Q75 | bit |  |  | SI | No Aplica / Sin Resultado (INR) |
| Q76 | bit |  |  | SI | No Aplica / Sin Resultado (Fibrinógeno) |
| Q77 | varchar |  |  | SI | Fecha de Nacimiento |
| Q78 | varchar |  |  | SI | Requerimiento de O2 |
| Q79 | varchar |  |  | SI | VMNI |
| Q80 | varchar |  |  | SI | ECMO |
| Q81 | varchar |  |  | SI | CEC |
| Q82 | varchar |  |  | SI | Unidad / Servicio |
| Q83 | varchar |  |  | SI | Sala / Cama |
| Q84 | varchar |  |  | SI | Cama |
| Q85 | varchar |  |  | SI | VMI |
| Q86 | varchar |  |  | SI | Médico Solicitante |
| Q87 | varchar |  |  | SI | Comentario concentrado de glóbulos rojos leucorred... |
| Q88 | varchar |  |  | SI | Comentario concentrado unitario de plaquetas |
| Q89 | varchar |  |  | SI | Comentario concentrado plaquetario de aféresis |
| Q90 | varchar |  |  | SI | Comentario plasma fresco congelado |
| Q91 | varchar |  |  | SI | Comentario crioprecipitado |
| Q92 | varchar |  |  | SI | Motivo de indicación concentrado de glóbulos rojos... |
| Q93 | varchar |  |  | SI | Motivo de indicación concentrado unitario de plaqu... |
| Q94 | varchar |  |  | SI | Motivo de indicación concentrado plaquetario de af... |
| Q95 | varchar |  |  | SI | Motivo de indicación plasma fresco congelado |
| Q96 | varchar |  |  | SI | Motivo de indicación crioprecipitado |
| Q97 | varchar |  |  | SI | Otra comorbilidad |
| Q98 | varchar |  |  | SI | Tipo unidad Concentrado de glóbulos rojos leucorre... |
| Q99 | varchar |  |  | SI | Tipo unidad Concentrado unitario de plaquetas |
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