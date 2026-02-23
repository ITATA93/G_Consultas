# questionnaire.QTCNIFRA

> Newborn/Infant Fall Risk Assessment Tool

**Schema:** questionnaire
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Newborn/Infant Fall Risk Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Assessment date |
| Q02 | time |  |  | SI | Assessment time |
| Q03 | varchar |  |  | SI | Risk Factors |
| Q04 | varchar |  |  | SI | Preventative Measures |
| Q05 | varchar |  |  | SI | Taking baby out of cot / incubator: |
| Q06 | varchar |  |  | SI | 1.0 For any reason |
| Q07 | varchar |  |  | SI | • The mother is informed about the falls risk |
| Q08 | varchar |  |  | SI | 1.1  For nutrition |
| Q09 | varchar |  |  | SI | • The floor of the mother's room is kept dry |
| Q10 | varchar |  |  | SI | 1.2 For bathing / baby care |
| Q11 | varchar |  |  | SI | • Support of a second person is provided |
| Q12 | varchar |  |  | SI | • The floor of the baby care room is always kept d... |
| Q13 | varchar |  |  | SI | • Bathing of the baby is done in the bathtub of th... |
| Q14 | varchar |  |  | SI | 1.3 For invasive interventions / examinations / ta... |
| Q15 | varchar |  |  | SI | • It is not allowed to hand the baby on during car... |
| Q16 | varchar |  |  | SI | 2. History of falling / dropping the baby |
| Q17 | varchar |  |  | SI | • The mother and the caring team are informed abou... |
| Q18 | varchar |  |  | SI | • Preventative measures against the cause are take... |
| Q19 | varchar |  |  | SI | 3. History of convulsions (of the mother and baby) |
| Q20 | varchar |  |  | SI | • The mother is informed |
| Q21 | varchar |  |  | SI | • She is not allowed to hold the baby by herself |
| Q22 | varchar |  |  | SI | • The mother is recommended to inform the health p... |
| Q23 | varchar |  |  | SI | 4. Invasive and non invasive equipment connected t... |
| Q24 | varchar |  |  | SI | • A safe working environment is provided |
| Q25 | varchar |  |  | SI | • The falling risk that may be caused by the conne... |
| Q26 | varchar |  |  | SI | 5. Transport of the baby |
| Q27 | varchar |  |  | SI | • The floor is inspected for dryness |
| Q28 | varchar |  |  | SI | • The safety of the equipment that will be used is... |
| Q29 | varchar |  |  | SI | • The baby should not be held in the arms, it shou... |
| Q30 | varchar |  |  | SI | • When moved around the cot must held from the met... |
| Q31 | varchar |  |  | SI | • When the baby is transported from the cot / incu... |
| Q32 | varchar |  |  | SI | • When an elevator is used during the transport of... |
| Q33 | varchar |  |  | SI | 6. Pain scores (equal or greater than 1) |
| Q34 | varchar |  |  | SI | • Treatment is initiated according to pain scores |
| Q35 | varchar |  |  | SI | • The side doors to the incubator should always be... |
| Q36 | varchar |  |  | SI | 7. Deterioration in the clinical status of the bab... |
| Q37 | varchar |  |  | SI | • The doctor of the baby is informed |
| Q38 | varchar |  |  | SI | • The mother is informed about risks of falling |
| Q39 | varchar |  |  | SI | 8. Risks regarding mother: |
| Q40 | varchar |  |  | SI | 8.1 Changes in the clinical condition (hypoglycemi... |
| Q41 | varchar |  |  | SI | • The risk of falling is evaluated by the 'Adult f... |
| Q42 | varchar |  |  | SI | • The mother is not allowed to hold the baby by he... |
| Q43 | varchar |  |  | SI | • The mother is informed about the risks of fallin... |
| Q44 | varchar |  |  | SI | 8.2 Disabled (physically disabled) mother who is t... |
| Q45 | varchar |  |  | SI | • The doctor of the baby is informed |
| Q46 | varchar |  |  | SI | • The mother is informed about the risks of fallin... |
| Q47 | varchar |  |  | SI | 8.3 Specific medication use (sedatives, hypnotics ... |
| Q48 | varchar |  |  | SI | • The mother is allowed to hold the baby in the su... |
| Q49 | varchar |  |  | SI | • The doctor of the baby is informed |
| Q50 | varchar |  |  | SI | 8.4 Pain scores (equal or greater than 1) |
| Q51 | varchar |  |  | SI | • The mother is informed about the risks of fallin... |
| Q52 | varchar |  |  | SI | • If pain score is equal or greater than 4, the mo... |
| Q53 | varchar |  |  | SI | • The doctor of the mother is informed |
| Q54 | varchar |  |  | SI | 8.5 Unawareness of the mother / family of the fall... |
| Q55 | varchar |  |  | SI | • The mother / accompanying person is re-educated ... |
| Q56 | varchar |  |  | SI | 9. Mother staying in hospital by herself |
| Q57 | varchar |  |  | SI | • The mother is informed to ask for nursing suppor... |
| Q58 | varchar |  |  | SI | 10. Mother who is given patient controlled analges... |
| Q59 | varchar |  |  | SI | • The mother is not allowed to move around by hers... |
| Q60 | varchar |  |  | SI | • The mother is not allowed to hold the baby when ... |
| Q61 | varchar |  |  | SI | • Support of a second person (nurse, accompanying ... |
| Q62 | varchar |  |  | SI | • The doctor of the mother is informed |
| Q63 | varchar |  |  | SI | (height difference may unbalance the cot, the cot ... |
| Q64 | varchar |  |  | SI | Score |
| Q65 | varchar |  |  | SI | Classification |
| Q66 | varchar |  |  | SI | 1 - 3 |
| Q67 | varchar |  |  | SI | Low Risk |
| Q68 | varchar |  |  | SI | Preventative Measures |
| Q69 | varchar |  |  | SI | 1. Preventative measures are taken against the det... |
| Q70 | varchar |  |  | SI | 2. The mother is informed about the risk of fallin... |
| Q71 | varchar |  |  | SI | 3. The falling risk of the mother is evaluated by ... |
| Q72 | varchar |  |  | SI | 4 - 22 |
| Q73 | varchar |  |  | SI | High Risk |
| Q74 | varchar |  |  | SI | Preventative Measures |
| Q75 | varchar |  |  | SI | 1. Preventative measures are taken against the det... |
| Q76 | varchar |  |  | SI | 2. The mother is informed about the risk of fallin... |
| Q77 | varchar |  |  | SI | 3. The falling risk of the mother is evaluated by ... |
| Q78 | varchar |  |  | SI | 4. Support of a second nurse is provided whenever ... |
| Q79 | varchar |  |  | SI | The risks for a newborn, including the risks for f... |
| Q80 | varchar |  |  | SI | This tool should be used in routine monitoring of ... |
| Q81 | varchar |  |  | SI | 1 - 3: Low Risk |
| Q82 | varchar |  |  | SI | 4 - 22: High Risk |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*