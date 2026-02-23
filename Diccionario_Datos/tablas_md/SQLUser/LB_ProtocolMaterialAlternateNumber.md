# SQLUser.LB_ProtocolMaterialAlternateNumber

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBPTMAN_ParRef | varchar | PK |  | NO | Patent |
| LBPTMAN_Department_DR | bigint |  | FK | SI | Department |
| LBPTMAN_Function | varchar |  |  | SI | Function
Indicates the purpose of the number and ... |
| LBPTMAN_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBPTMAN_Number | varchar |  |  | NO | Number |
| LBPTMAN_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Control Neurológico |
| Q02 | - |  |  | SI | Fecha Control Neurológico |
| Q03 | - |  |  | SI | Crisis Epilépticas |
| Q04 | - |  |  | SI | Fecha Última Crísis |
| Q05 | - |  |  | SI | GOT |
| Q05ObsDR | - |  |  | SI | GOT DR |
| Q06 | - |  |  | SI | GPT |
| Q06ObsDR | - |  |  | SI | GPT DR |
| Q07 | - |  |  | SI | Creatinina |
| Q07ObsDR | - |  |  | SI | Creatinina DR |
| Q08 | - |  |  | SI | Hemograma |
| Q08ObsDR | - |  |  | SI | Hemograma DR |
| Q09 | - |  |  | SI | Sodio |
| Q09ObsDR | - |  |  | SI | Sodio DR |
| Q10 | - |  |  | SI | Potasio |
| Q10ObsDR | - |  |  | SI | Potasio DR |
| Q11 | - |  |  | SI | Cloro |
| Q11ObsDR | - |  |  | SI | Cloro DR |
| Q12 | - |  |  | SI | Tratamiento Farmacológico |
| Q13 | - |  |  | SI | Fármacos |
| Q14 | - |  |  | SI | Otro |
| Q15 | - |  |  | SI | Adherencia |
| Q16 | - |  |  | SI | Síntomas Autonómicos |
| Q17 | - |  |  | SI | Síntomas Psíquicos |
| Q18 | - |  |  | SI | Otro Síntoma Autonómico |
| Q19 | - |  |  | SI | Escolaridad |
| Q20 | - |  |  | SI | Derivación |
| Q21 | - |  |  | SI | Peso Anterior |
| Q22 | - |  |  | SI | Peso Actual |
| Q22ObsDR | - |  |  | SI | Peso Actual DR |
| Q23 | - |  |  | SI | P/E |
| Q24 | - |  |  | SI | T/E |
| Q25 | - |  |  | SI | P/T |
| Q26 | - |  |  | SI | IMC |
| Q27 | - |  |  | SI | Tratamiento Anticonceptivo |
| Q28 | - |  |  | SI | Cual Tratamiento Anticonceptivo |
| Q29 | - |  |  | SI | Derivación Neurólogo |
| Q30 | - |  |  | SI | Control Embarazo |
| Q31 | - |  |  | SI | Uso de Drogas Ilícitas |
| Q32 | - |  |  | SI | ¿Cuál? |
| Q33 | - |  |  | SI | Intervención Psicológica |
| Q34 | - |  |  | SI | Educación a la Familia |
| Q35 | - |  |  | SI | Adherencia al Tratamiento |
| Q36 | - |  |  | SI | Efectos Colaterales del Tratamiento |
| Q37 | - |  |  | SI | Asistencia a Controles |
| Q38 | - |  |  | SI | Dieta Cetogénica |
| Q39 | - |  |  | SI | Otra Intervención |
| Q40 | - |  |  | SI | TP |
| Q40ObsDR | - |  |  | SI | TP DR |
| Q41 | - |  |  | SI | Electrolitos Plasmáticos |
| Q42 | - |  |  | SI | N° de Crisis |
| Q43 | - |  |  | SI | Centil Peso/Edad |
| Q44 | - |  |  | SI | Centil Talla/Edad |
| Q45 | - |  |  | SI | Centil Peso/Talla |
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