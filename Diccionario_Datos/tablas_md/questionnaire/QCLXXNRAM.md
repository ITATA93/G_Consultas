# questionnaire.QCLXXNRAM

> Notificación de Sospecha de Reacción Adversa a Medicamentos

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Notificación de Sospecha de Reacción Adversa a Medicamentos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Iniciales del Paciente  |
| Q02 | varchar |  |  | SI | N° de Ficha  |
| Q03 | varchar |  |  | SI | Unidad / Servicio  |
| Q04 | varchar |  |  | SI | Sexo  |
| Q05 | varchar |  |  | SI | Edad |
| Q06 | varchar |  |  | SI | Mes(s) |
| Q07 | varchar |  |  | SI | Talla |
| Q07ObsDR | varchar |  | FK | SI | Talla DR |
| Q08 | varchar |  |  | SI | Declara pueblo originario |
| Q09 | date |  |  | SI | FECHA INICIO RAM * |
| Q10 | numeric |  |  | SI | Duración de la RAM |
| Q11 | varchar |  |  | SI | duración de la ram |
| Q12 | varchar |  |  | SI | DESCRIPCIÓN DE LA REACCIÓN ADVERSA |
| Q13 | varchar |  |  | SI | Recibió Fármaco Concominante |
| Q15 | varchar |  |  | SI | Paciente recibió tratamiento de RAM (incluyendo su... |
| Q16 | varchar |  |  | SI | Describa |
| Q17 | varchar |  |  | SI | RESULTADO DE LA RAM |
| Q18 | date |  |  | SI | Fecha de Muerte  |
| Q19 | varchar |  |  | SI | Causa de muerte  |
| Q20 | varchar |  |  | SI | ¿Se suspendió el fármaco sospechoso luego de la ap... |
| Q21 | varchar |  |  | SI | ¿Tras disminuir o suspender el fármaco sospechoso ... |
| Q22 | varchar |  |  | SI | ¿Se readministró el fármaco sospechoso luego de su... |
| Q23 | varchar |  |  | SI | ¿Reapareció o se intensificó la RAM luego de la re... |
| Q24 | varchar |  |  | SI | Requirió Hospitalización |
| Q25 | varchar |  |  | SI | Prolongó Hospitalización |
| Q26 | numeric |  |  | SI | Señale días |
| Q27 | varchar |  |  | SI | Secuelas |
| Q28 | varchar |  |  | SI | Describa secuelas |
| Q29 | varchar |  |  | SI | Comentarios |
| Q30 | varchar |  |  | SI | Informado por |
| Q31 | varchar |  |  | SI | (Señalar)  |
| Q32 | varchar |  |  | SI | Nombre |
| Q33 | varchar |  |  | SI | Establecimiento (donde se detecta la RAM) |
| Q34 | date |  |  | SI | Fecha del Reportre |
| Q35 | varchar |  |  | SI | Dirección  |
| Q36 | varchar |  |  | SI | Teléfono  |
| Q37 | varchar |  |  | SI | E-Mail  |
| Q38 | varchar |  |  | SI | Ciudad |
| Q39 | varchar |  |  | SI | reporte inicial seguimiento |
| Q40 | varchar |  |  | SI | Peso |
| Q40ObsDR | varchar |  | FK | SI | Peso DR |
| Q41 | varchar |  |  | SI | Otro pueblo originario declarado |
| Q43 | varchar |  |  | SI | N° Episodio |
| Q44 | varchar |  |  | SI | Día(s) |
| Q45 | varchar |  |  | SI | Fecha de Nacimiento |
| Q46 | varchar |  |  | SI | Codigo Pueblo Originario |
| Q47 | varchar |  |  | SI | Número Interno |
| Q48 | varchar |  |  | SI | Estado de Notificación |
| Q49 | varchar |  |  | SI | Estado de Notificación ISP |
| Q50 | date |  |  | SI | Fecha de Reporte |
| Q51 | date |  |  | SI | Fecha de Toma de conocimiento |
| Q52 | varchar |  |  | SI | Tipo de vigilancia |
| Q53 | varchar |  |  | SI | ¿Paciente está embarazada? |
| Q55 | varchar |  |  | SI | ¿Es prematuro? |
| Q56 | varchar |  |  | SI | Grupo Etario |
| Q58 | varchar |  |  | SI | ¿Médicamento bajo ciego ? |
| Q59 | varchar |  |  | SI | ¿La RAM puso en riesgo la vida del paciente? |
| Q60 | varchar |  |  | SI | ¿La RAM causó alteraciones congénitas? |
| Q61 | varchar |  |  | SI | Declara Pueblo Originario |
| Q62 | varchar |  |  | SI | Unidad / Servicio |
| Q63 | varchar |  |  | SI | Sexo |
| Q64 | varchar |  |  | SI | ¿Requirió Hospitalización debido a la RAM? |
| Q65 | varchar |  |  | SI | ¿Se prolongó la hospitalización debido a la RAM? |
| Q66 | varchar |  |  | SI | ¿La RAM puso en riesgo la vida del paciente? |
| Q67 | varchar |  |  | SI | ¿El paciente quedó con discapacidad permanente o p... |
| Q68 | varchar |  |  | SI | Describa |
| Q69 | varchar |  |  | SI | meses |
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