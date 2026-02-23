# SQLUser.LBC_BPRulePatientEpisodeBPGroup

**Schema:** SQLUser
**Columnas:** 191
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPRPEBPG_ParRef | varchar | PK |  | NO | Parent Blood-Product Rule Episode Details DR |
| LBCBPRPEBPG_BloodProductGroup_DR | bigint |  | FK | NO | Blood Product Group |
| LBCBPRPEBPG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBPRPEBPG_DateTo | date |  |  | SI | Last day the record is active |
| LBCBPRPEBPG_Desc | varchar |  |  | SI | Rule Description |
| LBCBPRPEBPG_FullDesc | longvarchar |  |  | SI | Full Description |
| LBCBPRPEBPG_RowID | varchar |  |  | NO | - |
| LBCBPRPEBPG_Sequence | numeric |  |  | SI | Priority  Sequence |
| Q01 | - |  |  | SI | Realiza Control Prenatal |
| Q02 | - |  |  | SI | Fecha Primer Control |
| Q03 | - |  |  | SI | Flujo Vaginal |
| Q03ObsDR | - |  |  | SI | Flujo Vaginal DR |
| Q04 | - |  |  | SI | Líquido  Amniótico |
| Q04ObsDR | - |  |  | SI | Líquido  Amniótico DR |
| Q05 | - |  |  | SI | Fecha Último Control |
| Q06 | - |  |  | SI | Membranas |
| Q06ObsDR | - |  |  | SI | Membranas DR |
| Q07 | - |  |  | SI | Control ARO |
| Q08 | - |  |  | SI | Comentarios |
| Q09 | - |  |  | SI | Temperatura Axilar (C°) |
| Q09ObsDR | - |  |  | SI | Temperatura Axilar (C°) DR |
| Q10 | - |  |  | SI | Temperatura Rectal (C°) |
| Q10ObsDR | - |  |  | SI | Temperatura Rectal (C°) DR |
| Q11 | - |  |  | SI | Edad Gestacional (Sem.) |
| Q11ObsDR | - |  |  | SI | Edad Gestacional (Sem.) DR |
| Q12 | - |  |  | SI | Peso (kg) |
| Q12ObsDR | - |  |  | SI | Peso (kg) DR |
| Q13 | - |  |  | SI | Talla (cms.) |
| Q13ObsDR | - |  |  | SI | Talla (cms.) DR |
| Q14 | - |  |  | SI | Estado nutricional |
| Q14ObsDR | - |  |  | SI | Estado nutricional DR |
| Q15 | - |  |  | SI | Incremento mes siguiente |
| Q15ObsDR | - |  |  | SI | Incremento mes siguiente DR |
| Q16 | - |  |  | SI | Presión Sistólica (mmHg) |
| Q16ObsDR | - |  |  | SI | Presión Sistólica (mmHg) DR |
| Q17 | - |  |  | SI | Presión Diastólica (mmHg) |
| Q17ObsDR | - |  |  | SI | Presión Diastólica (mmHg) DR |
| Q18 | - |  |  | SI | Altura Uterina (cms.) |
| Q18ObsDR | - |  |  | SI | Altura Uterina (cms.) DR |
| Q19 | - |  |  | SI | Latidos cardiofetales Feto 1 (lpm) |
| Q19ObsDR | - |  |  | SI | Latidos cardiofetales Feto 1 (lpm) DR |
| Q20 | - |  |  | SI | Latidos cardiofetales Feto 2 (lpm) |
| Q20ObsDR | - |  |  | SI | Latidos cardiofetales Feto 2 (lpm) DR |
| Q21 | - |  |  | SI | Latidos cardiofetales Feto 3 (lpm) |
| Q21ObsDR | - |  |  | SI | Latidos cardiofetales Feto 3 (lpm) DR |
| Q22 | - |  |  | SI | Peso estimado Feto 1 |
| Q22ObsDR | - |  |  | SI | Peso estimado Feto 1 DR |
| Q23 | - |  |  | SI | Peso estimado Feto 2 |
| Q24 | - |  |  | SI | Peso estimado Feto 3 |
| Q25 | - |  |  | SI | Presentación |
| Q25ObsDR | - |  |  | SI | Presentación DR |
| Q26 | - |  |  | SI | Morbilidad |
| Q26ObsDR | - |  |  | SI | Morbilidad DR |
| Q27 | - |  |  | SI | Consistencia Cuello |
| Q27ObsDR | - |  |  | SI | Consistencia Cuello DR |
| Q28 | - |  |  | SI | Edema |
| Q28ObsDR | - |  |  | SI | Edema DR |
| Q29 | - |  |  | SI | Consejería |
| Q29ObsDR | - |  |  | SI | Consejería DR |
| Q30 | - |  |  | SI | Acompañante |
| Q30ObsDR | - |  |  | SI | Acompañante DR |
| Q31 | - |  |  | SI | Nombre del Profesional |
| Q32 | - |  |  | SI | Posición |
| Q32ObsDR | - |  |  | SI | Posición DR |
| Q33 | - |  |  | SI | Tabaquismo |
| Q34 | - |  |  | SI | Borramiento |
| Q34ObsDR | - |  |  | SI | Borramiento DR |
| Q35 | - |  |  | SI | Complicaciones Prenatales al ingreso |
| Q36 | - |  |  | SI | Fecha probable de parto |
| Q37 | - |  |  | SI | Ingreso C. Prenatal |
| Q37TxtOnly | - |  |  | SI | Ingreso C. Prenatal Plain Text Only |
| Q38 | - |  |  | SI | Tipo de Control |
| Q38ObsDR | - |  |  | SI | Tipo de Control  DR |
| Q39 | - |  |  | SI | Observaciones Ecografía |
| Q40 | - |  |  | SI | Fecha de Control |
| Q41 | - |  |  | SI | Curva Peso |
| Q42 | - |  |  | SI | Tono Uterino |
| Q42ObsDR | - |  |  | SI | Tono Uterino DR |
| Q43 | - |  |  | SI | Dinámica Uterina |
| Q43ObsDR | - |  |  | SI | Dinámica Uterina DR |
| Q44 | - |  |  | SI | Contracciones (Cada 10 Min) |
| Q44ObsDR | - |  |  | SI | Contracciones (Cada 10 Min) DR |
| Q45 | - |  |  | SI | Dilatación Cervical |
| Q45ObsDR | - |  |  | SI | Dilatación Cervical DR |
| Q46 | - |  |  | SI | Apoyo Cefálico |
| Q46ObsDR | - |  |  | SI | Apoyo Cefálico DR |
| Q47 | - |  |  | SI | Movimientos Feto 1 |
| Q47ObsDR | - |  |  | SI | Movimientos Feto 1 DR |
| Q48 | - |  |  | SI | Presentación Feto 1 |
| Q48ObsDR | - |  |  | SI | Presentación Feto 1 DR |
| Q49 | - |  |  | SI | Dorso Feto 1 |
| Q49ObsDR | - |  |  | SI | Dorso Feto 1 DR |
| Q50 | - |  |  | SI | Plano de Hodge Feto 1 |
| Q50ObsDR | - |  |  | SI | Plano de Hodge Feto 1 DR |
| Q51 | - |  |  | SI | Desaceleraciones Feto 1 |
| Q51ObsDR | - |  |  | SI | Desaceleraciones Feto 1 DR |
| Q52 | - |  |  | SI | LCF Feto 4 |
| Q52ObsDR | - |  |  | SI | LCF Feto 4 DR |
| Q53 | - |  |  | SI | Estimación Peso Feto 2 |
| Q53ObsDR | - |  |  | SI | Estimación Peso Feto 2 DR |
| Q54 | - |  |  | SI | Estimación Peso Feto 3 |
| Q54ObsDR | - |  |  | SI | Estimación Peso Feto 3 DR |
| Q55 | - |  |  | SI | Estimación Peso Feto 4 |
| Q55ObsDR | - |  |  | SI | Estimación Peso Feto 4 DR |
| Q56 | - |  |  | SI | Movimientos Feto 2 |
| Q56ObsDR | - |  |  | SI | Movimientos Feto 2 DR |
| Q57 | - |  |  | SI | Movimientos Feto 3 |
| Q57ObsDR | - |  |  | SI | Movimientos Feto 3 DR |
| Q58 | - |  |  | SI | Movimientos Feto 4 |
| Q58ObsDR | - |  |  | SI | Movimientos Feto 4 DR |
| Q59 | - |  |  | SI | Presentación Feto 2 |
| Q59ObsDR | - |  |  | SI | Presentación Feto 2 DR |
| Q60 | - |  |  | SI | Presentación Feto 3 |
| Q60ObsDR | - |  |  | SI | Presentación Feto 3 DR |
| Q61 | - |  |  | SI | Presentación Feto 4 |
| Q61ObsDR | - |  |  | SI | Presentación Feto 4 DR |
| Q62 | - |  |  | SI | Dorso Feto 2 |
| Q62ObsDR | - |  |  | SI | Dorso Feto 2 DR |
| Q63 | - |  |  | SI | Dorso Feto 3 |
| Q63ObsDR | - |  |  | SI | Dorso Feto 3 DR |
| Q64 | - |  |  | SI | Dorso Feto 4 |
| Q64ObsDR | - |  |  | SI | Dorso Feto 4 DR |
| Q65 | - |  |  | SI | Plano de Hodge Feto 2 |
| Q65ObsDR | - |  |  | SI | Plano de Hodge Feto 2 DR |
| Q66 | - |  |  | SI | Plano de Hodge Feto 3 |
| Q66ObsDR | - |  |  | SI | Plano de Hodge Feto 3 DR |
| Q67 | - |  |  | SI | Plano de Hodge Feto 4 |
| Q67ObsDR | - |  |  | SI | Plano de Hodge Feto 4 DR |
| Q68 | - |  |  | SI | Desaceleraciones Feto 2 |
| Q68ObsDR | - |  |  | SI | Desaceleraciones Feto 2 DR |
| Q69 | - |  |  | SI | Desaceleraciones Feto 3 |
| Q69ObsDR | - |  |  | SI | Desaceleraciones Feto 3 DR |
| Q70 | - |  |  | SI | Desaceleraciones Feto 4 |
| Q70ObsDR | - |  |  | SI | Desaceleraciones Feto 4 DR |
| Q71 | - |  |  | SI | Comentarios/Observaciones |
| Q72 | - |  |  | SI | RBNE |
| Q72ObsDR | - |  |  | SI | RBNE DR |
| Q73 | - |  |  | SI | RE/TTCE |
| Q73ObsDR | - |  |  | SI | RE/TTCE DR |
| Q74 | - |  |  | SI | Pelvis |
| Q75 | - |  |  | SI | Pelvis |
| Q75ObsDR | - |  |  | SI | Pelvis DR |
| Q76 | - |  |  | SI | Comentarios |
| Q76ObsDR | - |  |  | SI | Comentarios DR |
| Q77 | - |  |  | SI | Observaciones Generales |
| Q77ObsDR | - |  |  | SI | Observaciones Generales DR |
| Q78 | - |  |  | SI | Anamnesis |
| Q79 | - |  |  | SI | Observaciones Generales |
| Q80 | - |  |  | SI | FUR |
| Q81 | - |  |  | SI | Edad Gestacional |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*