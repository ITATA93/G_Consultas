# SQLUser.LBC_SpecimenGroupItem

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPGI_ParRef | bigint | PK |  | NO | Parent SpecimenGroup DR |
| ChildQ56DR | - |  |  | SI | Child Reference: Lista Hipótesis Diagnóstico |
| LBCSPGI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPGI_RowID | varchar |  |  | NO | - |
| LBCSPGI_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| Q01 | - |  |  | SI | Peso Actual |
| Q02 | - |  |  | SI | Peso Mínimo (-64) |
| Q03 | - |  |  | SI | Peso Máximo (-64) |
| Q04 | - |  |  | SI | Peso Ideal (-64 |
| Q05 | - |  |  | SI | Talla |
| Q06 | - |  |  | SI | Clasificacion |
| Q07 | - |  |  | SI | Adulto mayor 64 años |
| Q08 | - |  |  | SI | Peso Mínimo (+64) |
| Q09 | - |  |  | SI | Peso Máximo (+64) |
| Q10 | - |  |  | SI | Peso Ideal (-64) |
| Q11 | - |  |  | SI | I.M.C |
| Q12 | - |  |  | SI | C.N |
| Q13 | - |  |  | SI | Hipótesis Diagnóstico Médico |
| Q14 | - |  |  | SI | Problemas en relación a la ingesta de alimentos |
| Q15 | - |  |  | SI | Indicaciones Dietéticas Médicas |
| Q16 | - |  |  | SI | Tasa Metabólica Basal (T.A.B) |
| Q17 | - |  |  | SI | F. Act |
| Q18 | - |  |  | SI | F. Pat. |
| Q19 | - |  |  | SI | Hombre 18-30 años (01) |
| Q20 | - |  |  | SI | Hombre 18-30 años (02) |
| Q21 | - |  |  | SI | Hombre 18-30 años (03) |
| Q22 | - |  |  | SI | Hombre 30-60 años (01) |
| Q23 | - |  |  | SI | Hombre 30-60 años (02) |
| Q24 | - |  |  | SI | Hombre 60 y mas (01) |
| Q25 | - |  |  | SI | Hombre 60 y mas (02) |
| Q26 | - |  |  | SI | Hombre 60 y mas (03) |
| Q27 | - |  |  | SI | Calorias H 18-30 |
| Q28 | - |  |  | SI | Proteinas H. 18-30 |
| Q29 | - |  |  | SI | H.De.C  H. 18-30 |
| Q30 | - |  |  | SI | Lipidos  H. 18-30 |
| Q31 | - |  |  | SI | Calorias H. 30-60 |
| Q32 | - |  |  | SI | Proteinas H. 30-60 |
| Q33 | - |  |  | SI | H.De.C H. 30-60 |
| Q34 | - |  |  | SI | Lipidos H. 30-60 |
| Q35 | - |  |  | SI | Calorias H. 60 y mas |
| Q36 | - |  |  | SI | Proteinas H. 60 y mas |
| Q37 | - |  |  | SI | H.De.C H. 60 y mas |
| Q38 | - |  |  | SI | Lipidos H. 60 y mas |
| Q39 | - |  |  | SI | H / 18-30 AÑOS |
| Q40 | - |  |  | SI | H / 30-60 AÑOS |
| Q41 | - |  |  | SI | H / 60 Y MAS |
| Q42 | - |  |  | SI | M / 18-30 AÑOS |
| Q43 | - |  |  | SI | M / 30-60 AÑOS |
| Q44 | - |  |  | SI | M / 60 Y MAS |
| Q45 | - |  |  | SI | Calorias M 18-30 |
| Q46 | - |  |  | SI | Proteinas M 18-30 |
| Q47 | - |  |  | SI | H.De.C M 18-30 |
| Q48 | - |  |  | SI | Lipidos M 18-30 |
| Q49 | - |  |  | SI | Peso |
| Q49ObsDR | - |  |  | SI | Peso DR |
| Q50 | - |  |  | SI | Talla |
| Q50ObsDR | - |  |  | SI | Talla DR |
| Q51 | - |  |  | SI | IMC |
| Q51ObsDR | - |  |  | SI | IMC DR |
| Q52 | - |  |  | SI | Talla Transversal |
| Q52ObsDR | - |  |  | SI | Talla Transversal DR |
| Q53 | - |  |  | SI | Peso 2 |
| Q54 | - |  |  | SI | OBS |
| Q55 | - |  |  | SI | Hipótesis Diagnóstico Médico 2 |
| Q57 | - |  |  | SI | Menor de 64 Años |
| Q58 | - |  |  | SI | Mayor de 64 Años |
| Q59 | - |  |  | SI | Peso Ideal 18/30 |
| Q60 | - |  |  | SI | Peso Ideal 30/60 |
| Q61 | - |  |  | SI | Peso Ideal 60 y mas |
| Q62 | - |  |  | SI | % Proteina |
| Q63 | - |  |  | SI | % H. De. C |
| Q64 | - |  |  | SI | % Lipidos |
| Q65 | - |  |  | SI | Calorias M  30-60 |
| Q66 | - |  |  | SI | Calorias M 60 y mas |
| Q67 | - |  |  | SI | Proteinas M 30/60 |
| Q68 | - |  |  | SI | H.De.C M 30-60 |
| Q69 | - |  |  | SI | Lipidos M 30/60 |
| Q70 | - |  |  | SI | Proteinas M 60 y mas |
| Q71 | - |  |  | SI | H.De.C M 60 y mas |
| Q72 | - |  |  | SI | Lipidos M 60 y mas |
| Q73 | - |  |  | SI | Tipo de Ingreso |
| Q74 | - |  |  | SI | Peso Transversal |
| Q74ObsDR | - |  |  | SI | Peso Transversal DR |
| Q75 | - |  |  | SI | CALORIAS |
| Q76 | - |  |  | SI | PROTEINAS |
| Q77 | - |  |  | SI | HIDRATO DE CARBONO |
| Q78 | - |  |  | SI | LIPIDOS |
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