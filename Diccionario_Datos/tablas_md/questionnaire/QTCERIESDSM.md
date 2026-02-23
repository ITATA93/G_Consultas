# questionnaire.QTCERIESDSM

> Categorizacion Riesgo - Dependencia CUDYR-SM

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Categorizacion Riesgo - Dependencia CUDYR-SM

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Cuidados en Confort y Bienestar: Cuidado person... |
| Q02 | varchar |  |  | SI | 2. Cuidados en Deambulación, Movilización Transpor... |
| Q03 | varchar |  |  | SI | 3. Cuidados de Alimentación e Hidratación |
| Q04 | varchar |  |  | SI | 4. Cuidados en Eliminación requeridos según recepc... |
| Q05 | varchar |  |  | SI | 5. Apoyo Emocional, Psicosocial |
| Q06 | varchar |  |  | SI | 6. Vigilancia por Alteración de Conciencia, Riesgo... |
| Q07 | varchar |  |  | SI | 7. Medición diaria de Signos Vitales (2 o mas pará... |
| Q08 | varchar |  |  | SI | 8. Balance Hídrico |
| Q09 | varchar |  |  | SI | 9. Cuidados para integridad de la Piel y Curacione... |
| Q10 | varchar |  |  | SI | 10. Intervención en Agitación: Psicomotora; y/o Au... |
| Q11 | varchar |  |  | SI | 11. lntervención en Riesgo de Abandono de la Unida... |
| Q12 | varchar |  |  | SI | 12. Intervenciones Profesionales |
| Q13 | varchar |  |  | SI | 13. Administración de Tratamiento Farmacológico |
| Q14 | varchar |  |  | SI | 14. Presencia de Elementos Invasivos |
| Q15 | varchar |  |  | SI | Escala de Dependencia |
| Q16 | varchar |  |  | SI | Escala de Riesgo |
| Q17 | varchar |  |  | SI | Resultado Escala de Riesgo |
| Q18 | varchar |  |  | SI | Resultado Escala de Dependencia |
| Q19 | varchar |  |  | SI | Resultado Riesgo Dependencia |
| Q19ObsDR | varchar |  | FK | SI | Resultado Riesgo Dependencia DR |
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