# SQLUser.LBC_SystemCounter

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSCNT_RowID | bigint | PK |  | NO | - |
| CQ01 | - |  |  | SI | (null) |
| CQ14 | - |  |  | SI | (null) |
| CQ19 | - |  |  | SI | (null) |
| LBCSCNT_CounterLength | integer |  |  | NO | Counter Length |
| LBCSCNT_CreatedDate | date |  |  | SI | Created Date |
| LBCSCNT_CreatedTime | time |  |  | SI | Created Time |
| LBCSCNT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSCNT_DateFrom | date |  |  | SI | From Date |
| LBCSCNT_DateTo | date |  |  | SI | To Date |
| LBCSCNT_DelayDepartmentNumbers | varchar |  |  | SI | Delay the assignment of departmental numbers |
| LBCSCNT_Department_DR | bigint |  | FK | SI | Department |
| LBCSCNT_Format | varchar |  |  | SI | Prefix Format String |
| LBCSCNT_IncludeCheckCharacter | varchar |  |  | SI | Include Check Character |
| LBCSCNT_IncludeLabSitePrefix | varchar |  |  | SI | Include Lab Site Prefix |
| LBCSCNT_LabSiteList | varchar |  |  | SI | Lab Site List |
| LBCSCNT_PrefixString | varchar |  |  | SI | String Prefix |
| LBCSCNT_ResetFrequency | varchar |  |  | SI | Reset Frequency |
| LBCSCNT_SpecimenSeparator | varchar |  |  | NO | Specimen Counter Separator |
| LBCSCNT_StartCounterNumber | integer |  |  | SI | Start Counter Number
Counter Number |
| LBCSCNT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSCNT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSCNT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCSCNT_UseAlphaSpecimenCounter | varchar |  |  | SI | Use Alpha Counter |
| LBCSCNT_YearFormatYY | varchar |  |  | SI | 2 Digit For Year Format |
| Q01 | - |  |  | SI | Vive con : |
| Q02 | - |  |  | SI | HTA |
| Q03 | - |  |  | SI | DM |
| Q04 | - |  |  | SI | IG/RI |
| Q05 | - |  |  | SI | DLP |
| Q06 | - |  |  | SI | AR |
| Q07 | - |  |  | SI | OA |
| Q08 | - |  |  | SI | EPOC |
| Q09 | - |  |  | SI | ASMA |
| Q10 | - |  |  | SI | IR |
| Q11 | - |  |  | SI | IAM |
| Q12 | - |  |  | SI | AVE |
| Q13 | - |  |  | SI | IC |
| Q14 | - |  |  | SI | Hábitos : |
| Q15 | - |  |  | SI | Control Nutricional |
| Q16 | - |  |  | SI | Factores de Riesgo |
| Q17 | - |  |  | SI | Factores Protectores |
| Q18 | - |  |  | SI | Fecha |
| Q19 | - |  |  | SI | Atendido por : |
| Q20 | - |  |  | SI | Patologia Base |
| Q21 | - |  |  | SI | Fecha Proximo Control |
| Q22 | - |  |  | SI | RND : Registro Nacional de Incapacidad |
| Q23 | - |  |  | SI | Patologia Base |
| QACR | - |  |  | SI | Actividades Recreativas |
| QACT | - |  |  | SI | Actividades Terapeuticas |
| QADP | - |  |  | SI | Adaptacion del Hogar |
| QAVD | - |  |  | SI | Habilitacion y Rehabilitacion de AVD |
| QC2 | - |  |  | SI | Estilo de Vida y Conductas de Autocuidado |
| QC3 | - |  |  | SI | Actividades Fisicas |
| QC4 | - |  |  | SI | Tabaquismo |
| QCAT | - |  |  | SI | Confeccion de Ayudas Tecnicas |
| QCO | - |  |  | SI | Confeccion Ortesis |
| QEAT | - |  |  | SI | Evaluacion Ayudas Tecnicas |
| QET | - |  |  | SI | Ejercicios Terapeuticos |
| QFST | - |  |  | SI | Fisioterapia |
| QHAB | - |  |  | SI | Habilitacion Laboral Educacional |
| QIS | - |  |  | SI | Inclusion Social |
| QMST | - |  |  | SI | Masoterapia |
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