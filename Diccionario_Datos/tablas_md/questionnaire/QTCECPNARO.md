# questionnaire.QTCECPNARO

> Controles Prenatales ARO

**Schema:** questionnaire
**Columnas:** 183
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Controles Prenatales ARO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Realiza Control Prenatal |
| Q02 | date |  |  | SI | Fecha Primer Control |
| Q03 | varchar |  |  | SI | Flujo Vaginal |
| Q03ObsDR | varchar |  | FK | SI | Flujo Vaginal DR |
| Q04 | varchar |  |  | SI | Líquido  Amniótico |
| Q04ObsDR | varchar |  | FK | SI | Líquido  Amniótico DR |
| Q05 | date |  |  | SI | Fecha Último Control  |
| Q06 | varchar |  |  | SI | Membranas |
| Q06ObsDR | varchar |  | FK | SI | Membranas DR |
| Q07 | varchar |  |  | SI | Control ARO |
| Q08 | varchar |  |  | SI | Comentarios |
| Q09 | varchar |  |  | SI | Temperatura Axilar (C°) |
| Q09ObsDR | varchar |  | FK | SI | Temperatura Axilar (C°) DR |
| Q10 | varchar |  |  | SI | Temperatura Rectal (C°) |
| Q10ObsDR | varchar |  | FK | SI | Temperatura Rectal (C°) DR |
| Q11 | varchar |  |  | SI | Edad Gestacional (Sem.) |
| Q11ObsDR | varchar |  | FK | SI | Edad Gestacional (Sem.) DR |
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
| Q17 | varchar |  |  | SI | Presión Diastólica (mmHg) |
| Q17ObsDR | varchar |  | FK | SI | Presión Diastólica (mmHg) DR |
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
| Q27 | varchar |  |  | SI | Consistencia Cuello |
| Q27ObsDR | varchar |  | FK | SI | Consistencia Cuello DR |
| Q28 | varchar |  |  | SI | Edema |
| Q28ObsDR | varchar |  | FK | SI | Edema DR |
| Q29 | varchar |  |  | SI | Consejería |
| Q29ObsDR | varchar |  | FK | SI | Consejería DR |
| Q30 | varchar |  |  | SI | Acompañante |
| Q30ObsDR | varchar |  | FK | SI | Acompañante DR |
| Q31 | varchar |  |  | SI | Nombre del Profesional |
| Q32 | varchar |  |  | SI | Posición |
| Q32ObsDR | varchar |  | FK | SI | Posición DR |
| Q33 | varchar |  |  | SI | Tabaquismo |
| Q34 | varchar |  |  | SI | Borramiento |
| Q34ObsDR | varchar |  | FK | SI | Borramiento DR |
| Q35 | varchar |  |  | SI | Complicaciones Prenatales al ingreso |
| Q36 | varchar |  |  | SI | Fecha probable de parto |
| Q37 | bigint |  |  | SI | Ingreso C. Prenatal |
| Q37TxtOnly | bigint |  |  | SI | Ingreso C. Prenatal Plain Text Only |
| Q38 | varchar |  |  | SI | Tipo de Control  |
| Q38ObsDR | varchar |  | FK | SI | Tipo de Control  DR |
| Q39 | varchar |  |  | SI | Observaciones Ecografía |
| Q40 | date |  |  | SI | Fecha de Control |
| Q41 | varchar |  |  | SI | Curva Peso |
| Q42 | varchar |  |  | SI | Tono Uterino |
| Q42ObsDR | varchar |  | FK | SI | Tono Uterino DR |
| Q43 | varchar |  |  | SI | Dinámica Uterina |
| Q43ObsDR | varchar |  | FK | SI | Dinámica Uterina DR |
| Q44 | varchar |  |  | SI | Contracciones (Cada 10 Min) |
| Q44ObsDR | varchar |  | FK | SI | Contracciones (Cada 10 Min) DR |
| Q45 | varchar |  |  | SI | Dilatación Cervical |
| Q45ObsDR | varchar |  | FK | SI | Dilatación Cervical DR |
| Q46 | varchar |  |  | SI | Apoyo Cefálico |
| Q46ObsDR | varchar |  | FK | SI | Apoyo Cefálico DR |
| Q47 | varchar |  |  | SI | Movimientos Feto 1 |
| Q47ObsDR | varchar |  | FK | SI | Movimientos Feto 1 DR |
| Q48 | varchar |  |  | SI | Presentación Feto 1 |
| Q48ObsDR | varchar |  | FK | SI | Presentación Feto 1 DR |
| Q49 | varchar |  |  | SI | Dorso Feto 1 |
| Q49ObsDR | varchar |  | FK | SI | Dorso Feto 1 DR |
| Q50 | varchar |  |  | SI | Plano de Hodge Feto 1 |
| Q50ObsDR | varchar |  | FK | SI | Plano de Hodge Feto 1 DR |
| Q51 | varchar |  |  | SI | Desaceleraciones Feto 1 |
| Q51ObsDR | varchar |  | FK | SI | Desaceleraciones Feto 1 DR |
| Q52 | varchar |  |  | SI | LCF Feto 4 |
| Q52ObsDR | varchar |  | FK | SI | LCF Feto 4 DR |
| Q53 | varchar |  |  | SI | Estimación Peso Feto 2 |
| Q53ObsDR | varchar |  | FK | SI | Estimación Peso Feto 2 DR |
| Q54 | varchar |  |  | SI | Estimación Peso Feto 3 |
| Q54ObsDR | varchar |  | FK | SI | Estimación Peso Feto 3 DR |
| Q55 | varchar |  |  | SI | Estimación Peso Feto 4 |
| Q55ObsDR | varchar |  | FK | SI | Estimación Peso Feto 4 DR |
| Q56 | varchar |  |  | SI | Movimientos Feto 2 |
| Q56ObsDR | varchar |  | FK | SI | Movimientos Feto 2 DR |
| Q57 | varchar |  |  | SI | Movimientos Feto 3 |
| Q57ObsDR | varchar |  | FK | SI | Movimientos Feto 3 DR |
| Q58 | varchar |  |  | SI | Movimientos Feto 4 |
| Q58ObsDR | varchar |  | FK | SI | Movimientos Feto 4 DR |
| Q59 | varchar |  |  | SI | Presentación Feto 2 |
| Q59ObsDR | varchar |  | FK | SI | Presentación Feto 2 DR |
| Q60 | varchar |  |  | SI | Presentación Feto 3 |
| Q60ObsDR | varchar |  | FK | SI | Presentación Feto 3 DR |
| Q61 | varchar |  |  | SI | Presentación Feto 4 |
| Q61ObsDR | varchar |  | FK | SI | Presentación Feto 4 DR |
| Q62 | varchar |  |  | SI | Dorso Feto 2 |
| Q62ObsDR | varchar |  | FK | SI | Dorso Feto 2 DR |
| Q63 | varchar |  |  | SI | Dorso Feto 3 |
| Q63ObsDR | varchar |  | FK | SI | Dorso Feto 3 DR |
| Q64 | varchar |  |  | SI | Dorso Feto 4 |
| Q64ObsDR | varchar |  | FK | SI | Dorso Feto 4 DR |
| Q65 | varchar |  |  | SI | Plano de Hodge Feto 2 |
| Q65ObsDR | varchar |  | FK | SI | Plano de Hodge Feto 2 DR |
| Q66 | varchar |  |  | SI | Plano de Hodge Feto 3 |
| Q66ObsDR | varchar |  | FK | SI | Plano de Hodge Feto 3 DR |
| Q67 | varchar |  |  | SI | Plano de Hodge Feto 4 |
| Q67ObsDR | varchar |  | FK | SI | Plano de Hodge Feto 4 DR |
| Q68 | varchar |  |  | SI | Desaceleraciones Feto 2 |
| Q68ObsDR | varchar |  | FK | SI | Desaceleraciones Feto 2 DR |
| Q69 | varchar |  |  | SI | Desaceleraciones Feto 3 |
| Q69ObsDR | varchar |  | FK | SI | Desaceleraciones Feto 3 DR |
| Q70 | varchar |  |  | SI | Desaceleraciones Feto 4 |
| Q70ObsDR | varchar |  | FK | SI | Desaceleraciones Feto 4 DR |
| Q71 | varchar |  |  | SI | Comentarios/Observaciones |
| Q72 | varchar |  |  | SI | RBNE |
| Q72ObsDR | varchar |  | FK | SI | RBNE DR |
| Q73 | varchar |  |  | SI | RE/TTCE |
| Q73ObsDR | varchar |  | FK | SI | RE/TTCE DR |
| Q74 | varchar |  |  | SI | Pelvis |
| Q75 | varchar |  |  | SI | Pelvis |
| Q75ObsDR | varchar |  | FK | SI | Pelvis DR |
| Q76 | varchar |  |  | SI | Comentarios |
| Q76ObsDR | varchar |  | FK | SI | Comentarios DR |
| Q77 | varchar |  |  | SI | Observaciones Generales |
| Q77ObsDR | varchar |  | FK | SI | Observaciones Generales DR |
| Q78 | varchar |  |  | SI | Anamnesis |
| Q79 | varchar |  |  | SI | Observaciones Generales |
| Q80 | varchar |  |  | SI | FUR |
| Q81 | varchar |  |  | SI | Edad Gestacional |
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