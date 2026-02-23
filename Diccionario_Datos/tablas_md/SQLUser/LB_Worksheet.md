# SQLUser.LB_Worksheet

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWS_RowID | bigint | PK |  | NO | - |
| ChildQ28DR | - |  |  | SI | Child Reference: Tecnica Realizada |
| LBWS_Confidential | varchar |  |  | SI | Indicates if a worksheet is confdential |
| LBWS_DateCreated | date |  |  | SI | Date Worksheet created |
| LBWS_DatePrinted | date |  |  | SI | Date Last Printed |
| LBWS_DateTestSetAdded | date |  |  | SI | Date Test Set was last added |
| LBWS_Final | varchar |  |  | SI | Flag to indicate if there are pending results on t... |
| LBWS_LabSite_DR | bigint |  | FK | SI | Location  |
| LBWS_Status | varchar |  |  | NO | Status
StandardType: LabWorksheetStatus |
| LBWS_TimeCreated | time |  |  | SI | Time Worksheet created |
| LBWS_TimePrinted | time |  |  | SI | Time Last Printed |
| LBWS_TimeTestSetAdded | time |  |  | SI | Time Test Set was last added |
| LBWS_WorksheetDef_DR | bigint |  | FK | NO | CodeTable Entry related to worksheet |
| LBWS_WorksheetNumber | integer |  |  | NO | Worksheet number based on the worksheet definition... |
| Q01 | - |  |  | SI | RUN |
| Q02 | - |  |  | SI | Nombres |
| Q03 | - |  |  | SI | Apellido Paterno |
| Q04 | - |  |  | SI | Apellido Materno |
| Q05 | - |  |  | SI | Sexo |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Dirección |
| Q09 | - |  |  | SI | Región |
| Q10 | - |  |  | SI | Ciudad/Localidad |
| Q11 | - |  |  | SI | Comuna |
| Q12 | - |  |  | SI | Teléfono |
| Q13 | - |  |  | SI | Previsión |
| Q14 | - |  |  | SI | Profesional Responsable |
| Q15 | - |  |  | SI | Región |
| Q16 | - |  |  | SI | Provincia |
| Q17 | - |  |  | SI | Comuna |
| Q18 | - |  |  | SI | Dirección |
| Q19 | - |  |  | SI | Laboratorio/Hospital |
| Q20 | - |  |  | SI | Unidad |
| Q21 | - |  |  | SI | Correo Electronico |
| Q22 | - |  |  | SI | Fono |
| Q23 | - |  |  | SI | Fax |
| Q24 | - |  |  | SI | Fecha de La obtención |
| Q25 | - |  |  | SI | Hora Obtención |
| Q26 | - |  |  | SI | Tipo de Muestra |
| Q27 | - |  |  | SI | Otro (Tipo de muestra) |
| Q29 | - |  |  | SI | Antecedentes |
| Q30 | - |  |  | SI | Otros antecedentes |
| Q31 | - |  |  | SI | Plan |
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