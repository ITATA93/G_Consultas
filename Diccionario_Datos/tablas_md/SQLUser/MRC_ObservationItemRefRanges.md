# SQLUser.MRC_ObservationItemRefRanges

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RR_ParRef | bigint | PK |  | NO | MRC_ObservationItem Parent Reference |
| Q01 | - |  |  | SI | Evaluación de Necesidades Educativas |
| Q02 | - |  |  | SI | Otro (Evaluación) |
| Q03 | - |  |  | SI | Barreras de Aprendizaje |
| Q04 | - |  |  | SI | Otro (Barreras) |
| Q05 | - |  |  | SI | Recibe Educación |
| Q06 | - |  |  | SI | Razón para No Educar |
| Q07 | - |  |  | SI | Otro (Razón) |
| Q08 | - |  |  | SI | 1.- Patología(s) Presente(s) |
| Q09 | - |  |  | SI | Contenidos |
| Q10 | - |  |  | SI | Actividad Educativa |
| Q11 | - |  |  | SI | Especificaciones Entregadas |
| Q12 | - |  |  | SI | 2.- Seguridad Medicación |
| Q13 | - |  |  | SI | Contenidos |
| Q14 | - |  |  | SI | Actividad Educativa |
| Q15 | - |  |  | SI | Especificaciones Entregadas |
| Q16 | - |  |  | SI | 3.- Uso de Equipos Biomédicos |
| Q17 | - |  |  | SI | Contenidos |
| Q18 | - |  |  | SI | Actividad Educativa |
| Q19 | - |  |  | SI | Especificaciones Entregadas |
| Q20 | - |  |  | SI | 4.- Condiciones Clínicas |
| Q21 | - |  |  | SI | Contenidos |
| Q22 | - |  |  | SI | Actividad Educativa |
| Q23 | - |  |  | SI | Especificaciones Entregadas |
| Q24 | - |  |  | SI | Receptor de Educación |
| Q25 | - |  |  | SI | Comprensión de la Educación |
| Q26 | - |  |  | SI | Demostración Correcta |
| Q27 | - |  |  | SI | Comentarios |
| Q28 | - |  |  | SI | Contenidos Entregados |
| Q29 | - |  |  | SI | Otro (Receptor) |
| Q30 | - |  |  | SI | Profesional Responsable |
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
| RR_AgeFromDays | integer |  |  | SI | Range Age |
| RR_AgeFromMonth | integer |  |  | SI | Range Age |
| RR_AgeFromYears | integer |  |  | SI | Range Age |
| RR_AgeToDays | integer |  |  | SI | Range Age |
| RR_AgeToMonth | integer |  |  | SI | Range Age |
| RR_AgeToYears | integer |  |  | SI | Range Age |
| RR_Childsub | double |  |  | NO | Childsub |
| RR_DateFrom | date |  |  | SI | Date From |
| RR_DateTo | date |  |  | SI | Date To |
| RR_From | varchar |  |  | SI | Range From |
| RR_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| RR_PregnancyEvent | varchar |  |  | SI | Applies to Pregnancy Event ONLY |
| RR_RowId | varchar |  |  | NO | - |
| RR_Sex | bigint |  |  | SI | Range Sex |
| RR_To | varchar |  |  | SI | Range To |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*