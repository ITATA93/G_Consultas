# questionnaire.QTCPROM

> Patient-reported outcome measure (UL-PROM) for Duchenne Muscular Dystrophy (DMD)

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient-reported outcome measure (UL-PROM) for Duchenne Muscular Dystrophy (DMD)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date of evaluation |
| Q04 | varchar |  |  | SI | How the questionnaire was completed |
| Q05 | varchar |  |  | SI | The respondent is |
| Q06 | varchar |  |  | SI | Spinal surgery |
| Q07 | varchar |  |  | SI | Respiratory support - Night time |
| Q08 | varchar |  |  | SI | Mobility and transfers |
| Q09 | varchar |  |  | SI | Chair, bed and toilet are of standard height |
| Q10 | varchar |  |  | SI | Get on and off the floor |
| Q11 | varchar |  |  | SI | Get in and out of a chair |
| Q12 | varchar |  |  | SI | Get in and out of bed |
| Q13 | varchar |  |  | SI | Get on and off the toilet |
| Q14 | varchar |  |  | SI | Go up and down stairs |
| Q15 | varchar |  |  | SI | During the last week was it easy or hard for your ... |
| Q16 | varchar |  |  | SI | Drink from a glass without a straw |
| Q17 | varchar |  |  | SI | Cut up different textures of food |
| Q18 | varchar |  |  | SI | Feed himself |
| Q19 | varchar |  |  | SI | Pour a drink from a half liter bottle or a half pi... |
| Q20 | varchar |  |  | SI | Open a pack of crisps |
| Q21 | varchar |  |  | SI | Screw the cap off a bottle that has not been opene... |
| Q22 | varchar |  |  | SI | Open a can of softdrink |
| Q24 | varchar |  |  | SI | During the last week was it easy or hard for your ... |
| Q25 | varchar |  |  | SI | Brush his teeth |
| Q26 | varchar |  |  | SI | Pull up his trousers after using the toilet |
| Q27 | varchar |  |  | SI | Wash his hands |
| Q28 | varchar |  |  | SI | Button up |
| Q29 | varchar |  |  | SI | Put his jacket on |
| Q30 | varchar |  |  | SI | Fasten a zipper |
| Q31 | varchar |  |  | SI | Scratch his hair |
| Q32 | varchar |  |  | SI | Wipe his nose |
| Q34 | varchar |  |  | SI | During the last week was it easy or hard for your ... |
| Q35 | varchar |  |  | SI | Open a drawer |
| Q36 | varchar |  |  | SI | Open a fridge door |
| Q37 | varchar |  |  | SI | Take a book out of a bag on his lap |
| Q38 | varchar |  |  | SI | Pick up a pen from the floor |
| Q39 | varchar |  |  | SI | Press buttons on an elevator |
| Q40 | varchar |  |  | SI | Turn a light switch on/off on the wall at standard... |
| Q42 | varchar |  |  | SI | During the last week was it easy or hard for your ... |
| Q43 | varchar |  |  | SI | Use a remote control |
| Q44 | varchar |  |  | SI | Dial / Text on a cell phone |
| Q45 | varchar |  |  | SI | Bring a phone to his ear |
| Q46 | varchar |  |  | SI | Type on a computer with a keyboard |
| Q47 | varchar |  |  | SI | Use a mouse |
| Q48 | varchar |  |  | SI | Use a touchpad |
| Q49 | varchar |  |  | SI | Turn the pages of a book |
| Q50 | varchar |  |  | SI | Sign his name |
| Q51 | varchar |  |  | SI | Write several lines |
| Q52 | varchar |  |  | SI | Pick up small objects from the table |
| Q53 | varchar |  |  | SI | Take money from his wallet from his pocket to pay ... |
| Q54 | varchar |  |  | SI | Reach out to shake hands |
| Q56 | varchar |  |  | SI | List 5 activities you/your son usually do (e.g. ba... |
| Q57 | varchar |  |  | SI | Activity 1 |
| Q58 | varchar |  |  | SI | Follow up |
| Q59 | varchar |  |  | SI | Activity 2 |
| Q60 | varchar |  |  | SI | Follow up |
| Q61 | varchar |  |  | SI | Activity 3 |
| Q62 | varchar |  |  | SI | Follow up |
| Q63 | varchar |  |  | SI | Activity 4 |
| Q64 | varchar |  |  | SI | Follow up |
| Q65 | varchar |  |  | SI | Activity 5 |
| Q66 | varchar |  |  | SI | Follow up |
| Q67 | varchar |  |  | SI | Some kind of problems can make it hard for your so... |
| Q68 | varchar |  |  | SI | He may feel tired, need more time or need help and... |
| Q69 | varchar |  |  | SI | 3 - Easy |
| Q70 | varchar |  |  | SI | Can do independently without difficulty, without a... |
| Q71 | varchar |  |  | SI | 2 - A little hard |
| Q72 | varchar |  |  | SI | Can do independently with some difficulty: slowly ... |
| Q73 | varchar |  |  | SI | 1 - Very hard |
| Q74 | varchar |  |  | SI | Can do independently with a lot of difficulty or c... |
| Q75 | varchar |  |  | SI | 0 - Can not do |
| Q76 | varchar |  |  | SI | Can not do at all |
| Q77 | varchar |  |  | SI | Score |
| Q78 | varchar |  |  | SI | 0 - 126 |
| Q79 | varchar |  |  | SI | Classification |
| Q80 | varchar |  |  | SI | Higher scores indicate better conditions |
| Q81 | varchar |  |  | SI | A multidisciplinary international Clinical Outcome... |
| Q82 | varchar |  |  | SI | their advocacy groups designed the Performance of ... |
| Q83 | varchar |  |  | SI | according to a specific contextual framework of up... |
| Q84 | varchar |  |  | SI | 0 - 126: Higher scores indicate better conditions |
| Q85 | varchar |  |  | SI | Respiratory support - Day and night time |
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