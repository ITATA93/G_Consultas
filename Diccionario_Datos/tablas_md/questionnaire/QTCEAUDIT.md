# questionnaire.QTCEAUDIT

> Auto-diagnóstico sobre Riesgos en el Uso de Alcohol (AUDIT)

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Auto-diagnóstico sobre Riesgos en el Uso de Alcohol (AUDIT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ10medicoh | varchar |  |  | SI | - |
| CQ1frecoh | varchar |  |  | SI | - |
| CQ2unidadoh | varchar |  |  | SI | - |
| CQ3frec6oh | varchar |  |  | SI | - |
| CQ4pararoh | varchar |  |  | SI | - |
| CQ5haceroh | varchar |  |  | SI | - |
| CQ6ayunaoh | varchar |  |  | SI | - |
| CQ7culpaoh | varchar |  |  | SI | - |
| CQ8recuerdoh | varchar |  |  | SI | - |
| CQ9heridoh | varchar |  |  | SI | - |
| Q10medicoh | varchar |  |  | SI | 10.- ¿Algún familiar, amigo, médico o profesional ... |
| Q12 | varchar |  |  | SI | Intervenciones [REM] |
| Q1frecoh | varchar |  |  | SI | 1.- ¿Con qué frecuencia consume alguna bebida alco... |
| Q2unidadoh | varchar |  |  | SI | 2.- ¿Cuántos TRAGOS de alcohol suele beber en un d... |
| Q3frec6oh | varchar |  |  | SI | 3.- ¿Con qué frecuencia toma 5 o más TRAGOS en un ... |
| Q4pararoh | varchar |  |  | SI | 4.- ¿Con qué frecuencia en el curso del último año... |
| Q5haceroh | varchar |  |  | SI | 5.- ¿Con qué frecuencia en el curso del último año... |
| Q6ayunaoh | varchar |  |  | SI | 6.- ¿Con qué frecuencia en el curso del último año... |
| Q7culpaoh | varchar |  |  | SI | 7.- ¿Con qué frecuencia en el curso del último año... |
| Q8recuerdoh | varchar |  |  | SI | 8.- ¿Con qué frecuencia en el curso del último año... |
| Q9heridoh | varchar |  |  | SI | 9.- ¿Usted o alguna otra persona ha resultado heri... |
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
| Qr | varchar |  |  | SI | Resultado AUDIT |
| QrObsDR | varchar |  | FK | SI | Resultado AUDIT DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*