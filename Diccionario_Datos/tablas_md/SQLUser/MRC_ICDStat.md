# SQLUser.MRC_ICDStat

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCIS_RowID | bigint | PK |  | NO | - |
| MRCIS_Code | varchar |  |  | NO | ICD Status Code |
| MRCIS_CreatedDate | date |  |  | SI | Created Date |
| MRCIS_CreatedTime | time |  |  | SI | Created Time |
| MRCIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRCIS_Desc | varchar |  |  | NO | ICD Status Description |
| MRCIS_RcFlag | varchar |  |  | SI | Archived Flag |
| MRCIS_UpdatedDate | date |  |  | SI | Updated Date |
| MRCIS_UpdatedTime | time |  |  | SI | Updated Time |
| MRCIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Frecuencia Cardiaca (lpm) |
| Q01ObsDR | - |  |  | SI | Frecuencia Cardiaca (lpm) DR |
| Q02 | - |  |  | SI | Presión Arterial Sistólica (mmHg) |
| Q02ObsDR | - |  |  | SI | Presión Arterial Sistólica (mmHg) DR |
| Q03 | - |  |  | SI | Presión Arterial Diastólica (mmHg) |
| Q03ObsDR | - |  |  | SI | Presión Arterial Diastólica (mmHg) DR |
| Q04 | - |  |  | SI | Frecuencia Respiratoria (rpm) |
| Q04ObsDR | - |  |  | SI | Frecuencia Respiratoria (rpm) DR |
| Q05 | - |  |  | SI | FiO2 % |
| Q05ObsDR | - |  |  | SI | FiO2 % DR |
| Q06 | - |  |  | SI | Flujo de Oxígeno (Lt/min) |
| Q06ObsDR | - |  |  | SI | Flujo de Oxígeno (Lt/min) DR |
| Q07 | - |  |  | SI | Oxigenoterapia |
| Q07ObsDR | - |  |  | SI | Oxigenoterapia DR |
| Q08 | - |  |  | SI | Saturación O2 % |
| Q08ObsDR | - |  |  | SI | Saturación O2 % DR |
| Q09 | - |  |  | SI | Temperatura Axilar (°C) |
| Q09ObsDR | - |  |  | SI | Temperatura Axilar (°C) DR |
| Q10 | - |  |  | SI | Temperatura Rectal % |
| Q10ObsDR | - |  |  | SI | Temperatura Rectal % DR |
| Q11 | - |  |  | SI | Hemoglucotest (mg/dl) |
| Q11ObsDR | - |  |  | SI | Hemoglucotest (mg/dl) DR |
| Q12 | - |  |  | SI | comentario 01 |
| Q13 | - |  |  | SI | comentario 02 |
| Q14 | - |  |  | SI | comentario 03 |
| Q15 | - |  |  | SI | comentario 04 |
| Q16 | - |  |  | SI | comentario 05 |
| Q17 | - |  |  | SI | comentario 06 |
| Q18 | - |  |  | SI | comentario 07 |
| Q19 | - |  |  | SI | comentario 08 |
| Q20 | - |  |  | SI | comentario 09 |
| Q21 | - |  |  | SI | comentario 10 |
| Q22 | - |  |  | SI | comentario 11 |
| Q23 | - |  |  | SI | Tipo de Parto |
| Q23ObsDR | - |  |  | SI | Tipo de Parto DR |
| Q24 | - |  |  | SI | Descripción Mamas |
| Q24ObsDR | - |  |  | SI | Descripción Mamas DR |
| Q25 | - |  |  | SI | Descripción Pezones |
| Q25ObsDR | - |  |  | SI | Descripción Pezones DR |
| Q26 | - |  |  | SI | Lactancia Materna Exclusiva |
| Q26ObsDR | - |  |  | SI | Lactancia Materna Exclusiva DR |
| Q27 | - |  |  | SI | Útero |
| Q27ObsDR | - |  |  | SI | Útero DR |
| Q28 | - |  |  | SI | Herida Operatoria |
| Q28ObsDR | - |  |  | SI | Herida Operatoria DR |
| Q29 | - |  |  | SI | Episiotomía |
| Q29ObsDR | - |  |  | SI | Episiotomía DR |
| Q30 | - |  |  | SI | Flujo Genital Puérpera |
| Q30ObsDR | - |  |  | SI | Flujo Genital Puérpera DR |
| Q31 | - |  |  | SI | Cantidad Flujo Genital Puérpera |
| Q31ObsDR | - |  |  | SI | Cantidad Flujo Genital Puérpera DR |
| Q32 | - |  |  | SI | Diuresis |
| Q32ObsDR | - |  |  | SI | Diuresis DR |
| Q33 | - |  |  | SI | Deposiciones |
| Q33ObsDR | - |  |  | SI | Deposiciones DR |
| Q34 | - |  |  | SI | Extremidades Inferiores |
| Q34ObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q35 | - |  |  | SI | Edema |
| Q35ObsDR | - |  |  | SI | Edema DR |
| Q36 | - |  |  | SI | Valoración del Dolor |
| Q37 | - |  |  | SI | Escala de Dolor |
| Q37ObsDR | - |  |  | SI | Escala de Dolor DR |
| Q38 | - |  |  | SI | Ubicación del Dolor |
| Q39 | - |  |  | SI | Razones para no  Evaluar |
| Q40 | - |  |  | SI | Especifique Razón para no Evaluar |
| Q41 | - |  |  | SI | Abdomen |
| Q41ObsDR | - |  |  | SI | Abdomen DR |
| Q42 | - |  |  | SI | comentario 12 |
| Q43 | - |  |  | SI | comentario 13 |
| Q44 | - |  |  | SI | comentario 14 |
| Q45 | - |  |  | SI | comentario 15 |
| Q46 | - |  |  | SI | comentario 16 |
| Q47 | - |  |  | SI | comentario 17 |
| Q48 | - |  |  | SI | comentario 18 |
| Q49 | - |  |  | SI | comentario 19 |
| Q50 | - |  |  | SI | comentario 20 |
| Q51 | - |  |  | SI | comentario 22 |
| Q52 | - |  |  | SI | comentario 23 |
| Q53 | - |  |  | SI | comentario 24 |
| Q54 | - |  |  | SI | comentario 25 |
| Q55 | - |  |  | SI | comentario 26 |
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