# questionnaire.QCLXXOHAT

> Evaluación OHAT

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación OHAT

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Instrumento de Evaluación de Salud Oral (OHAT) par... |
| Q02 | varchar |  |  | SI | Cuidados Primarios |
| Q03 | varchar |  |  | SI | Tipo de Evaluación |
| Q04 | varchar |  |  | SI | NOTA: Una estrella * indica que se requiere la der... |
| Q05 | varchar |  |  | SI | Categoría |
| Q06 | varchar |  |  | SI | 0 = Saludable |
| Q07 | varchar |  |  | SI | 1 = Cambios |
| Q08 | varchar |  |  | SI | 2 = Enfermo |
| Q09 | varchar |  |  | SI | Labios |
| Q10 | varchar |  |  | SI | Intervención |
| Q11 | varchar |  |  | SI | Derivar a |
| Q12 | varchar |  |  | SI | Lengua |
| Q13 | varchar |  |  | SI | Intervención |
| Q14 | varchar |  |  | SI | Derivar a |
| Q15 | varchar |  |  | SI | Encías y tejidos |
| Q16 | varchar |  |  | SI | Intervención |
| Q17 | varchar |  |  | SI | Derivar a |
| Q18 | varchar |  |  | SI | Saliva |
| Q19 | varchar |  |  | SI | Intervención |
| Q20 | varchar |  |  | SI | Derivar a |
| Q21 | varchar |  |  | SI | Otro |
| Q22 | varchar |  |  | SI | Dientes Naturales |
| Q23 | varchar |  |  | SI | Dientes naturales |
| Q24 | varchar |  |  | SI | Derivar a |
| Q25 | varchar |  |  | SI | Prótesis dental |
| Q26 | varchar |  |  | SI | Prótesis dental |
| Q27 | varchar |  |  | SI | Intervención |
| Q28 | varchar |  |  | SI | Identificar la prótesis |
| Q29 | varchar |  |  | SI | Derivar a |
| Q30 | varchar |  |  | SI | Otro |
| Q31 | varchar |  |  | SI | Higiene oral |
| Q32 | varchar |  |  | SI | Intervención |
| Q33 | varchar |  |  | SI | Derivar a |
| Q34 | varchar |  |  | SI | Otro |
| Q35 | varchar |  |  | SI | Dolor dental |
| Q36 | varchar |  |  | SI | Derivar a |
| Q37 | varchar |  |  | SI | Otro |
| Q38 | varchar |  |  | SI | Otro |
| Q39 | varchar |  |  | SI | otro |
| Q40 | varchar |  |  | SI | otro |
| Q41 | varchar |  |  | SI | Otro |
| Q42 | varchar |  |  | SI | Notas |
| Q43 | varchar |  |  | SI | Completado por |
| Q44 | date |  |  | SI | Fecha |
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