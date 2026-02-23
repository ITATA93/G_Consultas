# SQLUser.CT_LocTransport

**Schema:** SQLUser
**Columnas:** 224
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANSP_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q01 | - |  |  | SI | Región |
| Q02 | - |  |  | SI | Servicio de Salud |
| Q03 | - |  |  | SI | Establecimiento |
| Q04 | - |  |  | SI | Consultorio donde se controlaría según su domicili... |
| Q05 | - |  |  | SI | Escolaridad |
| Q06 | - |  |  | SI | Ocupación |
| Q07 | - |  |  | SI | Domicilio Paciente |
| Q08 | - |  |  | SI | Fono |
| Q09 | - |  |  | SI | Comuna Residencia |
| Q10 | - |  |  | SI | Nombre |
| Q100 | - |  |  | SI | Cutánea |
| Q101 | - |  |  | SI | Digestiva |
| Q102 | - |  |  | SI | VIII Par |
| Q103 | - |  |  | SI | Otras |
| Q104 | - |  |  | SI | Atribuible a |
| Q105 | - |  |  | SI | Suspención de la droga |
| Q106 | - |  |  | SI | Días de hospitalización previo a la muerte |
| Q107 | - |  |  | SI | ¿Se formuló el diagnóstico de TBC al ingreso? |
| Q108 | - |  |  | SI | ¿Se formuló el diagnóstico de TBC al egreso? |
| Q109 | - |  |  | SI | En la asistencia del paciente a un establecimiento... |
| Q11 | - |  |  | SI | Apellido Paterno |
| Q110 | - |  |  | SI | En el diagnóstico de su TBC en el establecimiento |
| Q111 | - |  |  | SI | En la iniciativa del tratamiento |
| Q112 | - |  |  | SI | No hay evidencias  de demoras |
| Q113 | - |  |  | SI | La atención en salud antes de la muerte, fue adecu... |
| Q114 | - |  |  | SI | Por falta de atención médica |
| Q115 | - |  |  | SI | Falla Médica |
| Q116 | - |  |  | SI | falla de recursos |
| Q117 | - |  |  | SI | Por inaccesiblidad geográfica |
| Q118 | - |  |  | SI | Inaccesiblidad económica |
| Q119 | - |  |  | SI | Otras causas de atención inadecuada |
| Q12 | - |  |  | SI | Apellido Materno |
| Q120 | - |  |  | SI | Otras |
| Q121 | - |  |  | SI | Fecha de Fallecimiento |
| Q122 | - |  |  | SI | Falleció en |
| Q123 | - |  |  | SI | Servicio de Urgencia |
| Q124 | - |  |  | SI | Domicilio |
| Q125 | - |  |  | SI | Consultorio |
| Q126 | - |  |  | SI | Otros |
| Q127 | - |  |  | SI | Otro centro |
| Q128 | - |  |  | SI | Desconocido |
| Q129 | - |  |  | SI | Causa de la muerte |
| Q13 | - |  |  | SI | Edad |
| Q130 | - |  |  | SI | Causa Inmediata |
| Q131 | - |  |  | SI | Causas originarias |
| Q132 | - |  |  | SI | Estados morbosos concomitantes |
| Q133 | - |  |  | SI | Fundamentos del diagnóstico de la causa de muerte |
| Q134 | - |  |  | SI | Fundamentos Autopsia |
| Q135 | - |  |  | SI | Fundamentos Biopsia |
| Q136 | - |  |  | SI | Bacteriológica |
| Q137 | - |  |  | SI | D |
| Q138 | - |  |  | SI | Sólo C |
| Q139 | - |  |  | SI | Bacteriológica negativa |
| Q14 | - |  |  | SI | Fecha de Nacimiento |
| Q140 | - |  |  | SI | Desconocida |
| Q141 | - |  |  | SI | Laboratorio |
| Q142 | - |  |  | SI | ADA(+) |
| Q143 | - |  |  | SI | Otros (+) |
| Q144 | - |  |  | SI | Otros fundamentos |
| Q145 | - |  |  | SI | Solamente Clínica |
| Q146 | - |  |  | SI | Atención médica última enfermedad |
| Q147 | - |  |  | SI | Calidad de quien certifica la muerte |
| Q148 | - |  |  | SI | Se efectuó la notificación de TBC |
| Q149 | - |  |  | SI | ¿Estaba inscrito en su Consultorio? |
| Q15 | - |  |  | SI | Sexo |
| Q150 | - |  |  | SI | ¿Había consultado en alguna oportunidad antes del ... |
| Q151 | - |  |  | SI | ¿Estaba siendo controlado en algún Programa de Cró... |
| Q152 | - |  |  | SI | Cual programa crónico |
| Q153 | - |  |  | SI | ¿En que fecha fué la última consulta en su Centro ... |
| Q154 | - |  |  | SI | Fecha desconocida última consulta en su Centro de ... |
| Q155 | - |  |  | SI | ¿Se le pidió BK en la consulta a su Centro de Salu... |
| Q156 | - |  |  | SI | ¿En que fecha fue pedida la última BK, antes del d... |
| Q157 | - |  |  | SI | Se desconoce fecha de petición |
| Q158 | - |  |  | SI | ¿Como resultó el estudio de contacto en niños y ad... |
| Q159 | - |  |  | SI | Comentarios DR. |
| Q16 | - |  |  | SI | Previsión |
| Q160 | - |  |  | SI | Usted concluye que falleció de |
| Q161 | - |  |  | SI | Nombre del Médico Auditor Dr.(a) |
| Q162 | - |  |  | SI | Fecha Auditoria |
| Q163 | - |  |  | SI | Confirmación del diagnóstico de la localización pr... |
| Q164 | - |  |  | SI | Calificación al momento  del diagnóstico |
| Q165 | - |  |  | SI | Otros antecedentes |
| Q166 | - |  |  | SI | Tipo reacción |
| Q167 | - |  |  | SI | Historia del episodio |
| Q168 | - |  |  | SI | si la respuesta es no |
| Q169 | - |  |  | SI | Falleció en |
| Q17 | - |  |  | SI | Nacionalidad |
| Q170 | - |  |  | SI | Fundamentos del diagnóstico (+) |
| Q18 | - |  |  | SI | RUT |
| Q19 | - |  |  | SI | Factores de riesgo para tuberculosis (TBC) |
| Q20 | - |  |  | SI | Diagnóstico  TBC. Localización Principal |
| Q21 | - |  |  | SI | Organo |
| Q22 | - |  |  | SI | 2° Localización de TBC |
| Q23 | - |  |  | SI | Fecha de diagnóstico |
| Q24 | - |  |  | SI | Fecha de Notificación |
| Q25 | - |  |  | SI | Lugar de Notificación |
| Q26 | - |  |  | SI | Baciloscopía (BK) D+ |
| Q27 | - |  |  | SI | Baciloscopía C+ |
| Q28 | - |  |  | SI | N° colonias |
| Q29 | - |  |  | SI | Biopsia |
| Q30 | - |  |  | SI | Sin Confirmación (sc) |
| Q31 | - |  |  | SI | ADA (+) |
| Q32 | - |  |  | SI | Fundamento y diagnóstico de la 2°&nbsp |
| Q33 | - |  |  | SI | Caso Nuevo |
| Q34 | - |  |  | SI | Recaída |
| Q35 | - |  |  | SI | Abandono Recuperado |
| Q36 | - |  |  | SI | En caso de ser AT,  Fecha de la 1° TBC |
| Q37 | - |  |  | SI | Fracaso de tratamiendo anterior (cpn BKD+ >= 4° me... |
| Q38 | - |  |  | SI | Crónico |
| Q39 | - |  |  | SI | TBC desconocida previo a la muerte |
| Q40 | - |  |  | SI | N° Cicatrices de BCG |
| Q41 | - |  |  | SI | Dosis Diarias (DD): N° 1 |
| Q42 | - |  |  | SI | Dosis Diarias (DD): N° 2 |
| Q43 | - |  |  | SI | Dosis Diarias (DD): N° 3 |
| Q44 | - |  |  | SI | Dosis Diarias (DD): N° 4 |
| Q45 | - |  |  | SI | Dosis Diarias (DD): N° 5 |
| Q46 | - |  |  | SI | Dosis Bisemanal (DB): N° 1 |
| Q47 | - |  |  | SI | Dosis Bisemanal (DB): N° 2 |
| Q48 | - |  |  | SI | Dosis Bisemanal (DB): N° 3 |
| Q49 | - |  |  | SI | Dosis Bisemanal (DB): N° 4 |
| Q50 | - |  |  | SI | Dosis Bisemanal (DB): N° 5 |
| Q51 | - |  |  | SI | BK (D) 1° mes |
| Q52 | - |  |  | SI | BK (D) 2° mes |
| Q53 | - |  |  | SI | BK (D) 3° mes |
| Q54 | - |  |  | SI | BK (D) 4° Mes |
| Q55 | - |  |  | SI | BK (D) 5° mes |
| Q56 | - |  |  | SI | BK (D) 6° mes |
| Q57 | - |  |  | SI | BK (D) 7° mes |
| Q58 | - |  |  | SI | BK (D) 8° mes |
| Q59 | - |  |  | SI | BK (D) 9° mes |
| Q60 | - |  |  | SI | BK (C) 1° mes |
| Q61 | - |  |  | SI | BK (C) 2° mes |
| Q62 | - |  |  | SI | BK (C) 3° mes |
| Q63 | - |  |  | SI | BK (C) 4° mes |
| Q64 | - |  |  | SI | BK (C) 5° mes |
| Q65 | - |  |  | SI | BK (C) 6° mes |
| Q66 | - |  |  | SI | BK (C) 7° mes |
| Q67 | - |  |  | SI | BK (C) 8° mes |
| Q68 | - |  |  | SI | BK (C) 9° mes |
| Q69 | - |  |  | SI | Dosis recibida 1° mes |
| Q70 | - |  |  | SI | dosis recibida 2° mes |
| Q71 | - |  |  | SI | Dosis recibida 3° mes |
| Q72 | - |  |  | SI | dosis recibida 4° mes |
| Q73 | - |  |  | SI | dosis recibida 5° mes |
| Q74 | - |  |  | SI | dosis recibida 6° mes |
| Q75 | - |  |  | SI | dosis recibida 7° mes |
| Q76 | - |  |  | SI | Dosis recibida 8° mes |
| Q77 | - |  |  | SI | dosis recibida 9° mes |
| Q78 | - |  |  | SI | RX 1° mes |
| Q79 | - |  |  | SI | RX 2° mes |
| Q80 | - |  |  | SI | RX 3° mes |
| Q81 | - |  |  | SI | RX 4° mes |
| Q82 | - |  |  | SI | RX 5° mes |
| Q83 | - |  |  | SI | RX 6° mes |
| Q84 | - |  |  | SI | RX 7° mes |
| Q85 | - |  |  | SI | RX 8° mes |
| Q86 | - |  |  | SI | RX 9° mes |
| Q87 | - |  |  | SI | Peso (Kg) 1° mes |
| Q88 | - |  |  | SI | Peso (kg) 2° mes |
| Q89 | - |  |  | SI | Peso (Kg) 3° mes |
| Q90 | - |  |  | SI | Peso (Kg) 4° mes |
| Q91 | - |  |  | SI | Peso (Kg) 5° mes |
| Q92 | - |  |  | SI | Peso (Kg) 6° mes |
| Q93 | - |  |  | SI | Peso (Kg) 7° mes |
| Q94 | - |  |  | SI | Peso (Kg) 8° mes |
| Q95 | - |  |  | SI | Peso (Kg) 9° mes |
| Q96 | - |  |  | SI | VIH realizado |
| Q97 | - |  |  | SI | Resultado VIH |
| Q97ObsDR | - |  |  | SI | Resultado VIH DR |
| Q98 | - |  |  | SI | Reacciones Adversas a medicamentos |
| Q99 | - |  |  | SI | Hepática |
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
| TRANSP_Childsub | double |  |  | NO | Childsub |
| TRANSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRANSP_CreatedDate | date |  |  | SI | Created Date |
| TRANSP_CreatedTime | time |  |  | SI | Created Time |
| TRANSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRANSP_DateFrom | date |  |  | SI | Date From |
| TRANSP_DateTo | date |  |  | SI | Date To |
| TRANSP_RowId | varchar |  |  | NO | - |
| TRANSP_Transport_DR | bigint |  | FK | SI | Des Ref Transport |
| TRANSP_UpdatedDate | date |  |  | SI | Updated Date |
| TRANSP_UpdatedTime | time |  |  | SI | Updated Time |
| TRANSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*