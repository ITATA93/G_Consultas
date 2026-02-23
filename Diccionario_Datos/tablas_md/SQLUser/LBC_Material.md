# SQLUser.LBC_Material

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCM_RowID | bigint | PK |  | NO | - |
| LBCM_ApplySpecimenValidity | varchar |  |  | SI | Apply specimen validity to this materia (Y/N) |
| LBCM_BillingMode | varchar |  |  | SI | Billing Mode |
| LBCM_Code | varchar |  |  | NO | Code |
| LBCM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCM_CreatedDate | date |  |  | SI | Created Date |
| LBCM_CreatedTime | time |  |  | SI | Created Time |
| LBCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCM_DateFrom | date |  |  | SI | Date Active From |
| LBCM_DateTo | date |  |  | SI | Date Active To |
| LBCM_DefaultObservationDR | bigint |  | FK | SI | Default Observation |
| LBCM_Desc | varchar |  |  | NO | Description |
| LBCM_ExtendValidity | double |  |  | SI | Extend Validity by X hrs |
| LBCM_NumberRequired | integer |  |  | SI | Number of Labels Required |
| LBCM_Owner | varchar |  |  | SI | Owner |
| LBCM_PrintLabels | varchar |  |  | SI | Do we require labels (Y/N) |
| LBCM_Report_DR | bigint |  | FK | SI | Report |
| LBCM_Type | varchar |  |  | SI | None standard columns
Material Type |
| LBCM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Diabetes |
| Q02 | - |  |  | SI | Hipertensión o enfermedad cardiovascular |
| Q03 | - |  |  | SI | Antecedentes nefrourológicos: |
| Q04 | - |  |  | SI | Familiares 1º grado con ERC |
| Q05 | - |  |  | SI | Peso |
| Q06 | - |  |  | SI | Presión Sistólica |
| Q07 | - |  |  | SI | Presión Diastólica |
| Q08 | - |  |  | SI | Creatinina |
| Q09 | - |  |  | SI | Velocidad Filtración Glomerular (VFG) informada po... |
| Q10 | - |  |  | SI | Proteinura Confirmada: |
| Q11 | - |  |  | SI | Hematuria Opción |
| Q12 | - |  |  | SI | Otras alteraciones: |
| Q13 | - |  |  | SI | Otras alteraciones: |
| Q14 | - |  |  | SI | Paciente diabético: |
| Q15 | - |  |  | SI | Paciente no diabético: |
| Q17 | - |  |  | SI | Etapa Enfermedad Renal Crónica |
| Q17ObsDR | - |  |  | SI | Etapa Enfermedad Renal Crónica DR |
| Q18 | - |  |  | SI | Conducta Final |
| Q19 | - |  |  | SI | Infomdo Lab |
| Q20 | - |  |  | SI | Hombre |
| Q21Mujer | - |  |  | SI | Mujer |
| Q23 | - |  |  | SI | Microalbuminuría Opción |
| Q24 | - |  |  | SI | Proteinuría |
| Q24ObsDR | - |  |  | SI | Proteinuría DR |
| Q25 | - |  |  | SI | Microalbuminuría |
| Q25ObsDR | - |  |  | SI | Microalbuminuría DR |
| Q26 | - |  |  | SI | RAC |
| Q26ObsDR | - |  |  | SI | RAC DR |
| Q27 | - |  |  | SI | Hombre Raza |
| Q28 | - |  |  | SI | Mujer Raza |
| Q29 | - |  |  | SI | Velocidad de Filtración Glomerular Estimada |
| Q29ObsDR | - |  |  | SI | Velocidad de Filtración Glomerular Estimada DR |
| Q30 | - |  |  | SI | Velocidad de Filtración Glomerular (Cockcroft - Ga... |
| Q30ObsDR | - |  |  | SI | Velocidad de Filtración Glomerular (Cockcroft - Ga... |
| Q31 | - |  |  | SI | Categoría de Albuminuria |
| Q31ObsDR | - |  |  | SI | Categoría de Albuminuria DR |
| Q32 | - |  |  | SI | Creatinuria |
| Q33 | - |  |  | SI | Proteinuria Opción |
| Q34 | - |  |  | SI | Hematuria Fecha |
| Q35 | - |  |  | SI | Proteinuria  Fecha |
| Q36 | - |  |  | SI | Microalbuminuria Opción |
| Q37 | - |  |  | SI | Creatininuria Opción |
| Q38 | - |  |  | SI | Creatinemia Opción |
| Q39 | - |  |  | SI | Razón albuminuria-Creatininuria Opción |
| Q40 | - |  |  | SI | Microalbuminuría Fecha |
| Q41 | - |  |  | SI | Creatinemia Fecha |
| Q42 | - |  |  | SI | Creatininuria Fecha |
| Q43 | - |  |  | SI | Razón albuminuria-Creatininuria Fecha |
| Q44 | - |  |  | SI | Hematuria |
| Q44ObsDR | - |  |  | SI | Hematuria DR |
| Q45 | - |  |  | SI | Proteinuria |
| Q45ObsDR | - |  |  | SI | Proteinuria DR |
| Q46 | - |  |  | SI | Fecha del Examen |
| QEdadPacinte | - |  |  | SI | Edad del Paciente |
| QRPERC | - |  |  | SI | Resultado Pauta de Enfermedad Renal Crónica |
| QRPERCObsDR | - |  |  | SI | Resultado Pauta de Enfermedad Renal Crónica DR |
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