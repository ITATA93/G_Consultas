# questionnaire.QTCTP

> Adult Target Parameters

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Adult Target Parameters

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Values from the previous entry will display by def... |
| Q02 | varchar |  |  | SI | Mean arterial pressure (mmHg) |
| Q03 | varchar |  |  | SI | Systolic blood pressure (mmHg) |
| Q04 | varchar |  |  | SI | Fluid balance&nbsp;(mL per 24 hours) |
| Q05 | varchar |  |  | SI | Urine output (mL/h) |
| Q06 | varchar |  |  | SI | Oxygen saturation (%) |
| Q07 | varchar |  |  | SI | Partial pressure of oxygen |
| Q08 | varchar |  |  | SI | Partial pressure of carbon dioxide |
| Q09 | varchar |  |  | SI | Blood glucose concentration |
| Q10 | varchar |  |  | SI | Core temperature (°C) |
| Q11 | varchar |  |  | SI | Head of bed position (degrees elevated) |
| Q12 | varchar |  |  | SI | Sedation level |
| Q13 | varchar |  |  | SI | External ventricular drain (height above tragus in... |
| Q14 | varchar |  |  | SI | Comments |
| Q15 | varchar |  |  | SI | Last reviewed by |
| Q16 | date |  |  | SI | Review date / time |
| Q17 | time |  |  | SI | Review time |
| Q18 | date |  |  | SI | Next review due |
| Q19 | time |  |  | SI | Next review time |
| Q20 | varchar |  |  | SI | In various settings a patient is reviewed by a cli... |
| Q21 | varchar |  |  | SI | Nurses are then asked to monitor a variety of obse... |
| Q22 | varchar |  |  | SI |  In these circumstances the clinicians may initiat... |
| Q23 | varchar |  |  | SI | This form is used to document those treatment aims |
| Q24 | varchar |  |  | SI | Heart rate (per min) |
| Q25 | varchar |  |  | SI | Cardiac index (CI) |
| Q26 | varchar |  |  | SI | Venous oxygen saturation (%) |
| Q27 | varchar |  |  | SI | Central venous pressure (mmHg) |
| Q28 | varchar |  |  | SI | Haemoglobin (g/L) |
| Q29 | varchar |  |  | SI | Haematocrit (%) |
| Q30 | varchar |  |  | SI | Blood potassium concentration (mmol/L) |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
| Q33 | varchar |  |  | SI | Feeding |
| Q34 | varchar |  |  | SI | Height (cm) |
| Q34ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q35 | varchar |  |  | SI | Ideal body weight (IBW) - Male (kg) |
| Q36 | varchar |  |  | SI | Ideal body weight (IBW) - Female (kg) |
| Q37 | varchar |  |  | SI | Tidal volume (mL) |
| Q38 | varchar |  |  | SI | Based on mL/kg of IBW |
| Q39 | varchar |  |  | SI | Intracranial pressure (mmHg) |
| Q40 | varchar |  |  | SI | Cerebral perfusion pressure (mmHg) |
| Q41 | varchar |  |  | SI | Parameter 1 |
| Q42 | varchar |  |  | SI | Parameter 2 |
| Q43 | varchar |  |  | SI | Parameter 3 |
| Q44 | varchar |  |  | SI | Parameter 4 |
| Q45 | varchar |  |  | SI | Parameter 5 |
| Q46 | varchar |  |  | SI | Richmond Agitation-Sedation Scale (RASS) |
| Q47 | varchar |  |  | SI | +4: Combative - Combative, violent, immediate dang... |
| Q48 | varchar |  |  | SI | +3: Very Agitated - Pulls to remove tubes or cathe... |
| Q49 | varchar |  |  | SI | +2: Agitated - Frequent non-purposeful movement; f... |
| Q50 | varchar |  |  | SI | +1: Restless - Anxious, apprehensive, movements no... |
| Q51 | varchar |  |  | SI | 0: Alert & Calm - Spontaneously pays attention to ... |
| Q52 | varchar |  |  | SI | -1: Drowsy - Not fully alert, but has sustained aw... |
| Q53 | varchar |  |  | SI | -2: Light Sedation - Briefly awakens to voice (eye... |
| Q54 | varchar |  |  | SI | -3: Moderate Sedation - Movement of eye opening to... |
| Q55 | varchar |  |  | SI | -4: Deep Sedation - No response to voice, but move... |
| Q56 | varchar |  |  | SI | -5: Unrousable - No response to voice or physical ... |
| Q57 | varchar |  |  | SI | Ideal body weight (IBW) - Male (kg) |
| Q58 | varchar |  |  | SI | Ideal body weight (IBW) - Female (kg) |
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