# SQLUser.ARC_PackageGroupPrice

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRICE_ParRef | bigint | PK |  | NO | ARC_PackageGroup Parent Reference |
| PRICE_Childsub | double |  |  | NO | Childsub |
| PRICE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRICE_CreatedDate | date |  |  | SI | Created Date |
| PRICE_CreatedTime | time |  |  | SI | Created Time |
| PRICE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRICE_DateFrom | date |  |  | SI | DateFrom |
| PRICE_DateTo | date |  |  | SI | DateTo |
| PRICE_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| PRICE_Price | double |  |  | SI | Price |
| PRICE_Rank | integer |  |  | SI | Rank |
| PRICE_RowId | varchar |  |  | NO | - |
| PRICE_UpdatedDate | date |  |  | SI | Updated Date |
| PRICE_UpdatedTime | time |  |  | SI | Updated Time |
| PRICE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edad |
| Q02 | - |  |  | SI | Paciente |
| Q03 | - |  |  | SI | Apoderado |
| Q04 | - |  |  | SI | Médico Responsable |
| Q05 | - |  |  | SI | Diagnóstico Médico |
| Q06 | - |  |  | SI | Indicación Médica |
| Q07 | - |  |  | SI | ¿Es Hipertenso (a)? |
| Q08 | - |  |  | SI | Si es Hipertenso (a) ¿está controlado (a)? |
| Q09 | - |  |  | SI | ¿Es paciente con patología cardíaca? |
| Q10 | - |  |  | SI | ¿Utiliza marcapasos? |
| Q11 | - |  |  | SI | Sexo |
| Q12 | - |  |  | SI | ¿Está embarazada? |
| Q13 | - |  |  | SI | ¿Es Diabético (a)? |
| Q14 | - |  |  | SI | Si es Diabético (a) ¿está controlado (a)? |
| Q15 | - |  |  | SI | ¿Se ha sometido a alguna intervención quirúrgica e... |
| Q16 | - |  |  | SI | ¿Cuál/es? |
| Q17 | - |  |  | SI | ¿Utiliza algún tipo de prótesis traumatológica? |
| Q18 | - |  |  | SI | ¿Padece alguna enfermedad crónica? |
| Q19 | - |  |  | SI | ¿Cuál/es? |
| Q20 | - |  |  | SI | ¿Ingiere alguno de estos medicamentos? (Medicament... |
| Q21 | - |  |  | SI | Nombre/s |
| Q22 | - |  |  | SI | ¿Recibió indicaciones escritas antes de iniciar su... |
| Q23 | - |  |  | SI | ¿Ha presentado o presenta alguna alteración de sen... |
| Q24 | - |  |  | SI | ¿Ha presentado caídas en los últimos 3 meses? |
| Q25 | - |  |  | SI | ¿Presenta o ha presentado alguna enfermedad o cond... |
| Q26 | - |  |  | SI | ¿Utiliza alguna ayuda técnica? como bastones, sill... |
| Q27 | - |  |  | SI | ¿Cual? |
| Q28 | - |  |  | SI | ¿Presenta alguna alteración visual o auditiva? |
| Q29 | - |  |  | SI | Medicamentos |
| Q30 | - |  |  | SI | Otros Medicamentos |
| Q31 | - |  |  | SI | Comentarios Adicionales |
| Q32 | - |  |  | SI | Nombre Kinesiologo (a) |
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