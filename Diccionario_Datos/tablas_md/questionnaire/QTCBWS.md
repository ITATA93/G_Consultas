# questionnaire.QTCBWS

> Clinical Institute Withdrawal Assessment Scale - Benzodiazepines (CIWA-B)

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Institute Withdrawal Assessment Scale - Benzodiazepines (CIWA-B)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Not at all |
| Q02 | varchar |  |  | SI | Very much so |
| Q03 | varchar |  |  | SI | Do you feel irritable? |
| Q04 | varchar |  |  | SI | Do you feel fatigued? |
| Q05 | varchar |  |  | SI | Do you feel tense? |
| Q06 | varchar |  |  | SI | Do you have difficulty concentrating? |
| Q07 | varchar |  |  | SI | Do you have any loss of appetite? |
| Q08 | varchar |  |  | SI | Have you any numbness or burning in your face, han... |
| Q09 | varchar |  |  | SI | Do you feel your heart racing (palpitations)? |
| Q10 | varchar |  |  | SI | Does your head feel full or achy? |
| Q11 | varchar |  |  | SI | Do you feel muscle aches or stiffness? |
| Q12 | varchar |  |  | SI | Do you feel anxious, nervous or jittery? |
| Q13 | varchar |  |  | SI | Do you feel upset? |
| Q14 | varchar |  |  | SI | How restful was your sleep last night? |
| Q15 | varchar |  |  | SI | Do you feel weak? |
| Q16 | varchar |  |  | SI | Do you think you had enough sleep last night? |
| Q17 | varchar |  |  | SI | Do you have any visual disturbances?(sensitivity t... |
| Q18 | varchar |  |  | SI | Are you fearful? |
| Q19 | varchar |  |  | SI | Have you been worrying about possible misfortunes ... |
| Q20 | varchar |  |  | SI | Observe behaviour for restlessness and agitation	 |
| Q21 | varchar |  |  | SI | Ask the patient to extend arms with fingers apart,... |
| Q22 | varchar |  |  | SI | Observe for sweating - feel palms	 |
| Q23 | varchar |  |  | SI | Total score	 |
| Q25 | varchar |  |  | SI | Alert, orientated, obeys commands? If NO, complete... |
| Q26 | varchar |  |  | SI | Pupil size left |
| Q26ObsDR | varchar |  | FK | SI | Pupil size left DR |
| Q27 | varchar |  |  | SI | Pupil reaction left |
| Q27ObsDR | varchar |  | FK | SI | Pupil reaction left DR |
| Q28 | varchar |  |  | SI | Pupil size right |
| Q28ObsDR | varchar |  | FK | SI | Pupil size right DR |
| Q29 | varchar |  |  | SI | Pupil reaction right |
| Q29ObsDR | varchar |  | FK | SI | Pupil reaction right DR |
| Q30 | varchar |  |  | SI | Score |
| Q31 | varchar |  |  | SI | Classification |
| Q32 | varchar |  |  | SI | 1-20 |
| Q33 | varchar |  |  | SI | Mild withdrawal |
| Q34 | varchar |  |  | SI | 21-40 |
| Q35 | varchar |  |  | SI | Moderate withdrawal |
| Q36 | varchar |  |  | SI | 41-60 |
| Q37 | varchar |  |  | SI | Severe withdrawal |
| Q38 | varchar |  |  | SI | 61-80 |
| Q39 | varchar |  |  | SI | Very severe withdrawal |
| Q40 | varchar |  |  | SI | The Benzodiazepine Withdrawal Scale is used to ass... |
| Q41 | varchar |  |  | SI | 0 |
| Q42 | varchar |  |  | SI | No signs of withdrawal |
| Q43 | date |  |  | SI | Date |
| Q44 | time |  |  | SI | Time |
| Q45 | varchar |  |  | SI | Clinician to ask patient the following questions a... |
| Q46 | numeric |  |  | SI | How many hours of sleep do you think you had last ... |
| Q47 | numeric |  |  | SI | How many minutes do you think it took you to fall ... |
| Q48 | varchar |  |  | SI | The 'Clinical Institute Withdrawal Scale - Benzodi... |
| Q49 | varchar |  |  | SI | Hulse G, O’Neil G, Morris N, et al. Withdrawal and... |
| Q50 | varchar |  |  | SI | J Psychopharmacol&nbsp;2013;27:222–227. |
| Q51 | varchar |  |  | SI | Busto UE, Sykora K, Sellers EM. A clinical scale t... |
| Q52 | varchar |  |  | SI | Vital signs observation chart is required when com... |
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