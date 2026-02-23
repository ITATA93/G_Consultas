# questionnaire.QTCITCPC

> Interhospital Transport of Critically Ill Patient Checklist

**Schema:** questionnaire
**Columnas:** 140
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Interhospital Transport of Critically Ill Patient Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of transport |
| Q04 | time |  |  | SI | Time of transport |
| Q05 | varchar |  |  | SI | Destination |
| Q06 | varchar |  |  | SI | Other destination |
| Q07 | varchar |  |  | SI | Patient secured for transport |
| Q08 | varchar |  |  | SI | Doctor |
| Q09 | varchar |  |  | SI | Nurse |
| Q10 | varchar |  |  | SI | Other |
| Q11 | varchar |  |  | SI | Escort notes |
| Q12 | varchar |  |  | SI | Electrocardiogram (ECG) |
| Q13 | varchar |  |  | SI | End-Tidal C02 (ETC02) |
| Q14 | varchar |  |  | SI | Arterial blood pressure |
| Q15 | varchar |  |  | SI | Oxygen saturation (SpO2) |
| Q16 | varchar |  |  | SI | Non-invasive blood pressure |
| Q17 | varchar |  |  | SI | Intracranial pressure / Cerebral perfusion pressur... |
| Q18 | varchar |  |  | SI | Monitoring notes |
| Q19 | varchar |  |  | SI | Model |
| Q19ObsDR | varchar |  | FK | SI | Model DR |
| Q20 | varchar |  |  | SI | Mode |
| Q20ObsDR | varchar |  | FK | SI | Mode DR |
| Q21 | varchar |  |  | SI | Set Insp Pressure (cmH2O) |
| Q21ObsDR | varchar |  | FK | SI | Set Insp Pressure (cmH2O) DR |
| Q22 | varchar |  |  | SI | Set positive end expiratory pressure (cmH2O) |
| Q22ObsDR | varchar |  | FK | SI | Set positive end expiratory pressure (cmH2O) DR |
| Q23 | varchar |  |  | SI | Set fraction of inspired oxygen (%) |
| Q23ObsDR | varchar |  | FK | SI | Set fraction of inspired oxygen (%) DR |
| Q24 | varchar |  |  | SI | Set tidal volume  (mls) |
| Q24ObsDR | varchar |  | FK | SI | Set tidal volume  (mls) DR |
| Q25 | varchar |  |  | SI | Set minute volume (L/min) |
| Q25ObsDR | varchar |  | FK | SI | Set minute volume (L/min) DR |
| Q26 | varchar |  |  | SI | Transport ventilatory notes |
| Q27 | varchar |  |  | SI | Airway device |
| Q28 | varchar |  |  | SI | Endotracheal tube (ETT) size (mm) |
| Q28ObsDR | varchar |  | FK | SI | Endotracheal tube (ETT) size (mm) DR |
| Q29 | varchar |  |  | SI | ETT length at lip (cm) |
| Q29ObsDR | varchar |  | FK | SI | ETT length at lip (cm) DR |
| Q30 | varchar |  |  | SI | ETT length (cm) |
| Q30ObsDR | varchar |  | FK | SI | ETT length (cm) DR |
| Q31 | varchar |  |  | SI | ETT measured at |
| Q31ObsDR | varchar |  | FK | SI | ETT measured at DR |
| Q32 | varchar |  |  | SI | ETT cuff pressure (cmH20) |
| Q32ObsDR | varchar |  | FK | SI | ETT cuff pressure (cmH20) DR |
| Q33 | varchar |  |  | SI | Tracheostomy type |
| Q33ObsDR | varchar |  | FK | SI | Tracheostomy type DR |
| Q34 | varchar |  |  | SI | Tracheostomy tube size (mm) |
| Q34ObsDR | varchar |  | FK | SI | Tracheostomy tube size (mm) DR |
| Q35 | varchar |  |  | SI | Tracheostomy cuff pressure (cmH20) |
| Q35ObsDR | varchar |  | FK | SI | Tracheostomy cuff pressure (cmH20) DR |
| Q36 | varchar |  |  | SI | Airway and associated airway device(s) secure |
| Q37 | varchar |  |  | SI | Airway notes |
| Q38 | varchar |  |  | SI | Sedated or paralysed |
| Q39 | varchar |  |  | SI | Established on transport ventilator |
| Q40 | varchar |  |  | SI | Recent Arterial Blood Gas (ABG) |
| Q41 | varchar |  |  | SI | Intercostal Catheter (ICC) on suction |
| Q42 | varchar |  |  | SI | Breathing notes |
| Q43 | varchar |  |  | SI | Cardiovascular system stable |
| Q44 | varchar |  |  | SI | Haemoglobin > 70 (g/dl) |
| Q45 | varchar |  |  | SI | Sufficient vasopressor infusions |
| Q46 | varchar |  |  | SI | Intravascular access (IV) including emergency port |
| Q47 | varchar |  |  | SI | All IV lines visible and secure |
| Q48 | varchar |  |  | SI | Peripheral IV access (for contrast CT) |
| Q49 | varchar |  |  | SI | Circulation notes |
| Q50 | varchar |  |  | SI | Recent neuro observations documented and safe for ... |
| Q51 | varchar |  |  | SI | Pupillary size and response assessed |
| Q52 | varchar |  |  | SI | Blood Sugar Level (BSL) over 4 mmol/L |
| Q53 | varchar |  |  | SI | Cervical spine protected and documented |
| Q54 | varchar |  |  | SI | Disability notes |
| Q55 | varchar |  |  | SI | Temperature |
| Q55ObsDR | varchar |  | FK | SI | Temperature DR |
| Q56 | varchar |  |  | SI | Patient stable and dignified |
| Q57 | varchar |  |  | SI | Drains functioning and secure |
| Q58 | varchar |  |  | SI | Exposure notes |
| Q59 | varchar |  |  | SI | Destination department aware patient is in transit |
| Q60 | varchar |  |  | SI | Relatives informed |
| Q61 | varchar |  |  | SI | Consultant and team leader aware of transfer |
| Q62 | varchar |  |  | SI | Destination department aware if additional precaut... |
| Q63 | varchar |  |  | SI | Examples: Methicillin Resistant Staphylococcus Aur... |
| Q64 | varchar |  |  | SI | Organisation notes |
| Q65 | varchar |  |  | SI | Resuscitation pack |
| Q66 | varchar |  |  | SI | Portable suction and tubing in working order |
| Q67 | varchar |  |  | SI | Patient slide sheet. To remain under patient on im... |
| Q68 | varchar |  |  | SI | Automated External Defibrillator (AED) |
| Q69 | varchar |  |  | SI | Paralysis medication |
| Q70 | varchar |  |  | SI | Extra sedation / Pain relief |
| Q71 | varchar |  |  | SI | Metaraminol |
| Q72 | varchar |  |  | SI | Bag valve mask resuscitator |
| Q73 | varchar |  |  | SI | Sufficient oxygen supplies |
| Q74 | varchar |  |  | SI | Inner cannula, spare tracheostomy tube and trachea... |
| Q75 | varchar |  |  | SI | Intra Aortic Balloon Pump (IABP) |
| Q76 | varchar |  |  | SI | Equipment notes |
| Q77 | varchar |  |  | SI | Additional intravascular line length as per protoc... |
| Q78 | varchar |  |  | SI | Silver dressings removed |
| Q79 | varchar |  |  | SI | Intracranial pressure monitor cable / sensor coile... |
| Q80 | varchar |  |  | SI | Foley temperature catheter removed |
| Q81 | varchar |  |  | SI | MRI patient checklist completed |
| Q82 | varchar |  |  | SI | MRI transport notes |
| Q83 | varchar |  |  | SI | As per minimum standard for inter-hospital transpo... |
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