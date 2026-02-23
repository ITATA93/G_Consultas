# SQLUser.LBC_BPRulePatientEpisode

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPRPE_ParRef | bigint | PK |  | NO | Parent Blood-Product Rule Patient DR |
| LBCBPRPE_AgeFrom | double |  |  | SI | Age From |
| LBCBPRPE_AgeTo | double |  |  | SI | Age To |
| LBCBPRPE_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition |
| LBCBPRPE_DOB | date |  |  | SI | Date of Birth |
| LBCBPRPE_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBPRPE_DateTo | date |  |  | SI | Last day the record is active |
| LBCBPRPE_Desc | varchar |  |  | SI | Rule Description |
| LBCBPRPE_FullDesc | longvarchar |  |  | SI | Full Description
HTMLRRichText |
| LBCBPRPE_Operator | varchar |  |  | SI | Operator |
| LBCBPRPE_Pregnant | varchar |  |  | SI | Pregnant |
| LBCBPRPE_RowID | varchar |  |  | NO | - |
| LBCBPRPE_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCBPRPE_TestSetPriority_DR | bigint |  | FK | SI | Test Set Priority |
| LBCBPRPE_WeeksPregnantFrom | double |  |  | SI | Weeks Pregnant From |
| LBCBPRPE_WeeksPregnantTo | double |  |  | SI | Weeks Pregnant To |
| Q01 | - |  |  | SI | Realiza Control Prenatal |
| Q02 | - |  |  | SI | Fecha Primer Control |
| Q03 | - |  |  | SI | Edad Gestacional |
| Q03ObsDR | - |  |  | SI | Edad Gestacional DR |
| Q04 | - |  |  | SI | Peso (kg) |
| Q04ObsDR | - |  |  | SI | Peso (kg) DR |
| Q05 | - |  |  | SI | Fecha Último Control |
| Q06 | - |  |  | SI | Edad Gestacional |
| Q07 | - |  |  | SI | Control ARO |
| Q08 | - |  |  | SI | Comentarios |
| Q09 | - |  |  | SI | Temperatura Axilar (C°) |
| Q09ObsDR | - |  |  | SI | Temperatura Axilar (C°) DR |
| Q10 | - |  |  | SI | Temperatura Rectal (C°) |
| Q10ObsDR | - |  |  | SI | Temperatura Rectal (C°) DR |
| Q11 | - |  |  | SI | Edad Gestacional |
| Q11ObsDR | - |  |  | SI | Edad Gestacional DR |
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
| Q17 | - |  |  | SI | Presión Diastólica (mmHg) OLD |
| Q17ObsDR | - |  |  | SI | Presión Diastólica (mmHg) OLD DR |
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
| Q27 | - |  |  | SI | Morbilidad |
| Q27ObsDR | - |  |  | SI | Morbilidad DR |
| Q28 | - |  |  | SI | Edema |
| Q28ObsDR | - |  |  | SI | Edema DR |
| Q29 | - |  |  | SI | Consejería |
| Q29ObsDR | - |  |  | SI | Consejería DR |
| Q30 | - |  |  | SI | Acompañante |
| Q30ObsDR | - |  |  | SI | Acompañante DR |
| Q31 | - |  |  | SI | Nombre del Profesional |
| Q32 | - |  |  | SI | Tipo de Profesional |
| Q33 | - |  |  | SI | Tabaquismo |
| Q34 | - |  |  | SI | Grupo RH |
| Q35 | - |  |  | SI | Complicaciones Prenatales al ingreso |
| Q36 | - |  |  | SI | Fecha probable de parto |
| Q37 | - |  |  | SI | Ingreso C. Prenatal |
| Q37TxtOnly | - |  |  | SI | Ingreso C. Prenatal Plain Text Only |
| Q38 | - |  |  | SI | Tipo de Control |
| Q38ObsDR | - |  |  | SI | Tipo de Control  DR |
| Q39 | - |  |  | SI | Observaciones Ecografía |
| Q40 | - |  |  | SI | Fecha de Control |
| Q41 | - |  |  | SI | Curva Peso |
| Q42 | - |  |  | SI | Presión Diastólica (mmHg) |
| Q42ObsDR | - |  |  | SI | Presión Diastólica (mmHg)  DR |
| Q43 | - |  |  | SI | FUR |
| Q44 | - |  |  | SI | Edad Gestacional |
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