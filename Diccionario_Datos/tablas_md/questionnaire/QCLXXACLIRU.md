# questionnaire.QCLXXACLIRU

> REGISTRO ANTECEDENTES RUI

**Schema:** questionnaire
**Columnas:** 134
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REGISTRO ANTECEDENTES RUI

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | ANTECEDENTES CLÍNICOS |
| Q02 | varchar |  |  | SI | Resultado EFAM A |
| Q03 | varchar |  |  | SI | Resultado EFAM B |
| Q04 | varchar |  |  | SI | Resultado de MMSE |
| Q05 | varchar |  |  | SI | Mamografía |
| Q06 | varchar |  |  | SI | Papanicolau |
| Q07 | varchar |  |  | SI | Vacunación Influenza |
| Q08 | varchar |  |  | SI | Vacunación Neumococo |
| Q09 | varchar |  |  | SI | Fecha Registros Antecedentes RUI |
| Q09ObsDR | varchar |  | FK | SI | Fecha Registros Antecedentes RUI DR |
| Q10 | date |  |  | SI | Fecha Último Registro RUI |
| Q11 | varchar |  |  | SI | Beneficiario Programa Alimentario |
| Q12 | date |  |  | SI | Fecha Resultado EFAM A |
| Q13 | date |  |  | SI | Fecha Resultado EFAM B |
| Q14 | date |  |  | SI | Fecha Resultado de MMSE |
| Q15 | date |  |  | SI | Fecha Mamografía |
| Q16 | date |  |  | SI | Fecha Papanicolau |
| Q17 | date |  |  | SI | Fecha Vacunación Influenza |
| Q18 | date |  |  | SI | Fecha Vacunación Neumococo |
| Q19 | date |  |  | SI | Fecha Beneficiario Programa Alimentario |
| Q20 | varchar |  |  | SI | CHEQUEO DIAGNÓSTICOS CRÓNICOS |
| Q21 | varchar |  |  | SI | Enfermedad Renal Crónica |
| Q21ObsDR | varchar |  | FK | SI | Enfermedad Renal Crónica DR |
| Q22 | date |  |  | SI | Fecha Enfermedad Renal Crónica |
| Q23 | varchar |  |  | SI | EPOC |
| Q24 | date |  |  | SI | Fecha EPOC |
| Q25 | varchar |  |  | SI | Nivel Severidad EPOC |
| Q26 | varchar |  |  | SI | Diabetes Mellitus |
| Q27 | date |  |  | SI | Fecha Diabetes Mellitus |
| Q28 | varchar |  |  | SI | Resultado Riesgo Ulceración |
| Q28ObsDR | varchar |  | FK | SI | Resultado Riesgo Ulceración DR |
| Q29 | date |  |  | SI | Fecha Resultado Riesgo Ulceración |
| Q30 | varchar |  |  | SI | Amputación de extremidad |
| Q31 | date |  |  | SI | Fecha Amputación de extremidad |
| Q32 | varchar |  |  | SI | ACV |
| Q33 | date |  |  | SI | Fecha ACV |
| Q34 | varchar |  |  | SI | IAM |
| Q35 | date |  |  | SI | Fecha IAM |
| Q36 | varchar |  |  | SI | Sordera |
| Q37 | date |  |  | SI | Fecha Sordera |
| Q38 | varchar |  |  | SI | Retraso Mental |
| Q39 | date |  |  | SI | Fecha Retraso Mental |
| Q40 | varchar |  |  | SI | Fragilidad |
| Q41 | date |  |  | SI | Fecha Fragilidad |
| Q42 | varchar |  |  | SI | MORBILIDAD |
| Q43 | varchar |  |  | SI | Asistencia a Urgencias por Patología Crónica |
| Q44 | date |  |  | SI | Fecha Asistencia a Urgencias por Patología Crónica |
| Q45 | varchar |  |  | SI | Hospitalización por Patología Crónica |
| Q46 | date |  |  | SI | Fecha Hospitalización por patología crónica |
| Q47 | varchar |  |  | SI | HÁBITOS |
| Q48 | varchar |  |  | SI | Hábitos Alimenticios |
| Q49 | date |  |  | SI | Fecha Hábitos Alimenticios |
| Q50 | varchar |  |  | SI | Actividad Física Actual |
| Q51 | date |  |  | SI | Fecha Actividad Física Actual |
| Q52 | varchar |  |  | SI | Tabaquismo |
| Q53 | date |  |  | SI | Fecha Tabaquismo |
| Q54 | varchar |  |  | SI | Alcohol |
| Q55 | date |  |  | SI | Fecha Consumo de alcohol |
| Q56 | varchar |  |  | SI | Consumo de Drogas |
| Q57 | date |  |  | SI | Fecha Consumo de drogas |
| Q58 | varchar |  |  | SI | Alergia a Medicamentos |
| Q59 | date |  |  | SI | Fecha Alergia a Medicamentos |
| Q60 | varchar |  |  | SI | Monitoreo a Distancia |
| Q61 | date |  |  | SI | Fecha Monitoreo a Distancia |
| Q62 | varchar |  |  | SI | ANTECEDENTES FAMILIARES |
| Q63 | varchar |  |  | SI | Familiar con Condición Crónica |
| Q64 | date |  |  | SI | Fecha Familiar con Condición Crónica |
| Q65 | varchar |  |  | SI | Número de Integrantes Núcleo Familiar |
| Q65ObsDR | varchar |  | FK | SI | Número de Integrantes Núcleo Familiar DR |
| Q66 | date |  |  | SI | Fecha Número de Integrantes Nucleo Familiar |
| Q67 | varchar |  |  | SI | Red de apoyo |
| Q68 | date |  |  | SI | Fecha Red de Apoyo |
| Q69 | varchar |  |  | SI | Red de apoyo Principal |
| Q70 | date |  |  | SI | Fecha Red de Apoyo Principal |
| Q71 | varchar |  |  | SI | Institucionalizado |
| Q72 | date |  |  | SI | Fecha Institucionalizado |
| Q73 | varchar |  |  | SI | Situación de Calle |
| Q74 | date |  |  | SI | Fecha Situación de Calle |
| Q75 | varchar |  |  | SI | ANTECEDENTES DE SALUD MENTAL |
| Q76 | varchar |  |  | SI | Ideación / Intento Suicida |
| Q77 | date |  |  | SI | Fecha Ideación / Intento Suicida |
| Q78 | varchar |  |  | SI | Síntomas Psicóticos |
| Q79 | date |  |  | SI | Fecha Síntomas Psicóticos |
| Q80 | varchar |  |  | SI | Factores de Riesgo - Víctima de Violencia |
| Q81 | date |  |  | SI | Fecha Factores de Riesgo - Víctima de Violencia |
| Q82 | varchar |  |  | SI | Factores de Riesgo - Víctima de Abuso Sexual |
| Q83 | date |  |  | SI | Fecha Factores de Riesgo - Víctima de Abuso Sexual |
| Q84 | varchar |  |  | SI | Amputación de extremidad por DM |
| Q85 | date |  |  | SI | Fecha Amputación de extremidad Por DM |
| Q86 | varchar |  |  | SI | Hora Registros Antecedentes RUI |
| Q86ObsDR | varchar |  | FK | SI | Hora Registros Antecedentes RUI DR |
| Q87 | time |  |  | SI | Hora Último Registro RUI |
| Q89 | varchar |  |  | SI | Etapa Renal Crónica |
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