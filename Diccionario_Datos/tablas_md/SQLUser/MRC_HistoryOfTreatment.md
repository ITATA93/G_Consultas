# SQLUser.MRC_HistoryOfTreatment

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOT_RowId | bigint | PK |  | NO | - |
| HOT_Code | varchar |  |  | NO | Code |
| HOT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOT_CreatedDate | date |  |  | SI | Created Date |
| HOT_CreatedTime | time |  |  | SI | Created Time |
| HOT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOT_DateFrom | date |  |  | SI | Date From |
| HOT_DateTo | date |  |  | SI | Date To |
| HOT_Desc | varchar |  |  | NO | Description |
| HOT_Owner | varchar |  |  | SI | Owner |
| HOT_UpdatedDate | date |  |  | SI | Updated Date |
| HOT_UpdatedTime | time |  |  | SI | Updated Time |
| HOT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Ingreso |
| Q02 | - |  |  | SI | Establecimiento |
| Q03 | - |  |  | SI | Servicio |
| Q04 | - |  |  | SI | Diagnostico |
| Q05 | - |  |  | SI | Criterios de Asignacion de Riesgo |
| Q06 | - |  |  | SI | Caídas Anteriores |
| Q07 | - |  |  | SI | Debilidad Muscular |
| Q08 | - |  |  | SI | Deterioro de la vista |
| Q09 | - |  |  | SI | Alteración de la Audición o Equilibrio |
| Q10 | - |  |  | SI | Edad: Menores de 1 año |
| Q11 | - |  |  | SI | Edad: Mayores de 75 año |
| Q12 | - |  |  | SI | Alteraciones Neurologícas |
| Q13 | - |  |  | SI | Trastornos Síquicos o Mentales |
| Q14 | - |  |  | SI | Alteraciones del Ritmo Cardiovascular |
| Q15 | - |  |  | SI | Deambulación con Apoyo |
| Q16 | - |  |  | SI | Agitación Psicomotora |
| Q17 | - |  |  | SI | Transtornos Gastrointestinales |
| Q18 | - |  |  | SI | Tratamiento Farmacologico |
| Q19 | - |  |  | SI | Diuréticos |
| Q20 | - |  |  | SI | Hipotensores |
| Q21 | - |  |  | SI | Quimioterápicos (Efectos Adversos) |
| Q22 | - |  |  | SI | Depresores del SNC |
| Q23 | - |  |  | SI | Anestesia General Reciente (12hrs. Post Anestesia) |
| Q24 | - |  |  | SI | Drogas vaso activas |
| Q25 | - |  |  | SI | Puntaje Total |
| Q26 | - |  |  | SI | Criterios de Asignación de Riesgo |
| Q27 | - |  |  | SI | Tratamiento Farmacológico |
| Q28 | - |  |  | SI | Servicio |
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