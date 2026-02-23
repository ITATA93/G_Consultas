# SQLUser.LBC_StorageContainer

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSTC_RowID | bigint | PK |  | NO | - |
| ChildQ14DR | - |  |  | SI | Child Reference: Descripción de farmacos administr... |
| LBCSTC_AlphaColumns | varchar |  |  | SI | Alpha Columns |
| LBCSTC_AlphaRows | varchar |  |  | SI | Alpha Rows |
| LBCSTC_AutoPurge | varchar |  |  | SI | Auto Purge |
| LBCSTC_Code | varchar |  |  | SI | Code |
| LBCSTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSTC_ColumnWidth | numeric |  |  | SI | Column width
DEPRICATED |
| LBCSTC_Columns | numeric |  |  | SI | Columns |
| LBCSTC_CreatedDate | date |  |  | SI | Created Date |
| LBCSTC_CreatedTime | time |  |  | SI | Created Time |
| LBCSTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSTC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSTC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSTC_Desc | varchar |  |  | SI | Description |
| LBCSTC_LabSite_DR | bigint |  | FK | SI | User Site DR |
| LBCSTC_MaterialTypeList | varchar |  |  | SI | List of Material Types |
| LBCSTC_NumberOfPositions | numeric |  |  | SI | Number Of Positions |
| LBCSTC_Owner | varchar |  |  | SI | Owner |
| LBCSTC_RefreshTime | numeric |  |  | SI | Refresh Time |
| LBCSTC_ReservePositions | varchar |  |  | SI | Reserve Positions |
| LBCSTC_RestrictToUseByMaterialType | varchar |  |  | SI | Restricted to use by Material Type |
| LBCSTC_RestrictToUseBySpecimen | varchar |  |  | SI | Restricted to use by Specimens  |
| LBCSTC_Rows | numeric |  |  | SI | Rows |
| LBCSTC_SchemeSequence | double |  |  | SI | Sequence of the Storage Container within the Stora... |
| LBCSTC_SpecimenList | varchar |  |  | SI | List of Specimens |
| LBCSTC_StorageScheme_DR | bigint |  | FK | SI | Storage Scheme |
| LBCSTC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSTC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCSTC_WarnNotFinalTestSetStatus | varchar |  |  | SI | Warn in Any Test Set Status is not final |
| LBCSTC_WarnOustandingProcedure | varchar |  |  | SI | Warn Oustanding Procedure |
| Q01 | - |  |  | SI | Otros Motivos de Contención |
| Q01b | - |  |  | SI | Indicaciones de la Contención |
| Q02 | - |  |  | SI | EV |
| Q04 | - |  |  | SI | Efecto (Sedación) |
| Q05 | - |  |  | SI | IM |
| Q06 | - |  |  | SI | Tranquilizante |
| Q09 | - |  |  | SI | Turno |
| Q10 | - |  |  | SI | Medidas fracasadas antes de la contención física |
| Q11 | - |  |  | SI | Personal durante el procedimiento |
| Q12 | - |  |  | SI | Incidentes durante el procedimiento |
| Q13 | - |  |  | SI | Describa incidentes |
| Q15 | - |  |  | SI | Materiales usados para la contención |
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