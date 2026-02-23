# SQLUser.PAC_ConfidentialityCode

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONFCODE_RowId | bigint | PK |  | NO | - |
| CONFCODE_Code | varchar |  |  | NO | Code |
| CONFCODE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONFCODE_CreatedDate | date |  |  | SI | Created Date |
| CONFCODE_CreatedTime | time |  |  | SI | Created Time |
| CONFCODE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONFCODE_DateFrom | date |  |  | SI | Date From |
| CONFCODE_DateTo | date |  |  | SI | Date To |
| CONFCODE_Desc | varchar |  |  | NO | Description |
| CONFCODE_Owner | varchar |  |  | SI | Owner |
| CONFCODE_SubRegion_DR | bigint |  | FK | SI | Subregion |
| CONFCODE_UpdatedDate | date |  |  | SI | Updated Date |
| CONFCODE_UpdatedTime | time |  |  | SI | Updated Time |
| CONFCODE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Discussed with referring physician / MDT	 |
| Q03 | - |  |  | SI | Imaging reviewed	 |
| Q04 | - |  |  | SI | Relevant medical history	 |
| Q05 | - |  |  | SI | Informed consent	 |
| Q06 | - |  |  | SI | Contrast-Induced Nephropathy (CIN) prophylaxis	 |
| Q07 | - |  |  | SI | Specific tools present / ordered	 |
| Q08 | - |  |  | SI | Fasting order given	 |
| Q09 | - |  |  | SI | Relevant lab tests ordered	 |
| Q10 | - |  |  | SI | Anesthesiology necessary	 |
| Q11 | - |  |  | SI | Anticoagulant medication stopped	 |
| Q12 | - |  |  | SI | Contrast allergy prophylaxis necessary	 |
| Q13 | - |  |  | SI | Name	 |
| Q14 | - |  |  | SI | Role |
| Q15 | - |  |  | SI | Signature |
| Q15UDt | - |  |  | SI | Signature Last Updated Date |
| Q15UTm | - |  |  | SI | Signature Last Updated Time |
| Q16 | - |  |  | SI | All team members introduced	 |
| Q17 | - |  |  | SI | All records with patient	 |
| Q18 | - |  |  | SI | Correct patient / Site	 |
| Q19 | - |  |  | SI | Patient fasting	 |
| Q20 | - |  |  | SI | IV access	 |
| Q21 | - |  |  | SI | Monitoring equipment attached	 |
| Q22 | - |  |  | SI | Coagulation screen / Lab tests checked	 |
| Q23 | - |  |  | SI | Allergies and/or prophylaxis checked	 |
| Q24 | - |  |  | SI | Antibiotics / other drugs administered	 |
| Q25 | - |  |  | SI | Consent / complications discussed	 |
| Q26 | - |  |  | SI | Name |
| Q27 | - |  |  | SI | Role |
| Q28 | - |  |  | SI | Signature |
| Q28UDt | - |  |  | SI | Signature Last Updated Date |
| Q28UTm | - |  |  | SI | Signature Last Updated Time |
| Q29 | - |  |  | SI | Post-op note written	 |
| Q30 | - |  |  | SI | Vital signs normal during the procedure	 |
| Q31 | - |  |  | SI | Medication and CM recorded	 |
| Q32 | - |  |  | SI | Lab tests ordered	 |
| Q33 | - |  |  | SI | All samples labeled and sent to the lab	 |
| Q34 | - |  |  | SI | Procedure results discussed with the patient	 |
| Q35 | - |  |  | SI | Post-discharge instructions given	 |
| Q36 | - |  |  | SI | Follow up tests / imaging orders	 |
| Q37 | - |  |  | SI | Follow up OPD appointment made	 |
| Q38 | - |  |  | SI | Procedure results communicated to the referrer	 |
| Q39 | - |  |  | SI | Name |
| Q40 | - |  |  | SI | Role |
| Q41 | - |  |  | SI | Signature	 |
| Q41UDt | - |  |  | SI | Signature	 Last Updated Date |
| Q41UTm | - |  |  | SI | Signature	 Last Updated Time |
| Q42 | - |  |  | SI | Post-interventional (ICU) bed required	 |
| Q43 | - |  |  | SI | Correct laterality |
| Q44 | - |  |  | SI | Relevant medications ordered / in stock |
| Q45 | - |  |  | SI | Comment |
| Q46 | - |  |  | SI | Comment |
| Q47 | - |  |  | SI | Comment |
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