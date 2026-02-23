# SQLUser.CT_HospitalDRGBaseRate

**Schema:** SQLUser
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGBR_ParRef | bigint | PK |  | NO | CT_Hospital Parent Reference |
| DRGBR_BaseRate | double |  |  | SI | Base Rate |
| DRGBR_Childsub | double |  |  | NO | Childsub |
| DRGBR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGBR_CreatedDate | date |  |  | SI | Created Date |
| DRGBR_CreatedTime | time |  |  | SI | Created Time |
| DRGBR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGBR_DRGCostTariff_DR | bigint |  | FK | SI | DRG Cost Tariff, Des Ref ARCTariff |
| DRGBR_DRGGap | double |  |  | SI | DRG Gap |
| DRGBR_DRGMargin | double |  |  | SI | DRG Margin |
| DRGBR_DateFrom | date |  |  | SI | Date From |
| DRGBR_DateTo | date |  |  | SI | Date To |
| DRGBR_LTCARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGBR_OutlierARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGBR_Rowid | varchar |  |  | NO | - |
| DRGBR_SplitPayorPerc | double |  |  | SI | Split Payor Percentage |
| DRGBR_UpdatedDate | date |  |  | SI | Updated Date |
| DRGBR_UpdatedTime | time |  |  | SI | Updated Time |
| DRGBR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | A record of my future health care wishes |
| Q02 | - |  |  | SI | I declare that: |
| Q03 | - |  |  | SI | 1.  My current health problems include |
| Q04 | - |  |  | SI | If you have some specific health problems you may ... |
| Q05 | - |  |  | SI | Refer to Advance Care Plan Information Sheet. |
| Q06 | - |  |  | SI | 2.  This document has been explained to me and I u... |
| Q07 | - |  |  | SI | It will only be used if I am unable to make decisi... |
| Q08 | - |  |  | SI | 3.  I understand that it is important to discuss m... |
| Q09 | - |  |  | SI | 4.  I request that my wishes, and the beliefs and ... |
| Q10 | - |  |  | SI | I have written on page 2 of this form the things t... |
| Q11 | - |  |  | SI | 5.  I understand that doctors will only provide tr... |
| Q12 | - |  |  | SI | I also understand that irrespective of any decisio... |
| Q13 | - |  |  | SI | CPR |
| Q14 | - |  |  | SI | Life Prolonging Treatments |
| Q15 | - |  |  | SI | To me, a reasonable outcome means: |
| Q16 | - |  |  | SI | Decisions regarding CPR will be made by: |
| Q17 | - |  |  | SI | I choose to delegate decisions regarding CPR and l... |
| Q18 | - |  |  | SI | Medical Enduring Power of Attorney Name and Contac... |
| Q19 | - |  |  | SI | Name and relationship |
| Q20 | - |  |  | SI | The things that I most value in my life are  (e.g.... |
| Q21 | - |  |  | SI | Future situations that I would find unacceptable i... |
| Q22 | - |  |  | SI | Specific treatments that I would NOT want consider... |
| Q23 | - |  |  | SI | Other things that I would like known, which may he... |
| Q24 | - |  |  | SI | I ask that, if possible, my Medical Enduring Power... |
| Q25 | - |  |  | SI | If I am nearing death I would like the following  ... |
| Q26 | - |  |  | SI | Refusal of Treatment Certificate (RTC) exists |
| Q27 | - |  |  | SI | This is a true record of my wishes on this date |
| Q28 | - |  |  | SI | Signature provided by |
| Q29 | - |  |  | SI | Patient |
| Q29UDt | - |  |  | SI | Patient Last Updated Date |
| Q29UTm | - |  |  | SI | Patient Last Updated Time |
| Q30 | - |  |  | SI | If the patient is unable to sign but has indicated... |
| Q30UDt | - |  |  | SI | If the patient is unable to sign but has indicated... |
| Q30UTm | - |  |  | SI | If the patient is unable to sign but has indicated... |
| Q31 | - |  |  | SI | Name of witness |
| Q32 | - |  |  | SI | I believe that the person is competent and underst... |
| Q32UDt | - |  |  | SI | I believe that the person is competent and underst... |
| Q32UTm | - |  |  | SI | I believe that the person is competent and underst... |
| Q33 | - |  |  | SI | The contents of this Statement of Choices have als... |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Name |
| Q36 | - |  |  | SI | Relationship |
| Q37 | - |  |  | SI | Signature Person 1 |
| Q37UDt | - |  |  | SI | Signature Person 1 Last Updated Date |
| Q37UTm | - |  |  | SI | Signature Person 1 Last Updated Time |
| Q38 | - |  |  | SI | Date |
| Q39 | - |  |  | SI | Name |
| Q40 | - |  |  | SI | Relationship |
| Q41 | - |  |  | SI | Signature Person 2 |
| Q41UDt | - |  |  | SI | Signature Person 2 Last Updated Date |
| Q41UTm | - |  |  | SI | Signature Person 2 Last Updated Time |
| Q42 | - |  |  | SI | Care Provider |
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