# SQLUser.LBC_DiffCounterRuleCounterMap

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDCRCM_ParRef | varchar | PK |  | NO | Parent table |
| LBCDCRCM_CalFactor | numeric |  |  | SI | Calculation Factor
Default to 1 |
| LBCDCRCM_CalTestItem_DR | bigint |  | FK | SI | Test Set Item for Caldulation of Absolute Values
... |
| LBCDCRCM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDCRCM_CountTestItem_DR | bigint |  | FK | SI | The count used as the source to calculate the othe... |
| LBCDCRCM_IncludeInTotalCount | varchar |  |  | SI | Include In Total Count
Identify if the test set i... |
| LBCDCRCM_Key | varchar |  |  | SI | Char key assigned to the item (ASCII key code as I... |
| LBCDCRCM_RequestTestItem_DR | bigint |  | FK | SI | Test Set Item from Request Test Set
Request Test ... |
| LBCDCRCM_RowID | varchar |  |  | NO | - |
| LBCDCRCM_Sequence | double |  |  | SI | Sequence for The Differential Counter Rule Counter... |
| LBCDCRCM_TriggerTestItems | varchar |  |  | SI | Suppress Test set Item (from Trigger Test Set)
If... |
| Q01 | - |  |  | SI | Tipo de herida |
| Q02 | - |  |  | SI | Otro tipo de herida |
| Q03 | - |  |  | SI | Ubicación de la herida |
| Q04 | - |  |  | SI | Infección de la Herida |
| Q05 | - |  |  | SI | Tratamiento Antibiótico Actual |
| Q06 | - |  |  | SI | Descripción de la herida |
| Q07 | - |  |  | SI | Otra descripción de herida |
| Q08 | - |  |  | SI | Longitud (cm) |
| Q09 | - |  |  | SI | Ancho (cm) |
| Q10 | - |  |  | SI | Profundidad (cm) |
| Q11 | - |  |  | SI | Descripción del exudado |
| Q12 | - |  |  | SI | Otro descripción de contenido drenado |
| Q13 | - |  |  | SI | Acciones Realizadas en la Herida |
| Q14 | - |  |  | SI | Otra Acciones Realizadas en la Herida |
| Q15 | - |  |  | SI | Apósito Primario Utilizado |
| Q16 | - |  |  | SI | Otro apósito primario |
| Q17 | - |  |  | SI | Apósito secundario |
| Q18 | - |  |  | SI | Otro apósito secundario |
| Q19 | - |  |  | SI | Observaciones de la Herida |
| Q20 | - |  |  | SI | Imagen de la herida |
| Q20TxtOnly | - |  |  | SI | Imagen de la herida Plain Text Only |
| Q21 | - |  |  | SI | Actividad Vendaje |
| Q22 | - |  |  | SI | Dimensiones de la herida |
| Q23 | - |  |  | SI | cm |
| Q24 | - |  |  | SI | cm |
| Q25 | - |  |  | SI | cm |
| Q26 | - |  |  | SI | Mecanismo causante de la herida |
| Q27 | - |  |  | SI | Otra descripción del exudado |
| Q28 | - |  |  | SI | Cantidad de exudado |
| Q29 | - |  |  | SI | Presencia de sutura |
| Q30 | - |  |  | SI | Cuál |
| Q31 | - |  |  | SI | Tejido de la herida |
| Q32 | - |  |  | SI | Granulación (%) |
| Q33 | - |  |  | SI | Esfacelo (%) |
| Q34 | - |  |  | SI | Necrótico (%) |
| Q35 | - |  |  | SI | Piel circundante |
| Q36 | - |  |  | SI | Presencia de drenaje |
| Q37 | - |  |  | SI | Cuál |
| Q38 | - |  |  | SI | Tratamiento farmacológico relevante |
| Q39 | - |  |  | SI | Otro fármaco relevante |
| Q40 | - |  |  | SI | Limpieza de la piel |
| Q41 | - |  |  | SI | Limpieza de la herida |
| Q42 | - |  |  | SI | Arrastre mecánico |
| Q43 | - |  |  | SI | Cuál |
| Q44 | - |  |  | SI | Desbridamiento |
| Q45 | - |  |  | SI | Toma de cultivo |
| Q46 | - |  |  | SI | Apósito primario |
| Q47 | - |  |  | SI | Protección de la piel |
| Q48 | - |  |  | SI | Otra protección de la piel |
| Q49 | - |  |  | SI | Fijación |
| Q50 | - |  |  | SI | Otra fijación |
| Q51 | - |  |  | SI | Terapia coadyuvante |
| Q52 | - |  |  | SI | Otra terapia coadyuvante |
| Q53 | - |  |  | SI | Plan de Tratamiento / Comentarios |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*