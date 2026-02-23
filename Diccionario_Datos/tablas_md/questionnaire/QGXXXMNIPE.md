# questionnaire.QGXXXMNIPE

> Newborn Infant physical examination

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Newborn Infant physical examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Colour |
| Q02 | varchar |  |  | SI | Breathing |
| Q03 | varchar |  |  | SI | Behaviour |
| Q04 | varchar |  |  | SI | Activity |
| Q05 | varchar |  |  | SI | Posture |
| Q06 | varchar |  |  | SI | Face |
| Q07 | varchar |  |  | SI | Nose |
| Q08 | varchar |  |  | SI | Mouth |
| Q09 | varchar |  |  | SI | Ears |
| Q10 | varchar |  |  | SI | Neck |
| Q11 | varchar |  |  | SI | Head symmetry |
| Q12 | varchar |  |  | SI | Head circumference |
| Q12ObsDR | varchar |  | FK | SI | Head circumference DR |
| Q12a | varchar |  |  | SI | Head circumference |
| Q12aObsDR | varchar |  | FK | SI | Head circumference DR |
| Q13 | varchar |  |  | SI | Opacities |
| Q14 | varchar |  |  | SI | Red reflex |
| Q15 | varchar |  |  | SI | Position |
| Q16 | varchar |  |  | SI | Heart Rate |
| Q16ObsDR | varchar |  | FK | SI | Heart Rate DR |
| Q17 | varchar |  |  | SI | Rhythm and sounds |
| Q18 | varchar |  |  | SI | Murmurs |
| Q19 | varchar |  |  | SI | Femoral pulse volume |
| Q20 | varchar |  |  | SI | Shape |
| Q21 | varchar |  |  | SI | Organomegaly |
| Q22 | varchar |  |  | SI | Cord |
| Q23 | varchar |  |  | SI | Effort |
| Q24 | varchar |  |  | SI | Sounds |
| Q25 | varchar |  |  | SI | Respiratory rate |
| Q25ObsDR | varchar |  | FK | SI | Respiratory rate DR |
| Q26 | varchar |  |  | SI | Completeness |
| Q27 | varchar |  |  | SI | Patency |
| Q28 | varchar |  |  | SI | Undescended testes |
| Q29 | varchar |  |  | SI | Bony structure |
| Q30 | varchar |  |  | SI | Skin integrity |
| Q31 | varchar |  |  | SI | Texture |
| Q32 | varchar |  |  | SI | Birthmarks |
| Q33 | varchar |  |  | SI | Rashes |
| Q34 | varchar |  |  | SI | Tone |
| Q35 | varchar |  |  | SI | Hip symmetry |
| Q36 | varchar |  |  | SI | Skin folds |
| Q37 | varchar |  |  | SI | Neck |
| Q38 | varchar |  |  | SI | Clavicles |
| Q39 | varchar |  |  | SI | Limbs |
| Q40 | varchar |  |  | SI | Hands |
| Q41 | varchar |  |  | SI | Feet |
| Q42 | varchar |  |  | SI | Digits |
| Q43 | varchar |  |  | SI | Weight |
| Q43ObsDR | varchar |  | FK | SI | Weight DR |
| Q44 | varchar |  |  | SI | Additional Infomation (Head) |
| Q45 | varchar |  |  | SI | Additional information (Eyes) |
| Q46 | varchar |  |  | SI | Additional information (Proportions and Symmetry) |
| Q47 | varchar |  |  | SI | Additional information (Heart) |
| Q48 | varchar |  |  | SI | Additional information (Lungs) |
| Q49 | varchar |  |  | SI | Additional information (Abdomen) |
| Q50 | varchar |  |  | SI | Additional Information (Genitalia and Anus) |
| Q51 | varchar |  |  | SI | Additional information (Spine) |
| Q52 | varchar |  |  | SI | Additional information (Skin) |
| Q53 | varchar |  |  | SI | Additional information (CNS) |
| Q54 | varchar |  |  | SI | Additional information (Hips) |
| Q55 | varchar |  |  | SI | Birth weight |
| Q56 | varchar |  |  | SI | Additional Information (Birth weight) |
| Q57EYES | varchar |  |  | SI | Outcome |
| Q57HEART | varchar |  |  | SI | Outcome |
| Q57OTHER | varchar |  |  | SI | Any other outcomes |
| Q57TESTES | varchar |  |  | SI | Outcome |
| Q62 | varchar |  |  | SI | Galeazzi sign |
| Q63 | varchar |  |  | SI | Barlows test |
| Q63C | varchar |  |  | SI | Details |
| Q66 | varchar |  |  | SI | Fontanelles |
| Q67 | varchar |  |  | SI | Reflex Grasp |
| Q67HIPS | varchar |  |  | SI | Outcome |
| Q68 | varchar |  |  | SI | Moro |
| Q69 | varchar |  |  | SI | Sucking |
| Q70 | varchar |  |  | SI | Ortolani test |
| Q71 | varchar |  |  | SI | Are there any concerns with the following? |
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