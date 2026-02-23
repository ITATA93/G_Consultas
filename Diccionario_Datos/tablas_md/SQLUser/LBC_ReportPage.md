# SQLUser.LBC_ReportPage

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRP_RowID | bigint | PK |  | NO | - |
| ChildQ22DR | - |  |  | SI | Child Reference: Establecimiento  de Inicio de Tra... |
| LBCRP_Code | varchar |  |  | NO | Code |
| LBCRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRP_CreatedDate | date |  |  | SI | Created Date |
| LBCRP_CreatedTime | time |  |  | SI | Created Time |
| LBCRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRP_CumulativeEpisodes | integer |  |  | SI | Cumulatives Maximum Number of Episodes
The maximu... |
| LBCRP_DateFrom | date |  |  | SI | Effective date |
| LBCRP_DateTo | date |  |  | SI | End date
Last day the record is active  |
| LBCRP_DepartmentFooterClass | varchar |  |  | SI | Department Footer Class
The ZEN Report to use for... |
| LBCRP_DepartmentHeaderClass | varchar |  |  | SI | Department Header Class
The ZEN Report to use for... |
| LBCRP_DepartmentOrder | varchar |  |  | SI | Department Order
Specifies whether this ReportPag... |
| LBCRP_Desc | varchar |  |  | NO | Description |
| LBCRP_FooterClass | varchar |  |  | SI | Report Page Footer Class
This is the ZEN Report t... |
| LBCRP_Format | varchar |  |  | SI | Format
The format of the Report Page
N = NonPrin... |
| LBCRP_FormatClass | varchar |  |  | SI | ZEN Report for the ReportPage Format
No longer us... |
| LBCRP_HeaderClass | varchar |  |  | SI | Report Page Header Class
This is the ZEN Report t... |
| LBCRP_Owner | varchar |  |  | SI | Owner |
| LBCRP_ReportWriterClass | varchar |  |  | SI | Report Class Writer to support third-party Report ... |
| LBCRP_SectionFooterClass | varchar |  |  | SI | Section Footer Class
The ZEN Report to use for th... |
| LBCRP_SectionHeaderClass | varchar |  |  | SI | Section Header Class
The ZEN Report to use for th... |
| LBCRP_Sequence | double |  |  | SI | ReportPage Sequence
Within a LabEpisode, specifie... |
| LBCRP_SubsequentHeaderClass | varchar |  |  | SI | Report Subsequent Page Header Class
This is the Z... |
| LBCRP_TestSetFooterClass | varchar |  |  | SI | Test Set Footer Class
The ZEN Report to use for t... |
| LBCRP_TestSetHeaderClass | varchar |  |  | SI | Test Set Header Class
The ZEN Report to use for t... |
| LBCRP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCRP_UseTestItemAltCode | varchar |  |  | SI | Use Test Item Alternate Code in Report Body (Cumul... |
| LBCRP_UseTestItemAltDesc | varchar |  |  | SI | Use Test Item Alternate Description in Report Body... |
| LBCRP_UseTestSetAltDesc | varchar |  |  | SI | Use Test Set Alternate Description in Report Body ... |
| Q01 | - |  |  | SI | Nacionalidad |
| Q02 | - |  |  | SI | Pasaporte |
| Q02a | - |  |  | SI | VIH |
| Q02aObsDR | - |  |  | SI | VIH DR |
| Q03 | - |  |  | SI | Ocupación |
| Q03a | - |  |  | SI | Otra Ocupación |
| Q04 | - |  |  | SI | Domicilio Particular en Chile |
| Q05 | - |  |  | SI | Comuna Chile |
| Q07 | - |  |  | SI | Fono |
| Q08 | - |  |  | SI | Domicilio Laboral en Chile |
| Q09 | - |  |  | SI | Comuna de Trabajo |
| Q10 | - |  |  | SI | Fono Trabajo |
| Q11 | - |  |  | SI | Domicilio en país de origen:  Detalle |
| Q12 | - |  |  | SI | Diagnóstico de TBC (Órgano) |
| Q13 | - |  |  | SI | Confirmación |
| Q14 | - |  |  | SI | Caso Nuevo |
| Q15 | - |  |  | SI | AT por recaída |
| Q16 | - |  |  | SI | AT por Abandono |
| Q17 | - |  |  | SI | Esquema de Tratamiento |
| Q18 | - |  |  | SI | Fecha inicio de tratamiento |
| Q19 | - |  |  | SI | Lugar de Notificación |
| Q20 | - |  |  | SI | Fecha de Notificación |
| Q21 | - |  |  | SI | Servicio de Salud Residencia |
| Q23 | - |  |  | SI | Total Contactos Laborales |
| Q24 | - |  |  | SI | Niños |
| Q25 | - |  |  | SI | Adulto |
| Q26 | - |  |  | SI | Total Contactos Personales |
| Q27 | - |  |  | SI | Niños |
| Q28 | - |  |  | SI | Adultos |
| Q29 | - |  |  | SI | Total contactos con quimioprofilaxis |
| Q30 | - |  |  | SI | Total casos secundarios (Enfermos) |
| Q31 | - |  |  | SI | Traslado a (otro País) |
| Q32 | - |  |  | SI | Fecha Traslado |
| Q33 | - |  |  | SI | Condición de Egreso |
| Q34 | - |  |  | SI | Fecha  Condición de egreso |
| Q35 | - |  |  | SI | Observaciones |
| Q37 | - |  |  | SI | Nombre |
| Q38 | - |  |  | SI | Apellido Paterno |
| Q39 | - |  |  | SI | Apellido Materno |
| Q40 | - |  |  | SI | Edad |
| Q41 | - |  |  | SI | Sexo |
| Q42 | - |  |  | SI | RUT |
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