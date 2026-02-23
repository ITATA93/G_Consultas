# SQLUser.AR_QuoteMisc

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MISC_ParRef | bigint | PK |  | NO | AR_Quote Parent Reference |
| ChildQ14DR | - |  |  | SI | Child Reference: Tabla Fármaco |
| MISC_Childsub | double |  |  | NO | Childsub |
| MISC_Description | varchar |  |  | SI | Description |
| MISC_GST | varchar |  |  | SI | GST |
| MISC_Qty | integer |  |  | SI | Quantity |
| MISC_RowId | varchar |  |  | NO | - |
| MISC_ServiceTax | bigint |  |  | SI | Service Tax |
| MISC_TotalCost | double |  |  | SI | Total Cost |
| MISC_Value | double |  |  | SI | Value |
| Q01 | - |  |  | SI | Iniciales del Paciente |
| Q02 | - |  |  | SI | N° de Ficha |
| Q03 | - |  |  | SI | Unidad / Servicio |
| Q04 | - |  |  | SI | Sexo |
| Q05 | - |  |  | SI | Edad |
| Q06 | - |  |  | SI | Mes(s) |
| Q07 | - |  |  | SI | Talla |
| Q07ObsDR | - |  |  | SI | Talla DR |
| Q08 | - |  |  | SI | Declara pueblo originario |
| Q09 | - |  |  | SI | FECHA INICIO RAM * |
| Q10 | - |  |  | SI | Duración de la RAM |
| Q11 | - |  |  | SI | duración de la ram |
| Q12 | - |  |  | SI | DESCRIPCIÓN DE LA REACCIÓN ADVERSA |
| Q13 | - |  |  | SI | Recibió Fármaco Concominante |
| Q15 | - |  |  | SI | Paciente recibió tratamiento de RAM (incluyendo su... |
| Q16 | - |  |  | SI | Describa |
| Q17 | - |  |  | SI | RESULTADO DE LA RAM |
| Q18 | - |  |  | SI | Fecha de Muerte |
| Q19 | - |  |  | SI | Causa de muerte |
| Q20 | - |  |  | SI | ¿Se suspendió el fármaco sospechoso luego de la ap... |
| Q21 | - |  |  | SI | ¿Tras disminuir o suspender el fármaco sospechoso ... |
| Q22 | - |  |  | SI | ¿Se readministró el fármaco sospechoso luego de su... |
| Q23 | - |  |  | SI | ¿Reapareció o se intensificó la RAM luego de la re... |
| Q24 | - |  |  | SI | Requirió Hospitalización |
| Q25 | - |  |  | SI | Prolongó Hospitalización |
| Q26 | - |  |  | SI | Señale días |
| Q27 | - |  |  | SI | Secuelas |
| Q28 | - |  |  | SI | Describa secuelas |
| Q29 | - |  |  | SI | Comentarios |
| Q30 | - |  |  | SI | Informado por |
| Q31 | - |  |  | SI | (Señalar) |
| Q32 | - |  |  | SI | Nombre |
| Q33 | - |  |  | SI | Establecimiento (donde se detecta la RAM) |
| Q34 | - |  |  | SI | Fecha del Reportre |
| Q35 | - |  |  | SI | Dirección |
| Q36 | - |  |  | SI | Teléfono |
| Q37 | - |  |  | SI | E-Mail |
| Q38 | - |  |  | SI | Ciudad |
| Q39 | - |  |  | SI | reporte inicial seguimiento |
| Q40 | - |  |  | SI | Peso |
| Q40ObsDR | - |  |  | SI | Peso DR |
| Q41 | - |  |  | SI | Otro pueblo originario declarado |
| Q43 | - |  |  | SI | N° Episodio |
| Q44 | - |  |  | SI | Día(s) |
| Q45 | - |  |  | SI | Fecha de Nacimiento |
| Q46 | - |  |  | SI | Codigo Pueblo Originario |
| Q47 | - |  |  | SI | Número Interno |
| Q48 | - |  |  | SI | Estado de Notificación |
| Q49 | - |  |  | SI | Estado de Notificación ISP |
| Q50 | - |  |  | SI | Fecha de Reporte |
| Q51 | - |  |  | SI | Fecha de Toma de conocimiento |
| Q52 | - |  |  | SI | Tipo de vigilancia |
| Q53 | - |  |  | SI | ¿Paciente está embarazada? |
| Q55 | - |  |  | SI | ¿Es prematuro? |
| Q56 | - |  |  | SI | Grupo Etario |
| Q58 | - |  |  | SI | ¿Médicamento bajo ciego ? |
| Q59 | - |  |  | SI | ¿La RAM puso en riesgo la vida del paciente? |
| Q60 | - |  |  | SI | ¿La RAM causó alteraciones congénitas? |
| Q61 | - |  |  | SI | Declara Pueblo Originario |
| Q62 | - |  |  | SI | Unidad / Servicio |
| Q63 | - |  |  | SI | Sexo |
| Q64 | - |  |  | SI | ¿Requirió Hospitalización debido a la RAM? |
| Q65 | - |  |  | SI | ¿Se prolongó la hospitalización debido a la RAM? |
| Q66 | - |  |  | SI | ¿La RAM puso en riesgo la vida del paciente? |
| Q67 | - |  |  | SI | ¿El paciente quedó con discapacidad permanente o p... |
| Q68 | - |  |  | SI | Describa |
| Q69 | - |  |  | SI | meses |
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