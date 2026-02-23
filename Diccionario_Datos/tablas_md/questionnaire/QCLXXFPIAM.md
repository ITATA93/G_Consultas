# questionnaire.QCLXXFPIAM

> Ficha para Indicación de Andador Móvil

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha para Indicación de Andador Móvil

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Condición |
| Q02 | varchar |  |  | SI | Criterios |
| Q03 | varchar |  |  | SI | Trastorno del Equilibrio |
| Q04 | varchar |  |  | SI | Observación |
| Q05 | varchar |  |  | SI | Caídas frecuentes |
| Q06 | varchar |  |  | SI | Observación |
| Q07 | varchar |  |  | SI | Enfermedad de Parkinson |
| Q08 | varchar |  |  | SI | Observación |
| Q09 | varchar |  |  | SI | Artrosis de cadera y rodilla avanzada sin alcance ... |
| Q10 | varchar |  |  | SI | Observación |
| Q11 | varchar |  |  | SI | Disnea de esfuerzo que requiera descansos frecuent... |
| Q12 | varchar |  |  | SI | Observación |
| Q13 | varchar |  |  | SI | Desviación severa de columna |
| Q14 | varchar |  |  | SI | Observación  |
| Q15 | varchar |  |  | SI | Indemnidad de extremidades superiores |
| Q16 | varchar |  |  | SI | Observación |
| Q17 | varchar |  |  | SI | Adultos mayores con demencia en etapa inicial requ... |
| Q18 | varchar |  |  | SI | Observación |
| Q19 | varchar |  |  | SI | Cuadros de demencia en etapa inicial requerirán su... |
| Q20 | varchar |  |  | SI | Observación |
| Q21 | varchar |  |  | SI | Compromiso moderado a severo del equilibrio |
| Q22 | varchar |  |  | SI | Observación |
| Q23 | varchar |  |  | SI | Residencia en lugar que permita los desplazamiento... |
| Q24 | varchar |  |  | SI | Observación |
| Q25 | varchar |  |  | SI | Su entorno (patio y barrio) debe permitir libertad... |
| Q26 | varchar |  |  | SI | Observación |
| Q27 | varchar |  |  | SI | No indicar en |
| Q28 | varchar |  |  | SI | Problemas de: conciencia |
| Q29 | varchar |  |  | SI | Observación |
| Q30 | varchar |  |  | SI | Problemas cognitivos |
| Q31 | varchar |  |  | SI | Observación |
| Q32 | varchar |  |  | SI | Amputados |
| Q33 | varchar |  |  | SI | Observación |
| Q34 | varchar |  |  | SI | Hemipléjicos |
| Q35 | varchar |  |  | SI | Observación |
| Q36 | varchar |  |  | SI | Otras Observaciones |
| Q37 | varchar |  |  | SI | Consideraciones |
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