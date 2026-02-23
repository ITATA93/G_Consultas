# SQLUser.MRC_HDRActionGroup

**Schema:** SQLUser
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HDRAGRP_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Características del dolor |
| HDRAGRP_Code | varchar |  |  | SI | Code |
| HDRAGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HDRAGRP_CreatedDate | date |  |  | SI | Created Date |
| HDRAGRP_CreatedTime | time |  |  | SI | Created Time |
| HDRAGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HDRAGRP_DateFrom | date |  |  | SI | DateFrom |
| HDRAGRP_DateTo | date |  |  | SI | DateTo |
| HDRAGRP_Desc | varchar |  |  | SI | Description |
| HDRAGRP_Owner | varchar |  |  | SI | Owner |
| HDRAGRP_UpdatedDate | date |  |  | SI | Updated Date |
| HDRAGRP_UpdatedTime | time |  |  | SI | Updated Time |
| HDRAGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | N° Biopsia |
| Q03 | - |  |  | SI | Performance Status |
| Q04 | - |  |  | SI | Peso |
| Q04ObsDR | - |  |  | SI | Peso DR |
| Q05 | - |  |  | SI | Frecuencias Cardíaca |
| Q05ObsDR | - |  |  | SI | Frecuencias Cardíaca DR |
| Q06 | - |  |  | SI | Presión Sistólica |
| Q06ObsDR | - |  |  | SI | Presión Sistólica DR |
| Q07 | - |  |  | SI | Presión Diastólica |
| Q07ObsDR | - |  |  | SI | Presión Diastólica DR |
| Q08 | - |  |  | SI | Frecuencia Respiratoria |
| Q08ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q09 | - |  |  | SI | Derivado desde |
| Q10 | - |  |  | SI | EVA |
| Q10ObsDR | - |  |  | SI | EVA DR |
| Q12 | - |  |  | SI | Irradiación del dolor |
| Q13 | - |  |  | SI | Frecuencia en 24 horas |
| Q14 | - |  |  | SI | Duración en horas |
| Q15 | - |  |  | SI | El dolor impide la actividad diaria |
| Q16 | - |  |  | SI | El dolor impide el reposo |
| Q17 | - |  |  | SI | El dolor impide el sueño |
| Q18 | - |  |  | SI | El dolor cambia su humor |
| Q19 | - |  |  | SI | El dolor altera su relación familiar |
| Q20 | - |  |  | SI | El dolor altera su relación con los demas |
| Q21 | - |  |  | SI | Factores que aumentan su dolor |
| Q22 | - |  |  | SI | ¿Ha recibido tratamiento para el dolor? |
| Q23 | - |  |  | SI | ¿Cuál? ¿En qué dosis? |
| Q24 | - |  |  | SI | Tipo de síntomas y EVA |
| Q25 | - |  |  | SI | Observaciones |
| Q26 | - |  |  | SI | ¿Cuál es su mayor preocupación? |
| Q27 | - |  |  | SI | ¿Cómo cree usted que podemos ayudarle? |
| Q28 | - |  |  | SI | ¿Cuál es su mayor molestia? |
| Q29 | - |  |  | SI | ¿Cómo siente la atención recibida? |
| Q30 | - |  |  | SI | Atención Clínica |
| Q31 | - |  |  | SI | Tratamiento e Indicaciones |
| Q32 | - |  |  | SI | Asiste a consulta |
| Q33 | - |  |  | SI | Nombre del Profesional |
| Q34 | - |  |  | SI | Nivel de Atención Primaria |
| Q35 | - |  |  | SI | Nivel de Atención Secundaria |
| Q36 | - |  |  | SI | Nivel de Atención Terciaria |
| Q37 | - |  |  | SI | Condición Clínica del Paciente |
| Q38 | - |  |  | SI | Enfermedad de Base |
| Q39 | - |  |  | SI | Metástasis |
| Q40 | - |  |  | SI | Localización |
| Q41 | - |  |  | SI | Tratamientos |
| Q42 | - |  |  | SI | Otros tratamiento |
| Q43 | - |  |  | SI | Saturación |
| Q43ObsDR | - |  |  | SI | Saturación DR |
| Q44 | - |  |  | SI | Piel |
| Q44ObsDR | - |  |  | SI | Piel DR |
| Q45 | - |  |  | SI | Boca |
| Q46 | - |  |  | SI | Cabeza y Cuello |
| Q46ObsDR | - |  |  | SI | Cabeza y Cuello DR |
| Q47 | - |  |  | SI | Cardiaco |
| Q47ObsDR | - |  |  | SI | Cardiaco DR |
| Q48 | - |  |  | SI | Pulmonar |
| Q48ObsDR | - |  |  | SI | Pulmonar DR |
| Q49 | - |  |  | SI | Tórax y Pared addominal |
| Q49ObsDR | - |  |  | SI | Tórax y Pared addominal DR |
| Q50 | - |  |  | SI | Abdomen |
| Q50ObsDR | - |  |  | SI | Abdomen DR |
| Q51 | - |  |  | SI | Extremidades Superiores |
| Q51ObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q52 | - |  |  | SI | Extremidades Inferiores |
| Q52ObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q53 | - |  |  | SI | Observacion Exámen Físico |
| Q54 | - |  |  | SI | Nivel de Atención Primaria, Paciente debe ingresar... |
| Q55 | - |  |  | SI | Nivel de Atención Secundaria, Paciente debe ingres... |
| Q56 | - |  |  | SI | Nivel de Atención Terciaria, Paciente debe ingresa... |
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