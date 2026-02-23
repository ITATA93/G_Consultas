# SQLUser.LBC_PathogenGroupAntibiotic

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPAGA_ParRef | bigint | PK |  | NO | LBCPathogen Parent Reference |
| LBCPAGA_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site DR |
| LBCPAGA_Antibiotic_DR | bigint |  | FK | SI | Des Ref LBCAntibiotic |
| LBCPAGA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPAGA_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPAGA_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPAGA_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCPAGA_Lesion_DR | bigint |  | FK | SI | Lesion DR |
| LBCPAGA_NotApplicable | varchar |  |  | SI | Not Aplicable |
| LBCPAGA_PathogenExclusion | varchar |  |  | SI | Pathogen Exclusion
List of Pathogen IDs that are ... |
| LBCPAGA_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCPAGA_Reported | varchar |  |  | SI | Reported |
| LBCPAGA_RowID | varchar |  |  | NO | - |
| LBCPAGA_Sequence | double |  |  | SI | [DEPRECATED]Sequence[/DEPRECATED] |
| LBCPAGA_Species_DR | bigint |  | FK | SI | Species |
| LBCPAGA_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group DR |
| LBCPAGA_Specimen_DR | bigint |  | FK | SI | Specimen DR |
| LBCPAGA_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCPAGA_WeightedSequence | double |  |  | SI | Weighted Sequence |
| Q01 | - |  |  | SI | Horario Normal - Total Atención Solicitada - Menor... |
| Q02 | - |  |  | SI | Horario Normal - Rechazos - Menor 5 Años |
| Q03 | - |  |  | SI | Horario Normal - Total Atención Solicitada - 65 y ... |
| Q04 | - |  |  | SI | Horario Normal - Rechazos - 65 y más años |
| Q05 | - |  |  | SI | Horario Normal - Total Atención Solicitada - Embar... |
| Q06 | - |  |  | SI | Horario Normal - Rechazos - Embarazadas |
| Q07 | - |  |  | SI | Horario Continuado - Total Atención Utilizada - Me... |
| Q08 | - |  |  | SI | Horario Continuado - Rechazos - Menor 5 años |
| Q09 | - |  |  | SI | Horario Continuado - Total Atención Utilizada - 65... |
| Q10 | - |  |  | SI | Horario Continuado - Rechazo - 65 y Más Años |
| Q11 | - |  |  | SI | Horario Continuado - Total Atención Utilizada - Em... |
| Q12 | - |  |  | SI | Horario Continuado - Rechazo - Embarazadas |
| Q16 | - |  |  | SI | Mes |
| Q17 | - |  |  | SI | Año |
| QFF | - |  |  | SI | Fecha FIn |
| QFI | - |  |  | SI | Fecha Inicio |
| QHR | - |  |  | SI | Establecimiento |
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