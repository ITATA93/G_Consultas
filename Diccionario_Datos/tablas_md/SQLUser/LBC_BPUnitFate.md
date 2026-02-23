# SQLUser.LBC_BPUnitFate

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPUF_RowID | bigint | PK |  | NO | - |
| LBCBPUF_Code | varchar |  |  | NO | Code |
| LBCBPUF_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| LBCBPUF_CreatedDate | date |  |  | SI | Created Date |
| LBCBPUF_CreatedTime | time |  |  | SI | Created Time |
| LBCBPUF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPUF_Desc | varchar |  |  | SI | Description |
| LBCBPUF_Owner | varchar |  |  | SI | Owner |
| LBCBPUF_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPUF_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPUF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Control con Neurólogo |
| Q02 | - |  |  | SI | Adherencia a Controles APS |
| Q03 | - |  |  | SI | Adherencia a Indicaciones APS |
| Q04 | - |  |  | SI | GOT |
| Q04ObsDR | - |  |  | SI | GOT DR |
| Q05 | - |  |  | SI | GPT |
| Q05ObsDR | - |  |  | SI | GPT DR |
| Q06 | - |  |  | SI | Creatinina |
| Q06ObsDR | - |  |  | SI | Creatinina DR |
| Q07 | - |  |  | SI | Hemograma |
| Q07ObsDR | - |  |  | SI | Hemograma DR |
| Q08 | - |  |  | SI | Sodio |
| Q08ObsDR | - |  |  | SI | Sodio DR |
| Q09 | - |  |  | SI | Potasio |
| Q09ObsDR | - |  |  | SI | Potasio DR |
| Q10 | - |  |  | SI | Cloro |
| Q10ObsDR | - |  |  | SI | Cloro DR |
| Q11 | - |  |  | SI | INR |
| Q11ObsDR | - |  |  | SI | INR DR |
| Q12 | - |  |  | SI | Otro Examen |
| Q13 | - |  |  | SI | Tratamiento Farmacológico |
| Q14 | - |  |  | SI | Fármacos |
| Q15 | - |  |  | SI | Efectos Secundarios al Tratamiento |
| Q16 | - |  |  | SI | Describir Efectos Secundarios |
| Q17 | - |  |  | SI | Otro Fármaco |
| Q18 | - |  |  | SI | Adherencia |
| Q19 | - |  |  | SI | Laborales |
| Q20 | - |  |  | SI | Económicos |
| Q21 | - |  |  | SI | Psicológicos |
| Q22 | - |  |  | SI | Familiares |
| Q23 | - |  |  | SI | Consumo de Tabaco |
| Q24 | - |  |  | SI | Consumo de Alcohol |
| Q25 | - |  |  | SI | Consumo de Drogas |
| Q26 | - |  |  | SI | Trastorno de Sueño |
| Q27 | - |  |  | SI | Frecuencia de Consumo |
| Q28 | - |  |  | SI | Tipo de Droga |
| Q29 | - |  |  | SI | Observaciones del Trastorno del Sueño |
| Q30 | - |  |  | SI | Electrolitos Plasmáticos |
| Q31 | - |  |  | SI | TP |
| Q31ObsDR | - |  |  | SI | TP DR |
| Q32 | - |  |  | SI | Tratamietno Anticonceptivo |
| Q33 | - |  |  | SI | Tratamiento Adicional |
| Q34 | - |  |  | SI | Control de Embarazo |
| Q35 | - |  |  | SI | Tratamiento Ácido Fólico |
| Q36 | - |  |  | SI | Derivación Neurólogo |
| Q37 | - |  |  | SI | Describa Tto ACO |
| Q38 | - |  |  | SI | Describa Tto Adicional |
| Q39 | - |  |  | SI | Fecha de Última Crísis |
| Q40 | - |  |  | SI | N° de Crisis |
| Q41 | - |  |  | SI | Fecha último control neurólogo |
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