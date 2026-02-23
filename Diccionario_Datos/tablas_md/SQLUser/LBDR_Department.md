# SQLUser.LBDR_Department

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRD_ParRef | varchar | PK |  | NO | Parent Reference LBDRReportPage DR |
| ChildQ01DR | - |  |  | SI | Child Reference: Registro de Actividades |
| LBDRD_AccreditationNumber | varchar |  |  | SI | Accreditation Number |
| LBDRD_AdditionalBloodGroupDescs | varchar |  |  | SI | Patient Additional Blood Groups
Comma-list of Add... |
| LBDRD_AntibodyDescs | varchar |  |  | SI | Patient Antibodies
Comma-list of Antibody Descs
... |
| LBDRD_BloodGroupDesc | varchar |  |  | SI | Patient Blood Group Desc
HTMLTextBox |
| LBDRD_ClinicalConditions | varchar |  |  | SI | Clinical Conditions
A string with a comma-list of... |
| LBDRD_DepartmentCode | varchar |  |  | SI | Department Code (for readability and use in ZenRep... |
| LBDRD_DepartmentDesc | varchar |  |  | SI | Department Desc (for readability and use in ZenRep... |
| LBDRD_DepartmentFooterClass | varchar |  |  | SI | Department Footer Zen Report
The Zen Report which... |
| LBDRD_DepartmentFooterExtraText | varchar |  |  | SI | Department Footer Extra Text
Extra Text (such a P... |
| LBDRD_DepartmentHeaderClass | varchar |  |  | SI | Department Header Zen Report
The Zen Report which... |
| LBDRD_DepartmentHeaderExtraText | varchar |  |  | SI | Department Header Extra Text
Extra Text (such a P... |
| LBDRD_Department_DR | bigint |  | FK | SI | The Department within the ReportPage (can be "") |
| LBDRD_PrintSeparatePage | varchar |  |  | SI | Print New Page
Start a new page in the Doctors Re... |
| LBDRD_RowID | varchar |  |  | NO | - |
| LBDRD_SortKey | double |  |  | SI | The Sortkey used to sort Departments. |
| LBDRD_TelephoneNumber | varchar |  |  | SI | Telephone Number |
| Q02 | - |  |  | SI | Puntaje Evaluación HAQ-8 al Ingreso |
| Q03 | - |  |  | SI | Puntaje Evaluación HAQ-8 al Egreso |
| Q04 | - |  |  | SI | Edad del Paciente |
| Q05 | - |  |  | SI | Frecuencia Cardíaca Máxima (Tanaka) |
| Q06 | - |  |  | SI | Valor de 50% FC Máxima |
| Q07 | - |  |  | SI | Valor de 69% FC Máxima |
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