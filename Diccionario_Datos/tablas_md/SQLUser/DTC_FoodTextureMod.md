# SQLUser.DTC_FoodTextureMod

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FDTXT_RowId | bigint | PK |  | NO | - |
| FDTXT_Code | varchar |  |  | NO | Code |
| FDTXT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FDTXT_CreatedDate | date |  |  | SI | Created Date |
| FDTXT_CreatedTime | time |  |  | SI | Created Time |
| FDTXT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FDTXT_DateFrom | date |  |  | SI | Date From |
| FDTXT_DateTo | date |  |  | SI | Date To |
| FDTXT_Desc | varchar |  |  | NO | Description |
| FDTXT_Owner | varchar |  |  | SI | Owner |
| FDTXT_UpdatedDate | date |  |  | SI | Updated Date |
| FDTXT_UpdatedTime | time |  |  | SI | Updated Time |
| FDTXT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Reason for follow-up |
| Q04 | - |  |  | SI | Other reason for follow up details |
| Q05 | - |  |  | SI | Device |
| Q06 | - |  |  | SI | Device model |
| Q07 | - |  |  | SI | Presenting rhythm |
| Q08 | - |  |  | SI | Rate (bpm) |
| Q09 | - |  |  | SI | Underlying rhythm |
| Q10 | - |  |  | SI | Total atrial paced (%) |
| Q11 | - |  |  | SI | Total ventricular paced (%) |
| Q12 | - |  |  | SI | Biventricular paced (%) |
| Q13 | - |  |  | SI | Left ventricular paced (%) |
| Q14 | - |  |  | SI | Atrial tachycardia / Atrial fibrillation burden (%... |
| Q15 | - |  |  | SI | Model |
| Q16 | - |  |  | SI | Lower rate |
| Q17 | - |  |  | SI | Paced atrioventricular / Sensed atrioventricular |
| Q18 | - |  |  | SI | Cardiac resynchronisation therapy pacemaker (Adapt... |
| Q19 | - |  |  | SI | Battery voltage (V) |
| Q20 | - |  |  | SI | Last charge time (sec) |
| Q21 | - |  |  | SI | Remaining longevity estimate * |
| Q22 | - |  |  | SI | Lead measurements |
| Q23 | - |  |  | SI | Atrium |
| Q24 | - |  |  | SI | Right ventricle |
| Q25 | - |  |  | SI | Left ventricle |
| Q26 | - |  |  | SI | Sensing value |
| Q27 | - |  |  | SI | Pacing threshold |
| Q28 | - |  |  | SI | Impedance |
| Q29 | - |  |  | SI | Sensing value (mV) - Atrium |
| Q30 | - |  |  | SI | Sensing value (mV) - RV |
| Q31 | - |  |  | SI | Pacing threshold (V) - Atrium |
| Q32 | - |  |  | SI | Pacing threshold (V) - RV |
| Q33 | - |  |  | SI | Pacing threshold (V) - LV |
| Q34 | - |  |  | SI | V@ |
| Q35 | - |  |  | SI | V@ |
| Q36 | - |  |  | SI | V@ |
| Q37 | - |  |  | SI | Pacing threshold (ms) - Atrium |
| Q38 | - |  |  | SI | Pacing threshold (ms) - RV |
| Q39 | - |  |  | SI | Pacing threshold (ms) - LV |
| Q40 | - |  |  | SI | ms |
| Q41 | - |  |  | SI | ms |
| Q42 | - |  |  | SI | ms |
| Q43 | - |  |  | SI | Impedance (Ω) - Atrium |
| Q44 | - |  |  | SI | Impedance (Ω) - RV |
| Q45 | - |  |  | SI | Impedance (Ω) - LV |
| Q46 | - |  |  | SI | RV Defib |
| Q47 | - |  |  | SI | SVC Defib |
| Q48 | - |  |  | SI | Ω |
| Q49 | - |  |  | SI | Ω |
| Q50 | - |  |  | SI | LV pace polarity |
| Q51 | - |  |  | SI | Findings / Events |
| Q52 | - |  |  | SI | Programming changes |
| Q53 | - |  |  | SI | Sensing value	- Atrium |
| Q54 | - |  |  | SI | Pacing threshold - Atrium |
| Q55 | - |  |  | SI | Impedance - Atrium |
| Q56 | - |  |  | SI | Ω |
| Q57 | - |  |  | SI | Ω |
| Q58 | - |  |  | SI | Ω |
| Q59 | - |  |  | SI | Sensing value - Right ventricle |
| Q60 | - |  |  | SI | Pacing threshold - Right ventricle |
| Q61 | - |  |  | SI | Impedance - Right ventricle |
| Q62 | - |  |  | SI | Pacing threshold - Left ventricle |
| Q63 | - |  |  | SI | Impedance - Left ventricle |
| Q64 | - |  |  | SI | Right ventricle |
| Q65 | - |  |  | SI | Right ventricle |
| Q66 | - |  |  | SI | Left ventricle |
| Q67 | - |  |  | SI | mV |
| Q68 | - |  |  | SI | mV |
| Q69 | - |  |  | SI | LV pace polarity |
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