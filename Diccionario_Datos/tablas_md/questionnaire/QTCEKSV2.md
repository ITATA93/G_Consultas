# questionnaire.QTCEKSV2

> Egen Klassifikation Scale Version 2 (EK2)

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Egen Klassifikation Scale Version 2 (EK2)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | NOTE: Score the best you have done in the last two... |
| Q04 | varchar |  |  | SI | 1. Ability to use wheelchair. How do you get aroun... |
| Q05 | varchar |  |  | SI | 2. Ability to transfer from wheelchair. How do you... |
| Q06 | varchar |  |  | SI | 3. Ability to stand. Do you sometimes stand? How d... |
| Q07 | varchar |  |  | SI | 4. Ability to balance in the wheelchair. Can you b... |
| Q08 | varchar |  |  | SI | 5. Ability to move the arms. Can you move your fin... |
| Q09 | varchar |  |  | SI | 6. Ability to use the hands and arms for eating. C... |
| Q10 | varchar |  |  | SI | 7. Ability to turn in bed. How do you turn in bed ... |
| Q11 | varchar |  |  | SI | 8. Ability to cough. How do you cough when you hav... |
| Q12 | varchar |  |  | SI | 9. Ability to speak. Can you speak so that what yo... |
| Q13 | varchar |  |  | SI | 10. Physical well-being. This relates to respirato... |
| Q14 | varchar |  |  | SI | Use the categories as questions |
| Q15 | varchar |  |  | SI | 11. Daytime fatigue. Do you have to organize your ... |
| Q16 | varchar |  |  | SI | 12. Head control. How much head support do you nee... |
| Q17 | varchar |  |  | SI | 13. Ability to control joystick. What kind of joys... |
| Q18 | varchar |  |  | SI | 14. Food textures. Do you have to modify your food... |
| Q19 | varchar |  |  | SI | 15. Eating a meal (with or without assistance). Ho... |
| Q20 | varchar |  |  | SI | 16. Swallowing. Do you ever have problems with swa... |
| Q21 | varchar |  |  | SI | 17. Hand function. Which of these activities can y... |
| Q22 | varchar |  |  | SI | Score |
| Q23 | varchar |  |  | SI | Classification |
| Q24 | varchar |  |  | SI | 0 - 51 |
| Q25 | varchar |  |  | SI | Higher scores correspond to a higher level of disa... |
| Q26 | varchar |  |  | SI | 0 - 51: Higher scores correspond to a higher level... |
| Q27 | varchar |  |  | SI | The Egen Klassifikation Scale version 2 (EK2) is a... |
| Q28 | varchar |  |  | SI | It examined activities and abilities such as trans... |
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