# questionnaire.QCLXXPDBI

> PAUTA DE RIESGO BIOPSICOSOCIAL INFANTIL CHILE CRECE CONTIGO

**Schema:** questionnaire
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* PAUTA DE RIESGO BIOPSICOSOCIAL INFANTIL CHILE CRECE CONTIGO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Niña o niño sin control de salud al día. |
| Q02 | varchar |  |  | SI | 2. Niña o niño con múltiples consultas en SAPU, ot... |
| Q03 | varchar |  |  | SI | 3. Niña o niño con hospitalización anterior de med... |
| Q04 | varchar |  |  | SI | 4. Niña o niño con condición médica de base (síndr... |
| Q05 | varchar |  |  | SI | 5. Niña o niño con madre adolescente. |
| Q06 | varchar |  |  | SI | 6. Niña o niño cuya madre tiene escolaridad menor ... |
| Q07 | varchar |  |  | SI | 7. Niña o niño cuya madre presenta escala de Edimb... |
| Q08 | varchar |  |  | SI | 8. Niña o niño cuyo cuidador/a principal presenta ... |
| Q09 | varchar |  |  | SI | 9. Niña o niño que vive en familia monoparental si... |
| Q10 | varchar |  |  | SI | 10. Presencia de cualquier trastorno de salud ment... |
| Q11 | varchar |  |  | SI | 11. Niña o niño cuyo hermano/a tiene antecedentes ... |
| Q12 | varchar |  |  | SI | 12. Niña o niño cuyo padre, madre o cuidador/a pri... |
| Q13 | varchar |  |  | SI | 13. Niña o niño institucionalizado en residencia d... |
| Q14 | varchar |  |  | SI | 14. Niña o niño que crece en un contexto ambiental... |
| Q15 | varchar |  |  | SI | 15. Niña o niño que vive en una familia con aislam... |
| Q16 | varchar |  |  | SI | 16. Violencia intrafamiliar / niña o niña testigo ... |
| Q17 | varchar |  |  | SI | 17. Maltrato físico o abuso sexual. |
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