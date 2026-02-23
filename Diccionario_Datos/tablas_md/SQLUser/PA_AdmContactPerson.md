# SQLUser.PA_AdmContactPerson

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONT_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| CONT_Address2 | varchar |  |  | SI | Address2 |
| CONT_CTRLT_DR | bigint |  | FK | SI | Des Ref CTRLT |
| CONT_CarerContribution | varchar |  |  | SI | Carer Contribution |
| CONT_Childsub | double |  |  | NO | Childsub |
| CONT_ConsentToShareInfo | varchar |  |  | SI | Consent To Share Info |
| CONT_ContType_DR | bigint |  | FK | SI | Des Ref ContType |
| CONT_Country_DR | bigint |  | FK | SI | Des Ref CTCountry |
| CONT_DateFrom | date |  |  | SI | Date From |
| CONT_DateTo | date |  |  | SI | Date To |
| CONT_Deceased | varchar |  |  | SI | Deceased |
| CONT_Discharged | varchar |  |  | SI | Discharged |
| CONT_DocumentNumber | varchar |  |  | SI | DocumentNumber |
| CONT_HealthFundNo | varchar |  |  | SI | HealthFundNo |
| CONT_LetterComment | varchar |  |  | SI | Letter Comment |
| CONT_Marital_DR | bigint |  | FK | SI | Des Ref CTMarital |
| CONT_Nation_DR | bigint |  | FK | SI | Des Ref CTNation |
| CONT_NonConsentReason | varchar |  |  | SI | Non Consent Reason |
| CONT_NonGovOrg_DR | bigint |  | FK | SI | Des Ref NonGovOrg |
| CONT_Occupation_DR | bigint |  | FK | SI | Des Ref CTOccupation |
| CONT_PassportNumber | varchar |  |  | SI | PassportNumber |
| CONT_PensionType_DR | bigint |  | FK | SI | Des Ref PACPensionType |
| CONT_Person_DR | bigint |  | FK | SI | Des Ref Person |
| CONT_RowId | varchar |  |  | NO | - |
| CONT_SecondPhone | varchar |  |  | SI | SecondPhone |
| CONT_UpdateDate | date |  |  | SI | UpdateDate |
| CONT_UpdateTime | time |  |  | SI | UpdateTime |
| CONT_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| CONT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bundle Compliance Percentage |
| Q04 | - |  |  | SI | % |
| Q05 | - |  |  | SI | Surgical Procedure |
| Q06 | - |  |  | SI | Booked Procedure |
| Q07 | - |  |  | SI | Actual procedure |
| Q08 | - |  |  | SI | Date of procedure |
| Q09 | - |  |  | SI | Name of surgeon |
| Q10 | - |  |  | SI | Theatre N°: |
| Q11 | - |  |  | SI | Time of procedure: from |
| Q12 | - |  |  | SI | To |
| Q13 | - |  |  | SI | For high-risk orthopedic or cardiothoracic interve... |
| Q14 | - |  |  | SI | Bath taken night prior to surgery or on the day of... |
| Q15 | - |  |  | SI | Trichotomy not practiced |
| Q16 | - |  |  | SI | If performed trichotomy: used the electric razor (... |
| Q17 | - |  |  | SI | If performed trichotomy: performed shortly before ... |
| Q18 | - |  |  | SI | Antibiotic prophylaxis within 30-60 minutes prior ... |
| Q19 | - |  |  | SI | Single dose antibiotic prophylaxis, except in prot... |
| Q20 | - |  |  | SI | Skin antisepsis with 2% chlorhexidine in 70% alcoh... |
| Q21 | - |  |  | SI | Peri-operative normothermia (> 36 ° C) (possibly a... |
| Q22 | - |  |  | SI | Peri-operative High blood glucose test result |
| Q23 | - |  |  | SI | Sterile dressing not handled / removed for the fir... |
| Q24 | - |  |  | SI | Comments |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | 0 - 100: |
| Q28 | - |  |  | SI | Higher percetage indicates higher compliance |
| Q29 | - |  |  | SI | This questionnaire is used in the clinical practic... |
| Q30 | - |  |  | SI | 0 - 100: Higher percetage indicates higher complia... |
| Q31 | - |  |  | SI | Aseptic technique for wound dressing |
| Q32 | - |  |  | SI | If performed trichotomy: this has been done outsid... |
| Q33 | - |  |  | SI | If performed trichotomy: this has been done outsid... |
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