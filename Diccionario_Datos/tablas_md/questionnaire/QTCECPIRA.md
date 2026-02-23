# questionnaire.QTCECPIRA

> Control IRA.

**Schema:** questionnaire
**Columnas:** 124
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Control IRA.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Peso al Nacer |
| Q02 | varchar |  |  | SI | Talla al Nacer |
| Q03 | varchar |  |  | SI | Edad Gestacional (Semanas) |
| Q04 | varchar |  |  | SI | APGAR 1' |
| Q05 | varchar |  |  | SI | APGAR 3' |
| Q06 | varchar |  |  | SI | APGAR 5' |
| Q07 | varchar |  |  | SI | APGAR 10' |
| Q08 | varchar |  |  | SI | Perimetro Cefalico |
| Q09 | varchar |  |  | SI | Reanimación Respiratoria |
| Q10 | varchar |  |  | SI | Patología de Recien Nacido |
| Q11 | varchar |  |  | SI | Patología durante el embarazo |
| Q12 | varchar |  |  | SI | Detalle de Patología durante el Embarazo |
| Q13 | varchar |  |  | SI | Especificación otras patologías durante el embaraz... |
| Q14 | varchar |  |  | SI | Tipo de Parto |
| Q15 | varchar |  |  | SI | Resultado de Score de riesgo de Morir por Broncone... |
| Q16 | date |  |  | SI | 1.- Fecha Hospitalización |
| Q17 | varchar |  |  | SI | 1.- Edad Hospitalización |
| Q18 | varchar |  |  | SI | 1.- Diagnóstico/Causa |
| Q19 | date |  |  | SI | 2.- Fecha Hospitalización |
| Q20 | varchar |  |  | SI | 2.- Edad Hospitalización |
| Q21 | varchar |  |  | SI | 2.- Diagnóstico/Causa |
| Q22 | date |  |  | SI | 3.- Fecha Hospitalización |
| Q23 | varchar |  |  | SI | 3.- Edad Hospitalización |
| Q24 | varchar |  |  | SI | 3.- Diagnóstico/Causa |
| Q25 | date |  |  | SI | 4.- Fecha Hospitalización |
| Q26 | varchar |  |  | SI | 4.- Edad Hospitalización |
| Q27 | varchar |  |  | SI | 4.- Diagnóstico/Causa |
| Q28 | date |  |  | SI | 1.- Fecha IC |
| Q29 | varchar |  |  | SI | 1.- Especialidad IC |
| Q30 | varchar |  |  | SI | 1.- Motivo IC |
| Q31 | date |  |  | SI | 2.- Fecha IC |
| Q32 | varchar |  |  | SI | 2.- Especialidad IC |
| Q33 | varchar |  |  | SI | 2.- Motivo IC |
| Q34 | date |  |  | SI | 3.- Fecha IC |
| Q35 | varchar |  |  | SI | 3.- Especialidad IC |
| Q36 | varchar |  |  | SI | 3.- Motivo IC |
| Q37 | date |  |  | SI | 4.- Fecha IC |
| Q38 | varchar |  |  | SI | 4.- Especialidad IC |
| Q39 | varchar |  |  | SI | 4.- Motivo IC |
| Q40 | varchar |  |  | SI | Control por |
| Q41 | varchar |  |  | SI | Diagnóstico |
| Q42 | varchar |  |  | SI | Evaluación Control |
| Q43 | varchar |  |  | SI | PEF (%) |
| Q44 | varchar |  |  | SI | Indicaciones |
| Q45 | varchar |  |  | SI | Inhaladores de Mantención |
| Q46 | varchar |  |  | SI | Medicamentos |
| Q47 | varchar |  |  | SI | SCI (Score de Ingreso) |
| Q48 | varchar |  |  | SI | SCE (Score de Egreso) |
| Q49 | varchar |  |  | SI | Resultado RX Tórax |
| Q50 | varchar |  |  | SI | Detalle Resultado RX Tórax |
| Q51 | date |  |  | SI | Fecha Resultado RX Tórax |
| Q52 | varchar |  |  | SI | Resultado Flujometría |
| Q53 | varchar |  |  | SI | Detalle Resultado Flujometría |
| Q54 | date |  |  | SI | Fecha Resultado Flujometría |
| Q55 | varchar |  |  | SI | Resultado Espirometría |
| Q56 | varchar |  |  | SI | Detalle Resultado Espirometría |
| Q57 | date |  |  | SI | Fecha Resultado Espirometría |
| Q58 | varchar |  |  | SI | Resultado Test de Ejercicios |
| Q59 | varchar |  |  | SI | Detalle Resultado Test de Ejercicios |
| Q60 | date |  |  | SI | Fecha Resultado Test de Ejercicios |
| Q61 | varchar |  |  | SI | Resultado Eosinofilos |
| Q62 | varchar |  |  | SI | Detalle Resultado Eosinofilos |
| Q63 | date |  |  | SI | Fecha Resultado Eosinofilos |
| Q64 | varchar |  |  | SI | Resultado Test Cutáneo |
| Q65 | varchar |  |  | SI | Detalle Resultado Test Cutáneo |
| Q66 | date |  |  | SI | Fecha Resultado Test Cutáneo |
| Q67 | varchar |  |  | SI | Resultado Test del Sudor |
| Q68 | varchar |  |  | SI | Detalle Resultado Test del Sudor |
| Q69 | date |  |  | SI | Fecha Resultado Test del Sudor |
| Q70 | varchar |  |  | SI | Puntaje de Score de riesgo de Morir por Bronconeum... |
| Q71 | varchar |  |  | SI | HLHT |
| Q72 | varchar |  |  | SI | Origen de Paciente |
| Q73 | date |  |  | SI | 1.- Fecha de Alta  |
| Q74 | date |  |  | SI | 2.- Fecha de Alta |
| Q75 | date |  |  | SI | 3.- Fecha de Alta |
| Q76 | date |  |  | SI | 4.- Fecha de Alta |
| Q77 | varchar |  |  | SI | Clasificación de Control |
| Q78 | varchar |  |  | SI | Inhaladores de Rescate |
| Q79 | varchar |  |  | SI | Antecedentes de Descompensación |
| Q80 | varchar |  |  | SI | Antecedentes de Descompensación |
| Q81 | varchar |  |  | SI | Datos Relevantes Anamnesis/Examen Fisico |
| Q82 | varchar |  |  | SI | Vacuna Anti Influeza |
| Q83 | date |  |  | SI | Fecha ultimo Control |
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