# SQLUser.PAC_LacerationDegree

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEGLAC_RowId | bigint | PK |  | NO | - |
| ChildQ37DR | - |  |  | SI | Child Reference: Reassessment / Follow-up |
| DEGLAC_Code | varchar |  |  | NO | Code |
| DEGLAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEGLAC_CreatedDate | date |  |  | SI | Created Date |
| DEGLAC_CreatedTime | time |  |  | SI | Created Time |
| DEGLAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEGLAC_DateFrom | date |  |  | SI | Date From |
| DEGLAC_DateTo | date |  |  | SI | Date To |
| DEGLAC_Desc | varchar |  |  | NO | Description |
| DEGLAC_Owner | varchar |  |  | SI | Owner |
| DEGLAC_UpdatedDate | date |  |  | SI | Updated Date |
| DEGLAC_UpdatedTime | time |  |  | SI | Updated Time |
| DEGLAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q10 | - |  |  | SI | Poor appetite |
| Q11 | - |  |  | SI | Crying |
| Q12 | - |  |  | SI | Lack of sleep |
| Q13 | - |  |  | SI | Aggressive |
| Q14 | - |  |  | SI | Physical / Mental disability |
| Q15 | - |  |  | SI | Compliance of treatment |
| Q16 | - |  |  | SI | Patient and family grieving |
| Q17 | - |  |  | SI | Other/s (specify) |
| Q18 | - |  |  | SI | History of abuse / neglect |
| Q19 | - |  |  | SI | Patient needs spiritual / Cultural assessment |
| Q2 | - |  |  | SI | Legal responsibility for the patient |
| Q20 | - |  |  | SI | Patient needs economic assistance |
| Q21 | - |  |  | SI | Patient needs psychosocial assessment |
| Q22 | - |  |  | SI | Multidisplinary team |
| Q22A | - |  |  | SI | Attended Meetings |
| Q23 | - |  |  | SI | Multidisplinary team meeting date |
| Q24 | - |  |  | SI | Multidisplinary team meeting note |
| Q25 | - |  |  | SI | Patient / Family meeting |
| Q26 | - |  |  | SI | Patient / Family meeting date |
| Q27 | - |  |  | SI | Patient / Family meeting notes |
| Q28 | - |  |  | SI | Discharge Planning |
| Q29 | - |  |  | SI | Discharge planning |
| Q3 | - |  |  | SI | Specify name |
| Q30 | - |  |  | SI | Others (specify) |
| Q31 | - |  |  | SI | Recommendations |
| Q32 | - |  |  | SI | Medical social worker's name |
| Q33 | - |  |  | SI | Medical social worker's id |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Time |
| Q36 | - |  |  | SI | Signature |
| Q36UDt | - |  |  | SI | Signature Last Updated Date |
| Q36UTm | - |  |  | SI | Signature Last Updated Time |
| Q39 | - |  |  | SI | Date |
| Q4 | - |  |  | SI | Specify relationship |
| Q40 | - |  |  | SI | Time |
| Q5 | - |  |  | SI | Uncooperative |
| Q5A | - |  |  | SI | Social Worker Screening |
| Q6 | - |  |  | SI | Despair |
| Q7 | - |  |  | SI | Depressed |
| Q8 | - |  |  | SI | Low morale |
| Q9 | - |  |  | SI | Agitated |
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