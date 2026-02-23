# SQLUser.LBC_BPUnitStatus

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPUS_RowID | bigint | PK |  | NO | - |
| LBCBPUS_Code | varchar |  |  | NO | Code |
| LBCBPUS_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| LBCBPUS_CreatedDate | date |  |  | SI | Created Date |
| LBCBPUS_CreatedTime | time |  |  | SI | Created Time |
| LBCBPUS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPUS_Desc | varchar |  |  | SI | Description |
| LBCBPUS_Owner | varchar |  |  | SI | Owner |
| LBCBPUS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPUS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPUS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Crisis Epilépticas |
| Q02 | - |  |  | SI | Fecha Última Crisis |
| Q03 | - |  |  | SI | Peso Anterior |
| Q04 | - |  |  | SI | Peso Actual |
| Q04ObsDR | - |  |  | SI | Peso Actual DR |
| Q05 | - |  |  | SI | P/E |
| Q06 | - |  |  | SI | T/E |
| Q07 | - |  |  | SI | P/T |
| Q08 | - |  |  | SI | IMC |
| Q09 | - |  |  | SI | Consumo de Drogas |
| Q10 | - |  |  | SI | Cual Droga |
| Q11 | - |  |  | SI | Escolaridad |
| Q12 | - |  |  | SI | Derivación |
| Q13 | - |  |  | SI | GOT |
| Q13ObsDR | - |  |  | SI | GOT DR |
| Q14 | - |  |  | SI | GPT |
| Q14ObsDR | - |  |  | SI | GPT DR |
| Q15 | - |  |  | SI | Creatinemia |
| Q15ObsDR | - |  |  | SI | Creatinemia DR |
| Q16 | - |  |  | SI | Hemograma |
| Q16ObsDR | - |  |  | SI | Hemograma DR |
| Q17 | - |  |  | SI | Sodio |
| Q17ObsDR | - |  |  | SI | Sodio DR |
| Q18 | - |  |  | SI | Potasio |
| Q18ObsDR | - |  |  | SI | Potasio DR |
| Q19 | - |  |  | SI | Cloro |
| Q19ObsDR | - |  |  | SI | Cloro DR |
| Q20 | - |  |  | SI | Exámenes al Día |
| Q21 | - |  |  | SI | Tratamiento Farmacológico |
| Q22 | - |  |  | SI | Fármacos |
| Q23 | - |  |  | SI | Otro Fármaco |
| Q24 | - |  |  | SI | Adherencia |
| Q25 | - |  |  | SI | Efectos Adversos |
| Q26 | - |  |  | SI | Mencione Efecto Adversos |
| Q27 | - |  |  | SI | Intervención Psicológica |
| Q28 | - |  |  | SI | Educación a la Familia |
| Q29 | - |  |  | SI | Adherencia al Tratamiento |
| Q30 | - |  |  | SI | Efectos Colaterales del Tratamiento |
| Q31 | - |  |  | SI | Asistencia a Controles |
| Q32 | - |  |  | SI | Dieta Cetogénica |
| Q33 | - |  |  | SI | Otra Intervención |
| Q34 | - |  |  | SI | Médico |
| Q35 | - |  |  | SI | Enfermera |
| Q36 | - |  |  | SI | Neurólogo |
| Q37 | - |  |  | SI | TP |
| Q37ObsDR | - |  |  | SI | TP DR |
| Q38 | - |  |  | SI | Electrolitos Plasmáticos |
| Q39 | - |  |  | SI | Tratamiento Anticonceptivo |
| Q40 | - |  |  | SI | Derivación Neurólogo |
| Q41 | - |  |  | SI | Control de Embarazo |
| Q42 | - |  |  | SI | Uso de Drogas Ilícitas |
| Q43 | - |  |  | SI | Nombre Tto Aco |
| Q44 | - |  |  | SI | Nombre de Droga |
| Q45 | - |  |  | SI | N° de Crisis |
| Q46 | - |  |  | SI | Centil Peso/Edad |
| Q47 | - |  |  | SI | Centil Talla/Edad |
| Q48 | - |  |  | SI | Centil Peso/Talla |
| Q49 | - |  |  | SI | Control con neurólogo |
| Q50 | - |  |  | SI | Fecha último control neurólogo |
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