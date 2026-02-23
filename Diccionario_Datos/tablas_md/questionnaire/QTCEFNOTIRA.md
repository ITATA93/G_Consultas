# questionnaire.QTCEFNOTIRA

> Formulario Notificación Inmediata y Envío Muestras IRA Grave y Fallecidos Por Influenza

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario Notificación Inmediata y Envío Muestras IRA Grave y Fallecidos Por Influenza

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Trabajador avícola o granjas de cerdos |
| Q02 | varchar |  |  | SI | Personal de la salud |
| Q03 | numeric |  |  | SI | Semanas de gestación (semanas) |
| Q04 | numeric |  |  | SI | Semanas de gestación (días) |
| Q05 | varchar |  |  | SI | Embarazo |
| Q06 | date |  |  | SI | Fecha inicio síntomas |
| Q07 | date |  |  | SI | Fecha 1° Consulta |
| Q08 | varchar |  |  | SI | Fiebre (> o = 38.5°C) |
| Q09 | varchar |  |  | SI | Tos |
| Q10 | varchar |  |  | SI | Cefalea |
| Q11 | varchar |  |  | SI | Mialgias |
| Q12 | varchar |  |  | SI | Odinofagia |
| Q13 | varchar |  |  | SI | Rinorrea/congestión nasal |
| Q14 | varchar |  |  | SI | Neumonía |
| Q15 | varchar |  |  | SI | Hipoxemia |
| Q16 | varchar |  |  | SI | Deshidratación o rechazo alimentario |
| Q17 | varchar |  |  | SI | Dificultad respiratoria |
| Q18 | varchar |  |  | SI | Compromiso hemodinámico |
| Q19 | varchar |  |  | SI | Consulta repetida por deterioro clínico |
| Q20 | varchar |  |  | SI | Neumonía (A) |
| Q21 | varchar |  |  | SI | Taquipnea (A) |
| Q22 | varchar |  |  | SI | Hipotensión (A) |
| Q23 | varchar |  |  | SI | Disnea (A) |
| Q24 | varchar |  |  | SI | Cianosis (A) |
| Q25 | varchar |  |  | SI | Hipoxemia (A) |
| Q26 | varchar |  |  | SI | Consulta reptida por deterioro clínico (A) |
| Q27 | varchar |  |  | SI | Especifique (Enfermedad de base) |
| Q28 | varchar |  |  | SI | Enfermedad de base |
| Q29 | date |  |  | SI | Fecha hospitalización |
| Q30 | varchar |  |  | SI | Diagnóstico de Ingreso |
| Q31 | varchar |  |  | SI | Unidad Intermedia |
| Q32 | varchar |  |  | SI | UCI |
| Q33 | varchar |  |  | SI | VM |
| Q34 | varchar |  |  | SI | VAFO |
| Q35 | varchar |  |  | SI | ECMO |
| Q36 | date |  |  | SI | Fecha inicio (Uso antiviral) |
| Q37 | varchar |  |  | SI | Antiviral |
| Q38 | varchar |  |  | SI | Uso Antiviral |
| Q39 | varchar |  |  | SI | Nombre Hospital de Destino |
| Q40 | date |  |  | SI | Fecha de traslado |
| Q41 | varchar |  |  | SI | Traslado Hospitalario |
| Q42 | varchar |  |  | SI | Se Hospitaliza |
| Q43 | date |  |  | SI | Fecha fallecimiento |
| Q44 | varchar |  |  | SI | Diagnóstico fallecimiento |
| Q45 | varchar |  |  | SI | Fallece |
| Q46 | date |  |  | SI | Fecha vacunación |
| Q47 | varchar |  |  | SI | Vacuna contra influenza |
| Q48 | date |  |  | SI | Fecha obtención de la muestra |
| Q49 | date |  |  | SI | Fecha envío muestra |
| Q51 | varchar |  |  | SI | Tipo de muestra |
| Q52 | varchar |  |  | SI | Otro tipo de muestra |
| Q53 | varchar |  |  | SI | Establecimiento |
| Q54 | varchar |  |  | SI | Fono |
| Q55 | varchar |  |  | SI | Responsable de la notificación |
| Q56 | date |  |  | SI | Fecha de notificación |
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