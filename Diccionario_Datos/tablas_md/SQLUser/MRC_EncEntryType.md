# SQLUser.MRC_EncEntryType

**Schema:** SQLUser
**Columnas:** 172
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ETYPE_RowId | bigint | PK |  | NO | - |
| ChildQ32DR | - |  |  | SI | Child Reference: Tipo de aborto |
| ETYPE_AutolockPeriod | integer |  |  | SI | Period before automatically locking encounter entr... |
| ETYPE_AutolockUnits | varchar |  |  | SI | Units for automatically locking encounter entry |
| ETYPE_CheckUnlockedEntry | bit |  |  | SI | Check for Unlocked Entries upon Exit of ACN |
| ETYPE_Code | varchar |  |  | SI | Code |
| ETYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ETYPE_CreatedDate | date |  |  | SI | Created Date |
| ETYPE_CreatedTime | time |  |  | SI | Created Time |
| ETYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ETYPE_DateFrom | date |  |  | SI | DateFrom |
| ETYPE_DateTo | date |  |  | SI | DateTo |
| ETYPE_DefaultTimeline_DR | bigint |  | FK | SI | Default Clinical Timeline for this Entry Type |
| ETYPE_Desc | varchar |  |  | SI | Description |
| ETYPE_DisplayCopiedText | varchar |  |  | SI | Display Copied Text |
| ETYPE_Group_DR | bigint |  | FK | SI | Optional Group |
| ETYPE_IsProgressNote | bit |  |  | SI | is Progress Note |
| ETYPE_LocFilter | varchar |  |  | SI | Location Filter |
| ETYPE_OpenFirstAction | bit |  |  | SI | Open First Action Automatically |
| ETYPE_Owner | varchar |  |  | SI | Owner |
| ETYPE_Purpose | varchar |  |  | SI | Purpose |
| ETYPE_SSPFilter | varchar |  |  | SI | Access Profile Filter |
| ETYPE_SecGroupFilter | varchar |  |  | SI | Security Group Filter |
| ETYPE_TimelineView | varchar |  |  | SI | Default Timeline View for this Entry Type |
| ETYPE_UpdatedDate | date |  |  | SI | Updated Date |
| ETYPE_UpdatedTime | time |  |  | SI | Updated Time |
| ETYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombre de la madre |
| Q02 | - |  |  | SI | RUT de la madre |
| Q03 | - |  |  | SI | Pasaporte de la madre |
| Q04 | - |  |  | SI | Dirección de la madre |
| Q05 | - |  |  | SI | Dirección de la madre (comuna) |
| Q06 | - |  |  | SI | Dirección de la madre (Otro) |
| Q07 | - |  |  | SI | Edad de la madre |
| Q08 | - |  |  | SI | Último curso realizado |
| Q09 | - |  |  | SI | Nivel educacional |
| Q10 | - |  |  | SI | Ocupación |
| Q11 | - |  |  | SI | Categoría ocupacional |
| Q12 | - |  |  | SI | Nombre del progenitor |
| Q13 | - |  |  | SI | RUT / Pasaporte del progenitor |
| Q14 | - |  |  | SI | Edad del progenitor |
| Q15 | - |  |  | SI | Último curso realizado (progenitor) |
| Q16 | - |  |  | SI | Nivel educacional (progenitor) |
| Q17 | - |  |  | SI | Ocupación (progenitor) |
| Q18 | - |  |  | SI | Categoría ocupacional (progenitor) |
| Q19 | - |  |  | SI | Dirección del progenitor (Calle, N°, comuna) |
| Q20 | - |  |  | SI | Pueblo originario |
| Q21 | - |  |  | SI | Grupo cultural |
| Q22 | - |  |  | SI | Fecha de término del último embarazo |
| Q23 | - |  |  | SI | Fecha de inicio del control prenatal |
| Q24 | - |  |  | SI | Método anticonceptivo |
| Q25 | - |  |  | SI | ¿Embarazo planificado? |
| Q26 | - |  |  | SI | Causa de la última cesárea (si procede) |
| Q27 | - |  |  | SI | Peso habitual |
| Q28 | - |  |  | SI | Chequeo de antecedentes personales |
| Q29 | - |  |  | SI | Chequeo de antecedentes familiares |
| Q30 | - |  |  | SI | N° de gestaciones |
| Q31 | - |  |  | SI | N° de abortos no provocados |
| Q33 | - |  |  | SI | N° de partos |
| Q34 | - |  |  | SI | ¿Algún RN de peso inferior a 2.500 grs.? |
| Q35 | - |  |  | SI | ¿Alguna gesta de tres partos? |
| Q36 | - |  |  | SI | N° de partos vaginales |
| Q37 | - |  |  | SI | N° de partos por cesárea |
| Q38 | - |  |  | SI | N° de nacidos vivos |
| Q39 | - |  |  | SI | N° de mortinatos |
| Q40 | - |  |  | SI | N° de RN fallecido(s) a la 1era semana de vida |
| Q41 | - |  |  | SI | N° de RN fallecido(s) entre la 2da y 4ta semana de... |
| Q42 | - |  |  | SI | N° de hijos vivos actualmente |
| Q43 | - |  |  | SI | ¿Algún RN de peso superior a 4.000 grs.? |
| Q44 | - |  |  | SI | FUR (entregada por la paciente) |
| Q45 | - |  |  | SI | FUR (Operacional) |
| Q46 | - |  |  | SI | ¿Dudas en relación a la FUR? |
| Q47 | - |  |  | SI | Peso al ingreso |
| Q47ObsDR | - |  |  | SI | Peso al ingreso DR |
| Q48 | - |  |  | SI | Talla |
| Q48ObsDR | - |  |  | SI | Talla DR |
| Q49 | - |  |  | SI | Fecha probable de parto |
| Q50 | - |  |  | SI | Edad gestacional al ingreso |
| Q52 | - |  |  | SI | Grupo sanguíneo |
| Q53 | - |  |  | SI | Sensibilizada |
| Q55 | - |  |  | SI | Temperatura axilar (C°) |
| Q55ObsDR | - |  |  | SI | Temperatura axilar (C°) DR |
| Q56 | - |  |  | SI | Presión arterial sistólica (mmHg) |
| Q56ObsDR | - |  |  | SI | Presión arterial sistólica (mmHg) DR |
| Q57 | - |  |  | SI | Presión arterial diastólica (mmHg) |
| Q57ObsDR | - |  |  | SI | Presión arterial diastólica (mmHg) DR |
| Q58 | - |  |  | SI | Altura uterina (cms.) |
| Q58ObsDR | - |  |  | SI | Altura uterina (cms.) DR |
| Q59 | - |  |  | SI | Latidos cardiofetales feto 1 (lpm) |
| Q59ObsDR | - |  |  | SI | Latidos cardiofetales feto 1 (lpm) DR |
| Q60 | - |  |  | SI | Latidos cardiofetales feto 2 (lpm) |
| Q60ObsDR | - |  |  | SI | Latidos cardiofetales feto 2 (lpm) DR |
| Q61 | - |  |  | SI | Latidos cardiofetales feto 3 (lpm) |
| Q61ObsDR | - |  |  | SI | Latidos cardiofetales feto 3 (lpm) DR |
| Q62 | - |  |  | SI | Patología materna al ingreso |
| Q63 | - |  |  | SI | Destino |
| Q64 | - |  |  | SI | Nombre del profesional |
| Q65 | - |  |  | SI | Tipo de profesional |
| Q66 | - |  |  | SI | Alfabeta |
| Q67 | - |  |  | SI | N° de abortos provocados |
| Q68 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q69 | - |  |  | SI | Presión Arterial Media (mmHg) |
| Q70 | - |  |  | SI | Frecuencia Respiratoria |
| Q71 | - |  |  | SI | FIO2 % |
| Q72 | - |  |  | SI | Flujo de Oxígeno (Lt/Min) |
| Q73 | - |  |  | SI | Oxigenoterapia |
| Q74 | - |  |  | SI | Saturación O2 (%) |
| Q75 | - |  |  | SI | Hemoglucotest (mg/dl) |
| Q76 | - |  |  | SI | Temperatura Rectal (°C) |
| Q77 | - |  |  | SI | Frecuencia Cardíaca (lpm) |
| Q77ObsDR | - |  |  | SI | Frecuencia Cardíaca (lpm)  DR |
| Q78 | - |  |  | SI | Presión Arterial Media |
| Q78ObsDR | - |  |  | SI | Presión Arterial Media  DR |
| Q79 | - |  |  | SI | Frecuencia Respiratoria |
| Q79ObsDR | - |  |  | SI | Frecuencia Respiratoria  DR |
| Q80 | - |  |  | SI | FIO2 % |
| Q80ObsDR | - |  |  | SI | FIO2 %  DR |
| Q81 | - |  |  | SI | Flujo de Oxígeno (Lt/Min) |
| Q81ObsDR | - |  |  | SI | Flujo de Oxígeno (Lt/Min)  DR |
| Q82 | - |  |  | SI | Oxigenoterapia |
| Q82ObsDR | - |  |  | SI | Oxigenoterapia  DR |
| Q83 | - |  |  | SI | Saturación O2 (%) |
| Q83ObsDR | - |  |  | SI | Saturación O2 (%)  DR |
| Q84 | - |  |  | SI | Hemoglucotest (mg/dl) |
| Q84ObsDR | - |  |  | SI | Hemoglucotest (mg/dl)  DR |
| Q85 | - |  |  | SI | Temperatura Rectal (°C) |
| Q85ObsDR | - |  |  | SI | Temperatura Rectal (°C) DR |
| Q86 | - |  |  | SI | Curva Peso |
| Q87 | - |  |  | SI | N° de Hijos Fallecidos Total |
| Q88 | - |  |  | SI | Otros |
| Q89 | - |  |  | SI | Otros |
| Q90 | - |  |  | SI | Plan de Ingreso |
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