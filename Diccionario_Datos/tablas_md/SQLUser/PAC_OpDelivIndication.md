# SQLUser.PAC_OpDelivIndication

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPDEL_RowId | bigint | PK |  | NO | - |
| OPDEL_Active | varchar |  |  | SI | OPDEL_Active |
| OPDEL_Code | varchar |  |  | NO | Code |
| OPDEL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPDEL_CreatedDate | date |  |  | SI | Created Date |
| OPDEL_CreatedTime | time |  |  | SI | Created Time |
| OPDEL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPDEL_DateFrom | date |  |  | SI | Date From |
| OPDEL_DateTo | date |  |  | SI | Date To |
| OPDEL_Desc | varchar |  |  | NO | Description |
| OPDEL_NationalCode | varchar |  |  | SI | National code |
| OPDEL_Owner | varchar |  |  | SI | Owner |
| OPDEL_UpdatedDate | date |  |  | SI | Updated Date |
| OPDEL_UpdatedTime | time |  |  | SI | Updated Time |
| OPDEL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Intensidad del Dolor |
| Q02 | - |  |  | SI | Cuidado personal (lavarse, vestirse, etc) |
| Q03 | - |  |  | SI | Levantamiento de objetos |
| Q04 | - |  |  | SI | Caminar |
| Q05 | - |  |  | SI | Sentarse |
| Q06 | - |  |  | SI | Permanecer de pie |
| Q07 | - |  |  | SI | Dormir |
| Q08 | - |  |  | SI | Vida sexual |
| Q09 | - |  |  | SI | Vida social |
| Q10 | - |  |  | SI | Viajar |
| Q11 | - |  |  | SI | Tipo de Visita |
| Q12 | - |  |  | SI | 0% - 20%: Discapacidad mínima |
| Q13 | - |  |  | SI | 21% – 40%: Discapacidad moderada |
| Q14 | - |  |  | SI | 41% – 60%: Discapacidad severa |
| Q15 | - |  |  | SI | 61% – 80%: Dolor de espalda invalidante |
| Q16 | - |  |  | SI | 81% – 100%:&nbsp |
| Q17 | - |  |  | SI | Each section is scored on a 0–5 scale, 5 represent... |
| Q18 | - |  |  | SI | The index is calculated by dividing the summed sco... |
| Q19 | - |  |  | SI | To assess symptoms and severity of low back pain i... |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | 0% - 20% |
| Q23 | - |  |  | SI | Minimal disability |
| Q24 | - |  |  | SI | 21% – 40% |
| Q25 | - |  |  | SI | Moderate disability |
| Q26 | - |  |  | SI | 41% – 60% |
| Q27 | - |  |  | SI | Severe disability |
| Q28 | - |  |  | SI | 61% – 80% |
| Q29 | - |  |  | SI | Crippling back pain |
| Q30 | - |  |  | SI | 81% – 100% |
| Q31 | - |  |  | SI | These patients are either bed-bound or have an exa... |
| Q32 | - |  |  | SI | Score |
| Q33 | - |  |  | SI | Percentage |
| Q34 | - |  |  | SI | All sections are 'Not applicable |
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