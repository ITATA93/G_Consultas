# questionnaire.QTCEITP

> Informe de traslado de pacientes TBC

**Schema:** questionnaire
**Columnas:** 162
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe de traslado de pacientes TBC

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | ORIGEN  |
| Q02 | varchar |  |  | SI | Servicio de Salud |
| Q03 | varchar |  |  | SI | Establecimiento |
| Q04 | varchar |  |  | SI | Comuna y Ciudad |
| Q05 | numeric |  |  | SI | Fono |
| Q06 | varchar |  |  | SI | DESTINO |
| Q07 | varchar |  |  | SI | Servicio de Salud |
| Q08 | varchar |  |  | SI | LUGAR DE TRASLADO DE PACIENTE |
| Q09 | varchar |  |  | SI | DOMICILIO |
| Q10 | varchar |  |  | SI | Comuna |
| Q100 | varchar |  |  | SI | Fase intermitente dosis recibida |
| Q101 | varchar |  |  | SI | Baciloscopia Inicio |
| Q102 | varchar |  |  | SI | Baciloscopia 1 Mes |
| Q103 | varchar |  |  | SI | Baciloscopia 2 Meses |
| Q104 | varchar |  |  | SI | Baciloscopia 3 Meses |
| Q105 | varchar |  |  | SI | Baciloscopia 4 Meses |
| Q106 | varchar |  |  | SI | Baciloscopia 5 Meses |
| Q107 | varchar |  |  | SI | Baciloscopia 6 Meses |
| Q108 | varchar |  |  | SI | Baciloscopia 7 Meses |
| Q109 | varchar |  |  | SI | Baciloscopia 8 Meses |
| Q11 | varchar |  |  | SI | Comuna |
| Q110 | varchar |  |  | SI | Baciloscopia 9 Meses |
| Q111 | varchar |  |  | SI | Cultivo Inicio |
| Q112 | varchar |  |  | SI | Cultivo 1 Mes |
| Q113 | varchar |  |  | SI | Cultivo 2 Meses |
| Q114 | varchar |  |  | SI | Cultivo 3 Meses |
| Q115 | varchar |  |  | SI | Cultivo 4 Meses |
| Q116 | varchar |  |  | SI | Cultivo 5 Meses |
| Q117 | varchar |  |  | SI | Cultivo 6 Meses |
| Q118 | varchar |  |  | SI | Cultivo 7 Meses |
| Q119 | varchar |  |  | SI | Cultivo 8 Meses |
| Q12 | numeric |  |  | SI | Fono |
| Q120 | varchar |  |  | SI | Cultivo 9 Meses |
| Q13 | varchar |  |  | SI | DIAGNOSTICO TBC |
| Q14 | varchar |  |  | SI | CONFIRMACIÓN |
| Q15 | varchar |  |  | SI | BKD N°Cruces Directo |
| Q16 | varchar |  |  | SI | Cult. N° Colonias |
| Q17 | numeric |  |  | SI | Valor ADA |
| Q18 | varchar |  |  | SI | Tipo de Muestra |
| Q19 | varchar |  |  | SI | Resultado Riesgo de Abandono |
| Q19ObsDR | varchar |  | FK | SI | Resultado Riesgo de Abandono DR |
| Q20 | varchar |  |  | SI | ANTECEDENTES DE TRATAMIENTO |
| Q21 | bit |  |  | SI | Virgen a Tratamiento |
| Q22 | bit |  |  | SI | Antes Tratado |
| Q23 | bit |  |  | SI | Recaída |
| Q24 | bit |  |  | SI | Abandono |
| Q25 | date |  |  | SI | Fecha de 1° TBC |
| Q26 | date |  |  | SI | Fecha de Recaída |
| Q27 | date |  |  | SI | Fecha de último abandono |
| Q28 | varchar |  |  | SI | NOTIFICACIÓN |
| Q29 | date |  |  | SI | Fecha |
| Q30 | varchar |  |  | SI | Lugar de Notificación |
| Q31 | varchar |  |  | SI | TRATAMIENTO ACTUAL INDICADO |
| Q32 | date |  |  | SI | Fecha de Inicio de Tratamiento |
| Q33 | numeric |  |  | SI | Fase Diaria N° dosis a recibir |
| Q34 | numeric |  |  | SI | Fase Bisemanal N° Dosis a recibir |
| Q35 | numeric |  |  | SI | Total dosis recibidas |
| Q36 | numeric |  |  | SI | Total dosis recibidas |
| Q37 | varchar |  |  | SI | DOCUMENTOS ADJUNTOS |
| Q38 | bit |  |  | SI | Radiografía Tórax |
| Q39 | bit |  |  | SI | Tarjeta Tratamiento |
| Q40 | bit |  |  | SI | Epicrisis |
| Q41 | varchar |  |  | SI | ANTECEDENTES MÓRBIDOS |
| Q42 | varchar |  |  | SI | Alcohol |
| Q43 | bit |  |  | SI | DM |
| Q44 | varchar |  |  | SI | Tabaquismo |
| Q45 | bit |  |  | SI | Silicosis |
| Q46 | bit |  |  | SI | Coinfección Retroviral |
| Q47 | varchar |  |  | SI | Otras |
| Q48 | varchar |  |  | SI | Observaciones  |
| Q49 | bit |  |  | SI | Reacciones adversas a medicamentos |
| Q50 | varchar |  |  | SI | Corresponde estudio de Contacto |
| Q51 | numeric |  |  | SI | Fono |
| Q52 | varchar |  |  | SI | Correos@ |
| Q53 | varchar |  |  | SI | Nombre y Firma del Profesional |
| Q54 | varchar |  |  | SI | Origen |
| Q55 | varchar |  |  | SI | Establecimiento o CESFAM |
| Q56 | varchar |  |  | SI | Organo |
| Q57 | varchar |  |  | SI | LUGAR TRASLADO DEL PACIENTE |
| Q58 | varchar |  |  | SI | Hepatitis |
| Q59 | bit |  |  | SI | Fármaco Isoniacida |
| Q60 | bit |  |  | SI | Fármaco Rifampicina |
| Q61 | bit |  |  | SI | Fármaco Pirazinamida |
| Q62 | bit |  |  | SI | Fármaco Estreptomicina |
| Q63 | bit |  |  | SI | Dosis Diaria Isoniacida (5mg/kg/d (300 mg/d)) |
| Q64 | bit |  |  | SI | Dosis Diaria Rifampicina (10 mg/kg/d (600 mg/d)) |
| Q65 | bit |  |  | SI | Dosis Diaria Pirazinamida (25-30 mg/kg/d) |
| Q66 | bit |  |  | SI | Dosis Diaria Etambutol (15-20 mg/kg/d) |
| Q67 | bit |  |  | SI | Dosis Diaria Estreptomicina (15 mg/kg/d) |
| Q68 | bit |  |  | SI | Dosis Trisemanal  Isoniacida (10 mg/kg/d) |
| Q69 | bit |  |  | SI | Dosis Trisemanal Rifampicina (10 mg/kg/d) |
| Q70 | bit |  |  | SI | Dosis Trisemanal Pirazinamida (35 mg/kg) |
| Q71 | bit |  |  | SI | Dosis Trisemanal Estambutol (30 mg/kg) |
| Q72 | bit |  |  | SI | Presentación Isoniacida 100 mg |
| Q73 | bit |  |  | SI | Presentación Isoniacida 300 mg |
| Q74 | bit |  |  | SI | Presentación Rifampicina 300 mg |
| Q75 | bit |  |  | SI | Presentación Pirazamida 250 mg |
| Q76 | bit |  |  | SI | Presentación Etambutol 400 mg |
| Q77 | bit |  |  | SI | Presentación Estreptomicina 1 gr |
| Q78 | numeric |  |  | SI | Total  dosis Isoniacida |
| Q79 | numeric |  |  | SI | total dosis rifampicina |
| Q80 | numeric |  |  | SI | Total dosis pirazinamida |
| Q81 | numeric |  |  | SI | Total dosis etambutamol |
| Q82 | numeric |  |  | SI | Total dosis estreptomicina |
| Q83 | numeric |  |  | SI | Cantidad de tabletas isoniacida |
| Q84 | numeric |  |  | SI | Cantidad de tabletas rifampicina |
| Q85 | numeric |  |  | SI | Cantidad de tabletas pirazinamida |
| Q86 | numeric |  |  | SI | Cantidad de tabletas etambutol |
| Q87 | numeric |  |  | SI | Cantidad de tabletas estreptomicina |
| Q88 | numeric |  |  | SI | Total Administrado Isoniacida |
| Q89 | numeric |  |  | SI | Total Administrado Rifampicina |
| Q90 | numeric |  |  | SI | Total Administrado Pirazinamida |
| Q91 | numeric |  |  | SI | Total Administrado etambutol |
| Q92 | numeric |  |  | SI | total administrado estreptomicina |
| Q93 | bit |  |  | SI | Fármaco Estambutol |
| Q94 | bit |  |  | SI | Fármaco Isoniacida |
| Q95 | date |  |  | SI | Fase diaria fecha de inicio |
| Q96 | date |  |  | SI | Fase  intermitente  fecha de incio |
| Q97 | date |  |  | SI | fase diaria tiempo cumplido |
| Q98 | date |  |  | SI | Fase intermitente tiempo cumplido |
| Q99 | varchar |  |  | SI | fase diaria dosis recibida |
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