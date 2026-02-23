# questionnaire.QTCECEFAII

> Evaluación Fonoaudiología 2da parte

**Schema:** questionnaire
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Fonoaudiología 2da parte

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Estática |
| Q02 | varchar |  |  | SI | Dinámica |
| Q03 | varchar |  |  | SI | Dinámica |
| Q04 | varchar |  |  | SI | Palpación |
| Q05 | varchar |  |  | SI | Respiración |
| Q06 | varchar |  |  | SI | Emisión |
| Q07 | varchar |  |  | SI | Intensidad |
| Q08 | varchar |  |  | SI | Altura Tonal |
| Q09 | varchar |  |  | SI | Extensión  |
| Q10 | varchar |  |  | SI | Ataque Vocal |
| Q11 | varchar |  |  | SI | Quiebres Tonales |
| Q12 | varchar |  |  | SI | Prosodia |
| Q13 | varchar |  |  | SI | Colocación |
| Q14 | varchar |  |  | SI | Resonancia |
| Q15 | varchar |  |  | SI | Mordiente |
| Q16 | varchar |  |  | SI | Articulación |
| Q17 | varchar |  |  | SI | Apertura Bucal |
| Q18 | varchar |  |  | SI | Temblor de Voz |
| Q19 | varchar |  |  | SI | TMF /o/ |
| Q20 | varchar |  |  | SI | TMF /s/ |
| Q21 | varchar |  |  | SI | Indice s/o |
| Q22 | varchar |  |  | SI | Observaciones |
| Q23 | varchar |  |  | SI | Compromiso Cognitivo |
| Q24 | varchar |  |  | SI | OFA |
| Q25 | varchar |  |  | SI | CMO |
| Q26 | varchar |  |  | SI | Reflejos Orales |
| Q27 | varchar |  |  | SI | Tos Voluntaria |
| Q28 | varchar |  |  | SI | Elevación Laríngea |
| Q29 | varchar |  |  | SI | Reflejos Patológicos Orales |
| Q30 | varchar |  |  | SI | Auscuración Cervical |
| Q31 | varchar |  |  | SI | Deglución en Seco |
| Q32 | numeric |  |  | SI | SpO2 |
| Q33 | numeric |  |  | SI | FiO2 |
| Q34 | varchar |  |  | SI | Consistencia Líquida |
| Q35 | varchar |  |  | SI | Consistencia Pastosa |
| Q36 | varchar |  |  | SI | Consistencia Sólida |
| Q37 | varchar |  |  | SI | Fase Preoperatoria Oral  |
| Q38 | varchar |  |  | SI | Fase Oral |
| Q39 | varchar |  |  | SI | Fase Faríngea |
| Q40 | varchar |  |  | SI | Observaciones |
| Q41 | bit |  |  | SI | TECAL |
| Q42 | bit |  |  | SI | TEPROSIF |
| Q43 | bit |  |  | SI | STSG Expresivo |
| Q44 | bit |  |  | SI | STSG Receptivo |
| Q45 | bit |  |  | SI | TAR |
| Q46 | bit |  |  | SI | Protocolo Pragmático de Prutting |
| Q47 | bit |  |  | SI | Protocolo Pragmático de Luis Martinez |
| Q48 | varchar |  |  | SI | Otro(s) ¿Cual(es)? |
| Q49 | varchar |  |  | SI | Resultados y Observaciones |
| Q50 | bit |  |  | SI | Test de Boston |
| Q51 | bit |  |  | SI | Protocolo para pacientes afásicos (González, R. 20... |
| Q52 | bit |  |  | SI | Mini protocolo para pacientes afásicos |
| Q53 | bit |  |  | SI | TokenTest |
| Q54 | varchar |  |  | SI | Otro(s) ¿Cuál(es)? |
| Q55 | varchar |  |  | SI | Resultados y Observaciones |
| Q56 | bit |  |  | SI | Protocolo de Evaluación de Habla |
| Q57 | bit |  |  | SI | Protocolo de Disartria |
| Q58 | varchar |  |  | SI | Otro(s) ¿Cual(es)? |
| Q59 | varchar |  |  | SI | Resultados y Observación |
| Q60 | bit |  |  | SI | Pauta de Evaluación Cognitiva-linguística (Gonzále... |
| Q61 | bit |  |  | SI | Mini Mental State Examination (MMSE) |
| Q62 | bit |  |  | SI | Test de la Figura Compleja de Rey |
| Q63 | bit |  |  | SI | Test de Wisconsin  |
| Q64 | bit |  |  | SI | Test de Barcelona |
| Q65 | varchar |  |  | SI | Otros(s) ¿Cual(es)? |
| Q66 | bit |  |  | SI | Protocolo Evaluación Vocal |
| Q67 | varchar |  |  | SI | Otro(s) ¿Cual(es)? |
| Q68 | varchar |  |  | SI | Resultados y Observaciones |
| Q69 | bit |  |  | SI | Test delVaso de Agua |
| Q70 | bit |  |  | SI | Pauta de Evaluación Clínica de la Deglución (Gonzá... |
| Q71 | bit |  |  | SI | NFC Laríngea Directa |
| Q72 | bit |  |  | SI | NCF Laríngea Indirecta |
| Q73 | varchar |  |  | SI | Otro(s) ¿Cuál(es)? |
| Q74 | varchar |  |  | SI | Sintesis |
| Q75 | varchar |  |  | SI | Indicaciones |
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