# questionnaire.QCLXXFEGSUB

> Ficha Evaluación Global Subjetiva

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Evaluación Global Subjetiva

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evalaución |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | A. ANAMNESIS |
| Q04 | varchar |  |  | SI | 1. PESO |
| Q05 | numeric |  |  | SI | Peso Habitual |
| Q06 | varchar |  |  | SI | Pérdida de peso en los últimos 6 meses |
| Q07 | numeric |  |  | SI | Cantidad perdida |
| Q08 | varchar |  |  | SI | % de Pérdida en relación a su peso Habitual |
| Q09 | varchar |  |  | SI | Las últimas dos semana |
| Q10 | varchar |  |  | SI | 2. INGESTA ALIMENTARIA CON RELACIÓN A LA HABITUAL |
| Q11 | varchar |  |  | SI | Ingesta Alimentaria |
| Q12 | numeric |  |  | SI | Hace cuanto Tiempo (días) |
| Q13 | varchar |  |  | SI | Tipo de Dieta |
| Q14 | varchar |  |  | SI | 3. SÍNTOMAS GASTROINTESTINALES |
| Q15 | varchar |  |  | SI | Presente hace más de 15 días |
| Q16 | varchar |  |  | SI | Vómitos |
| Q17 | varchar |  |  | SI | Náuseas |
| Q18 | varchar |  |  | SI | Diarrea (+ de 3 Evacuaciones liquidas/día) |
| Q19 | varchar |  |  | SI | Falta de Apetito |
| Q20 | varchar |  |  | SI | 4. CAPACIDAD FUNCIONAL |
| Q21 | varchar |  |  | SI | Disfunción |
| Q22 | numeric |  |  | SI | Hace cuanto tiempo (días) |
| Q23 | varchar |  |  | SI | Que tipo |
| Q24 | varchar |  |  | SI | 5. DIAGNÓSTICO PRINCIPAL Y SU RELACIÓN CON LAS NEC... |
| Q25 | varchar |  |  | SI | Diagnostico Principal |
| Q26 | varchar |  |  | SI | Demanda Metabólica |
| Q27 | varchar |  |  | SI | B. EXAMEN FÍSICO |
| Q28 | varchar |  |  | SI | Pérdida de Grasa Subcutánea |
| Q29 | varchar |  |  | SI | Pérdida Muscular ( Cuadriceps o Deltoides) |
| Q30 | varchar |  |  | SI | Edema de Tobillos |
| Q31 | varchar |  |  | SI | Edema Sacro |
| Q32 | varchar |  |  | SI | Ascitis |
| Q33 | varchar |  |  | SI | C. EVALUCIÓN SUBJETIVA |
| Q34 | varchar |  |  | SI | Resultado Evaluación Subjetiva |
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