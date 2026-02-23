# questionnaire.QTCECPN

> Controles Prenatales APS

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Controles Prenatales APS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Realiza Control Prenatal |
| Q02 | date |  |  | SI | Fecha Primer Control |
| Q03 | varchar |  |  | SI | Edad Gestacional |
| Q03ObsDR | varchar |  | FK | SI | Edad Gestacional DR |
| Q04 | varchar |  |  | SI | Peso (kg) |
| Q04ObsDR | varchar |  | FK | SI | Peso (kg) DR |
| Q05 | date |  |  | SI | Fecha Último Control  |
| Q06 | numeric |  |  | SI | Edad Gestacional |
| Q07 | varchar |  |  | SI | Control ARO |
| Q08 | varchar |  |  | SI | Comentarios |
| Q09 | varchar |  |  | SI | Temperatura Axilar (C°) |
| Q09ObsDR | varchar |  | FK | SI | Temperatura Axilar (C°) DR |
| Q10 | varchar |  |  | SI | Temperatura Rectal (C°) |
| Q10ObsDR | varchar |  | FK | SI | Temperatura Rectal (C°) DR |
| Q11 | varchar |  |  | SI | Edad Gestacional |
| Q11ObsDR | varchar |  | FK | SI | Edad Gestacional DR |
| Q12 | varchar |  |  | SI | Peso (kg) |
| Q12ObsDR | varchar |  | FK | SI | Peso (kg) DR |
| Q13 | varchar |  |  | SI | Talla (cms.) |
| Q13ObsDR | varchar |  | FK | SI | Talla (cms.) DR |
| Q14 | varchar |  |  | SI | Estado nutricional |
| Q14ObsDR | varchar |  | FK | SI | Estado nutricional DR |
| Q15 | varchar |  |  | SI | Incremento mes siguiente |
| Q15ObsDR | varchar |  | FK | SI | Incremento mes siguiente DR |
| Q16 | varchar |  |  | SI | Presión Sistólica (mmHg) |
| Q16ObsDR | varchar |  | FK | SI | Presión Sistólica (mmHg) DR |
| Q17 | varchar |  |  | SI | Presión Diastólica (mmHg) OLD |
| Q17ObsDR | varchar |  | FK | SI | Presión Diastólica (mmHg) OLD DR |
| Q18 | varchar |  |  | SI | Altura Uterina (cms.) |
| Q18ObsDR | varchar |  | FK | SI | Altura Uterina (cms.) DR |
| Q19 | varchar |  |  | SI | Latidos cardiofetales Feto 1 (lpm) |
| Q19ObsDR | varchar |  | FK | SI | Latidos cardiofetales Feto 1 (lpm) DR |
| Q20 | varchar |  |  | SI | Latidos cardiofetales Feto 2 (lpm) |
| Q20ObsDR | varchar |  | FK | SI | Latidos cardiofetales Feto 2 (lpm) DR |
| Q21 | varchar |  |  | SI | Latidos cardiofetales Feto 3 (lpm) |
| Q21ObsDR | varchar |  | FK | SI | Latidos cardiofetales Feto 3 (lpm) DR |
| Q22 | varchar |  |  | SI | Peso estimado Feto 1 |
| Q22ObsDR | varchar |  | FK | SI | Peso estimado Feto 1 DR |
| Q23 | numeric |  |  | SI | Peso estimado Feto 2 |
| Q24 | numeric |  |  | SI | Peso estimado Feto 3 |
| Q25 | varchar |  |  | SI | Presentación |
| Q25ObsDR | varchar |  | FK | SI | Presentación DR |
| Q26 | varchar |  |  | SI | Morbilidad |
| Q26ObsDR | varchar |  | FK | SI | Morbilidad DR |
| Q27 | varchar |  |  | SI | Morbilidad |
| Q27ObsDR | varchar |  | FK | SI | Morbilidad DR |
| Q28 | varchar |  |  | SI | Edema |
| Q28ObsDR | varchar |  | FK | SI | Edema DR |
| Q29 | varchar |  |  | SI | Consejería |
| Q29ObsDR | varchar |  | FK | SI | Consejería DR |
| Q30 | varchar |  |  | SI | Acompañante |
| Q30ObsDR | varchar |  | FK | SI | Acompañante DR |
| Q31 | varchar |  |  | SI | Nombre del Profesional |
| Q32 | varchar |  |  | SI | Tipo de Profesional |
| Q33 | varchar |  |  | SI | Tabaquismo |
| Q34 | varchar |  |  | SI | Grupo RH |
| Q35 | varchar |  |  | SI | Complicaciones Prenatales al ingreso |
| Q36 | varchar |  |  | SI | Fecha probable de parto |
| Q37 | bigint |  |  | SI | Ingreso C. Prenatal |
| Q37TxtOnly | bigint |  |  | SI | Ingreso C. Prenatal Plain Text Only |
| Q38 | varchar |  |  | SI | Tipo de Control  |
| Q38ObsDR | varchar |  | FK | SI | Tipo de Control  DR |
| Q39 | varchar |  |  | SI | Observaciones Ecografía |
| Q40 | date |  |  | SI | Fecha de Control |
| Q41 | varchar |  |  | SI | Curva Peso |
| Q42 | varchar |  |  | SI | Presión Diastólica (mmHg)  |
| Q42ObsDR | varchar |  | FK | SI | Presión Diastólica (mmHg)  DR |
| Q43 | varchar |  |  | SI | FUR |
| Q44 | varchar |  |  | SI | Edad Gestacional |
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