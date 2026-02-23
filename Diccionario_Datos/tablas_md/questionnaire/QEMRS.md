# questionnaire.QEMRS

> MRS

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(MRS)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Bochornos, sudoración, calores. |
| Q02 | varchar |  |  | SI | Molestias al corazón (sentir latidos del corazón, ... |
| Q03 | varchar |  |  | SI | Molestias musculares y articulares (dolores de hue... |
| Q04 | varchar |  |  | SI | Dificultades en el sueño (insomnio, duerme poco). |
| Q05 | varchar |  |  | SI | Estado de ánimo depresivo (sentirse deprimida, dec... |
| Q06 | varchar |  |  | SI | Irritabilidad (sentirse tensa, explota fácil, sent... |
| Q07 | varchar |  |  | SI | Ansiedad (sentirse angustiada, temerosa, inquieta,... |
| Q08 | varchar |  |  | SI | Cansancio físico y mental (rinde menos, se cansa f... |
| Q09 | varchar |  |  | SI | Problemas sexuales (menos ganas de sexo, menor fre... |
| Q10 | varchar |  |  | SI | Problemas con la orina (problemas al orinar, orina... |
| Q11 | varchar |  |  | SI | Sequedad vaginal (sensación de genitales secos, ma... |
| Q12 | varchar |  |  | SI | Somático |
| Q13 | varchar |  |  | SI | Psicológico |
| Q14 | varchar |  |  | SI | Urogenital |
| Q15 | varchar |  |  | SI | Total |
| Q17 | varchar |  |  | SI | Resultado Escala MRS Dominio Somático |
| Q17ObsDR | varchar |  | FK | SI | Resultado Escala MRS Dominio Somático DR |
| Q18 | varchar |  |  | SI | Resultado Escala MRS Dominio Psicológico |
| Q18ObsDR | varchar |  | FK | SI | Resultado Escala MRS Dominio Psicológico DR |
| Q19 | varchar |  |  | SI | Resultado Escala MRS Dominio Urogenital |
| Q19ObsDR | varchar |  | FK | SI | Resultado Escala MRS Dominio Urogenital DR |
| Q20 | varchar |  |  | SI | Resultado Escala MRS |
| Q20ObsDR | varchar |  | FK | SI | Resultado Escala MRS DR |
| Q21 | varchar |  |  | SI | ¿Paciente Bajo Terapia Hormonal de Reemplazo? [REM... |
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