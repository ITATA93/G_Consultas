# SQLUser.CT_HealthSpecialtyCodes

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HSC_RowId | bigint | PK |  | NO | - |
| HSC_Code | varchar |  |  | NO | Code |
| HSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HSC_CreatedDate | date |  |  | SI | Created Date |
| HSC_CreatedTime | time |  |  | SI | Created Time |
| HSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HSC_DateFrom | date |  |  | SI | Date From |
| HSC_DateTo | date |  |  | SI | Date To |
| HSC_Desc | varchar |  |  | NO | Description |
| HSC_Owner | varchar |  |  | SI | Owner |
| HSC_UpdatedDate | date |  |  | SI | Updated Date |
| HSC_UpdatedTime | time |  |  | SI | Updated Time |
| HSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Values from the previous entry will display by def... |
| Q02 | - |  |  | SI | Mean arterial pressure (mmHg) |
| Q03 | - |  |  | SI | Systolic blood pressure (mmHg) |
| Q04 | - |  |  | SI | Fluid balance&nbsp |
| Q05 | - |  |  | SI | Urine output (mL/h) |
| Q06 | - |  |  | SI | Oxygen saturation (%) |
| Q07 | - |  |  | SI | Partial pressure of oxygen |
| Q08 | - |  |  | SI | Partial pressure of carbon dioxide |
| Q09 | - |  |  | SI | Blood glucose concentration |
| Q10 | - |  |  | SI | Core temperature (°C) |
| Q11 | - |  |  | SI | Head of bed position (degrees elevated) |
| Q12 | - |  |  | SI | Sedation level |
| Q13 | - |  |  | SI | External ventricular drain (height above tragus in... |
| Q14 | - |  |  | SI | Comments |
| Q15 | - |  |  | SI | Last reviewed by |
| Q16 | - |  |  | SI | Review date / time |
| Q17 | - |  |  | SI | Review time |
| Q18 | - |  |  | SI | Next review due |
| Q19 | - |  |  | SI | Next review time |
| Q20 | - |  |  | SI | In various settings a patient is reviewed by a cli... |
| Q21 | - |  |  | SI | Nurses are then asked to monitor a variety of obse... |
| Q22 | - |  |  | SI | In these circumstances the clinicians may initiate... |
| Q23 | - |  |  | SI | This form is used to document those treatment aims |
| Q24 | - |  |  | SI | Heart rate (per min) |
| Q25 | - |  |  | SI | Cardiac index (CI) |
| Q26 | - |  |  | SI | Venous oxygen saturation (%) |
| Q27 | - |  |  | SI | Central venous pressure (mmHg) |
| Q28 | - |  |  | SI | Haemoglobin (g/L) |
| Q29 | - |  |  | SI | Haematocrit (%) |
| Q30 | - |  |  | SI | Blood potassium concentration (mmol/L) |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
| Q33 | - |  |  | SI | Feeding |
| Q34 | - |  |  | SI | Height (cm) |
| Q34ObsDR | - |  |  | SI | Height (cm) DR |
| Q35 | - |  |  | SI | Ideal body weight (IBW) - Male (kg) |
| Q36 | - |  |  | SI | Ideal body weight (IBW) - Female (kg) |
| Q37 | - |  |  | SI | Tidal volume (mL) |
| Q38 | - |  |  | SI | Based on mL/kg of IBW |
| Q39 | - |  |  | SI | Intracranial pressure (mmHg) |
| Q40 | - |  |  | SI | Cerebral perfusion pressure (mmHg) |
| Q41 | - |  |  | SI | Parameter 1 |
| Q42 | - |  |  | SI | Parameter 2 |
| Q43 | - |  |  | SI | Parameter 3 |
| Q44 | - |  |  | SI | Parameter 4 |
| Q45 | - |  |  | SI | Parameter 5 |
| Q46 | - |  |  | SI | Richmond Agitation-Sedation Scale (RASS) |
| Q47 | - |  |  | SI | +4: Combative - Combative, violent, immediate dang... |
| Q48 | - |  |  | SI | +3: Very Agitated - Pulls to remove tubes or cathe... |
| Q49 | - |  |  | SI | +2: Agitated - Frequent non-purposeful movement |
| Q50 | - |  |  | SI | +1: Restless - Anxious, apprehensive, movements no... |
| Q51 | - |  |  | SI | 0: Alert & Calm - Spontaneously pays attention to ... |
| Q52 | - |  |  | SI | -1: Drowsy - Not fully alert, but has sustained aw... |
| Q53 | - |  |  | SI | -2: Light Sedation - Briefly awakens to voice (eye... |
| Q54 | - |  |  | SI | -3: Moderate Sedation - Movement of eye opening to... |
| Q55 | - |  |  | SI | -4: Deep Sedation - No response to voice, but move... |
| Q56 | - |  |  | SI | -5: Unrousable - No response to voice or physical ... |
| Q57 | - |  |  | SI | Ideal body weight (IBW) - Male (kg) |
| Q58 | - |  |  | SI | Ideal body weight (IBW) - Female (kg) |
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