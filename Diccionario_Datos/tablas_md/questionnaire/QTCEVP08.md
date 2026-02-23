# questionnaire.QTCEVP08

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Examen Físico General |
| Q02 | varchar | PK |  | SI | Descripción: Estado General |
| Q09 | varchar | PK |  | SI | Cabeza |
| Q10 | varchar | PK |  | SI | Cabeza: Descripción |
| Q14 | varchar | PK |  | SI | Cuello |
| Q15 | varchar | PK |  | SI | Cuello: Descripción |
| Q18 | varchar | PK |  | SI | Tórax |
| Q19 | varchar | PK |  | SI | Tórax: Descripción |
| Q20 | varchar | PK |  | SI | Mamas: Descripción |
| Q21 | varchar | PK |  | SI | Examen Cardíaco: Descripción |
| Q22 | varchar | PK |  | SI | Pulmonar: Descripción |
| Q23 | varchar | PK |  | SI | Abdomen |
| Q24 | varchar | PK |  | SI | Abdomen: Descripción |
| Q25 | varchar | PK |  | SI | Ex. Anorrectal |
| Q26 | varchar | PK |  | SI | Ex. Anorrectal: Descripción |
| Q27 | varchar | PK |  | SI | Ex. Genital |
| Q28 | varchar | PK |  | SI | Examen Genital: Descripción |
| Q29 | varchar | PK |  | SI | Columna |
| Q30 | varchar | PK |  | SI | Columna: Descripción |
| Q31 | varchar | PK |  | SI | Extremidades |
| Q32 | varchar | PK |  | SI | Extremidades: Descripción |
| Q33 | varchar | PK |  | SI | Mamas |
| Q34 | varchar | PK |  | SI | Examen Cardiaco |
| Q35 | varchar | PK |  | SI | Examen Pulmonar |
| Q36 | varchar | PK |  | SI | Examen Neurológico |
| Q37 | varchar | PK |  | SI | Examen Neurológico: Descripción |
| Q38 | varchar | PK |  | SI | Examen Ginecológico |
| Q39 | varchar | PK |  | SI | Examen Ginecológico: Descripción |
| Q40 | varchar | PK |  | SI | Comentarios |
| Q42 | varchar | PK |  | SI | ¿Desea agregar algun comentario? |
| Q43 | bit | PK |  | SI | Profilaxia ocular |
| Q44 | bit | PK |  | SI | Vitamina K |
| Q45 | bit | PK |  | SI | Identificación |
| Q46 | bit | PK |  | SI | Muestra Cordón |
| Q47 | bit | PK |  | SI | Aspiración Gástrica |
| Q51 | varchar | PK |  | SI | Reflejos |
| Q52 | varchar | PK |  | SI | Tonicidad |
| Q53 | varchar | PK |  | SI | Piel |
| Q54 | varchar | PK |  | SI | Perfusión |
| Q55 | varchar | PK |  | SI | Clavicula |
| Q56 | varchar | PK |  | SI | Ombligo |
| Q57 | varchar | PK |  | SI | Vísceras |
| Q58 | varchar | PK |  | SI | Ortolani |
| Q59 | varchar | PK |  | SI | Describa las anormalidades encontradas |
| Q60 | varchar | PK |  | SI | Complemento Examen Recien Nacido |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |
| Qvp88 | numeric | PK |  | SI | Practicado a las |
| Qvp89 | varchar | PK |  | SI | horas de vida |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*