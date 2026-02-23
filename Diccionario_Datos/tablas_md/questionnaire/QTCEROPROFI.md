# questionnaire.QTCEROPROFI

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | varchar | PK |  | SI | Pieza dental |
| Q03 | date | PK |  | SI | Fecha |
| Q04 | varchar | PK |  | SI | Otro |
| Q05 | varchar | PK |  | SI | Prótesis |
| Q06 | varchar | PK |  | SI | Color |
| Q09 | date | PK |  | SI | Impresion |
| Q10 | date | PK |  | SI | Preparación biomecánica y provisorio        |
| Q11 | date | PK |  | SI | Instalación de perno muñón + prueba de color 1    ... |
| Q12 | date | PK |  | SI | Altura y/o prueba de base + prueba de color       ... |
| Q13 | date | PK |  | SI | Prueba de Casqueta |
| Q14 | date | PK |  | SI | Prueba de Casqueta, prueba de porcelana  |
| Q15 | varchar | PK |  | SI | Instalación de prótesis y cito a control |
| Q16 | bit | PK |  | SI | Acta de recepción |
| Q17 | varchar | PK |  | SI | Comprobante de Recepción de Protesis |
| Q18 | date | PK |  | SI | Control 1 |
| Q19 | varchar | PK |  | SI | Pronostico |
| Q20 | varchar | PK |  | SI | Nuevo Tratamiento1 |
| Q21 | varchar | PK |  | SI | Nuevo Tratamiento2 |
| Q22 | varchar | PK |  | SI | Nuevo Tratamiento3 |
| Q23 | date | PK |  | SI | Impresion1 |
| Q24 | date | PK |  | SI | Preparación biomecánica y provisorio1 |
| Q25 | date | PK |  | SI | Instalación de perno muñón + prueba de color      ... |
| Q27 | date | PK |  | SI | Impresion2 |
| Q28 | date | PK |  | SI | Impresion3 |
| Q29 | date | PK |  | SI | Preparación biomecánica y provisorio2 |
| Q30 | date | PK |  | SI | Preparación biomecánica y provisorio3 |
| Q31 | date | PK |  | SI | Instalación de perno muñón + prueba de color 1 |
| Q32 | date | PK |  | SI | Instalación de perno muñón + prueba de color 2    ... |
| Q33 | date | PK |  | SI | Instalación de perno muñón + prueba de color 3 |
| Q34 | date | PK |  | SI | Altura y/o prueba de base + prueba de color 1     ... |
| Q35 | date | PK |  | SI | Altura y/o prueba de base + prueba de color 2 |
| Q36 | date | PK |  | SI | Altura y/o prueba de base + prueba de color 3 |
| Q37 | date | PK |  | SI | Prueba de Casqueta, prueba de porcelana 1 |
| Q38 | date | PK |  | SI | Prueba de Casqueta, prueba de porcelana 2 |
| Q39 | date | PK |  | SI | Prueba de Casqueta, prueba de porcelana 3 |
| Q40 | varchar | PK |  | SI | Color 1 |
| Q41 | date | PK |  | SI | Prueba de porcelana  |
| Q42 | date | PK |  | SI | Cementación Alta |
| Q43 | date | PK |  | SI | Control 2 |
| Q44 | date | PK |  | SI | Control |
| Q45 | varchar | PK |  | SI | Color 2 |
| Q47 | varchar | PK |  | SI | Color 5 |
| Q48 | varchar | PK |  | SI | Color 4 |
| Q49 | varchar | PK |  | SI | Color 6 |
| Q50 | varchar | PK |  | SI | Color 3 |
| Q51 | varchar | PK |  | SI | Color |
| Q52 | varchar | PK |  | SI | Digitado por |
| QRem1 | date | PK |  | SI | Instalación/Alta  |
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