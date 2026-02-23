# SQLUser.CT_Company

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCO_RowId | bigint | PK |  | NO | - |
| CTCO_Addr | varchar |  |  | SI | Address |
| CTCO_ApPer_DR | varchar |  | FK | SI | Not Used Financial Period - des ref to CTFPR |
| CTCO_ApYr | double |  |  | SI | AP Financial Year |
| CTCO_ArPer_DR | varchar |  | FK | SI | Not Used AR Financial Year - des ref to CTFP |
| CTCO_ArYr | double |  |  | SI | AR Financial Year |
| CTCO_City_DR | bigint |  | FK | SI | Des Ref to CTCIT |
| CTCO_Code | varchar |  |  | NO | Company Code |
| CTCO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTCO_ContractPerson | varchar |  |  | SI | Contact Person |
| CTCO_CreatedDate | date |  |  | SI | Created Date |
| CTCO_CreatedTime | time |  |  | SI | Created Time |
| CTCO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCO_Desc | varchar |  |  | NO | Description |
| CTCO_GLPer_DR | varchar |  | FK | SI | Not Used Financial Period - des ref to CTFPR |
| CTCO_GLYr | double |  |  | SI | GL Financial Year |
| CTCO_HanjinChild | varchar |  |  | SI | Child Company of Hanjin |
| CTCO_NotUseFlag | varchar |  |  | SI | Not Use Flag |
| CTCO_Owner | varchar |  |  | SI | Owner |
| CTCO_Password | varchar |  |  | SI | Company Password |
| CTCO_PrimBillingCode | varchar |  |  | SI | Primary Billing Code |
| CTCO_Remarks | varchar |  |  | SI | Remarks |
| CTCO_SecondBillCode | varchar |  |  | SI | Secondary Billing Code |
| CTCO_ShDesc | varchar |  |  | SI | Short Company Desc |
| CTCO_State_DR | bigint |  | FK | SI | Des Ref to CTSTT |
| CTCO_Tel | varchar |  |  | SI | Company Telephone |
| CTCO_UpdatedDate | date |  |  | SI | Updated Date |
| CTCO_UpdatedTime | time |  |  | SI | Updated Time |
| CTCO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTCO_Zip_DR | bigint |  | FK | SI | Des Ref to CTZIP |
| CTCP_CurrCode_DR | bigint |  | FK | SI | Des Ref to CTCUR |
| Q01 | - |  |  | SI | Diagnóstico |
| Q02 | - |  |  | SI | IMC |
| Q02ObsDR | - |  |  | SI | IMC DR |
| Q03 | - |  |  | SI | Diabetes |
| Q04 | - |  |  | SI | Hipertensión Arterial |
| Q05 | - |  |  | SI | Cáncer |
| Q06 | - |  |  | SI | Inmunodepresión |
| Q07 | - |  |  | SI | Tabaquismo |
| Q08 | - |  |  | SI | Drogadicción |
| Q09 | - |  |  | SI | Insuficiencia Venosa |
| Q10 | - |  |  | SI | Insuficiencia Arterial |
| Q11 | - |  |  | SI | Otras |
| Q12 | - |  |  | SI | Hematocrito |
| Q13 | - |  |  | SI | Hemoglobina |
| Q14 | - |  |  | SI | VHS |
| Q15 | - |  |  | SI | Albuminemia |
| Q16 | - |  |  | SI | Proteinemia |
| Q17 | - |  |  | SI | Glicemia |
| Q18 | - |  |  | SI | Cultivos |
| Q19 | - |  |  | SI | Otros |
| Q20 | - |  |  | SI | Antibióticos |
| Q21 | - |  |  | SI | Corticoesteroides |
| Q22 | - |  |  | SI | Tratamiento anticoagulante |
| Q23 | - |  |  | SI | Otros |
| Q24 | - |  |  | SI | Aspecto (Obsoleto) |
| Q25 | - |  |  | SI | Diámetro (Obsoleto) |
| Q26 | - |  |  | SI | Profundidad (Obsoleto) |
| Q27 | - |  |  | SI | Cantidad Exudado (Obsoleto) |
| Q28 | - |  |  | SI | Calidad Exudado (Obsoleto) |
| Q29 | - |  |  | SI | Tejido Esfacelado/Necrótico (Obsoleto) |
| Q30 | - |  |  | SI | Tejido Granulatorio (Obsoleto) |
| Q31 | - |  |  | SI | Edema (Obsoleto) |
| Q32 | - |  |  | SI | Dolor (Obsoleto) |
| Q33 | - |  |  | SI | Piel Circundante (Obsoleto) |
| Q34 | - |  |  | SI | Agente Utilizado |
| Q35 | - |  |  | SI | Apósito o Cobertura |
| Q36 | - |  |  | SI | Tipo de Fijación |
| Q37 | - |  |  | SI | Describa Antibióticos |
| Q38 | - |  |  | SI | Describa Corticoesteroides |
| Q39 | - |  |  | SI | Describa Anticoagulantes |
| Q40 | - |  |  | SI | Aspecto |
| Q41 | - |  |  | SI | Diámetro |
| Q42 | - |  |  | SI | Profundidad |
| Q43 | - |  |  | SI | Cantidad Exudado |
| Q44 | - |  |  | SI | Calidad Exudado |
| Q45 | - |  |  | SI | Tejido Esfacelado/Necrótico |
| Q46 | - |  |  | SI | Tejido Granulatorio |
| Q47 | - |  |  | SI | Edema |
| Q48 | - |  |  | SI | Dolor |
| Q49 | - |  |  | SI | Piel Circundante |
| Q50 | - |  |  | SI | Hemoglobina Glicosilada |
| Q51 | - |  |  | SI | mg/dL |
| Q52 | - |  |  | SI | mg/dL |
| Q53 | - |  |  | SI | % |
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