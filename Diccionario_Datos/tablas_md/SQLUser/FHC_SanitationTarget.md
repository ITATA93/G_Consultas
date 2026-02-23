# SQLUser.FHC_SanitationTarget

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCST_RowId | bigint | PK |  | NO | - |
| FHCST_Code | varchar |  |  | NO | Sanitation Target Code |
| FHCST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCST_CreatedDate | date |  |  | SI | Created Date |
| FHCST_CreatedTime | time |  |  | SI | Created Time |
| FHCST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCST_DateFrom | date |  |  | NO | Date From |
| FHCST_DateTo | date |  |  | SI | Date To |
| FHCST_Desc | varchar |  |  | NO | Sanitation Target Description |
| FHCST_NationalCode | varchar |  |  | SI | National Code |
| FHCST_Owner | varchar |  |  | SI | Owner |
| FHCST_UpdatedDate | date |  |  | SI | Updated Date |
| FHCST_UpdatedTime | time |  |  | SI | Updated Time |
| FHCST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Cuidados en Confort y Bienestar: Cambio de Ropa |
| Q02 | - |  |  | SI | 2. Cuidados en Confort y Bienestar: Movilización y... |
| Q03 | - |  |  | SI | 3. Cuidados de Alimentación |
| Q04 | - |  |  | SI | 4. Cuidados de Eliminación |
| Q05 | - |  |  | SI | 5. Apoyo Psicosocial y Emocional |
| Q06 | - |  |  | SI | 6. Vigilancia |
| Q07 | - |  |  | SI | 7. Medición diaria de Signos Vitales (2 o mas pará... |
| Q08 | - |  |  | SI | 8. Balance Hídrico |
| Q09 | - |  |  | SI | 9. Cuidados en Oxigenoterapia |
| Q10 | - |  |  | SI | 10. Cuidados diarios de la Vía Aérea |
| Q11 | - |  |  | SI | 11. Intervenciones Profesionales |
| Q12 | - |  |  | SI | 12. Cuidados de Piel y Curaciones |
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