# SQLUser.LBC_Queue

**Schema:** SQLUser
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCQ_RowID | bigint | PK |  | NO | - |
| LBCQ_AlertTime | integer |  |  | SI | Alert Time |
| LBCQ_AtomicResultOnly | varchar |  |  | SI | For External Interface Queue, when ticked, message... |
| LBCQ_ClassificationSystem_DR | bigint |  | FK | SI | Classification System |
| LBCQ_Code | varchar |  |  | NO | Code	 |
| LBCQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCQ_Courier_DR | bigint |  | FK | SI | Courier for Schedule   |
| LBCQ_CreatedDate | date |  |  | SI | Created Date |
| LBCQ_CreatedTime | time |  |  | SI | Created Time |
| LBCQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCQ_DateFrom | date |  |  | SI | Effective date for the record |
| LBCQ_DateTo | date |  |  | SI | Last day the record is active  |
| LBCQ_DefaultTransferQueue_DR | bigint |  | FK | SI | Default Transfer Queue |
| LBCQ_Desc | varchar |  |  | NO | Description  |
| LBCQ_EnableBulkTransfer | varchar |  |  | SI | Enable Bulk Transfer |
| LBCQ_EnableBulkValidation | varchar |  |  | SI | Enable Bulk Validation |
| LBCQ_ExternalInterface_DR | varchar |  | FK | SI | External Interface |
| LBCQ_IncludeConfidentialTest | varchar |  |  | SI | Include Confidential Tests
Only applies to Extern... |
| LBCQ_LabEpisodeFinalOnly | varchar |  |  | SI | Lab Episode Final Only - The test sets will be pro... |
| LBCQ_LabSiteRestrictions | varchar |  |  | SI | Lab Site Restrictions |
| LBCQ_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCQ_MaxTime | integer |  |  | SI | Max Time |
| LBCQ_Owner | varchar |  |  | SI | Owner |
| LBCQ_PreventValidationLRE | varchar |  |  | SI | Prevent validation when accessed via Lab Result En... |
| LBCQ_ProcessAfterMaxTime | varchar |  |  | SI | Process External Interface after Max Time |
| LBCQ_QuarantineBloodUnit | varchar |  |  | SI | Quarantine Blood Unit |
| LBCQ_RecipientBased | varchar |  |  | SI | Recipient Based Interface
Only applies to Externa... |
| LBCQ_RemoveOnAuthorisation | varchar |  |  | SI | - |
| LBCQ_RemoveOnNotPerformed | varchar |  |  | SI | Remove On Not Performed |
| LBCQ_Reportable | varchar |  |  | SI | Reportable
Flag to indicate if queue is reportabl... |
| LBCQ_RestrictResultEntry | varchar |  |  | SI | Restrict Result Entry
Disables all test items not... |
| LBCQ_Sequence | integer |  |  | SI | Sorting Sequence |
| LBCQ_SortOrder | varchar |  |  | SI | Queue Sort Order
Standard type (TestSetSortOrder)... |
| LBCQ_TestItemRestrictions | varchar |  |  | SI | Test Item Restriction
When LBCQRestrictResultEntr... |
| LBCQ_TestSetRestrictions | varchar |  |  | SI | Test Set Restrictions
Only applies to External In... |
| LBCQ_Type | varchar |  |  | SI | Queue Type
Standard type (LabQueueType) to indica... |
| LBCQ_UpdatedDate | date |  |  | SI | Updated Date |
| LBCQ_UpdatedTime | time |  |  | SI | Updated Time |
| LBCQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | VEF1 (lt) Basal Real |
| Q02 | - |  |  | SI | VEF1 (lt) Basal Predicho |
| Q03 | - |  |  | SI | VEF1 (lt) Basal % Predicho |
| Q04 | - |  |  | SI | VEF1 (lt) Basal P95 |
| Q05 | - |  |  | SI | VEF1 (lt) Posbroncodilatador REAL |
| Q06 | - |  |  | SI | VEF1 (lt) Posbroncodilatador % Predicho |
| Q07 | - |  |  | SI | VEF1 (lt) Postboncodilatador % Cambio |
| Q08 | - |  |  | SI | CVF (lt) Basal Real |
| Q09 | - |  |  | SI | CVF (lt) Basal Predicho |
| Q10 | - |  |  | SI | CVF (lt) Basal % Predicho |
| Q11 | - |  |  | SI | CVF (lt) Basal P95 |
| Q12 | - |  |  | SI | CVF (lt) Postbroncodilatador |
| Q13 | - |  |  | SI | CVF (lt) postbroncodilatador % Predicho |
| Q14 | - |  |  | SI | CVF (lt) postbroncodilatador % Cambio |
| Q15 | - |  |  | SI | VEF1/CVF (%) Basal Real |
| Q16 | - |  |  | SI | VEF1/CVF (%) Basal Predicho |
| Q17 | - |  |  | SI | VEF/CVF (%) Basal % Predicho |
| Q18 | - |  |  | SI | VEF/CVF (%) Basal P95 |
| Q19 | - |  |  | SI | VEF/CVF (%) posbroncodilatador REAL |
| Q20 | - |  |  | SI | VEF/CVF (%) Postbroncodilator % Predicho |
| Q21 | - |  |  | SI | VEF/CVF (%) postbroncodilatador % Cambio |
| Q22 | - |  |  | SI | FEF 25-75 (lt/seg) Basal REAL |
| Q23 | - |  |  | SI | FEF 25-75 (lt/seg) Basal Predicho |
| Q24 | - |  |  | SI | FEF 25-75 (lt/seg) Basal % Predicho |
| Q25 | - |  |  | SI | FEF 25-75 (lt/seg) Basal P95 |
| Q26 | - |  |  | SI | FEF 25-75 (lt/seg) postbroncodilatador Real |
| Q27 | - |  |  | SI | FEF 25-75 (lt/seg) postbroncodilatador % Predicho |
| Q28 | - |  |  | SI | FEF 25-75 (lt/seg) postbroncodilatador % Cambio |
| Q29 | - |  |  | SI | Conclusión |
| Q30 | - |  |  | SI | Espirometría |
| Q31 | - |  |  | SI | Peso |
| Q31ObsDR | - |  |  | SI | Peso DR |
| Q32 | - |  |  | SI | Talla |
| Q32ObsDR | - |  |  | SI | Talla DR |
| Q33 | - |  |  | SI | IMC |
| Q34 | - |  |  | SI | Edad |
| Q35 | - |  |  | SI | Meses |
| Q36 | - |  |  | SI | Días |
| Q37 | - |  |  | SI | Diferencia en Litros del VEF1 |
| Q38 | - |  |  | SI | Diferencia en Litros de la CVF |
| Q39 | - |  |  | SI | Diferencia en Litros de la FEF 25-75 |
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