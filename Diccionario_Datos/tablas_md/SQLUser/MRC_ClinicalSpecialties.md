# SQLUser.MRC_ClinicalSpecialties

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLSPEC_RowID | bigint | PK |  | NO | - |
| CLSPEC_Code | varchar |  |  | NO | Code |
| CLSPEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLSPEC_CreatedDate | date |  |  | SI | Created Date |
| CLSPEC_CreatedTime | time |  |  | SI | Created Time |
| CLSPEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLSPEC_DateFrom | date |  |  | SI | Date From |
| CLSPEC_DateTo | date |  |  | SI | Date To |
| CLSPEC_Desc | varchar |  |  | NO | Description |
| CLSPEC_Owner | varchar |  |  | SI | Owner |
| CLSPEC_UpdatedDate | date |  |  | SI | Updated Date |
| CLSPEC_UpdatedTime | time |  |  | SI | Updated Time |
| CLSPEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQ13 | - |  |  | SI | (null) |
| CQ15 | - |  |  | SI | (null) |
| Q1 | - |  |  | SI | Fecha del Informe |
| Q10 | - |  |  | SI | Nombre del Profesional |
| Q11 | - |  |  | SI | R.U.N del Profesional |
| Q12 | - |  |  | SI | N° de FOLIO |
| Q13 | - |  |  | SI | ¿Diagnóstico corresponde a AUGE? |
| Q14 | - |  |  | SI | El Tratamiento deberá iniciarse a más tardar el: |
| Q15 | - |  |  | SI | ¿Confirma que el diagnóstico pertenece al sistema ... |
| Q2 | - |  |  | SI | Hora del Informe |
| Q3 | - |  |  | SI | Problema de Salud AUGE |
| Q4 | - |  |  | SI | Diagnostico corresponde a AUGE |
| Q5 | - |  |  | SI | Subgrupo o Subproblema AUGE |
| Q6 | - |  |  | SI | Diagnostico |
| Q7 | - |  |  | SI | Fundamentos del Diagnostico |
| Q8 | - |  |  | SI | Tratamiento y/o Indicaciones |
| Q9 | - |  |  | SI | Fecha a iniciar el tratamiento |
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