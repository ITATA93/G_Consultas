# SQLUser.PAC_MaternalRefusal

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MATREF_RowId | bigint | PK |  | NO | - |
| MATREF_Code | varchar |  |  | NO | Code |
| MATREF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MATREF_CreatedDate | date |  |  | SI | Created Date |
| MATREF_CreatedTime | time |  |  | SI | Created Time |
| MATREF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MATREF_DateFrom | date |  |  | SI | DateFrom |
| MATREF_DateTo | date |  |  | SI | DateTo |
| MATREF_Desc | varchar |  |  | NO | Description |
| MATREF_Owner | varchar |  |  | SI | Owner |
| MATREF_UpdatedDate | date |  |  | SI | Updated Date |
| MATREF_UpdatedTime | time |  |  | SI | Updated Time |
| MATREF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Assessment date |
| Q02 | - |  |  | SI | Assessment time |
| Q03 | - |  |  | SI | Risk Factors |
| Q04 | - |  |  | SI | Preventative Measures |
| Q05 | - |  |  | SI | Taking baby out of cot / incubator: |
| Q06 | - |  |  | SI | 1.0 For any reason |
| Q07 | - |  |  | SI | • The mother is informed about the falls risk |
| Q08 | - |  |  | SI | 1.1  For nutrition |
| Q09 | - |  |  | SI | • The floor of the mother's room is kept dry |
| Q10 | - |  |  | SI | 1.2 For bathing / baby care |
| Q11 | - |  |  | SI | • Support of a second person is provided |
| Q12 | - |  |  | SI | • The floor of the baby care room is always kept d... |
| Q13 | - |  |  | SI | • Bathing of the baby is done in the bathtub of th... |
| Q14 | - |  |  | SI | 1.3 For invasive interventions / examinations / ta... |
| Q15 | - |  |  | SI | • It is not allowed to hand the baby on during car... |
| Q16 | - |  |  | SI | 2. History of falling / dropping the baby |
| Q17 | - |  |  | SI | • The mother and the caring team are informed abou... |
| Q18 | - |  |  | SI | • Preventative measures against the cause are take... |
| Q19 | - |  |  | SI | 3. History of convulsions (of the mother and baby) |
| Q20 | - |  |  | SI | • The mother is informed |
| Q21 | - |  |  | SI | • She is not allowed to hold the baby by herself |
| Q22 | - |  |  | SI | • The mother is recommended to inform the health p... |
| Q23 | - |  |  | SI | 4. Invasive and non invasive equipment connected t... |
| Q24 | - |  |  | SI | • A safe working environment is provided |
| Q25 | - |  |  | SI | • The falling risk that may be caused by the conne... |
| Q26 | - |  |  | SI | 5. Transport of the baby |
| Q27 | - |  |  | SI | • The floor is inspected for dryness |
| Q28 | - |  |  | SI | • The safety of the equipment that will be used is... |
| Q29 | - |  |  | SI | • The baby should not be held in the arms, it shou... |
| Q30 | - |  |  | SI | • When moved around the cot must held from the met... |
| Q31 | - |  |  | SI | • When the baby is transported from the cot / incu... |
| Q32 | - |  |  | SI | • When an elevator is used during the transport of... |
| Q33 | - |  |  | SI | 6. Pain scores (equal or greater than 1) |
| Q34 | - |  |  | SI | • Treatment is initiated according to pain scores |
| Q35 | - |  |  | SI | • The side doors to the incubator should always be... |
| Q36 | - |  |  | SI | 7. Deterioration in the clinical status of the bab... |
| Q37 | - |  |  | SI | • The doctor of the baby is informed |
| Q38 | - |  |  | SI | • The mother is informed about risks of falling |
| Q39 | - |  |  | SI | 8. Risks regarding mother: |
| Q40 | - |  |  | SI | 8.1 Changes in the clinical condition (hypoglycemi... |
| Q41 | - |  |  | SI | • The risk of falling is evaluated by the 'Adult f... |
| Q42 | - |  |  | SI | • The mother is not allowed to hold the baby by he... |
| Q43 | - |  |  | SI | • The mother is informed about the risks of fallin... |
| Q44 | - |  |  | SI | 8.2 Disabled (physically disabled) mother who is t... |
| Q45 | - |  |  | SI | • The doctor of the baby is informed |
| Q46 | - |  |  | SI | • The mother is informed about the risks of fallin... |
| Q47 | - |  |  | SI | 8.3 Specific medication use (sedatives, hypnotics ... |
| Q48 | - |  |  | SI | • The mother is allowed to hold the baby in the su... |
| Q49 | - |  |  | SI | • The doctor of the baby is informed |
| Q50 | - |  |  | SI | 8.4 Pain scores (equal or greater than 1) |
| Q51 | - |  |  | SI | • The mother is informed about the risks of fallin... |
| Q52 | - |  |  | SI | • If pain score is equal or greater than 4, the mo... |
| Q53 | - |  |  | SI | • The doctor of the mother is informed |
| Q54 | - |  |  | SI | 8.5 Unawareness of the mother / family of the fall... |
| Q55 | - |  |  | SI | • The mother / accompanying person is re-educated ... |
| Q56 | - |  |  | SI | 9. Mother staying in hospital by herself |
| Q57 | - |  |  | SI | • The mother is informed to ask for nursing suppor... |
| Q58 | - |  |  | SI | 10. Mother who is given patient controlled analges... |
| Q59 | - |  |  | SI | • The mother is not allowed to move around by hers... |
| Q60 | - |  |  | SI | • The mother is not allowed to hold the baby when ... |
| Q61 | - |  |  | SI | • Support of a second person (nurse, accompanying ... |
| Q62 | - |  |  | SI | • The doctor of the mother is informed |
| Q63 | - |  |  | SI | (height difference may unbalance the cot, the cot ... |
| Q64 | - |  |  | SI | Score |
| Q65 | - |  |  | SI | Classification |
| Q66 | - |  |  | SI | 1 - 3 |
| Q67 | - |  |  | SI | Low Risk |
| Q68 | - |  |  | SI | Preventative Measures |
| Q69 | - |  |  | SI | 1. Preventative measures are taken against the det... |
| Q70 | - |  |  | SI | 2. The mother is informed about the risk of fallin... |
| Q71 | - |  |  | SI | 3. The falling risk of the mother is evaluated by ... |
| Q72 | - |  |  | SI | 4 - 22 |
| Q73 | - |  |  | SI | High Risk |
| Q74 | - |  |  | SI | Preventative Measures |
| Q75 | - |  |  | SI | 1. Preventative measures are taken against the det... |
| Q76 | - |  |  | SI | 2. The mother is informed about the risk of fallin... |
| Q77 | - |  |  | SI | 3. The falling risk of the mother is evaluated by ... |
| Q78 | - |  |  | SI | 4. Support of a second nurse is provided whenever ... |
| Q79 | - |  |  | SI | The risks for a newborn, including the risks for f... |
| Q80 | - |  |  | SI | This tool should be used in routine monitoring of ... |
| Q81 | - |  |  | SI | 1 - 3: Low Risk |
| Q82 | - |  |  | SI | 4 - 22: High Risk |
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