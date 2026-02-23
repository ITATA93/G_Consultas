# questionnaire.QTCEHEE

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Dilatacion Cervical |
| Q01ObsDR | varchar | PK | FK | SI | Dilatacion Cervical DR |
| Q02 | varchar | PK |  | SI | ASA |
| Q03 | varchar | PK |  | SI | Ayuno |
| Q04 | numeric | PK |  | SI | No Horas Ayuno |
| Q05 | varchar | PK |  | SI | Tipo de Ingesta |
| Q06 | varchar | PK |  | SI | Observacions Evaluacion Preanestesia |
| Q07 | varchar | PK |  | SI | Anestesiologo Evaluación |
| Q08 | varchar | PK |  | SI | Posicion de La Paciente |
| Q09 | varchar | PK |  | SI | Sitio de Punción |
| Q10 | numeric | PK |  | SI | No de Trocar |
| Q11 | numeric | PK |  | SI | Cateter No |
| Q12 | varchar | PK |  | SI | Aspiración LCR |
| Q13 | varchar | PK |  | SI | Parestesias |
| Q14 | varchar | PK |  | SI | Parestesias TL |
| Q15 | varchar | PK |  | SI | Anestesicos |
| Q16 | varchar | PK |  | SI | PA |
| Q16ObsDR | varchar | PK | FK | SI | PA DR |
| Q17 | varchar | PK |  | SI | FC |
| Q17ObsDR | varchar | PK | FK | SI | FC DR |
| Q18 | varchar | PK |  | SI | LCF |
| Q18ObsDR | varchar | PK | FK | SI | LCF DR |
| Q19 | time | PK |  | SI | 2a Dose Hora |
| Q20 | varchar | PK |  | SI | 2o Dosis Aspiracion |
| Q21 | varchar | PK |  | SI | 2o Dosis PA |
| Q21ObsDR | varchar | PK | FK | SI | 2o Dosis PA DR |
| Q22 | varchar | PK |  | SI | 2o Dosis FC |
| Q22ObsDR | varchar | PK | FK | SI | 2o Dosis FC DR |
| Q23 | varchar | PK |  | SI | 2o Dosis LCF |
| Q23ObsDR | varchar | PK | FK | SI | 2o Dosis LCF DR |
| Q24 | varchar | PK |  | SI | Anestesiologo |
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
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
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