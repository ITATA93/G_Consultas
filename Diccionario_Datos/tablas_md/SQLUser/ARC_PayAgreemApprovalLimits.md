# SQLUser.ARC_PayAgreemApprovalLimits

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPRLIM_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| APPRLIM_ApprovalLimit | double |  |  | SI | Approval Limit |
| APPRLIM_Childsub | double |  |  | NO | Childsub |
| APPRLIM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APPRLIM_Contract_DR | bigint |  | FK | SI | Des Ref Contract |
| APPRLIM_CreatedDate | date |  |  | SI | Created Date |
| APPRLIM_CreatedTime | time |  |  | SI | Created Time |
| APPRLIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPRLIM_DateFrom | date |  |  | SI | DateFrom |
| APPRLIM_DateTo | date |  |  | SI | DateTo |
| APPRLIM_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| APPRLIM_EpisodeType | varchar |  |  | SI | Episode Type |
| APPRLIM_OrdItmStatusList | varchar |  |  | SI | Exempt Order Item Status List |
| APPRLIM_Rank | double |  |  | SI | Rank |
| APPRLIM_RowId | varchar |  |  | NO | - |
| APPRLIM_UpdatedDate | date |  |  | SI | Updated Date |
| APPRLIM_UpdatedTime | time |  |  | SI | Updated Time |
| APPRLIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. Estoy preocupado todo el tiempo pensando en si ... |
| Q02 | - |  |  | SI | 2. Siento que ya no puedo más |
| Q03 | - |  |  | SI | 3. Es terrible y siento que esto nunca va a mejora... |
| Q04 | - |  |  | SI | 4. Es horrible y siento que esto es más fuerte que... |
| Q05 | - |  |  | SI | 5. Siento que no puedo soportarlo más |
| Q06 | - |  |  | SI | 6. Temo que el dolor empeore |
| Q07 | - |  |  | SI | 7. No dejo de pensar en otras situaciones en las q... |
| Q08 | - |  |  | SI | 8. Deseo desesperadamente que desaparezca el dolor |
| Q09 | - |  |  | SI | 9. No puedo apartar el dolor de mi mente |
| Q10 | - |  |  | SI | 10. No dejo de pensar en lo mucho que me duele |
| Q11 | - |  |  | SI | 11. No dejo de pensar en lo mucho que deseo que de... |
| Q12 | - |  |  | SI | 12. No hay nada que pueda hacer para aliviar la in... |
| Q13 | - |  |  | SI | 13. Me pregunto si me puede pasar algo |
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