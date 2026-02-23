# SQLUser.FHC_RemovalReason

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCRR_RowId | bigint | PK |  | NO | - |
| FHCRR_Code | varchar |  |  | NO | Removal Reason Code |
| FHCRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCRR_CreatedDate | date |  |  | SI | Created Date |
| FHCRR_CreatedTime | time |  |  | SI | Created Time |
| FHCRR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCRR_DateFrom | date |  |  | NO | Date From |
| FHCRR_DateTo | date |  |  | SI | Date To |
| FHCRR_DefaultRemove | varchar |  |  | SI | Default Remove |
| FHCRR_Desc | varchar |  |  | NO | Removal Reason Description |
| FHCRR_NationalCode | varchar |  |  | SI | National Code |
| FHCRR_Owner | varchar |  |  | SI | Owner |
| FHCRR_UpdatedDate | date |  |  | SI | Updated Date |
| FHCRR_UpdatedTime | time |  |  | SI | Updated Time |
| FHCRR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Cuidados en Confort y Bienestar: Cuidado person... |
| Q02 | - |  |  | SI | 2. Cuidados en Deambulación, Movilización Transpor... |
| Q03 | - |  |  | SI | 3. Cuidados de Alimentación e Hidratación |
| Q04 | - |  |  | SI | 4. Cuidados en Eliminación requeridos según recepc... |
| Q05 | - |  |  | SI | 5. Apoyo Emocional, Psicosocial |
| Q06 | - |  |  | SI | 6. Vigilancia por Alteración de Conciencia, Riesgo... |
| Q07 | - |  |  | SI | 7. Medición diaria de Signos Vitales (2 o mas pará... |
| Q08 | - |  |  | SI | 8. Balance Hídrico |
| Q09 | - |  |  | SI | 9. Cuidados para integridad de la Piel y Curacione... |
| Q10 | - |  |  | SI | 10. Intervención en Agitación: Psicomotora |
| Q11 | - |  |  | SI | 11. lntervención en Riesgo de Abandono de la Unida... |
| Q12 | - |  |  | SI | 12. Intervenciones Profesionales |
| Q13 | - |  |  | SI | 13. Administración de Tratamiento Farmacológico |
| Q14 | - |  |  | SI | 14. Presencia de Elementos Invasivos |
| Q15 | - |  |  | SI | Escala de Dependencia |
| Q16 | - |  |  | SI | Escala de Riesgo |
| Q17 | - |  |  | SI | Resultado Escala de Riesgo |
| Q18 | - |  |  | SI | Resultado Escala de Dependencia |
| Q19 | - |  |  | SI | Resultado Riesgo Dependencia |
| Q19ObsDR | - |  |  | SI | Resultado Riesgo Dependencia DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*