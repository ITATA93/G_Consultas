# questionnaire.QTCEEXGINE

> Examen Ginecológico

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Ginecológico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Comentario Examen Ginecológico |
| Q02 | bit |  |  | SI | Resto del Examen Ginecológico realizado, sin alter... |
| Q03 | varchar |  |  | SI | Inspección |
| Q05 | varchar |  |  | SI | Tacto Vaginal |
| Q06 | varchar |  |  | SI | Residuo Vaginal |
| Q07 | bit |  |  | SI | Paredes vaginales elásticas. Mucosa vaginal normal... |
| Q08 | bit |  |  | SI | Saco de Douglas libre |
| Q09 | bit |  |  | SI | Cuello uterino de consistencia y tamaño normal |
| Q10 | bit |  |  | SI | Útero en antero versión, de tamaño y consistencia ... |
| Q11 | bit |  |  | SI | Flujo Vaginal normal |
| Q12 | bit |  |  | SI | Anexos libres e indoloros |
| Q13 | bit |  |  | SI | Parámetros normales |
| Q14 | bit |  |  | SI | Labios mayores y menores de tamaño y aspecto norma... |
| Q15 | bit |  |  | SI | Clítoris de tamaño y aspecto normal |
| Q16 | bit |  |  | SI | Glándulas de Bartolino normales |
| Q17 | varchar |  |  | SI | Descripción Tacto Vaginal |
| Q18 | varchar |  |  | SI | Descripción Especuloscopía |
| Q19 | bit |  |  | SI | Vagina de elasticidad conservada |
| Q20 | bit |  |  | SI | Cuello central de coloración normal, sin lesiones ... |
| Q21 | varchar |  |  | SI | Descripción Examen Mamas |
| Q22 | bit |  |  | SI | Mamas de tamaño y desarrollo normal, simétricas |
| Q23 | bit |  |  | SI | No se palpan masas ni adenopatías locales |
| Q24 | bit |  |  | SI | Pezones sin lesiones ni secreción anormal |
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