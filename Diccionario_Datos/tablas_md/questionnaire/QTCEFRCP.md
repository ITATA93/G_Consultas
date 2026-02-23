# questionnaire.QTCEFRCP

> Ficha Registro Cuidados Paliativos y Alivio del Dolor

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Registro Cuidados Paliativos y Alivio del Dolor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | numeric |  |  | SI | N° Biopsia |
| Q03 | varchar |  |  | SI | Performance Status |
| Q04 | varchar |  |  | SI | Peso |
| Q04ObsDR | varchar |  | FK | SI | Peso DR |
| Q05 | varchar |  |  | SI | Frecuencias Cardíaca |
| Q05ObsDR | varchar |  | FK | SI | Frecuencias Cardíaca DR |
| Q06 | varchar |  |  | SI | Presión Sistólica |
| Q06ObsDR | varchar |  | FK | SI | Presión Sistólica DR |
| Q07 | varchar |  |  | SI | Presión Diastólica |
| Q07ObsDR | varchar |  | FK | SI | Presión Diastólica DR |
| Q08 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q08ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q09 | varchar |  |  | SI | Derivado desde |
| Q10 | varchar |  |  | SI | EVA |
| Q10ObsDR | varchar |  | FK | SI | EVA DR |
| Q12 | varchar |  |  | SI | Irradiación del dolor |
| Q13 | varchar |  |  | SI | Frecuencia en 24 horas |
| Q14 | varchar |  |  | SI | Duración en horas |
| Q15 | varchar |  |  | SI | El dolor impide la actividad diaria |
| Q16 | varchar |  |  | SI | El dolor impide el reposo |
| Q17 | varchar |  |  | SI | El dolor impide el sueño |
| Q18 | varchar |  |  | SI | El dolor cambia su humor |
| Q19 | varchar |  |  | SI | El dolor altera su relación familiar |
| Q20 | varchar |  |  | SI | El dolor altera su relación con los demas |
| Q21 | varchar |  |  | SI | Factores que aumentan su dolor |
| Q22 | varchar |  |  | SI | ¿Ha recibido tratamiento para el dolor? |
| Q23 | varchar |  |  | SI | ¿Cuál? ¿En qué dosis? |
| Q24 | varchar |  |  | SI | Tipo de síntomas y EVA |
| Q25 | varchar |  |  | SI | Observaciones |
| Q26 | varchar |  |  | SI | ¿Cuál es su mayor preocupación? |
| Q27 | varchar |  |  | SI | ¿Cómo cree usted que podemos ayudarle? |
| Q28 | varchar |  |  | SI | ¿Cuál es su mayor molestia? |
| Q29 | varchar |  |  | SI | ¿Cómo siente la atención recibida? |
| Q30 | varchar |  |  | SI | Atención Clínica |
| Q31 | varchar |  |  | SI | Tratamiento e Indicaciones |
| Q32 | varchar |  |  | SI | Asiste a consulta |
| Q33 | varchar |  |  | SI | Nombre del Profesional |
| Q34 | varchar |  |  | SI | Nivel de Atención Primaria |
| Q35 | varchar |  |  | SI | Nivel de Atención Secundaria |
| Q36 | varchar |  |  | SI | Nivel de Atención Terciaria |
| Q37 | varchar |  |  | SI | Condición Clínica del Paciente |
| Q38 | varchar |  |  | SI | Enfermedad de Base |
| Q39 | varchar |  |  | SI | Metástasis |
| Q40 | varchar |  |  | SI | Localización |
| Q41 | varchar |  |  | SI | Tratamientos |
| Q42 | varchar |  |  | SI | Otros tratamiento |
| Q43 | varchar |  |  | SI | Saturación |
| Q43ObsDR | varchar |  | FK | SI | Saturación DR |
| Q44 | varchar |  |  | SI | Piel |
| Q44ObsDR | varchar |  | FK | SI | Piel DR |
| Q45 | varchar |  |  | SI | Boca |
| Q46 | varchar |  |  | SI | Cabeza y Cuello |
| Q46ObsDR | varchar |  | FK | SI | Cabeza y Cuello DR |
| Q47 | varchar |  |  | SI | Cardiaco |
| Q47ObsDR | varchar |  | FK | SI | Cardiaco DR |
| Q48 | varchar |  |  | SI | Pulmonar |
| Q48ObsDR | varchar |  | FK | SI | Pulmonar DR |
| Q49 | varchar |  |  | SI | Tórax y Pared addominal |
| Q49ObsDR | varchar |  | FK | SI | Tórax y Pared addominal DR |
| Q50 | varchar |  |  | SI | Abdomen |
| Q50ObsDR | varchar |  | FK | SI | Abdomen DR |
| Q51 | varchar |  |  | SI | Extremidades Superiores |
| Q51ObsDR | varchar |  | FK | SI | Extremidades Superiores DR |
| Q52 | varchar |  |  | SI | Extremidades Inferiores |
| Q52ObsDR | varchar |  | FK | SI | Extremidades Inferiores DR |
| Q53 | varchar |  |  | SI | Observacion Exámen Físico |
| Q54 | varchar |  |  | SI | Nivel de Atención Primaria, Paciente debe ingresar... |
| Q55 | varchar |  |  | SI | Nivel de Atención Secundaria, Paciente debe ingres... |
| Q56 | varchar |  |  | SI | Nivel de Atención Terciaria, Paciente debe ingresa... |
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