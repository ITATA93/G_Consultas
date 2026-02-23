# SQLUser.PAC_WLGuaranteedWait

**Schema:** SQLUser
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLGW_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Procedure to be performed |
| Q02 | - |  |  | SI | Clinician performing procedure |
| Q03 | - |  |  | SI | Assisting clinician |
| Q04 | - |  |  | SI | Date |
| Q05 | - |  |  | SI | Time |
| Q06 | - |  |  | SI | Sedation Agents |
| Q07 | - |  |  | SI | Agent(s) to be used |
| Q08 | - |  |  | SI | 2 staff required, 1 RN or medical staff member |
| Q09 | - |  |  | SI | Fasting: 2 hours solids and liquids |
| Q10 | - |  |  | SI | 6 hours solids 4 hours breast feed 2 hours clear f... |
| Q11 | - |  |  | SI | 2 staff required, 1 accredited |
| Q12 | - |  |  | SI | 2 hours solids |
| Q13 | - |  |  | SI | 2 hours breast feed |
| Q14 | - |  |  | SI | 2 hours clear fluids |
| Q15 | - |  |  | SI | Risk Assessment and Exclusion Criteria for Nitrous... |
| Q16 | - |  |  | SI | Prior adverse event |
| Q17 | - |  |  | SI | Prior allergic reaction |
| Q18 | - |  |  | SI | Significant liver disease / failure |
| Q19 | - |  |  | SI | Acute systemic infection |
| Q20 | - |  |  | SI | Significant cardiovascular impairment |
| Q21 | - |  |  | SI | Immunosuppression |
| Q22 | - |  |  | SI | Abnormal conscious state / risk of raised ICP |
| Q23 | - |  |  | SI | Significant respiratory disease |
| Q24 | - |  |  | SI | Patient receiving opioids or other sedative agents |
| Q25 | - |  |  | SI | Age less than or equal to 6 months(for oral agents... |
| Q26 | - |  |  | SI | Age less than or equal to 2 years(for nitrous oxid... |
| Q27 | - |  |  | SI | Lung cyst |
| Q28 | - |  |  | SI | Bowel obstruction |
| Q29 | - |  |  | SI | Middle ear disease |
| Q30 | - |  |  | SI | Pneumothorax |
| Q31 | - |  |  | SI | Recent retinal surgery |
| Q32 | - |  |  | SI | If YES answered to any of the above criteria, DO N... |
| Q33 | - |  |  | SI | Sedation handout discussed with patient / parent |
| Q34 | - |  |  | SI | Informed consent obtained |
| Q35 | - |  |  | SI | Indications and possible adverse events discussed |
| Q36 | - |  |  | SI | Adequate staff available(minimum of 2 division 1 a... |
| Q37 | - |  |  | SI | Baseline observations recorded |
| Q38 | - |  |  | SI | Positive patient identification name bands in situ... |
| Q39 | - |  |  | SI | Patient fasted as per fasting requirement times |
| Q40 | - |  |  | SI | Private area available / treatment area |
| Q41 | - |  |  | SI | Suction functioning and connected to wall |
| Q42 | - |  |  | SI | Oxygen continuous / wall mounted supply |
| Q43 | - |  |  | SI | Pulse oximetry machine |
| Q44 | - |  |  | SI | Appropriate sized face masks/bag present |
| Q45 | - |  |  | SI | Resuscitation trolley located and available |
| Q46 | - |  |  | SI | Minimum staff present / available |
| Q47 | - |  |  | SI | Disposable nitrous oxide circuit and nitrous cylin... |
| Q48 | - |  |  | SI | Scavenger system attached to circuit |
| Q49 | - |  |  | SI | Portable emergency phone in treatment room |
| Q50 | - |  |  | SI | Emergency sedation pack / reversal drugs present |
| Q51 | - |  |  | SI | Stethoscope and thermometer available |
| Q52 | - |  |  | SI | Drugs ordered on medication chart |
| Q53 | - |  |  | SI | Line of sight medical / nursing provided constantl... |
| Q54 | - |  |  | SI | Observations / Sedation score documented every 5 m... |
| Q55 | - |  |  | SI | Delivered 100% oxygen for 5 minutes |
| Q56 | - |  |  | SI | Patient returned to baseline sedation score |
| Q57 | - |  |  | SI | Observations within normal limits |
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
| WLGW_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WLGW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLGW_CreatedDate | date |  |  | SI | Created Date |
| WLGW_CreatedTime | time |  |  | SI | Created Time |
| WLGW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLGW_DateCalculateWaitFrom | varchar |  |  | SI | DateCalculateWaitFrom |
| WLGW_DateFrom | date |  |  | SI | Date From |
| WLGW_DateTo | date |  |  | SI | Date To |
| WLGW_EpisSubtype_DR | bigint |  | FK | SI | Des Ref EpisSubtype |
| WLGW_HCR_DR | bigint |  | FK | SI | Des Ref HCR |
| WLGW_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| WLGW_Owner | varchar |  |  | SI | Owner |
| WLGW_Services_DR | bigint |  | FK | SI | Des Ref Services |
| WLGW_StatePPP_DR | bigint |  | FK | SI | PAC_StatePPP Des Ref |
| WLGW_TTGWaitTime | double |  |  | SI | TTG Wait Time |
| WLGW_UpdatedDate | date |  |  | SI | Updated Date |
| WLGW_UpdatedTime | time |  |  | SI | Updated Time |
| WLGW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WLGW_WaitTime | double |  |  | SI | Wait Time |
| WLGW_WaitTimeStandard_DR | bigint |  | FK | SI | Des Ref WaitTimeStandard |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*