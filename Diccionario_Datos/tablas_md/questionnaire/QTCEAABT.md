# questionnaire.QTCEAABT

> Auditoría de abandono al tratamiento de tuberculosis

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Auditoría de abandono al tratamiento de tuberculosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Servicio de Salud |
| Q02 | varchar |  |  | SI | Establecimiento  |
| Q03 | varchar |  |  | SI | Comuna |
| Q04 | date |  |  | SI | Fecha |
| Q05 | varchar |  |  | SI | Nombre Paciente |
| Q06 | varchar |  |  | SI | Apellido Paterno |
| Q07 | varchar |  |  | SI | Apellido Materno |
| Q08 | varchar |  |  | SI | Edad |
| Q09 | varchar |  |  | SI | Sexo |
| Q10 | varchar |  |  | SI | RUT |
| Q11 | varchar |  |  | SI | Estado civil |
| Q12 | varchar |  |  | SI | ¿Cuenta con grupo familiar? |
| Q13 | varchar |  |  | SI | ¿Con quién vive? |
| Q14 | varchar |  |  | SI | Escolaridad |
| Q15 | varchar |  |  | SI | Ocupación |
| Q16 | varchar |  |  | SI | Trabajo Estable |
| Q17 | date |  |  | SI | Fecha del 1° Diagnóstico |
| Q18 | date |  |  | SI | Fecha de recaída (si corresponde) |
| Q19 | varchar |  |  | SI | Órgano |
| Q20 | varchar |  |  | SI | Confirmación Diagnóstica |
| Q21 | numeric |  |  | SI | Valor ADA en secreciones (si corresponde) |
| Q22 | varchar |  |  | SI | Antecedentes del tratamiento (antes de este abando... |
| Q23 | date |  |  | SI | Fecha de inicio de fase diaria antes de este aband... |
| Q24 | varchar |  |  | SI | Medicamentos y dosis usadas en la fase diaria |
| Q25 | numeric |  |  | SI | N° dosis diarias recibidas antes de este último ab... |
| Q26 | date |  |  | SI | Fecha de inicio de fase bisemanal antes de este ab... |
| Q27 | varchar |  |  | SI | Medicamentos y dosis usadas en la fase bisemanal |
| Q28 | numeric |  |  | SI | N° de dosis bisemanales recibidas antes de este úl... |
| Q29 | date |  |  | SI | Fecha BK |
| Q30 | varchar |  |  | SI | Resultado última BK de control de tratamiento |
| Q31 | varchar |  |  | SI | Factores de riesgo de abandono |
| Q32 | numeric |  |  | SI | N°  de abandonos anteriores |
| Q33 | varchar |  |  | SI | Clasificación riesgo |
| Q34 | varchar |  |  | SI | Medidas de prevención del abandono programadas seg... |
| Q35 | numeric |  |  | SI | N° Consultas enfermería |
| Q36 | varchar |  |  | SI | ¿Que otras acciones se hicieron? |
| Q37 | date |  |  | SI | Fecha de último abandono |
| Q38 | varchar |  |  | SI | Control Médico |
| Q39 | varchar |  |  | SI | Consultas de enfermera |
| Q40 | varchar |  |  | SI | Otras consultas enfermera |
| Q41 | bit |  |  | SI | Visitas Domiciliaria al ingreso |
| Q42 | bit |  |  | SI | Visita domiciliaria a la 1° semana de inasistencia |
| Q43 | varchar |  |  | SI | Causa de la inasistencia 1 |
| Q44 | bit |  |  | SI | Visita domiciliaria a las 2°  semana de inasistenc... |
| Q45 | varchar |  |  | SI | Causa de inasistencia 2 |
| Q46 | bit |  |  | SI | Visita domiciliaria a la 3° semana de inasistencia |
| Q47 | varchar |  |  | SI | Causa de la inasistencia 3 |
| Q48 | varchar |  |  | SI | Que otra acciones que se hicieron |
| Q49 | varchar |  |  | SI | Condición de egreso al momento de la auditoría |
| Q50 | varchar |  |  | SI | Resultado de Baciloscopias del año actual |
| Q51 | varchar |  |  | SI | Causas del paciente |
| Q52 | varchar |  |  | SI | Otras causas |
| Q53 | varchar |  |  | SI | Causas Institucionales de este abandono |
| Q54 | varchar |  |  | SI | Otras causas institucionales |
| Q55 | varchar |  |  | SI | Observaciones |
| Q56 | varchar |  |  | SI | Resultados de estudio de contacto (EC) |
| Q57 | varchar |  |  | SI | Nombre de Enfermera encargada |
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