# SQLUser.MR_Allergy

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Registro de **Alergias** del paciente.

Documenta alergias conocidas:
- Medicamentos
- Alimentos
- Sustancias ambientales

**Campos clave:**
- MRALG_ParRef: Referencia al registro medico
- MRALG_Allergy_DR: Tipo de alergia
- MRALG_Reaction: Reaccion observada
- MRALG_Severity: Severidad

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRALL_MRADM_ParRef | bigint | PK |  | NO | Des Ref to MRADM |
| MRALL_ALG_DR | varchar |  | FK | SI | Des Ref to ALG |
| MRALL_Childsub | numeric |  |  | NO | MRALL Childsub (NewKey) |
| MRALL_Date | date |  |  | SI | Date |
| MRALL_DocCode_DR | varchar |  | FK | NO | Des Ref to CTPCP |
| MRALL_Entered | varchar |  |  | SI | Entered Allergy (Comp) |
| MRALL_OthAllergy | varchar |  |  | SI | Other Allergy |
| MRALL_PHCGE_DR | bigint |  | FK | SI | Des Ref to PHCGE |
| MRALL_PHCSC_DR | varchar |  | FK | SI | Des Ref to PHCSC |
| MRALL_Reaction | varchar |  |  | SI | Reaction on allergy |
| MRALL_RowId | varchar |  |  | NO | - |
| MRALL_Sort | varchar |  |  | SI | MRALL_Sort |
| MRALL_Status | varchar |  |  | SI | Status of Allergy |
| MRALL_Time | time |  |  | SI | Time |
| MRALL_Type_DR | bigint |  | FK | SI | Des Ref to MRC Allergy Type |
| Q01 | - |  |  | SI | Edad del Paciente |
| Q02 | - |  |  | SI | Frecuencia Respiratoria &lt |
| Q03 | - |  |  | SI | Frecuencia Respiratoria Mayor o Igual a 6 meses |
| Q04 | - |  |  | SI | Sibilancias |
| Q05 | - |  |  | SI | Cianosis |
| Q06 | - |  |  | SI | Retracción |
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