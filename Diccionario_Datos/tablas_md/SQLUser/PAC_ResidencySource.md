# SQLUser.PAC_ResidencySource

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RSDSRC_RowId | bigint | PK |  | NO | - |
| Q1 | - |  |  | SI | To be completed following every patient fall |
| Q10 | - |  |  | SI | Complete AVPU Conscious Level |
| Q11 | - |  |  | SI | Assess if the patient is complaining of new pain o... |
| Q12 | - |  |  | SI | Assess if there is any new loss of movement in the... |
| Q13 | - |  |  | SI | Is there any obvious deformity or internal / exter... |
| Q14 | - |  |  | SI | If patient complains of pain, please detail. |
| Q15 | - |  |  | SI | Assess for fractures, spinal injuries or significa... |
| Q16 | - |  |  | SI | Assess for head injury. Mark on body map |
| Q17 | - |  |  | SI | Body map hyperlink |
| Q18 | - |  |  | SI | Full neurological examination and consider risk of... |
| Q19 | - |  |  | SI | If any of the above are suspected, leave the patie... |
| Q2 | - |  |  | SI | Date of fall |
| Q20 | - |  |  | SI | Was the patient dizzy before the fall? |
| Q21 | - |  |  | SI | Record observations to include pulse, lying and st... |
| Q22 | - |  |  | SI | Record neurological observations, especially if fa... |
| Q23 | - |  |  | SI | Neurological observations half hourly until Glasgo... |
| Q24 | - |  |  | SI | Then, |
| Q25 | - |  |  | SI | Half hourly for 2 hours, one hourly for 4 hours, 2... |
| Q26 | - |  |  | SI | Should the patient with Glasgow Coma Scale equal t... |
| Q27 | - |  |  | SI | Did the patient have chest pains or palpitations i... |
| Q28 | - |  |  | SI | Did the patient have new limb weakness or difficul... |
| Q29 | - |  |  | SI | If yes, to any of the above please detail. |
| Q3 | - |  |  | SI | Time of fall |
| Q30 | - |  |  | SI | Patient's bed placed against wall (if indicated)? |
| Q31 | - |  |  | SI | A falls risk care plan is in place and updated |
| Q32 | - |  |  | SI | Bed rails and entrapment risk assessment is in pla... |
| Q33 | - |  |  | SI | Patient's consultant has been informed |
| Q34 | - |  |  | SI | Datix has been completed |
| Q35 | - |  |  | SI | The fall has been documented |
| Q36 | - |  |  | SI | The patient's next of kin has been informed of fal... |
| Q37 | - |  |  | SI | Patient experience |
| Q38 | - |  |  | SI | Ask the patient who has fallen the following quest... |
| Q39 | - |  |  | SI | Did you have your call bell to hand? |
| Q4 | - |  |  | SI | Was the doctor called? |
| Q40 | - |  |  | SI | If no, why not? |
| Q41 | - |  |  | SI | Did you press your call bell for assistance? |
| Q42 | - |  |  | SI | If no. why not? |
| Q43 | - |  |  | SI | How did you feel before the fall? |
| Q44 | - |  |  | SI | Additional comments |
| Q45 | - |  |  | SI | What do you think caused you to fall? |
| Q46 | - |  |  | SI | What do you think could have helped prevent the fa... |
| Q47 | - |  |  | SI | What do you think the ward / department could cons... |
| Q48 | - |  |  | SI | Date |
| Q49 | - |  |  | SI | Time |
| Q5 | - |  |  | SI | Name of doctor |
| Q6 | - |  |  | SI | Was the fall witnessed? |
| Q7 | - |  |  | SI | Name and designation of witness(s) |
| Q8 | - |  |  | SI | Complete quick visual check |
| Q9 | - |  |  | SI | Assess for airway, breathing, circulation, disabil... |
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
| RSDSRC_Code | varchar |  |  | NO | Code |
| RSDSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RSDSRC_CreatedDate | date |  |  | SI | Created Date |
| RSDSRC_CreatedTime | time |  |  | SI | Created Time |
| RSDSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RSDSRC_DateFrom | date |  |  | SI | DateFrom |
| RSDSRC_DateTo | date |  |  | SI | DateTo |
| RSDSRC_Desc | varchar |  |  | NO | Description |
| RSDSRC_Owner | varchar |  |  | SI | Owner |
| RSDSRC_UpdatedDate | date |  |  | SI | Updated Date |
| RSDSRC_UpdatedTime | time |  |  | SI | Updated Time |
| RSDSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*