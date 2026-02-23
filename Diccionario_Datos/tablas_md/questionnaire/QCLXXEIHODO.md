# questionnaire.QCLXXEIHODO

> Evaluación Ingreso Hospitalización Domiciliaria

**Schema:** questionnaire
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Ingreso Hospitalización Domiciliaria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora de Evaluación |
| Q03 | varchar |  |  | SI | Nombres Paciente |
| Q04 | varchar |  |  | SI | Apellido Paterno |
| Q05 | varchar |  |  | SI | Apellido Materno |
| Q06 | varchar |  |  | SI | RUN |
| Q07 | varchar |  |  | SI | Edad |
| Q08 | varchar |  |  | SI | Habitación |
| Q09 | varchar |  |  | SI | Cama |
| Q10 | varchar |  |  | SI | Previsión |
| Q11 | varchar |  |  | SI | Plan |
| Q12 | varchar |  |  | SI | Dirección |
| Q13 | varchar |  |  | SI | Número |
| Q14 | varchar |  |  | SI | Teléfono Contacto |
| Q15 | varchar |  |  | SI | Número Celular |
| Q16 | varchar |  |  | SI | Telefono de Recado |
| Q17 | varchar |  |  | SI | Diagnóstico Principal |
| Q18 | varchar |  |  | SI | Diagnóstico Secundario |
| Q19 | varchar |  |  | SI | Tratamiento |
| Q20 | varchar |  |  | SI | Exámenes y Signos Vitales |
| Q20ObsDR | varchar |  | FK | SI | Exámenes y Signos Vitales DR |
| Q21 | varchar |  |  | SI | Motivo de Ingreso |
| Q22 | numeric |  |  | SI | Número de Días |
| Q23 | varchar |  |  | SI | Horario |
| Q24 | varchar |  |  | SI | Horario 2 |
| Q25 | numeric |  |  | SI | Total Días |
| Q26 | varchar |  |  | SI | Medicamento |
| Q27 | varchar |  |  | SI | Estado General del Paciente |
| Q28 | varchar |  |  | SI | Conciente |
| Q29 | varchar |  |  | SI | Lucida |
| Q30 | varchar |  |  | SI | Postrado |
| Q31 | varchar |  |  | SI | Orientado |
| Q32 | varchar |  |  | SI | Alimentación |
| Q33 | varchar |  |  | SI | UPP |
| Q34 | varchar |  |  | SI | Grado |
| Q35 | varchar |  |  | SI | Frecuencia Curación |
| Q36 | varchar |  |  | SI | CUP |
| Q37 | date |  |  | SI | Fecha INS |
| Q38 | numeric |  |  | SI | Número de Días |
| Q39 | varchar |  |  | SI | Gastrostomía |
| Q40 | date |  |  | SI | Fecha Inst. |
| Q41 | numeric |  |  | SI | N° Días |
| Q42 | varchar |  |  | SI | Tratamiento |
| Q43 | date |  |  | SI | Fecha Ins |
| Q44 | numeric |  |  | SI | N° de Días |
| Q45 | varchar |  |  | SI | Uso de O2 |
| Q46 | varchar |  |  | SI | Nec.Aspir. |
| Q47 | varchar |  |  | SI | Existe Cuidador |
| Q48 | varchar |  |  | SI | Tratamiento EV fin de semana |
| Q49 | varchar |  |  | SI | Reg.Sup Int. |
| Q50 | varchar |  |  | SI | Tramite Ortesis |
| Q51 | date |  |  | SI | Fecha |
| Q52 | varchar |  |  | SI | Pendiente |
| Q53 | date |  |  | SI | Fecha Tramitación |
| Q54 | varchar |  |  | SI | Entrevista con Cuidador |
| Q55 | varchar |  |  | SI | Medicamentos |
| Q56 | varchar |  |  | SI | Descripción de Medicamentos |
| Q57 | varchar |  |  | SI | Consultorio |
| Q58 | varchar |  |  | SI | PCR |
| Q58ObsDR | varchar |  | FK | SI | PCR DR |
| Q59 | varchar |  |  | SI | Creatinina |
| Q59ObsDR | varchar |  | FK | SI | Creatinina DR |
| Q60 | varchar |  |  | SI | Gl |
| Q60ObsDR | varchar |  | FK | SI | Gl DR |
| Q61 | varchar |  |  | SI | Hemogluco Test |
| Q61ObsDR | varchar |  | FK | SI | Hemogluco Test DR |
| Q62 | varchar |  |  | SI | Urocultivo |
| Q62ObsDR | varchar |  | FK | SI | Urocultivo DR |
| Q63 | date |  |  | SI | Fecha Examenes |
| Q64 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q64ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q65 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q65ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q66 | varchar |  |  | SI | Temperatura Axilar |
| Q66ObsDR | varchar |  | FK | SI | Temperatura Axilar DR |
| Q67 | varchar |  |  | SI | Temperatura Rectal |
| Q67ObsDR | varchar |  | FK | SI | Temperatura Rectal DR |
| Q68 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q68ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q69 | varchar |  |  | SI | Saturación O2 |
| Q69ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q70 | varchar |  |  | SI | Resultado de Examenes |
| Q71 | varchar |  |  | SI | Signos Vitales |
| Q72 | date |  |  | SI | Fecha Signos Vitales |
| Q73 | varchar |  |  | SI | Trat.EV detalle |
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