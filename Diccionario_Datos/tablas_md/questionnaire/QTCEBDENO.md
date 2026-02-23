# questionnaire.QTCEBDENO

> Boletín Declaración Enfermedades de Notificación Obligatoria (ENO)

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Boletín Declaración Enfermedades de Notificación Obligatoria (ENO)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ008 | varchar |  |  | SI | - |
| CQ009 | varchar |  |  | SI | - |
| CQ015 | varchar |  |  | SI | - |
| CQ11 | varchar |  |  | SI | - |
| CQ13 | varchar |  |  | SI | - |
| CQ21 | varchar |  |  | SI | - |
| CQ22 | varchar |  |  | SI | - |
| CQ23 | varchar |  |  | SI | - |
| CQ25 | varchar |  |  | SI | - |
| CQ26 | varchar |  |  | SI | - |
| Q001 | varchar |  |  | SI | Seremi |
| Q002 | varchar |  |  | SI | Código Seremi |
| Q003 | varchar |  |  | SI | Oficina Provincial |
| Q004 | varchar |  |  | SI | Código Oficina Provincial |
| Q005 | date |  |  | SI | Fecha de última dosis |
| Q006 | numeric |  |  | SI | Número Dosis |
| Q007 | varchar |  |  | SI | COMPLETAR SOLO SI LA DECLARACIÓN CORRESPONDE A TBC... |
| Q008 | varchar |  |  | SI | Indicar si corresponde a: |
| Q009 | varchar |  |  | SI | S |
| Q010 | varchar |  |  | SI | DATOS DEL PROFESIONAL QUE NOTIFICA |
| Q011 | varchar |  |  | SI | Correo Electrónico |
| Q012 | date |  |  | SI | Fecha de Notificación en el establecimiento |
| Q013 | date |  |  | SI | Fecha de notificación desde la seremi al minsal |
| Q015 | varchar |  |  | SI | Condición de Actividad |
| Q016 | varchar |  |  | SI | Código Ocupación |
| Q017 | varchar |  |  | SI | Ocupación |
| Q018 | varchar |  |  | SI | Otro Diagnóstico Confirmado |
| Q050 | varchar |  |  | SI | Categoría Ocupacional |
| Q1 | varchar |  |  | SI | Servicio de Salud |
| Q10 | date |  |  | SI | Fecha de Nacimiento |
| Q11 | varchar |  |  | SI | Embarazo |
| Q12 | varchar |  |  | SI | Semanas de Gestación |
| Q13 | varchar |  |  | SI | Sexo |
| Q14 | varchar |  |  | SI | Dirección |
| Q15 | varchar |  |  | SI | Comuna de Residencia |
| Q16 | varchar |  |  | SI | Código Comuna |
| Q16a | varchar |  |  | SI | Código Postal |
| Q17 | numeric |  |  | SI | Teléfono |
| Q18 | varchar |  |  | SI | Diagnóstico |
| Q19 | varchar |  |  | SI | Código CIE |
| Q2 | varchar |  |  | SI | Código Servicio de Salud |
| Q20 | date |  |  | SI | Fecha Primeros Síntomas (o primera consulta) |
| Q21 | varchar |  |  | SI | Confirmación Diagnóstica |
| Q22 | varchar |  |  | SI | Antec. Vacunación |
| Q23 | varchar |  |  | SI | País de contagio |
| Q24 | varchar |  |  | SI | País |
| Q25 | varchar |  |  | SI | I |
| Q26 | varchar |  |  | SI | Sólo para recaídas  |
| Q27 | varchar |  |  | SI | Nombre Profesional |
| Q28 | varchar |  |  | SI | Teléfono Profesional |
| Q29 | date |  |  | SI | Fecha de Notificación |
| Q3 | varchar |  |  | SI | Establecimiento |
| Q4 | varchar |  |  | SI | N° Establecimiento |
| Q47 | varchar |  |  | SI | Confirmación Diagnóstica |
| Q48 | varchar |  |  | SI | Nombre Establecimiento |
| Q5 | varchar |  |  | SI | Ficha Clinica |
| Q50 | varchar |  |  | SI | N° Historia Clínica |
| Q51 | varchar |  |  | SI | Diagnóstico Confirmado |
| Q54 | varchar |  |  | SI | Código VIH-SIDA |
| Q55 | varchar |  |  | SI | Datos de Identificación del Paciente: |
| Q56 | varchar |  |  | SI | Datos Clínicos: |
| Q57 | varchar |  |  | SI | Completar sólo si la declaración corresponde a TBC |
| Q58 | varchar |  |  | SI | Datos del Profesional que Notifica: |
| Q59 | varchar |  |  | SI | Fecha de Notificación: |
| Q6 | varchar |  |  | SI | R.U.T. |
| Q7 | varchar |  |  | SI | Apellido Paterno |
| Q8 | varchar |  |  | SI | Apellido Materno |
| Q9 | varchar |  |  | SI | Nombres |
| QIdDia | varchar |  |  | SI | Id Diagnóstico |
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