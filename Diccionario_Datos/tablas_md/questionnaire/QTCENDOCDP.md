# questionnaire.QTCENDOCDP

> Endoscopy Care During Procedure

**Schema:** questionnaire
**Columnas:** 132
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Care During Procedure

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient preparation |
| Q04 | varchar |  |  | SI | If a general anaesthetic patient please record the... |
| Q05 | varchar |  |  | SI | Bodymap |
| Q06 | varchar |  |  | SI | Record temperature on arrival into procedure area ... |
| Q07 | varchar |  |  | SI | Specify type and serial no. (if applicable) |
| Q08 | varchar |  |  | SI | Intravenous cannula insertion (if applicable) |
| Q09 | varchar |  |  | SI | Type |
| Q10 | varchar |  |  | SI | Gauge |
| Q11 | varchar |  |  | SI | Location |
| Q12 | numeric |  |  | SI | Number of attempts |
| Q13 | varchar |  |  | SI | Sedation given as prescribed |
| Q14 | varchar |  |  | SI | Intravenous fluids administered as prescribed |
| Q15 | varchar |  |  | SI | Vital signs monitored and within normal limits pri... |
| Q16 | varchar |  |  | SI | Eye protection i.e. Goggles / Visor mask provided |
| Q17 | varchar |  |  | SI | Can the patient complete all movement independentl... |
| Q18 | varchar |  |  | SI | If no, please complete manual handling assessment |
| Q18a | varchar |  |  | SI | If no, please complete manual handling assessment |
| Q19 | varchar |  |  | SI | Patient positioned safely for procedure |
| Q20 | varchar |  |  | SI | Are the patient's pressure areas intact where visi... |
| Q21 | varchar |  |  | SI | If no, please detail |
| Q22 | varchar |  |  | SI | Pressure relieving devices used |
| Q23 | varchar |  |  | SI | If pressure relieving devices in situ, please spec... |
| Q24 | varchar |  |  | SI | Patient warming device used |
| Q25 | varchar |  |  | SI | Temperature is monitored throughout the procedure ... |
| Q26 | varchar |  |  | SI | Patient is suitable for entonox to be used |
| Q27 | time |  |  | SI | Throat spray given at? |
| Q28 | varchar |  |  | SI | Helicobacter pylori test performed |
| Q29 | numeric |  |  | SI | Number of biopsies taken |
| Q30 | varchar |  |  | SI | Balloon dilatation performed |
| Q31 | varchar |  |  | SI | Stent inserted |
| Q32 | varchar |  |  | SI | Please specify any therapeutic interventions (if a... |
| Q33 | time |  |  | SI | Throat spray given at? |
| Q34 | varchar |  |  | SI | Therapeutic procedures undertaken |
| Q34a | varchar |  |  | SI | Therapeutic procedures undertaken |
| Q35 | varchar |  |  | SI | Stent type if applicable |
| Q36 | varchar |  |  | SI | Additional information: |
| Q37 | varchar |  |  | SI | Biopsies taken |
| Q38 | varchar |  |  | SI | Additional information: |
| Q39 | time |  |  | SI | Throat spray given at? |
| Q40 | varchar |  |  | SI | Local anaesthetic used |
| Q41 | varchar |  |  | SI | Intubation route |
| Q42 | varchar |  |  | SI | Histology taken, specify: |
| Q43 | varchar |  |  | SI | Additional information: |
| Q44 | varchar |  |  | SI | Skin preparation |
| Q45 | varchar |  |  | SI | Skin closure type |
| Q46 | varchar |  |  | SI | Dressing type |
| Q47 | varchar |  |  | SI | Prophylactic antibiotics given |
| Q48 | varchar |  |  | SI | Additional information: |
| Q49 | varchar |  |  | SI | Diathermy plate removed and site shows no adverse ... |
| Q50 | varchar |  |  | SI | Please detail if any adverse reactions noted |
| Q51 | varchar |  |  | SI | Specimens labelled, checked and sent to laboratory |
| Q52 | varchar |  |  | SI | Post procedure, patient pressure areas are intact ... |
| Q53 | varchar |  |  | SI | Please detail if any issues noted |
| Q54 | varchar |  |  | SI | Sedation score |
| Q55 | varchar |  |  | SI | Modified Gloucester comfort score |
| Q56 | varchar |  |  | SI | Discharged back to ward - Bypass recovery |
| Q57 | varchar |  |  | SI | Type of anaesthetic |
| Q57a | varchar |  |  | SI | Type of anaesthetic |
| Q58 | varchar |  |  | SI | If intravenous sedation - please state drug and do... |
| Q59 | varchar |  |  | SI | Throat spray used |
| Q60 | time |  |  | SI | If yes state nil by mouth until time |
| Q61 | varchar |  |  | SI | Oxygen administered as prescribed via |
| Q62 | varchar |  |  | SI | Flow rate (litres per minute) |
| Q63 | varchar |  |  | SI | Patients colour / perfusion assessed and acceptabl... |
| Q64 | varchar |  |  | SI | Vital signs monitored, recorded and evaluated on a... |
| Q65 | varchar |  |  | SI | Patients temperature is above 36 degrees (state te... |
| Q66 | varchar |  |  | SI | Warming device used if temperature below 36 degree... |
| Q67 | varchar |  |  | SI | PEG site assessed, dressing intact and dry (if app... |
| Q68 | varchar |  |  | SI | Pain managed and level acceptable to patient (comf... |
| Q69 | varchar |  |  | SI | Additional comments: |
| Q70 | varchar |  |  | SI | Was the quality of the bowel preparation satisfact... |
| Q71 | numeric |  |  | SI | Number of specimens taken |
| Q72 | varchar |  |  | SI | Colonoscopy completion to caecum / terminal ileum |
| Q73 | varchar |  |  | SI | If abandoned please give reason |
| Q74 | numeric |  |  | SI | Number of polyps removed |
| Q75 | numeric |  |  | SI | Number of polyps retrieved |
| Q76 | varchar |  |  | SI | Anaesthetic Care |
| Q77 | varchar |  |  | SI | Upper Gastrointestinal Endoscopy |
| Q78 | varchar |  |  | SI | Lower Gastrointestinal Endoscopy |
| Q79 | varchar |  |  | SI | Endoscopic Retrograde Cholangiopancreatography Pro... |
| Q80 | varchar |  |  | SI | Endoscopic Ultrasound (Ultrasound) |
| Q81 | varchar |  |  | SI | Bronchoscopy |
| Q82 | varchar |  |  | SI | Percutaneous Endoscopic Gastrostomy Procedures Onl... |
| Q83 | varchar |  |  | SI | Post Procedure |
| Q84 | varchar |  |  | SI | Endoscopy To Recovery / Ward Handover |
| Q85 | varchar |  |  | SI | Please specify any therapeutic interventions (if a... |
| Q89 | varchar |  |  | SI | Care provider 1 |
| Q90 | varchar |  |  | SI | Care provider 2 |
| Q91 | varchar |  |  | SI | Care provider 3 |
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