# SQLUser.ORC_ReasonEqNotAvail

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REQNAV_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | NOTE: Score the best you have done in the last two... |
| Q04 | - |  |  | SI | 1. Ability to use wheelchair. How do you get aroun... |
| Q05 | - |  |  | SI | 2. Ability to transfer from wheelchair. How do you... |
| Q06 | - |  |  | SI | 3. Ability to stand. Do you sometimes stand? How d... |
| Q07 | - |  |  | SI | 4. Ability to balance in the wheelchair. Can you b... |
| Q08 | - |  |  | SI | 5. Ability to move the arms. Can you move your fin... |
| Q09 | - |  |  | SI | 6. Ability to use the hands and arms for eating. C... |
| Q10 | - |  |  | SI | 7. Ability to turn in bed. How do you turn in bed ... |
| Q11 | - |  |  | SI | 8. Ability to cough. How do you cough when you hav... |
| Q12 | - |  |  | SI | 9. Ability to speak. Can you speak so that what yo... |
| Q13 | - |  |  | SI | 10. Physical well-being. This relates to respirato... |
| Q14 | - |  |  | SI | Use the categories as questions |
| Q15 | - |  |  | SI | 11. Daytime fatigue. Do you have to organize your ... |
| Q16 | - |  |  | SI | 12. Head control. How much head support do you nee... |
| Q17 | - |  |  | SI | 13. Ability to control joystick. What kind of joys... |
| Q18 | - |  |  | SI | 14. Food textures. Do you have to modify your food... |
| Q19 | - |  |  | SI | 15. Eating a meal (with or without assistance). Ho... |
| Q20 | - |  |  | SI | 16. Swallowing. Do you ever have problems with swa... |
| Q21 | - |  |  | SI | 17. Hand function. Which of these activities can y... |
| Q22 | - |  |  | SI | Score |
| Q23 | - |  |  | SI | Classification |
| Q24 | - |  |  | SI | 0 - 51 |
| Q25 | - |  |  | SI | Higher scores correspond to a higher level of disa... |
| Q26 | - |  |  | SI | 0 - 51: Higher scores correspond to a higher level... |
| Q27 | - |  |  | SI | The Egen Klassifikation Scale version 2 (EK2) is a... |
| Q28 | - |  |  | SI | It examined activities and abilities such as trans... |
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
| REQNAV_Code | varchar |  |  | NO | Code |
| REQNAV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REQNAV_CreatedDate | date |  |  | SI | Created Date |
| REQNAV_CreatedTime | time |  |  | SI | Created Time |
| REQNAV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REQNAV_DateFrom | date |  |  | SI | DateFrom |
| REQNAV_DateTo | date |  |  | SI | DateTo |
| REQNAV_Desc | varchar |  |  | NO | Description |
| REQNAV_Owner | varchar |  |  | SI | Owner |
| REQNAV_UpdatedDate | date |  |  | SI | Updated Date |
| REQNAV_UpdatedTime | time |  |  | SI | Updated Time |
| REQNAV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*