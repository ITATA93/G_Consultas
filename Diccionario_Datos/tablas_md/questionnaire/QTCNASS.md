# questionnaire.QTCNASS

> Score de Síndrome Abstinencia Neonatal (NAS)

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Score de Síndrome Abstinencia Neonatal (NAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Llanto |
| Q02 | varchar |  |  | SI | Sueño |
| Q03 | varchar |  |  | SI | Reflejo Moro |
| Q04 | varchar |  |  | SI | Temblor |
| Q05 | varchar |  |  | SI | Hipertonía |
| Q06 | varchar |  |  | SI | Excoriaciones (área) |
| Q07 | varchar |  |  | SI | Sacudidas mioclónicas |
| Q08 | varchar |  |  | SI | Convulsiones generalizadas |
| Q09 | varchar |  |  | SI | Sudoración |
| Q10 | varchar |  |  | SI | Fiebre |
| Q11 | varchar |  |  | SI | Bostezos frecuentes &gt;3 ó 4 veces tiempo obs. |
| Q12 | varchar |  |  | SI | Piel marmorata |
| Q13 | varchar |  |  | SI | Congestion nasal |
| Q14 | varchar |  |  | SI | Estornudos &gt;3 ó 4 veces tiempo obs. |
| Q15 | varchar |  |  | SI | Aleteo nasal |
| Q16 | varchar |  |  | SI | Frecuencia respiratoria |
| Q17 | varchar |  |  | SI | Succión excesiva |
| Q18 | varchar |  |  | SI | Mal apetito |
| Q19 | varchar |  |  | SI | Regurgitación |
| Q20 | varchar |  |  | SI | Deposiciones |
| Q21 | varchar |  |  | SI | Comments |
| Q22 | varchar |  |  | SI | Comments |
| Q23 | varchar |  |  | SI | Comments |
| Q24 | varchar |  |  | SI | Comments |
| Q25 | varchar |  |  | SI | Comments |
| Q26 | varchar |  |  | SI | Comments |
| Q27 | date |  |  | SI | Fecha |
| Q28 | time |  |  | SI | Hora |
| Q29 | varchar |  |  | SI | Summary statement |
| Q30 | varchar |  |  | SI | Puntaje |
| Q31 | varchar |  |  | SI | Classification |
| Q32 | varchar |  |  | SI | 0 - 37 |
| Q33 | varchar |  |  | SI | Un puntaje más alto podría indicar un riesgo aumen... |
| Q34 | varchar |  |  | SI | 0 - 37: Un puntaje más alto podría indicar un ries... |
| Q35 | varchar |  |  | SI | The Neonatal Abstinence Scoring System (NASS) is u... |
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