# SQLUser.LBC_Worksheet

**Schema:** SQLUser
**Columnas:** 141
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCWS_RowID | bigint | PK |  | NO | - |
| ChildQ50DR | - |  |  | SI | Child Reference: Virus detectado localmente |
| LBCWS_AddItemsToClosedWorksheets | varchar |  |  | SI | Should closed test sets be filled up. This flag do... |
| LBCWS_AllowMovePendingToCurrent | varchar |  |  | SI | Flag to indicate if move of pending test sets to c... |
| LBCWS_AllowQCOnlyWorksheet | varchar |  |  | SI | Allow Generation of QC Only Worksheet |
| LBCWS_CloseOnPrinting | varchar |  |  | SI | Should be closed when printed |
| LBCWS_Code | varchar |  |  | NO | Code |
| LBCWS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCWS_ColumnsStartWith | integer |  |  | SI | Columns Start With |
| LBCWS_CreatedDate | date |  |  | SI | Created Date  |
| LBCWS_CreatedTime | time |  |  | SI | Created Time |
| LBCWS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCWS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCWS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCWS_DaysPendingBeforeMove | integer |  |  | SI | Days Pending before move to new Worksheet (depends... |
| LBCWS_Departments | varchar |  |  | SI | Worksheet departments
The worksheet's test set's ... |
| LBCWS_Desc | varchar |  |  | NO | Description |
| LBCWS_GridColumns | integer |  |  | SI | Grid Columns |
| LBCWS_GridIDReportGroup_DR | bigint |  | FK | SI | The Grid ID barcode report group for Worksheet Gri... |
| LBCWS_GridListReportGroup_DR | bigint |  | FK | SI | The Worksheet Grid content list report group |
| LBCWS_GridProgression | varchar |  |  | SI | Grid Progression: Specifies the direction focus wi... |
| LBCWS_GridRows | integer |  |  | SI | Grid Rows |
| LBCWS_InUse | bit |  |  | SI | Flag to indicate if a worksheet is in use |
| LBCWS_LabSiteRestriction_DR | bigint |  | FK | SI | Lab Site Restriction |
| LBCWS_ManualWorksheetAssignment | varchar |  |  | SI | Manually Assign to Worksheets |
| LBCWS_MaxEpisodesPerPage | integer |  |  | SI | /Maximum number of episodes to display on a page |
| LBCWS_MaxEpisodesPerSheet | integer |  |  | SI | Maximum number of episodes before create a new she... |
| LBCWS_MaxSpecimens | integer |  |  | SI | Maximum Specimens Per Grid |
| LBCWS_Owner | varchar |  |  | SI | Owner |
| LBCWS_PeriodBasedQC | varchar |  |  | SI | Period Based QC Enabled |
| LBCWS_PrintLabelsReportOnGridCreation | varchar |  |  | SI | Print Labels Report on Worksheet Grid creation |
| LBCWS_PrintReportOnGridCreation | varchar |  |  | SI | Print Report on Worksheet Grid creation |
| LBCWS_QCValidityPeriod | integer |  |  | SI | QC Validity Period (hours) |
| LBCWS_RowsStartWith | varchar |  |  | SI | Rows Start With |
| LBCWS_SortOrder | varchar |  |  | SI | Determines how episodes are sorted on the workshee... |
| LBCWS_Type | varchar |  |  | SI | Worksheet Type |
| LBCWS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCWS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCWS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCWS_UrgentFirst | varchar |  |  | SI | Urgent at top of worksheet |
| LBCWS_UseAltTestItemDesc | varchar |  |  | SI | Use Alternate Test Item Description |
| LBCWS_WorkArea_DR | bigint |  | FK | SI | Work Area |
| LBCWS_WorksheetAllocation | varchar |  |  | SI | Worksheet Allocation |
| LBCWS_WorksheetAllocationProcedure | bigint |  |  | SI | Worksheet Allocation Procedure |
| LBCWS_WorksheetGroup_DR | bigint |  | FK | SI | Worksheet Group |
| LBCWS_WorksheetReport_DR | bigint |  | FK | SI | Worksheet Report |
| Q01 | - |  |  | SI | Trabajador avícola o granjas de cerdos |
| Q02 | - |  |  | SI | Personal de la salud |
| Q03 | - |  |  | SI | Semanas de gestación (semanas) |
| Q04 | - |  |  | SI | Semanas de gestación (días) |
| Q05 | - |  |  | SI | Embarazo |
| Q06 | - |  |  | SI | Fecha inicio síntomas |
| Q07 | - |  |  | SI | Fecha 1° Consulta |
| Q08 | - |  |  | SI | Fiebre (> o = 38.5°C) |
| Q09 | - |  |  | SI | Tos |
| Q10 | - |  |  | SI | Cefalea |
| Q11 | - |  |  | SI | Mialgias |
| Q12 | - |  |  | SI | Odinofagia |
| Q13 | - |  |  | SI | Rinorrea/congestión nasal |
| Q14 | - |  |  | SI | Neumonía |
| Q15 | - |  |  | SI | Hipoxemia |
| Q16 | - |  |  | SI | Deshidratación o rechazo alimentario |
| Q17 | - |  |  | SI | Dificultad respiratoria |
| Q18 | - |  |  | SI | Compromiso hemodinámico |
| Q19 | - |  |  | SI | Consulta repetida por deterioro clínico |
| Q20 | - |  |  | SI | Neumonía (A) |
| Q21 | - |  |  | SI | Taquipnea (A) |
| Q22 | - |  |  | SI | Hipotensión (A) |
| Q23 | - |  |  | SI | Disnea (A) |
| Q24 | - |  |  | SI | Cianosis (A) |
| Q25 | - |  |  | SI | Hipoxemia (A) |
| Q26 | - |  |  | SI | Consulta reptida por deterioro clínico (A) |
| Q27 | - |  |  | SI | Especifique (Enfermedad de base) |
| Q28 | - |  |  | SI | Enfermedad de base |
| Q29 | - |  |  | SI | Fecha hospitalización |
| Q30 | - |  |  | SI | Diagnóstico de Ingreso |
| Q31 | - |  |  | SI | Unidad Intermedia |
| Q32 | - |  |  | SI | UCI |
| Q33 | - |  |  | SI | VM |
| Q34 | - |  |  | SI | VAFO |
| Q35 | - |  |  | SI | ECMO |
| Q36 | - |  |  | SI | Fecha inicio (Uso antiviral) |
| Q37 | - |  |  | SI | Antiviral |
| Q38 | - |  |  | SI | Uso Antiviral |
| Q39 | - |  |  | SI | Nombre Hospital de Destino |
| Q40 | - |  |  | SI | Fecha de traslado |
| Q41 | - |  |  | SI | Traslado Hospitalario |
| Q42 | - |  |  | SI | Se Hospitaliza |
| Q43 | - |  |  | SI | Fecha fallecimiento |
| Q44 | - |  |  | SI | Diagnóstico fallecimiento |
| Q45 | - |  |  | SI | Fallece |
| Q46 | - |  |  | SI | Fecha vacunación |
| Q47 | - |  |  | SI | Vacuna contra influenza |
| Q48 | - |  |  | SI | Fecha obtención de la muestra |
| Q49 | - |  |  | SI | Fecha envío muestra |
| Q51 | - |  |  | SI | Tipo de muestra |
| Q52 | - |  |  | SI | Otro tipo de muestra |
| Q53 | - |  |  | SI | Establecimiento |
| Q54 | - |  |  | SI | Fono |
| Q55 | - |  |  | SI | Responsable de la notificación |
| Q56 | - |  |  | SI | Fecha de notificación |
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