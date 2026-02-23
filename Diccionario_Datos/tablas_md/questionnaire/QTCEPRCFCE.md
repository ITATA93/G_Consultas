# questionnaire.QTCEPRCFCE

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Resposable Indicación |
| Q02 | varchar | PK |  | SI | Enfermera Responsable |
| Q03 | date | PK |  | SI | Fecha Indicación |
| Q04 | time | PK |  | SI | Hora |
| Q05 | varchar | PK |  | SI | Turno |
| Q10 | varchar | PK |  | SI | Medidas Fracasadas antes de la contención física |
| Q12 | varchar | PK |  | SI | Incidentes durante el procedimiento |
| Q13 | varchar | PK |  | SI | Detalle del incidente |
| Q15 | varchar | PK |  | SI | Farmacos Indicados |
| Q18 | time | PK |  | SI | Hora Control 1 |
| Q19 | time | PK |  | SI | Hora Control 2 |
| Q20 | time | PK |  | SI | Hora Control 3 |
| Q21 | time | PK |  | SI | Hora Control 4 |
| Q22 | time | PK |  | SI | Hora Control 5 |
| Q23 | time | PK |  | SI | Hora Control 6 |
| Q24 | varchar | PK |  | SI | Aseo y Confort 1 |
| Q25 | varchar | PK |  | SI | Aseo y Confort 2 |
| Q26 | varchar | PK |  | SI | Aseo y Confort 3 |
| Q27 | varchar | PK |  | SI | Aseo y Confort 4 |
| Q28 | varchar | PK |  | SI | Aseo y Confort 5 |
| Q29 | varchar | PK |  | SI | Aseo y Confort 6 |
| Q30 | bit | PK |  | SI | Alimentación Asistida 1 |
| Q31 | bit | PK |  | SI | Alimentación Asistida 2 |
| Q32 | bit | PK |  | SI | Alimentación Asistida 3 |
| Q33 | bit | PK |  | SI | Alimentación Asistida 4 |
| Q34 | bit | PK |  | SI | Alimentación Asistida 5 |
| Q35 | bit | PK |  | SI | Alimentación Asistida 6 |
| Q36 | varchar | PK |  | SI | Prevencion UPP1 |
| Q37 | varchar | PK |  | SI | Prevencion UPP2 |
| Q38 | varchar | PK |  | SI | Prevencion UPP3 |
| Q39 | varchar | PK |  | SI | Prevencion UPP4 |
| Q40 | varchar | PK |  | SI | Prevencion UPP5 |
| Q41 | varchar | PK |  | SI | Prevencion UPP6 |
| Q42 | varchar | PK |  | SI | Diuresis + 1 |
| Q43 | varchar | PK |  | SI | Diuresis + 2 |
| Q44 | varchar | PK |  | SI | Diuresis + 3 |
| Q45 | varchar | PK |  | SI | Diuresis + 4 |
| Q46 | varchar | PK |  | SI | Diuresis + 5 |
| Q47 | varchar | PK |  | SI | Diuresis + 6 |
| Q48 | varchar | PK |  | SI | Diuresis - 1 |
| Q49 | varchar | PK |  | SI | Diuresis - 2 |
| Q50 | varchar | PK |  | SI | Diuresis - 3 |
| Q51 | varchar | PK |  | SI | Diuresis - 4 |
| Q52 | varchar | PK |  | SI | Diuresis - 6 |
| Q53 | varchar | PK |  | SI | Deposiciones + 1 |
| Q54 | varchar | PK |  | SI | Deposiciones + 2 |
| Q55 | varchar | PK |  | SI | Deposiciones + 3 |
| Q56 | varchar | PK |  | SI | Deposiciones + 4 |
| Q57 | varchar | PK |  | SI | Deposiciones + 5 |
| Q58 | varchar | PK |  | SI | Deposiciones + 6 |
| Q59 | varchar | PK |  | SI | Deposiciones - 1 |
| Q60 | varchar | PK |  | SI | Deposiciones - 2 |
| Q61 | varchar | PK |  | SI | Deposiciones - 3 |
| Q62 | varchar | PK |  | SI | Deposiciones - 4 |
| Q63 | varchar | PK |  | SI | Deposiciones - 5 |
| Q64 | varchar | PK |  | SI | Deposiciones - 6 |
| Q65 | varchar | PK |  | SI | TENS Responsable 1 |
| Q66 | varchar | PK |  | SI | TENS Responsable 2 |
| Q67 | varchar | PK |  | SI | TENS Responsable 3 |
| Q68 | varchar | PK |  | SI | TENS Responsable 4 |
| Q69 | varchar | PK |  | SI | TENS Responsable 5 |
| Q70 | varchar | PK |  | SI | TENS Responsable 6 |
| Q71 | varchar | PK |  | SI | Diuresis - 5 |
| Q72 | varchar | PK |  | SI | TENS en supervicion y observacion 2 horas |
| Q73 | varchar | PK |  | SI | TENS supervicion y observacion 8 horas |
| Q74 | date | PK |  | SI | Fecha 1 |
| Q75 | date | PK |  | SI | Fecha 2 |
| Q76 | date | PK |  | SI | Fecha 3 |
| Q77 | date | PK |  | SI | Fecha 4 |
| Q78 | date | PK |  | SI | Fecha 5 |
| Q79 | date | PK |  | SI | Fecha 6 |
| Q80 | date | PK |  | SI | Fecha Término |
| Q81 | time | PK |  | SI | Hora Término |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*