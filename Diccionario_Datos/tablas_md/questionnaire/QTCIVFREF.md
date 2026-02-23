# questionnaire.QTCIVFREF

> In Vitro Fertilization (IVF) Referral

**Schema:** questionnaire
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* In Vitro Fertilization (IVF) Referral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Patient's Clinical Information |
| Q02 | numeric |  |  | SI | Duration of Infertility (years) |
| Q03 | varchar |  |  | SI | Parity |
| Q03ObsDR | varchar |  | FK | SI | Parity DR |
| Q04 | varchar |  |  | SI | Number of Living Child |
| Q04ObsDR | varchar |  | FK | SI | Number of Living Child DR |
| Q05 | numeric |  |  | SI | Number of Abortions |
| Q07 | varchar |  |  | SI | Partner's Laboratory Results |
| Q08 | varchar |  |  | SI | Partner's Hormones (Cycle Day 2-4) |
| Q09 | varchar |  |  | SI | Follicle-Stimulating Hormone (FSH) |
| Q09ObsDR | varchar |  | FK | SI | Follicle-Stimulating Hormone (FSH) DR |
| Q10 | varchar |  |  | SI | Luteinizing Hormone (LH) |
| Q10ObsDR | varchar |  | FK | SI | Luteinizing Hormone (LH) DR |
| Q11 | varchar |  |  | SI | Estradiol (E2) |
| Q11ObsDR | varchar |  | FK | SI | Estradiol (E2) DR |
| Q12 | varchar |  |  | SI | Prolactin |
| Q12ObsDR | varchar |  | FK | SI | Prolactin DR |
| Q13 | varchar |  |  | SI | Thyroid-Stimulating Hormone (TSH) |
| Q13ObsDR | varchar |  | FK | SI | Thyroid-Stimulating Hormone (TSH) DR |
| Q14 | varchar |  |  | SI | Date of Hormone Results |
| Q14ObsDR | varchar |  | FK | SI | Date of Hormone Results DR |
| Q15 | varchar |  |  | SI | Partner's Serology Results |
| Q16 | varchar |  |  | SI | Hepatitis B Surface Antigen |
| Q16ObsDR | varchar |  | FK | SI | Hepatitis B Surface Antigen DR |
| Q17 | varchar |  |  | SI | Anti Hepatitis C Antibody |
| Q17ObsDR | varchar |  | FK | SI | Anti Hepatitis C Antibody DR |
| Q18 | varchar |  |  | SI | Human Immunodeficiency Virus (HIV) |
| Q18ObsDR | varchar |  | FK | SI | Human Immunodeficiency Virus (HIV) DR |
| Q19 | varchar |  |  | SI | Date of Serology |
| Q19ObsDR | varchar |  | FK | SI | Date of Serology DR |
| Q20 | varchar |  |  | SI | Pap Smear |
| Q20ObsDR | varchar |  | FK | SI | Pap Smear DR |
| Q21 | varchar |  |  | SI | Date of Pap Smear |
| Q21ObsDR | varchar |  | FK | SI | Date of Pap Smear DR |
| Q22 | varchar |  |  | SI | Hysterosalpingogram (HSG) |
| Q22ObsDR | varchar |  | FK | SI | Hysterosalpingogram (HSG) DR |
| Q23 | varchar |  |  | SI | Date of Hysterosalpingogram (HSG) |
| Q23ObsDR | varchar |  | FK | SI | Date of Hysterosalpingogram (HSG) DR |
| Q24 | varchar |  |  | SI | Other Results |
| Q25 | varchar |  |  | SI | Partner's Demographics and Clinical Information |
| Q25A | varchar |  |  | SI | Partner's Demographic Information |
| Q25B | varchar |  |  | SI | Partner's Serology Results |
| Q26 | varchar |  |  | SI | Partner's Name |
| Q27 | varchar |  |  | SI | Partner's Nationality |
| Q28 | date |  |  | SI | Partner's Date of Birth |
| Q29 | numeric |  |  | SI | Partner's Medical Record Number |
| Q30 | varchar |  |  | SI | Partner's Hepatitis B Surface Antigen |
| Q31 | varchar |  |  | SI | Partner's Human Immunodeficiency Virus (HIV) |
| Q32 | varchar |  |  | SI | Partner's Anti Hepatitis C Antibody |
| Q33 | date |  |  | SI | Date of Partner's Serology |
| Q34 | varchar |  |  | SI | Partner's Semen Analysis |
| Q35 | numeric |  |  | SI | Volume (ml) |
| Q36 | numeric |  |  | SI | Count (million / ml) |
| Q37 | numeric |  |  | SI | Motility (%) |
| Q38 | varchar |  |  | SI | Morpholgy |
| Q39 | date |  |  | SI | Date of Semen Analysis |
| Q40 | varchar |  |  | SI | Other Results |
| Q41 | varchar |  |  | SI | Diagnosis Type |
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