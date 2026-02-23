# SQLUser.ARC_AuxilInsurTypePostOffice

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLANPO_ParRef | bigint | PK |  | NO | ARC_AuxilInsurType Parent Reference |
| PLANPO_Childsub | double |  |  | NO | Childsub |
| PLANPO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLANPO_CreatedDate | date |  |  | SI | Created Date |
| PLANPO_CreatedTime | time |  |  | SI | Created Time |
| PLANPO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLANPO_DateFrom | date |  |  | SI | Date From |
| PLANPO_DateTo | date |  |  | SI | Date To |
| PLANPO_PostOffice_DR | bigint |  | FK | NO | Post Office |
| PLANPO_RowId | varchar |  |  | NO | - |
| PLANPO_UpdatedDate | date |  |  | SI | Updated Date |
| PLANPO_UpdatedTime | time |  |  | SI | Updated Time |
| PLANPO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. ¿Te has sentido bajoneado/a, deprimido/a, irrit... |
| Q02 | - |  |  | SI | 2. ¿Has tenido poco interés o placer al hacer las ... |
| Q03 | - |  |  | SI | 3. ¿Has tenido problemas para quedarte dormido/a, ... |
| Q04 | - |  |  | SI | 4. ¿Te has sentido cansado/a o con poca energía? |
| Q05 | - |  |  | SI | 5. ¿Has tenido poco apetito, has bajado de peso, o... |
| Q06 | - |  |  | SI | 6. ¿Te has sentido mal respecto de ti mismo/a– o h... |
| Q07 | - |  |  | SI | 7. ¿Has tenido problemas para concentrarte en acti... |
| Q08 | - |  |  | SI | 8. ¿Te has movido o hablado tan lento que las otra... |
| Q09 | - |  |  | SI | 9. ¿Has pensado que sería mejor estar muerto/a o h... |
| Q10 | - |  |  | SI | a. En el último año, ¿te has sentido deprimido o t... |
| Q11 | - |  |  | SI | b. Si estás experimentando alguno de los problemas... |
| Q12 | - |  |  | SI | c. Durante el último mes ¿has pensado en algún mom... |
| Q13 | - |  |  | SI | d. Alguna vez en tu vida, ¿has tratado de matarte ... |
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