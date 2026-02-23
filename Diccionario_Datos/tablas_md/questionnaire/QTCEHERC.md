# questionnaire.QTCEHERC

> Hoja Evaluación Riesgo Caídas

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hoja Evaluación Riesgo Caídas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Ingreso |
| Q02 | varchar |  |  | SI | Establecimiento |
| Q03 | varchar |  |  | SI | Servicio |
| Q04 | varchar |  |  | SI | Diagnostico |
| Q05 | varchar |  |  | SI | Criterios de Asignacion de Riesgo |
| Q06 | varchar |  |  | SI | Caídas Anteriores |
| Q07 | varchar |  |  | SI | Debilidad Muscular |
| Q08 | varchar |  |  | SI | Deterioro de la vista |
| Q09 | varchar |  |  | SI | Alteración de la Audición o Equilibrio |
| Q10 | varchar |  |  | SI | Edad: Menores de 1 año |
| Q11 | varchar |  |  | SI | Edad: Mayores de 75 año |
| Q12 | varchar |  |  | SI | Alteraciones Neurologícas |
| Q13 | varchar |  |  | SI | Trastornos Síquicos o Mentales |
| Q14 | varchar |  |  | SI | Alteraciones del Ritmo Cardiovascular |
| Q15 | varchar |  |  | SI | Deambulación con Apoyo |
| Q16 | varchar |  |  | SI | Agitación Psicomotora |
| Q17 | varchar |  |  | SI | Transtornos Gastrointestinales |
| Q18 | varchar |  |  | SI | Tratamiento Farmacologico |
| Q19 | varchar |  |  | SI | Diuréticos  |
| Q20 | varchar |  |  | SI | Hipotensores |
| Q21 | varchar |  |  | SI | Quimioterápicos (Efectos Adversos) |
| Q22 | varchar |  |  | SI | Depresores del SNC |
| Q23 | varchar |  |  | SI | Anestesia General Reciente (12hrs. Post Anestesia)... |
| Q24 | varchar |  |  | SI | Drogas vaso activas |
| Q25 | varchar |  |  | SI | Puntaje Total |
| Q26 | varchar |  |  | SI | Criterios de Asignación de Riesgo |
| Q27 | varchar |  |  | SI | Tratamiento Farmacológico |
| Q28 | varchar |  |  | SI | Servicio |
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