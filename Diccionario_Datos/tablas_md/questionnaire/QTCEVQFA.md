# questionnaire.QTCEVQFA

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | LUGAR DE CONSULTA |
| Q02 | varchar | PK |  | SI | NOMBRE Y APELLIDO DEL AFECTADO |
| Q03 | date | PK |  | SI | FECHA DE OCURRENCIA DEL ACCIDENTE |
| Q06 | varchar | PK |  | SI | AÑOS |
| Q07 | varchar | PK |  | SI | MESES |
| Q08 | date | PK |  | SI | FECHA DE CONSULTA |
| Q09 | time | PK |  | SI | HORA OCURRENCIA DEL ACCIDENTE |
| Q10 | varchar | PK |  | SI | COMUNA DE ORIGEN DEL  AFECTADO |
| Q11 | bit | PK |  | SI | PETARDO |
| Q12 | bit | PK |  | SI | CHISPITA |
| Q13 | bit | PK |  | SI | ESTRELLITA |
| Q14 | bit | PK |  | SI | VOLADOR |
| Q15 | bit | PK |  | SI | SALTARINA |
| Q16 | bit | PK |  | SI | OTRO |
| Q17 | varchar | PK |  | SI | ¿CUAL? |
| Q18 | varchar | PK |  | SI | ESPECIFIQUE EL LUGAR DONDE SE ADQUIRIO EL FUEGO AR... |
| Q19 | bit | PK |  | SI | PREPARADO EN CASA EN FORMA CASERA |
| Q20 | bit | PK |  | SI | AFECTADO |
| Q21 | bit | PK |  | SI | OTRO |
| Q22 | varchar | PK |  | SI | ¿CUAL? |
| Q30 | bit | PK |  | SI | SUPERFICIAL (A) |
| Q31 | bit | PK |  | SI | INTERMEDIA (AB) |
| Q32 | bit | PK |  | SI | PROFUNDA (B) |
| Q33 | bit | PK |  | SI | SI |
| Q34 | bit | PK |  | SI | NO |
| Q35 | varchar | PK |  | SI | ESPECIFIQUE |
| Q36 | bit | PK |  | SI | ATENCION AMBULATORIA |
| Q37 | bit | PK |  | SI | HOSPITALIZACION |
| Q38 | bit | PK |  | SI | MEDICO |
| Q39 | bit | PK |  | SI | ENFERMERA |
| Q40 | bit | PK |  | SI | AUXILIAR |
| Q41 | varchar | PK |  | SI | NOMBRE |
| Q42 | varchar | PK |  | SI | FIRMA |
| Q45 | varchar | PK |  | SI | LOCALIZACION DE LA QUEMADURA |
| Q47 | varchar | PK |  | SI | SEXO |
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