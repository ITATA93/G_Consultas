# SQLUser.MRC_PhyExam

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXAM_RowId | bigint | PK |  | NO | - |
| EXAM_Code | varchar |  |  | SI | Code |
| EXAM_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| EXAM_CreatedDate | date |  |  | SI | Created Date |
| EXAM_CreatedTime | time |  |  | SI | Created Time |
| EXAM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXAM_DateFrom | date |  |  | SI | Date From |
| EXAM_DateTo | date |  |  | SI | Date To |
| EXAM_Desc | varchar |  |  | SI | Description |
| EXAM_Owner | varchar |  |  | SI | Owner |
| EXAM_UpdatedDate | date |  |  | SI | Updated Date |
| EXAM_UpdatedTime | time |  |  | SI | Updated Time |
| EXAM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Pregunta A: ¿Este paciente presenta una amenaza re... |
| Q02 | - |  |  | SI | Pregunta B: ¿Se trata de un paciente que no debe e... |
| Q03 | - |  |  | SI | Pregunta C: ¿Cuántos recursos se necesitan para la... |
| Q04 | - |  |  | SI | Pregunta D: ¿Signos vitales en zona de riesgo? |
| Q05 | - |  |  | SI | ESI |
| Q06 | - |  |  | SI | Condición 1 |
| Q07 | - |  |  | SI | Condición 2 |
| Q08 | - |  |  | SI | Profesión |
| Q09 | - |  |  | SI | Profesional Ejecutor |
| Q10 | - |  |  | SI | AVDI |
| Q11 | - |  |  | SI | Distrés / ¿situación de alto riesgo? |
| Q12 | - |  |  | SI | Dolor, EVA |
| Q13 | - |  |  | SI | Saturometría |
| Q13ObsDR | - |  |  | SI | Saturometría DR |
| Q14 | - |  |  | SI | Frecuencia Respiratoria |
| Q14ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q15 | - |  |  | SI | Frecuencia Cardiaca |
| Q15ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q16 | - |  |  | SI | Temperatura |
| Q16ObsDR | - |  |  | SI | Temperatura DR |
| Q17 | - |  |  | SI | Condición 3 |
| Q18 | - |  |  | SI | Esquema de inmunizaciones incompleto |
| Q19 | - |  |  | SI | Fiebre de origen no evidente a la evaluación |
| Q20 | - |  |  | SI | Asignar Nivel de Categorización C4 |
| Q21 | - |  |  | SI | Asignar Nivel de Categorización C5 |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*