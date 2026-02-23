# SQLUser.ARC_AuxilInsurType

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUXIT_RowId | bigint | PK |  | NO | - |
| AUXIT_Category | varchar |  |  | SI | Category |
| AUXIT_Code | varchar |  |  | NO | Code |
| AUXIT_Code1 | varchar |  |  | SI | Code1 |
| AUXIT_Code2 | varchar |  |  | SI | Code2 |
| AUXIT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AUXIT_CodeTranslated | varchar |  |  | SI | Code Translated |
| AUXIT_CreatedDate | date |  |  | SI | Created Date |
| AUXIT_CreatedTime | time |  |  | SI | Created Time |
| AUXIT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AUXIT_DateFrom | date |  |  | SI | Date From |
| AUXIT_DateTo | date |  |  | SI | Date To |
| AUXIT_Desc | varchar |  |  | NO | Description |
| AUXIT_DescTranslated | varchar |  |  | SI | Description Translated |
| AUXIT_ExclFromBatchInvoice | varchar |  |  | SI | Exclude From Batch Invoice |
| AUXIT_GenSeparateBatch | varchar |  |  | SI | GenSeparateBatch |
| AUXIT_InsType_DR | bigint |  | FK | NO |  Des Ref to InsType |
| AUXIT_NationalCode | varchar |  |  | SI | National Code |
| AUXIT_Owner | varchar |  |  | SI | Owner |
| AUXIT_PlanGroup1 | varchar |  |  | SI | Plan Group 1 |
| AUXIT_PlanGroup2 | varchar |  |  | SI | Plan Group 2 |
| AUXIT_PlanGroup3 | varchar |  |  | SI | Plan Group 3 |
| AUXIT_PlanGroup4 | varchar |  |  | SI | Plan Group 4 |
| AUXIT_PlanGroup5 | varchar |  |  | SI | Plan Group 5 |
| AUXIT_PlanGroup6 | varchar |  |  | SI | Plan Group 6 |
| AUXIT_Priority | double |  |  | SI | Priority |
| AUXIT_QualificationStatusDR | bigint |  | FK | SI | Qualification Status DR |
| AUXIT_Subregion_DR | bigint |  | FK | SI | Subregion  |
| AUXIT_UpdatedDate | date |  |  | SI | Updated Date |
| AUXIT_UpdatedTime | time |  |  | SI | Updated Time |
| AUXIT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tratamiento Endodóntico |
| Q02 | - |  |  | SI | Piezas |
| Q03 | - |  |  | SI | 1. Preparación de conducto(s) e instrumentos biome... |
| Q04 | - |  |  | SI | Longitud Aparente del Diente |
| Q05 | - |  |  | SI | Radiografía de Control de Longitud |
| Q06 | - |  |  | SI | Longitud Real del Diente |
| Q07 | - |  |  | SI | 2. Irrigación y acondicionamiento |
| Q10 | - |  |  | SI | Imprimir Indicaciones |
| Q11 | - |  |  | SI | Radiografia de Control |
| Q12 | - |  |  | SI | Observaciones |
| Q17 | - |  |  | SI | Pronostico |
| Q18 | - |  |  | SI | Conductor |
| Q19 | - |  |  | SI | Conducto 2 |
| Q20 | - |  |  | SI | Conducto 3 |
| Q21 | - |  |  | SI | Conducto 4 |
| Q22 | - |  |  | SI | Longitud Aparente del Diente 2 |
| Q23 | - |  |  | SI | Longitud Aparente del Diente 3 |
| Q24 | - |  |  | SI | Longitud Aparente del Diente 4 |
| Q25 | - |  |  | SI | Radiografía de Control de Longitud 2 |
| Q26 | - |  |  | SI | Radiografía de Control de Longitud 3 |
| Q27 | - |  |  | SI | Radiografía de Control de Longitud 4 |
| Q28 | - |  |  | SI | Imprimir |
| Q28UDt | - |  |  | SI | Imprimir Last Updated Date |
| Q28UTm | - |  |  | SI | Imprimir Last Updated Time |
| Q29 | - |  |  | SI | 3. Sellando de Conducto |
| Q32 | - |  |  | SI | observacion 1 |
| Q39 | - |  |  | SI | Categoria de la carta |
| Q41 | - |  |  | SI | Digitado Por |
| Q50 | - |  |  | SI | Longitud Real del Diente 2 |
| Q51 | - |  |  | SI | Longitud Real del Diente 3 |
| Q52 | - |  |  | SI | Longitud Real del Diente 4 |
| QRem1 | - |  |  | SI | Instalación/Alta |
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