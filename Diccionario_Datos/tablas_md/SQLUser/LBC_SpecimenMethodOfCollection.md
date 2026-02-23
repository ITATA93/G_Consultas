# SQLUser.LBC_SpecimenMethodOfCollection

**Schema:** SQLUser
**Columnas:** 166
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPMC_ParRef | bigint | PK |  | NO | Parent Specimen DR |
| LBCSPMC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPMC_MethodOfCollection_DR | bigint |  | FK | SI | Method Of Collection DR |
| LBCSPMC_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | ORIGEN |
| Q02 | - |  |  | SI | Servicio de Salud |
| Q03 | - |  |  | SI | Establecimiento |
| Q04 | - |  |  | SI | Comuna y Ciudad |
| Q05 | - |  |  | SI | Fono |
| Q06 | - |  |  | SI | DESTINO |
| Q07 | - |  |  | SI | Servicio de Salud |
| Q08 | - |  |  | SI | LUGAR DE TRASLADO DE PACIENTE |
| Q09 | - |  |  | SI | DOMICILIO |
| Q10 | - |  |  | SI | Comuna |
| Q100 | - |  |  | SI | Fase intermitente dosis recibida |
| Q101 | - |  |  | SI | Baciloscopia Inicio |
| Q102 | - |  |  | SI | Baciloscopia 1 Mes |
| Q103 | - |  |  | SI | Baciloscopia 2 Meses |
| Q104 | - |  |  | SI | Baciloscopia 3 Meses |
| Q105 | - |  |  | SI | Baciloscopia 4 Meses |
| Q106 | - |  |  | SI | Baciloscopia 5 Meses |
| Q107 | - |  |  | SI | Baciloscopia 6 Meses |
| Q108 | - |  |  | SI | Baciloscopia 7 Meses |
| Q109 | - |  |  | SI | Baciloscopia 8 Meses |
| Q11 | - |  |  | SI | Comuna |
| Q110 | - |  |  | SI | Baciloscopia 9 Meses |
| Q111 | - |  |  | SI | Cultivo Inicio |
| Q112 | - |  |  | SI | Cultivo 1 Mes |
| Q113 | - |  |  | SI | Cultivo 2 Meses |
| Q114 | - |  |  | SI | Cultivo 3 Meses |
| Q115 | - |  |  | SI | Cultivo 4 Meses |
| Q116 | - |  |  | SI | Cultivo 5 Meses |
| Q117 | - |  |  | SI | Cultivo 6 Meses |
| Q118 | - |  |  | SI | Cultivo 7 Meses |
| Q119 | - |  |  | SI | Cultivo 8 Meses |
| Q12 | - |  |  | SI | Fono |
| Q120 | - |  |  | SI | Cultivo 9 Meses |
| Q13 | - |  |  | SI | DIAGNOSTICO TBC |
| Q14 | - |  |  | SI | CONFIRMACIÓN |
| Q15 | - |  |  | SI | BKD N°Cruces Directo |
| Q16 | - |  |  | SI | Cult. N° Colonias |
| Q17 | - |  |  | SI | Valor ADA |
| Q18 | - |  |  | SI | Tipo de Muestra |
| Q19 | - |  |  | SI | Resultado Riesgo de Abandono |
| Q19ObsDR | - |  |  | SI | Resultado Riesgo de Abandono DR |
| Q20 | - |  |  | SI | ANTECEDENTES DE TRATAMIENTO |
| Q21 | - |  |  | SI | Virgen a Tratamiento |
| Q22 | - |  |  | SI | Antes Tratado |
| Q23 | - |  |  | SI | Recaída |
| Q24 | - |  |  | SI | Abandono |
| Q25 | - |  |  | SI | Fecha de 1° TBC |
| Q26 | - |  |  | SI | Fecha de Recaída |
| Q27 | - |  |  | SI | Fecha de último abandono |
| Q28 | - |  |  | SI | NOTIFICACIÓN |
| Q29 | - |  |  | SI | Fecha |
| Q30 | - |  |  | SI | Lugar de Notificación |
| Q31 | - |  |  | SI | TRATAMIENTO ACTUAL INDICADO |
| Q32 | - |  |  | SI | Fecha de Inicio de Tratamiento |
| Q33 | - |  |  | SI | Fase Diaria N° dosis a recibir |
| Q34 | - |  |  | SI | Fase Bisemanal N° Dosis a recibir |
| Q35 | - |  |  | SI | Total dosis recibidas |
| Q36 | - |  |  | SI | Total dosis recibidas |
| Q37 | - |  |  | SI | DOCUMENTOS ADJUNTOS |
| Q38 | - |  |  | SI | Radiografía Tórax |
| Q39 | - |  |  | SI | Tarjeta Tratamiento |
| Q40 | - |  |  | SI | Epicrisis |
| Q41 | - |  |  | SI | ANTECEDENTES MÓRBIDOS |
| Q42 | - |  |  | SI | Alcohol |
| Q43 | - |  |  | SI | DM |
| Q44 | - |  |  | SI | Tabaquismo |
| Q45 | - |  |  | SI | Silicosis |
| Q46 | - |  |  | SI | Coinfección Retroviral |
| Q47 | - |  |  | SI | Otras |
| Q48 | - |  |  | SI | Observaciones |
| Q49 | - |  |  | SI | Reacciones adversas a medicamentos |
| Q50 | - |  |  | SI | Corresponde estudio de Contacto |
| Q51 | - |  |  | SI | Fono |
| Q52 | - |  |  | SI | Correos@ |
| Q53 | - |  |  | SI | Nombre y Firma del Profesional |
| Q54 | - |  |  | SI | Origen |
| Q55 | - |  |  | SI | Establecimiento o CESFAM |
| Q56 | - |  |  | SI | Organo |
| Q57 | - |  |  | SI | LUGAR TRASLADO DEL PACIENTE |
| Q58 | - |  |  | SI | Hepatitis |
| Q59 | - |  |  | SI | Fármaco Isoniacida |
| Q60 | - |  |  | SI | Fármaco Rifampicina |
| Q61 | - |  |  | SI | Fármaco Pirazinamida |
| Q62 | - |  |  | SI | Fármaco Estreptomicina |
| Q63 | - |  |  | SI | Dosis Diaria Isoniacida (5mg/kg/d (300 mg/d)) |
| Q64 | - |  |  | SI | Dosis Diaria Rifampicina (10 mg/kg/d (600 mg/d)) |
| Q65 | - |  |  | SI | Dosis Diaria Pirazinamida (25-30 mg/kg/d) |
| Q66 | - |  |  | SI | Dosis Diaria Etambutol (15-20 mg/kg/d) |
| Q67 | - |  |  | SI | Dosis Diaria Estreptomicina (15 mg/kg/d) |
| Q68 | - |  |  | SI | Dosis Trisemanal  Isoniacida (10 mg/kg/d) |
| Q69 | - |  |  | SI | Dosis Trisemanal Rifampicina (10 mg/kg/d) |
| Q70 | - |  |  | SI | Dosis Trisemanal Pirazinamida (35 mg/kg) |
| Q71 | - |  |  | SI | Dosis Trisemanal Estambutol (30 mg/kg) |
| Q72 | - |  |  | SI | Presentación Isoniacida 100 mg |
| Q73 | - |  |  | SI | Presentación Isoniacida 300 mg |
| Q74 | - |  |  | SI | Presentación Rifampicina 300 mg |
| Q75 | - |  |  | SI | Presentación Pirazamida 250 mg |
| Q76 | - |  |  | SI | Presentación Etambutol 400 mg |
| Q77 | - |  |  | SI | Presentación Estreptomicina 1 gr |
| Q78 | - |  |  | SI | Total  dosis Isoniacida |
| Q79 | - |  |  | SI | total dosis rifampicina |
| Q80 | - |  |  | SI | Total dosis pirazinamida |
| Q81 | - |  |  | SI | Total dosis etambutamol |
| Q82 | - |  |  | SI | Total dosis estreptomicina |
| Q83 | - |  |  | SI | Cantidad de tabletas isoniacida |
| Q84 | - |  |  | SI | Cantidad de tabletas rifampicina |
| Q85 | - |  |  | SI | Cantidad de tabletas pirazinamida |
| Q86 | - |  |  | SI | Cantidad de tabletas etambutol |
| Q87 | - |  |  | SI | Cantidad de tabletas estreptomicina |
| Q88 | - |  |  | SI | Total Administrado Isoniacida |
| Q89 | - |  |  | SI | Total Administrado Rifampicina |
| Q90 | - |  |  | SI | Total Administrado Pirazinamida |
| Q91 | - |  |  | SI | Total Administrado etambutol |
| Q92 | - |  |  | SI | total administrado estreptomicina |
| Q93 | - |  |  | SI | Fármaco Estambutol |
| Q94 | - |  |  | SI | Fármaco Isoniacida |
| Q95 | - |  |  | SI | Fase diaria fecha de inicio |
| Q96 | - |  |  | SI | Fase  intermitente  fecha de incio |
| Q97 | - |  |  | SI | fase diaria tiempo cumplido |
| Q98 | - |  |  | SI | Fase intermitente tiempo cumplido |
| Q99 | - |  |  | SI | fase diaria dosis recibida |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*