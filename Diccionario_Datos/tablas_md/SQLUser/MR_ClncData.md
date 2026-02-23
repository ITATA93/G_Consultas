# SQLUser.MR_ClncData

**Schema:** SQLUser
**Columnas:** 195
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCLN_MRADM_ParRef | bigint | PK |  | NO | Des Ref to MRADM |
| MRCLN_BldPressDias | double |  |  | SI | Blood Pressure Diastolic |
| MRCLN_BldPressSyst | double |  |  | SI | Blood Pressure Systolic |
| MRCLN_BodyTemp | varchar |  |  | SI | Body Temperature |
| MRCLN_CTPCP_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| MRCLN_Childsub | numeric |  |  | NO | MRCLN Childsub (NewKey) |
| MRCLN_Date | date |  |  | SI | Date |
| MRCLN_DateUpdate | date |  |  | SI | DateUpdate |
| MRCLN_OrderState | bigint |  |  | SI | Admin Order State Des Ref to OECOrdSt |
| MRCLN_PRCrit | varchar |  |  | SI | Pulse Rate Critical Flag |
| MRCLN_PressCrit | varchar |  |  | SI | Blood Pressure Critical Flag |
| MRCLN_PulseRate | double |  |  | SI | Pulse Rate |
| MRCLN_RespirationRate | double |  |  | SI | Respiration Rate |
| MRCLN_RowId | varchar |  |  | NO | - |
| MRCLN_TempCrit | varchar |  |  | SI | Temperature Critical Flag |
| MRCLN_Time | time |  |  | SI | Time |
| MRCLN_TimeUpdate | time |  |  | SI | TimeUpdate |
| MRCLN_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Identidad |
| Q01a | - |  |  | SI | Identidad (Doble Identificador) |
| Q02 | - |  |  | SI | Brazalete de identificación (Paciente correcto, le... |
| Q02a | - |  |  | SI | Brazalete de identificación (Paciente correcto, le... |
| Q03 | - |  |  | SI | Ficha |
| Q04 | - |  |  | SI | Area Operatoria |
| Q05 | - |  |  | SI | Procedimiento Quirúrgico |
| Q06 | - |  |  | SI | Consentimiento Quirurgico |
| Q06a | - |  |  | SI | Consentimiento Quirúrgico Informado Firmado |
| Q07 | - |  |  | SI | Area Operatoria Marcada |
| Q07a | - |  |  | SI | Área Operatoria / Lateralidad Marcada |
| Q08 | - |  |  | SI | No Aplica |
| Q09 | - |  |  | SI | Medias Antiembolicas |
| Q09a | - |  |  | SI | Medidas de Prevención Tromboembólica |
| Q10 | - |  |  | SI | No aplica |
| Q100 | - |  |  | SI | Comentario |
| Q101 | - |  |  | SI | Instrumental e insumos en condiciones de ser utili... |
| Q102 | - |  |  | SI | Comentario |
| Q103 | - |  |  | SI | Hay Instrumental y ayuda disponible |
| Q104 | - |  |  | SI | Comentario |
| Q105 | - |  |  | SI | Lugar del cuerpo a intervenir |
| Q106 | - |  |  | SI | Paciente inconsciente |
| Q107 | - |  |  | SI | Paciente traqueotomizado (TQT) |
| Q108 | - |  |  | SI | Incisión sobre xifoides |
| Q109 | - |  |  | SI | Uso de material instrumento comburente (electrobis... |
| Q10a | - |  |  | SI | Implica Máquina de anestesia/ Drogas anestésicas/ ... |
| Q11 | - |  |  | SI | Chequeo Seguridad Anestesica |
| Q110 | - |  |  | SI | Uso de oxígeno fuente abierta (naricera, mascarill... |
| Q111 | - |  |  | SI | ¿Se utiliza antes de la operación un antiséptico p... |
| Q112 | - |  |  | SI | ¿Hay otros posibles contribuyentes (p. ej., desfib... |
| Q113 | - |  |  | SI | Paciente intubación endotraqueal (IET) |
| Q114 | - |  |  | SI | Comentario |
| Q115 | - |  |  | SI | Comentario |
| Q116 | - |  |  | SI | Comentario |
| Q117 | - |  |  | SI | Comentario |
| Q118 | - |  |  | SI | Comentario |
| Q119 | - |  |  | SI | Comentario |
| Q12 | - |  |  | SI | Consentimiento Anestesico |
| Q120 | - |  |  | SI | Comentario |
| Q121 | - |  |  | SI | Comentario |
| Q122 | - |  |  | SI | Comentario |
| Q123 | - |  |  | SI | Profesional Responsable de la Medición |
| Q124 | - |  |  | SI | Comentarios / Observaciones |
| Q125 | - |  |  | SI | Cirugía / Procedimiento Principal |
| Q126 | - |  |  | SI | Exámenes preoperatorios |
| Q127 | - |  |  | SI | Comentario |
| Q128 | - |  |  | SI | Ayuno |
| Q129 | - |  |  | SI | Comentario |
| Q12a | - |  |  | SI | Consentimiento Anestesico |
| Q12b | - |  |  | SI | Consentimiento Anestesico |
| Q13 | - |  |  | SI | Oximetro de Pulso instalado y funcionando |
| Q130 | - |  |  | SI | Paciente bañado |
| Q131 | - |  |  | SI | Comentario |
| Q132 | - |  |  | SI | Vaciamiento de vejiga o micción |
| Q133 | - |  |  | SI | comentario |
| Q134 | - |  |  | SI | Ropa de pabellón |
| Q135 | - |  |  | SI | comentario |
| Q136 | - |  |  | SI | Sin ropa interior |
| Q137 | - |  |  | SI | comentario |
| Q13a | - |  |  | SI | Oximetro de Pulso instalado y funcionando |
| Q13b | - |  |  | SI | Oximetro de Pulso instalado y funcionando |
| Q14 | - |  |  | SI | Alergias conocidas |
| Q15 | - |  |  | SI | Vía Aérea Difícil |
| Q16 | - |  |  | SI | Riesgo de Aspiración |
| Q17 | - |  |  | SI | Riesgo sangramiento > 500 ml. ( 7ML/KG en niños) |
| Q18 | - |  |  | SI | Confirmacion miembros del equipo |
| Q19 | - |  |  | SI | Identidad del paciente |
| Q20 | - |  |  | SI | Area Operatoria |
| Q21 | - |  |  | SI | Procedimiento quirúrgico |
| Q22 | - |  |  | SI | Escenarios Imprevistos |
| Q23 | - |  |  | SI | Duración estimada cirugía |
| Q24 | - |  |  | SI | Pérdidas de sangres estimadas |
| Q25 | - |  |  | SI | Otros |
| Q26 | - |  |  | SI | Equipo Anestesia revisa |
| Q27 | - |  |  | SI | Ropa |
| Q28 | - |  |  | SI | Instrumental |
| Q29 | - |  |  | SI | Funcionamiento correcto de equipos |
| Q2a | - |  |  | SI | Identidad (Doble Identificador) |
| Q30 | - |  |  | SI | ¿ Se realizó profilaxis antibiótica? |
| Q31 | - |  |  | SI | ¿Se ha desplegado la imagenología necesaria? |
| Q32 | - |  |  | SI | El nombre del procedimiento realizado |
| Q33 | - |  |  | SI | Conteo instrumental correcto |
| Q34 | - |  |  | SI | Conteo compresas correcto |
| Q35 | - |  |  | SI | Conteo agujas correcto |
| Q36 | - |  |  | SI | No Aplica |
| Q37 | - |  |  | SI | No Aplica |
| Q38 | - |  |  | SI | Nombre completo del paciente |
| Q39 | - |  |  | SI | RUT del paciente |
| Q3a | - |  |  | SI | Ficha |
| Q40 | - |  |  | SI | Fecha de toma de la muestra |
| Q41 | - |  |  | SI | Identificación clara del tejido u órgano y  locali... |
| Q42 | - |  |  | SI | Numeración de la muestra en caso de haber más de u... |
| Q43 | - |  |  | SI | Problema Equipamiento |
| Q44 | - |  |  | SI | Revision datos importantes para la recuperacion |
| Q45 | - |  |  | SI | Comentario |
| Q46 | - |  |  | SI | Comentario |
| Q47 | - |  |  | SI | Comentario |
| Q48 | - |  |  | SI | Comentario |
| Q49 | - |  |  | SI | Comentario |
| Q50 | - |  |  | SI | Comentario |
| Q51 | - |  |  | SI | Comentario |
| Q52 | - |  |  | SI | Máquina de Anestesia |
| Q52a | - |  |  | SI | Comentario |
| Q53 | - |  |  | SI | Fármacos disponibles y al alcance de ser utilizado... |
| Q53a | - |  |  | SI | Comentario |
| Q54 | - |  |  | SI | Insumos |
| Q54a | - |  |  | SI | Comentario |
| Q55 | - |  |  | SI | Laringoscopio |
| Q55a | - |  |  | SI | Comentario |
| Q56 | - |  |  | SI | Equipos de Aspiración |
| Q56a | - |  |  | SI | Comentario |
| Q57 | - |  |  | SI | Evaluación Preanestésica |
| Q57a | - |  |  | SI | Comentario |
| Q58 | - |  |  | SI | Consentimiento Anestésico Informado Firmado |
| Q58a | - |  |  | SI | Comentario |
| Q59 | - |  |  | SI | Oxímetro de Pulso instalado y funcionando |
| Q59a | - |  |  | SI | Comentario |
| Q5a | - |  |  | SI | Procedimiento / Intervención Quirúrgica |
| Q60 | - |  |  | SI | Brazalete de Alergia (legible) |
| Q61 | - |  |  | SI | Comentario |
| Q62 | - |  |  | SI | Comentario |
| Q63 | - |  |  | SI | Comentario |
| Q64 | - |  |  | SI | Comentario |
| Q65 | - |  |  | SI | Comentario |
| Q87 | - |  |  | SI | Previsión Accesos Venosos / Reposición Volumen |
| Q88 | - |  |  | SI | Comentario |
| Q89 | - |  |  | SI | Destino Post-Operatorio |
| Q90 | - |  |  | SI | Comentario |
| Q91 | - |  |  | SI | Hay Instrumental y ayuda disponible |
| Q92 | - |  |  | SI | Comentarios Hay Instrumental y ayuda disponible |
| Q93 | - |  |  | SI | Se ha provisto disponibilidad de líquidos adecuado... |
| Q94 | - |  |  | SI | Comentario |
| Q95 | - |  |  | SI | Confirma indicación profilaxis ATB |
| Q96 | - |  |  | SI | Comentario |
| Q97 | - |  |  | SI | Confirma disponibilidad de imágenes |
| Q98 | - |  |  | SI | Comentario |
| Q99 | - |  |  | SI | Equipos, instrumental, insumos, implantes, rayos d... |
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