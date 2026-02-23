# questionnaire.QTCEANFA

> Antecedentes para la auditoria de muerte durante el tratamiento de tuberculosis

**Schema:** questionnaire
**Columnas:** 212
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antecedentes para la auditoria de muerte durante el tratamiento de tuberculosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Región |
| Q02 | varchar |  |  | SI | Servicio de Salud |
| Q03 | varchar |  |  | SI | Establecimiento |
| Q04 | varchar |  |  | SI | Consultorio donde se controlaría según su domicili... |
| Q05 | varchar |  |  | SI | Escolaridad |
| Q06 | varchar |  |  | SI | Ocupación |
| Q07 | varchar |  |  | SI | Domicilio Paciente |
| Q08 | varchar |  |  | SI | Fono  |
| Q09 | varchar |  |  | SI | Comuna Residencia |
| Q10 | varchar |  |  | SI | Nombre |
| Q100 | bit |  |  | SI | Cutánea |
| Q101 | bit |  |  | SI | Digestiva |
| Q102 | bit |  |  | SI | VIII Par |
| Q103 | varchar |  |  | SI | Otras |
| Q104 | varchar |  |  | SI | Atribuible a |
| Q105 | varchar |  |  | SI | Suspención de la droga |
| Q106 | numeric |  |  | SI | Días de hospitalización previo a la muerte |
| Q107 | varchar |  |  | SI | ¿Se formuló el diagnóstico de TBC al ingreso? |
| Q108 | varchar |  |  | SI | ¿Se formuló el diagnóstico de TBC al egreso? |
| Q109 | bit |  |  | SI | En la asistencia del paciente a un establecimiento... |
| Q11 | varchar |  |  | SI | Apellido Paterno |
| Q110 | bit |  |  | SI | En el diagnóstico de su TBC en el establecimiento |
| Q111 | bit |  |  | SI | En la iniciativa del tratamiento |
| Q112 | bit |  |  | SI | No hay evidencias  de demoras |
| Q113 | varchar |  |  | SI | La atención en salud antes de la muerte, fue adecu... |
| Q114 | bit |  |  | SI | Por falta de atención médica |
| Q115 | bit |  |  | SI | Falla Médica |
| Q116 | bit |  |  | SI | falla de recursos  |
| Q117 | bit |  |  | SI | Por inaccesiblidad geográfica |
| Q118 | bit |  |  | SI | Inaccesiblidad económica |
| Q119 | bit |  |  | SI | Otras causas de atención inadecuada |
| Q12 | varchar |  |  | SI | Apellido Materno |
| Q120 | varchar |  |  | SI | Otras |
| Q121 | date |  |  | SI | Fecha de Fallecimiento |
| Q122 | varchar |  |  | SI | Falleció en |
| Q123 | bit |  |  | SI | Servicio de Urgencia |
| Q124 | bit |  |  | SI | Domicilio |
| Q125 | bit |  |  | SI | Consultorio |
| Q126 | bit |  |  | SI | Otros |
| Q127 | varchar |  |  | SI | Otro centro  |
| Q128 | bit |  |  | SI | Desconocido |
| Q129 | varchar |  |  | SI | Causa de la muerte |
| Q13 | varchar |  |  | SI | Edad |
| Q130 | varchar |  |  | SI | Causa Inmediata |
| Q131 | varchar |  |  | SI | Causas originarias |
| Q132 | varchar |  |  | SI | Estados morbosos concomitantes |
| Q133 | varchar |  |  | SI | Fundamentos del diagnóstico de la causa de muerte |
| Q134 | varchar |  |  | SI | Fundamentos Autopsia |
| Q135 | varchar |  |  | SI | Fundamentos Biopsia |
| Q136 | bit |  |  | SI | Bacteriológica |
| Q137 | bit |  |  | SI | D |
| Q138 | bit |  |  | SI | Sólo C |
| Q139 | bit |  |  | SI | Bacteriológica negativa |
| Q14 | varchar |  |  | SI | Fecha de Nacimiento |
| Q140 | bit |  |  | SI | Desconocida |
| Q141 | bit |  |  | SI | Laboratorio |
| Q142 | bit |  |  | SI | ADA(+) |
| Q143 | bit |  |  | SI | Otros (+) |
| Q144 | varchar |  |  | SI | Otros fundamentos |
| Q145 | varchar |  |  | SI | Solamente Clínica |
| Q146 | varchar |  |  | SI | Atención médica última enfermedad |
| Q147 | varchar |  |  | SI | Calidad de quien certifica la muerte |
| Q148 | varchar |  |  | SI | Se efectuó la notificación de TBC |
| Q149 | varchar |  |  | SI | ¿Estaba inscrito en su Consultorio? |
| Q15 | varchar |  |  | SI | Sexo |
| Q150 | varchar |  |  | SI | ¿Había consultado en alguna oportunidad antes del ... |
| Q151 | varchar |  |  | SI | ¿Estaba siendo controlado en algún Programa de Cró... |
| Q152 | varchar |  |  | SI | Cual programa crónico |
| Q153 | date |  |  | SI | ¿En que fecha fué la última consulta en su Centro ... |
| Q154 | bit |  |  | SI | Fecha desconocida última consulta en su Centro de ... |
| Q155 | varchar |  |  | SI | ¿Se le pidió BK en la consulta a su Centro de Salu... |
| Q156 | date |  |  | SI | ¿En que fecha fue pedida la última BK, antes del d... |
| Q157 | bit |  |  | SI | Se desconoce fecha de petición |
| Q158 | varchar |  |  | SI | ¿Como resultó el estudio de contacto en niños y ad... |
| Q159 | varchar |  |  | SI | Comentarios DR. |
| Q16 | varchar |  |  | SI | Previsión |
| Q160 | varchar |  |  | SI | Usted concluye que falleció de |
| Q161 | varchar |  |  | SI | Nombre del Médico Auditor Dr.(a) |
| Q162 | date |  |  | SI | Fecha Auditoria |
| Q163 | varchar |  |  | SI | Confirmación del diagnóstico de la localización pr... |
| Q164 | varchar |  |  | SI | Calificación al momento  del diagnóstico |
| Q165 | varchar |  |  | SI | Otros antecedentes |
| Q166 | varchar |  |  | SI | Tipo reacción |
| Q167 | varchar |  |  | SI | Historia del episodio |
| Q168 | varchar |  |  | SI | si la respuesta es no |
| Q169 | varchar |  |  | SI | Falleció en |
| Q17 | varchar |  |  | SI | Nacionalidad |
| Q170 | varchar |  |  | SI | Fundamentos del diagnóstico (+) |
| Q18 | varchar |  |  | SI | RUT |
| Q19 | varchar |  |  | SI | Factores de riesgo para tuberculosis (TBC) |
| Q20 | varchar |  |  | SI | Diagnóstico  TBC. Localización Principal |
| Q21 | varchar |  |  | SI | Organo |
| Q22 | varchar |  |  | SI | 2° Localización de TBC |
| Q23 | date |  |  | SI | Fecha de diagnóstico |
| Q24 | date |  |  | SI | Fecha de Notificación |
| Q25 | varchar |  |  | SI | Lugar de Notificación |
| Q26 | bit |  |  | SI | Baciloscopía (BK) D+ |
| Q27 | bit |  |  | SI | Baciloscopía C+ |
| Q28 | numeric |  |  | SI | N° colonias |
| Q29 | bit |  |  | SI | Biopsia |
| Q30 | bit |  |  | SI | Sin Confirmación (sc) |
| Q31 | numeric |  |  | SI | ADA (+) |
| Q32 | varchar |  |  | SI | Fundamento y diagnóstico de la 2°&nbsp; Localizaci... |
| Q33 | bit |  |  | SI | Caso Nuevo |
| Q34 | bit |  |  | SI | Recaída |
| Q35 | bit |  |  | SI | Abandono Recuperado |
| Q36 | date |  |  | SI | En caso de ser AT,  Fecha de la 1° TBC |
| Q37 | bit |  |  | SI | Fracaso de tratamiendo anterior (cpn BKD+ >= 4° me... |
| Q38 | bit |  |  | SI | Crónico |
| Q39 | bit |  |  | SI | TBC desconocida previo a la muerte |
| Q40 | numeric |  |  | SI | N° Cicatrices de BCG |
| Q41 | numeric |  |  | SI | Dosis Diarias (DD): N° 1 |
| Q42 | numeric |  |  | SI | Dosis Diarias (DD): N° 2 |
| Q43 | numeric |  |  | SI | Dosis Diarias (DD): N° 3 |
| Q44 | numeric |  |  | SI | Dosis Diarias (DD): N° 4 |
| Q45 | numeric |  |  | SI | Dosis Diarias (DD): N° 5 |
| Q46 | numeric |  |  | SI | Dosis Bisemanal (DB): N° 1 |
| Q47 | numeric |  |  | SI | Dosis Bisemanal (DB): N° 2 |
| Q48 | numeric |  |  | SI | Dosis Bisemanal (DB): N° 3 |
| Q49 | numeric |  |  | SI | Dosis Bisemanal (DB): N° 4 |
| Q50 | numeric |  |  | SI | Dosis Bisemanal (DB): N° 5 |
| Q51 | numeric |  |  | SI | BK (D) 1° mes |
| Q52 | numeric |  |  | SI | BK (D) 2° mes |
| Q53 | numeric |  |  | SI | BK (D) 3° mes |
| Q54 | numeric |  |  | SI | BK (D) 4° Mes |
| Q55 | numeric |  |  | SI | BK (D) 5° mes |
| Q56 | numeric |  |  | SI | BK (D) 6° mes |
| Q57 | numeric |  |  | SI | BK (D) 7° mes |
| Q58 | numeric |  |  | SI | BK (D) 8° mes |
| Q59 | numeric |  |  | SI | BK (D) 9° mes |
| Q60 | numeric |  |  | SI | BK (C) 1° mes |
| Q61 | numeric |  |  | SI | BK (C) 2° mes |
| Q62 | numeric |  |  | SI | BK (C) 3° mes |
| Q63 | numeric |  |  | SI | BK (C) 4° mes |
| Q64 | numeric |  |  | SI | BK (C) 5° mes |
| Q65 | numeric |  |  | SI | BK (C) 6° mes |
| Q66 | numeric |  |  | SI | BK (C) 7° mes |
| Q67 | numeric |  |  | SI | BK (C) 8° mes |
| Q68 | numeric |  |  | SI | BK (C) 9° mes |
| Q69 | numeric |  |  | SI | Dosis recibida 1° mes |
| Q70 | numeric |  |  | SI | dosis recibida 2° mes |
| Q71 | numeric |  |  | SI | Dosis recibida 3° mes |
| Q72 | numeric |  |  | SI | dosis recibida 4° mes |
| Q73 | numeric |  |  | SI | dosis recibida 5° mes |
| Q74 | numeric |  |  | SI | dosis recibida 6° mes |
| Q75 | numeric |  |  | SI | dosis recibida 7° mes |
| Q76 | numeric |  |  | SI | Dosis recibida 8° mes |
| Q77 | numeric |  |  | SI | dosis recibida 9° mes |
| Q78 | varchar |  |  | SI | RX 1° mes |
| Q79 | varchar |  |  | SI | RX 2° mes |
| Q80 | varchar |  |  | SI | RX 3° mes |
| Q81 | varchar |  |  | SI | RX 4° mes |
| Q82 | varchar |  |  | SI | RX 5° mes |
| Q83 | varchar |  |  | SI | RX 6° mes  |
| Q84 | varchar |  |  | SI | RX 7° mes |
| Q85 | varchar |  |  | SI | RX 8° mes |
| Q86 | varchar |  |  | SI | RX 9° mes |
| Q87 | numeric |  |  | SI | Peso (Kg) 1° mes |
| Q88 | numeric |  |  | SI | Peso (kg) 2° mes |
| Q89 | numeric |  |  | SI | Peso (Kg) 3° mes |
| Q90 | numeric |  |  | SI | Peso (Kg) 4° mes |
| Q91 | numeric |  |  | SI | Peso (Kg) 5° mes |
| Q92 | numeric |  |  | SI | Peso (Kg) 6° mes |
| Q93 | numeric |  |  | SI | Peso (Kg) 7° mes |
| Q94 | numeric |  |  | SI | Peso (Kg) 8° mes |
| Q95 | numeric |  |  | SI | Peso (Kg) 9° mes |
| Q96 | varchar |  |  | SI | VIH realizado |
| Q97 | varchar |  |  | SI | Resultado VIH |
| Q97ObsDR | varchar |  | FK | SI | Resultado VIH DR |
| Q98 | varchar |  |  | SI | Reacciones Adversas a medicamentos |
| Q99 | bit |  |  | SI | Hepática |
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