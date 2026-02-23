# SQLUser.MRC_CancerStageTumourSize

**Schema:** SQLUser
**Columnas:** 195
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SIZE_ParRef | bigint | PK |  | NO | Parent Reference |
| Q01 | - |  |  | SI | Motivo de la Indicación |
| Q02 | - |  |  | SI | Carácter de la Transfusión |
| Q03 | - |  |  | SI | Fecha programada |
| Q04 | - |  |  | SI | Transfusiones Previas |
| Q05 | - |  |  | SI | Reacciones Adversas |
| Q06 | - |  |  | SI | Cuando? |
| Q07 | - |  |  | SI | Cuáles? |
| Q08 | - |  |  | SI | Globulos Rojos |
| Q09 | - |  |  | SI | Globulos Rojos Pobres en Leucocitos |
| Q10 | - |  |  | SI | Plasma Fresco Congelado |
| Q100 | - |  |  | SI | Tipo unidad Concentrado plaquetario de aféresis |
| Q101 | - |  |  | SI | Tipo unidad Plasma fresco Congelado |
| Q102 | - |  |  | SI | Tipo unidad Crioprecipitado |
| Q103 | - |  |  | SI | Reserva de Pabellón |
| Q104 | - |  |  | SI | Progenitores |
| Q105 | - |  |  | SI | Tipo unidad Progenitores |
| Q106 | - |  |  | SI | Filtrados (Progenitores) |
| Q107 | - |  |  | SI | Irradiados (Progenitores) |
| Q108 | - |  |  | SI | Comentario Progenitores |
| Q109 | - |  |  | SI | Otros ¿Cuál? |
| Q11 | - |  |  | SI | Plaquetas |
| Q110 | - |  |  | SI | Otros Cantidad |
| Q111 | - |  |  | SI | Tipo unidad Otros |
| Q112 | - |  |  | SI | Filtrados (Otros) |
| Q113 | - |  |  | SI | Irradiados (Otros) |
| Q114 | - |  |  | SI | Comentario Otros |
| Q115 | - |  |  | SI | Test Rápido de Hemoglobina |
| Q116 | - |  |  | SI | No Aplica / Sin Resultado (Test Rápido de Hemoglob... |
| Q117 | - |  |  | SI | Criterio indicación médica para Glóbulos Rojos |
| Q118 | - |  |  | SI | Criterio indicación médica Plaquetas |
| Q119 | - |  |  | SI | Trombocitopenia por falla medular |
| Q12 | - |  |  | SI | Crioprecipitado |
| Q120 | - |  |  | SI | Trombocitopenia por consumo |
| Q121 | - |  |  | SI | Trombocitopenia por destrucción aumentada |
| Q122 | - |  |  | SI | Disfunción plaquetaria congénita o adquirida |
| Q123 | - |  |  | SI | Criterio indicación médica Plasma Fresco Congelado |
| Q124 | - |  |  | SI | Criterio indicación médica Crioprecipitados |
| Q125 | - |  |  | SI | Otra comorbilidad concentrado de glóbulos rojos le... |
| Q126 | - |  |  | SI | Otra comorbilidad concentrado unitario de plaqueta... |
| Q127 | - |  |  | SI | Otra comorbilidad concentrado plaquetario de afére... |
| Q128 | - |  |  | SI | Otra comorbilidad plasma fresco congelado |
| Q129 | - |  |  | SI | Otra comorbilidad crioprecipitado |
| Q13 | - |  |  | SI | Carácter de la Transfusión |
| Q14 | - |  |  | SI | Transfusiones Previas |
| Q15 | - |  |  | SI | Reacciones Adversas |
| Q16 | - |  |  | SI | Edad |
| Q17 | - |  |  | SI | Peso |
| Q17ObsDR | - |  |  | SI | Peso DR |
| Q18 | - |  |  | SI | Talla |
| Q18ObsDR | - |  |  | SI | Talla DR |
| Q19 | - |  |  | SI | Grupo ABO y Rh |
| Q20 | - |  |  | SI | Para el día |
| Q21 | - |  |  | SI | Hora |
| Q22 | - |  |  | SI | Lugar |
| Q23 | - |  |  | SI | Para el día |
| Q24 | - |  |  | SI | Hora |
| Q25 | - |  |  | SI | Fecha Transfusión Previa |
| Q26 | - |  |  | SI | Fecha Reacciones Adversas |
| Q27 | - |  |  | SI | Tipo de Reacción |
| Q28 | - |  |  | SI | Concentrado de Glóbulos Rojos Leucorreducidos |
| Q29 | - |  |  | SI | Irradiados (Concentrado de Glóbulos Rojos Leucorre... |
| Q30 | - |  |  | SI | Filtrados (Concentrado de Glóbulos Rojos Leucorred... |
| Q31 | - |  |  | SI | Concentrado Unitario de Plaquetas |
| Q32 | - |  |  | SI | Irradiados (Concentrado Unitario de Plaquetas) |
| Q33 | - |  |  | SI | Filtrados (Concentrado Unitario de Plaquetas) |
| Q34 | - |  |  | SI | Concentrado Plaquetario de Aféresis |
| Q35 | - |  |  | SI | Irradiados (Concentrado Plaquetario de Aféresis) |
| Q36 | - |  |  | SI | Filtrados (Concentrado Plaquetario de Aféresis) |
| Q37 | - |  |  | SI | Plasma Fresco Congelado |
| Q38 | - |  |  | SI | Irradiados (Plasma Fresco Congelado) |
| Q39 | - |  |  | SI | Filtrados (Plasma Fresco Congelado) |
| Q40 | - |  |  | SI | Crioprecipitado |
| Q41 | - |  |  | SI | Irradiados (Crioprecipitado) |
| Q42 | - |  |  | SI | Filtrados (Crioprecipitado) |
| Q43 | - |  |  | SI | Fecha |
| Q44 | - |  |  | SI | Hematocrito |
| Q44ObsDR | - |  |  | SI | Hematocrito DR |
| Q45 | - |  |  | SI | Hemoglobina |
| Q45ObsDR | - |  |  | SI | Hemoglobina DR |
| Q46 | - |  |  | SI | Recuento Plaquetario |
| Q46ObsDR | - |  |  | SI | Recuento Plaquetario DR |
| Q47 | - |  |  | SI | TP |
| Q47ObsDR | - |  |  | SI | TP DR |
| Q48 | - |  |  | SI | TTPA |
| Q48ObsDR | - |  |  | SI | TTPA DR |
| Q49 | - |  |  | SI | INR |
| Q49ObsDR | - |  |  | SI | INR DR |
| Q50 | - |  |  | SI | Fibrinógeno |
| Q50ObsDR | - |  |  | SI | Fibrinógeno DR |
| Q51 | - |  |  | SI | Otros |
| Q52 | - |  |  | SI | Edad |
| Q53 | - |  |  | SI | Grupo ABO y Rh |
| Q53ObsDR | - |  |  | SI | Grupo ABO y Rh DR |
| Q54 | - |  |  | SI | TTPA |
| Q54ObsDR | - |  |  | SI | TTPA DR |
| Q55 | - |  |  | SI | INR |
| Q55ObsDR | - |  |  | SI | INR DR |
| Q56 | - |  |  | SI | Fecha Solicitud |
| Q57 | - |  |  | SI | Hora Solicitud |
| Q58 | - |  |  | SI | Nombre Paciente |
| Q59 | - |  |  | SI | Apellido Paterno |
| Q60 | - |  |  | SI | Apellido Materno |
| Q61 | - |  |  | SI | RUN |
| Q62 | - |  |  | SI | Unidad/ Servicio / Local (ambulatorio) |
| Q63 | - |  |  | SI | Sala |
| Q64 | - |  |  | SI | Diagnóstico |
| Q65 | - |  |  | SI | N° Folio |
| Q66 | - |  |  | SI | Medico Solicitante |
| Q67 | - |  |  | SI | Plasma Inmune (HANTA) |
| Q68 | - |  |  | SI | Filtrado |
| Q69 | - |  |  | SI | Irradiado |
| Q70 | - |  |  | SI | No Aplica / Sin Resultado (Hematocrito) |
| Q71 | - |  |  | SI | No Aplica / Sin Resultado (Hemoglobina) |
| Q72 | - |  |  | SI | No Aplica / Sin Resultado (Recuento Plaquetario) |
| Q73 | - |  |  | SI | No Aplica / Sin Resultado (TP) |
| Q74 | - |  |  | SI | No Aplica / Sin Resultado (TTPA) |
| Q75 | - |  |  | SI | No Aplica / Sin Resultado (INR) |
| Q76 | - |  |  | SI | No Aplica / Sin Resultado (Fibrinógeno) |
| Q77 | - |  |  | SI | Fecha de Nacimiento |
| Q78 | - |  |  | SI | Requerimiento de O2 |
| Q79 | - |  |  | SI | VMNI |
| Q80 | - |  |  | SI | ECMO |
| Q81 | - |  |  | SI | CEC |
| Q82 | - |  |  | SI | Unidad / Servicio |
| Q83 | - |  |  | SI | Sala / Cama |
| Q84 | - |  |  | SI | Cama |
| Q85 | - |  |  | SI | VMI |
| Q86 | - |  |  | SI | Médico Solicitante |
| Q87 | - |  |  | SI | Comentario concentrado de glóbulos rojos leucorred... |
| Q88 | - |  |  | SI | Comentario concentrado unitario de plaquetas |
| Q89 | - |  |  | SI | Comentario concentrado plaquetario de aféresis |
| Q90 | - |  |  | SI | Comentario plasma fresco congelado |
| Q91 | - |  |  | SI | Comentario crioprecipitado |
| Q92 | - |  |  | SI | Motivo de indicación concentrado de glóbulos rojos... |
| Q93 | - |  |  | SI | Motivo de indicación concentrado unitario de plaqu... |
| Q94 | - |  |  | SI | Motivo de indicación concentrado plaquetario de af... |
| Q95 | - |  |  | SI | Motivo de indicación plasma fresco congelado |
| Q96 | - |  |  | SI | Motivo de indicación crioprecipitado |
| Q97 | - |  |  | SI | Otra comorbilidad |
| Q98 | - |  |  | SI | Tipo unidad Concentrado de glóbulos rojos leucorre... |
| Q99 | - |  |  | SI | Tipo unidad Concentrado unitario de plaquetas |
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
| SIZE_Childsub | double |  |  | NO | Childsub |
| SIZE_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| SIZE_CreatedDate | date |  |  | SI | Created Date |
| SIZE_CreatedTime | time |  |  | SI | Created Time |
| SIZE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SIZE_DateFrom | date |  |  | SI | Date From |
| SIZE_DateTo | date |  |  | SI | Date To |
| SIZE_Desc | varchar |  |  | SI | Description |
| SIZE_RowId | varchar |  |  | NO | - |
| SIZE_TumourSize | varchar |  |  | SI | Size |
| SIZE_UpdatedDate | date |  |  | SI | Updated Date |
| SIZE_UpdatedTime | time |  |  | SI | Updated Time |
| SIZE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*