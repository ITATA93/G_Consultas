# questionnaire.QTCEECOGINE

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Posición |
| Q02 | varchar | PK |  | SI | Miometrio |
| Q03 | varchar | PK |  | SI | Endometrio |
| Q04 | varchar | PK |  | SI | Grosor |
| Q05 | varchar | PK |  | SI | Longuitud |
| Q06 | varchar | PK |  | SI | Aposterior |
| Q07 | varchar | PK |  | SI | Transverso |
| Q08 | varchar | PK |  | SI | DIU |
| Q09 | varchar | PK |  | SI | Distancia al fondo |
| Q10 | varchar | PK |  | SI | Long OD |
| Q11 | varchar | PK |  | SI | Long OI |
| Q12 | varchar | PK |  | SI | Trans OD |
| Q13 | varchar | PK |  | SI | Trans OI |
| Q14 | varchar | PK |  | SI | Vol OD |
| Q15 | varchar | PK |  | SI | Vol OI |
| Q16 | varchar | PK |  | SI | Douglas |
| Q18 | varchar | PK |  | SI | Observaciones |
| Q188 | varchar | PK |  | SI | Observaciones |
| Q19 | varchar | PK |  | SI | Conclision |
| Q198 | varchar | PK |  | SI | Hipótesis Diagnóstica |
| Q20 | varchar | PK |  | SI | Anexos |
| Q208 | varchar | PK |  | SI | Anexos |
| Q21 | varchar | PK |  | SI | Diámetro Antero Posterior OD |
| Q22 | varchar | PK |  | SI | Diámetro Antero Posterior OI |
| Q23 | varchar | PK |  | SI | Douglas Ocupado |
| Q24 | varchar | PK |  | SI | Saco de Douglas |
| QDISDIU | varchar | PK |  | SI | DISDIU |
| QDISDIU4 | varchar | PK |  | SI | Distancia al Fondo |
| QDIU | varchar | PK |  | SI | DIU |
| QDIU2 | varchar | PK |  | SI | DIU |
| QFECHAEXAMEN | date | PK |  | SI | FECHAEXAMEN |
| QPOSICION | varchar | PK |  | SI | Posición |
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