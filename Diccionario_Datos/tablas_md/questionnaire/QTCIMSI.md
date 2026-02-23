# questionnaire.QTCIMSI

> Internalized Stigma of Mental Illness Inventory (ISMI)

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Internalized Stigma of Mental Illness Inventory (ISMI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | 8. I feel inferior to others who dont have a menta... |
| Q11 | varchar |  |  | SI | 9. I dont socialize as much as I used to because m... |
| Q12 | varchar |  |  | SI | 10. People with mental illness cannot live a good,... |
| Q13 | varchar |  |  | SI | 11. I dont talk about myself much because I dont w... |
| Q14 | varchar |  |  | SI | 12. Negative stereotypes about mental illness keep... |
| Q15 | varchar |  |  | SI | 13. Being around people who dont have a mental ill... |
| Q16 | varchar |  |  | SI | 14. I feel comfortable being seen in public with a... |
| Q17 | varchar |  |  | SI | 15. People often patronize me, or treat me like a ... |
| Q18 | varchar |  |  | SI | 16. I am disappointed in myself for having a menta... |
| Q19 | varchar |  |  | SI | 17. Having a mental illness has spoiled my life |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | 18. People can tell that I have a mental illness b... |
| Q21 | varchar |  |  | SI | 19. Because I have a mental illness, I need others... |
| Q22 | varchar |  |  | SI | 20. I stay away from social situations in order to... |
| Q23 | varchar |  |  | SI | 21. People without mental illness could not possib... |
| Q24 | varchar |  |  | SI | 22. People ignore me or take me less seriously jus... |
| Q25 | varchar |  |  | SI | 23. I cant contribute anything to society because ... |
| Q26 | varchar |  |  | SI | 24. Living with mental illness has made me a tough... |
| Q27 | varchar |  |  | SI | 25. Nobody would be interested in getting close to... |
| Q28 | varchar |  |  | SI | 26. In general, I am able to live my life the way ... |
| Q29 | varchar |  |  | SI | 27. I can have a good, fulfilling life, despite my... |
| Q3 | varchar |  |  | SI | 1. I feel out of place in the world because I have... |
| Q30 | varchar |  |  | SI | 28. Others think that I cant achieve much in life ... |
| Q31 | varchar |  |  | SI | 29. Stereotypes about the mentally ill apply to me |
| Q32 | varchar |  |  | SI | Score |
| Q33 | varchar |  |  | SI | Classification |
| Q34 | varchar |  |  | SI | 29 - 116 |
| Q35 | varchar |  |  | SI | A high total score on the ISMI scale indicates mor... |
| Q36 | varchar |  |  | SI | 29 - 116: A high total score on the ISMI scale ind... |
| Q37 | varchar |  |  | SI | The IMSI is a 29-item measure with five subscales:... |
| Q4 | varchar |  |  | SI | 2. Mentally ill people tend to be violent. |
| Q5 | varchar |  |  | SI | 3. People discriminate against me because I have a... |
| Q6 | varchar |  |  | SI | 4. I avoid getting close to people who dont have a... |
| Q7 | varchar |  |  | SI | 5. I am embarrassed or ashamed that I have a menta... |
| Q8 | varchar |  |  | SI | 6. Mentally ill people shouldnt get married |
| Q9 | varchar |  |  | SI | 7. People with mental illness make important contr... |
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