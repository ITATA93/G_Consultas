# SQLUser.MRC_ObservationItemEWS

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EWS_ParRef | bigint | PK |  | NO | MRC_ObservationItem Parent Reference |
| EWS_AgeFromDays | integer |  |  | SI | Range Age |
| EWS_AgeFromMonth | integer |  |  | SI | Range Age |
| EWS_AgeFromYears | integer |  |  | SI | Range Age |
| EWS_AgeToDays | integer |  |  | SI | Range Age |
| EWS_AgeToMonth | integer |  |  | SI | Range Age |
| EWS_AgeToYears | integer |  |  | SI | Range Age |
| EWS_CTLoc_DR | bigint |  | FK | SI | Des Ref to Location CT  |
| EWS_Childsub | double |  |  | NO | Childsub |
| EWS_DateFrom | date |  |  | SI | - |
| EWS_DateTo | date |  |  | SI | - |
| EWS_DisplayWarning | varchar |  |  | SI | Display Warning |
| EWS_EarlyWarningScoringSystem | bigint |  |  | SI | Early Warning Scoring System |
| EWS_From | varchar |  |  | SI | Range From |
| EWS_ObsItemLookupValue_DR | varchar |  | FK | SI | Des Ref to Observation Item Lookup Values CT  |
| EWS_ObsItem_DR | bigint |  | FK | SI | Des Ref to Observation Item CT (lookup only) |
| EWS_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| EWS_PatientAlert_DR | bigint |  | FK | SI | Des Ref to Patient Alert CT |
| EWS_PregnancyEvent | varchar |  |  | SI | Applies to Pregnancy Event ONLY |
| EWS_Range_DR | bigint |  | FK | SI | EWS Range |
| EWS_RowId | varchar |  |  | NO | - |
| EWS_To | varchar |  |  | SI | Range To |
| Q01 | - |  |  | SI | Fecha Resultado PAP |
| Q02 | - |  |  | SI | Diagnóstico Principal PAP |
| Q02ObsDR | - |  |  | SI | Diagnóstico Principal PAP DR |
| Q03 | - |  |  | SI | Otros Diagnósticos PAP |
| Q03ObsDR | - |  |  | SI | Otros Diagnósticos PAP DR |
| Q04 | - |  |  | SI | Otros Diagnósticos PAP (S) |
| Q04ObsDR | - |  |  | SI | Otros Diagnósticos PAP (S) DR |
| Q05 | - |  |  | SI | Descripción de sugerencias |
| Q05ObsDR | - |  |  | SI | Descripción de sugerencias DR |
| Q06 | - |  |  | SI | Fecha Próximo Exámen |
| Q06ObsDR | - |  |  | SI | Fecha Próximo Exámen DR |
| Q07 | - |  |  | SI | Fecha de Vencimiento |
| Q08 | - |  |  | SI | Fecha Toma de PAP |
| Q09 | - |  |  | SI | Diagnósticos Primarios |
| Q09ObsDR | - |  |  | SI | Diagnósticos Primarios DR |
| Q10 | - |  |  | SI | Descripción de la Calidad de la Muestra |
| Q10ObsDR | - |  |  | SI | Descripción de la Calidad de la Muestra  DR |
| Q11 | - |  |  | SI | Diagnósticos Secundarios |
| Q11ObsDR | - |  |  | SI | Diagnósticos Secundarios  DR |
| Q12 | - |  |  | SI | Fecha de Ingreso PAP |
| Q12ObsDR | - |  |  | SI | Fecha de Ingreso PAP  DR |
| Q13 | - |  |  | SI | Lugar Realización Examen |
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