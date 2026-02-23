# questionnaire.QTCECEFRN

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Reflejos |
| Q02 | varchar | PK |  | SI | Tonicidad |
| Q03 | varchar | PK |  | SI | Piel |
| Q04 | varchar | PK |  | SI | Perfusión |
| Q05 | varchar | PK |  | SI | Cabeza |
| Q06 | varchar | PK |  | SI | Ojos |
| Q07 | varchar | PK |  | SI | Nariz |
| Q08 | varchar | PK |  | SI | Oídos |
| Q09 | varchar | PK |  | SI | Boca |
| Q10 | varchar | PK |  | SI | Pulmones |
| Q11 | varchar | PK |  | SI | Corazón |
| Q12 | varchar | PK |  | SI | Abdomen |
| Q13 | varchar | PK |  | SI | Vísceras |
| Q14 | varchar | PK |  | SI | Omblígo |
| Q15 | varchar | PK |  | SI | Genitales |
| Q16 | varchar | PK |  | SI | Ano |
| Q17 | varchar | PK |  | SI | Columna |
| Q18 | varchar | PK |  | SI | Extremidades |
| Q19 | varchar | PK |  | SI | Articulación |
| Q20 | varchar | PK |  | SI | Ortolani |
| Q21 | varchar | PK |  | SI | REFLEJOS |
| Q22 | varchar | PK |  | SI | TONICIDAD |
| Q23 | varchar | PK |  | SI | PIEL |
| Q25 | varchar | PK |  | SI | PERFUSION |
| Q26 | varchar | PK |  | SI | CABEZA |
| Q27 | varchar | PK |  | SI | OJOS |
| Q28 | varchar | PK |  | SI | NARIZ |
| Q29 | varchar | PK |  | SI | OIDOS |
| Q30 | varchar | PK |  | SI | BOCA |
| Q31 | varchar | PK |  | SI | PULMONES |
| Q32 | varchar | PK |  | SI | CORAZON |
| Q33 | varchar | PK |  | SI | ABDOMEN |
| Q34 | varchar | PK |  | SI | VISCERAS |
| Q35 | varchar | PK |  | SI | OMBLIGO |
| Q36 | varchar | PK |  | SI | GENITALES |
| Q37 | varchar | PK |  | SI | ANO |
| Q38 | varchar | PK |  | SI | COLUMNA |
| Q39 | varchar | PK |  | SI | EXTREMIDADES |
| Q40 | varchar | PK |  | SI | ARTICULACION |
| Q41 | varchar | PK |  | SI | ORTOLANI |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*