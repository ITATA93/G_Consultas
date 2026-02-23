# questionnaire.QCLXXEFCIR

> Examen Físico

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q19 | varchar |  |  | SI | P. Arterial Sistólica |
| Q19ObsDR | varchar |  | FK | SI | P. Arterial Sistólica DR |
| Q20 | varchar |  |  | SI | P. Arterial Diastólica |
| Q20ObsDR | varchar |  | FK | SI | P. Arterial Diastólica DR |
| Q21 | varchar |  |  | SI | Frecuencia cardíaca |
| Q21ObsDR | varchar |  | FK | SI | Frecuencia cardíaca DR |
| Q22 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q22ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q23 | varchar |  |  | SI | Temperatura axilar |
| Q23ObsDR | varchar |  | FK | SI | Temperatura axilar DR |
| Q24 | varchar |  |  | SI | Saturación O2 (%) |
| Q24ObsDR | varchar |  | FK | SI | Saturación O2 (%) DR |
| Q25 | varchar |  |  | SI | FiO2 (%) |
| Q25ObsDR | varchar |  | FK | SI | FiO2 (%) DR |
| Q26 | varchar |  |  | SI | Escala de dolor (EVA) |
| Q26ObsDR | varchar |  | FK | SI | Escala de dolor (EVA) DR |
| Q27 | bit |  |  | SI | Cabeza normal. Yugulares no ingurgitadas, pulso ca... |
| Q28 | varchar |  |  | SI | Cabeza y cuello |
| Q29 | varchar |  |  | SI | Descripción, cabeza y cuello |
| Q30 | bit |  |  | SI | Resto del examen realizado, sin alteraciones (cyc) |
| Q31 | varchar |  |  | SI | Auscultación (<3) |
| Q32 | varchar |  |  | SI | Descripción, <3 |
| Q33 | bit |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q34 | bit |  |  | SI | Resto del examen realizado, sin alteraciones (<3) |
| Q36 | bit |  |  | SI | Resto del examen realizado sin alteraciones (pl) |
| Q37 | bit |  |  | SI | Murmullo pulmonar simétrico normal, sin ruidos agr... |
| Q38 | varchar |  |  | SI | Descripción, pulmonar |
| Q40 | bit |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q41 | bit |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q42 | varchar |  |  | SI | Descripción, abdomen |
| Q43 | bit |  |  | SI | Región anogenital normal |
| Q44 | varchar |  |  | SI | Descripción, región anogenital |
| Q47 | bit |  |  | SI | Extremidades normales, sin lesiones. Edema (-). Ar... |
| Q48 | varchar |  |  | SI | Descripción, extremidades |
| Q49 | varchar |  |  | SI | Exámenes de laboratorio |
| Q50 | varchar |  |  | SI | Exámenes de imagenología |
| Q53 | varchar |  |  | SI | Profesional de salud |
| Q54 | bit |  |  | SI | Resto del examen realizado, sin alteraciones (ext) |
| Q55 | varchar |  |  | SI | Descripción examen físico general |
| Q56 | bit |  |  | SI | Pulsos simétricos, amplitud normal. |
| Q57 | varchar |  |  | SI | Descripción Examen físico simple |
| Q58 | bit |  |  | SI | Resto del examen realizado, sin alteraciones (anog... |
| Q59 | varchar |  |  | SI | (Ingresar  valor de 1 a 10) |
| Q60 | varchar |  |  | SI | mmHg |
| Q61 | varchar |  |  | SI | lpm |
| Q62 | varchar |  |  | SI | mmHg |
| Q63 | varchar |  |  | SI | rpm |
| Q64 | varchar |  |  | SI | % |
| Q65 | varchar |  |  | SI | % |
| Q66 | varchar |  |  | SI | °C |
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