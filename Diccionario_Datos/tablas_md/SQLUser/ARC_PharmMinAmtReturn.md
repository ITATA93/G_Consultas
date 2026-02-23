# SQLUser.ARC_PharmMinAmtReturn

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PMAR_RowId | bigint | PK |  | NO | - |
| PMAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PMAR_CreatedDate | date |  |  | SI | Created Date |
| PMAR_CreatedTime | time |  |  | SI | Created Time |
| PMAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PMAR_DateFrom | date |  |  | SI | DateFrom |
| PMAR_DateTo | date |  |  | SI | DateTo |
| PMAR_HandlingFee | double |  |  | SI | HandlingFee |
| PMAR_MinAmtReturnable | double |  |  | SI | MinAmtReturnable |
| PMAR_Owner | varchar |  |  | SI | Owner |
| PMAR_UpdatedDate | date |  |  | SI | Updated Date |
| PMAR_UpdatedTime | time |  |  | SI | Updated Time |
| PMAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora de Evaluación |
| Q03 | - |  |  | SI | Nombres Paciente |
| Q04 | - |  |  | SI | Apellido Paterno |
| Q05 | - |  |  | SI | Apellido Materno |
| Q06 | - |  |  | SI | RUN |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Habitación |
| Q09 | - |  |  | SI | Cama |
| Q10 | - |  |  | SI | Previsión |
| Q11 | - |  |  | SI | Plan |
| Q12 | - |  |  | SI | Dirección |
| Q13 | - |  |  | SI | Número |
| Q14 | - |  |  | SI | Teléfono Contacto |
| Q15 | - |  |  | SI | Número Celular |
| Q16 | - |  |  | SI | Telefono de Recado |
| Q17 | - |  |  | SI | Diagnóstico Principal |
| Q18 | - |  |  | SI | Diagnóstico Secundario |
| Q19 | - |  |  | SI | Tratamiento |
| Q20 | - |  |  | SI | Exámenes y Signos Vitales |
| Q20ObsDR | - |  |  | SI | Exámenes y Signos Vitales DR |
| Q21 | - |  |  | SI | Motivo de Ingreso |
| Q22 | - |  |  | SI | Número de Días |
| Q23 | - |  |  | SI | Horario |
| Q24 | - |  |  | SI | Horario 2 |
| Q25 | - |  |  | SI | Total Días |
| Q26 | - |  |  | SI | Medicamento |
| Q27 | - |  |  | SI | Estado General del Paciente |
| Q28 | - |  |  | SI | Conciente |
| Q29 | - |  |  | SI | Lucida |
| Q30 | - |  |  | SI | Postrado |
| Q31 | - |  |  | SI | Orientado |
| Q32 | - |  |  | SI | Alimentación |
| Q33 | - |  |  | SI | UPP |
| Q34 | - |  |  | SI | Grado |
| Q35 | - |  |  | SI | Frecuencia Curación |
| Q36 | - |  |  | SI | CUP |
| Q37 | - |  |  | SI | Fecha INS |
| Q38 | - |  |  | SI | Número de Días |
| Q39 | - |  |  | SI | Gastrostomía |
| Q40 | - |  |  | SI | Fecha Inst. |
| Q41 | - |  |  | SI | N° Días |
| Q42 | - |  |  | SI | Tratamiento |
| Q43 | - |  |  | SI | Fecha Ins |
| Q44 | - |  |  | SI | N° de Días |
| Q45 | - |  |  | SI | Uso de O2 |
| Q46 | - |  |  | SI | Nec.Aspir. |
| Q47 | - |  |  | SI | Existe Cuidador |
| Q48 | - |  |  | SI | Tratamiento EV fin de semana |
| Q49 | - |  |  | SI | Reg.Sup Int. |
| Q50 | - |  |  | SI | Tramite Ortesis |
| Q51 | - |  |  | SI | Fecha |
| Q52 | - |  |  | SI | Pendiente |
| Q53 | - |  |  | SI | Fecha Tramitación |
| Q54 | - |  |  | SI | Entrevista con Cuidador |
| Q55 | - |  |  | SI | Medicamentos |
| Q56 | - |  |  | SI | Descripción de Medicamentos |
| Q57 | - |  |  | SI | Consultorio |
| Q58 | - |  |  | SI | PCR |
| Q58ObsDR | - |  |  | SI | PCR DR |
| Q59 | - |  |  | SI | Creatinina |
| Q59ObsDR | - |  |  | SI | Creatinina DR |
| Q60 | - |  |  | SI | Gl |
| Q60ObsDR | - |  |  | SI | Gl DR |
| Q61 | - |  |  | SI | Hemogluco Test |
| Q61ObsDR | - |  |  | SI | Hemogluco Test DR |
| Q62 | - |  |  | SI | Urocultivo |
| Q62ObsDR | - |  |  | SI | Urocultivo DR |
| Q63 | - |  |  | SI | Fecha Examenes |
| Q64 | - |  |  | SI | Presión Arterial Sistólica |
| Q64ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q65 | - |  |  | SI | Presión Arterial Diastólica |
| Q65ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q66 | - |  |  | SI | Temperatura Axilar |
| Q66ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q67 | - |  |  | SI | Temperatura Rectal |
| Q67ObsDR | - |  |  | SI | Temperatura Rectal DR |
| Q68 | - |  |  | SI | Frecuencia Cardiaca |
| Q68ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q69 | - |  |  | SI | Saturación O2 |
| Q69ObsDR | - |  |  | SI | Saturación O2 DR |
| Q70 | - |  |  | SI | Resultado de Examenes |
| Q71 | - |  |  | SI | Signos Vitales |
| Q72 | - |  |  | SI | Fecha Signos Vitales |
| Q73 | - |  |  | SI | Trat.EV detalle |
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