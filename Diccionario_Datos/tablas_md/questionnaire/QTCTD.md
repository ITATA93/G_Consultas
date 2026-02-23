# questionnaire.QTCTD

> Nursing Transfer Checklist

**Schema:** questionnaire
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nursing Transfer Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Receiving clinician |
| Q02 | varchar |  |  | SI | Receiving clinician contact details |
| Q03 | varchar |  |  | SI | Receiving ward manager |
| Q04 | varchar |  |  | SI | Receiving bed manager |
| Q05 | varchar |  |  | SI | Receiving facility ready for transfer? |
| Q06 | date |  |  | SI | Date/Time bed expected to be ready |
| Q07 | time |  |  | SI | Time bed expected to be ready |
| Q08 | varchar |  |  | SI | Transport arranged |
| Q09 | varchar |  |  | SI | Transport company |
| Q10 | varchar |  |  | SI | Escort |
| Q100 | varchar |  |  | SI | Travel itineraries received for |
| Q101 | varchar |  |  | SI | Travel itineraries notes |
| Q102 | varchar |  |  | SI | Accommodation booked for hospital staff |
| Q103 | varchar |  |  | SI | Accommodation notes |
| Q104 | varchar |  |  | SI | Clearance to fly, oxygen request forms completd |
| Q105 | varchar |  |  | SI | Clearance to fly and oxygen request forms notes |
| Q106 | varchar |  |  | SI | 5 cab charges collected |
| Q107 | varchar |  |  | SI | Cab charges notes |
| Q108 | varchar |  |  | SI | Cardiac interstate transfer notes |
| Q11 | varchar |  |  | SI | Nutrition and Swallowing |
| Q12 | varchar |  |  | SI | Fasting status |
| Q13 | date |  |  | SI | Date and time of last intake |
| Q14 | time |  |  | SI | Time of last intake |
| Q15 | varchar |  |  | SI | Main nutritional intake method |
| Q16 | varchar |  |  | SI | Diet type |
| Q16ObsDR | varchar |  | FK | SI | Diet type DR |
| Q17 | varchar |  |  | SI | Food consistency |
| Q17ObsDR | varchar |  | FK | SI | Food consistency DR |
| Q18 | varchar |  |  | SI | Fluid consistency |
| Q18ObsDR | varchar |  | FK | SI | Fluid consistency DR |
| Q19 | varchar |  |  | SI | Safe swallowing strategies |
| Q20 | varchar |  |  | SI | Dietary supplements |
| Q21 | varchar |  |  | SI | Tablet medication format |
| Q22 | varchar |  |  | SI | Enteral nutrition method |
| Q22ObsDR | varchar |  | FK | SI | Enteral nutrition method DR |
| Q23 | varchar |  |  | SI | Parenteral nutrition method |
| Q23ObsDR | varchar |  | FK | SI | Parenteral nutrition method DR |
| Q24 | varchar |  |  | SI | Feed sent? |
| Q25 | varchar |  |  | SI | Additional information |
| Q26 | varchar |  |  | SI | Bladder and Bowels |
| Q27 | varchar |  |  | SI | Continence status |
| Q28 | varchar |  |  | SI | Details of catheter insertion should be included i... |
| Q29 | date |  |  | SI | Last voided date and time |
| Q30 | time |  |  | SI | Last voided time |
| Q31 | date |  |  | SI | Bowels last opened date and time |
| Q32 | time |  |  | SI | Bowels last opened time |
| Q33 | varchar |  |  | SI | Mobility and Dependence |
| Q34 | varchar |  |  | SI | Mobility |
| Q35 | varchar |  |  | SI | Transferring |
| Q36 | varchar |  |  | SI | Activities of daily living / hygiene |
| Q37 | varchar |  |  | SI | Personal Belongings |
| Q38 | varchar |  |  | SI | Clothing |
| Q39 | varchar |  |  | SI | Dentures |
| Q40 | varchar |  |  | SI | Glasses |
| Q41 | varchar |  |  | SI | Contact lens |
| Q42 | varchar |  |  | SI | Hearing aids |
| Q43 | varchar |  |  | SI | Ambulatory aid |
| Q44 | varchar |  |  | SI | Prosthesis |
| Q45 | varchar |  |  | SI | Other belongings (specify in comments) |
| Q46 | varchar |  |  | SI | Personal belonging details |
| Q47 | varchar |  |  | SI | Valuables |
| Q48 | varchar |  |  | SI | Wallet / Money |
| Q49 | varchar |  |  | SI | Important papers |
| Q50 | varchar |  |  | SI | Jewellery |
| Q51 | varchar |  |  | SI | Mobile phone |
| Q52 | varchar |  |  | SI | Other electronic device |
| Q53 | varchar |  |  | SI | Other valuables (specify in comments) |
| Q54 | varchar |  |  | SI | Valuables comments |
| Q55 | varchar |  |  | SI | Physical documents sent with patient |
| Q56 | varchar |  |  | SI | Form completed by |
| Q57 | varchar |  |  | SI | Second signing by |
| Q58 | date |  |  | SI | Date |
| Q59 | time |  |  | SI | Time |
| Q60 | varchar |  |  | SI | Behaviour |
| Q61 | varchar |  |  | SI | Behavioural issues |
| Q62 | varchar |  |  | SI | Additional information |
| Q63 | varchar |  |  | SI | Additional information |
| Q64 | varchar |  |  | SI | Additional information |
| Q65 | varchar |  |  | SI | Other escort details |
| Q66 | varchar |  |  | SI | Receiving hospital |
| Q67 | varchar |  |  | SI | Transfer date discussed with patient |
| Q68 | date |  |  | SI | Date of transfer |
| Q69 | varchar |  |  | SI | Family member notified of transfer |
| Q70 | varchar |  |  | SI | Substitute decision maker notified of transfer |
| Q71 | varchar |  |  | SI | Patient / Family member discussion notes |
| Q72 | varchar |  |  | SI | Mode of transport |
| Q73 | varchar |  |  | SI | Other mode of transport notes |
| Q74 | varchar |  |  | SI | Escort required |
| Q75 | varchar |  |  | SI | Escort type |
| Q76 | varchar |  |  | SI | Other escort type |
| Q77 | varchar |  |  | SI | Escort approved |
| Q79 | varchar |  |  | SI | Patient details |
| Q80 | varchar |  |  | SI | Patient ID band on patient |
| Q81 | varchar |  |  | SI | Patient property given to |
| Q82 | varchar |  |  | SI | (please see patient property form if appropriate) |
| Q83 | varchar |  |  | SI | Patient has own medication returned |
| Q84 | varchar |  |  | SI | Patient own medication notes |
| Q85 | varchar |  |  | SI | If patient is being transferred to an interstate h... |
| Q86 | varchar |  |  | SI | Nursing transfer / discharge summary questionnaire... |
| Q87 | varchar |  |  | SI | Nursing discharge note completed |
| Q88 | varchar |  |  | SI | Patient transfer nursing information printed off |
| Q89 | varchar |  |  | SI | Medical discharge summary completed and printed |
| Q90 | varchar |  |  | SI | Nursing transfer notes |
| Q91 | varchar |  |  | SI | Cardiac Interstate Transfers |
| Q92 | varchar |  |  | SI | Hospital escort required |
| Q93 | varchar |  |  | SI | Other escort notes |
| Q94 | varchar |  |  | SI | If escorted, 2 x IV cannula in situ, patent and da... |
| Q95 | varchar |  |  | SI | Cannulation notes |
| Q96 | varchar |  |  | SI | Cardiac Clinical Nurse Consultant aware of transfe... |
| Q97 | varchar |  |  | SI | Cardiac Clinical Nurse Consultant notes |
| Q98 | varchar |  |  | SI | Hospital staff organised and booked |
| Q99 | varchar |  |  | SI | Hospital staff booked notes |
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