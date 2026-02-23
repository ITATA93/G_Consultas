# questionnaire.QTCENUTCA4

> FORMULARIO DE INGRESO ADULTO

**Schema:** questionnaire
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* FORMULARIO DE INGRESO ADULTO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Peso Actual |
| Q02 | varchar |  |  | SI | Peso Mínimo (-64) |
| Q03 | varchar |  |  | SI | Peso Máximo (-64) |
| Q04 | varchar |  |  | SI | Peso Ideal (-64 |
| Q05 | numeric |  |  | SI | Talla |
| Q06 | varchar |  |  | SI | Clasificacion |
| Q07 | varchar |  |  | SI | Adulto mayor 64 años |
| Q08 | varchar |  |  | SI | Peso Mínimo (+64) |
| Q09 | varchar |  |  | SI | Peso Máximo (+64) |
| Q10 | varchar |  |  | SI | Peso Ideal (-64) |
| Q11 | varchar |  |  | SI | I.M.C |
| Q12 | varchar |  |  | SI | C.N |
| Q13 | varchar |  |  | SI | Hipótesis Diagnóstico Médico |
| Q14 | varchar |  |  | SI | Problemas en relación a la ingesta de alimentos |
| Q15 | varchar |  |  | SI | Indicaciones Dietéticas Médicas |
| Q16 | varchar |  |  | SI | Tasa Metabólica Basal (T.A.B) |
| Q17 | numeric |  |  | SI | F. Act |
| Q18 | numeric |  |  | SI | F. Pat. |
| Q19 | numeric |  |  | SI | Hombre 18-30 años (01) |
| Q20 | numeric |  |  | SI | Hombre 18-30 años (02) |
| Q21 | numeric |  |  | SI | Hombre 18-30 años (03) |
| Q22 | numeric |  |  | SI | Hombre 30-60 años (01) |
| Q23 | numeric |  |  | SI | Hombre 30-60 años (02) |
| Q24 | numeric |  |  | SI | Hombre 60 y mas (01) |
| Q25 | numeric |  |  | SI | Hombre 60 y mas (02) |
| Q26 | numeric |  |  | SI | Hombre 60 y mas (03) |
| Q27 | varchar |  |  | SI | Calorias H 18-30 |
| Q28 | varchar |  |  | SI | Proteinas H. 18-30 |
| Q29 | varchar |  |  | SI | H.De.C  H. 18-30 |
| Q30 | varchar |  |  | SI | Lipidos  H. 18-30 |
| Q31 | varchar |  |  | SI | Calorias H. 30-60 |
| Q32 | varchar |  |  | SI | Proteinas H. 30-60  |
| Q33 | varchar |  |  | SI | H.De.C H. 30-60 |
| Q34 | varchar |  |  | SI | Lipidos H. 30-60 |
| Q35 | varchar |  |  | SI | Calorias H. 60 y mas |
| Q36 | varchar |  |  | SI | Proteinas H. 60 y mas |
| Q37 | varchar |  |  | SI | H.De.C H. 60 y mas |
| Q38 | varchar |  |  | SI | Lipidos H. 60 y mas |
| Q39 | varchar |  |  | SI | H / 18-30 AÑOS |
| Q40 | varchar |  |  | SI | H / 30-60 AÑOS |
| Q41 | varchar |  |  | SI | H / 60 Y MAS |
| Q42 | varchar |  |  | SI | M / 18-30 AÑOS |
| Q43 | varchar |  |  | SI | M / 30-60 AÑOS |
| Q44 | varchar |  |  | SI | M / 60 Y MAS |
| Q45 | varchar |  |  | SI | Calorias M 18-30 |
| Q46 | varchar |  |  | SI | Proteinas M 18-30 |
| Q47 | varchar |  |  | SI | H.De.C M 18-30 |
| Q48 | varchar |  |  | SI | Lipidos M 18-30 |
| Q49 | varchar |  |  | SI | Peso |
| Q49ObsDR | varchar |  | FK | SI | Peso DR |
| Q50 | varchar |  |  | SI | Talla |
| Q50ObsDR | varchar |  | FK | SI | Talla DR |
| Q51 | varchar |  |  | SI | IMC |
| Q51ObsDR | varchar |  | FK | SI | IMC DR |
| Q52 | varchar |  |  | SI | Talla Transversal |
| Q52ObsDR | varchar |  | FK | SI | Talla Transversal DR |
| Q53 | numeric |  |  | SI | Peso 2 |
| Q54 | varchar |  |  | SI | OBS |
| Q55 | varchar |  |  | SI | Hipótesis Diagnóstico Médico 2 |
| Q57 | varchar |  |  | SI | Menor de 64 Años |
| Q58 | varchar |  |  | SI | Mayor de 64 Años |
| Q59 | varchar |  |  | SI | Peso Ideal 18/30 |
| Q60 | varchar |  |  | SI | Peso Ideal 30/60 |
| Q61 | varchar |  |  | SI | Peso Ideal 60 y mas |
| Q62 | numeric |  |  | SI | % Proteina  |
| Q63 | numeric |  |  | SI | % H. De. C |
| Q64 | numeric |  |  | SI | % Lipidos |
| Q65 | varchar |  |  | SI | Calorias M  30-60 |
| Q66 | varchar |  |  | SI | Calorias M 60 y mas |
| Q67 | varchar |  |  | SI | Proteinas M 30/60 |
| Q68 | varchar |  |  | SI | H.De.C M 30-60 |
| Q69 | varchar |  |  | SI | Lipidos M 30/60 |
| Q70 | varchar |  |  | SI | Proteinas M 60 y mas |
| Q71 | varchar |  |  | SI | H.De.C M 60 y mas |
| Q72 | varchar |  |  | SI | Lipidos M 60 y mas |
| Q73 | varchar |  |  | SI | Tipo de Ingreso |
| Q74 | varchar |  |  | SI | Peso Transversal |
| Q74ObsDR | varchar |  | FK | SI | Peso Transversal DR |
| Q75 | varchar |  |  | SI | CALORIAS |
| Q76 | varchar |  |  | SI | PROTEINAS |
| Q77 | varchar |  |  | SI | HIDRATO DE CARBONO |
| Q78 | varchar |  |  | SI | LIPIDOS |
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