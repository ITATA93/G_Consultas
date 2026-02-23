# SQLUser.CT_PhoneNumCategory

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHNC_RowId | bigint | PK |  | NO | - |
| PHNC_Code | varchar |  |  | NO | Code |
| PHNC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHNC_CreatedDate | date |  |  | SI | Created Date |
| PHNC_CreatedTime | time |  |  | SI | Created Time |
| PHNC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHNC_Desc | varchar |  |  | NO | Description |
| PHNC_Owner | varchar |  |  | SI | Owner |
| PHNC_UpdatedDate | date |  |  | SI | Updated Date |
| PHNC_UpdatedTime | time |  |  | SI | Updated Time |
| PHNC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Servicio de Salud |
| Q02 | - |  |  | SI | Establecimiento |
| Q03 | - |  |  | SI | Comuna |
| Q04 | - |  |  | SI | Fecha |
| Q05 | - |  |  | SI | Nombre Paciente |
| Q06 | - |  |  | SI | Apellido Paterno |
| Q07 | - |  |  | SI | Apellido Materno |
| Q08 | - |  |  | SI | Edad |
| Q09 | - |  |  | SI | Sexo |
| Q10 | - |  |  | SI | RUT |
| Q11 | - |  |  | SI | Estado civil |
| Q12 | - |  |  | SI | ¿Cuenta con grupo familiar? |
| Q13 | - |  |  | SI | ¿Con quién vive? |
| Q14 | - |  |  | SI | Escolaridad |
| Q15 | - |  |  | SI | Ocupación |
| Q16 | - |  |  | SI | Trabajo Estable |
| Q17 | - |  |  | SI | Fecha del 1° Diagnóstico |
| Q18 | - |  |  | SI | Fecha de recaída (si corresponde) |
| Q19 | - |  |  | SI | Órgano |
| Q20 | - |  |  | SI | Confirmación Diagnóstica |
| Q21 | - |  |  | SI | Valor ADA en secreciones (si corresponde) |
| Q22 | - |  |  | SI | Antecedentes del tratamiento (antes de este abando... |
| Q23 | - |  |  | SI | Fecha de inicio de fase diaria antes de este aband... |
| Q24 | - |  |  | SI | Medicamentos y dosis usadas en la fase diaria |
| Q25 | - |  |  | SI | N° dosis diarias recibidas antes de este último ab... |
| Q26 | - |  |  | SI | Fecha de inicio de fase bisemanal antes de este ab... |
| Q27 | - |  |  | SI | Medicamentos y dosis usadas en la fase bisemanal |
| Q28 | - |  |  | SI | N° de dosis bisemanales recibidas antes de este úl... |
| Q29 | - |  |  | SI | Fecha BK |
| Q30 | - |  |  | SI | Resultado última BK de control de tratamiento |
| Q31 | - |  |  | SI | Factores de riesgo de abandono |
| Q32 | - |  |  | SI | N°  de abandonos anteriores |
| Q33 | - |  |  | SI | Clasificación riesgo |
| Q34 | - |  |  | SI | Medidas de prevención del abandono programadas seg... |
| Q35 | - |  |  | SI | N° Consultas enfermería |
| Q36 | - |  |  | SI | ¿Que otras acciones se hicieron? |
| Q37 | - |  |  | SI | Fecha de último abandono |
| Q38 | - |  |  | SI | Control Médico |
| Q39 | - |  |  | SI | Consultas de enfermera |
| Q40 | - |  |  | SI | Otras consultas enfermera |
| Q41 | - |  |  | SI | Visitas Domiciliaria al ingreso |
| Q42 | - |  |  | SI | Visita domiciliaria a la 1° semana de inasistencia |
| Q43 | - |  |  | SI | Causa de la inasistencia 1 |
| Q44 | - |  |  | SI | Visita domiciliaria a las 2°  semana de inasistenc... |
| Q45 | - |  |  | SI | Causa de inasistencia 2 |
| Q46 | - |  |  | SI | Visita domiciliaria a la 3° semana de inasistencia |
| Q47 | - |  |  | SI | Causa de la inasistencia 3 |
| Q48 | - |  |  | SI | Que otra acciones que se hicieron |
| Q49 | - |  |  | SI | Condición de egreso al momento de la auditoría |
| Q50 | - |  |  | SI | Resultado de Baciloscopias del año actual |
| Q51 | - |  |  | SI | Causas del paciente |
| Q52 | - |  |  | SI | Otras causas |
| Q53 | - |  |  | SI | Causas Institucionales de este abandono |
| Q54 | - |  |  | SI | Otras causas institucionales |
| Q55 | - |  |  | SI | Observaciones |
| Q56 | - |  |  | SI | Resultados de estudio de contacto (EC) |
| Q57 | - |  |  | SI | Nombre de Enfermera encargada |
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