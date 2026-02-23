# SQLUser.ARC_ItemAgeSexRestriction

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGE_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| AGE_AgeFrom | varchar |  |  | SI | Age From |
| AGE_AgeTo | varchar |  |  | SI | AgeTo |
| AGE_Childsub | double |  |  | NO | Childsub |
| AGE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGE_CreatedDate | date |  |  | SI | Created Date |
| AGE_CreatedTime | time |  |  | SI | Created Time |
| AGE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGE_RowId | varchar |  |  | NO | - |
| AGE_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| AGE_UpdatedDate | date |  |  | SI | Updated Date |
| AGE_UpdatedTime | time |  |  | SI | Updated Time |
| AGE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Motivo de Consulta |
| Q02 | - |  |  | SI | Control de Mantención |
| Q03 | - |  |  | SI | Evaluación de Ansiedad |
| Q04 | - |  |  | SI | Malos Habitos |
| Q05 | - |  |  | SI | Examen Intraoral 2 |
| Q06 | - |  |  | SI | Mucosa |
| Q07 | - |  |  | SI | Periodonto |
| Q08 | - |  |  | SI | Observacion Mucosa |
| Q09 | - |  |  | SI | Oclusión |
| Q10 | - |  |  | SI | Alteración del Esmalte |
| Q24 | - |  |  | SI | Fumador |
| Q25 | - |  |  | SI | Observacion Malos Habitos |
| Q26 | - |  |  | SI | Hábitos de higiene |
| Q27 | - |  |  | SI | Hábitos de higiene (frecuencia) |
| Q28 | - |  |  | SI | MER |
| Q28ObsDR | - |  |  | SI | MER DR |
| Q29 | - |  |  | SI | Condición del Paciente |
| Q30 | - |  |  | SI | Otros Antecedentes |
| Q31 | - |  |  | SI | Examen Intraoral |
| Q32 | - |  |  | SI | Número Total de Dientes Primarios en Boca |
| Q33 | - |  |  | SI | Número Total de Dientes Permanentes&nbsp |
| Q35 | - |  |  | SI | Consumo Dieta Cariogenica |
| Q36 | - |  |  | SI | Educacion en Tecnica de Higiene Bucal indicada |
| Q41 | - |  |  | SI | Educacion individual con instruccion de tecnica de... |
| Q45 | - |  |  | SI | Observacion Educacion en Tecnica de Higiene Bucal ... |
| Q51 | - |  |  | SI | Observacion Consumo Dieta Cariogenica |
| Q52 | - |  |  | SI | Observacion Periodonto |
| Q53 | - |  |  | SI | Observacion Oclusión |
| Q54 | - |  |  | SI | Observacion Alteración del Esmalte |
| QCO | - |  |  | SI | Colegio |
| QCU | - |  |  | SI | Curso |
| QJN | - |  |  | SI | Paciente Junaeb |
| QNE | - |  |  | SI | Nivel de Escolaridad |
| QRem1 | - |  |  | SI | Instalación/Alta |
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