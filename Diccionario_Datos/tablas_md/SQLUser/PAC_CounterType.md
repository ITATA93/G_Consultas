# SQLUser.PAC_CounterType

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CNT_RowId | bigint | PK |  | NO | - |
| CNT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CNT_Counter | double |  |  | SI | Counter |
| CNT_CreatedDate | date |  |  | SI | Created Date |
| CNT_CreatedTime | time |  |  | SI | Created Time |
| CNT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CNT_Desc | varchar |  |  | NO | Description |
| CNT_Length | double |  |  | NO | Length |
| CNT_Owner | varchar |  |  | SI | Owner |
| CNT_Prefix | varchar |  |  | SI | Prefix |
| CNT_Suffix | varchar |  |  | SI | Suffix |
| CNT_UpdatedDate | date |  |  | SI | Updated Date |
| CNT_UpdatedTime | time |  |  | SI | Updated Time |
| CNT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Patient's Clinical Information |
| Q02 | - |  |  | SI | Duration of Infertility (years) |
| Q03 | - |  |  | SI | Parity |
| Q03ObsDR | - |  |  | SI | Parity DR |
| Q04 | - |  |  | SI | Number of Living Child |
| Q04ObsDR | - |  |  | SI | Number of Living Child DR |
| Q05 | - |  |  | SI | Number of Abortions |
| Q07 | - |  |  | SI | Partner's Laboratory Results |
| Q08 | - |  |  | SI | Partner's Hormones (Cycle Day 2-4) |
| Q09 | - |  |  | SI | Follicle-Stimulating Hormone (FSH) |
| Q09ObsDR | - |  |  | SI | Follicle-Stimulating Hormone (FSH) DR |
| Q10 | - |  |  | SI | Luteinizing Hormone (LH) |
| Q10ObsDR | - |  |  | SI | Luteinizing Hormone (LH) DR |
| Q11 | - |  |  | SI | Estradiol (E2) |
| Q11ObsDR | - |  |  | SI | Estradiol (E2) DR |
| Q12 | - |  |  | SI | Prolactin |
| Q12ObsDR | - |  |  | SI | Prolactin DR |
| Q13 | - |  |  | SI | Thyroid-Stimulating Hormone (TSH) |
| Q13ObsDR | - |  |  | SI | Thyroid-Stimulating Hormone (TSH) DR |
| Q14 | - |  |  | SI | Date of Hormone Results |
| Q14ObsDR | - |  |  | SI | Date of Hormone Results DR |
| Q15 | - |  |  | SI | Partner's Serology Results |
| Q16 | - |  |  | SI | Hepatitis B Surface Antigen |
| Q16ObsDR | - |  |  | SI | Hepatitis B Surface Antigen DR |
| Q17 | - |  |  | SI | Anti Hepatitis C Antibody |
| Q17ObsDR | - |  |  | SI | Anti Hepatitis C Antibody DR |
| Q18 | - |  |  | SI | Human Immunodeficiency Virus (HIV) |
| Q18ObsDR | - |  |  | SI | Human Immunodeficiency Virus (HIV) DR |
| Q19 | - |  |  | SI | Date of Serology |
| Q19ObsDR | - |  |  | SI | Date of Serology DR |
| Q20 | - |  |  | SI | Pap Smear |
| Q20ObsDR | - |  |  | SI | Pap Smear DR |
| Q21 | - |  |  | SI | Date of Pap Smear |
| Q21ObsDR | - |  |  | SI | Date of Pap Smear DR |
| Q22 | - |  |  | SI | Hysterosalpingogram (HSG) |
| Q22ObsDR | - |  |  | SI | Hysterosalpingogram (HSG) DR |
| Q23 | - |  |  | SI | Date of Hysterosalpingogram (HSG) |
| Q23ObsDR | - |  |  | SI | Date of Hysterosalpingogram (HSG) DR |
| Q24 | - |  |  | SI | Other Results |
| Q25 | - |  |  | SI | Partner's Demographics and Clinical Information |
| Q25A | - |  |  | SI | Partner's Demographic Information |
| Q25B | - |  |  | SI | Partner's Serology Results |
| Q26 | - |  |  | SI | Partner's Name |
| Q27 | - |  |  | SI | Partner's Nationality |
| Q28 | - |  |  | SI | Partner's Date of Birth |
| Q29 | - |  |  | SI | Partner's Medical Record Number |
| Q30 | - |  |  | SI | Partner's Hepatitis B Surface Antigen |
| Q31 | - |  |  | SI | Partner's Human Immunodeficiency Virus (HIV) |
| Q32 | - |  |  | SI | Partner's Anti Hepatitis C Antibody |
| Q33 | - |  |  | SI | Date of Partner's Serology |
| Q34 | - |  |  | SI | Partner's Semen Analysis |
| Q35 | - |  |  | SI | Volume (ml) |
| Q36 | - |  |  | SI | Count (million / ml) |
| Q37 | - |  |  | SI | Motility (%) |
| Q38 | - |  |  | SI | Morpholgy |
| Q39 | - |  |  | SI | Date of Semen Analysis |
| Q40 | - |  |  | SI | Other Results |
| Q41 | - |  |  | SI | Diagnosis Type |
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