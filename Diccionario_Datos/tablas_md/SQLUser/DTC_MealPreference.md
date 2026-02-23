# SQLUser.DTC_MealPreference

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEALP_RowId | bigint | PK |  | NO | - |
| MEALP_Code | varchar |  |  | NO | Code |
| MEALP_CreatedDate | date |  |  | SI | Created Date |
| MEALP_CreatedTime | time |  |  | SI | Created Time |
| MEALP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEALP_Desc | varchar |  |  | NO | Description |
| MEALP_UpdatedDate | date |  |  | SI | Updated Date |
| MEALP_UpdatedTime | time |  |  | SI | Updated Time |
| MEALP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Device |
| Q02 | - |  |  | SI | Clinic date	 |
| Q03 | - |  |  | SI | Date implant inserted	 |
| Q04 | - |  |  | SI | Device manufacturer |
| Q05 | - |  |  | SI | Device manufacturer |
| Q06 | - |  |  | SI | Medtronic (Pacemaker) |
| Q07 | - |  |  | SI | Medtronic (ILR)	 |
| Q08 | - |  |  | SI | ELA Sorin	 |
| Q09 | - |  |  | SI | Boston Scientific	 |
| Q10 | - |  |  | SI | St Jude Medical	 |
| Q11 | - |  |  | SI | Biotronic	 |
| Q12 | - |  |  | SI | Vitatron |
| Q13 | - |  |  | SI | Model or type (Pacemaker)	 |
| Q14 | - |  |  | SI | Model or type (ILR)	 |
| Q15 | - |  |  | SI | Mode (Single)	 |
| Q16 | - |  |  | SI | Mode (Dual)	 |
| Q17 | - |  |  | SI | Base rate	 |
| Q18 | - |  |  | SI | Magnet rate	 |
| Q19 | - |  |  | SI | Threshold A =	 |
| Q20 | - |  |  | SI | A=XV@ 	 |
| Q21 | - |  |  | SI | Threshold V =	 |
| Q22 | - |  |  | SI | V=XV@	 |
| Q23 | - |  |  | SI | Sensing P =	 |
| Q24 | - |  |  | SI | R=	 |
| Q25 | - |  |  | SI | Impedance A =	 |
| Q26 | - |  |  | SI | V=	 |
| Q27 | - |  |  | SI | Notes |
| Q28 | - |  |  | SI | ( please include wound appearance, high rates, any... |
| Q29 | - |  |  | SI | (30-180 bpm) |
| Q30 | - |  |  | SI | (70-110 bpm) |
| Q31 | - |  |  | SI | (0-20 V) |
| Q32 | - |  |  | SI | (0-5 MS) |
| Q33 | - |  |  | SI | (0-20 V)	 |
| Q34 | - |  |  | SI | (0-5 MS) |
| Q35 | - |  |  | SI | (0-20 mV) |
| Q36 | - |  |  | SI | (0-60 mV) |
| Q37 | - |  |  | SI | (0-3500 ohms) |
| Q38 | - |  |  | SI | (0-3500 ohms) |
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