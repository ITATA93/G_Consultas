# questionnaire.QTCECDD

> Criterios Diagnósticos Depresión CIE-10

**Schema:** questionnaire
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Criterios Diagnósticos Depresión CIE-10

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Durante las últimas semanas: |
| Q02 | varchar |  |  | SI | ¿Se ha sentido triste o deprimido(a) la mayor part... |
| Q03 | varchar |  |  | SI | ¿Ha estado desinteresad(a) o incapaz d disfrutarl ... |
| Q04 | varchar |  |  | SI | ¿Ha tenido problemas para dormir (Insomnio o dormi... |
| Q05 | varchar |  |  | SI | ¿Se ha sentido cansado(a) o con menos energía la m... |
| Q06 | varchar |  |  | SI | ¿Ha notado problemas de concentración o memoria, c... |
| Q07 | varchar |  |  | SI | ¿Ha estado mas lento(a) para hacer las cosas, casi... |
| Q08 | varchar |  |  | SI | ¿Ha estado tan inquieto(a) que no puede permanecer... |
| Q09 | varchar |  |  | SI | ¿Ha sentido que Ud. no es tan hábil o capaz como o... |
| Q10 | varchar |  |  | SI | ¿Se ha sentido despreciable o culpable, casi todos... |
| Q11 | varchar |  |  | SI | ¿Ha notado un cambio importante en el apetito? (Au... |
| Q12 | varchar |  |  | SI | ¿Ha notado un cambio de peso de mas de 4 kilos? (A... |
| Q13 | varchar |  |  | SI | ¿Ha pensado realmente que no vale la pena vivir? |
| Q14 | varchar |  |  | SI | ¿Ha pensado quitarse la vida? |
| Q15 | varchar |  |  | SI | Resultado Criterios Diagnostico Depresión |
| Q15ObsDR | varchar |  | FK | SI | Resultado Criterios Diagnostico Depresión DR |
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