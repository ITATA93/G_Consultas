# questionnaire.QTCENUTPESO

> Estado Nutricional

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Estado Nutricional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Peso  Actual |
| Q01ObsDR | varchar |  | FK | SI | Peso  Actual DR |
| Q02 | date |  |  | SI | Fecha |
| Q03 | numeric |  |  | SI | Peso Anterior |
| Q05 | varchar |  |  | SI | Clasificación  |
| Q06 | varchar |  |  | SI | Variacion de Peso  |
| Q07 | varchar |  |  | SI | Ingesta Alimentaria en relación a lo habitual |
| Q09 | varchar |  |  | SI | Patología de baja demanda metabólica: Hipoglicemia... |
| Q10 | varchar |  |  | SI | Severidad de la Enfermedad |
| Q11 | varchar |  |  | SI | Pérdida de Peso Involuntaria en 1 Mes |
| Q12 | varchar |  |  | SI | Pacientes crónicos c / complicaciones agudas. Frac... |
| Q13 | varchar |  |  | SI | Cirugía mayor abdominal.Neumonía severa. EPOC desc... |
| Q14 | varchar |  |  | SI | Shock. Pancreatitis, Balthzar D y E. TEC grave, Po... |
| Q15 | varchar |  |  | SI | Clasificación |
| Q16 | varchar |  |  | SI | Observaciones |
| Q17 | date |  |  | SI | Fecha Peso Anterior |
| Q18 | varchar |  |  | SI | Peso |
| Q18ObsDR | varchar |  | FK | SI | Peso DR |
| Q19 | varchar |  |  | SI | Talla |
| Q19ObsDR | varchar |  | FK | SI | Talla DR |
| Q20 | varchar |  |  | SI | IMC |
| Q21 | varchar |  |  | SI | Estado Nutricional |
| Q21ObsDR | varchar |  | FK | SI | Estado Nutricional DR |
| Q22 | varchar |  |  | SI | Kg |
| Q23 | varchar |  |  | SI | Kg |
| Q24 | varchar |  |  | SI | Kg |
| Q25 | varchar |  |  | SI | cm |
| Q26 | numeric |  |  | SI | Peso Habitual  |
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