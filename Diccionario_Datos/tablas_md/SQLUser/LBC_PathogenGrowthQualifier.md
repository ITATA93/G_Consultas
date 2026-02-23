# SQLUser.LBC_PathogenGrowthQualifier

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAGQ_RowID | bigint | PK |  | NO | - |
| LBCPAGQ_Code | varchar |  |  | SI | Code
Exception for collation to allow + and - sig... |
| LBCPAGQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAGQ_CreatedDate | date |  |  | SI | Created Date |
| LBCPAGQ_CreatedTime | time |  |  | SI | Created Time |
| LBCPAGQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPAGQ_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAGQ_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAGQ_Desc | varchar |  |  | SI | Description
Exception for collation to allow + an... |
| LBCPAGQ_Owner | varchar |  |  | SI | Owner |
| LBCPAGQ_RestrictToPathogenGroups | varchar |  |  | SI | Restrict To Pathogen groups |
| LBCPAGQ_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPAGQ_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPAGQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Servicio |
| Q02 | - |  |  | SI | Percepción Sensorial |
| Q03 | - |  |  | SI | Movilidad |
| Q04 | - |  |  | SI | Actividad |
| Q05 | - |  |  | SI | Humedad |
| Q06 | - |  |  | SI | Nutrición |
| Q07 | - |  |  | SI | Fuerzas de fricción y cizalla |
| Q08 | - |  |  | SI | Reevaluación |
| Q09 | - |  |  | SI | Información a familiar (Primer Contacto) |
| Q10 | - |  |  | SI | Fecha de información a familia |
| Q11 | - |  |  | SI | Aceptación de Medidas |
| Q12 | - |  |  | SI | Nombre del Familiar |
| Q13 | - |  |  | SI | Nombre Responsable |
| Q14 | - |  |  | SI | Grado |
| Q14ObsDR | - |  |  | SI | Grado DR |
| Q15 | - |  |  | SI | Etiqueta Riesgo Bajo |
| Q16 | - |  |  | SI | Etiqueta Riesgo Moderado |
| Q17 | - |  |  | SI | Etiqueta Riesgo Alto |
| Q18 | - |  |  | SI | Se realizan medidas según riesgo evaluado |
| Q19 | - |  |  | SI | Razón de No Realización |
| Q20 | - |  |  | SI | Servicio |
| Q21 | - |  |  | SI | Fecha de la Actividad |
| Q22 | - |  |  | SI | Hora de la Actividad |
| Q30 | - |  |  | SI | Examen de Piel: Valoración Diaria |
| Q31 | - |  |  | SI | Higiene de la Piel: Diario 3 veces/día |
| Q32 | - |  |  | SI | Cambios Posturales: Cada 2 horas |
| Q33 | - |  |  | SI | Superficies de Apoyo: Dinámicas |
| Q35 | - |  |  | SI | Examen de Piel: Valoración Diaria |
| Q36 | - |  |  | SI | Higiene de la Piel: Diario 2 veces/día |
| Q37 | - |  |  | SI | Cambios Posturales: Cada 2-3 horas |
| Q38 | - |  |  | SI | Superficie de Apoyo: Dinámicas |
| Q40 | - |  |  | SI | Examen de Piel: Valoración Diaria |
| Q41 | - |  |  | SI | Higiene de la Piel: Diario 2 veces/día |
| Q42 | - |  |  | SI | Cambios Posturales: Cada 4 horas |
| Q43 | - |  |  | SI | Superficies de Apoyo: Estáticas |
| Q44 | - |  |  | SI | Cada 7 días |
| Q45 | - |  |  | SI | Cada 3 días |
| Q46 | - |  |  | SI | Cada 7 días |
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