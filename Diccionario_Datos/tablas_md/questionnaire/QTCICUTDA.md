# questionnaire.QTCICUTDA

> Tracheostomy Insertion and Care

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tracheostomy Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Insertion date |
| Q02 | time |  |  | SI | Insertion time |
| Q03 | date |  |  | SI | Removal date |
| Q04 | time |  |  | SI | Removal time |
| Q05 | varchar |  |  | SI | Procedure notes |
| Q07 | varchar |  |  | SI | Size |
| Q08 | varchar |  |  | SI | Types |
| Q09 | varchar |  |  | SI | Emergency equipment in room |
| Q10 | varchar |  |  | SI | Securing device |
| Q10ObsDR | varchar |  | FK | SI | Securing device DR |
| Q11 | bit |  |  | SI | Inner cannula in situ |
| Q12 | date |  |  | SI | Date |
| Q13 | time |  |  | SI | Time |
| Q14 | varchar |  |  | SI | Current Insertion Details |
| Q15 | varchar |  |  | SI | Insertion status |
| Q16 | varchar |  |  | SI | Pre Procedure Checklist |
| Q17 | varchar |  |  | SI | Tracheostomy Safety Checklist |
| Q18 | varchar |  |  | SI | Consent completed |
| Q19 | varchar |  |  | SI | Coagulation (INR <1.5, APTT < 50) or factors admin... |
| Q20 | varchar |  |  | SI | Platelets > 50 x 10<sup>9</sup> (or platelets tran... |
| Q21 | varchar |  |  | SI | Fraction of inspired oxygen (FiO2) ≥ 0.6 |
| Q22 | varchar |  |  | SI | Positive end-expiratory pressure (PEEP) ≤ 10cmH2O |
| Q23 | varchar |  |  | SI | Cervical spine stable |
| Q24 | varchar |  |  | SI | Site examined (nil infection, masses, acceptable a... |
| Q25 | varchar |  |  | SI | Bronchoscope available and working |
| Q26 | varchar |  |  | SI | End-tidal carbon dioxide (ETCO2) monitor available... |
| Q27 | varchar |  |  | SI | Feeds stopped > 4hrs ago |
| Q28 | varchar |  |  | SI | Difficult airway equipment available |
| Q29 | varchar |  |  | SI | Grade of previous intubation |
| Q30 | varchar |  |  | SI | Safety check notes |
| Q31 | varchar |  |  | SI | Pre Insertion Checks |
| Q32 | varchar |  |  | SI | Insertion site assessed and marked if appropriate |
| Q33 | varchar |  |  | SI | Barrier precautions used |
| Q34 | varchar |  |  | SI | Aseptic technique used |
| Q35 | varchar |  |  | SI | Skin disinfected with |
| Q36 | varchar |  |  | SI | Pre-procedure notes |
| Q37 | varchar |  |  | SI | Insertion Details |
| Q38 | varchar |  |  | SI | Reason for insertion |
| Q39 | varchar |  |  | SI | Indication for tracheostomy tube change |
| Q40 | varchar |  |  | SI | Type |
| Q41 | varchar |  |  | SI | Brand |
| Q42 | numeric |  |  | SI | Size of tracheostomy tube (mm) |
| Q43 | varchar |  |  | SI | Chest x-ray post procedure viewed and checked |
| Q44 | varchar |  |  | SI | Inserted by |
| Q45 | varchar |  |  | SI | Airway operator |
| Q46 | varchar |  |  | SI | Emergency Equipment in Room / Available |
| Q47 | varchar |  |  | SI | Tracheostomy tube of same size and type |
| Q48 | varchar |  |  | SI | Tracheostomy tube of same type but one size smalle... |
| Q49 | varchar |  |  | SI | Tracheal dilators |
| Q50 | varchar |  |  | SI | Bag valve mask |
| Q51 | varchar |  |  | SI | Suction equipment |
| Q52 | varchar |  |  | SI | Spare inner cannula |
| Q53 | varchar |  |  | SI | Dummy1 |
| Q54 | varchar |  |  | SI | Dummy2 |
| Q55 | varchar |  |  | SI | Equipment notes |
| Q56 | varchar |  |  | SI | Tracheostomy Tube Change Record |
| Q57 | date |  |  | SI | Date |
| Q58 | time |  |  | SI | Time |
| Q59 | varchar |  |  | SI | Consent |
| Q60 | varchar |  |  | SI | Indication for tracheostomy tube change |
| Q61 | varchar |  |  | SI | Other change indication |
| Q62 | varchar |  |  | SI | Type of tracheostomy tube |
| Q63 | numeric |  |  | SI | Size of tracheostomy tube |
| Q64 | varchar |  |  | SI | Cuffed |
| Q65 | varchar |  |  | SI | Fenestrated |
| Q66 | varchar |  |  | SI | Chest x-ray post procedure to confirm placement |
| Q67 | varchar |  |  | SI | Care provider 1 |
| Q68 | varchar |  |  | SI | Care provider 2 |
| Q69 | varchar |  |  | SI | Procedure notes |
| Q71 | varchar |  |  | SI | Assessments |
| Q72 | varchar |  |  | SI | Indications for removal |
| Q73 | varchar |  |  | SI | Other removal reason |
| Q74 | varchar |  |  | SI | Consent obtained |
| Q75 | varchar |  |  | SI | Removed by |
| Q76 | varchar |  |  | SI | Removal notes |
| Q77 | varchar |  |  | SI | Complications |
| Q78 | varchar |  |  | SI | Complication |
| Q79 | varchar |  |  | SI | Other complication |
| Q80 | varchar |  |  | SI | Complication notes |
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