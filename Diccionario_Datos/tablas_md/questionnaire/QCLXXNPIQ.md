# questionnaire.QCLXXNPIQ

> Test NPI - Q

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Test NPI - Q

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Delirios ¿Cree el/la paciente en cosas que no son ... |
| Q02 | varchar |  |  | SI | Gravedad del Síntoma |
| Q03 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q04 | varchar |  |  | SI | Alucinaciones. ¿El/la paciente ve cosas o personas... |
| Q05 | varchar |  |  | SI | Gravedad del Síntoma |
| Q06 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q07 | varchar |  |  | SI | Agresividad. ¿El/la paciente insulta o se molesta ... |
| Q08 | varchar |  |  | SI | Gravedad del Síntoma |
| Q09 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q10 | varchar |  |  | SI | Depresión. ¿El/la paciente está triste o desanimad... |
| Q11 | varchar |  |  | SI | Gravedad del Síntoma |
| Q12 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q13 | varchar |  |  | SI | Ansiedad ¿El/la paciente está nervioso, inquieto, ... |
| Q14 | varchar |  |  | SI | Gravedad del Síntoma |
| Q15 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q16 | varchar |  |  | SI | Euforia. ¿Parece el/la paciente estar demasiado al... |
| Q17 | varchar |  |  | SI | Gravedad del Síntoma |
| Q18 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q19 | varchar |  |  | SI | Apatía. ¿El/la paciente parece poco interesado, po... |
| Q20 | varchar |  |  | SI | Gravedad del Síntoma |
| Q21 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q22 | varchar |  |  | SI | Desinhibición. ¿El/la paciente actúa impulsivament... |
| Q23 | varchar |  |  | SI | Gravedad del Síntoma |
| Q24 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q25 | varchar |  |  | SI | Irritabilidad. ¿Está el/la paciente irritable o se... |
| Q26 | varchar |  |  | SI | Gravedad del Síntoma |
| Q27 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q28 | varchar |  |  | SI | Conducta Motora Anómala. ¿El/la paciente se dedica... |
| Q29 | varchar |  |  | SI | Gravedad del Síntoma |
| Q30 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q31 | varchar |  |  | SI | Problema de Sueño. ¿El/la paciente tiene dificulta... |
| Q32 | varchar |  |  | SI | Gravedad del Síntoma |
| Q33 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
| Q34 | varchar |  |  | SI | Problemas de Apetito. ¿El/la paciente ha perdido o... |
| Q35 | varchar |  |  | SI | Gravedad del Síntoma |
| Q36 | varchar |  |  | SI | Estrés que a usted le provoca la presencia del sín... |
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