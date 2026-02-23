# questionnaire.QTCEINECON1

> Informe de Ecografía Obstétrica Nivel 1

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe de Ecografía Obstétrica Nivel 1

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Ecografía N° |
| Q02 | varchar |  |  | SI | Ecografía Solicitada por |
| Q03 | date |  |  | SI | FUR |
| Q04 | numeric |  |  | SI | Semanas |
| Q05 | numeric |  |  | SI | Días |
| Q06 | varchar |  |  | SI | Diagnóstico |
| Q07 | varchar |  |  | SI | Gestación |
| Q08 | varchar |  |  | SI | Actividad Caridíaca |
| Q09 | varchar |  |  | SI | Mov. Corporales |
| Q10 | varchar |  |  | SI | Saco Gestacional |
| Q11 | numeric |  |  | SI | Largo (mm) |
| Q12 | numeric |  |  | SI | Alto (mm) |
| Q13 | numeric |  |  | SI | Ancho (mm) |
| Q14 | varchar |  |  | SI | Saco Vitelino |
| Q15 | numeric |  |  | SI | Diámetro (mm) |
| Q16 | numeric |  |  | SI | DBP (mm) |
| Q17 | numeric |  |  | SI | DFO (mm) |
| Q18 | numeric |  |  | SI | Fémur (mm) |
| Q19 | numeric |  |  | SI | Húmero (mm) |
| Q20 | numeric |  |  | SI | LCN |
| Q21 | numeric |  |  | SI | Abdomen Transverso |
| Q22 | numeric |  |  | SI | Anteroposterior |
| Q23 | numeric |  |  | SI | Circunsferencia Abdominal |
| Q24 | varchar |  |  | SI | Calota |
| Q25 | varchar |  |  | SI | Columna Vertebral |
| Q26 | varchar |  |  | SI | Corazón |
| Q27 | varchar |  |  | SI | Estómago |
| Q28 | varchar |  |  | SI | Vejiga |
| Q29 | varchar |  |  | SI | Extremidades |
| Q30 | varchar |  |  | SI | Riñones |
| Q31 | varchar |  |  | SI | Traslucencia Nucal |
| Q32 | numeric |  |  | SI | Mide (mm) |
| Q33 | varchar |  |  | SI | Localización |
| Q34 | varchar |  |  | SI | Grado de Granumm |
| Q35 | varchar |  |  | SI | Relación con el OCI |
| Q36 | varchar |  |  | SI | Trofoblasto |
| Q37 | varchar |  |  | SI | Liquido Amniotico |
| Q38 | bigint |  |  | SI | Observaciones |
| Q38TxtOnly | bigint |  |  | SI | Observaciones Plain Text Only |
| Q39 | bigint |  |  | SI | Conclusión Ecografía |
| Q39TxtOnly | bigint |  |  | SI | Conclusión Ecografía Plain Text Only |
| Q40 | date |  |  | SI | Fecha de Exámen |
| Q41 | varchar |  |  | SI | Acompañante |
| Q41ObsDR | varchar |  | FK | SI | Acompañante DR |
| Q42 | varchar |  |  | SI | Hueso Nasal |
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