# SQLUser.PA_Adm2HandoverHistory

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOH_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| HOH_CareProviderType_DR | bigint |  | FK | SI | - |
| HOH_CareProvider_DR | varchar |  | FK | SI | - |
| HOH_Childsub | double |  |  | NO | Childsub |
| HOH_CreateDate | date |  |  | SI | - |
| HOH_CreateHospital_DR | bigint |  | FK | SI | - |
| HOH_CreateLoc_DR | bigint |  | FK | SI | - |
| HOH_CreateTime | time |  |  | SI | - |
| HOH_CreateUser_DR | bigint |  | FK | SI | - |
| HOH_EndDate | date |  |  | SI | - |
| HOH_EndTime | time |  |  | SI | - |
| HOH_LastUpdateDate | date |  |  | SI | - |
| HOH_LastUpdateHospital_DR | bigint |  | FK | SI | - |
| HOH_LastUpdateLoc_DR | bigint |  | FK | SI | - |
| HOH_LastUpdateTime | time |  |  | SI | - |
| HOH_LastUpdateUser_DR | bigint |  | FK | SI | - |
| HOH_RowId | varchar |  |  | NO | - |
| HOH_StartDate | date |  |  | SI | - |
| HOH_StartTime | time |  |  | SI | - |
| HOH_Type | varchar |  |  | SI | - |
| Q01 | - |  |  | SI | Need to blow nose |
| Q02 | - |  |  | SI | Nasal blockage  	 |
| Q03 | - |  |  | SI | Sneezing	 |
| Q04 | - |  |  | SI | Runny nose	 |
| Q05 | - |  |  | SI | Cough	 |
| Q06 | - |  |  | SI | Post-nasal discharge	 |
| Q07 | - |  |  | SI | Thick nasal discharge	 |
| Q08 | - |  |  | SI | Ear fullness	 |
| Q09 | - |  |  | SI | Dizziness	 |
| Q10 | - |  |  | SI | Ear pain	 |
| Q11 | - |  |  | SI | Facial pain / pressure	 |
| Q12 | - |  |  | SI | Decreased sense of smell / taste	 |
| Q13 | - |  |  | SI | Difficulty falling asleep	 |
| Q14 | - |  |  | SI | Wake up at night	 |
| Q15 | - |  |  | SI | Lack of a good night’s sleep	 |
| Q16 | - |  |  | SI | Wake up tired |
| Q17 | - |  |  | SI | Fatigue |
| Q18 | - |  |  | SI | Reduced productivity	 |
| Q19 | - |  |  | SI | Reduced concentration	 |
| Q20 | - |  |  | SI | Frustrated / restless / irritable	 |
| Q21 | - |  |  | SI | Sad |
| Q22 | - |  |  | SI | Embarrassed	 |
| Q23 | - |  |  | SI | Mark the most important items affecting your healt... |
| Q24 | - |  |  | SI | 1. Considering how severe the problem is when you ... |
| Q25 | - |  |  | SI | 2. Please mark the most important items affecting ... |
| Q26 | - |  |  | SI | Score	 |
| Q27 | - |  |  | SI | Classification	 |
| Q28 | - |  |  | SI | <8	 |
| Q29 | - |  |  | SI | 8 - 20 |
| Q30 | - |  |  | SI | 21 - 50	 |
| Q31 | - |  |  | SI | >50 |
| Q32 | - |  |  | SI | The Sino-nasal Outcome Test (Snot-22) is a tool to... |
| Q33 | - |  |  | SI | The stratification of the SNOT-22 scores into Mild... |
| Q34 | - |  |  | SI | Normal |
| Q35 | - |  |  | SI | Mild |
| Q36 | - |  |  | SI | Moderate |
| Q37 | - |  |  | SI | Severe |
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