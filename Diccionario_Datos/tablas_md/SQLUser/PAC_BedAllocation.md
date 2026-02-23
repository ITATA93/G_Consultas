# SQLUser.PAC_BedAllocation

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BALL_RowId | bigint | PK |  | NO | - |
| BALL_Beds | double |  |  | NO | Number of Beds |
| BALL_CTLOC_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| BALL_CreatedDate | date |  |  | SI | Created Date |
| BALL_CreatedTime | time |  |  | SI | Created Time |
| BALL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BALL_Date | date |  |  | NO | Date |
| BALL_UpdatedDate | date |  |  | SI | Updated Date |
| BALL_UpdatedTime | time |  |  | SI | Updated Time |
| BALL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bag & mask, positive end expiratory pressure (PEEP... |
| Q04 | - |  |  | SI | Oropharyngeal airway present and correct size avai... |
| Q05 | - |  |  | SI | Emergency intravascular port identified / peripher... |
| Q06 | - |  |  | SI | Details |
| Q07 | - |  |  | SI | Suction equipment present and functional |
| Q08 | - |  |  | SI | All equipment plugged in and powered |
| Q09 | - |  |  | SI | Medications: orders versus infusions checked |
| Q10 | - |  |  | SI | Ventilator settings and alarms checked |
| Q11 | - |  |  | SI | Apnoea parameters checked |
| Q12 | - |  |  | SI | Monitor alarm limits checked |
| Q13 | - |  |  | SI | Safety check notes |
| Q14 | - |  |  | SI | Equipment Changes |
| Q15 | - |  |  | SI | Closed suction system |
| Q16 | - |  |  | SI | Due for change every 3 days |
| Q17 | - |  |  | SI | Date due for change |
| Q18 | - |  |  | SI | Yankauer sucker and tubing |
| Q19 | - |  |  | SI | Check daily |
| Q20 | - |  |  | SI | Ventilator circuit / Hiflow circuit |
| Q21 | - |  |  | SI | Due for change every 2 weeks |
| Q22 | - |  |  | SI | Date due for change |
| Q23 | - |  |  | SI | Humidifier water bag |
| Q24 | - |  |  | SI | Change daily |
| Q25 | - |  |  | SI | Date due for change |
| Q26 | - |  |  | SI | Checked for any additional due equipment changes |
| Q27 | - |  |  | SI | Additional equipment check notes |
| Q28 | - |  |  | SI | General |
| Q29 | - |  |  | SI | Identification band (+/- red allergy band in situ) |
| Q30 | - |  |  | SI | Falls risk assessment completed |
| Q31 | - |  |  | SI | Pressure injury risk and skin assessment completed |
| Q32 | - |  |  | SI | Wound charts reviewed |
| Q33 | - |  |  | SI | Invasive devices summary reviewed and updated |
| Q34 | - |  |  | SI | Cognition and delirium assessment completed |
| Q35 | - |  |  | SI | Compression stockings and calf compressors in situ... |
| Q36 | - |  |  | SI | Oral assessment and regular oral care attended |
| Q37 | - |  |  | SI | Electrocardiograph (ECG) dots |
| Q38 | - |  |  | SI | Due for change: daily |
| Q39 | - |  |  | SI | General notes |
| Q40 | - |  |  | SI | Cardiovascular |
| Q41 | - |  |  | SI | Daily 12 lead ECG (before rounds, if on inotropes) |
| Q42 | - |  |  | SI | Cardiovascular notes |
| Q43 | - |  |  | SI | Respiratory |
| Q44 | - |  |  | SI | Air entry |
| Q44ObsDR | - |  |  | SI | Air entry DR |
| Q45 | - |  |  | SI | Work of breathing |
| Q45ObsDR | - |  |  | SI | Work of breathing DR |
| Q46 | - |  |  | SI | Breath sounds (Left) |
| Q46ObsDR | - |  |  | SI | Breath sounds (Left) DR |
| Q47 | - |  |  | SI | Breath sounds (Right) |
| Q47ObsDR | - |  |  | SI | Breath sounds (Right) DR |
| Q48 | - |  |  | SI | Breath sounds |
| Q49 | - |  |  | SI | Respiratory notes |
| Q50 | - |  |  | SI | Gastrointestinal |
| Q51 | - |  |  | SI | Nasogastric / Orogastric tube position checked |
| Q52 | - |  |  | SI | Bowel sounds |
| Q52ObsDR | - |  |  | SI | Bowel sounds DR |
| Q53 | - |  |  | SI | Bowels last opened (start protocol if bowels not o... |
| Q54 | - |  |  | SI | Enteral feeding line and container (change every 2... |
| Q55 | - |  |  | SI | Sterile water for oral medications (date and label... |
| Q56 | - |  |  | SI | Gastrointestinal notes |
| Q57 | - |  |  | SI | Renal |
| Q58 | - |  |  | SI | Catheter care attended and documented |
| Q59 | - |  |  | SI | Catheter securement device in situ |
| Q60 | - |  |  | SI | Daily weight performed |
| Q61 | - |  |  | SI | Urine bag labelled and dated |
| Q62 | - |  |  | SI | Due for change every 7 days |
| Q63 | - |  |  | SI | Date change is due |
| Q64 | - |  |  | SI | Waste drain flushed with water |
| Q65 | - |  |  | SI | If on continuous renal replacement therapy (CCRT) |
| Q66 | - |  |  | SI | Renal notes |
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