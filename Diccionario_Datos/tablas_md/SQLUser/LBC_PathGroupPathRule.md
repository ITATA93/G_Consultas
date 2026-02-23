# SQLUser.LBC_PathGroupPathRule

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAGPR_ParRef | bigint | PK |  | NO | LBCPathogen Group Parent Reference |
| LBCPAGPR_AdmType | varchar |  |  | SI | Admission Type
Compared with the value of Admissi... |
| LBCPAGPR_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCPAGPR_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCPAGPR_AnatomicalSiteQualifiers | varchar |  |  | SI | Anatomical Site Qualifier |
| LBCPAGPR_AnatomicalSites | varchar |  |  | SI | Anatomical Site |
| LBCPAGPR_AssignAntibioticPanel | varchar |  |  | SI | Assign Antibiotic Panel |
| LBCPAGPR_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition |
| LBCPAGPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAGPR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAGPR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAGPR_Desc | varchar |  |  | NO | Description |
| LBCPAGPR_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCPAGPR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCPAGPR_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCPAGPR_PathogenExclusion | varchar |  |  | SI | Pathogen Exclusion
List of Pathogen IDs that are ... |
| LBCPAGPR_PathogenGrowthQualifier_DR | bigint |  | FK | SI | Organism Growth Qualifier |
| LBCPAGPR_PathogenSubType_DR | varchar |  | FK | SI | Sub Type of Pathogen |
| LBCPAGPR_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCPAGPR_RowID | varchar |  |  | NO | - |
| LBCPAGPR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCPAGPR_Species | varchar |  |  | SI | Species |
| LBCPAGPR_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCPAGPR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCPAGPR_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCPAGPR_Type | varchar |  |  | SI | Type |
| QDiagProblem | - |  |  | SI | MRDiagnos with PAProblem |
| QFechaConf | - |  |  | SI | Fecha de Confirmación |
| QFechaConfImp | - |  |  | SI | Fecha Confirmación Impresión IPD |
| QFechaDes | - |  |  | SI | Fecha Descarte |
| QFechaDesImp | - |  |  | SI | Fecha Descarte Impresión |
| QFechaNot | - |  |  | SI | Fecha Notificación |
| QFechaNotImp | - |  |  | SI | Fecha Notificación Impresión |
| QHoraConf | - |  |  | SI | Hora de Confirmación |
| QHoraConfImp | - |  |  | SI | Hora Confirmación Impresión IPD |
| QHoraDes | - |  |  | SI | Hora Descarte |
| QHoraDesImp | - |  |  | SI | Hora Desacarte Impresión |
| QHoraNot | - |  |  | SI | Hora Notificación |
| QHoraNotImp | - |  |  | SI | Hora Notificación Impresión |
| QMRDIAGNOS | - |  |  | SI | MRDiagnos |
| QPACREFTEMPLATE | - |  |  | SI | Problema de Salud |
| QPAPROBLEM | - |  |  | SI | PAProblem |
| QPAWAITINGLIST | - |  |  | SI | PAWaitingList |
| QRBOperatingRoom | - |  |  | SI | Operating Room |
| QTeleconsulta | - |  |  | SI | Teleconsulta |
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
| QUserConf | - |  |  | SI | Usuario Confirmación |
| QUserDes | - |  |  | SI | Usuario de Descarte |
| QUserImpConf | - |  |  | SI | Usuario Imprime la Confirmación |
| QUserImpDes | - |  |  | SI | Usuario Imprime el Descarte |
| QUserImpNot | - |  |  | SI | Usuario Imprime la Notificación |
| QUserNot | - |  |  | SI | Código Usuario Notificación |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*