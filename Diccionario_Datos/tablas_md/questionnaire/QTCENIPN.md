# questionnaire.QTCENIPN

> Ingreso Prenatal APS

**Schema:** questionnaire
**Columnas:** 149
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Prenatal APS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre de la madre |
| Q02 | varchar |  |  | SI | RUT de la madre |
| Q03 | varchar |  |  | SI | Pasaporte de la madre |
| Q04 | varchar |  |  | SI | Dirección de la madre |
| Q05 | varchar |  |  | SI | Dirección de la madre (comuna) |
| Q06 | varchar |  |  | SI | Dirección de la madre (Otro) |
| Q07 | varchar |  |  | SI | Edad de la madre |
| Q08 | varchar |  |  | SI | Último curso realizado |
| Q09 | varchar |  |  | SI | Nivel educacional |
| Q10 | varchar |  |  | SI | Ocupación |
| Q11 | varchar |  |  | SI | Categoría ocupacional |
| Q12 | varchar |  |  | SI | Nombre del progenitor |
| Q13 | varchar |  |  | SI | RUT / Pasaporte del progenitor |
| Q14 | varchar |  |  | SI | Edad del progenitor |
| Q15 | varchar |  |  | SI | Último curso realizado (progenitor) |
| Q16 | varchar |  |  | SI | Nivel educacional (progenitor) |
| Q17 | varchar |  |  | SI | Ocupación (progenitor) |
| Q18 | varchar |  |  | SI | Categoría ocupacional (progenitor) |
| Q19 | varchar |  |  | SI | Dirección del progenitor (Calle, N°, comuna) |
| Q20 | varchar |  |  | SI | Pueblo originario |
| Q21 | varchar |  |  | SI | Grupo cultural |
| Q22 | date |  |  | SI | Fecha de término del último embarazo  |
| Q23 | date |  |  | SI | Fecha de inicio del control prenatal |
| Q24 | varchar |  |  | SI | Método anticonceptivo |
| Q25 | varchar |  |  | SI | ¿Embarazo planificado? |
| Q26 | varchar |  |  | SI | Causa de la última cesárea (si procede) |
| Q27 | numeric |  |  | SI | Peso habitual |
| Q28 | varchar |  |  | SI | Chequeo de antecedentes personales |
| Q29 | varchar |  |  | SI | Chequeo de antecedentes familiares |
| Q30 | varchar |  |  | SI | N° de gestaciones |
| Q31 | varchar |  |  | SI | N° de abortos no provocados |
| Q33 | varchar |  |  | SI | N° de partos |
| Q34 | varchar |  |  | SI | ¿Algún RN de peso inferior a 2.500 grs.? |
| Q35 | varchar |  |  | SI | ¿Alguna gesta de tres partos? |
| Q36 | varchar |  |  | SI | N° de partos vaginales |
| Q37 | numeric |  |  | SI | N° de partos por cesárea |
| Q38 | varchar |  |  | SI | N° de nacidos vivos |
| Q39 | varchar |  |  | SI | N° de mortinatos |
| Q40 | varchar |  |  | SI | N° de RN fallecido(s) a la 1era semana de vida |
| Q41 | varchar |  |  | SI | N° de RN fallecido(s) entre la 2da y 4ta semana de... |
| Q42 | varchar |  |  | SI | N° de hijos vivos actualmente |
| Q43 | varchar |  |  | SI | ¿Algún RN de peso superior a 4.000 grs.? |
| Q44 | varchar |  |  | SI | FUR (entregada por la paciente) |
| Q45 | varchar |  |  | SI | FUR (Operacional) |
| Q46 | varchar |  |  | SI | ¿Dudas en relación a la FUR? |
| Q47 | varchar |  |  | SI | Peso al ingreso |
| Q47ObsDR | varchar |  | FK | SI | Peso al ingreso DR |
| Q48 | varchar |  |  | SI | Talla |
| Q48ObsDR | varchar |  | FK | SI | Talla DR |
| Q49 | varchar |  |  | SI | Fecha probable de parto |
| Q50 | numeric |  |  | SI | Edad gestacional al ingreso |
| Q52 | varchar |  |  | SI | Grupo sanguíneo |
| Q53 | varchar |  |  | SI | Sensibilizada |
| Q55 | varchar |  |  | SI | Temperatura axilar (C°) |
| Q55ObsDR | varchar |  | FK | SI | Temperatura axilar (C°) DR |
| Q56 | varchar |  |  | SI | Presión arterial sistólica (mmHg) |
| Q56ObsDR | varchar |  | FK | SI | Presión arterial sistólica (mmHg) DR |
| Q57 | varchar |  |  | SI | Presión arterial diastólica (mmHg) |
| Q57ObsDR | varchar |  | FK | SI | Presión arterial diastólica (mmHg) DR |
| Q58 | varchar |  |  | SI | Altura uterina (cms.) |
| Q58ObsDR | varchar |  | FK | SI | Altura uterina (cms.) DR |
| Q59 | varchar |  |  | SI | Latidos cardiofetales feto 1 (lpm) |
| Q59ObsDR | varchar |  | FK | SI | Latidos cardiofetales feto 1 (lpm) DR |
| Q60 | varchar |  |  | SI | Latidos cardiofetales feto 2 (lpm) |
| Q60ObsDR | varchar |  | FK | SI | Latidos cardiofetales feto 2 (lpm) DR |
| Q61 | varchar |  |  | SI | Latidos cardiofetales feto 3 (lpm) |
| Q61ObsDR | varchar |  | FK | SI | Latidos cardiofetales feto 3 (lpm) DR |
| Q62 | varchar |  |  | SI | Patología materna al ingreso |
| Q63 | varchar |  |  | SI | Destino |
| Q64 | varchar |  |  | SI | Nombre del profesional |
| Q65 | varchar |  |  | SI | Tipo de profesional |
| Q66 | varchar |  |  | SI | Alfabeta |
| Q67 | varchar |  |  | SI | N° de abortos provocados |
| Q68 | numeric |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q69 | varchar |  |  | SI | Presión Arterial Media (mmHg) |
| Q70 | numeric |  |  | SI | Frecuencia Respiratoria |
| Q71 | numeric |  |  | SI | FIO2 % |
| Q72 | numeric |  |  | SI | Flujo de Oxígeno (Lt/Min) |
| Q73 | varchar |  |  | SI | Oxigenoterapia  |
| Q74 | numeric |  |  | SI | Saturación O2 (%) |
| Q75 | varchar |  |  | SI | Hemoglucotest (mg/dl) |
| Q76 | numeric |  |  | SI | Temperatura Rectal (°C) |
| Q77 | varchar |  |  | SI | Frecuencia Cardíaca (lpm)  |
| Q77ObsDR | varchar |  | FK | SI | Frecuencia Cardíaca (lpm)  DR |
| Q78 | varchar |  |  | SI | Presión Arterial Media  |
| Q78ObsDR | varchar |  | FK | SI | Presión Arterial Media  DR |
| Q79 | varchar |  |  | SI | Frecuencia Respiratoria  |
| Q79ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria  DR |
| Q80 | varchar |  |  | SI | FIO2 %  |
| Q80ObsDR | varchar |  | FK | SI | FIO2 %  DR |
| Q81 | varchar |  |  | SI | Flujo de Oxígeno (Lt/Min)  |
| Q81ObsDR | varchar |  | FK | SI | Flujo de Oxígeno (Lt/Min)  DR |
| Q82 | varchar |  |  | SI | Oxigenoterapia  |
| Q82ObsDR | varchar |  | FK | SI | Oxigenoterapia  DR |
| Q83 | varchar |  |  | SI | Saturación O2 (%)  |
| Q83ObsDR | varchar |  | FK | SI | Saturación O2 (%)  DR |
| Q84 | varchar |  |  | SI | Hemoglucotest (mg/dl)  |
| Q84ObsDR | varchar |  | FK | SI | Hemoglucotest (mg/dl)  DR |
| Q85 | varchar |  |  | SI | Temperatura Rectal (°C) |
| Q85ObsDR | varchar |  | FK | SI | Temperatura Rectal (°C) DR |
| Q86 | varchar |  |  | SI | Curva Peso |
| Q87 | numeric |  |  | SI | N° de Hijos Fallecidos Total |
| Q88 | varchar |  |  | SI | Otros |
| Q89 | varchar |  |  | SI | Otros |
| Q90 | varchar |  |  | SI | Plan de Ingreso |
| Q91 | numeric |  |  | SI | Edad gestacional al inicio del control extrasistem... |
| Q92 | varchar |  |  | SI | Ingreso por Traslado |
| Q93 | varchar |  |  | SI | Ingreso con Control Precoz Extrasistema |
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