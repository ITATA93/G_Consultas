# SQLUser.BLC_ContractDetails

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTR_RowId | bigint | PK |  | NO | - |
| CONTR_CreatedDate | date |  |  | SI | Created Date |
| CONTR_CreatedTime | time |  |  | SI | Created Time |
| CONTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTR_DepartmentBased | varchar |  |  | SI | Department Based |
| CONTR_Desc | varchar |  |  | NO | CONTR_Desc |
| CONTR_EpisodeBased | varchar |  |  | SI | Episode Based |
| CONTR_HospitalBased | varchar |  |  | SI | Hospital Based |
| CONTR_InclExcl | varchar |  |  | SI | Inclusive/Exclusive |
| CONTR_Owner | varchar |  |  | SI | Owner |
| CONTR_SelectionMethod | varchar |  |  | SI | Selection Method |
| CONTR_UpdatedDate | date |  |  | SI | Updated Date |
| CONTR_UpdatedTime | time |  |  | SI | Updated Time |
| CONTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Lactancia materna exclusiva |
| Q02 | - |  |  | SI | Mamadera nocturna (desde los 18 meses) |
| Q03 | - |  |  | SI | Consumo de sal y azúcar durante los primeros 1000 ... |
| Q04 | - |  |  | SI | Momentos de azúcar entre comidas |
| Q05 | - |  |  | SI | Uso de medicamentos azucarados |
| Q06 | - |  |  | SI | Hábito de cepillado |
| Q07 | - |  |  | SI | Uso de pasta de dientes |
| Q08 | - |  |  | SI | Chupete de entretención (mayores de 3 años) |
| Q09 | - |  |  | SI | Succión digital |
| Q10 | - |  |  | SI | Dientes perinatales |
| Q11 | - |  |  | SI | Placa bacteriana |
| Q12 | - |  |  | SI | Anomalías dento-maxilares |
| Q13 | - |  |  | SI | Urgencias odontológicas |
| Q14 | - |  |  | SI | Derivación |
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