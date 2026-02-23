# SQLUser.PAC_CareProfAssocType

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAREPAT_RowId | bigint | PK |  | NO | - |
| CAREPAT_Code | varchar |  |  | NO | Code |
| CAREPAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CAREPAT_CreatedDate | date |  |  | SI | Created Date |
| CAREPAT_CreatedTime | time |  |  | SI | Created Time |
| CAREPAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CAREPAT_DateFrom | date |  |  | SI | Date From |
| CAREPAT_DateTo | date |  |  | SI | Date To |
| CAREPAT_Desc | varchar |  |  | NO | Description |
| CAREPAT_Owner | varchar |  |  | SI | Owner |
| CAREPAT_UpdatedDate | date |  |  | SI | Updated Date |
| CAREPAT_UpdatedTime | time |  |  | SI | Updated Time |
| CAREPAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | 8. I feel inferior to others who dont have a menta... |
| Q11 | - |  |  | SI | 9. I dont socialize as much as I used to because m... |
| Q12 | - |  |  | SI | 10. People with mental illness cannot live a good,... |
| Q13 | - |  |  | SI | 11. I dont talk about myself much because I dont w... |
| Q14 | - |  |  | SI | 12. Negative stereotypes about mental illness keep... |
| Q15 | - |  |  | SI | 13. Being around people who dont have a mental ill... |
| Q16 | - |  |  | SI | 14. I feel comfortable being seen in public with a... |
| Q17 | - |  |  | SI | 15. People often patronize me, or treat me like a ... |
| Q18 | - |  |  | SI | 16. I am disappointed in myself for having a menta... |
| Q19 | - |  |  | SI | 17. Having a mental illness has spoiled my life |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | 18. People can tell that I have a mental illness b... |
| Q21 | - |  |  | SI | 19. Because I have a mental illness, I need others... |
| Q22 | - |  |  | SI | 20. I stay away from social situations in order to... |
| Q23 | - |  |  | SI | 21. People without mental illness could not possib... |
| Q24 | - |  |  | SI | 22. People ignore me or take me less seriously jus... |
| Q25 | - |  |  | SI | 23. I cant contribute anything to society because ... |
| Q26 | - |  |  | SI | 24. Living with mental illness has made me a tough... |
| Q27 | - |  |  | SI | 25. Nobody would be interested in getting close to... |
| Q28 | - |  |  | SI | 26. In general, I am able to live my life the way ... |
| Q29 | - |  |  | SI | 27. I can have a good, fulfilling life, despite my... |
| Q3 | - |  |  | SI | 1. I feel out of place in the world because I have... |
| Q30 | - |  |  | SI | 28. Others think that I cant achieve much in life ... |
| Q31 | - |  |  | SI | 29. Stereotypes about the mentally ill apply to me |
| Q32 | - |  |  | SI | Score |
| Q33 | - |  |  | SI | Classification |
| Q34 | - |  |  | SI | 29 - 116 |
| Q35 | - |  |  | SI | A high total score on the ISMI scale indicates mor... |
| Q36 | - |  |  | SI | 29 - 116: A high total score on the ISMI scale ind... |
| Q37 | - |  |  | SI | The IMSI is a 29-item measure with five subscales:... |
| Q4 | - |  |  | SI | 2. Mentally ill people tend to be violent. |
| Q5 | - |  |  | SI | 3. People discriminate against me because I have a... |
| Q6 | - |  |  | SI | 4. I avoid getting close to people who dont have a... |
| Q7 | - |  |  | SI | 5. I am embarrassed or ashamed that I have a menta... |
| Q8 | - |  |  | SI | 6. Mentally ill people shouldnt get married |
| Q9 | - |  |  | SI | 7. People with mental illness make important contr... |
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