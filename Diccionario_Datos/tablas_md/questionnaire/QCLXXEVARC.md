# questionnaire.QCLXXEVARC

> Evaluación de Riesgo de Caídas

**Schema:** questionnaire
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación de Riesgo de Caídas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Factores de Riesgo |
| Q02 | varchar |  |  | SI | Mayor o igual a 65 años o pediátrico |
| Q03 | varchar |  |  | SI | Caídas Previas |
| Q04 | varchar |  |  | SI | En algún procedimiento anterior |
| Q05 | varchar |  |  | SI | Alteraciones Neurológicas |
| Q06 | varchar |  |  | SI | Epilepsia, convulsiones, paresia, parálisis, Parki... |
| Q07 | varchar |  |  | SI | Trastornos Psíquicos |
| Q08 | varchar |  |  | SI | Alcoholismo y/o drogadicción |
| Q09 | varchar |  |  | SI | Actitud resistente, agresiva o temerosa, crisis de... |
| Q10 | varchar |  |  | SI | Depresión, trastorno bipolar en etapa aguda |
| Q11 | varchar |  |  | SI | Defectos Visión /Audición |
| Q12 | varchar |  |  | SI | Cataratas, glaucoma, retinopatía y trastornos vest... |
| Q13 | varchar |  |  | SI | Alteraciones de conciencia |
| Q14 | varchar |  |  | SI | Confuso, desorientado, agitación psicomotora |
| Q15 | varchar |  |  | SI | Uso de Fármacos |
| Q16 | varchar |  |  | SI | Tranquilizantes-sedantes |
| Q17 | varchar |  |  | SI | Diuréticos |
| Q18 | varchar |  |  | SI | Hipotensores (No diuréticos)  |
| Q19 | varchar |  |  | SI | Antiparkinsonianos |
| Q20 | varchar |  |  | SI | Antidepresivos |
| Q21 | varchar |  |  | SI | Otros |
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