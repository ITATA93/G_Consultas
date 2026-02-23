# questionnaire.QCLXXIPVHU

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Diagnostico |
| Q02 | varchar | PK |  | SI | IMC |
| Q02ObsDR | varchar | PK | FK | SI | IMC DR |
| Q03 | varchar | PK |  | SI | Diabetes |
| Q04 | varchar | PK |  | SI | Hipertensión Arterial |
| Q05 | varchar | PK |  | SI | Cáncer |
| Q06 | varchar | PK |  | SI | Inmunoderpresión |
| Q07 | varchar | PK |  | SI | Tabaquismo |
| Q08 | varchar | PK |  | SI | Drogadicción |
| Q09 | varchar | PK |  | SI | Insuficiencia Venosa |
| Q10 | varchar | PK |  | SI | Insuficiencia Arterial |
| Q11 | varchar | PK |  | SI | Otras |
| Q12 | varchar | PK |  | SI | Hematocrito |
| Q13 | varchar | PK |  | SI | Hemoglobina |
| Q14 | varchar | PK |  | SI | VHS |
| Q15 | varchar | PK |  | SI | Albuminemia |
| Q16 | varchar | PK |  | SI | Proteinemia |
| Q17 | varchar | PK |  | SI | Glicemia |
| Q18 | varchar | PK |  | SI | Cultivos |
| Q19 | varchar | PK |  | SI | Otros |
| Q20 | varchar | PK |  | SI | Antibióticos |
| Q21 | varchar | PK |  | SI | Corticoesteroides |
| Q22 | varchar | PK |  | SI | Tratamiento anticoagulante |
| Q23 | varchar | PK |  | SI | Otros |
| Q24 | varchar | PK |  | SI | Aspecto |
| Q25 | varchar | PK |  | SI | Diametro |
| Q26 | varchar | PK |  | SI | Profundidad |
| Q27 | varchar | PK |  | SI | Cantidad Exudado |
| Q28 | varchar | PK |  | SI | Calidad Exudado |
| Q29 | varchar | PK |  | SI | Tejido Esfacelado/Necrótico |
| Q30 | varchar | PK |  | SI | Tejido Granulatorio |
| Q31 | varchar | PK |  | SI | Edema |
| Q32 | varchar | PK |  | SI | Dolor |
| Q33 | varchar | PK |  | SI | Piel Circundante |
| Q34 | varchar | PK |  | SI | Agente Utilizado |
| Q35 | varchar | PK |  | SI | Apósito o Cobertura |
| Q36 | varchar | PK |  | SI | Tipo de Fijación |
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