# questionnaire.QCLXXSOLHD

> Solicitud de Ingreso a Hospitalización Domiciliaria

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Ingreso a Hospitalización Domiciliaria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre |
| Q02 | varchar |  |  | SI | Apellido Paterno |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | N° Ced. Identidad |
| Q05 | varchar |  |  | SI | Fecha de Nacimiento |
| Q06 | varchar |  |  | SI | Domicilio |
| Q07 | varchar |  |  | SI | Nombre Cuidador |
| Q08 | varchar |  |  | SI | Teléfono |
| Q09 | varchar |  |  | SI | Motivo de Hospitalización |
| Q10 | varchar |  |  | SI | Otras Lesiones |
| Q11 | varchar |  |  | SI | Tratamiento U.P.P. u Otras Lesiones |
| Q12 | varchar |  |  | SI | Otros Antecedentes |
| Q13 | varchar |  |  | SI | Fármacos |
| Q14 | varchar |  |  | SI | Número de la Dirección  |
| Q15 | varchar |  |  | SI | Etnia |
| Q16 | varchar |  |  | SI | Edad |
| Q17 | varchar |  |  | SI | Categorización (Riesgo/Dependencia) |
| Q18 | date |  |  | SI | Fecha Próximo Control 1era. |
| Q19 | varchar |  |  | SI | Especialidad 1era. |
| Q20 | varchar |  |  | SI | Zona |
| Q21 | varchar |  |  | SI | Especialidad 2da. |
| Q22 | varchar |  |  | SI | Teléfono Contacto |
| Q23 | varchar |  |  | SI | Estado Conyugal |
| Q24 | date |  |  | SI | Fecha Próximo Control 2da. |
| Q25 | varchar |  |  | SI | Estado Ocupacional |
| Q26 | varchar |  |  | SI | Otros cuidados a realizar en el hogar |
| Q27 | varchar |  |  | SI | Diagnóstico de Egreso |
| Q28 | varchar |  |  | SI | Sala |
| Q29 | varchar |  |  | SI | Servicio que Deriva |
| Q30 | date |  |  | SI | Fecha Solicitud |
| Q31 | varchar |  |  | SI | Médico Solicitante |
| Q32 | varchar |  |  | SI | Teléfono Celular |
| Q33 | varchar |  |  | SI | Licencia Médica Entregada |
| Q34 | varchar |  |  | SI | Cuidados de Enfermería |
| Q35 | varchar |  |  | SI | Régimren |
| Q36 | varchar |  |  | SI | Reposo |
| Q37 | varchar |  |  | SI | Oxigeno |
| Q38 | varchar |  |  | SI | Resultado Escala  Braden |
| Q38ObsDR | varchar |  | FK | SI | Resultado Escala  Braden DR |
| Q39 | varchar |  |  | SI | Cama |
| Q40 | varchar |  |  | SI | Requisitos Necesarios para la Hospitalización Domi... |
| Q41 | varchar |  |  | SI | 1. Fácil acceso a domicilio |
| Q42 | varchar |  |  | SI | 2. Inscrito(a) en CESFAM |
| Q43 | varchar |  |  | SI | 3. Presencia del Cuidador en Domicilio |
| Q44 | varchar |  |  | SI | 4. Cond.Higiénicas adecuadas en el Hogar |
| Q45 | varchar |  |  | SI | 5. Paciente no crítico |
| Q46 | varchar |  |  | SI | 6. Acceso Telefónico |
| Q47 | varchar |  |  | SI | 7. Educación a familia y/o Cuidador |
| Q48 | varchar |  |  | SI | 8. Previsón FONASA |
| Q49 | varchar |  |  | SI | Cual |
| Q50 | varchar |  |  | SI | INFORMACIÓN PREVIA |
| Q51 | varchar |  |  | SI | Tipo de Hospitalización Domiciliaria |
| Q52 | varchar |  |  | SI |  ¿Paciente ingresa a Hospitalización Domiciliaria ... |
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