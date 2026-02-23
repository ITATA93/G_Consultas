# SQLUser.PAC_ContVenue

**Schema:** SQLUser
**Columnas:** 151
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTVENUE_RowId | bigint | PK |  | NO | - |
| CONTVENUE_Code | varchar |  |  | NO | Code |
| CONTVENUE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTVENUE_CreatedDate | date |  |  | SI | Created Date |
| CONTVENUE_CreatedTime | time |  |  | SI | Created Time |
| CONTVENUE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTVENUE_DateFrom | date |  |  | SI | Date From |
| CONTVENUE_DateTo | date |  |  | SI | Date To |
| CONTVENUE_Desc | varchar |  |  | NO | Description |
| CONTVENUE_Owner | varchar |  |  | SI | Owner |
| CONTVENUE_UpdatedDate | date |  |  | SI | Updated Date |
| CONTVENUE_UpdatedTime | time |  |  | SI | Updated Time |
| CONTVENUE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ57DR | - |  |  | SI | Child Reference: Add staff member |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Parity |
| Q04 | - |  |  | SI | Number of previous vaginal birth(s) |
| Q05 | - |  |  | SI | Fetus number |
| Q06 | - |  |  | SI | No indication is absolute and clinical judgement i... |
| Q07 | - |  |  | SI | Indications |
| Q08 | - |  |  | SI | Indications (other) |
| Q09 | - |  |  | SI | Potential contraindications |
| Q10 | - |  |  | SI | Potential contraindications (other) |
| Q11 | - |  |  | SI | Presence of factors associated with higher rate of... |
| Q12 | - |  |  | SI | Presence of factors (other) |
| Q13 | - |  |  | SI | Fetal descent |
| Q14 | - |  |  | SI | Fetal descent (other) |
| Q15 | - |  |  | SI | Cervix is fully dilated and the membranes ruptured |
| Q16 | - |  |  | SI | Cervix is fully dilated and the membranes ruptured... |
| Q17 | - |  |  | SI | Station at level of ischial spines or below |
| Q18 | - |  |  | SI | Station at level of ischial spines or below (other... |
| Q19 | - |  |  | SI | Position of the fetal head has been determined |
| Q20 | - |  |  | SI | Position of the fetal head has been determined (ot... |
| Q21 | - |  |  | SI | Ultrasound assessment of the fetal head position p... |
| Q22 | - |  |  | SI | Ultrasound assessment of the fetal head position |
| Q23 | - |  |  | SI | Ultrasound assessment notes |
| Q24 | - |  |  | SI | Caput and moulding is no more than moderate (or +2... |
| Q25 | - |  |  | SI | Caput and moulding (other) |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | Outlet |
| Q28 | - |  |  | SI | Low |
| Q29 | - |  |  | SI | Mid |
| Q30 | - |  |  | SI | Fetal scalp visible without separating the labia |
| Q31 | - |  |  | SI | Fetal skull has reached the perineum |
| Q32 | - |  |  | SI | Rotation does not exceed 45° |
| Q33 | - |  |  | SI | Fetal skull is at station +2 cm, but not on the pe... |
| Q34 | - |  |  | SI | Two subdivisions: |
| Q35 | - |  |  | SI | 1. Non-rotational ≤45° |
| Q36 | - |  |  | SI | 2. Rotational &gt |
| Q37 | - |  |  | SI | Fetal head is no more than one-fifth palpable per ... |
| Q38 | - |  |  | SI | Leading point of the skull is at station 0 or +1cm |
| Q39 | - |  |  | SI | Two subdivisions: |
| Q40 | - |  |  | SI | 1. Non-rotational ≤45° |
| Q41 | - |  |  | SI | 2. Rotational &gt |
| Q42 | - |  |  | SI | Examination notes |
| Q43 | - |  |  | SI | Clear explanation given and woman's consent obtain... |
| Q44 | - |  |  | SI | Consent notes |
| Q45 | - |  |  | SI | Clear explanation given and written woman's consen... |
| Q46 | - |  |  | SI | Trust established and full cooperation sought and ... |
| Q47 | - |  |  | SI | Discussion notes |
| Q48 | - |  |  | SI | Appropriate analgesia is in place |
| Q49 | - |  |  | SI | For midpelvic or rotational birth, this will usual... |
| Q50 | - |  |  | SI | Other analgesia notes |
| Q51 | - |  |  | SI | Bladder emptied |
| Q52 | - |  |  | SI | Bladder emptying time |
| Q53 | - |  |  | SI | Aseptic measures are in place |
| Q54 | - |  |  | SI | Facilities in place |
| Q55 | - |  |  | SI | Other facilities |
| Q56 | - |  |  | SI | For midpelvic births, theatre facilities should be... |
| Q59 | - |  |  | SI | Total number of pulls |
| Q60 | - |  |  | SI | Instrumental vaginal birth procedure notes |
| Q61 | - |  |  | SI | Fetal complications |
| Q62 | - |  |  | SI | Other fetal complications |
| Q63 | - |  |  | SI | Maternal complications |
| Q64 | - |  |  | SI | Other maternal complications |
| Q65 | - |  |  | SI | Prophylactic antibiotics |
| Q66 | - |  |  | SI | Thromboprophylaxis |
| Q67 | - |  |  | SI | Post - procedure analgesia |
| Q68 | - |  |  | SI | Urine void monitoring |
| Q69 | - |  |  | SI | Post-intervention discussion with operator |
| Q70 | - |  |  | SI | Pelvic floor assessment |
| Q71 | - |  |  | SI | Psychological assessment |
| Q72 | - |  |  | SI | Information for future birth |
| Q73 | - |  |  | SI | When should vacuum-assisted birth be discontinued ... |
| Q74 | - |  |  | SI | •&nbsp |
| Q75 | - |  |  | SI | •&nbsp |
| Q76 | - |  |  | SI | •&nbsp |
| Q77 | - |  |  | SI | the fetal position has been incorrectly diagnosed ... |
| Q78 | - |  |  | SI | Experienced operators should re-evaluate the clini... |
| Q79 | - |  |  | SI | •&nbsp |
| Q80 | - |  |  | SI | Less experienced operators should seek senior supp... |
| Q81 | - |  |  | SI | •&nbsp |
| Q82 | - |  |  | SI | •&nbsp |
| Q83 | - |  |  | SI | However, the operator needs to balance the risks o... |
| Q84 | - |  |  | SI | •&nbsp |
| Q85 | - |  |  | SI | and should inform the neonatologist when this occu... |
| Q86 | - |  |  | SI | •&nbsp |
| Q87 | - |  |  | SI | When should attempted forceps birth be discontinue... |
| Q88 | - |  |  | SI | •&nbsp |
| Q89 | - |  |  | SI | •&nbsp |
| Q90 | - |  |  | SI | •&nbsp |
| Q91 | - |  |  | SI | •&nbsp |
| Q92 | - |  |  | SI | the position has been incorrectly diagnosed or the... |
| Q93 | - |  |  | SI | •&nbsp |
| Q94 | - |  |  | SI | •&nbsp |
| Q95 | - |  |  | SI | •&nbsp |
| Q96 | - |  |  | SI | •&nbsp |
| Q97 | - |  |  | SI | and should be prepared to disimpact the fetal head... |
| Q98 | - |  |  | SI | Murphy, DJ,&nbsp |
| Q99 | - |  |  | SI | Facilities in place |
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