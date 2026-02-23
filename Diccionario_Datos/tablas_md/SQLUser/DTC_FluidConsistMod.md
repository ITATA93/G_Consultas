# SQLUser.DTC_FluidConsistMod

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLCNS_RowId | bigint | PK |  | NO | - |
| FLCNS_Code | varchar |  |  | NO | Code |
| FLCNS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FLCNS_CreatedDate | date |  |  | SI | Created Date |
| FLCNS_CreatedTime | time |  |  | SI | Created Time |
| FLCNS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FLCNS_DateFrom | date |  |  | SI | Date From |
| FLCNS_DateTo | date |  |  | SI | Date To |
| FLCNS_Desc | varchar |  |  | NO | Description |
| FLCNS_Owner | varchar |  |  | SI | Owner |
| FLCNS_UpdatedDate | date |  |  | SI | Updated Date |
| FLCNS_UpdatedTime | time |  |  | SI | Updated Time |
| FLCNS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Transport arranged |
| Q02 | - |  |  | SI | Someone staying with patient overnight |
| Q03 | - |  |  | SI | Carer's name and phone number |
| Q04 | - |  |  | SI | Support services arranged |
| Q05 | - |  |  | SI | Type of service |
| Q06 | - |  |  | SI | Phone number |
| Q07 | - |  |  | SI | Action taken |
| Q08 | - |  |  | SI | Patient lives within 20km of a hospital |
| Q09 | - |  |  | SI | Accommodation arranged |
| Q10 | - |  |  | SI | Medical certificate required |
| Q11 | - |  |  | SI | Completed and given to the patient |
| Q12 | - |  |  | SI | ECG monitoring commenced |
| Q13 | - |  |  | SI | Any difficulties with swallowing |
| Q14 | - |  |  | SI | Antiseptic wash |
| Q15 | - |  |  | SI | Lie flat post sheath removal |
| Q16 | - |  |  | SI | May sit up at |
| Q17 | - |  |  | SI | Bed rest |
| Q18 | - |  |  | SI | Ambulate at |
| Q19 | - |  |  | SI | Food and fluids as desired at |
| Q20 | - |  |  | SI | Observe wound / puncture site blood pressure, puls... |
| Q21 | - |  |  | SI | Observe wound / puncture site blood pressure, puls... |
| Q22 | - |  |  | SI | Continue medication as charted |
| Q23 | - |  |  | SI | No arm movements on affected side for 24 hours |
| Q24 | - |  |  | SI | Post procedure ECG |
| Q25 | - |  |  | SI | Post procedure X-Ray on inspiration / non inspirat... |
| Q26 | - |  |  | SI | Patient requires telemetry monitoring |
| Q27 | - |  |  | SI | Check activated clotting time at |
| Q28 | - |  |  | SI | Other |
| Q29 | - |  |  | SI | Report to HMO immediately |
| Q30 | - |  |  | SI | - signs of peripheral ischaemia |
| Q31 | - |  |  | SI | - insertion / puncture site haematoma |
| Q32 | - |  |  | SI | IV cannula removed |
| Q33 | - |  |  | SI | Wound dry and dressing intact |
| Q34 | - |  |  | SI | Nausea and vomiting controlled |
| Q35 | - |  |  | SI | Pain controlled |
| Q36 | - |  |  | SI | Tolerating fluids and diet |
| Q37 | - |  |  | SI | Discharge medication given to patient |
| Q38 | - |  |  | SI | Home management plan understood by patient and car... |
| Q39 | - |  |  | SI | Vital signs within normal parameters |
| Q40 | - |  |  | SI | Valuables returned to patient |
| Q41 | - |  |  | SI | Follow up appointment arranged |
| Q42 | - |  |  | SI | Patient ambulant without assistance (if previously... |
| Q43 | - |  |  | SI | Patient reviewed by medical staff |
| Q44 | - |  |  | SI | Cardiac rehabilitation referral completed |
| Q45 | - |  |  | SI | Medications to be recommenced as per medication ch... |
| Q46 | - |  |  | SI | Date |
| Q47 | - |  |  | SI | Time |
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