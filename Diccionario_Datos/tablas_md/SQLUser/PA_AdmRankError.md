# SQLUser.PA_AdmRankError

**Schema:** SQLUser
**Columnas:** 157
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RKERRowID | bigint | PK |  | NO | - |
| ChildQ78DR | - |  |  | SI | Child Reference: Escort information |
| Q01 | - |  |  | SI | Receiving clinician |
| Q02 | - |  |  | SI | Receiving clinician contact details |
| Q03 | - |  |  | SI | Receiving ward manager |
| Q04 | - |  |  | SI | Receiving bed manager |
| Q05 | - |  |  | SI | Receiving facility ready for transfer? |
| Q06 | - |  |  | SI | Date/Time bed expected to be ready |
| Q07 | - |  |  | SI | Time bed expected to be ready |
| Q08 | - |  |  | SI | Transport arranged |
| Q09 | - |  |  | SI | Transport company |
| Q10 | - |  |  | SI | Escort |
| Q100 | - |  |  | SI | Travel itineraries received for |
| Q101 | - |  |  | SI | Travel itineraries notes |
| Q102 | - |  |  | SI | Accommodation booked for hospital staff |
| Q103 | - |  |  | SI | Accommodation notes |
| Q104 | - |  |  | SI | Clearance to fly, oxygen request forms completd |
| Q105 | - |  |  | SI | Clearance to fly and oxygen request forms notes |
| Q106 | - |  |  | SI | 5 cab charges collected |
| Q107 | - |  |  | SI | Cab charges notes |
| Q108 | - |  |  | SI | Cardiac interstate transfer notes |
| Q11 | - |  |  | SI | Nutrition and Swallowing |
| Q12 | - |  |  | SI | Fasting status |
| Q13 | - |  |  | SI | Date and time of last intake |
| Q14 | - |  |  | SI | Time of last intake |
| Q15 | - |  |  | SI | Main nutritional intake method |
| Q16 | - |  |  | SI | Diet type |
| Q16ObsDR | - |  |  | SI | Diet type DR |
| Q17 | - |  |  | SI | Food consistency |
| Q17ObsDR | - |  |  | SI | Food consistency DR |
| Q18 | - |  |  | SI | Fluid consistency |
| Q18ObsDR | - |  |  | SI | Fluid consistency DR |
| Q19 | - |  |  | SI | Safe swallowing strategies |
| Q20 | - |  |  | SI | Dietary supplements |
| Q21 | - |  |  | SI | Tablet medication format |
| Q22 | - |  |  | SI | Enteral nutrition method |
| Q22ObsDR | - |  |  | SI | Enteral nutrition method DR |
| Q23 | - |  |  | SI | Parenteral nutrition method |
| Q23ObsDR | - |  |  | SI | Parenteral nutrition method DR |
| Q24 | - |  |  | SI | Feed sent? |
| Q25 | - |  |  | SI | Additional information |
| Q26 | - |  |  | SI | Bladder and Bowels |
| Q27 | - |  |  | SI | Continence status |
| Q28 | - |  |  | SI | Details of catheter insertion should be included i... |
| Q29 | - |  |  | SI | Last voided date and time |
| Q30 | - |  |  | SI | Last voided time |
| Q31 | - |  |  | SI | Bowels last opened date and time |
| Q32 | - |  |  | SI | Bowels last opened time |
| Q33 | - |  |  | SI | Mobility and Dependence |
| Q34 | - |  |  | SI | Mobility |
| Q35 | - |  |  | SI | Transferring |
| Q36 | - |  |  | SI | Activities of daily living / hygiene |
| Q37 | - |  |  | SI | Personal Belongings |
| Q38 | - |  |  | SI | Clothing |
| Q39 | - |  |  | SI | Dentures |
| Q40 | - |  |  | SI | Glasses |
| Q41 | - |  |  | SI | Contact lens |
| Q42 | - |  |  | SI | Hearing aids |
| Q43 | - |  |  | SI | Ambulatory aid |
| Q44 | - |  |  | SI | Prosthesis |
| Q45 | - |  |  | SI | Other belongings (specify in comments) |
| Q46 | - |  |  | SI | Personal belonging details |
| Q47 | - |  |  | SI | Valuables |
| Q48 | - |  |  | SI | Wallet / Money |
| Q49 | - |  |  | SI | Important papers |
| Q50 | - |  |  | SI | Jewellery |
| Q51 | - |  |  | SI | Mobile phone |
| Q52 | - |  |  | SI | Other electronic device |
| Q53 | - |  |  | SI | Other valuables (specify in comments) |
| Q54 | - |  |  | SI | Valuables comments |
| Q55 | - |  |  | SI | Physical documents sent with patient |
| Q56 | - |  |  | SI | Form completed by |
| Q57 | - |  |  | SI | Second signing by |
| Q58 | - |  |  | SI | Date |
| Q59 | - |  |  | SI | Time |
| Q60 | - |  |  | SI | Behaviour |
| Q61 | - |  |  | SI | Behavioural issues |
| Q62 | - |  |  | SI | Additional information |
| Q63 | - |  |  | SI | Additional information |
| Q64 | - |  |  | SI | Additional information |
| Q65 | - |  |  | SI | Other escort details |
| Q66 | - |  |  | SI | Receiving hospital |
| Q67 | - |  |  | SI | Transfer date discussed with patient |
| Q68 | - |  |  | SI | Date of transfer |
| Q69 | - |  |  | SI | Family member notified of transfer |
| Q70 | - |  |  | SI | Substitute decision maker notified of transfer |
| Q71 | - |  |  | SI | Patient / Family member discussion notes |
| Q72 | - |  |  | SI | Mode of transport |
| Q73 | - |  |  | SI | Other mode of transport notes |
| Q74 | - |  |  | SI | Escort required |
| Q75 | - |  |  | SI | Escort type |
| Q76 | - |  |  | SI | Other escort type |
| Q77 | - |  |  | SI | Escort approved |
| Q79 | - |  |  | SI | Patient details |
| Q80 | - |  |  | SI | Patient ID band on patient |
| Q81 | - |  |  | SI | Patient property given to |
| Q82 | - |  |  | SI | (please see patient property form if appropriate) |
| Q83 | - |  |  | SI | Patient has own medication returned |
| Q84 | - |  |  | SI | Patient own medication notes |
| Q85 | - |  |  | SI | If patient is being transferred to an interstate h... |
| Q86 | - |  |  | SI | Nursing transfer / discharge summary questionnaire... |
| Q87 | - |  |  | SI | Nursing discharge note completed |
| Q88 | - |  |  | SI | Patient transfer nursing information printed off |
| Q89 | - |  |  | SI | Medical discharge summary completed and printed |
| Q90 | - |  |  | SI | Nursing transfer notes |
| Q91 | - |  |  | SI | Cardiac Interstate Transfers |
| Q92 | - |  |  | SI | Hospital escort required |
| Q93 | - |  |  | SI | Other escort notes |
| Q94 | - |  |  | SI | If escorted, 2 x IV cannula in situ, patent and da... |
| Q95 | - |  |  | SI | Cannulation notes |
| Q96 | - |  |  | SI | Cardiac Clinical Nurse Consultant aware of transfe... |
| Q97 | - |  |  | SI | Cardiac Clinical Nurse Consultant notes |
| Q98 | - |  |  | SI | Hospital staff organised and booked |
| Q99 | - |  |  | SI | Hospital staff booked notes |
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
| RKERDate | date |  |  | SI | Date |
| RKERLocDR | bigint |  | FK | NO | Des Ref Location |
| RKERTime | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*