# SQLUser.PAC_AllocationReason

**Schema:** SQLUser
**Columnas:** 144
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALLREA_RowId | bigint | PK |  | NO | - |
| ALLREA_Code | varchar |  |  | NO | Code |
| ALLREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALLREA_CreatedDate | date |  |  | SI | Created Date |
| ALLREA_CreatedTime | time |  |  | SI | Created Time |
| ALLREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALLREA_Desc | varchar |  |  | NO | Description |
| ALLREA_Owner | varchar |  |  | SI | Owner |
| ALLREA_UpdatedDate | date |  |  | SI | Updated Date |
| ALLREA_UpdatedTime | time |  |  | SI | Updated Time |
| ALLREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Post-op day |
| Q04 | - |  |  | SI | Alert and oriented |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Patient monitored and assessed for delirium |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q11 | - |  |  | SI | Variance |
| Q12 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Patient provided education on using patient-contro... |
| Q15 | - |  |  | SI | Variance |
| Q16 | - |  |  | SI | All medication administered as ordered |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | Intravenous fluid therapy administered as prescrib... |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | Patient is receiving appropriate venous thrombus p... |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Patient provided education and demonstrated how to... |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Patient supervised in the self administration of e... |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | All ordered investigations / tests taken and resul... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Episodes of nausea and vomiting are effectively co... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Patient is tolerating oral fluids and diet |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Strict fluid balance chart maintained |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Urine output > 30 mLs per hour |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | All bowel motions documented |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | Drain remained patent and all drainage documented.... |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Drain removed as ordered with no complications |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Surgical wound observed for signs of haematoma, oo... |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Surgical wound observed for signs of haematoma, oo... |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Patient skin integrity assessed and free from pres... |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Patient has received regular pressure area care wi... |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Pressure relieving devices in situ as needed |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | Personal hygiene attended |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Patient showered with assistance |
| Q57 | - |  |  | SI | Variance |
| Q58 | - |  |  | SI | Patient received mouth care as clinically indicate... |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Hip abduction pillow insitu (for 24 hours post-op) |
| Q61 | - |  |  | SI | Variance |
| Q62 | - |  |  | SI | Patient has stood / sat out of bed, if indicated |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Patient mobilised with assistance from physiothera... |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | All interventions explained to patient / family |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Patient provided orientation to ward if required |
| Q69 | - |  |  | SI | Variance |
| Q70 | - |  |  | SI | Patient safety considered, bedside rails, boarder ... |
| Q71 | - |  |  | SI | Variance |
| Q72 | - |  |  | SI | Complex case coordinator review if indicated |
| Q73 | - |  |  | SI | Variation |
| Q74 | - |  |  | SI | Occupational therapist has reviewed and assessed f... |
| Q75 | - |  |  | SI | Variance |
| Q76 | - |  |  | SI | Referrals arranged as necessary. Consider rehabili... |
| Q77 | - |  |  | SI | Variance |
| Q78 | - |  |  | SI | Commence discharge planning |
| Q79 | - |  |  | SI | Variance |
| Q80 | - |  |  | SI | Continue discharge planning |
| Q81 | - |  |  | SI | Variation |
| Q82 | - |  |  | SI | Outpatient appointment booked |
| Q83 | - |  |  | SI | Variation |
| Q84 | - |  |  | SI | Plan for suture removal |
| Q85 | - |  |  | SI | Variation |
| Q86 | - |  |  | SI | Enoxaparin information pack provided to patient |
| Q87 | - |  |  | SI | Variation |
| Q88 | - |  |  | SI | Community referral for enoxaparin administration i... |
| Q89 | - |  |  | SI | Variation |
| Q90 | - |  |  | SI | Equipment is ready for discharge |
| Q91 | - |  |  | SI | Variation |
| Q92 | - |  |  | SI | Discharge medications ordered |
| Q93 | - |  |  | SI | Variation |
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