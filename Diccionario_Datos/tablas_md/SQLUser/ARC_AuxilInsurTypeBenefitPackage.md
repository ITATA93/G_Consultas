# SQLUser.ARC_AuxilInsurTypeBenefitPackage

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLANBENP_ParRef | bigint | PK |  | NO | ARC_AuxilInsurType Parent Reference |
| PLANBENP_Childsub | double |  |  | NO | Childsub |
| PLANBENP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLANBENP_CreatedDate | date |  |  | SI | Created Date |
| PLANBENP_CreatedTime | time |  |  | SI | Created Time |
| PLANBENP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLANBENP_DateFrom | date |  |  | SI | Date From |
| PLANBENP_DateTo | date |  |  | SI | Date To |
| PLANBENP_FreeText1 | varchar |  |  | SI | Free Text 1 |
| PLANBENP_FreeText2 | varchar |  |  | SI | Free Text 2 |
| PLANBENP_IDPayor | varchar |  |  | NO | Benefit Package ID |
| PLANBENP_Name | varchar |  |  | NO | Benefit Package Name |
| PLANBENP_ProductName | varchar |  |  | SI | Product Name |
| PLANBENP_RowId | varchar |  |  | NO | - |
| PLANBENP_UpdatedDate | date |  |  | SI | Updated Date |
| PLANBENP_UpdatedTime | time |  |  | SI | Updated Time |
| PLANBENP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Localización de la herida primaria |
| Q02 | - |  |  | SI | 2. Localización topográfica |
| Q03 | - |  |  | SI | 3. Número de zonas afectadas |
| Q04 | - |  |  | SI | 4. Isquemia |
| Q05 | - |  |  | SI | * ITB: Índice tobillo brazo, medido por doppler |
| Q06 | - |  |  | SI | ** IDB: Índice dedo brazo, con dedo se refiere al ... |
| Q07 | - |  |  | SI | 5. Infección |
| Q08 | - |  |  | SI | 6. Edema |
| Q09 | - |  |  | SI | 7. Neuropatía |
| Q10 | - |  |  | SI | 8. Área |
| Q11 | - |  |  | SI | 9. Profundidad |
| Q12 | - |  |  | SI | 10. Etapa de Cicatrización |
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