# questionnaire.QTCPFC

> Post Falls Checklist

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Post Falls Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | To be completed following every patient fall |
| Q10 | varchar |  |  | SI | Complete AVPU Conscious Level |
| Q11 | varchar |  |  | SI | Assess if the patient is complaining of new pain o... |
| Q12 | varchar |  |  | SI | Assess if there is any new loss of movement in the... |
| Q13 | varchar |  |  | SI | Is there any obvious deformity or internal / exter... |
| Q14 | varchar |  |  | SI | If patient complains of pain, please detail. |
| Q15 | varchar |  |  | SI | Assess for fractures, spinal injuries or significa... |
| Q16 | varchar |  |  | SI | Assess for head injury. Mark on body map |
| Q17 | varchar |  |  | SI | Body map hyperlink |
| Q18 | varchar |  |  | SI | Full neurological examination and consider risk of... |
| Q19 | varchar |  |  | SI | If any of the above are suspected, leave the patie... |
| Q2 | date |  |  | SI | Date of fall |
| Q20 | varchar |  |  | SI | Was the patient dizzy before the fall? |
| Q21 | varchar |  |  | SI | Record observations to include pulse, lying and st... |
| Q22 | varchar |  |  | SI | Record neurological observations, especially if fa... |
| Q23 | varchar |  |  | SI | Neurological observations half hourly until Glasgo... |
| Q24 | varchar |  |  | SI | Then, |
| Q25 | varchar |  |  | SI | Half hourly for 2 hours, one hourly for 4 hours, 2... |
| Q26 | varchar |  |  | SI | Should the patient with Glasgow Coma Scale equal t... |
| Q27 | varchar |  |  | SI | Did the patient have chest pains or palpitations i... |
| Q28 | varchar |  |  | SI | Did the patient have new limb weakness or difficul... |
| Q29 | varchar |  |  | SI | If yes, to any of the above please detail. |
| Q3 | time |  |  | SI | Time of fall |
| Q30 | varchar |  |  | SI | Patient's bed placed against wall (if indicated)? |
| Q31 | varchar |  |  | SI | A falls risk care plan is in place and updated |
| Q32 | varchar |  |  | SI | Bed rails and entrapment risk assessment is in pla... |
| Q33 | varchar |  |  | SI | Patient's consultant has been informed |
| Q34 | varchar |  |  | SI | Datix has been completed |
| Q35 | varchar |  |  | SI | The fall has been documented |
| Q36 | varchar |  |  | SI | The patient's next of kin has been informed of fal... |
| Q37 | varchar |  |  | SI | Patient experience |
| Q38 | varchar |  |  | SI | Ask the patient who has fallen the following quest... |
| Q39 | varchar |  |  | SI | Did you have your call bell to hand? |
| Q4 | varchar |  |  | SI | Was the doctor called? |
| Q40 | varchar |  |  | SI | If no, why not? |
| Q41 | varchar |  |  | SI | Did you press your call bell for assistance? |
| Q42 | varchar |  |  | SI | If no. why not? |
| Q43 | varchar |  |  | SI | How did you feel before the fall? |
| Q44 | varchar |  |  | SI | Additional comments |
| Q45 | varchar |  |  | SI | What do you think caused you to fall? |
| Q46 | varchar |  |  | SI | What do you think could have helped prevent the fa... |
| Q47 | varchar |  |  | SI | What do you think the ward / department could cons... |
| Q48 | date |  |  | SI | Date |
| Q49 | time |  |  | SI | Time |
| Q5 | varchar |  |  | SI | Name of doctor |
| Q6 | varchar |  |  | SI | Was the fall witnessed? |
| Q7 | varchar |  |  | SI | Name and designation of witness(s) |
| Q8 | varchar |  |  | SI | Complete quick visual check |
| Q9 | varchar |  |  | SI | Assess for airway, breathing, circulation, disabil... |
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