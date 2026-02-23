# questionnaire.QTCICUNASC

> Intensive Care Nursing Assessment and Shift Checks

**Schema:** questionnaire
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intensive Care Nursing Assessment and Shift Checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bag & mask, positive end expiratory pressure (PEEP... |
| Q04 | varchar |  |  | SI | Oropharyngeal airway present and correct size avai... |
| Q05 | varchar |  |  | SI | Emergency intravascular port identified / peripher... |
| Q06 | varchar |  |  | SI | Details |
| Q07 | varchar |  |  | SI | Suction equipment present and functional |
| Q08 | varchar |  |  | SI | All equipment plugged in and powered |
| Q09 | varchar |  |  | SI | Medications: orders versus infusions checked |
| Q10 | varchar |  |  | SI | Ventilator settings and alarms checked |
| Q11 | varchar |  |  | SI | Apnoea parameters checked |
| Q12 | varchar |  |  | SI | Monitor alarm limits checked |
| Q13 | varchar |  |  | SI | Safety check notes |
| Q14 | varchar |  |  | SI | Equipment Changes |
| Q15 | varchar |  |  | SI | Closed suction system |
| Q16 | varchar |  |  | SI | Due for change every 3 days |
| Q17 | date |  |  | SI | Date due for change |
| Q18 | varchar |  |  | SI | Yankauer sucker and tubing |
| Q19 | varchar |  |  | SI | Check daily |
| Q20 | varchar |  |  | SI | Ventilator circuit / Hiflow circuit |
| Q21 | varchar |  |  | SI | Due for change every 2 weeks |
| Q22 | date |  |  | SI | Date due for change |
| Q23 | varchar |  |  | SI | Humidifier water bag |
| Q24 | varchar |  |  | SI | Change daily |
| Q25 | date |  |  | SI | Date due for change |
| Q26 | varchar |  |  | SI | Checked for any additional due equipment changes |
| Q27 | varchar |  |  | SI | Additional equipment check notes |
| Q28 | varchar |  |  | SI | General |
| Q29 | varchar |  |  | SI | Identification band (+/- red allergy band in situ) |
| Q30 | varchar |  |  | SI | Falls risk assessment completed |
| Q31 | varchar |  |  | SI | Pressure injury risk and skin assessment completed |
| Q32 | varchar |  |  | SI | Wound charts reviewed |
| Q33 | varchar |  |  | SI | Invasive devices summary reviewed and updated |
| Q34 | varchar |  |  | SI | Cognition and delirium assessment completed |
| Q35 | varchar |  |  | SI | Compression stockings and calf compressors in situ... |
| Q36 | varchar |  |  | SI | Oral assessment and regular oral care attended |
| Q37 | varchar |  |  | SI | Electrocardiograph (ECG) dots |
| Q38 | varchar |  |  | SI | Due for change: daily |
| Q39 | varchar |  |  | SI | General notes |
| Q40 | varchar |  |  | SI | Cardiovascular |
| Q41 | varchar |  |  | SI | Daily 12 lead ECG (before rounds, if on inotropes) |
| Q42 | varchar |  |  | SI | Cardiovascular notes |
| Q43 | varchar |  |  | SI | Respiratory |
| Q44 | varchar |  |  | SI | Air entry |
| Q44ObsDR | varchar |  | FK | SI | Air entry DR |
| Q45 | varchar |  |  | SI | Work of breathing |
| Q45ObsDR | varchar |  | FK | SI | Work of breathing DR |
| Q46 | varchar |  |  | SI | Breath sounds (Left) |
| Q46ObsDR | varchar |  | FK | SI | Breath sounds (Left) DR |
| Q47 | varchar |  |  | SI | Breath sounds (Right) |
| Q47ObsDR | varchar |  | FK | SI | Breath sounds (Right) DR |
| Q48 | varchar |  |  | SI | Breath sounds |
| Q49 | varchar |  |  | SI | Respiratory notes |
| Q50 | varchar |  |  | SI | Gastrointestinal |
| Q51 | varchar |  |  | SI | Nasogastric / Orogastric tube position checked |
| Q52 | varchar |  |  | SI | Bowel sounds |
| Q52ObsDR | varchar |  | FK | SI | Bowel sounds DR |
| Q53 | varchar |  |  | SI | Bowels last opened (start protocol if bowels not o... |
| Q54 | varchar |  |  | SI | Enteral feeding line and container (change every 2... |
| Q55 | varchar |  |  | SI | Sterile water for oral medications (date and label... |
| Q56 | varchar |  |  | SI | Gastrointestinal notes |
| Q57 | varchar |  |  | SI | Renal |
| Q58 | varchar |  |  | SI | Catheter care attended and documented |
| Q59 | varchar |  |  | SI | Catheter securement device in situ |
| Q60 | varchar |  |  | SI | Daily weight performed |
| Q61 | varchar |  |  | SI | Urine bag labelled and dated |
| Q62 | varchar |  |  | SI | Due for change every 7 days |
| Q63 | date |  |  | SI | Date change is due |
| Q64 | varchar |  |  | SI | Waste drain flushed with water |
| Q65 | varchar |  |  | SI | If on continuous renal replacement therapy (CCRT) |
| Q66 | varchar |  |  | SI | Renal notes |
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