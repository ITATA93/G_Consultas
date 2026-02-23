# SQLUser.MRC_ICDDxEdition

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ED_ParRef | bigint | PK |  | NO | MRC_ICDDx Parent Reference |
| ED_Childsub | double |  |  | NO | Childsub |
| ED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ED_CreatedDate | date |  |  | SI | Created Date |
| ED_CreatedTime | time |  |  | SI | Created Time |
| ED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ED_DateFrom | date |  |  | SI | DateFrom |
| ED_DateTo | date |  |  | SI | DateTo |
| ED_Edition_DR | bigint |  | FK | SI | Des Ref Edition |
| ED_RowId | varchar |  |  | NO | - |
| ED_UpdatedDate | date |  |  | SI | Updated Date |
| ED_UpdatedTime | time |  |  | SI | Updated Time |
| ED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Peso  Actual |
| Q01ObsDR | - |  |  | SI | Peso  Actual DR |
| Q02 | - |  |  | SI | Fecha |
| Q03 | - |  |  | SI | Peso Anterior |
| Q05 | - |  |  | SI | Clasificación |
| Q06 | - |  |  | SI | Variacion de Peso |
| Q07 | - |  |  | SI | Ingesta Alimentaria en relación a lo habitual |
| Q09 | - |  |  | SI | Patología de baja demanda metabólica: Hipoglicemia... |
| Q10 | - |  |  | SI | Severidad de la Enfermedad |
| Q11 | - |  |  | SI | Pérdida de Peso Involuntaria en 1 Mes |
| Q12 | - |  |  | SI | Pacientes crónicos c / complicaciones agudas. Frac... |
| Q13 | - |  |  | SI | Cirugía mayor abdominal.Neumonía severa. EPOC desc... |
| Q14 | - |  |  | SI | Shock. Pancreatitis, Balthzar D y E. TEC grave, Po... |
| Q15 | - |  |  | SI | Clasificación |
| Q16 | - |  |  | SI | Observaciones |
| Q17 | - |  |  | SI | Fecha Peso Anterior |
| Q18 | - |  |  | SI | Peso |
| Q18ObsDR | - |  |  | SI | Peso DR |
| Q19 | - |  |  | SI | Talla |
| Q19ObsDR | - |  |  | SI | Talla DR |
| Q20 | - |  |  | SI | IMC |
| Q21 | - |  |  | SI | Estado Nutricional |
| Q21ObsDR | - |  |  | SI | Estado Nutricional DR |
| Q22 | - |  |  | SI | Kg |
| Q23 | - |  |  | SI | Kg |
| Q24 | - |  |  | SI | Kg |
| Q25 | - |  |  | SI | cm |
| Q26 | - |  |  | SI | Peso Habitual |
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