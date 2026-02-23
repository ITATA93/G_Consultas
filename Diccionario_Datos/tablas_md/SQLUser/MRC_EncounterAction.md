# SQLUser.MRC_EncounterAction

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACT_RowId | bigint | PK |  | NO | - |
| ACT_ChartEprReadOnly | varchar |  |  | SI | If the action is a chart, this property determines... |
| ACT_Code | varchar |  |  | SI | Code |
| ACT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACT_Context | varchar |  |  | SI | Action context |
| ACT_CreatedDate | date |  |  | SI | Created Date |
| ACT_CreatedTime | time |  |  | SI | Created Time |
| ACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACT_DateFrom | date |  |  | SI | Date From |
| ACT_DateTo | date |  |  | SI | Date To |
| ACT_Desc | varchar |  |  | SI | Description |
| ACT_DispOrdDet | varchar |  |  | SI | Always display order details - for one touch order... |
| ACT_DocType_DR | bigint |  | FK | SI | - |
| ACT_Filter | varchar |  |  | SI | Filter |
| ACT_GroupedActions | varchar |  |  | SI | Grouped Actions
List of MRCEncounterAction |
| ACT_IsGroup | varchar |  |  | SI | Is Action Group |
| ACT_LinkJSFunction | varchar |  |  | SI | Additional Javascript to run on button click |
| ACT_Location_DR | bigint |  | FK | SI | Location |
| ACT_OpenNewWindowUPR | varchar |  |  | SI | Determines whether, in the UPR, the action opens i... |
| ACT_Owner | varchar |  |  | SI | Owner |
| ACT_Purpose | varchar |  |  | SI | Purpose |
| ACT_QuesLink | varchar |  |  | SI | Link Questionnaire To (Patient Booking, Anaestheti... |
| ACT_SecurityGroup_DR | bigint |  | FK | SI | Security Group |
| ACT_UpdatedDate | date |  |  | SI | Updated Date |
| ACT_UpdatedTime | time |  |  | SI | Updated Time |
| ACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ACT_WorkFlow_DR | bigint |  | FK | SI | Action WorkFlow - overrides default WorkFlow confi... |
| Q01 | - |  |  | SI | N° de Mensajes 1 |
| Q02 | - |  |  | SI | N° de Mensajes 2 |
| Q03 | - |  |  | SI | N° de Mensajes 3 |
| Q04 | - |  |  | SI | N° de Participantes 1 |
| Q05 | - |  |  | SI | N° de Participantes 2 |
| Q06 | - |  |  | SI | N° de Participantes 3 |
| Q07 | - |  |  | SI | Menores de 1 año 1 |
| Q08 | - |  |  | SI | Menores de 1 año 2 |
| Q09 | - |  |  | SI | Menores de 1 año 3 |
| Q10 | - |  |  | SI | Niños 12 a 23 meses 1 |
| Q11 | - |  |  | SI | Niños 12 a 23 meses 2 |
| Q12 | - |  |  | SI | Niños 12 a 23 meses 3 |
| Q13 | - |  |  | SI | Menor de 2 años 1 |
| Q14 | - |  |  | SI | Menor de 2 años 2 |
| Q15 | - |  |  | SI | Menor de 2 años 3 |
| Q16 | - |  |  | SI | 2 a 4 años 1 |
| Q17 | - |  |  | SI | 2 a 4 años 2 |
| Q18 | - |  |  | SI | 2 a 4 años 3 |
| Q19 | - |  |  | SI | 5 a 9 años 1 |
| Q20 | - |  |  | SI | 5 a 9 años 2 |
| Q21 | - |  |  | SI | 5 a 9 años 3 |
| Q22 | - |  |  | SI | 10 a 14 años 1 |
| Q23 | - |  |  | SI | 10 a 14 años 2 |
| Q24 | - |  |  | SI | 10 a 14 años 3 |
| Q25 | - |  |  | SI | 15 a 19 años 1 |
| Q26 | - |  |  | SI | 15 a 19 años 2 |
| Q27 | - |  |  | SI | 15 a 19 años 3 |
| Q28 | - |  |  | SI | 20 -24 años 1 |
| Q29 | - |  |  | SI | 20 -24 años 2 |
| Q30 | - |  |  | SI | 20 -24 años 3 |
| Q31 | - |  |  | SI | 25 -29 años 1 |
| Q32 | - |  |  | SI | 25 -29 años 2 |
| Q33 | - |  |  | SI | 25 -29 años 3 |
| Q34 | - |  |  | SI | 30 - 34 años 1 |
| Q35 | - |  |  | SI | 30 - 34 años 2 |
| Q36 | - |  |  | SI | 30 - 34 años 3 |
| Q37 | - |  |  | SI | 35 - 39 años 1 |
| Q38 | - |  |  | SI | 35 - 39 años 2 |
| Q39 | - |  |  | SI | 35 - 39 años 3 |
| Q40 | - |  |  | SI | 40 - 44 años 1 |
| Q41 | - |  |  | SI | 40 - 44 años 2 |
| Q42 | - |  |  | SI | 40 - 44 años 3 |
| Q43 | - |  |  | SI | 45 - 49 años 1 |
| Q44 | - |  |  | SI | 45 - 49 años 2 |
| Q45 | - |  |  | SI | 45 - 49 años 3 |
| Q46 | - |  |  | SI | 50 - 54 años 1 |
| Q47 | - |  |  | SI | 50 - 54 años 2 |
| Q48 | - |  |  | SI | 50 - 54 años 3 |
| Q49 | - |  |  | SI | 55 - 59 años 1 |
| Q50 | - |  |  | SI | 55 - 59 años 2 |
| Q51 | - |  |  | SI | 55 - 59 años 3 |
| Q52 | - |  |  | SI | 60 - 64 años 1 |
| Q53 | - |  |  | SI | 60 - 64 años 2 |
| Q54 | - |  |  | SI | 60 - 64 años 3 |
| Q55 | - |  |  | SI | Gestantes 1 |
| Q56 | - |  |  | SI | Gestantes 2 |
| Q57 | - |  |  | SI | Gestantes 3 |
| Q58 | - |  |  | SI | Post Parto 1 |
| Q59 | - |  |  | SI | Post Parto 2 |
| Q60 | - |  |  | SI | Post Parto 3 |
| Q62 | - |  |  | SI | Mes |
| Q63 | - |  |  | SI | Año |
| QHD | - |  |  | SI | Establecimiento |
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